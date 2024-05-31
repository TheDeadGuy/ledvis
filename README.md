# ledvis install
(Excuse me for the unordered readme. it's a mix of previous owner and me)

Install all requirements & dependencies @ https://github.com/TheDeadGuy/ledvis#requirements first
```
cd ~
git clone https://github.com/TheDeadGuy/ledvis.git
cd ledvis
cd ~/ledvis/Services
sed -i -e "s/<username>/"$USER"/g" ledvis.service flask.service
sudo cp * /etc/systemd/system/
```
To run use following command:
```
sudo systemctl start ledvis.service
```

`sudo` is needed because this we are starting a system service

## Requirements

This is meant to run on a Raspberry Pi. (original author used pi 3. I'm using pi 4)

 * rpi_ws281x
 * adafruit-ads1x15
 * screen
 * Flask

Run this to install the rpi_ws281x (LED) driver library (Be aware that this goes against best practices. If you want this done correctly. the package needs to be done under venv)
```
sudo pip3 install rpi_ws281x --break-system-packages
```

And run this to install the other dependencies - (Be aware that this goes against best practices. If you want this done correctly. the package needs to be done under venv)
```
pip install adafruit-ads1x15 --user --break-system-packages	# install the ADS1015 i2c library
sudo apt install screen python3-matplotlib python3-pyaudio python3-requests python3-flask		# get screen
```

We also need to disable audio taking ownership of PWM. to do this run this command
```
echo "blacklist snd_bcm2835" | sudo tee /etc/modprobe.d/alsa-blacklist.conf
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
sudo systemctl enable ledvis.service
```

I also found that one of the PWM channels wasn't initializing properly. To fix this i used the following entry in ```\boot\config.txt```
```dtoverlay=pwm-2chan,pin=12,func=4,pin2=13,func2=4```

If you have issues with it complaining about audio channels. it may be that the default audio device is being used. run "pyaudio_test.py" to get the device number and remember to put that in your config.py file
