# Rofi Proxmox

Docker container that calls Proxmox API for all IPs from virtual machines(Qemu) with guest agent installed. Can be piped into Rofi to provide a quick IP lookup and or piped into `xclip`.

<p align="center"><a href="https://i.imgur.com/kebwh6I.gif"><img src="https://i.imgur.com/BL3Mrsq.png"></a></p>

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