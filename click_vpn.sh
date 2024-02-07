#!/bin/sh

# Actually works for ProtonVPN
# we are connected if the directory exists
if [ -d /proc/sys/net/ipv4/conf/tun0 ]; then
  # we are connected, so propose disconnexion
  echo "Disconnect VPN"
  nmcli connection down Russia-udp
else
  echo "Connect VPN"
  nmcli connection up Russia-udp passwd-file ${HOME}/myvpnpassword
fi
