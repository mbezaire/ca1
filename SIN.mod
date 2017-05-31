INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}

NEURON {
  POINT_PROCESS sinstim
  RANGE del, dur, amp, baseamp, i, freq
  NONSPECIFIC_CURRENT i
}

UNITS {
  (nA) = (nanoamp)
  PI  = (pi) (1)
}

PARAMETER {
  freq = 5 (Hz)
  del = 0  (ms)
  dur = 1e10 (ms)
  amp = 0 (nA)
  baseamp = 0 (nA)
}
ASSIGNED { i (nA) }

BREAKPOINT {
  if (t>del && t<dur+del) {
    i = -baseamp - sin(2*PI*freq*(t-del)/1000.)*amp
  } else {
    i = 0.0
  }
}
