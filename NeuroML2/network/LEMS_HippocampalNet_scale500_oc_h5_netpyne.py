'''
NETPYNE simulator compliant export for:

Components:
    null (Type: notes)
    null (Type: property)
    null (Type: notes)
    CavL (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    CavN (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KCaS (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Kdrfast (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KvA (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KvCaB (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Nav (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    leak_chan (Type: ionChannelPassive:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    fixedCapool (Type: FixedCaConcentrationModel)
    Capool (Type: BezaireCaConcentrationModel:  restingConc=5.0E-5 (SI concentration) decayConstant=0.009000000000000001 (SI time) shellThickness=2.0E-7 (SI length) Faraday=96520.0 (SI charge_per_mole))
    Capoolngf (Type: BezaireCaConcentrationModel:  restingConc=5.0E-6 (SI concentration) decayConstant=0.01 (SI time) shellThickness=2.0E-7 (SI length) Faraday=96520.0 (SI charge_per_mole))
    axoaxoniccell (Type: cell)
    null (Type: notes)
    Navbis (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    bistratifiedcell (Type: cell)
    null (Type: notes)
    HCN (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KvGroup (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Navcck (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    cckcell (Type: cell)
    null (Type: notes)
    Kdrfastngf (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KvAngf (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Navngf (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    ivycell (Type: cell)
    ngfcell (Type: cell)
    null (Type: notes)
    HCNolm (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KvAolm (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    olmcell (Type: cell)
    null (Type: notes)
    HCNp (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    HCNsomap (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Kdrp (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KvAproxp (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KvAdistp (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Navp (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    Navapicalp (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Navaxonp (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    poolosyncell (Type: cell)
    pvbasketcell (Type: cell)
    scacell (Type: cell)
    syn_cck_to_bistratified (Type: expTwoSynapse:  tauRise=4.32E-4 (SI time) tauDecay=0.00449 (SI time) peakTime=0.0011190597986863605 (SI time) waveformFactor=1.4196299918241655 (dimensionless) gbase=7.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ca3_to_poolosyn (Type: expTwoSynapse:  tauRise=5.0E-4 (SI time) tauDecay=0.003 (SI time) peakTime=0.0010750556815368332 (SI time) waveformFactor=1.7171628973263067 (dimensionless) gbase=2.0000000000000003E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_sca_to_pvbasket (Type: expTwoSynapse:  tauRise=4.19E-4 (SI time) tauDecay=0.0049900000000000005 (SI time) peakTime=0.0011331450429356179 (SI time) waveformFactor=1.3699675937330524 (dimensionless) gbase=1.3E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_ec_to_ngf (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=3.5000000000000003E-9 (SI conductance) erev=0.0 (SI voltage))
    syn_ca3_to_bistratified (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=1.5E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_bistratified_to_olm (Type: expTwoSynapse:  tauRise=0.001 (SI time) tauDecay=0.008 (SI time) peakTime=0.002376504619062669 (SI time) waveformFactor=1.5381716487226926 (dimensionless) gbase=2.0000000000000002E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_sca_to_sca (Type: expTwoSynapse:  tauRise=2.0E-4 (SI time) tauDecay=0.002 (SI time) peakTime=5.116855762208991E-4 (SI time) waveformFactor=1.435055183349871 (dimensionless) gbase=1.0E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_ivy_to_axoaxonic (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=5.7000000000000003E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_ivy_to_ivy (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=5.7000000000000003E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_poolosyn_to_sca (Type: expTwoSynapse:  tauRise=3.0E-4 (SI time) tauDecay=6.0E-4 (SI time) peakTime=4.158883083359671E-4 (SI time) waveformFactor=4.0 (dimensionless) gbase=4.0500000000000005E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_bistratified_to_axoaxonic (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=6.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_cck_to_cck (Type: expTwoSynapse:  tauRise=4.32E-4 (SI time) tauDecay=0.00449 (SI time) peakTime=0.0011190597986863605 (SI time) waveformFactor=1.4196299918241655 (dimensionless) gbase=4.5000000000000005E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ivy_to_bistratified (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=7.7E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_cck_to_ivy (Type: expTwoSynapse:  tauRise=4.32E-4 (SI time) tauDecay=0.00449 (SI time) peakTime=0.0011190597986863605 (SI time) waveformFactor=1.4196299918241655 (dimensionless) gbase=3.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ca3_to_ivy (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=3.0E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_ivy_to_cck (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=3.7E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_pvbasket_to_bistratified (Type: expTwoSynapse:  tauRise=1.7999999999999998E-4 (SI time) tauDecay=4.5000000000000004E-4 (SI time) peakTime=2.748872195622465E-4 (SI time) waveformFactor=3.0700262488669883 (dimensionless) gbase=2.9E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_bistratified_to_bistratified (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=5.1E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_pvbasket_to_poolosyn (Type: expTwoSynapse:  tauRise=3.0E-4 (SI time) tauDecay=0.006200000000000001 (SI time) peakTime=9.547544236035908E-4 (SI time) waveformFactor=1.225794971825537 (dimensionless) gbase=2.0000000000000003E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_olm_to_cck (Type: expTwoSynapse:  tauRise=7.28E-4 (SI time) tauDecay=0.0202 (SI time) peakTime=0.0025096919188377386 (SI time) waveformFactor=1.1746229968441386 (dimensionless) gbase=1.2E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_pvbasket_to_pvbasket (Type: expTwoSynapse:  tauRise=8.0E-5 (SI time) tauDecay=0.0048 (SI time) peakTime=3.3309921862145905E-4 (SI time) waveformFactor=1.0900273513005547 (dimensionless) gbase=1.6000000000000003E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_ec_to_cck (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=6.5E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_bistratified_to_cck (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=8.000000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ngf_to_poolosyn_A (Type: expTwoSynapse:  tauRise=0.009000000000000001 (SI time) tauDecay=0.039 (SI time) peakTime=0.017156143704883095 (SI time) waveformFactor=2.018319804023249 (dimensionless) gbase=6.500000000000001E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_ngf_to_poolosyn_B (Type: expTwoSynapse:  tauRise=0.18 (SI time) tauDecay=0.2 (SI time) peakTime=0.18964892818408724 (SI time) waveformFactor=25.811747917131978 (dimensionless) gbase=1.9288E-11 (SI conductance) erev=-0.09 (SI voltage))
    syn_ivy_to_sca (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=3.7E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_olm_to_olm (Type: expTwoSynapse:  tauRise=2.5E-4 (SI time) tauDecay=0.0075 (SI time) peakTime=8.796200124988334E-4 (SI time) waveformFactor=1.1632109250720026 (dimensionless) gbase=1.2E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_poolosyn_to_bistratified (Type: expTwoSynapse:  tauRise=1.1E-4 (SI time) tauDecay=2.5E-4 (SI time) peakTime=1.6126403701371666E-4 (SI time) waveformFactor=3.4037393745369364 (dimensionless) gbase=1.9E-9 (SI conductance) erev=0.0 (SI voltage))
    syn_olm_to_poolosyn (Type: expTwoSynapse:  tauRise=1.3000000000000002E-4 (SI time) tauDecay=0.011 (SI time) peakTime=5.83855200082304E-4 (SI time) waveformFactor=1.0671230800079607 (dimensionless) gbase=3.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ivy_to_olm (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=5.7000000000000003E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_pvbasket_to_sca (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=6.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_poolosyn_to_axoaxonic (Type: expTwoSynapse:  tauRise=3.0E-4 (SI time) tauDecay=6.0E-4 (SI time) peakTime=4.158883083359671E-4 (SI time) waveformFactor=4.0 (dimensionless) gbase=4.0000000000000004E-11 (SI conductance) erev=0.0 (SI voltage))
    syn_bistratified_to_ivy (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=5.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_poolosyn_to_ivy (Type: expTwoSynapse:  tauRise=3.0E-4 (SI time) tauDecay=6.0E-4 (SI time) peakTime=4.158883083359671E-4 (SI time) waveformFactor=4.0 (dimensionless) gbase=4.0500000000000005E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_ec_to_sca (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=4.5000000000000005E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_cck_to_pvbasket (Type: expTwoSynapse:  tauRise=4.32E-4 (SI time) tauDecay=0.00449 (SI time) peakTime=0.0011190597986863605 (SI time) waveformFactor=1.4196299918241655 (dimensionless) gbase=9.000000000000001E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_olm_to_axoaxonic (Type: expTwoSynapse:  tauRise=7.28E-4 (SI time) tauDecay=0.01 (SI time) peakTime=0.00205714908079322 (SI time) waveformFactor=1.3248521854125708 (dimensionless) gbase=1.2E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_axoaxonic_to_poolosyn (Type: expTwoSynapse:  tauRise=2.8000000000000003E-4 (SI time) tauDecay=0.008400000000000001 (SI time) peakTime=9.851744139986935E-4 (SI time) waveformFactor=1.1632109250720026 (dimensionless) gbase=1.15E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_bistratified_to_poolosyn (Type: expTwoSynapse:  tauRise=1.1E-4 (SI time) tauDecay=0.0097 (SI time) peakTime=4.983858865705835E-4 (SI time) waveformFactor=1.0647978670176388 (dimensionless) gbase=5.1E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_sca_to_ivy (Type: expTwoSynapse:  tauRise=4.19E-4 (SI time) tauDecay=0.0049900000000000005 (SI time) peakTime=0.0011331450429356179 (SI time) waveformFactor=1.3699675937330524 (dimensionless) gbase=8.500000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ca3_to_pvbasket (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=2.2000000000000002E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_pvbasket_to_cck (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=1.2E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_ivy_to_ngf (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=5.7000000000000003E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_ec_to_axoaxonic (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=1.2E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_olm_to_ngf (Type: expTwoSynapse:  tauRise=0.0013000000000000002 (SI time) tauDecay=0.010199999999999999 (SI time) peakTime=0.0030692034858662313 (SI time) waveformFactor=1.548425713511671 (dimensionless) gbase=9.800000000000001E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_cck_to_poolosyn (Type: expTwoSynapse:  tauRise=2.0E-4 (SI time) tauDecay=0.004200000000000001 (SI time) peakTime=6.393497119219188E-4 (SI time) waveformFactor=1.2226446837204854 (dimensionless) gbase=5.200000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_olm_to_sca (Type: expTwoSynapse:  tauRise=7.000000000000001E-5 (SI time) tauDecay=0.029 (SI time) peakTime=4.2287965467839903E-4 (SI time) waveformFactor=1.0171440692602471 (dimensionless) gbase=1.5E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_sca_to_cck (Type: expTwoSynapse:  tauRise=4.19E-4 (SI time) tauDecay=0.0049900000000000005 (SI time) peakTime=0.0011331450429356179 (SI time) waveformFactor=1.3699675937330524 (dimensionless) gbase=8.500000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_cck_to_olm (Type: expTwoSynapse:  tauRise=0.001 (SI time) tauDecay=0.008 (SI time) peakTime=0.002376504619062669 (SI time) waveformFactor=1.5381716487226926 (dimensionless) gbase=7.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ca3_to_sca (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=3.0E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_ivy_to_poolosyn (Type: expTwoSynapse:  tauRise=0.0011 (SI time) tauDecay=0.011 (SI time) peakTime=0.0028142706692149445 (SI time) waveformFactor=1.435055183349871 (dimensionless) gbase=4.100000000000001E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_cck_to_axoaxonic (Type: expTwoSynapse:  tauRise=4.32E-4 (SI time) tauDecay=0.00449 (SI time) peakTime=0.0011190597986863605 (SI time) waveformFactor=1.4196299918241655 (dimensionless) gbase=7.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ngf_to_ngf_A (Type: expTwoSynapse:  tauRise=0.0031000000000000003 (SI time) tauDecay=0.042 (SI time) peakTime=0.008723291243813708 (SI time) waveformFactor=1.3289282339374142 (dimensionless) gbase=1.6000000000000002E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ngf_to_ngf_B (Type: expTwoSynapse:  tauRise=0.18 (SI time) tauDecay=0.2 (SI time) peakTime=0.18964892818408724 (SI time) waveformFactor=25.811747917131978 (dimensionless) gbase=4.7478E-11 (SI conductance) erev=-0.09 (SI voltage))
    syn_ca3_to_axoaxonic (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=1.2E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_sca_to_axoaxonic (Type: expTwoSynapse:  tauRise=4.19E-4 (SI time) tauDecay=0.0049900000000000005 (SI time) peakTime=0.0011331450429356179 (SI time) waveformFactor=1.3699675937330524 (dimensionless) gbase=6.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_cck_to_sca (Type: expTwoSynapse:  tauRise=4.32E-4 (SI time) tauDecay=0.00449 (SI time) peakTime=0.0011190597986863605 (SI time) waveformFactor=1.4196299918241655 (dimensionless) gbase=7.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_olm_to_pvbasket (Type: expTwoSynapse:  tauRise=2.5E-4 (SI time) tauDecay=0.0075 (SI time) peakTime=8.796200124988334E-4 (SI time) waveformFactor=1.1632109250720026 (dimensionless) gbase=1.1000000000000001E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_sca_to_poolosyn (Type: expTwoSynapse:  tauRise=1.5E-4 (SI time) tauDecay=0.0039 (SI time) peakTime=5.082630599313511E-4 (SI time) waveformFactor=1.1847651563769113 (dimensionless) gbase=7.600000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_poolosyn_to_pvbasket (Type: expTwoSynapse:  tauRise=7.000000000000001E-5 (SI time) tauDecay=2.0E-4 (SI time) peakTime=1.1305776725370377E-4 (SI time) waveformFactor=2.707624689928131 (dimensionless) gbase=7.0E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_ec_to_poolosyn (Type: expTwoSynapse:  tauRise=5.0E-4 (SI time) tauDecay=0.003 (SI time) peakTime=0.0010750556815368332 (SI time) waveformFactor=1.7171628973263067 (dimensionless) gbase=2.0000000000000003E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_sca_to_olm (Type: expTwoSynapse:  tauRise=0.001 (SI time) tauDecay=0.008 (SI time) peakTime=0.002376504619062669 (SI time) waveformFactor=1.5381716487226926 (dimensionless) gbase=8.500000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_poolosyn_to_poolosyn (Type: expTwoSynapse:  tauRise=1.0E-4 (SI time) tauDecay=0.0015 (SI time) peakTime=2.901482358323797E-4 (SI time) waveformFactor=1.3000789959133998 (dimensionless) gbase=7.0E-8 (SI conductance) erev=0.0 (SI voltage))
    syn_bistratified_to_sca (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=8.000000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ec_to_bistratified (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=1.5E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_bistratified_to_pvbasket (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=9.000000000000001E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_olm_to_bistratified (Type: expTwoSynapse:  tauRise=6.0E-4 (SI time) tauDecay=0.015 (SI time) peakTime=0.002011797390542625 (SI time) waveformFactor=1.1911769125863754 (dimensionless) gbase=1.1000000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ca3_to_cck (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=6.5E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_pvbasket_to_ivy (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=1.6000000000000002E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_pvbasket_to_axoaxonic (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=1.2E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_sca_to_bistratified (Type: expTwoSynapse:  tauRise=4.19E-4 (SI time) tauDecay=0.0049900000000000005 (SI time) peakTime=0.0011331450429356179 (SI time) waveformFactor=1.3699675937330524 (dimensionless) gbase=6.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ivy_to_pvbasket (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=7.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_poolosyn_to_olm (Type: expTwoSynapse:  tauRise=3.0E-4 (SI time) tauDecay=6.0E-4 (SI time) peakTime=4.158883083359671E-4 (SI time) waveformFactor=4.0 (dimensionless) gbase=2.0000000000000003E-10 (SI conductance) erev=0.0 (SI voltage))
    stim_ec (Type: SpikeSourcePoisson:  start=0.0 (SI time) duration=0.5 (SI time) rate=0.65 (SI per_time) end=0.5 (SI time) LONG_TIME=3.6E12 (SI time))
    stim_ca3 (Type: SpikeSourcePoisson:  start=0.0 (SI time) duration=0.5 (SI time) rate=0.65 (SI per_time) end=0.5 (SI time) LONG_TIME=3.6E12 (SI time))
    HippocampalNet_scale500_oc (Type: networkWithTemperature:  temperature=307.15 (SI temperature))
    Sim_HippocampalNet_scale500_oc (Type: Simulation:  length=0.5 (SI time) step=1.0E-5 (SI time))


    This NETPYNE file has been generated by org.neuroml.export (see https://github.com/NeuroML/org.neuroml.export)
         org.neuroml.export  v1.5.3
         org.neuroml.model   v1.5.3
         jLEMS               v0.9.9.0

'''
# Main NetPyNE script for: HippocampalNet_scale500_oc

