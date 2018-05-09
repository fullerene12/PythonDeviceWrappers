from PyDAQmx import *
from ctypes import byref, c_ulong,c_int32
import numpy as np

class DAQSimpleDITask(Task):
    '''
    a simple task that read one digital input line
    '''
    
    def __init__(self,chan= 'Dev2/port0/line5'):
        '''
        chan: name of the chanel, in the format of Dev2/port0/line0
        '''
        Task.__init__(self)
        self.chan = chan
        self.CreateDIChan(self.chan,'',DAQmx_Val_ChanPerLine)
        
    def write(self,timeout = 0.0001):
        '''
        read a single sample from the digital line
        
        timeout: timeout in seconds
        '''
        read_array = c_int8(0)
        written = c_int32(0)
        wrrten2 = c_int32(0)
        self.WriteDigitalLines(1,timeout,DAQmx_Val_GroupByScanNumber,read_array,byref(written),byref(written2),None)
        return read_array
        
  
    def close(self):
        '''
        close task
        '''
        self.ClearTask()