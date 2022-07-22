#  By convention, beam generating sequences are synced to 1Hz at restart
#  Allow sequences may be swapped in at any time, so they may require an extra sync;
#  Put that sync at the end and set the start address in the allow table ('async_start')
#
#  This is specific to LCLS2 given the translation of markers to time intervals
#
def seq_lookup(arg):
    #  Code below assumes soft timeslot is before hard timeslot
    SoftTsm = 1
    HardTsm = 8
    BothTsm = 9
    d = {'0 Hz'       :{'instr':['Branch.unconditional(0)'],
                        'async_start':0},
         '1 Hz'       :{'instr':['BeamRequest(0)','FixedRateSync("1H",1)','Branch.unconditional(0)'],
                        'async_start':1},
         '10 Hz'      :{'instr':['BeamRequest(0)','FixedRateSync("10H",1)','Branch.unconditional(0)'],
                        'async_start':1},
         '50 Hz'      :{'instr':['BeamRequest(0)','FixedRateSync("100H",2)','Branch.unconditional(0)',
                                 'FixedRateSync("10H",1)','Branch.unconditional(0)'], 
                        'async_start':3},
         '100 Hz'     :{'instr':['BeamRequest(0)','FixedRateSync("100H",1)','Branch.unconditional(0)'],
                        'async_start':1},
         '200 Hz'     :{'instr':['BeamRequest(0)','FixedRateSync("1kH",5)','Branch.unconditional(0)',
                                 'FixedRateSync("100H",1)','Branch.unconditional(0)'],
                        'async_start':3},
         '500 Hz'     :{'instr':['BeamRequest(0)','FixedRateSync("1kH",2)','Branch.unconditional(0)',
                                 'FixedRateSync("100H",1)','Branch.unconditional(0)'],
                        'async_start':3},
         '1 kHz'      :{'instr':['BeamRequest(0)','FixedRateSync("1kH",1)','Branch.unconditional(0)'],
                        'async_start':1},
         '1.4 kHz'    :{'instr':['BeamRequest(0)','FixedRateSync("70kH",50)','Branch.unconditional(0)',
                                 'FixedRateSync("100H",1)','Branch.unconditional(0)'],
                        'async_start':3},
         '5 kHz'      :{'instr':['BeamRequest(0)','FixedRateSync("10kH",2)','Branch.unconditional(0)',
                                 'FixedRateSync("1kH",1)','Branch.unconditional(0)'],
                        'async_start':3},
         '9.3 kHz'    :{'instr':['BeamRequest(0)','FixedRateSync("910kH",100)','Branch.unconditional(0)',
                                 'FixedRateSync("100H",1)','Branch.unconditional(0)'],
                        'async_start':3},
         '10 kHz'     :{'instr':['BeamRequest(0)','FixedRateSync("10kH",1)','Branch.unconditional(0)'],
                        'async_start':1},
	 '23 kHz'     :{'instr':['BeamRequest(0)','FixedRateSync("910kH",40)','Branch.unconditional(0)',
                                 'FixedRateSync("100H",1)','Branch.unconditional(0)'],
                        'async_start':3},
         '33 kHz'     :{'instr':['BeamRequest(0)','FixedRateSync("910kH",28)','Branch.unconditional(0)',
                                 'FixedRateSync("100H",1)','Branch.unconditional(0)'],
                        'async_start':3},
         '46 kHz'     :{'instr':['BeamRequest(0)','FixedRateSync("910kH",20)','Branch.unconditional(0)',
                                 'FixedRateSync("100H",1)','Branch.unconditional(0)'],
                        'async_start':3},
         '71 kHz'     :{'instr':['BeamRequest(0)','FixedRateSync("70kH",1)','Branch.unconditional(0)'],'async_start':1},
         '93 kHz'     :{'instr':['BeamRequest(0)','FixedRateSync("910kH",10)','Branch.unconditional(0)',
                                 'FixedRateSync("1kH",1)','Branch.unconditional(0)'],
                        'async_start':3},
         '186 kHz'    :{'instr':['BeamRequest(0)','FixedRateSync("910kH",5)','Branch.unconditional(0)',
                                 'FixedRateSync("1kH",1)','Branch.unconditional(0)'],
                        'async_start':3},
         '464 kHz'    :{'instr':['BeamRequest(0)','FixedRateSync("910kH",2)','Branch.unconditional(0)',
                                 'FixedRateSync("1kH",1)','Branch.unconditional(0)'],
                        'async_start':3},
         '929 kHz'    :{'instr':['BeamRequest(0)','FixedRateSync("910kH",1)','Branch.unconditional(0)'],
                        'async_start':0},
         '1 Hz off'   :{'instr':['FixedRateSync("10H",5)','BeamRequest(0)','FixedRateSync("10H",5)','Branch.unconditional(0)',
                                 'FixedRateSync("1H",1)','Branch.unconditional(0)'],
                        'async_start':4},
         '10 Hz off'  :{'instr':['FixedRateSync("100H",5)','BeamRequest(0)','FixedRateSync("100H",5)','Branch.unconditional(0)',
                                 'FixedRateSync("10H",1)','Branch.unconditional(0)'],
                        'async_start':4},
         '100 Hz off' :{'instr':['FixedRateSync("1kH",5)','BeamRequest(0)','FixedRateSync("1kH",5)','Branch.unconditional(0)',
                                 'FixedRateSync("100H",1)','Branch.unconditional(0)'],
                        'async_start':4},
         '1 kHz off'  :{'instr':['FixedRateSync("10kH",5)','BeamRequest(0)','FixedRateSync("10kH",5)','Branch.unconditional(0)',
                                 'FixedRateSync("1kH",1)','Branch.unconditional(0)'],
                        'async_start':4},
         '93 kHz off' :{'instr':['FixedRateSync("910kH",5)','BeamRequest(0)','FixedRateSync("910kH",5)','Branch.unconditional(0)',
                                 'FixedRateSync("1kH",1)','Branch.unconditional(0)'],
                        'async_start':4},
         '100 Hz off 0 Hz' :{'instr':['BeamRequest(0)','FixedRateSync("100H",1)','Branch.unconditional(0)'],
                            'async_start':1},
         '99 Hz off 1 Hz'  :{'instr':['FixedRateSync("100H",1)','BeamRequest(0)','Branch.conditional(0, 0, 98)','FixedRateSync("100H",1)','Branch.unconditional(0)',
                                      'FixedRateSync("1H",1)','Branch.unconditional(0)'],
                            'async_start':5},
         '90 Hz off 10 Hz' :{'instr':['FixedRateSync("100H",1)','BeamRequest(0)','Branch.conditional(0, 0, 8)','FixedRateSync("100H",1)','Branch.unconditional(0)', 
                                      'FixedRateSync("10H",1)','Branch.unconditional(0)'],
                            'async_start':5},
         '50 Hz off 50 Hz' :{'instr':['FixedRateSync("100H",1)','BeamRequest(0)','FixedRateSync("100H",1)','Branch.unconditional(0)',
                                      'FixedRateSync("10H",1)','Branch.unconditional(0)'],
                            'async_start':4},
         '0.5 Hz AC'  :{'instr':['ACRateSync(0,"0.5H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '1 Hz AC'    :{'instr':['ACRateSync(0,"1H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '5 Hz AC'    :{'instr':['ACRateSync(0,"5H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '10 Hz AC'   :{'instr':['ACRateSync(0,"10H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '30 Hz AC'   :{'instr':['ACRateSync(0,"30H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '60 Hz AC'   :{'instr':['ACRateSync(0,"60H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         #  Separate S and H sequences for complementary rates up to 119 Hz
         '120 Hz AC'  :{'instr':[f'ACRateSync({BothTsm},"60H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '1 Hz ACS'   :{'instr':[f'ACRateSync({SoftTsm},"1H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '5 Hz ACS'   :{'instr':[f'ACRateSync({SoftTsm},"5H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '10 Hz ACS'  :{'instr':[f'ACRateSync({SoftTsm},"10H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '30 Hz ACS'  :{'instr':[f'ACRateSync({SoftTsm},"30H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '60 Hz ACS'  :{'instr':[f'ACRateSync({SoftTsm},"60H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '90 Hz ACS'  :{'instr':[f'ACRateSync({SoftTsm},"30H",1)','BeamRequest(0)',f'ACRateSync({HardTsm},"30H",1)',
                                 f'ACRateSync({BothTsm},"60H",1)','BeamRequest(0)','Branch.conditional(3,0,1)',
                                 'Branch.unconditional(0)'],
                        'async_start':0},
         '110 Hz ACS' :{'instr':[f'ACRateSync({SoftTsm},"10H",1)','BeamRequest(0)',f'ACRateSync({HardTsm},"10H",1)',
                                 f'ACRateSync({BothTsm},"60H",1)','BeamRequest(0)','Branch.conditional(3,0,9)',
                                 'Branch.unconditional(0)'],
                        'async_start':0},
         '115 Hz ACS' :{'instr':[f'ACRateSync({SoftTsm},"5H",1)','BeamRequest(0)',f'ACRateSync({HardTsm},"5H",1)',
                                 f'ACRateSync({BothTsm},"60H",1)','BeamRequest(0)','Branch.conditional(3,0,21)',
                                 'Branch.unconditional(0)'],
                        'async_start':0},
         '119 Hz ACS' :{'instr':[f'ACRateSync({SoftTsm},"1H",1)','BeamRequest(0)',f'ACRateSync({HardTsm},"1H",1)',
                                 f'ACRateSync({BothTsm},"60H",1)','BeamRequest(0)','Branch.conditional(3,0,117)',
                                 'Branch.unconditional(0)'],
                        'async_start':0},
         '1 Hz ACH'   :{'instr':[f'ACRateSync({HardTsm},"1H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '5 Hz ACH'   :{'instr':[f'ACRateSync({HardTsm},"5H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '10 Hz ACH'  :{'instr':[f'ACRateSync({HardTsm},"10H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '30 Hz ACH'  :{'instr':[f'ACRateSync({HardTsm},"30H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '60 Hz ACH'  :{'instr':[f'ACRateSync({HardTsm},"60H",1)','BeamRequest(0)','Branch.unconditional(0)'],
                        'async_start':0},
         '90 Hz ACH'  :{'instr':[f'ACRateSync({SoftTsm},"30H",1)',f'ACRateSync({HardTsm},"30H",1)','BeamRequest(0)',
                                 f'ACRateSync({BothTsm},"60H",1)','BeamRequest(0)','Branch.conditional(3,0,1)',
                                 'Branch.unconditional(0)'],
                        'async_start':0},
         '110 Hz ACH' :{'instr':[f'ACRateSync({SoftTsm},"10H",1)',f'ACRateSync({HardTsm},"10H",1)','BeamRequest(0)',
                                 f'ACRateSync({BothTsm},"60H",1)','BeamRequest(0)','Branch.conditional(3,0,9)',
                                 'Branch.unconditional(0)'],
                        'async_start':0},
         '115 Hz ACH' :{'instr':[f'ACRateSync({SoftTsm},"5H",1)',f'ACRateSync({HardTsm},"5H",1)','BeamRequest(0)',
                                 f'ACRateSync({BothTsm},"60H",1)','BeamRequest(0)','Branch.conditional(3,0,21)',
                                 'Branch.unconditional(0)'],
                        'async_start':0},
         '119 Hz ACH' :{'instr':[f'ACRateSync({SoftTsm},"1H",1)',f'ACRateSync({HardTsm},"1H",1)','BeamRequest(0)',
                                 f'ACRateSync({BothTsm},"60H",1)','BeamRequest(0)','Branch.conditional(3,0,117)',
                                 'Branch.unconditional(0)'],
                        'async_start':0},
         '100 Hz_skip2'     :{'instr':['FixedRateSync("100H",2)','BeamRequest(0)','FixedRateSync("100H",1)','Branch.conditional(1,0,97)','Branch.unconditional(0)',' FixedRateSync("1H",1)', 'Branch.unconditional(0)'], 
                        'async_start':5},
         '1/10/100 Hz' : {'instr':['ControlRequest(7)', # fire 1/10/100Hz bits
                                   'FixedRateSync("100H",1)','ControlRequest(4)','Branch.conditional(line=1,counter=0,value=8)',  # fire 100Hz bit
                                   'FixedRateSync("100H",1)','ControlRequest(6)','Branch.conditional(line=1,counter=1,value=8)',  # fire 10/100Hz bits
                                   'FixedRateSync("100H",1)','ControlRequest(4)','Branch.conditional(line=7,counter=0,value=8)',  # fire 100Hz bit
                                   'FixedRateSync("1H",1)','Branch.unconditional(0)'],
                          'async_start':10},
         '1/10/10 Hz' : {'instr':['ControlRequest(7)', # fire 1/10/10Hz bits
                                    'FixedRateSync("10H",1)','ControlRequest(6)','Branch.conditional(1,0,8)', # fire 10Hz bit
                                    'FixedRateSync("1H",1)','Branch.unconditional(0)'],
                           'async_start':4},

         '1/1/1 Hz' : {'instr':['ControlRequest(7)',
                                    'FixedRateSync("1H",1)','Branch.unconditional(0)'],
                           'async_start':1},
         '30 Hz SimAC' : {'instr':['BeamRequest(0)','FixedRateSync("70kH",583)',
                                   'FixedRateSync("70kH",583)',
                                   'FixedRateSync("70kH",584)',
                                   'FixedRateSync("70kH",583)',
                                   'BeamRequest(0)','FixedRateSync("70kH",583)',
                                   'FixedRateSync("70kH",584)',
                                   'FixedRateSync("70kH",583)',
                                   'FixedRateSync("70kH",583)',
                                   'BeamRequest(0)','FixedRateSync("70kH",584)',
                                   'FixedRateSync("70kH",583)',
                                   'FixedRateSync("70kH",583)',
                                   'FixedRateSync("70kH",584)',
                                   'Branch.unconditional(0)',
                                   'FixedRateSync("1H",1)','Branch.unconditional(0)'],
                           'async_start':16},
         '90 Hz SimAC' : {'instr':['FixedRateSync("70kH",583)',
                                   'BeamRequest(0)','FixedRateSync("70kH",583)',
                                   'BeamRequest(0)','FixedRateSync("70kH",584)',
                                   'BeamRequest(0)','FixedRateSync("70kH",583)',
                                   'FixedRateSync("70kH",583)',
                                   'BeamRequest(0)','FixedRateSync("70kH",584)',
                                   'BeamRequest(0)','FixedRateSync("70kH",583)',
                                   'BeamRequest(0)','FixedRateSync("70kH",583)',
                                   'FixedRateSync("70kH",584)',
                                   'BeamRequest(0)','FixedRateSync("70kH",583)',
                                   'BeamRequest(0)','FixedRateSync("70kH",583)',
                                   'BeamRequest(0)','FixedRateSync("70kH",584)',
                                   'Branch.unconditional(0)',
                                   'FixedRateSync("1H",1)','Branch.unconditional(0)'],
                           'async_start':22},
         '10 Hz SimAC' : {'instr':['BeamRequest(0)','FixedRateSync("70kH",4*(583*2+584))',
                                   'Branch.unconditional(0)',
                                   'FixedRateSync("1H",1)','Branch.unconditional(0)'],
                           'async_start':3},
         '110 Hz SimAC' : {'instr':['FixedRateSync("70kH",583)',
                                    'BeamRequest(0)','FixedRateSync("70kH",583)',
                                    'BeamRequest(0)','FixedRateSync("70kH",584)',
                                    'BeamRequest(0)','FixedRateSync("70kH",583)',
                                    'BeamRequest(0)','FixedRateSync("70kH",583)',
                                    'BeamRequest(0)','FixedRateSync("70kH",584)',
                                    'Branch.conditional(line=5, counter=0, 2)',
                                    'Branch.conditional(line=0, counter=1, 9)',
                                    'Branch.unconditional(0)',
                                    'FixedRateSync("1H",1)','Branch.unconditional(0)'],
                           'async_start':14},
         }

    name = arg['name']
    if name in d:
        instr = ['instrset = []']
        for i in d[name]['instr']:
            #  Make custom replacements
            if 'request' in arg and i=='BeamRequest(0)':
                i = arg['request']
            if 'timeslots' in arg and 'ACRateSync(0,' in i:
                i = i.replace('ACRateSync(0,','ACRateSync({},'.format(arg['timeslots']))
            instr.append('instrset.append({})'.format(i))
        return {'instr':instr, 'async_start':d[name]['async_start']}
    else:
        raise ValueError('{} not in seqlookup'.format(name))
