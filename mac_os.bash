#!/bin/bash

#script to automatically start backend but not working
osascript -e 'tell application "Terminal" to do script "echo Running Flask development server && source env/bin/activate && python main.py"'
