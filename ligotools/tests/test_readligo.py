from ligotools import readligo as rl
import h5py
import json

def test_ligo_loaddata():
    fn_data = 'data/H-H1_LOSC_4_V2-1126259446-32.hdf5'
    try:
        strain, time, dq = rl.loaddata(fn_data, 'H1')
        # assert dq is not None 
        assert strain is not None
    except:
        print("Cannot find data file " +fn_data)
        print("FAILED.")
        assert False


def test_ligo_loadevents():
    eventname = 'GW150914'
    try:
        fnjson = "data/BBH_events_v3.json"
        try:
            events = json.load(open(fnjson,"r"))
        except IOError:
            print("Cannot find resource file "+fnjson)
            print("FAILED.")
            assert False
        
        # did the user select the eventname ?
        try: 
            events[eventname]
        except:
            print('You must select an eventname that is in '+fnjson+'! FAILED.')
            assert False
    except:
        print('Read events FAILED')
        assert False
   
