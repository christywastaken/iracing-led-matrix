# iRacing LED Matrix Display

This project is a dynamic LED Matrix Display system for iRacing telemetry data. It utilizes a Raspberry Pi 3, an Adafruit RGB Bonnet, and a 64 x 32 LED matrix to display various telemetry metrics in real-time during iRacing sessions. The telemetry data is obtained from iRacing using the pyirsdk package and displayed on the LED matrix using the rpi-rgb-led-matrix package. Numpy is used to create 2D matrices for displaying various elements on the LED Matrix. 

The system consists of two main parts:

- **Client App**: A client-side application that runs on the Raspberry Pi and displays data, received through a socket, on the LED Matrix.
- **Server App**: A server-side application that runs on your PC, fetches data from iRacing and sends it to the Client App through a socket.

## Prerequisites

- Raspberry Pi 3 (other rPi also work)
- Adafruit RGB Bonnet (optional)
- 64 x 32 LED Matrix
- Python
- pyirsdk
- rpi-rgb-led-matrix
- Numpy

## Installation

1. Install [Python](https://www.python.org/downloads/) on your Raspberry Pi and PC. 

2. Install the [pyirsdk](https://github.com/kutu/pyirsdk) Python package on your PC.

3. Instrcutions for wiring up your Raspberry Pi can be found [here](https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/wiring.md)

4. Clone the [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) package on your Raspberry Pi:

```
git clone https://github.com/hzeller/rpi-rgb-led-matrix.git
```

5. Build/Install the package:

```
sudo apt-get update && sudo apt-get install python3-dev python3-pillow -y
make build-python PYTHON=$(command -v python3)
sudo make install-python PYTHON=$(command -v python3)

```

4. Install Numpy on the RPi

```
pip install numpy
```

5. Clone this repo to your RPi and PC:

```
git clone https://github.com/christywastaken/iracing-led-matrix.git
```

## Usage
Before running the app, PC_IP to your PC local IP in client_app.py. This allows the client on the Raspberry Pi to connect to the PC through LAN.
```
PC_IP = '<YOUR_PC_IP>'
```

On your PC, navigate to the directory containing the project files (server) and run the server app:
```
python server_app.py
```

On your Raspberry Pi, navigate to the directory containing the project files (client) and run the client app:
```
sudo python3 client_app.py 
```