#!/bin/bash

DATA_DIR=$(python manage.py get_conf_var DATA_DIR)

for year in $(python manage.py get_conf_var years --rettype=iterable)
do
    echo "Getting links for $year"
    TAR="$DATA_DIR/$year"
    mkdir -p $TAR
    LINKS=$(python manage.py obdobi_links $year)
    cd $TAR
    echo $LINKS | xargs -P 10 -r -n 1 wget -N
    find -name '*.zip' -exec sh -c 'unzip -o -d "${1%.*}" "$1"' _ {} \;
    cd -
done
