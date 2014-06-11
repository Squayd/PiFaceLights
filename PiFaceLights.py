#!/usr/bin/env python3
#PiFaceLights
#Program to toggle LEDs on PiFaceDigital
#Interfaces with bootstrap-based webpage

import pifacedigitalio

class Board(object):
  #Easy wrapper for the piface
  def __init__(self):
    self.piface = pifacedigitalio.PiFaceDigital()
    self.piface.init()
    self.lights =[0,0,0,0,0,0,0,0]
  def lightOn (self, n):
    if ((n < 0) || (n > 7))
      print "LED out of range"
      return
    self.lights[n] = 1
    self.piface.leds[n].turn_on()
  def lightOff (self, n):
    if ((n < 0) || (n > 7))
      print "LED out of range"
      return
    self.lights[n] = 0
    self.piface.leds[n].turn_off()

if __name__ == "__main__"
  face = Board();
