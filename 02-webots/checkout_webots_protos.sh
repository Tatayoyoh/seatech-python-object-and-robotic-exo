#!/bin/bash

# Télécharge en local l'ensemble des fichiers PROTO trouvés dans l'installation Webots
# Cela permet de rechercher une fonctionnalité par la suite dans ces définitions de PROTO (gps, lidar, ...)

DLL_PATH=$HOME/webots_protos

for PROTO in $(egrep -roh "https.*proto" /usr/local/webots/projects/robots/ | grep 'projects/robots' | sort | uniq ) ; do 
    f=$(basename $PROTO) 
    p=`echo $PROTO | cut -d '/' -f9`
    dest=$DLL_PATH/$p
    [ ! -d "$dest" ] && mkdir -p $dest
    wget -q $PROTO -O $dest/$f
    echo "Téléchargé $dest/$f"
done

