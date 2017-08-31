#!/bin/bash
# calls jnml netpye (to zip necessary files afterwards and send to NSG-R)

cd $1/network/
jnml LEMS_$2.xml -netpyne