# See https://github.com/Neurosim-lab/netpyne

from netpyne import specs  # import netpyne specs module
from netpyne import sim    # import netpyne sim module

from neuron import h

import sys


###############################################################################
# NETWORK PARAMETERS
###############################################################################

nml2_file_name = 'HippocampalNet_scale500_oc.net.nml.h5'

###############################################################################
# SIMULATION PARAMETERS
###############################################################################

simConfig = specs.SimConfig()   # object of class SimConfig to store the simulation configuration

# Simulation parameters
simConfig.duration = simConfig.tstop = 500.0 # Duration of the simulation, in ms
simConfig.dt = 0.01 # Internal integration timestep to use

# Seeds for randomizers (connectivity, input stimulation and cell locations)
# Note: locations and connections should be fully specified by the structure of the NeuroML,
# so seeds for conn & loc shouldn't affect networks structure/behaviour
simConfig.seeds = {'conn': 0, 'stim': 12345, 'loc': 0} 

simConfig.createNEURONObj = 1  # create HOC objects when instantiating network
simConfig.createPyStruct = 1  # create Python structure (simulator-independent) when instantiating network
simConfig.verbose = False  # show detailed messages 
simConfig.hParams['celsius'] = (307.15 - 273.15)

# Recording 
simConfig.recordCells = ['all']  
simConfig.recordTraces = {}

