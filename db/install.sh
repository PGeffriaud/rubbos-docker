
#!/bin/bash

# Script bash permettant le téléchargement de la base de données de Rubbos

echo "Step 2: Downloading the database files.."
curl -L https://googledrive.com/host/0BzlS97rKsAqgfnB2LV8zTUJ2aktjN1phampiSVE4RjJOUFZXdUIzNndtVzJ1RVVyaGM0bkU/data.zip > data.zip
unzip data.zip
