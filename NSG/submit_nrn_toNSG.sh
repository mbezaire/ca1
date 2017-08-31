#!/bin/bash

source ./read_env_variables

echo "Accessing: $URL/job/$USERNAME for user $USERNAME"

curl -i --user $USERNAME:$PASSWORD \
     -H cipres-appkey:$DIRECT_APPID \
      $URL/job/$USERNAME \
     -F tool='NEURON74_TG' \
     -F input.infile_=@./CA1_nrn.zip \
     -F metadata.clientJobId=$1 \
     -F metadata.statusEmail=true \
     -F vparam.number_cores_=24 \
     -F vparam.number_nodes_=$2
