# This script uses utilities in https://github.com/NeuroML/pyNeuroML to generate
# plots for the activation variables, etc. of selected channels in nml files



pynml-channelanalysis CavL.channel.nml -temperature 24 -caConc 5e-6 -scaleDt 0.25 -html -md
