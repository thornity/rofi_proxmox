# Rofi Proxmox

Provides a docker container that calls into Proxmox API to grab all of the IPs from virtual machines(Qemu) that have the guest agent installed providing an IP.

This can be paired with Rofi to provide a quick IP lookup to your clipboard

```bash

# Copy env & modify it
mkdir -p ~/rofi_promox && cd "$_"
wget https://raw.githubusercontent.com/thornity/rofi_proxmox/main/.env.dist -O ~/rofi_promox/.env
vim ~/rofi_promox/.env

# Pull container
docker pull thornity/rofi_proxmox:latest

# Run
docker run -v ${PWD}/.env:/usr/app/src/.env thornity/rofi_proxmox:latest | rofi -dmenu -p "IP address To Copy" | cut -d ',' -f4 | xclip -selection clipboard
```