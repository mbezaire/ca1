#!/bin/bash

source ./read_env_variables

echo "Deleting job: $1 for user $USERNAME"

curl -i --user $USERNAME:$PASSWORD \
     -H cipres-appkey:$DIRECT_APPID \
     -X DELETE \
     $URL/job/$USERNAME/$1 
