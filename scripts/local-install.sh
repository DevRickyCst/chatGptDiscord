#!/bin/bash
activate_virtual_environment() {

    echo Systeme $OSTYPE detected
    # Détecter le système d'exploitation
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Commande pour activer un environnement virtuel dans les systèmes Linux
        source venv/bin/activate
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Commande pour activer un environnement virtuel dans macOS
        source venv/bin/activate
    elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        # Commande pour activer un environnement virtuel dans Windows (Git Bash)
        source venv/Scripts/activate
    else
        echo "Système d'exploitation non pris en charge."
        exit 1
    fi

    # Votre code à exécuter dans l'environnement virtuel
}

if [[ ! -d "$DIRECTORY" ]]
then
    echo Creating virtual environnement
    python3 -m venv venv
else
    echo Virtual environnement already existed
fi
activate_virtual_environment
echo pip install -r requirements.txt
pip install -r requirements.txt
