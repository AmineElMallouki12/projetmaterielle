#!/bin/bash

echo "========================================"
echo "  Configuration du Projet Flask"
echo "========================================"
echo

echo "[1/5] Verification de Python..."
if command -v python3 &> /dev/null; then
    echo "✅ Python3 detecte: $(python3 --version)"
elif command -v python &> /dev/null; then
    echo "✅ Python detecte: $(python --version)"
else
    echo "❌ Python n'est pas installe"
    echo "Veuillez installer Python 3.8+"
    exit 1
fi

echo
echo "[2/5] Creation de l'environnement virtuel..."
if [ -d "venv" ]; then
    echo "ℹ️  L'environnement virtuel existe deja"
else
    python3 -m venv venv 2>/dev/null || python -m venv venv
    echo "✅ Environnement virtuel cree"
fi

echo
echo "[3/5] Activation de l'environnement virtuel..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "❌ Erreur lors de l'activation de l'environnement virtuel"
    exit 1
fi
echo "✅ Environnement virtuel active"

echo
echo "[4/5] Installation des dependances..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Erreur lors de l'installation des dependances"
    exit 1
fi
echo "✅ Dependances installees"

echo
echo "[5/5] Configuration de la base de donnees..."
echo "⚠️  Assurez-vous que MongoDB est demarre avant de continuer"
echo
read -p "Voulez-vous configurer la base de donnees maintenant? (o/n): " choice
if [[ $choice =~ ^[Oo]$ ]]; then
    python setup_database.py
else
    echo "ℹ️  Vous pourrez configurer la base de donnees plus tard avec: python setup_database.py"
fi

echo
echo "========================================"
echo "  Configuration terminee!"
echo "========================================"
echo
echo "Pour demarrer l'application:"
echo "1. Activer l'environnement virtuel: source venv/bin/activate"
echo "2. Lancer l'application: python app.py"
echo "3. Ouvrir: http://127.0.0.1:5000"
echo
echo "Utilisateurs par defaut:"
echo "- Admin: admin / admin123"
echo "- Technicien: technicien / tech123"
echo "- Professeur: professeur / prof123"
echo "- Etudiant: etudiant / etud123"
echo

# Rendre le script executable
chmod +x setup_unix.sh
