from dotenv import load_dotenv
from proxmoxer import ProxmoxAPI
import urllib3
import os

load_dotenv()
urllib3.disable_warnings()

proxmox = ProxmoxAPI(
    host=os.getenv('PROXMOX_HOST', "localhost"),
    user=os.getenv('PROXMOX_USER'),
    token_name=os.getenv('PROXMOX_TNAME'),
    token_value=os.getenv('PROMOX_TVALUE'),
    verify_ssl=os.getenv('proxmox_ssl', False)
)

# Get the list of all the nodes available from the connected node
nodes = proxmox.nodes.get()

# Iterate through each node and print the containers and their status
for pve_node in nodes:
    node_name = pve_node['node']

    # Get the list of containers in the current node
    containers = proxmox(f"nodes/{node_name}/qemu").get()
    for container in containers:
        container_name = container["name"]
        try:
            # Get the network interfaces for the current container
            network_interfaces = proxmox(f"nodes/{node_name}/qemu/{container['vmid']}/agent/network-get-interfaces").get()["result"]
            for interface in network_interfaces:
                if interface["name"] != "lo":
                    for ip_address in interface['ip-addresses']:
                        print(f"{node_name},{container_name},{interface['name']},{ip_address['ip-address']}")
        except:
            # print(f"{node_name},{container_name}")
            pass
