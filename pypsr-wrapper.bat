@echo off

REM Vérifier la présence de Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python n'est pas installé sur le système.
    echo Veuillez installer Python avant d'exécuter ce script.
    pause
    exit /b
)

REM Vérifier la présence de pip
pip --version >nul 2>&1
if errorlevel 1 (
    echo pip n'est pas installé sur le système.
    echo Veuillez installer pip avant d'exécuter ce script.
    pause
    exit /b
)

REM Installer les dépendances à partir du fichier requirements.txt
pip install -r requirements.txt

REM Démarrer le script main.py
start python main.py
