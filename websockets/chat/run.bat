@echo off

if "%~1"=="" (
    echo Please provide an argument: 'python' or 'javascript'.
    goto end
)

if "%~1"=="javascript" (
    echo Running JavaScript environment setup...
    
    npm install
    node backend\javascript\index.js
    goto end
)

if "%~1"=="python" (
    echo Running Python environment setup...
    python -m venv backend\python\venv
    CALL backend\python\venv\Scripts\activate.bat
    pip install -r backend\python\requirements.txt
    python backend\python\main.py
    CALL backend\python\venv\Scripts\deactivate.bat
    goto end
)

echo Invalid argument. Please use 'python' or 'javascript'.

:end
pause
@echo on
