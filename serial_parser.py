#!/usr/bin/env python
#
#  Copyright 2016 Alexis Pojomovsky <apojomovsky@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import os
import sys
import serial
import time
import argparse
import pdb

PORT = 'COM11'
BAUD = 9600

class serial_parser:
    def __init__(self, port = PORT, baud = BAUD, timeout = 0.5):
        self.port = port
        self.baud = baud
        self.timeout = timeout
        self.out_data = []
        self.in_data = []
        self._isSending = False
        self._isReceiving = False

    def connect(self):
        try:

            self.ser = serial.Serial(self.port, self.baud, timeout = self.timeout)
            time.sleep(2)
        except serial.SerialException:
            print "Serial port " + self.port + " cannot be open"
            sys.exit(0)
        print "Serial port " + self.port + " opened successfully"

    def generate_data(self, modeCA):
        command = []   
        if(modeCA =='Rf'):
            pass
        elif(modeCA =='Rb'):
            pass
        elif(modeCA =='Af'):
            pass

    def send_data(self,data):
        if not self._isReceiving:
            try:
                self._isSending = True
                self.out_data = data
                self.ser.write(self.out_data)
                self._isSending = False
            except serial.SerialException:
                self._isSending = False
                print "Unable to send data to " + self.port

    def read_data(self):
        if not self._isSending:
            if self.ser.is_open:
                try:
                    self._isReceiving = True
                    self.ser.in_data = self.ser.readline()
                    if self.ser.in_data:
                        self._isReceiving = False
                        return self.ser.in_data
                except serial.SerialException:
                    self._isReceiving = False
                    print "Cannot read data from " + self.port
            else:
                print "Unable to read from a closed port"

    def close(self):
        self.ser.close()

    def __del__(self):
        self.ser.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Serial communication for SDV project')
    parser.add_argument('-p', '--port', action='store',
                        dest='port', default=PORT,
                        help="COM port")
    parser.add_argument('-b', '--baud', action='store',
                        dest='baud', default=BAUD,
                        help="Baudrate")
    parser.add_argument('-t', '--timeout', action='store',
                        dest='timeout', default=0.1,
                        help="Timeout")
    args = parser.parse_args()

    comm = serial_parser(args.port, args.baud)
    comm.connect()
    for i in range(5):
        print "I've received: " + comm.read_data()
        time.sleep(1)