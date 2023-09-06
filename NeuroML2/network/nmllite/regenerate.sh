set -e

python GenerateExamples.py -all

python GenerateNetwork.py -all

python GenerateNetwork.py -test -nml

