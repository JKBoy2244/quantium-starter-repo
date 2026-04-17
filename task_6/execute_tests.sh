#!/usr/bin/env bash

source venv/Scripts/activate

python -m pytest task_5/test_app.py -v

if [ $? -eq 0 ]; then
    exit 0
else
    exit 1
fi
