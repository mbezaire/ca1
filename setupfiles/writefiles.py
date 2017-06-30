import neuron
# neuron.h(''' create soma''')

def listMechParams( flag ):
    sec = neuron.h.cas()
    # sec.insert('hh')
    # sec.insert('ch_Nav')
    totmechct=0
    neuron.h(''' objref paramlist''')
    neuron.h(''' paramlist = new List()''')
    #neuron.h('''begintemplate String\npublic s\nstrdef s\nproc init() {s = $s1}\nendtemplate String''')
    neuron.h('objref gg')
    for mech in sec(0.5):
        if flag==1:
            # coming back to hoc
            params=[elem for elem in dir(mech) if "_"+mech.name() in elem]
        else:
            # all in python
            params=[elem.replace('_'+mech.name(),'') for elem in dir(mech) if "_"+mech.name() in elem]
        if not params:
            params = [mech.name()[0:-4]+ "i", mech.name()[0:-4]+ "o"]
        totmechct = totmechct + len(params)
        for param in params:
            neuron.h(''' gg = new String("''' + param + '''")\n{paramlist.append(gg)}''')
    # neuron.h('print paramlist.count()')
    return totmechct