# For saving to file: Sim_HippocampalNet_scale500_oc.ivycell.v.dat (ref: Sim_HippocampalNet_scale500_oc_ivycell_v_dat)
# Column: pop_ivy_0_ivycell_v: Pop: pop_ivy; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_ivy','cellLabel':0}}
# Column: pop_ivy_1_ivycell_v: Pop: pop_ivy; cell: 1; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_1_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_ivy','cellLabel':1}}
# Column: pop_ivy_2_ivycell_v: Pop: pop_ivy; cell: 2; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_2_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_ivy','cellLabel':2}}
# Column: pop_ivy_3_ivycell_v: Pop: pop_ivy; cell: 3; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_3_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_ivy','cellLabel':3}}
# Column: pop_ivy_4_ivycell_v: Pop: pop_ivy; cell: 4; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_4_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_ivy','cellLabel':4}}
# For saving to file: Sim_HippocampalNet_scale500_oc.cckcell.v.dat (ref: Sim_HippocampalNet_scale500_oc_cckcell_v_dat)
# Column: pop_cck_0_cckcell_v: Pop: pop_cck; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_cck','cellLabel':0}}
# Column: pop_cck_1_cckcell_v: Pop: pop_cck; cell: 1; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_1_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_cck','cellLabel':1}}
# Column: pop_cck_2_cckcell_v: Pop: pop_cck; cell: 2; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_2_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_cck','cellLabel':2}}
# Column: pop_cck_3_cckcell_v: Pop: pop_cck; cell: 3; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_3_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_cck','cellLabel':3}}
# Column: pop_cck_4_cckcell_v: Pop: pop_cck; cell: 4; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_4_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_cck','cellLabel':4}}
# For saving to file: Sim_HippocampalNet_scale500_oc.poolosyncell.v.dat (ref: Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat)
# Column: pop_poolosyn_0_poolosyncell_v: Pop: pop_poolosyn; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_poolosyn','cellLabel':0}}
# Column: pop_poolosyn_1_poolosyncell_v: Pop: pop_poolosyn; cell: 1; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_1_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_poolosyn','cellLabel':1}}
# Column: pop_poolosyn_2_poolosyncell_v: Pop: pop_poolosyn; cell: 2; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_2_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_poolosyn','cellLabel':2}}
# Column: pop_poolosyn_3_poolosyncell_v: Pop: pop_poolosyn; cell: 3; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_3_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_poolosyn','cellLabel':3}}
# Column: pop_poolosyn_4_poolosyncell_v: Pop: pop_poolosyn; cell: 4; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_4_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_poolosyn','cellLabel':4}}
# For saving to file: Sim_HippocampalNet_scale500_oc.pvbasketcell.v.dat (ref: Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat)
# Column: pop_pvbasket_0_pvbasketcell_v: Pop: pop_pvbasket; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_pvbasket','cellLabel':0}}
# Column: pop_pvbasket_1_pvbasketcell_v: Pop: pop_pvbasket; cell: 1; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_1_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_pvbasket','cellLabel':1}}
# Column: pop_pvbasket_2_pvbasketcell_v: Pop: pop_pvbasket; cell: 2; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_2_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_pvbasket','cellLabel':2}}
# Column: pop_pvbasket_3_pvbasketcell_v: Pop: pop_pvbasket; cell: 3; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_3_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_pvbasket','cellLabel':3}}
# Column: pop_pvbasket_4_pvbasketcell_v: Pop: pop_pvbasket; cell: 4; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_4_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_pvbasket','cellLabel':4}}
# For saving to file: Sim_HippocampalNet_scale500_oc.scacell.v.dat (ref: Sim_HippocampalNet_scale500_oc_scacell_v_dat)
# Column: pop_sca_0_scacell_v: Pop: pop_sca; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_scacell_v_dat_pop_sca_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_sca','cellLabel':0}}
# For saving to file: Sim_HippocampalNet_scale500_oc.ngfcell.v.dat (ref: Sim_HippocampalNet_scale500_oc_ngfcell_v_dat)
# Column: pop_ngf_0_ngfcell_v: Pop: pop_ngf; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_ngf','cellLabel':0}}
# Column: pop_ngf_1_ngfcell_v: Pop: pop_ngf; cell: 1; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_1_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_ngf','cellLabel':1}}
# Column: pop_ngf_2_ngfcell_v: Pop: pop_ngf; cell: 2; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_2_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_ngf','cellLabel':2}}
# Column: pop_ngf_3_ngfcell_v: Pop: pop_ngf; cell: 3; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_3_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_ngf','cellLabel':3}}
# Column: pop_ngf_4_ngfcell_v: Pop: pop_ngf; cell: 4; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_4_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_ngf','cellLabel':4}}
# For saving to file: Sim_HippocampalNet_scale500_oc.axoaxoniccell.v.dat (ref: Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat)
# Column: pop_axoaxonic_0_axoaxoniccell_v: Pop: pop_axoaxonic; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat_pop_axoaxonic_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_axoaxonic','cellLabel':0}}
# Column: pop_axoaxonic_1_axoaxoniccell_v: Pop: pop_axoaxonic; cell: 1; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat_pop_axoaxonic_1_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_axoaxonic','cellLabel':1}}
# For saving to file: Sim_HippocampalNet_scale500_oc.bistratifiedcell.v.dat (ref: Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat)
# Column: pop_bistratified_0_bistratifiedcell_v: Pop: pop_bistratified; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_bistratified','cellLabel':0}}
# Column: pop_bistratified_1_bistratifiedcell_v: Pop: pop_bistratified; cell: 1; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_1_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_bistratified','cellLabel':1}}
# Column: pop_bistratified_2_bistratifiedcell_v: Pop: pop_bistratified; cell: 2; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_2_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_bistratified','cellLabel':2}}
# Column: pop_bistratified_3_bistratifiedcell_v: Pop: pop_bistratified; cell: 3; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_3_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_bistratified','cellLabel':3}}
# For saving to file: Sim_HippocampalNet_scale500_oc.olmcell.v.dat (ref: Sim_HippocampalNet_scale500_oc_olmcell_v_dat)
# Column: pop_olm_0_olmcell_v: Pop: pop_olm; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_olmcell_v_dat_pop_olm_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_olm','cellLabel':0}}
# Column: pop_olm_1_olmcell_v: Pop: pop_olm; cell: 1; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_olmcell_v_dat_pop_olm_1_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_olm','cellLabel':1}}
# Column: pop_olm_2_olmcell_v: Pop: pop_olm; cell: 2; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['Sim_HippocampalNet_scale500_oc_olmcell_v_dat_pop_olm_2_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_olm','cellLabel':2}}


simConfig.plotCells = ['all']


simConfig.recordStim = True  # record spikes of cell stims
simConfig.recordStep = simConfig.dt # Step size in ms to save data (eg. V traces, LFP, etc)



# Analysis and plotting, see http://neurosimlab.org/netpyne/reference.html#analysis-related-functions
simConfig.analysis['plotRaster'] = False  # Plot raster
simConfig.analysis['plot2Dnet'] = False  # Plot 2D net cells and connections
simConfig.analysis['plotSpikeHist'] = False # plot spike histogram
simConfig.analysis['plotConn'] = False # plot network connectivity
simConfig.analysis['plotSpikePSD'] = False # plot 3d architecture
simConfig.analysis['plotShape'] = False # plot shape in Neuron

# Saving
simConfig.filename = 'HippocampalNet_scale500_oc.txt'  # Set file output name
simConfig.saveFileStep = simConfig.dt # step size in ms to save data to disk
# simConfig.saveDat = True # save to dat file


###############################################################################
# IMPORT & RUN
###############################################################################

print("Running a NetPyNE based simulation for %sms (dt: %sms) at %s degC"%(simConfig.duration, simConfig.dt, h.celsius))

gids = sim.importNeuroML2SimulateAnalyze(nml2_file_name,simConfig)

print("Finished simulation")


###############################################################################
#   Saving data (this ensures the data gets saved in the format/files 
#   as specified in the LEMS <Simulation> element)
###############################################################################


