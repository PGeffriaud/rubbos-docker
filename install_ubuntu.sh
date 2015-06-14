#!/bin/bash 

# Script permettant l'installation des paquets liés à notre programme 

echo "Step 1: Installing software..."

sudo apt-get update
sudo apt-get install -y wget curl python python-psutil
wget -qO- https://get.docker.com/ | sh

cd db && ./install.sh


echo "Install finished"
echo "Please make sure that the DB files have the good rights"
