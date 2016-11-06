#!/bin/sh

# Author: Adam Cécile <acecile@mandriva.com>
# License: Public domain

. /usr/share/megactl/create-devices-nodes

create_node

if [ $? -eq 0 ]; then
    /usr/sbin/megactl.real $@
else
    echo "No LSI MegaRAID cards found. You may try megasasctl instead."
    exit 1
fi
