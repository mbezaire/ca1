
NEURON {
    SUFFIX ica_clamp
    USEION ca WRITE ica
    RANGE ica_clamp
}

UNITS {
	(mV) =	(millivolt)
	(mA) =	(milliamp)
}

PARAMETER {
    delay = 50 (ms)
    duration = 100 (ms)
    magnitude = 1
    gbar = 1e-6 (mho/cm2)
    E = 50 (mV)
}

ASSIGNED {
    ica_clamp 
    ica (mA/cm2)   
}


BREAKPOINT {
    
    if (t <=  delay) {
        ica_clamp = 0
    }
    
    if (t >=  delay  && t <=  duration  +  delay) {
        ica_clamp = magnitude
    }
    
    if (t >=  duration  +  delay) {
        ica_clamp = 0
    }

    ica = gbar*ica_clamp*(v-E)
}

