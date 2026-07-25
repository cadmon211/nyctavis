# NYCTAVIS — Microsoft Store listing kit

Everything to fill the Partner Center "Store listings" step. Cleaned screenshots
(Windows taskbar removed, folder paths blurred) live in:

- `assets/screenshots/en/`  (10) — **primary gallery, used for all markets**
- `assets/screenshots/es/`  (10) — optional Spanish captures
- `assets/screenshots/fr/`  (11) — optional French captures

> Microsoft Store lets one screenshot set serve every language, so the **EN set
> below is enough for launch**. Swap in `es/` or `fr/` only if you want localized captures.

---

## Product identity
- **Product name:** NYCTAVIS
- **Category:** Utilities & tools  →  **Sub-category:** File & folder tools
- **Privacy policy URL:** `https://nyctavis.com/privacy.html`
- **Support / website:** `https://nyctavis.com`  ·  **Support email:** hello@nyctavis.com
- **Price:** Free (Pro add-on added later)
- **Age rating (IARC questionnaire):** no mature content → expect PEGI 3 / Everyone.

## Search terms / keywords
`disk cleanup`, `duplicate finder`, `free up space`, `system cleanup`, `junk files`,
`recycle bin`, `local`, `privacy`, `storage analyzer`, `nettoyage disque`, `doublons`,
`limpieza de disco`, `duplicados`

---

## Recommended gallery (order matters — best first)

| # | File (assets/screenshots/en/) | Caption EN | Caption ES | Caption FR |
|---|---|---|---|---|
| 1 | `01_dashboard.png` | See your storage at a glance and choose a scan | Consulta tu almacenamiento y elige un análisis | Visualisez votre stockage et choisissez une analyse |
| 2 | `08_recommendations.png` | Clear recommendations: duplicates, junk, reclaimable space | Recomendaciones claras: duplicados, basura, espacio recuperable | Recommandations claires : doublons, fichiers inutiles, espace récupérable |
| 3 | `10_performance_result.png` | Read-only performance check (CPU, memory, disk) | Chequeo de rendimiento de solo lectura (CPU, memoria, disco) | Contrôle de performances en lecture seule (CPU, mémoire, disque) |
| 4 | `03_quarantine.png` | Safe quarantine — review and restore before deleting | Cuarentena segura: revisa y restaura antes de borrar | Quarantaine sûre — vérifiez et restaurez avant de supprimer |
| 5 | `04_history.png` | Full history of scans and reclaimed space | Historial completo de análisis y espacio recuperado | Historique complet des analyses et de l'espace récupéré |
| 6 | `07_scan_in_progress.png` | Fast local scan — nothing leaves your PC | Análisis local rápido: nada sale de tu PC | Analyse locale rapide — rien ne quitte votre PC |
| 7 | `05_settings.png` | Local-first: no cloud, no telemetry, no account | Local primero: sin nube, sin telemetría, sin cuenta | Local d'abord : sans cloud, sans télémétrie, sans compte |

*(Store minimum: 1 screenshot; up to 9. The 7 above are a strong set.)*

---

## Short description (≤ ~100 chars)
- **EN:** Find junk, duplicates and reclaimable disk space — and clean only what you approve. 100% local.
- **ES:** Encuentra basura, duplicados y espacio recuperable — y limpia solo lo que apruebas. 100% local.
- **FR:** Trouvez fichiers inutiles, doublons et espace récupérable — et ne nettoyez que ce que vous approuvez. 100% local.

## Description (long)

**EN**
> NYCTAVIS is a local-first Windows utility that helps you understand and reclaim your disk
> space — safely. It scans your system, surfaces junk and true duplicate files, and guides
> you through a cleanup where nothing is removed without your confirmation.
>
> Everything runs on your computer: no cloud upload, no telemetry, no account.
>
> • Quick scan of the main user areas
> • Guided system cleanup (temp, caches, old installers, recycle bin)
> • Duplicate finder based on file content
> • Reversible quarantine and full action history
> • Available in English, Spanish and French
>
> NYCTAVIS Pro unlocks deep (full) scans, folder-picked scans and the performance monitor.

**ES**
> NYCTAVIS es una utilidad local para Windows que te ayuda a entender y recuperar tu espacio
> en disco, con seguridad. Escanea tu sistema, detecta basura y duplicados reales, y te guía
> en una limpieza donde nada se elimina sin tu confirmación.
>
> Todo se ejecuta en tu ordenador: sin nube, sin telemetría, sin cuenta.
>
> • Análisis rápido de las zonas principales
> • Limpieza guiada del sistema (temporales, cachés, instaladores antiguos, papelera)
> • Buscador de duplicados por contenido
> • Cuarentena reversible e historial completo
> • Disponible en inglés, español y francés
>
> NYCTAVIS Pro desbloquea el análisis completo, el escaneo por carpetas y el monitor de rendimiento.

**FR**
> NYCTAVIS est un utilitaire Windows local qui vous aide à comprendre et récupérer votre
> espace disque, en toute sécurité. Il analyse votre système, révèle les fichiers inutiles et
> les vrais doublons, et vous guide dans un nettoyage où rien n'est supprimé sans votre
> confirmation.
>
> Tout s'exécute sur votre ordinateur : sans cloud, sans télémétrie, sans compte.
>
> • Analyse rapide des zones principales
> • Nettoyage système guidé (temporaires, caches, anciens installeurs, corbeille)
> • Détecteur de doublons basé sur le contenu
> • Quarantaine réversible et historique complet
> • Disponible en anglais, espagnol et français
>
> NYCTAVIS Pro débloque l'analyse complète, l'analyse par dossiers et le moniteur de performances.

---

## Submission checklist
- [ ] Upload `dist\NYCTAVIS.msix` (built unsigned; Microsoft signs it).
- [ ] Paste short + long description (EN, and ES/FR if you add those languages).
- [ ] Upload the 7 gallery screenshots (EN set).
- [ ] Privacy policy URL: `https://nyctavis.com/privacy.html`.
- [ ] Category Utilities & tools; price Free; markets: all.
- [ ] Complete the age-rating questionnaire.
- [ ] Submit for certification.
