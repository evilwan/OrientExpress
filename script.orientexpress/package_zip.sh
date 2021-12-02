#!/bin/sh
#
# Create zip installer for add-on
#

ADDON=`basename $(dirname $(readlink -f $0))`
VERSION=`cat VERSION`
OUTFILE=${ADDON}-${VERSION}.zip

sed -i "s/\(^<addon.*version=\"\)[^\"]*\(\".*\)/\1${VERSION}\2/" addon.xml

HERE=`pwd`
cd ..
zip -r ${OUTFILE} ${ADDON}/*
cd ${HERE}
