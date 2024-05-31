# This script uses utilities in https://github.com/NeuroML/pyNeuroML to generate
# plots for the activation variables, etc. of selected channels in nml files

# CavL.channel.nml    See analyse_chans2.sh ; requires -scaleDt 0.25 
# KCaS.channel.nml \

pynml-channelanalysis Kdrslow.channel.nml Kdrfast.channel.nml  Kdrp.channel.nml Kdrfastngf.channel.nml \
                      KvAolm.channel.nml KvA.channel.nml KvAproxp.channel.nml KvAdistp.channel.nml \
                      KvAngf.channel.nml KvGroup.channel.nml \
                      KvCaB.channel.nml \
                      KvMnew.channel.nml \
		              HCNolm.channel.nml HCN.channel.nml  HCNp.channel.nml \
                      Nav.channel.nml Navbis.channel.nml Navcck.channel.nml Navccknew.channel.nml \
                      Navaxonp.channel.nml Navngf.channel.nml Navp.channel.nml \
                      CavN.channel.nml \
                      -temperature 34 -caConc 5e-6  -html -md
