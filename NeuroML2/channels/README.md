### NeuroML2 channels

- see documented individual channel descriptions in .channel.nml files
- see summary of channel dynamics in [/channel_summary](/channel_summary/README.md) (based on the NeuroML2 version)
- to compare the NeuroML2 version to the original .mod files run:

    ```
    ../../analyse_modchans.sh  # analyses original .mod channels (using pyNeuroML and saves .dat files)
    ./analyse_chans.sh  # analyses .nml channels (using pyNeuroML and saves .dat files + creates /channel_summary)
    python compare_nml_mod.py  # loads in .dat files (created by the bash scripts) and plots them together!
    ```
