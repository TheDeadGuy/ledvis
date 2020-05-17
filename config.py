import numpy as np

# PYAUDIO CONFIGURATION
CHUNK_SIZE 		=  2**8	 # How many audio samples to read in per step
FORMAT 			= 8
NUM_CHANNELS 	= 2	      # Number of audio channels
SAMPLING_FREQ	= 48000  # Sampling frequency of incoming audio
DEVICE_INDEX 	= 0      # Which audio device to read from (listed in pyaudio_test.py)

# RUN CONFIGURATION
PRINT_LOOP_FREQUENCY = True
SAMPLE_ARRAY_SIZE = 4 * CHUNK_SIZE
DEFAULT_REQUIRED_SAMPLES = SAMPLE_ARRAY_SIZE

# VISUALIZER CONFIG (Now obsolete. Incorporated into webpage)
WEBPAGEOVRIDE  = 1       # 0 for no. 1 for yes. If 1 values below become redundant
VOOMETER_RAND  = 0       # 0 for no. 1 for yes. If 0 below values become active.
VOOMETER_RED   = 255     # Between 0 and 255
VOOMETER_GREEN = 0       # Between 0 and 255
VOOMETER_BLUE  = 255     # Between 0 and 255

#STRIPS FIXED COLOUR (Now obsolete. Incorporated into webpage)
WEBPAGEOVERIDE = 1       # 0 for no. 1 for yes. If 1 values below become redundant
FIXED_RED      = 255     # Between 0 and 255
FIXED_GREEN    = 0       # Between 0 and 255
FIXED_BLUE     = 255     # Between 0 and 255

# LED STRIPS CONFIGURATION
LED_1_COUNT      = 30     # Number of LED pixels.
LED_1_PIN        = 19      # GPIO pin connected to the pixels (must support hardware PWM! Pi4 pins GPIO 12, 13, 18 & 19 (Pins 18 & 12 tied to same pwm signal aswell as 13 & 19).
LED_1_FREQ_HZ    = 600000  # LED signal frequency in hertz (usually 800khz)
LED_1_DMA        = 10      # DMA channel to use for generating signal (Between 1 and 14)
LED_1_BRIGHTNESS = 50      # Set to 0 for darkest and 255 for brightest
LED_1_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_1_CHANNEL    = 1       # 0 or 1 (Pins 18 & 12 for channel 0. Pins 13 & 19 for channel 1)

LED_2_COUNT      = 30     # Number of LED pixels.
LED_2_PIN        = 12      # GPIO pin connected to the pixels (must support hardware PWM! Pi4 pins GPIO 12, 13, 18 & 19 (Pins 18 & 12 tied to same pwm signal aswell as 13 & 19).
LED_2_FREQ_HZ    = 600000  # LED signal frequency in hertz (usually 800khz)
LED_2_DMA        = 10      # DMA channel to use for generating signal (Between 1 and 14)
LED_2_BRIGHTNESS = 50      # Set to 0 for darkest and 255 for brightest
LED_2_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_2_CHANNEL    = 0       # 0 or 1 (Pins 18 & 12 for channel 0. Pins 13 & 19 for channel 1)

LED_WRITE_DELAY  = 0.0045   # wait (in seconds) after writing to each LED strip

# ADC CONFIGURATION
ADC_GAIN = 4
ADC_CHANNEL = 0
ADC_MIN = -2048
ADC_MAX = 2048

# SERVER CONFIGURATION
SERVER_ADDRESS = 'pi-visualizer'
SERVER_PORT    = 5000

