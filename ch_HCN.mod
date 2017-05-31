TITLE Hyperpolarization-activated, CN-gated channel (voltage dependent)

COMMENT
Hyperpolarization-activated, CN-gated channel (voltage dependent)

Ions: non-specific

Style: quasi-ohmic

From: Chen et al (2001), distal dendrite, control h channel
(modeling by Ildiko Aradi, iaradi@uci.edu)

Updates:
2014 December (Marianne Bezaire): documented, only slow tau used, fake
ion switched to a non-specific current
ENDCOMMENT


VERBATIM
#include <stdlib.h> /* 	Include this library so that the following
						(innocuous) warning does not appear:
						 In function '_thread_cleanup':
						 warning: incompatible implicit declaration of 
						          built-in function 'free'  */
ENDVERBATIM
 
UNITS {
	(mA) =(milliamp)
	(mV) =(millivolt)
	(uF) = (microfarad)
	(molar) = (1/liter)
	(nA) = (nanoamp)
	(mM) = (millimolar)
	(um) = (micron)
	FARADAY = 96520 (coul)
	R = 8.3134	(joule/degC)
}
 
NEURON { 
	SUFFIX ch_HCN 
	NONSPECIFIC_CURRENT i
	RANGE gmax, g, i, e
	RANGE hinf
	RANGE slow_tau :, fast_tau
	RANGE myi
}
 
 
PARAMETER {
	gmax  (mho/cm2)
	e (mV)
}
 
STATE {
	h
}
 
ASSIGNED {
	v (mV) 
	celsius (degC)
	dt (ms)    
  
	g (mho/cm2)
 	i (mA/cm2)
	
	hinf 
 	:fast_tau (ms)
 	slow_tau (ms) 
 	myi (mA/cm2)
} 

BREAKPOINT {
	SOLVE states METHOD cnexp
		
	g = gmax*h*h
	i = g*(v - e)
	myi = i
}
 
UNITSOFF
 
INITIAL { : called from hoc to calculate hinf at resting potential
	trates(v)
	h = hinf
}

DERIVATIVE states {	:computes h at current v and dt 
	trates(v)
	h' = (hinf-h)/slow_tau :  + (hinf-h)/fast_tau
}
 
LOCAL q10
PROCEDURE trates(v) {  :Computes rate and other constants at current v.
	TABLE hinf, slow_tau : , fast_tau
	DEPEND celsius 
	FROM -120 TO 100 WITH 220
                           
    :q10 = 3^((celsius - 6.3)/10)
    q10 = 3^((celsius - 34)/10)
       
	hinf =  1 / (1 + exp( (v+91)/10 ))

	:"hyf" FAST CONTROL Hype activation system
	:fast_tau = (14.9 + 14.1 / (1+exp(-(v+95.2)/0.5)))/q10

	:"hys" SLOW CONTROL Hype activation system
	slow_tau = (80*1.5 + .75*172.7 / (1+exp(-(v+59.3)/-0.83)))/q10

}

UNITSON
