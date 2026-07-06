# Cycle 8 — Force auto-régulée

Application de musculation (PWA) : un programme de 8 semaines, 4 séances/semaine
(haut/bas), auto-régulé au RPE. Suivi des séances, charges qui s'adaptent au
ressenti, records, journal et test des maxs en fin de bloc. **100% local** : tes
données restent sur ton appareil (localStorage), aucune connexion requise après
le premier chargement.

## Fichiers

- `index.html` — l'application (autonome).
- `manifest.webmanifest` — métadonnées PWA (nom, couleurs, icônes).
- `sw.js` — service worker : met l'app en cache pour un usage hors-ligne.
- `icons/` — icônes de l'app (dont `icon-180.png` pour l'écran d'accueil iOS).

## Installer sur l'écran d'accueil d'un iPhone (iOS)

1. Ouvrir l'URL de l'app **dans Safari** (pas Chrome — sur iOS seul Safari
   sait ajouter une vraie icône à l'écran d'accueil).
2. Toucher le bouton **Partager** (le carré avec la flèche vers le haut).
3. Choisir **« Sur l'écran d'accueil »**.
4. Valider avec **Ajouter**. L'icône « Cycle 8 » apparaît comme une vraie app,
   en plein écran.

## Publier l'app (GitHub Pages)

Dans le dépôt GitHub : **Settings → Pages**, source **Deploy from a branch**,
choisir la branche puis le dossier **/(root)**, enregistrer. L'URL publique est
de la forme `https://<utilisateur>.github.io/<dépôt>/`.
