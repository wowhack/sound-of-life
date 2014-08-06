from pyo import *
from consts import *

class Sound:
  def __init__(self, freqs, vol):
    self.shape = CosTable([(0,0),(50,1),(500,.25),(8191,0)])
    self.wave = SawTable(12)

    self.vol = vol
    self.freqs = freqs
    self.q = []
    #self.freqs = []
    #for f in freqs:
      #self.freqs.append(Freq(f, self.shape, self.wave, vol))

  def play(self, freq):
    """Play a note"""
    self.q.extend([
        Sine(freq = self.freqs[freq % len(self.freqs)], mul = self.vol).out(dur = beat_duration),
        Sine(freq = 2*self.freqs[freq % len(self.freqs)], mul = self.vol).out(dur = beat_duration),
        Sine(freq = self.freqs[freq % len(self.freqs)], mul = self.vol).out(1, dur = beat_duration),
        Sine(freq = 2*self.freqs[freq % len(self.freqs)], mul = self.vol).out(1, dur = beat_duration)
      ])
    #self.freqs[freq % len(self.freqs)].play()


class Freq:
  def __init__(self, freq, shape, wave, vol):
    self.trig = Trig()

    self.trigenv = TrigEnv(input = self.trig, table = shape, dur = beat_duration*0.7)

    self.osc = Osc(table = wave, freq = freq, mul = self.trigenv * vol).out()
    self.osc2 = Osc(table = wave, freq = freq, mul = self.trigenv * vol).out(1)

  def play(self):
    self.trig.play()
