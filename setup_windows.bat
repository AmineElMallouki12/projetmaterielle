@echo off
echo ========================================
echo   Configuration du Projet Flask
echo ========================================
echo.

echo [1/5] Verification de Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python n'est pas installe ou pas dans le PATH
    echo Veuillez installer Python 3.8+ depuis python.org
    pause
    exit /b 1
)
echo ✅ Python detecte

echo.
echo [2/5] Creation de l'environnement virtuel...
if exist "venv" (
    echo ℹ️  L'environnement virtuel existe deja
) else (
    python -m venv venv
    echo ✅ Environnement virtuel cree
)

echo.
echo [3/5] Activation de l'environnement virtuel...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ Erreur lors de l'activation de l'environnement virtuel
    pause
    exit /b 1
)
echo ✅ Environnement virtuel active

echo.
echo [4/5] Installation des dependances...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Erreur lors de l'installation des dependances
    pause
    exit /b 1
)
echo ✅ Dependances installees

echo.
echo [5/5] Configuration de la base de donnees...
echo ⚠️  Assurez-vous que MongoDB est demarre avant de continuer
echo.
set /p choice="Voulez-vous configurer la base de donnees maintenant? (o/n): "
if /i "%choice%"=="o" (
    python setup_database.py
) else (
    echo ℹ️  Vous pourrez configurer la base de donnees plus tard avec: python setup_database.py
)

echo.
echo ========================================
echo   Configuration terminee!
echo ========================================
echo.
echo Pour demarrer l'application:
echo 1. Activer l'environnement virtuel: venv\Scripts\activate.bat
echo 2. Lancer l'application: python app.py
echo 3. Ouvrir: http://127.0.0.1:5000
echo.
echo Utilisateurs par defaut:
echo - Admin: admin / admin123
echo - Technicien: technicien / tech123
echo - Professeur: professeur / prof123
echo - Etudiant: etudiant / etud123
echo.
pause
