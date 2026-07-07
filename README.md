# BENCH+ — Spécialisation Développé Couché

Application de musculation (PWA) : un programme de **6 semaines, 4 séances/semaine**
centré sur le développé couché (séances lourd / volume / technique + une séance
deadlift pour le bas du corps). Auto-régulé au RPE : les charges s'adaptent au
ressenti, échauffements calculés automatiquement, minuteur de repos, records,
journal et test des maxs en fin de bloc. **100% local** : tes données restent sur
ton appareil (localStorage), aucune connexion requise après le premier chargement.

## Fichiers

- `index.html` — l'application (autonome).
- `manifest.webmanifest` — métadonnées PWA (nom, couleurs, icônes).
- `sw.js` — service worker : met l'app en cache pour un usage hors-ligne.
- `icons/` — icônes de l'app (dont les icônes *maskable* pour Android/Samsung).
- `scripts/make_icons.py` — script de génération des icônes (Pillow).

## Installer sur un Samsung (Android)

Sur Android, une PWA s'installe comme une **vraie application** : icône dans le
tiroir d'apps, plein écran, fonctionnement hors-ligne.

### Avec Samsung Internet
1. Ouvrir l'URL de l'app dans **Samsung Internet**.
2. Toucher le menu **☰** (en bas à droite).
3. Choisir **« Ajouter la page à »** → **« Écran d'accueil »** (ou l'icône
   d'installation qui apparaît dans la barre d'adresse).
4. Confirmer. L'icône **BENCH+** apparaît sur l'écran d'accueil.

### Avec Chrome
1. Ouvrir l'URL de l'app dans **Chrome**.
2. Une bannière **« Installer l'application »** apparaît en bas — la toucher.
   (Sinon : menu **⋮** → **« Installer l'application »** / **« Ajouter à
   l'écran d'accueil »**.)
3. Confirmer avec **Installer**.

L'app se lance ensuite en plein écran, sans barre de navigateur, et fonctionne
sans connexion.

## Publier l'app (GitHub Pages)

Dans le dépôt GitHub : **Settings → Pages**, source **Deploy from a branch**,
choisir la branche puis le dossier **/(root)**, enregistrer. L'URL publique est
de la forme `https://<utilisateur>.github.io/<dépôt>/`. Ouvre cette URL sur ton
Samsung pour installer l'app.

> Une PWA nécessite **HTTPS** pour être installable. GitHub Pages fournit le
> HTTPS automatiquement.

## Régénérer les icônes

```bash
pip install pillow
python3 scripts/make_icons.py
```
