#!/bin/sh

# Author: Adam Cécile <acecile@mandriva.com>
# License: Public domain

. /usr/share/megactl/create-devices-nodes

create_node_sas

if [ $? -eq 0 ]; then
    /usr/sbin/megasasctl.real $@
else
    echo "No LSI MegaRAID SAS cards found. You may try megactl instead."
    exit 1
fi
