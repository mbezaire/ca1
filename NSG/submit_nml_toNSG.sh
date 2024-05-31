#!/bin/bash

source ./read_env_variables

echo "Accessing: $URL/job/$USERNAME for user $USERNAME"

curl -i --user $USERNAME:$PASSWORD \
     -H cipres-appkey:$DIRECT_APPID \
      $URL/job/$USERNAME \
     -F tool='OSBPYNEURON74' \
     -F input.infile_=@./CA1_nml_scale$1.zip \
     -F metadata.clientJobId=$2 \
     -F metadata.statusEmail=true \
     -F vparam.number_cores_=20 \
     -F vparam.number_nodes_=$3 \
     -F vparam.runtime_=$4
