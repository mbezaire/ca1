set -e
# small nets
python GeneratePINGNet_oc.py -test

# main network
python GenerateHippocampalNet_oc.py -test
