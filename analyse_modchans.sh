# This script uses utilities in https://github.com/NeuroML/pyNeuroML to generate
# plots for the activation variables, etc. of selected channels in mod files
# added by Andras - only for .mod vs .channel.nml comparison!

# just to make sure:
rm -rf x86_64
nrnivmodl

# create .dat files
pynml-modchananalysis ch_CavN       -temperature 34 -stepV 5 -caConc 5e-6 -duration 50000 -nogui

pynml-modchananalysis ch_HCN        -temperature 34 -stepV 5 -nogui
pynml-modchananalysis ch_HCNolm     -temperature 34 -stepV 5 -duration 30000 -nogui
pynml-modchananalysis ch_HCNp       -temperature 34 -stepV 5 -nogui

pynml-modchananalysis ch_KvCaB      -temperature 34 -stepV 5 -caConc 5e-6   -nogui

pynml-modchananalysis ch_Kdrfast    -temperature 34 -stepV 5 -nogui
pynml-modchananalysis ch_Kdrfastngf -temperature 34 -stepV 5 -nogui
pynml-modchananalysis ch_Kdrp       -temperature 34 -stepV 5 -nogui
pynml-modchananalysis ch_Kdrslow    -temperature 34 -stepV 5 -nogui

pynml-modchananalysis ch_KvA        -temperature 34 -stepV 5 -nogui
pynml-modchananalysis ch_KvAdistp   -temperature 34 -stepV 5 -nogui
pynml-modchananalysis ch_KvAngf     -temperature 34 -stepV 5 -nogui
pynml-modchananalysis ch_KvAolm     -temperature 34 -stepV 5 -nogui # not working properly??
pynml-modchananalysis ch_KvAproxp   -temperature 34 -stepV 5 -nogui
pynml-modchananalysis ch_KvGroup    -temperature 34 -stepV 5 -nogui
pynml-modchananalysis ch_KvMnew     -temperature 34 -stepV 5 -nogui

pynml-modchananalysis ch_Nav        -temperature 34 -stepV 5 -nogui -dt 0.001
pynml-modchananalysis ch_Navaxonp   -temperature 34 -stepV 5 -nogui -dt 0.001
pynml-modchananalysis ch_Navbis     -temperature 34 -stepV 5 -nogui -dt 0.001
pynml-modchananalysis ch_Navcck     -temperature 34 -stepV 5 -nogui -dt 0.001
pynml-modchananalysis ch_Navccknew  -temperature 34 -stepV 5 -nogui -dt 0.001
pynml-modchananalysis ch_Navngf     -temperature 34 -stepV 5 -nogui -dt 0.001
pynml-modchananalysis ch_Navp       -temperature 34 -stepV 5 -nogui -dt 0.001
                      
