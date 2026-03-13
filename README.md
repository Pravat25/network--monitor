# Network Monitor

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Networking](https://img.shields.io/badge/Tool-Networking-red)
![Status](https://img.shields.io/badge/Status-Active-success)

## Overview

Network Monitor is a Python tool that checks the connectivity of multiple hosts by sending ping requests.

It can help identify whether a system is reachable on the network.

## Features

- Monitor multiple hosts
- Detect if host is UP or DOWN
- Simple command line interface

## Technologies Used

- Python
- OS module
- Platform module

## Project Structure
network-monitor
│
├── network_monitor.py
└── README.md


## How to Run

Clone repository:


git clone https://github.com/Pravat25/network-monitor.git


Navigate to folder:


cd network-monitor


Run script:


python network_monitor.py


## Example Output


Enter hosts to monitor (type 'done' when finished)

Host: google.com
Host: 8.8.8.8
Host: done

===== Network Monitoring Report =====

google.com : UP
8.8.8.8 : UP


## Disclaimer

Educational purposes only.
