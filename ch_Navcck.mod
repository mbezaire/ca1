TITLE sodium channel (voltage dependent)

COMMENT
sodium channel (voltage dependent)

Ions: na

Style: quasi-ohmic

From: not sure where from

Updates:
2014 December (Marianne Bezaire): documented
ENDCOMMENT


VERBATIM
#include <stdlib.h> 
/* 	Include this library so that the following (innocuous) warning does not appear:
		In function '_thread_cleanup':
		warning: incompatible implicit declaration of built-in function 'free'  */
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
	SUFFIX ch_Navcck
	USEION na READ ena WRITE ina VALENCE 1
	RANGE g, gmax, minf, mtau, hinf, htau, ina, m, h, sinf, taus, s, sexp
	RANGE myi
	THREADSAFE
}
 
PARAMETER {
	ena  (mV)
	gmax (mho/cm2)   
	sh   = 15		(mV)

	mAlphC = -0.5 (1) : -0.6 (1)
	mAlphV = 42 (mV) : 44 (mV)
	mBetaC = 0.3 (1) : 0.3
	mBetaV = 13.0 (mV) : 14.5 (mV)

	hAlphC = 0.6 (1) : 23
	hAlphV = 65 (mV)
	hBetaC = 1.3 (1) : 3.33
	hBetaV = 12.5 (mV)

	sAlphC = 0.003 (1) : 0.04 (1) : 23
	sAlphV = 45 (mV) : 45 (mV)
	sBetaC = 0.005 (1) :1 (1) : 3.33
	sBetaV = 35 (mV) : 12.5 (mV)

	vhalfs = -60	(mV)	: slow inact.
	a0s = 0.0003	(ms)	: a0s=b0s
	zetas = 12		(1)
	gms = 0.2		(1)
	smax = 10		(ms)
	vvh = -58		(mV) 
	vvs = 2			(mV)
	ar2 = 0.2			(1)		: 1=no inact., 0=max inact.
}
 
STATE {
	m h s
}
 
ASSIGNED {
	v (mV) 
	celsius (degC) : temperature - set in hoc; default is 6.3
	dt (ms) 

	g (mho/cm2)
	ina (mA/cm2)
	minf
	hinf
	mtau (ms)
	htau (ms)
	mexp
	hexp 
	sexp 
	myi (mA/cm2)
	sinf 	
	taus		(ms)
} 

BREAKPOINT {
	SOLVE states
	g = gmax*m*m*m*h*s :(1-(1-s)*.5)
	ina = g*(v - ena)
	myi = ina
}
 
UNITSOFF
 
INITIAL {
	trates(v)
	m = minf
	h = hinf
	s = sinf
}

PROCEDURE states() {	:Computes state variables m, h, and n 
	trates(v)			:      at the current v and dt.
	m = m + mexp*(minf-m)
	h = h + hexp*(hinf-h)
	:printf("t=%.2f, s=%.3f, sinf=%.3f, sexp=%.4f\n", t, s, sinf, sexp)
	s = s + sexp*(sinf-s)
}

FUNCTION alpv(v(mV)) {
	alpv = 1/(1+exp((v-vvh-sh)/vvs))
}
        
FUNCTION alps(v(mV)) {  
	alps = exp(1.e-3*zetas*(v-vhalfs-sh)*9.648e4/(8.315*(273.16+celsius)))
}

FUNCTION bets(v(mV)) {
	bets = .2*exp(1.e-3*zetas*gms*(v-vhalfs-sh)*9.648e4/(8.315*(273.16+celsius)))
}
 
LOCAL q10	: declare outside a block so available to whole mechanism
PROCEDURE rates(v) {  :Computes rate and other constants at current v.
                      :Call once from HOC to initialize inf at resting v.
	LOCAL  alpha, beta, c, sum	: only available to block; must be first line in block

	q10 = 3^((celsius - 34)/10)

	:"m" sodium activation system - act and inact cross at -40
	alpha = mAlphC*vtrap((v+mAlphV),-5)
	beta = mBetaC*vtrap((v+mBetaV),5)
	sum = alpha+beta        
	mtau = 1/sum 
	minf = alpha/sum
	
	:"h" sodium inactivation system
	alpha = hAlphC/exp((v+hAlphV)/20)
	beta = hBetaC/(1+exp((v+hBetaV)/-10))
	sum = alpha+beta
	htau = 1/sum 
	hinf = alpha/sum 		
	
	:"s" slow sodium inactivation system
	alpha = sAlphC/exp((v+sAlphV)/6)  : 10
	beta = sBetaC/(1+exp((v+sBetaV)/-20)) : -10
	sum = alpha+beta
	taus = 1/sum 
	sinf = alpha/sum 

	:c=alpv(v)
	:sinf = c+ar2*(1-c)
	:taus = bets(v)/(a0s*(1+alps(v)))
	if (taus<smax) {taus=smax}
}
 
PROCEDURE trates(v) {  :Computes rate and other constants at current v.
                      :Call once from HOC to initialize inf at resting v.
	LOCAL tinc	: only available to block; must be first line in block
	TABLE minf, mexp, hinf, hexp, mtau, htau, sinf, taus, sexp
	DEPEND dt, celsius, mAlphV, mAlphC, mBetaV, mBetaC, hAlphV, hAlphC, hBetaV, hBetaC, sAlphV, sAlphC, sBetaV, sBetaC
	FROM -100 TO 100 WITH 200
                                   
	rates(v)	: not consistently executed from here if usetable_hh == 1
				: so don't expect the tau values to be tracking along with
				: the inf values in hoc

	tinc = -dt * q10

	mexp = 1 - exp(tinc/mtau)
	hexp = 1 - exp(tinc/htau)
	sexp = 1 - exp(tinc/taus)
	:printf("t=%.2f, taus=%.2f, sinf=%.2f\n", t, taus, sinf)
	:if (t>100.0 && t<100.3) {printf("t=%.2f, taus=%.2f, sinf=%.2f\n", t, taus, sinf)}
	:if (t>900.0 && t<900.3) {printf("t=%.2f, taus=%.2f, sinf=%.2f\n", t, taus, sinf)}
}
 
FUNCTION vtrap(x,y) {  :Traps for 0 in denominator of rate eqns.
	if (fabs(x/y) < 1e-6) {
		vtrap = y*(1 - x/y/2)
	}else{  
		vtrap = x/(exp(x/y) - 1)
	}
}
 
UNITSON

