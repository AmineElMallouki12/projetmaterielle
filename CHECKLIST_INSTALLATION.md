# ✅ Checklist d'Installation

## 🔍 Vérifications Préalables

### Système d'Exploitation
- [ ] **Windows 10/11** ou **macOS 10.15+** ou **Linux Ubuntu 20.04+**

### Python
- [ ] **Python 3.8+** installé
- [ ] **pip** disponible (`pip --version`)
- [ ] **venv** disponible (`python -m venv --help`)

### MongoDB
- [ ] **MongoDB 4.4+** installé
- [ ] **Service MongoDB** démarré
- [ ] **Port 27017** accessible

## 📦 Fichiers du Projet

### Fichiers Principaux
- [ ] `app.py` - Application Flask
- [ ] `requirements.txt` - Dépendances Python
- [ ] `setup_database.py` - Configuration DB
- [ ] `README.md` - Documentation complète
- [ ] `QUICK_START.md` - Guide rapide

### Scripts d'Installation
- [ ] `setup_windows.bat` - Installation Windows
- [ ] `setup_unix.sh` - Installation macOS/Linux

### Dossiers
- [ ] `templates/` - Templates HTML
- [ ] `static/` - Fichiers statiques (CSS, JS, uploads)

## 🚀 Étapes d'Installation

### 1. Préparation
- [ ] Extraire le fichier ZIP dans un dossier
- [ ] Ouvrir un terminal/commande dans ce dossier
- [ ] Vérifier que MongoDB est démarré

### 2. Installation Automatique
- [ ] **Windows** : Double-cliquer sur `setup_windows.bat`
- [ ] **macOS/Linux** : Exécuter `./setup_unix.sh`

### 3. Installation Manuelle (si nécessaire)
- [ ] Créer l'environnement virtuel : `python -m venv venv`
- [ ] Activer l'environnement virtuel
- [ ] Installer les dépendances : `pip install -r requirements.txt`
- [ ] Configurer la base de données : `python setup_database.py`

### 4. Test
- [ ] Lancer l'application : `python app.py`
- [ ] Ouvrir : http://127.0.0.1:5000
- [ ] Se connecter avec `admin` / `admin123`

## 🔧 Résolution de Problèmes

### Erreurs Courantes
- [ ] **Python non reconnu** → Installer Python et cocher "Add to PATH"
- [ ] **MongoDB connection failed** → Démarrer le service MongoDB
- [ ] **Module not found** → Activer l'environnement virtuel et réinstaller
- [ ] **Port 5000 occupé** → Changer le port dans `app.py`

### Vérifications
- [ ] **Environnement virtuel** activé (voir `(venv)` au début de la ligne de commande)
- [ ] **MongoDB** accessible sur localhost:27017
- [ ] **Dépendances** installées (`pip list` affiche Flask, PyMongo, etc.)

## 📱 Test Final

### Fonctionnalités à Tester
- [ ] **Connexion** avec différents utilisateurs
- [ ] **Tableau de bord** accessible
- [ ] **Inventaire** visible et navigable
- [ ] **Réservations** créables
- [ ] **Exports** fonctionnels (pour les rôles autorisés)

### Utilisateurs de Test
- [ ] **Admin** : `admin` / `admin123` - Accès complet
- [ ] **Technicien** : `technicien` / `tech123` - Gestion équipements
- [ ] **Professeur** : `professeur` / `prof123` - Approbation réservations
- [ ] **Étudiant** : `etudiant` / `etud123` - Création réservations

## 🎯 Succès

Si toutes les cases sont cochées ✅, votre projet fonctionne parfaitement !

**URL d'accès** : http://127.0.0.1:5000

---

**Besoin d'aide ?** Consultez le `README.md` ou créez une issue sur le projet.
