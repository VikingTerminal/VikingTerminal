#!/bin/bash

# Nome esatto della directory
REPO_NAME="VikingTerminal"

# Rimuove la directory esistente
rm -rf $REPO_NAME

# Clona il repository
git clone https://github.com/VikingTerminal/VikingTerminal

# Entra nella directory
cd $REPO_NAME

# Rende eseguibili i file .pyc
chmod +x *.pyc

# Esegue il file PROMPT.pyc
python PROMPT.pyc
