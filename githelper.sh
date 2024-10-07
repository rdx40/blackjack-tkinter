#!/bin/bash

echo "What do you want to do?"
echo "1. Status"
echo "2. Add all"
echo "3. Commit"
echo "4. Push"
read -p "Choose an option (1-4): " option

case $option in
    1) git status ;;
    2) git add . ;;
    3) 
       read -p "Enter commit message: " msg
       git commit -m "$msg"
       ;;
    4) git push ;;
    *) echo "Invalid option" ;;
esac