if sim.rank==0: 
    print("Saving traces to file: Sim_HippocampalNet_scale500_oc.ivycell.v.dat (ref: Sim_HippocampalNet_scale500_oc_ivycell_v_dat)")

 
    # Column: t
    col_Sim_HippocampalNet_scale500_oc_ivycell_v_dat_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: pop_ivy_0_ivycell_v: Pop: pop_ivy; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_0_ivycell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_0_Seg0_soma_0_v']['cell_%s'%gids['pop_ivy'][0]]

    # Column: pop_ivy_1_ivycell_v: Pop: pop_ivy; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_1_ivycell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_1_Seg0_soma_0_v']['cell_%s'%gids['pop_ivy'][1]]

    # Column: pop_ivy_2_ivycell_v: Pop: pop_ivy; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_2_ivycell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_2_Seg0_soma_0_v']['cell_%s'%gids['pop_ivy'][2]]

    # Column: pop_ivy_3_ivycell_v: Pop: pop_ivy; cell: 3; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_3_ivycell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_3_Seg0_soma_0_v']['cell_%s'%gids['pop_ivy'][3]]

    # Column: pop_ivy_4_ivycell_v: Pop: pop_ivy; cell: 4; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_4_ivycell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_4_Seg0_soma_0_v']['cell_%s'%gids['pop_ivy'][4]]

    dat_file_Sim_HippocampalNet_scale500_oc_ivycell_v_dat = open('Sim_HippocampalNet_scale500_oc.ivycell.v.dat', 'w')
    for i in range(len(col_Sim_HippocampalNet_scale500_oc_ivycell_v_dat_t)):
        dat_file_Sim_HippocampalNet_scale500_oc_ivycell_v_dat.write( '%s\t'%(col_Sim_HippocampalNet_scale500_oc_ivycell_v_dat_t[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_0_ivycell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_1_ivycell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_2_ivycell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_3_ivycell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_ivycell_v_dat_pop_ivy_4_ivycell_v[i]/1000.0) +  '\n')
    dat_file_Sim_HippocampalNet_scale500_oc_ivycell_v_dat.close()

    print("Saving traces to file: Sim_HippocampalNet_scale500_oc.cckcell.v.dat (ref: Sim_HippocampalNet_scale500_oc_cckcell_v_dat)")

 
    # Column: t
    col_Sim_HippocampalNet_scale500_oc_cckcell_v_dat_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: pop_cck_0_cckcell_v: Pop: pop_cck; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_0_cckcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_0_Seg0_soma_0_v']['cell_%s'%gids['pop_cck'][0]]

    # Column: pop_cck_1_cckcell_v: Pop: pop_cck; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_1_cckcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_1_Seg0_soma_0_v']['cell_%s'%gids['pop_cck'][1]]

    # Column: pop_cck_2_cckcell_v: Pop: pop_cck; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_2_cckcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_2_Seg0_soma_0_v']['cell_%s'%gids['pop_cck'][2]]

    # Column: pop_cck_3_cckcell_v: Pop: pop_cck; cell: 3; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_3_cckcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_3_Seg0_soma_0_v']['cell_%s'%gids['pop_cck'][3]]

    # Column: pop_cck_4_cckcell_v: Pop: pop_cck; cell: 4; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_4_cckcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_4_Seg0_soma_0_v']['cell_%s'%gids['pop_cck'][4]]

    dat_file_Sim_HippocampalNet_scale500_oc_cckcell_v_dat = open('Sim_HippocampalNet_scale500_oc.cckcell.v.dat', 'w')
    for i in range(len(col_Sim_HippocampalNet_scale500_oc_cckcell_v_dat_t)):
        dat_file_Sim_HippocampalNet_scale500_oc_cckcell_v_dat.write( '%s\t'%(col_Sim_HippocampalNet_scale500_oc_cckcell_v_dat_t[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_0_cckcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_1_cckcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_2_cckcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_3_cckcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_cckcell_v_dat_pop_cck_4_cckcell_v[i]/1000.0) +  '\n')
    dat_file_Sim_HippocampalNet_scale500_oc_cckcell_v_dat.close()

    print("Saving traces to file: Sim_HippocampalNet_scale500_oc.poolosyncell.v.dat (ref: Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat)")

 
    # Column: t
    col_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: pop_poolosyn_0_poolosyncell_v: Pop: pop_poolosyn; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_0_poolosyncell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_0_Seg0_soma_0_v']['cell_%s'%gids['pop_poolosyn'][0]]

    # Column: pop_poolosyn_1_poolosyncell_v: Pop: pop_poolosyn; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_1_poolosyncell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_1_Seg0_soma_0_v']['cell_%s'%gids['pop_poolosyn'][1]]

    # Column: pop_poolosyn_2_poolosyncell_v: Pop: pop_poolosyn; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_2_poolosyncell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_2_Seg0_soma_0_v']['cell_%s'%gids['pop_poolosyn'][2]]

    # Column: pop_poolosyn_3_poolosyncell_v: Pop: pop_poolosyn; cell: 3; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_3_poolosyncell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_3_Seg0_soma_0_v']['cell_%s'%gids['pop_poolosyn'][3]]

    # Column: pop_poolosyn_4_poolosyncell_v: Pop: pop_poolosyn; cell: 4; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_4_poolosyncell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_4_Seg0_soma_0_v']['cell_%s'%gids['pop_poolosyn'][4]]

    dat_file_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat = open('Sim_HippocampalNet_scale500_oc.poolosyncell.v.dat', 'w')
    for i in range(len(col_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_t)):
        dat_file_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat.write( '%s\t'%(col_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_t[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_0_poolosyncell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_1_poolosyncell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_2_poolosyncell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_3_poolosyncell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat_pop_poolosyn_4_poolosyncell_v[i]/1000.0) +  '\n')
    dat_file_Sim_HippocampalNet_scale500_oc_poolosyncell_v_dat.close()

    print("Saving traces to file: Sim_HippocampalNet_scale500_oc.pvbasketcell.v.dat (ref: Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat)")

 
    # Column: t
    col_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: pop_pvbasket_0_pvbasketcell_v: Pop: pop_pvbasket; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_0_pvbasketcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_0_Seg0_soma_0_v']['cell_%s'%gids['pop_pvbasket'][0]]

    # Column: pop_pvbasket_1_pvbasketcell_v: Pop: pop_pvbasket; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_1_pvbasketcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_1_Seg0_soma_0_v']['cell_%s'%gids['pop_pvbasket'][1]]

    # Column: pop_pvbasket_2_pvbasketcell_v: Pop: pop_pvbasket; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_2_pvbasketcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_2_Seg0_soma_0_v']['cell_%s'%gids['pop_pvbasket'][2]]

    # Column: pop_pvbasket_3_pvbasketcell_v: Pop: pop_pvbasket; cell: 3; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_3_pvbasketcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_3_Seg0_soma_0_v']['cell_%s'%gids['pop_pvbasket'][3]]

    # Column: pop_pvbasket_4_pvbasketcell_v: Pop: pop_pvbasket; cell: 4; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_4_pvbasketcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_4_Seg0_soma_0_v']['cell_%s'%gids['pop_pvbasket'][4]]

    dat_file_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat = open('Sim_HippocampalNet_scale500_oc.pvbasketcell.v.dat', 'w')
    for i in range(len(col_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_t)):
        dat_file_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat.write( '%s\t'%(col_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_t[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_0_pvbasketcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_1_pvbasketcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_2_pvbasketcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_3_pvbasketcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat_pop_pvbasket_4_pvbasketcell_v[i]/1000.0) +  '\n')
    dat_file_Sim_HippocampalNet_scale500_oc_pvbasketcell_v_dat.close()

    print("Saving traces to file: Sim_HippocampalNet_scale500_oc.scacell.v.dat (ref: Sim_HippocampalNet_scale500_oc_scacell_v_dat)")

 
    # Column: t
    col_Sim_HippocampalNet_scale500_oc_scacell_v_dat_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: pop_sca_0_scacell_v: Pop: pop_sca; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_scacell_v_dat_pop_sca_0_scacell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_scacell_v_dat_pop_sca_0_Seg0_soma_0_v']['cell_%s'%gids['pop_sca'][0]]

    dat_file_Sim_HippocampalNet_scale500_oc_scacell_v_dat = open('Sim_HippocampalNet_scale500_oc.scacell.v.dat', 'w')
    for i in range(len(col_Sim_HippocampalNet_scale500_oc_scacell_v_dat_t)):
        dat_file_Sim_HippocampalNet_scale500_oc_scacell_v_dat.write( '%s\t'%(col_Sim_HippocampalNet_scale500_oc_scacell_v_dat_t[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_scacell_v_dat_pop_sca_0_scacell_v[i]/1000.0) +  '\n')
    dat_file_Sim_HippocampalNet_scale500_oc_scacell_v_dat.close()

    print("Saving traces to file: Sim_HippocampalNet_scale500_oc.ngfcell.v.dat (ref: Sim_HippocampalNet_scale500_oc_ngfcell_v_dat)")

 
    # Column: t
    col_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: pop_ngf_0_ngfcell_v: Pop: pop_ngf; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_0_ngfcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_0_Seg0_soma_0_v']['cell_%s'%gids['pop_ngf'][0]]

    # Column: pop_ngf_1_ngfcell_v: Pop: pop_ngf; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_1_ngfcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_1_Seg0_soma_0_v']['cell_%s'%gids['pop_ngf'][1]]

    # Column: pop_ngf_2_ngfcell_v: Pop: pop_ngf; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_2_ngfcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_2_Seg0_soma_0_v']['cell_%s'%gids['pop_ngf'][2]]

    # Column: pop_ngf_3_ngfcell_v: Pop: pop_ngf; cell: 3; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_3_ngfcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_3_Seg0_soma_0_v']['cell_%s'%gids['pop_ngf'][3]]

    # Column: pop_ngf_4_ngfcell_v: Pop: pop_ngf; cell: 4; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_4_ngfcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_4_Seg0_soma_0_v']['cell_%s'%gids['pop_ngf'][4]]

    dat_file_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat = open('Sim_HippocampalNet_scale500_oc.ngfcell.v.dat', 'w')
    for i in range(len(col_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_t)):
        dat_file_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat.write( '%s\t'%(col_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_t[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_0_ngfcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_1_ngfcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_2_ngfcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_3_ngfcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat_pop_ngf_4_ngfcell_v[i]/1000.0) +  '\n')
    dat_file_Sim_HippocampalNet_scale500_oc_ngfcell_v_dat.close()

    print("Saving traces to file: Sim_HippocampalNet_scale500_oc.axoaxoniccell.v.dat (ref: Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat)")

 
    # Column: t
    col_Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: pop_axoaxonic_0_axoaxoniccell_v: Pop: pop_axoaxonic; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat_pop_axoaxonic_0_axoaxoniccell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat_pop_axoaxonic_0_Seg0_soma_0_v']['cell_%s'%gids['pop_axoaxonic'][0]]

    # Column: pop_axoaxonic_1_axoaxoniccell_v: Pop: pop_axoaxonic; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat_pop_axoaxonic_1_axoaxoniccell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat_pop_axoaxonic_1_Seg0_soma_0_v']['cell_%s'%gids['pop_axoaxonic'][1]]

    dat_file_Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat = open('Sim_HippocampalNet_scale500_oc.axoaxoniccell.v.dat', 'w')
    for i in range(len(col_Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat_t)):
        dat_file_Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat.write( '%s\t'%(col_Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat_t[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat_pop_axoaxonic_0_axoaxoniccell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat_pop_axoaxonic_1_axoaxoniccell_v[i]/1000.0) +  '\n')
    dat_file_Sim_HippocampalNet_scale500_oc_axoaxoniccell_v_dat.close()

    print("Saving traces to file: Sim_HippocampalNet_scale500_oc.bistratifiedcell.v.dat (ref: Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat)")

 
    # Column: t
    col_Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: pop_bistratified_0_bistratifiedcell_v: Pop: pop_bistratified; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_0_bistratifiedcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_0_Seg0_soma_0_v']['cell_%s'%gids['pop_bistratified'][0]]

    # Column: pop_bistratified_1_bistratifiedcell_v: Pop: pop_bistratified; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_1_bistratifiedcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_1_Seg0_soma_0_v']['cell_%s'%gids['pop_bistratified'][1]]

    # Column: pop_bistratified_2_bistratifiedcell_v: Pop: pop_bistratified; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_2_bistratifiedcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_2_Seg0_soma_0_v']['cell_%s'%gids['pop_bistratified'][2]]

    # Column: pop_bistratified_3_bistratifiedcell_v: Pop: pop_bistratified; cell: 3; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_3_bistratifiedcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_3_Seg0_soma_0_v']['cell_%s'%gids['pop_bistratified'][3]]

    dat_file_Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat = open('Sim_HippocampalNet_scale500_oc.bistratifiedcell.v.dat', 'w')
    for i in range(len(col_Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_t)):
        dat_file_Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat.write( '%s\t'%(col_Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_t[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_0_bistratifiedcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_1_bistratifiedcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_2_bistratifiedcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat_pop_bistratified_3_bistratifiedcell_v[i]/1000.0) +  '\n')
    dat_file_Sim_HippocampalNet_scale500_oc_bistratifiedcell_v_dat.close()

    print("Saving traces to file: Sim_HippocampalNet_scale500_oc.olmcell.v.dat (ref: Sim_HippocampalNet_scale500_oc_olmcell_v_dat)")

 
    # Column: t
    col_Sim_HippocampalNet_scale500_oc_olmcell_v_dat_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: pop_olm_0_olmcell_v: Pop: pop_olm; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_olmcell_v_dat_pop_olm_0_olmcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_olmcell_v_dat_pop_olm_0_Seg0_soma_0_v']['cell_%s'%gids['pop_olm'][0]]

    # Column: pop_olm_1_olmcell_v: Pop: pop_olm; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_olmcell_v_dat_pop_olm_1_olmcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_olmcell_v_dat_pop_olm_1_Seg0_soma_0_v']['cell_%s'%gids['pop_olm'][1]]

    # Column: pop_olm_2_olmcell_v: Pop: pop_olm; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: v
    col_Sim_HippocampalNet_scale500_oc_olmcell_v_dat_pop_olm_2_olmcell_v = sim.allSimData['Sim_HippocampalNet_scale500_oc_olmcell_v_dat_pop_olm_2_Seg0_soma_0_v']['cell_%s'%gids['pop_olm'][2]]

    dat_file_Sim_HippocampalNet_scale500_oc_olmcell_v_dat = open('Sim_HippocampalNet_scale500_oc.olmcell.v.dat', 'w')
    for i in range(len(col_Sim_HippocampalNet_scale500_oc_olmcell_v_dat_t)):
        dat_file_Sim_HippocampalNet_scale500_oc_olmcell_v_dat.write( '%s\t'%(col_Sim_HippocampalNet_scale500_oc_olmcell_v_dat_t[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_olmcell_v_dat_pop_olm_0_olmcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_olmcell_v_dat_pop_olm_1_olmcell_v[i]/1000.0) +  '%s\t'%(col_Sim_HippocampalNet_scale500_oc_olmcell_v_dat_pop_olm_2_olmcell_v[i]/1000.0) +  '\n')
    dat_file_Sim_HippocampalNet_scale500_oc_olmcell_v_dat.close()


    print("Saving spikes to file: Sim_HippocampalNet_scale500_oc.pop_axoaxonic.spikes (ref: Spikes_file__pop_axoaxonic)")
    to_record = {}
    # 0: Pop: pop_axoaxonic; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_axoaxonic'][0]] = 0
    # 1: Pop: pop_axoaxonic; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_axoaxonic'][1]] = 1

    spike_file_Spikes_file__pop_axoaxonic = open('Sim_HippocampalNet_scale500_oc.pop_axoaxonic.spikes', 'w')
    to_record_keys = to_record.keys()
    for t, id in zip(sim.allSimData['spkt'],sim.allSimData['spkid']):
        if id in to_record_keys:
            spike_file_Spikes_file__pop_axoaxonic.write('%i\t%s\n'%(to_record[id],t/1000.))   # format: ID_TIME
    spike_file_Spikes_file__pop_axoaxonic.close()


    print("Saving spikes to file: Sim_HippocampalNet_scale500_oc.pop_bistratified.spikes (ref: Spikes_file__pop_bistratified)")
    to_record = {}
    # 0: Pop: pop_bistratified; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_bistratified'][0]] = 0
    # 1: Pop: pop_bistratified; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_bistratified'][1]] = 1
    # 2: Pop: pop_bistratified; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_bistratified'][2]] = 2
    # 3: Pop: pop_bistratified; cell: 3; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_bistratified'][3]] = 3

    spike_file_Spikes_file__pop_bistratified = open('Sim_HippocampalNet_scale500_oc.pop_bistratified.spikes', 'w')
    to_record_keys = to_record.keys()
    for t, id in zip(sim.allSimData['spkt'],sim.allSimData['spkid']):
        if id in to_record_keys:
            spike_file_Spikes_file__pop_bistratified.write('%i\t%s\n'%(to_record[id],t/1000.))   # format: ID_TIME
    spike_file_Spikes_file__pop_bistratified.close()


    print("Saving spikes to file: Sim_HippocampalNet_scale500_oc.pop_cck.spikes (ref: Spikes_file__pop_cck)")
    to_record = {}
    # 0: Pop: pop_cck; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_cck'][0]] = 0
    # 1: Pop: pop_cck; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_cck'][1]] = 1
    # 2: Pop: pop_cck; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_cck'][2]] = 2
    # 3: Pop: pop_cck; cell: 3; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_cck'][3]] = 3
    # 4: Pop: pop_cck; cell: 4; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_cck'][4]] = 4
    # 5: Pop: pop_cck; cell: 5; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_cck'][5]] = 5
    # 6: Pop: pop_cck; cell: 6; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_cck'][6]] = 6

    spike_file_Spikes_file__pop_cck = open('Sim_HippocampalNet_scale500_oc.pop_cck.spikes', 'w')
    to_record_keys = to_record.keys()
    for t, id in zip(sim.allSimData['spkt'],sim.allSimData['spkid']):
        if id in to_record_keys:
            spike_file_Spikes_file__pop_cck.write('%i\t%s\n'%(to_record[id],t/1000.))   # format: ID_TIME
    spike_file_Spikes_file__pop_cck.close()


    print("Saving spikes to file: Sim_HippocampalNet_scale500_oc.pop_ivy.spikes (ref: Spikes_file__pop_ivy)")
    to_record = {}
    # 0: Pop: pop_ivy; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][0]] = 0
    # 1: Pop: pop_ivy; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][1]] = 1
    # 2: Pop: pop_ivy; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][2]] = 2
    # 3: Pop: pop_ivy; cell: 3; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][3]] = 3
    # 4: Pop: pop_ivy; cell: 4; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][4]] = 4
    # 5: Pop: pop_ivy; cell: 5; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][5]] = 5
    # 6: Pop: pop_ivy; cell: 6; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][6]] = 6
    # 7: Pop: pop_ivy; cell: 7; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][7]] = 7
    # 8: Pop: pop_ivy; cell: 8; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][8]] = 8
    # 9: Pop: pop_ivy; cell: 9; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][9]] = 9
    # 10: Pop: pop_ivy; cell: 10; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][10]] = 10
    # 11: Pop: pop_ivy; cell: 11; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][11]] = 11
    # 12: Pop: pop_ivy; cell: 12; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][12]] = 12
    # 13: Pop: pop_ivy; cell: 13; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][13]] = 13
    # 14: Pop: pop_ivy; cell: 14; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][14]] = 14
    # 15: Pop: pop_ivy; cell: 15; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][15]] = 15
    # 16: Pop: pop_ivy; cell: 16; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ivy'][16]] = 16

    spike_file_Spikes_file__pop_ivy = open('Sim_HippocampalNet_scale500_oc.pop_ivy.spikes', 'w')
    to_record_keys = to_record.keys()
    for t, id in zip(sim.allSimData['spkt'],sim.allSimData['spkid']):
        if id in to_record_keys:
            spike_file_Spikes_file__pop_ivy.write('%i\t%s\n'%(to_record[id],t/1000.))   # format: ID_TIME
    spike_file_Spikes_file__pop_ivy.close()


    print("Saving spikes to file: Sim_HippocampalNet_scale500_oc.pop_ngf.spikes (ref: Spikes_file__pop_ngf)")
    to_record = {}
    # 0: Pop: pop_ngf; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ngf'][0]] = 0
    # 1: Pop: pop_ngf; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ngf'][1]] = 1
    # 2: Pop: pop_ngf; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ngf'][2]] = 2
    # 3: Pop: pop_ngf; cell: 3; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ngf'][3]] = 3
    # 4: Pop: pop_ngf; cell: 4; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ngf'][4]] = 4
    # 5: Pop: pop_ngf; cell: 5; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ngf'][5]] = 5
    # 6: Pop: pop_ngf; cell: 6; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_ngf'][6]] = 6

    spike_file_Spikes_file__pop_ngf = open('Sim_HippocampalNet_scale500_oc.pop_ngf.spikes', 'w')
    to_record_keys = to_record.keys()
    for t, id in zip(sim.allSimData['spkt'],sim.allSimData['spkid']):
        if id in to_record_keys:
            spike_file_Spikes_file__pop_ngf.write('%i\t%s\n'%(to_record[id],t/1000.))   # format: ID_TIME
    spike_file_Spikes_file__pop_ngf.close()


    print("Saving spikes to file: Sim_HippocampalNet_scale500_oc.pop_olm.spikes (ref: Spikes_file__pop_olm)")
    to_record = {}
    # 0: Pop: pop_olm; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_olm'][0]] = 0
    # 1: Pop: pop_olm; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_olm'][1]] = 1
    # 2: Pop: pop_olm; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_olm'][2]] = 2

    spike_file_Spikes_file__pop_olm = open('Sim_HippocampalNet_scale500_oc.pop_olm.spikes', 'w')
    to_record_keys = to_record.keys()
    for t, id in zip(sim.allSimData['spkt'],sim.allSimData['spkid']):
        if id in to_record_keys:
            spike_file_Spikes_file__pop_olm.write('%i\t%s\n'%(to_record[id],t/1000.))   # format: ID_TIME
    spike_file_Spikes_file__pop_olm.close()


    print("Saving spikes to file: Sim_HippocampalNet_scale500_oc.pop_pvbasket.spikes (ref: Spikes_file__pop_pvbasket)")
    to_record = {}
    # 0: Pop: pop_pvbasket; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_pvbasket'][0]] = 0
    # 1: Pop: pop_pvbasket; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_pvbasket'][1]] = 1
    # 2: Pop: pop_pvbasket; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_pvbasket'][2]] = 2
    # 3: Pop: pop_pvbasket; cell: 3; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_pvbasket'][3]] = 3
    # 4: Pop: pop_pvbasket; cell: 4; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_pvbasket'][4]] = 4
    # 5: Pop: pop_pvbasket; cell: 5; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_pvbasket'][5]] = 5
    # 6: Pop: pop_pvbasket; cell: 6; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_pvbasket'][6]] = 6
    # 7: Pop: pop_pvbasket; cell: 7; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_pvbasket'][7]] = 7
    # 8: Pop: pop_pvbasket; cell: 8; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_pvbasket'][8]] = 8
    # 9: Pop: pop_pvbasket; cell: 9; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_pvbasket'][9]] = 9
    # 10: Pop: pop_pvbasket; cell: 10; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_pvbasket'][10]] = 10

    spike_file_Spikes_file__pop_pvbasket = open('Sim_HippocampalNet_scale500_oc.pop_pvbasket.spikes', 'w')
    to_record_keys = to_record.keys()
    for t, id in zip(sim.allSimData['spkt'],sim.allSimData['spkid']):
        if id in to_record_keys:
            spike_file_Spikes_file__pop_pvbasket.write('%i\t%s\n'%(to_record[id],t/1000.))   # format: ID_TIME
    spike_file_Spikes_file__pop_pvbasket.close()


    print("Saving spikes to file: Sim_HippocampalNet_scale500_oc.pop_sca.spikes (ref: Spikes_file__pop_sca)")
    to_record = {}
    # 0: Pop: pop_sca; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_sca'][0]] = 0

    spike_file_Spikes_file__pop_sca = open('Sim_HippocampalNet_scale500_oc.pop_sca.spikes', 'w')
    to_record_keys = to_record.keys()
    for t, id in zip(sim.allSimData['spkt'],sim.allSimData['spkid']):
        if id in to_record_keys:
            spike_file_Spikes_file__pop_sca.write('%i\t%s\n'%(to_record[id],t/1000.))   # format: ID_TIME
    spike_file_Spikes_file__pop_sca.close()


    print("Saving spikes to file: Sim_HippocampalNet_scale500_oc.poolosyncell.spikes (ref: Sim_HippocampalNet_scale500_oc_poolosyncell_spikes)")
    to_record = {}
    # 0: Pop: pop_poolosyn; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][0]] = 0
    # 1: Pop: pop_poolosyn; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][1]] = 1
    # 2: Pop: pop_poolosyn; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][2]] = 2
    # 3: Pop: pop_poolosyn; cell: 3; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][3]] = 3
    # 4: Pop: pop_poolosyn; cell: 4; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][4]] = 4
    # 5: Pop: pop_poolosyn; cell: 5; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][5]] = 5
    # 6: Pop: pop_poolosyn; cell: 6; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][6]] = 6
    # 7: Pop: pop_poolosyn; cell: 7; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][7]] = 7
    # 8: Pop: pop_poolosyn; cell: 8; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][8]] = 8
    # 9: Pop: pop_poolosyn; cell: 9; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][9]] = 9
    # 10: Pop: pop_poolosyn; cell: 10; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][10]] = 10
    # 11: Pop: pop_poolosyn; cell: 11; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][11]] = 11
    # 12: Pop: pop_poolosyn; cell: 12; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][12]] = 12
    # 13: Pop: pop_poolosyn; cell: 13; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][13]] = 13
    # 14: Pop: pop_poolosyn; cell: 14; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][14]] = 14
    # 15: Pop: pop_poolosyn; cell: 15; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][15]] = 15
    # 16: Pop: pop_poolosyn; cell: 16; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][16]] = 16
    # 17: Pop: pop_poolosyn; cell: 17; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][17]] = 17
    # 18: Pop: pop_poolosyn; cell: 18; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][18]] = 18
    # 19: Pop: pop_poolosyn; cell: 19; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][19]] = 19
    # 20: Pop: pop_poolosyn; cell: 20; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][20]] = 20
    # 21: Pop: pop_poolosyn; cell: 21; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][21]] = 21
    # 22: Pop: pop_poolosyn; cell: 22; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][22]] = 22
    # 23: Pop: pop_poolosyn; cell: 23; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][23]] = 23
    # 24: Pop: pop_poolosyn; cell: 24; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][24]] = 24
    # 25: Pop: pop_poolosyn; cell: 25; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][25]] = 25
    # 26: Pop: pop_poolosyn; cell: 26; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][26]] = 26
    # 27: Pop: pop_poolosyn; cell: 27; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][27]] = 27
    # 28: Pop: pop_poolosyn; cell: 28; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][28]] = 28
    # 29: Pop: pop_poolosyn; cell: 29; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][29]] = 29
    # 30: Pop: pop_poolosyn; cell: 30; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][30]] = 30
    # 31: Pop: pop_poolosyn; cell: 31; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][31]] = 31
    # 32: Pop: pop_poolosyn; cell: 32; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][32]] = 32
    # 33: Pop: pop_poolosyn; cell: 33; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][33]] = 33
    # 34: Pop: pop_poolosyn; cell: 34; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][34]] = 34
    # 35: Pop: pop_poolosyn; cell: 35; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][35]] = 35
    # 36: Pop: pop_poolosyn; cell: 36; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][36]] = 36
    # 37: Pop: pop_poolosyn; cell: 37; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][37]] = 37
    # 38: Pop: pop_poolosyn; cell: 38; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][38]] = 38
    # 39: Pop: pop_poolosyn; cell: 39; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][39]] = 39
    # 40: Pop: pop_poolosyn; cell: 40; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][40]] = 40
    # 41: Pop: pop_poolosyn; cell: 41; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][41]] = 41
    # 42: Pop: pop_poolosyn; cell: 42; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][42]] = 42
    # 43: Pop: pop_poolosyn; cell: 43; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][43]] = 43
    # 44: Pop: pop_poolosyn; cell: 44; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][44]] = 44
    # 45: Pop: pop_poolosyn; cell: 45; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][45]] = 45
    # 46: Pop: pop_poolosyn; cell: 46; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][46]] = 46
    # 47: Pop: pop_poolosyn; cell: 47; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][47]] = 47
    # 48: Pop: pop_poolosyn; cell: 48; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][48]] = 48
    # 49: Pop: pop_poolosyn; cell: 49; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][49]] = 49
    # 50: Pop: pop_poolosyn; cell: 50; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][50]] = 50
    # 51: Pop: pop_poolosyn; cell: 51; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][51]] = 51
    # 52: Pop: pop_poolosyn; cell: 52; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][52]] = 52
    # 53: Pop: pop_poolosyn; cell: 53; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][53]] = 53
    # 54: Pop: pop_poolosyn; cell: 54; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][54]] = 54
    # 55: Pop: pop_poolosyn; cell: 55; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][55]] = 55
    # 56: Pop: pop_poolosyn; cell: 56; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][56]] = 56
    # 57: Pop: pop_poolosyn; cell: 57; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][57]] = 57
    # 58: Pop: pop_poolosyn; cell: 58; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][58]] = 58
    # 59: Pop: pop_poolosyn; cell: 59; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][59]] = 59
    # 60: Pop: pop_poolosyn; cell: 60; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][60]] = 60
    # 61: Pop: pop_poolosyn; cell: 61; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][61]] = 61
    # 62: Pop: pop_poolosyn; cell: 62; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][62]] = 62
    # 63: Pop: pop_poolosyn; cell: 63; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][63]] = 63
    # 64: Pop: pop_poolosyn; cell: 64; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][64]] = 64
    # 65: Pop: pop_poolosyn; cell: 65; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][65]] = 65
    # 66: Pop: pop_poolosyn; cell: 66; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][66]] = 66
    # 67: Pop: pop_poolosyn; cell: 67; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][67]] = 67
    # 68: Pop: pop_poolosyn; cell: 68; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][68]] = 68
    # 69: Pop: pop_poolosyn; cell: 69; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][69]] = 69
    # 70: Pop: pop_poolosyn; cell: 70; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][70]] = 70
    # 71: Pop: pop_poolosyn; cell: 71; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][71]] = 71
    # 72: Pop: pop_poolosyn; cell: 72; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][72]] = 72
    # 73: Pop: pop_poolosyn; cell: 73; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][73]] = 73
    # 74: Pop: pop_poolosyn; cell: 74; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][74]] = 74
    # 75: Pop: pop_poolosyn; cell: 75; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][75]] = 75
    # 76: Pop: pop_poolosyn; cell: 76; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][76]] = 76
    # 77: Pop: pop_poolosyn; cell: 77; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][77]] = 77
    # 78: Pop: pop_poolosyn; cell: 78; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][78]] = 78
    # 79: Pop: pop_poolosyn; cell: 79; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][79]] = 79
    # 80: Pop: pop_poolosyn; cell: 80; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][80]] = 80
    # 81: Pop: pop_poolosyn; cell: 81; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][81]] = 81
    # 82: Pop: pop_poolosyn; cell: 82; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][82]] = 82
    # 83: Pop: pop_poolosyn; cell: 83; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][83]] = 83
    # 84: Pop: pop_poolosyn; cell: 84; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][84]] = 84
    # 85: Pop: pop_poolosyn; cell: 85; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][85]] = 85
    # 86: Pop: pop_poolosyn; cell: 86; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][86]] = 86
    # 87: Pop: pop_poolosyn; cell: 87; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][87]] = 87
    # 88: Pop: pop_poolosyn; cell: 88; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][88]] = 88
    # 89: Pop: pop_poolosyn; cell: 89; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][89]] = 89
    # 90: Pop: pop_poolosyn; cell: 90; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][90]] = 90
    # 91: Pop: pop_poolosyn; cell: 91; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][91]] = 91
    # 92: Pop: pop_poolosyn; cell: 92; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][92]] = 92
    # 93: Pop: pop_poolosyn; cell: 93; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][93]] = 93
    # 94: Pop: pop_poolosyn; cell: 94; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][94]] = 94
    # 95: Pop: pop_poolosyn; cell: 95; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][95]] = 95
    # 96: Pop: pop_poolosyn; cell: 96; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][96]] = 96
    # 97: Pop: pop_poolosyn; cell: 97; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][97]] = 97
    # 98: Pop: pop_poolosyn; cell: 98; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][98]] = 98
    # 99: Pop: pop_poolosyn; cell: 99; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][99]] = 99
    # 100: Pop: pop_poolosyn; cell: 100; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][100]] = 100
    # 101: Pop: pop_poolosyn; cell: 101; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][101]] = 101
    # 102: Pop: pop_poolosyn; cell: 102; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][102]] = 102
    # 103: Pop: pop_poolosyn; cell: 103; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][103]] = 103
    # 104: Pop: pop_poolosyn; cell: 104; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][104]] = 104
    # 105: Pop: pop_poolosyn; cell: 105; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][105]] = 105
    # 106: Pop: pop_poolosyn; cell: 106; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][106]] = 106
    # 107: Pop: pop_poolosyn; cell: 107; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][107]] = 107
    # 108: Pop: pop_poolosyn; cell: 108; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][108]] = 108
    # 109: Pop: pop_poolosyn; cell: 109; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][109]] = 109
    # 110: Pop: pop_poolosyn; cell: 110; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][110]] = 110
    # 111: Pop: pop_poolosyn; cell: 111; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][111]] = 111
    # 112: Pop: pop_poolosyn; cell: 112; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][112]] = 112
    # 113: Pop: pop_poolosyn; cell: 113; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][113]] = 113
    # 114: Pop: pop_poolosyn; cell: 114; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][114]] = 114
    # 115: Pop: pop_poolosyn; cell: 115; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][115]] = 115
    # 116: Pop: pop_poolosyn; cell: 116; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][116]] = 116
    # 117: Pop: pop_poolosyn; cell: 117; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][117]] = 117
    # 118: Pop: pop_poolosyn; cell: 118; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][118]] = 118
    # 119: Pop: pop_poolosyn; cell: 119; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][119]] = 119
    # 120: Pop: pop_poolosyn; cell: 120; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][120]] = 120
    # 121: Pop: pop_poolosyn; cell: 121; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][121]] = 121
    # 122: Pop: pop_poolosyn; cell: 122; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][122]] = 122
    # 123: Pop: pop_poolosyn; cell: 123; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][123]] = 123
    # 124: Pop: pop_poolosyn; cell: 124; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][124]] = 124
    # 125: Pop: pop_poolosyn; cell: 125; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][125]] = 125
    # 126: Pop: pop_poolosyn; cell: 126; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][126]] = 126
    # 127: Pop: pop_poolosyn; cell: 127; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][127]] = 127
    # 128: Pop: pop_poolosyn; cell: 128; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][128]] = 128
    # 129: Pop: pop_poolosyn; cell: 129; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][129]] = 129
    # 130: Pop: pop_poolosyn; cell: 130; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][130]] = 130
    # 131: Pop: pop_poolosyn; cell: 131; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][131]] = 131
    # 132: Pop: pop_poolosyn; cell: 132; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][132]] = 132
    # 133: Pop: pop_poolosyn; cell: 133; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][133]] = 133
    # 134: Pop: pop_poolosyn; cell: 134; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][134]] = 134
    # 135: Pop: pop_poolosyn; cell: 135; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][135]] = 135
    # 136: Pop: pop_poolosyn; cell: 136; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][136]] = 136
    # 137: Pop: pop_poolosyn; cell: 137; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][137]] = 137
    # 138: Pop: pop_poolosyn; cell: 138; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][138]] = 138
    # 139: Pop: pop_poolosyn; cell: 139; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][139]] = 139
    # 140: Pop: pop_poolosyn; cell: 140; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][140]] = 140
    # 141: Pop: pop_poolosyn; cell: 141; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][141]] = 141
    # 142: Pop: pop_poolosyn; cell: 142; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][142]] = 142
    # 143: Pop: pop_poolosyn; cell: 143; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][143]] = 143
    # 144: Pop: pop_poolosyn; cell: 144; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][144]] = 144
    # 145: Pop: pop_poolosyn; cell: 145; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][145]] = 145
    # 146: Pop: pop_poolosyn; cell: 146; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][146]] = 146
    # 147: Pop: pop_poolosyn; cell: 147; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][147]] = 147
    # 148: Pop: pop_poolosyn; cell: 148; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][148]] = 148
    # 149: Pop: pop_poolosyn; cell: 149; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][149]] = 149
    # 150: Pop: pop_poolosyn; cell: 150; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][150]] = 150
    # 151: Pop: pop_poolosyn; cell: 151; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][151]] = 151
    # 152: Pop: pop_poolosyn; cell: 152; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][152]] = 152
    # 153: Pop: pop_poolosyn; cell: 153; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][153]] = 153
    # 154: Pop: pop_poolosyn; cell: 154; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][154]] = 154
    # 155: Pop: pop_poolosyn; cell: 155; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][155]] = 155
    # 156: Pop: pop_poolosyn; cell: 156; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][156]] = 156
    # 157: Pop: pop_poolosyn; cell: 157; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][157]] = 157
    # 158: Pop: pop_poolosyn; cell: 158; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][158]] = 158
    # 159: Pop: pop_poolosyn; cell: 159; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][159]] = 159
    # 160: Pop: pop_poolosyn; cell: 160; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][160]] = 160
    # 161: Pop: pop_poolosyn; cell: 161; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][161]] = 161
    # 162: Pop: pop_poolosyn; cell: 162; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][162]] = 162
    # 163: Pop: pop_poolosyn; cell: 163; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][163]] = 163
    # 164: Pop: pop_poolosyn; cell: 164; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][164]] = 164
    # 165: Pop: pop_poolosyn; cell: 165; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][165]] = 165
    # 166: Pop: pop_poolosyn; cell: 166; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][166]] = 166
    # 167: Pop: pop_poolosyn; cell: 167; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][167]] = 167
    # 168: Pop: pop_poolosyn; cell: 168; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][168]] = 168
    # 169: Pop: pop_poolosyn; cell: 169; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][169]] = 169
    # 170: Pop: pop_poolosyn; cell: 170; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][170]] = 170
    # 171: Pop: pop_poolosyn; cell: 171; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][171]] = 171
    # 172: Pop: pop_poolosyn; cell: 172; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][172]] = 172
    # 173: Pop: pop_poolosyn; cell: 173; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][173]] = 173
    # 174: Pop: pop_poolosyn; cell: 174; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][174]] = 174
    # 175: Pop: pop_poolosyn; cell: 175; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][175]] = 175
    # 176: Pop: pop_poolosyn; cell: 176; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][176]] = 176
    # 177: Pop: pop_poolosyn; cell: 177; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][177]] = 177
    # 178: Pop: pop_poolosyn; cell: 178; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][178]] = 178
    # 179: Pop: pop_poolosyn; cell: 179; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][179]] = 179
    # 180: Pop: pop_poolosyn; cell: 180; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][180]] = 180
    # 181: Pop: pop_poolosyn; cell: 181; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][181]] = 181
    # 182: Pop: pop_poolosyn; cell: 182; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][182]] = 182
    # 183: Pop: pop_poolosyn; cell: 183; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][183]] = 183
    # 184: Pop: pop_poolosyn; cell: 184; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][184]] = 184
    # 185: Pop: pop_poolosyn; cell: 185; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][185]] = 185
    # 186: Pop: pop_poolosyn; cell: 186; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][186]] = 186
    # 187: Pop: pop_poolosyn; cell: 187; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][187]] = 187
    # 188: Pop: pop_poolosyn; cell: 188; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][188]] = 188
    # 189: Pop: pop_poolosyn; cell: 189; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][189]] = 189
    # 190: Pop: pop_poolosyn; cell: 190; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][190]] = 190
    # 191: Pop: pop_poolosyn; cell: 191; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][191]] = 191
    # 192: Pop: pop_poolosyn; cell: 192; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][192]] = 192
    # 193: Pop: pop_poolosyn; cell: 193; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][193]] = 193
    # 194: Pop: pop_poolosyn; cell: 194; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][194]] = 194
    # 195: Pop: pop_poolosyn; cell: 195; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][195]] = 195
    # 196: Pop: pop_poolosyn; cell: 196; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][196]] = 196
    # 197: Pop: pop_poolosyn; cell: 197; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][197]] = 197
    # 198: Pop: pop_poolosyn; cell: 198; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][198]] = 198
    # 199: Pop: pop_poolosyn; cell: 199; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][199]] = 199
    # 200: Pop: pop_poolosyn; cell: 200; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][200]] = 200
    # 201: Pop: pop_poolosyn; cell: 201; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][201]] = 201
    # 202: Pop: pop_poolosyn; cell: 202; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][202]] = 202
    # 203: Pop: pop_poolosyn; cell: 203; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][203]] = 203
    # 204: Pop: pop_poolosyn; cell: 204; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][204]] = 204
    # 205: Pop: pop_poolosyn; cell: 205; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][205]] = 205
    # 206: Pop: pop_poolosyn; cell: 206; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][206]] = 206
    # 207: Pop: pop_poolosyn; cell: 207; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][207]] = 207
    # 208: Pop: pop_poolosyn; cell: 208; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][208]] = 208
    # 209: Pop: pop_poolosyn; cell: 209; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][209]] = 209
    # 210: Pop: pop_poolosyn; cell: 210; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][210]] = 210
    # 211: Pop: pop_poolosyn; cell: 211; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][211]] = 211
    # 212: Pop: pop_poolosyn; cell: 212; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][212]] = 212
    # 213: Pop: pop_poolosyn; cell: 213; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][213]] = 213
    # 214: Pop: pop_poolosyn; cell: 214; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][214]] = 214
    # 215: Pop: pop_poolosyn; cell: 215; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][215]] = 215
    # 216: Pop: pop_poolosyn; cell: 216; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][216]] = 216
    # 217: Pop: pop_poolosyn; cell: 217; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][217]] = 217
    # 218: Pop: pop_poolosyn; cell: 218; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][218]] = 218
    # 219: Pop: pop_poolosyn; cell: 219; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][219]] = 219
    # 220: Pop: pop_poolosyn; cell: 220; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][220]] = 220
    # 221: Pop: pop_poolosyn; cell: 221; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][221]] = 221
    # 222: Pop: pop_poolosyn; cell: 222; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][222]] = 222
    # 223: Pop: pop_poolosyn; cell: 223; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][223]] = 223
    # 224: Pop: pop_poolosyn; cell: 224; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][224]] = 224
    # 225: Pop: pop_poolosyn; cell: 225; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][225]] = 225
    # 226: Pop: pop_poolosyn; cell: 226; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][226]] = 226
    # 227: Pop: pop_poolosyn; cell: 227; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][227]] = 227
    # 228: Pop: pop_poolosyn; cell: 228; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][228]] = 228
    # 229: Pop: pop_poolosyn; cell: 229; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][229]] = 229
    # 230: Pop: pop_poolosyn; cell: 230; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][230]] = 230
    # 231: Pop: pop_poolosyn; cell: 231; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][231]] = 231
    # 232: Pop: pop_poolosyn; cell: 232; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][232]] = 232
    # 233: Pop: pop_poolosyn; cell: 233; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][233]] = 233
    # 234: Pop: pop_poolosyn; cell: 234; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][234]] = 234
    # 235: Pop: pop_poolosyn; cell: 235; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][235]] = 235
    # 236: Pop: pop_poolosyn; cell: 236; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][236]] = 236
    # 237: Pop: pop_poolosyn; cell: 237; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][237]] = 237
    # 238: Pop: pop_poolosyn; cell: 238; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][238]] = 238
    # 239: Pop: pop_poolosyn; cell: 239; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][239]] = 239
    # 240: Pop: pop_poolosyn; cell: 240; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][240]] = 240
    # 241: Pop: pop_poolosyn; cell: 241; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][241]] = 241
    # 242: Pop: pop_poolosyn; cell: 242; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][242]] = 242
    # 243: Pop: pop_poolosyn; cell: 243; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][243]] = 243
    # 244: Pop: pop_poolosyn; cell: 244; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][244]] = 244
    # 245: Pop: pop_poolosyn; cell: 245; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][245]] = 245
    # 246: Pop: pop_poolosyn; cell: 246; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][246]] = 246
    # 247: Pop: pop_poolosyn; cell: 247; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][247]] = 247
    # 248: Pop: pop_poolosyn; cell: 248; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][248]] = 248
    # 249: Pop: pop_poolosyn; cell: 249; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][249]] = 249
    # 250: Pop: pop_poolosyn; cell: 250; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][250]] = 250
    # 251: Pop: pop_poolosyn; cell: 251; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][251]] = 251
    # 252: Pop: pop_poolosyn; cell: 252; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][252]] = 252
    # 253: Pop: pop_poolosyn; cell: 253; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][253]] = 253
    # 254: Pop: pop_poolosyn; cell: 254; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][254]] = 254
    # 255: Pop: pop_poolosyn; cell: 255; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][255]] = 255
    # 256: Pop: pop_poolosyn; cell: 256; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][256]] = 256
    # 257: Pop: pop_poolosyn; cell: 257; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][257]] = 257
    # 258: Pop: pop_poolosyn; cell: 258; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][258]] = 258
    # 259: Pop: pop_poolosyn; cell: 259; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][259]] = 259
    # 260: Pop: pop_poolosyn; cell: 260; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][260]] = 260
    # 261: Pop: pop_poolosyn; cell: 261; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][261]] = 261
    # 262: Pop: pop_poolosyn; cell: 262; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][262]] = 262
    # 263: Pop: pop_poolosyn; cell: 263; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][263]] = 263
    # 264: Pop: pop_poolosyn; cell: 264; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][264]] = 264
    # 265: Pop: pop_poolosyn; cell: 265; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][265]] = 265
    # 266: Pop: pop_poolosyn; cell: 266; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][266]] = 266
    # 267: Pop: pop_poolosyn; cell: 267; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][267]] = 267
    # 268: Pop: pop_poolosyn; cell: 268; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][268]] = 268
    # 269: Pop: pop_poolosyn; cell: 269; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][269]] = 269
    # 270: Pop: pop_poolosyn; cell: 270; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][270]] = 270
    # 271: Pop: pop_poolosyn; cell: 271; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][271]] = 271
    # 272: Pop: pop_poolosyn; cell: 272; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][272]] = 272
    # 273: Pop: pop_poolosyn; cell: 273; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][273]] = 273
    # 274: Pop: pop_poolosyn; cell: 274; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][274]] = 274
    # 275: Pop: pop_poolosyn; cell: 275; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][275]] = 275
    # 276: Pop: pop_poolosyn; cell: 276; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][276]] = 276
    # 277: Pop: pop_poolosyn; cell: 277; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][277]] = 277
    # 278: Pop: pop_poolosyn; cell: 278; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][278]] = 278
    # 279: Pop: pop_poolosyn; cell: 279; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][279]] = 279
    # 280: Pop: pop_poolosyn; cell: 280; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][280]] = 280
    # 281: Pop: pop_poolosyn; cell: 281; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][281]] = 281
    # 282: Pop: pop_poolosyn; cell: 282; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][282]] = 282
    # 283: Pop: pop_poolosyn; cell: 283; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][283]] = 283
    # 284: Pop: pop_poolosyn; cell: 284; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][284]] = 284
    # 285: Pop: pop_poolosyn; cell: 285; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][285]] = 285
    # 286: Pop: pop_poolosyn; cell: 286; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][286]] = 286
    # 287: Pop: pop_poolosyn; cell: 287; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][287]] = 287
    # 288: Pop: pop_poolosyn; cell: 288; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][288]] = 288
    # 289: Pop: pop_poolosyn; cell: 289; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][289]] = 289
    # 290: Pop: pop_poolosyn; cell: 290; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][290]] = 290
    # 291: Pop: pop_poolosyn; cell: 291; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][291]] = 291
    # 292: Pop: pop_poolosyn; cell: 292; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][292]] = 292
    # 293: Pop: pop_poolosyn; cell: 293; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][293]] = 293
    # 294: Pop: pop_poolosyn; cell: 294; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][294]] = 294
    # 295: Pop: pop_poolosyn; cell: 295; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][295]] = 295
    # 296: Pop: pop_poolosyn; cell: 296; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][296]] = 296
    # 297: Pop: pop_poolosyn; cell: 297; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][297]] = 297
    # 298: Pop: pop_poolosyn; cell: 298; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][298]] = 298
    # 299: Pop: pop_poolosyn; cell: 299; segment id: 0; segment name: Seg0_soma_0; value: spike
    assert 0==0 # Only able to record events at soma (seg_id = 0)
    to_record[gids['pop_poolosyn'][299]] = 299

    spike_file_Sim_HippocampalNet_scale500_oc_poolosyncell_spikes = open('Sim_HippocampalNet_scale500_oc.poolosyncell.spikes', 'w')
    to_record_keys = to_record.keys()
    for t, id in zip(sim.allSimData['spkt'],sim.allSimData['spkid']):
        if id in to_record_keys:
            spike_file_Sim_HippocampalNet_scale500_oc_poolosyncell_spikes.write('%i\t%s\n'%(to_record[id],t/1000.))   # format: ID_TIME
    spike_file_Sim_HippocampalNet_scale500_oc_poolosyncell_spikes.close()




    print("Saved all data.")

if '-nogui' in sys.argv:
    quit()
