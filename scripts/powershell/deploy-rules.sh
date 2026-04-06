#!/bin/bash
# Script to deploy Firestore Security Rules to Firebase Project
# 
# Prerequisites:
#   - Firebase CLI installed: npm install -g firebase-tools
#   - Logged into Firebase: firebase login
#   - Project initialized: firebase init firestore

echo "================================"
echo "Firebase Rules Deployment Script"
echo "================================"
echo ""

# Check if firebase CLI is installed
if ! command -v firebase &> /dev/null; then
    echo "❌ Firebase CLI not found. Please install it:"
    echo "   npm install -g firebase-tools"
    exit 1
fi

# Check if user is logged in
if ! firebase projects:list &> /dev/null; then
    echo "❌ Not logged into Firebase. Please run:"
    echo "   firebase login"
    exit 1
fi

# List available projects
echo "📋 Available Firebase Projects:"
firebase projects:list
echo ""

# Deploy rules
echo "🚀 Deploying Firestore Security Rules..."
firebase deploy --only firestore:rules --project apps-e1163

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Rules deployed successfully!"
    echo ""
    echo "🔍 Verify deployment:"
    echo "   Go to Firebase Console → Firestore → Rules"
    echo "   Or run: firebase firestore:indexes --project apps-e1163"
else
    echo ""
    echo "❌ Deployment failed. Check the error messages above."
    exit 1
fi
