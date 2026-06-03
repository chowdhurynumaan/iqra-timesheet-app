// Service Worker for Attendance Analytics Pro
// Enables offline functionality and caching

const CACHE_NAME = 'attendance-pro-v2';
const URLS_TO_CACHE = [
  './',
  './index.html',
  './dashboard.html',
  'https://cdn.jsdelivr.net/npm/chart.js@4.4.1',
  'https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.2/papaparse.min.js',
  'https://cdn.tailwindcss.com',
  'https://unpkg.com/lucide@0.263.1',
  'https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js'
];

// Install event - cache resources
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        return cache.addAll(URLS_TO_CACHE).catch(() => {
          // Continue even if some resources fail to cache
          return Promise.resolve();
        });
      })
      .catch(() => {
        // Service worker installation continues even if caching fails
        return Promise.resolve();
      })
  );
  self.skipWaiting();
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
  // Skip non-GET requests
  if (event.request.method !== 'GET') return;

  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // Return cached response if available
        if (response) {
          return response;
        }

        // Try to fetch from network
        return fetch(event.request)
          .then((response) => {
            // Cache successful network responses
            if (!response || response.status !== 200 || response.type === 'error') {
              return response;
            }

            // Clone the response to cache
            const responseToCache = response.clone();
            caches.open(CACHE_NAME)
              .then((cache) => {
                cache.put(event.request, responseToCache);
              });

            return response;
          })
          .catch(() => {
            // Fallback for offline - serve cached version or offline page
            return caches.match('./dashboard.html');
          });
      })
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((cacheNames) => {
        return Promise.all(
          cacheNames.map((cacheName) => {
            if (cacheName !== CACHE_NAME) {
              return caches.delete(cacheName);
            }
          })
        );
      })
  );
  self.clients.claim();
});

// Handle messages from clients
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});
