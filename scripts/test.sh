#!/bin/bash
#
for i in sdms/*/* ; do #
    if [ ! -d "$i"/output ]; then #
        mkdir "$i"/output #
        chmod 777 "$i"/output #
    fi #
done #
