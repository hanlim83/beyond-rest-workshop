#!/bin/bash

# chmod +x ./run.sh
# ./run.sh


if [ "$#" -eq 0 ]; then
    echo "Please provide an argument: 'python' or 'javascript'."
    exit 1
fi

if [ "$1" == "javascript" ]; then
    echo "Running JavaScript environment setup..."

    npm install
    node backend/javascript/index.js

elif [ "$1" == "python" ]; then
    echo "Running Python environment setup..."

    virtualenv ./backend/python/venv
    source ./backend/python/venv/bin/activate
    pip install -r ./backend/python/requirements.txt
    python backend/python/main.py

else
    echo "Invalid argument. Please use 'python' or 'javascript'."
    exit 1
fi
