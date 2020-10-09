# CheesyQuotes
The goal of this project is to connect e-ink screen to a rpi and display random quotes. Enjoy :)

# Motivation
The motivation behind this project is too decorate our homes and inspire ourselves.
Moreover, the second goal is too learn how to make an electronic project and how to use an e-ink screen.

# Technologies

### RPI
A Raspberrypi 0 w is used in this project with a small python scrip to retrieve and display quotes

##### Hardware
 - Raspberry pi zero w
 - micro-usb chip 
 - Electric cables
 - 5 volt power supply with 10 amps
 - waveshare e-ink 2.13inch display
 - 3D printed box

# Features
- Display quotes at different intervals
- Display quotes from different categories

# How to use
#### **Commands for Systemd**
 - sudo nano /lib/systemd/system/cheesyquotes.service 
 - sudo chmod +x /lib/systemd/system/cheesyquotes.service
 - sudo systemctl daemon-reload
 - sudo systemctl enable cheesyquotes.service
 - sudo systemctl status cheesyquotes.service

#### **Command for Cronjobs**
 - sudo crontab -e
 - sudo crontab -l

# Installation
 #### Rpi
 1. Enable SSH, VNC and SPI in interfaces configuration
 2. Install Git, Python and Pip :
    - sudo apt install git
    - sudo apt install python3
    - sudo apt-get install python3-pip
 3. Install requirements : sudo pip3 install -r requirements.txt
 4. Add Systemd unit file to systemd deamon
    - sudo cp cheesyquotes.service /lib/systemd/system/
    - sudo chmod +x /lib/systemd/system/cheesyquotes.service
    - sudo systemctl daemon-reload
    - sudo systemctl enable cheesyquotes.service
    - sudo systemctl status cheesyquotes.service
 5. Reboot
    - sudo reboot

# Credits
n/a

# Liscense
MIT

# RoadMap
*September 2020*
- [x] Complete script
- [x] Assemble the electronics of the projet
- [x] Create a 3d printed box for the rpi0w and e-ink screen

