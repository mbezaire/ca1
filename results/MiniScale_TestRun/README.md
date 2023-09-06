- data files used for creating NeuroML2 network (see more [here](https://github.com/mbezaire/ca1/tree/development/NeuroML2/network/GenerateHippocampalNet.py))
> folder added by Andras (by running):

    cd ../../
    nrniv -c "NumData=101" -c "ConnData=430" -c "SynData=120" -c "Scale=100000" -c "SimDuration=100" -c "strdef RunName" -c "RunName= \"MiniScale_TestRun\"" ./main.hoc -c "quit()"  # runs the simulation (saves files into results/MiniScale_TestRun/)
    nrniv -c "NumData=101" -c "ConnData=430" -c "SynData=120" -c "Scale=100000" ./launch_synapse_printer.hoc -c "quit()"  # saves more data about synapses into results/
