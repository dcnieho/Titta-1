# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 08:39:57 2018

@author: Marcus
"""

from psychopy import core
import numpy as np

def get_defaults(et_name):
    
    settings = Settings(et_name)
    
    if et_name == 'IS4_Large_Peripheral':
        settings.SAMPLING_RATE = 90
    elif et_name == 'Tobii Pro Spectrum':
        settings.SAMPLING_RATE = 600    
        settings.TRACKING_MODE = 'human'
    elif et_name == 'Tobii Pro Nano':
        settings.SAMPLING_RATE = 60
    elif et_name == 'Tobii TX300':
        settings.SAMPLING_RATE = 300
    elif et_name == 'Tobii T60 XL':
        settings.SAMPLING_RATE = 60
    elif et_name == 'Tobii Pro X3-120 EPU':
        settings.SAMPLING_RATE = 120
    elif et_name == 'Tobii Pro X3-120':
        settings.SAMPLING_RATE = 120        
    elif et_name == 'X2-60_Compact':
        settings.SAMPLING_RATE = 60
    elif et_name == 'X2-30_Compact':
        settings.SAMPLING_RATE = 40        
    elif et_name == 'Tobii X60':
        settings.SAMPLING_RATE = 60     
    elif et_name == 'Tobii X120':
        settings.SAMPLING_RATE = 120   
    elif et_name == 'Tobii T60':
        settings.SAMPLING_RATE = 60   
    elif et_name == 'Tobii T120':
        settings.SAMPLING_RATE = 120           
    else:
        print('eye tracker type not supported')
        core.quit()
    return settings
    
    
class Connect(object):   
    def __init__(self, in_arg='dummy'):
        '''  in_arg can be either string with eye tracker name
        or 'settings' generated by calling (and optionally modifying)
        the output from get_defaults()
        '''
        
        if isinstance(in_arg, str):
            if 'dummy' in in_arg:
                from titta import Tobii_dummy
                self.__class__ = Tobii_dummy.Connect
                self.__class__.__init__(self)  
            else:            
                from titta import Tobii
                self.__class__ = Tobii.myTobii
                self.__class__.__init__(self, in_arg)
        else:
            from titta import Tobii
            self.__class__ = Tobii.myTobii
            self.__class__.__init__(self, in_arg)
            
            

class Settings(object):
    
    def __init__(self, et_name):
        ''' Default settings for eye tracker 
        '''
        
        self.graphics = Graphics()
        
        # Default name of et-data file
        self.FILENAME                    = 'test.tsv' 
        
        # Tracking parameters
        self.TRACKER_ADDRESS  = ''           # If none is given, find one on the network
        self.SAMPLING_RATE = 600             # Set sampling rate of tracker        
        self.eye_tracker_name = et_name
        self.TRACKING_MODE = 'Default'
        
        # Parameters for calibration
        self.PACING_INTERVAL = 1.0           # How long to present the dot until samples are collected
        self.AUTO_PACE = 1                   # autoaccept (2), semi autoaccept (1, accept first point, default) 
                                        # of accept with space bar (0)
                                            
        self.ANIMATE_CALIBRATION = True      # Static or animated calibration dots
        self.RECORD_EYE_IMAGES_DURING_CALIBRATION = False
        self.RECORD_EXTERNAL_SIGNAL_DURING_CALIBRATION = False
        self.N_CAL_TARGETS = 5               # Valid: 0, 1, 5, 9, 13        
        
        # List all possible calibration points (in Tobii's coordinate system)
        # (0.0, 0.0) is the upper left corner and (1.0, 1.0) is the lower right corner.
        
        # Define the 13 point array (reading order)
        self.CAL_TARGETS = np.array([[0.1, 0.1], [0.5, 0.1], [.9,.1], 
                           [.3,.3], [.7,.3], 
                           [.1,.5], [.5,.5], [.9,.5], 
                           [.3,.7], [.7,.7], 
                           [.1,.9], [.5,.9], [.9,.9]])
        
            
        self.VAL_POS_TOBII = np.array([[0.2, 0.5], [0.5, 0.8], [0.8, 0.5], [0.5, 0.2]])
        
        # CAL_POS_TOBII = np.array([[0.5, 0.5], [0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0],
        #                           [0.5, 1.0], [0.5, 0.0], [0.0, 0.5], [1.0, 0.5]])
        
        # if N_CAL_TARGETS == 0:
        #     CAL_POS_TOBII = []
        # elif N_CAL_TARGETS == 1:
        #     CAL_POS_TOBII = CAL_POS_TOBII[0, :]
        # elif N_CAL_TARGETS == 5:
        #     CAL_POS_TOBII = CAL_POS_TOBII[[0, 1, 2, 3, 4], :]  
            
        # # VAL_POS_TOBII = np.array([[0.2, 0.2], [0.2, 0.8], [0.8, 0.2], [0.8, 0.8]])    
        # VAL_POS_TOBII = np.array([[0.2, 0.5], [0.5, 0.8], [0.8, 0.5], [0.5, 0.2]]) 
            
        # # Scale the positions so they look good on the screen
        # scaling = 0.7
        # corr = 0.5 - (scaling * 0.5)
        # self.CAL_POS_TOBII = CAL_POS_TOBII * scaling + corr
        # self.VAL_POS_TOBII = VAL_POS_TOBII * scaling + corr    
        
class Graphics(object):
    
    def __init__(self):
        ''' Default settings for graphics
        '''            
        
        blue = tuple(np.array([37, 97, 163]) / 255.0 * 2 - 1)
        blue_active = tuple(np.array([11, 122, 244]) / 255.0 * 2 - 1)
        green = tuple(np.array([0, 120, 0]) / 255.0 * 2 - 1)
        red = tuple(np.array([150, 0, 0]) / 255.0 * 2 - 1)
        yellow = tuple(np.array([255, 255, 0]) / 255.0 * 2 - 1)
        yellow_linecolor = tuple(np.array([255, 255, 0]) / 255.0 * 2 - 1)
        
        self.blue = blue
        self.blue_active = blue_active
        
        self.TEXT_SIZE = 0.04 # Size of text
        self.TEXT_COLOR = 'white' 
        
        self.ET_SAMPLE_RADIUS = 0.1 # in deg
        
        # SIze of calibration dots
        self.TARGET_SIZE=0.6 # in deg
        self.TARGET_SIZE_INNER=self.TARGET_SIZE / float(5)  # inner diameter of dot
        
        # Theses parameters are changed directly in the EThead class
        # self.HEAD_POS_CIRCLE_FIXED_COLOR = blue
        # self.HEAD_POS_CIRCLE_FIXED_RADIUS = 0.25
        
        # self.HEAD_POS_CIRCLE_MOVING_COLOR = yellow
        # self.HEAD_POS_CIRCLE_MOVING_FILLCOLOR = yellow
        # self.HEAD_POS_CIRCLE_MOVING_RADIUS = 0.25
        # self.HEAD_POS_CIRCLE_MOVING_MIN_RADIUS = 0.05
        
        self.POS_CAL_BUTTON = (0.5, -0.8)
        self.COLOR_CAL_BUTTON =  green
        self.WIDTH_CAL_BUTTON = 0.30
        self.HEIGHT_CAL_BUTTON = 0.08
        self.CAL_BUTTON = 'space'
        self.CAL_BUTTON_TEXT = 'calibrate (spacebar)'
        
        self.POS_RECAL_BUTTON = (-0.5, -0.8)
        self.COLOR_RECAL_BUTTON =  red
        self.WIDTH_RECAL_BUTTON = 0.30
        self.HEIGHT_RECAL_BUTTON = 0.08
        self.RECAL_BUTTON = 'c'
        self.RECAL_BUTTON_TEXT = 're-calibrate (c)'
        
        self.POS_REVAL_BUTTON = (-0.21, -0.8)
        self.COLOR_REVAL_BUTTON =  red
        self.WIDTH_REVAL_BUTTON = 0.30
        self.HEIGHT_REVAL_BUTTON = 0.08
        self.REVAL_BUTTON = 'v'
        self.REVAL_BUTTON_TEXT = 're-validate (v)'
        
        # Button for showing eye images
        self.POS_SETUP_BUTTON = (-0.5, -0.8)
        self.COLOR_SETUP_BUTTON = blue
        self.WIDTH_SETUP_BUTTON = 0.30
        self.HEIGHT_SETUP_BUTTON = 0.08
        self.SETUP_BUTTON = 'e'
        self.SETUP_BUTTON_TEXT = 'eye images (e)'
        
        self.POS_ACCEPT_BUTTON = (0.5, -0.8)
        self.COLOR_ACCEPT_BUTTON = green
        self.WIDTH_ACCEPT_BUTTON = 0.30
        self.HEIGHT_ACCEPT_BUTTON = 0.08
        self.ACCEPT_BUTTON = 'space'
        self.ACCEPT_BUTTON_TEXT = 'accept (spacebar)'
        
        self.POS_BACK_BUTTON = (-0.5, -0.8)
        self.COLOR_BACK_BUTTON = blue
        self.WIDTH_BACK_BUTTON = 0.30
        self.HEIGHT_BACK_BUTTON = 0.08
        self.BACK_BUTTON = 'b'
        self.BACK_BUTTON_TEXT = 'basic (b)'
        
        self.POS_GAZE_BUTTON = (0.8, 0.8)
        self.COLOR_GAZE_BUTTON = blue
        self.WIDTH_GAZE_BUTTON = 0.25
        self.HEIGHT_GAZE_BUTTON = 0.08
        self.GAZE_BUTTON = 'g'
        self.GAZE_BUTTON_TEXT = 'show gaze (g)'
        
        self.POS_CAL_IMAGE_BUTTON = (-0.8, 0.8)
        self.COLOR_CAL_IMAGE_BUTTON = (0.2, 0.2, 0.2)
        self.WIDTH_CAL_IMAGE_BUTTON = 0.25
        self.HEIGHT_CAL_IMAGE_BUTTON = 0.08
        self.CAL_IMAGE_BUTTON = 's'
        self.CAL_IMAGE_BUTTON_TEXT = 'Show calibration (s)'
        
        self.SETUP_DOT_OUTER_DIAMETER = 0.03 # Height unit
        self.SETUP_DOT_INNER_DIAMETER = 0.005        
        
        # Parameters for eye images
        self.EYE_IMAGE_SIZE = (0.5, 0.25)
        self.EYE_IMAGE_SIZE_PIX = (175, 496)
        self.EYE_IMAGE_SIZE_PIX_FULL_FRAME = (512, 640)
        self.EYE_IMAGE_POS_L = (0.5, -0.4)
        self.EYE_IMAGE_POS_R = (-0.5, -0.4)
        
        # Parameters for tracking monitor (norm units)
        self.EYE_SIZE = 0.03
        self.EYE_COLOR_VALID = green
        self.EYE_COLOR_INVALID = red
        self.TRACKING_MONITOR_SIZE = [0.5, 0.5]
        self.TRACKING_MONITOR_POS = [0, 0.4]
        self.TRACKING_MONITOR_COLOR = [0.2, 0.2, 0.2]        
        
    