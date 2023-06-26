#!/usr/bin/env bash
if ["$#" -lt 4 ]; then
  echo "Usage: $0 PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
else
  file_path=$1
  server_ip=$2
  username=$3
  ssh_key=$4

  scp -o StrictHostKeyChecking=no -i "$ssh_key" "$file_path" "$username@$server_ip:~/"
fi
