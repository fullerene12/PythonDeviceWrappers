# Python Device Wrappers

These are python wrappers for controlling laboratory hardware devices. The majority of work was done at the [Molecular Foundary](http://foundry.lbl.gov/facilities/imaging_and_manipulation_of_nanostructures/index.html) at Lawrence Berkeley National Laboratory, and the [Murthy Lab](https://vnmurthylab.org/) at Harvard University.

## Getting Started

### Prerequisites

All packages are written with [Anaconda Python 3.6 distribution](https://www.anaconda.com/download/), numpy is needed for most of the packages.

```
conda install numpy
```


### Installing

You could clone this repository, or download specific wrapper file for the device you are using. Each device wrapper will contain a README for detailed instruction.

## List of drivers

* **arduino_motor**  - arduino control for one single stepper motor
* **arduino_odometer**  - arduino control for odometer modified from a PS/2 computer mouse
* **arduino_sol**  - arduino control of 4 channel analog solenoid valves, using 4 MCP4821 DAC chip
* **arduino_sol8**  - arduino control of 8 channel analog solenoid valves, using 1 MAX528 DAC chip
* **camera**  - generic webcam wrapper 
* **daq_ai**  - NI-DAQmx analog input wrapper
* **daq_do**  - NI-DAQmx digital output wrapper
* **daqmotor**  - tracking device control wrapper, the device is made up of 2 stepper motor controlled by NI-DAQ
* **flircam**  - FLIR camera wrappers
* **thorcam**  - Thorlabs camera wrappers

## Contributors

* **Hao Wu** - *Creator* - [fullerene12](https://github.com/fullrene12)
* **Vikrant Kapoor** - *hardware design*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Edward Barnard for the ScopeFoundry framework [edbarnard](https://github.com/edbarnard)
* Daniel Dietz for uc480 code [ddietz](http://ddietze.github.io/Py-Hardware-Support/index.html)
* Frank Ogletree for getting me started using python for hardware control