# Sense Hat

The [Raspberry Pi Sense HAT](https://www.raspberrypi.org/products/sense-hat/) features an 8x8 RGB LED matrix, a mini joystick and the following sensors:

* Gyroscope
* Accelerometer
* Magnetometer
* Temperature
* Humidity
* Barometric pressure


## Installation

To install the Sense HAT software, enter the following commands in a terminal::

```bash
sudo apt-get update
sudo apt-get install sense-hat
sudo reboot
```

## Usage

Hello world example:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.show_message("Hello world!")
```

