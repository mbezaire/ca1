### NeuroML2 channels

- see documented individual channel descriptions in .channel.nml files, e.g. [KvAolm.channel.nml](KvAolm.channel.nml)
- see summary of channel dynamics in [channel_summary](channel_summary/README.md) (plots generated from the NeuroML2 files)
- to compare the NeuroML2 versions to the original .mod files run:

```
../../analyse_modchans.sh  # analyses original .mod channels (using pyNeuroML and saves .dat files)
./analyse_nmlchans.sh  # analyses .nml channels (using pyNeuroML and saves .dat files + creates /channel_summary)
python compare_nml_mod.py  # loads in .dat files (created by the bash scripts) and plots them together!
```
