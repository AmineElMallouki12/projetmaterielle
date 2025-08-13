# 🚀 Guide de Démarrage Rapide

## ⚡ Installation en 5 minutes

### Windows
1. **Double-cliquez sur `setup_windows.bat`**
2. Suivez les instructions à l'écran
3. C'est tout ! 🎉

### macOS/Linux
1. **Ouvrez un terminal dans le dossier du projet**
2. **Rendez le script executable et lancez-le :**
   ```bash
   chmod +x setup_unix.sh
   ./setup_unix.sh
   ```
3. Suivez les instructions à l'écran

## 🔧 Installation Manuelle

### 1. Prérequis
- **Python 3.8+** installé
- **MongoDB** démarré et accessible

### 2. Commandes
```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Configurer la base de données
python setup_database.py

# Lancer l'application
python app.py
```

### 3. Accès
- **URL** : http://127.0.0.1:5000
- **Admin** : `admin` / `admin123`

## 🆘 Problèmes Courants

### "Python n'est pas reconnu"
- Installez Python depuis [python.org](https://python.org)
- Cochez "Add to PATH" lors de l'installation

### "MongoDB connection failed"
- Installez MongoDB depuis [mongodb.com](https://mongodb.com)
- Démarrez le service MongoDB

### "Module not found"
- Activez l'environnement virtuel : `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (macOS/Linux)
- Réinstallez : `pip install -r requirements.txt`

## 📱 Test Rapide

1. **Lancez l'application** : `python app.py`
2. **Ouvrez** : http://127.0.0.1:5000
3. **Connectez-vous** avec `admin` / `admin123`
4. **Explorez** le tableau de bord !

---

**Besoin d'aide ?** Consultez le `README.md` complet pour plus de détails.
