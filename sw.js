/* Service worker Cycle 8.
   Stratégie "réseau d'abord" : quand tu as du réseau, tu obtiens TOUJOURS la
   dernière version de l'app (et on met à jour le cache au passage) ; hors-ligne,
   on sert la dernière version mise en cache. Les domaines externes (ex. YouTube)
   ne sont pas interceptés. */
const CACHE = 'cycle8-v2';
const ASSETS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon-180.png',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-512-maskable.png',
  './icons/icon-32.png'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return; // laisse passer les ressources externes

  // Réseau d'abord : on récupère la version à jour et on rafraîchit le cache ;
  // en cas d'échec (hors-ligne), on retombe sur le cache, puis sur index.html.
  e.respondWith(
    fetch(req).then(res => {
      const copy = res.clone();
      caches.open(CACHE).then(c => c.put(req, copy));
      return res;
    }).catch(() => caches.match(req).then(c => c || caches.match('./index.html')))
  );
});
