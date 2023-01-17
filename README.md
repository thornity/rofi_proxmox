# Rofi Proxmox

Provides a docker container that calls into Proxmox API to grab all of the IPs from virtual machines(Qemu) that have the guest agent installed providing an IP.

This can be paired with Rofi to provide a quick IP lookup to your clipboard

```bash

# Copy env & modify it
cp ./.env.dist ./.env
vim ./.env

docker run -v ${PWD}/.env:/usr/app/src/.env ghcr.io/thornity/rofi_proxmox:latest | rofi -dmenu -p "IP address To Copy" | cut -d ',' -f4 | xclip -selection clipboard
```