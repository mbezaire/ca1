: sgate.mod
: draws from netstim.mod 2212 2008-09-08 14:32:26Z hines
: Passes a fraction of "input" events that arrive while it is on.
: The fraction fluctuates between 1 (100%) and 1-depth (0<=depth<=1)
: and is governed by
:   p(t) = 1 + depth*(cos(2*PI*(t-start)/period) - 1)/2
:   p(t) = 1 + depth*(cos(2*PI*(t-phase)/period) - 1)/2
: where
:   depth = modulation depth (0..1, 1 == pass all, 0 == pass none, 0.5 = pass half)
:   period = duration of a modulation cycle
:   start = time at which modulation begins
: Gate is on for "number" modulation cycles

COMMENT
Supplied (written?) by Ted Carnevale
This mechanism can be combined with a NetStim that has noise=1 
to implement a non-homogeneous Poisson process.
Quoting from http://en.wikipedia.org/wiki/Non-homogeneous_Poisson_process
retrieved on 5/1/2012:
"To simulate a non-homogeneous Poisson process with intensity function λ(t), 
choose a sufficiently large λ so that λ(t) = λ p(t) and simulate a Poisson 
process with rate parameter λ. Accept an event from the Poisson simulation at 
time t with probability p(t)."
This statement cited Ross, Sheldon M. (2006). Simulation. Academic Press. p. 32.
Note:  fifth edition is planned for 11/29/2012
ENDCOMMENT

NEURON  { 
  ARTIFICIAL_CELL SGate : "Stochastic Gate"
  RANGE period, number, start, phase
  RANGE depth, gid, randi
  THREADSAFE : only true if every instance has its own distinct Random
  POINTER donotuse
}

UNITS {
  PI = (pi) (1)
}

PARAMETER {
  period = 100 (ms) <1e-9,1e9>: duration of a modulation cycle (msec)
  number = 1 <0,1e9> : number of modulation cycles
  start = 50 (ms) : start of first cycle
  depth = 0 <0,1> : modulation depth
  phase = 0 (ms): peak of first cycle
	gid = 0
	randi = 0
}

ASSIGNED {
  on (1)
  donotuse
  numtogo (1) : how many modulation cycles remain to be launched
  r (1)
}

INITIAL {
  if (period < 0) { period = 1e9 }
  if (number < 0) { number = 0 }
  if (start < 0) { start = 0 }
  if (phase < 0) { phase = 0 }
  if (depth < 0) { depth = 0 }
  if (depth > 1) { depth = 1 }

  on = 0 : off--no events pass
  if (number > 0) {
    numtogo = number
    net_send(start, 1) : to turn gate on
  }
}  

PROCEDURE seed(x) {
  set_seed(x)
}

VERBATIM
double nrn_random_pick(void* r);
void* nrn_random_arg(int argpos);
ENDVERBATIM

FUNCTION erand() {
VERBATIM
  if (_p_donotuse) {
    /*
    :Supports separate independent but reproducible streams for
    : each instance. However, the corresponding hoc Random
    : distribution MUST be set to Random.uniform(0,1)
    */
    _lerand = nrn_random_pick(_p_donotuse);
  }else{
    /* only can be used in main thread */
    if (_nt != nrn_threads) {
hoc_execerror("multithread random in NetStim"," only via hoc Random");
    }
ENDVERBATIM
    : the old standby. Cannot use if reproducible parallel sim
    : independent of nhost or which host this instance is on
    : is desired, since each instance on this cpu draws from
    : the same stream
    erand = scop_random()
VERBATIM
  }
ENDVERBATIM
}

PROCEDURE noiseFromRandom() {
VERBATIM
 {
  void** pv = (void**)(&_p_donotuse);
  if (ifarg(1)) {
    *pv = nrn_random_arg(1);
  }else{
    *pv = (void*)0;
  }
 }
ENDVERBATIM
}

:   p(t) = 1 + depth*(cos(2*PI*(t-phase)/period) - 1)/2

FUNCTION p(t (ms)) {
  p = 0
  if (on == 1) {
    p = 1 + depth*(cos(2*PI*(t-phase)/period) - 1)/2
  }
}

: flag  action
: 0     if ON, decide whether to pass event
: 1     decide whether to start a modulation cycle
NET_RECEIVE (w) {
  if (flag == 0) { : external event
    if (on == 1) {
      : decide whether to pass this event
        r = erand()
        if (r < p(t)) { net_event(t) }
    }
  } else if (flag == 1) {
    if (numtogo>0) { : launch a new cycle
      on = 1
      numtogo = numtogo-1
      net_send(period, 1) : to end this cycle
    } else { : all done
      on = 0
    }
  }
}
