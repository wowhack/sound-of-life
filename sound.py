from pyo import *
from consts import *
import time 

class Sound:
  def __init__(self, freqs, vol):
    self.env = CosTable([(0,0),(50,1),(500,.25),(8191,0)])
    self.wav = SquareTable(12)

    self.freqs = []
    for f in freqs:
      self.freqs.append(Freq(f, self.env, self.wav, vol))

  def play(self, freq):
    """Play a note"""
    self.freqs[freq % len(self.freqs)].play()


class Freq:
  def __init__(self, freq, env, wav, vol):
    self.trig = Trig()

    self.trigenv = TrigEnv(input = self.trig, table = env, dur = beat_duration)

    self.osc = Osc(table = wav, freq = freq, mul = self.trigenv * vol).out()
    self.osc2 = Osc(table = wav, freq = freq, mul = self.trigenv * vol).out(1)

  def play(self):
    self.trig.play()
