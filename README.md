# ledvis install

Install all requirements & dependencies @ https://github.com/TheDeadGuy/ledvis#requirments first
```
git clone https://github.com/TheDeadGuy/ledvis.git
cd ledvis
cd /home/pi/ledvis/Services
cp * /etc/systemd/system/
```

To run use following command:
```
sudo systemctl start flask.service ledvis.service
```

`sudo` is needed because this we are starting a system service

## Requirements

This is meant to run on a Raspberry Pi. (original author used pi 3. I'm using pi 4)

 * rpi_ws281x
 * adafruit-ads1x15
 * screen
 * Flask

Run this to install the rpi_ws281x (LED) driver library
```
cd ~
git clone https://github.com/jgarff/rpi_ws281x.git
sudo apt install scons swig
cd rpi_ws281x
scons
cd python
sudo -H python setup.py build
sudo -H python setup.py install
```

And run this to install the other dependencies
```
pip install adafruit-ads1x15 --user	# install the ADS1015 i2c library
pip3 install Flask	--user			# get Flask (best to use python3)
sudo apt install screen python-matplotlib python-pyaudio		# get screen
```

## Repo Organization

 * **run.py** contains execture three processes: one to sample the ADC, one to process the data, and one to write to the LEDs
 * **visualizer.py** contains classes the define how to process a sample array into color values to be displayed
 * **sound_processing.py** contains functions for normalizing and smoothing the incoming audio signal
 * **masker.py** contains functions for create a color mask given an amplitude (used in `VooMeter` in `visualizer.py`)
 * **config.py** does what is sounds like it does

## To get it to run automatically on the Pi

Run the following commands:

```
sudo systemctl enable flask.service ledvis.service
```
 
