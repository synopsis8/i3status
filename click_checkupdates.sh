#!/bin/sh

# we click on the count of available packages to update
# so let's update the system
echo "Update OS..."
sudo pacman -Suy --noconfirm
