#!/bin/sh

# Author: Adam Cécile <acecile@mandriva.com>
# License: Public domain

. /usr/share/megactl/create-devices-nodes

create_node
create_node_sas

/usr/sbin/megatrace.real $@
