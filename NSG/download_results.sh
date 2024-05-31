#!/bin/bash

source ./read_env_variables

echo "Accessing: $URL/job/$USERNAME/$1 for user $USERNAME"

curl --user $USERNAME:$PASSWORD \
     -H cipres-appkey:$DIRECT_APPID \
     -O -J \
     $URL/job/$USERNAME/$1/output/$2
