#!/bin/bash 

# Script permettant l'installation des paquets liés à notre programme 

echo "Step 1: Installing software..."

yaourt -S --noconfirm docker wget curl python python-psutil

cd db && ./install.sh


echo "Install finished"
echo "Please make sure that the DB files have the good rights"
