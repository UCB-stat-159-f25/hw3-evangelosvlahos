from ligotools.utils import whiten, write_wavfile, reqshift
from ligotools import readligo as rl
import h5py
import json
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.interpolate import interp1d

def test_utils_whiten():
    fn_data = 'data/H-H1_LOSC_4_V2-1126259446-32.hdf5'
    try:
        fs = 4096
        strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_data, 'H1')
        NFFT = 4*fs
        Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
        psd_H1 = interp1d(freqs, Pxx_H1)
        dt = 0.000244140625
        strain_H1_whiten = whiten(strain_H1,psd_H1,dt)
        print(strain_H1_whiten)
        assert strain_H1_whiten is not None 
    except:
        print("Cannot find data file " +fn_data)
        print("FAILED.")
        assert False

def test_utils_reqshift():
    fn_data = 'data/H-H1_LOSC_4_V2-1126259446-32.hdf5'
    try:
        fs = 4096
        fshift = 400.
        strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_data, 'H1')
        NFFT = 4*fs
        Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
        psd_H1 = interp1d(freqs, Pxx_H1)
        dt = 0.000244140625
        strain_H1_whiten = whiten(strain_H1,psd_H1,dt)
        strain_H1_shifted = reqshift(strain_H1_whiten,fshift=fshift,sample_rate=fs)
        assert strain_H1_shifted is not None
    except:
        print("Cannot find data file " +fn_data)
        print("FAILED.")
        assert False