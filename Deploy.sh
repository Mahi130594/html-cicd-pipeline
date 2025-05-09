#!/bin/bash

# GitHub repo URL
REPO_URL="https://github.com/Mahi130594/html-cicd-pipeline.git"
TMP_DIR="/tmp/html-cicd"
DEST_DIR="/var/www/html"

echo "Deploying the latest code..."

# Remove old temp folder
rm -rf $TMP_DIR

# Clone the repo
git clone $REPO_URL $TMP_DIR

# Copy HTML file to nginx default web directory
sudo cp $TMP_DIR/index.html $DEST_DIR/index.html

# Restart nginx to load new content
sudo systemctl restart nginx

echo "Deployment done!"
