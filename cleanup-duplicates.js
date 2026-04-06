#!/usr/bin/env node

/**
 * Firebase Duplicate Employee Cleanup Script
 * 
 * This script removes duplicate employee records from Firestore
 * Keeps the first occurrence of each employee per month, deletes the rest
 * 
 * Usage:
 *   1. Download service account key from Firebase Console
 *   2. Save it as 'serviceAccountKey.json' in this directory
 *   3. Run: node cleanup-duplicates.js
 */

const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

// Path to service account key
const serviceAccountPath = path.join(__dirname, 'serviceAccountKey.json');

// Check if service account key exists
if (!fs.existsSync(serviceAccountPath)) {
  console.error(`\n❌ ERROR: Service account key not found!`);
  console.error(`\n📋 To get your service account key:`);
  console.error(`   1. Go to: https://console.firebase.google.com`);
  console.error(`   2. Select project: "apps-e1163"`);
  console.error(`   3. Click ⚙️ Settings (top left)`);
  console.error(`   4. Go to "Service Accounts" tab`);
  console.error(`   5. Click "Generate New Private Key"`);
  console.error(`   6. Save the downloaded JSON file as "serviceAccountKey.json"`);
  console.error(`   7. Place it in: ${__dirname}`);
  console.error(`\n⚠️  IMPORTANT: Keep this file secret! Add to .gitignore after downloading.\n`);
  process.exit(1);
}

const serviceAccount = require(serviceAccountPath);

// Initialize Firebase Admin
try {
  admin.initializeApp({
    credential: admin.credential.cert(serviceAccount)
  });
  console.log('✅ Firebase Admin initialized\n');
} catch (error) {
  console.error('❌ Failed to initialize Firebase Admin:', error.message);
  process.exit(1);
}

const db = admin.firestore();

async function cleanupDuplicates() {
  try {
    console.log('🔍 Scanning for duplicate employee records...\n');

    // Get all documents from employees collection
    const snapshot = await db.collectionGroup('employees').get();
    
    if (snapshot.empty) {
      console.log('ℹ️  No employee records found in database');
      process.exit(0);
    }

    console.log(`📊 Found ${snapshot.size} total employee records\n`);

    // Group by employee ID and month
    const empsByIdMonth = {};
    const documents = [];

    snapshot.forEach(doc => {
      const data = doc.data();
      const key = `${data.id}_${data.monthId || 'unknown'}`;
      
      if (!empsByIdMonth[key]) {
        empsByIdMonth[key] = [];
      }

      documents.push({
        docId: doc.ref.path,
        id: data.id,
        name: data.name,
        monthId: data.monthId,
        created: data.lastUpdated || data.timestamp || 'unknown'
      });

      empsByIdMonth[key].push({
        docId: doc.ref.path,
        data: data,
        created: data.lastUpdated || data.timestamp
      });
    });

    // Find duplicates
    const duplicates = [];
    let totalDuplicates = 0;

    for (const [key, docs] of Object.entries(empsByIdMonth)) {
      if (docs.length > 1) {
        console.log(`⚠️  Found ${docs.length} copies of: ${docs[0].data.name} (ID: ${docs[0].data.id}, Month: ${docs[0].data.monthId})`);
        
        // Sort by creation date to keep the oldest
        const sorted = docs.sort((a, b) => {
          const aTime = new Date(a.created).getTime();
          const bTime = new Date(b.created).getTime();
          return aTime - bTime;
        });

        // Keep first, mark rest for deletion
        for (let i = 1; i < sorted.length; i++) {
          console.log(`   🗑️  Will delete: ${sorted[i].docId}`);
          duplicates.push(sorted[i].docId);
          totalDuplicates++;
        }
        console.log('');
      }
    }

    if (duplicates.length === 0) {
      console.log('✅ No duplicates found! Database is clean.\n');
      process.exit(0);
    }

    // Ask for confirmation
    console.log(`\n📋 Summary:`);
    console.log(`   Total records: ${documents.length}`);
    console.log(`   Duplicates found: ${totalDuplicates}`);
    console.log(`   Will delete: ${duplicates.length} documents\n`);

    // Delete duplicates
    console.log('🗑️  Deleting duplicate documents...\n');
    let deleted = 0;
    let failed = 0;

    for (const docPath of duplicates) {
      try {
        // Parse the document path and delete
        const docRef = db.doc(docPath);
        await docRef.delete();
        console.log(`   ✅ Deleted: ${docPath}`);
        deleted++;
      } catch (error) {
        console.error(`   ❌ Failed to delete ${docPath}: ${error.message}`);
        failed++;
      }
    }

    console.log(`\n✅ Cleanup complete!`);
    console.log(`   Successfully deleted: ${deleted} documents`);
    if (failed > 0) {
      console.log(`   Failed: ${failed} documents`);
    }
    console.log('');

    process.exit(0);
  } catch (error) {
    console.error('❌ Error during cleanup:', error.message);
    console.error('\nStack trace:', error);
    process.exit(1);
  }
}

// Run cleanup
cleanupDuplicates();
