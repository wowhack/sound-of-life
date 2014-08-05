from pyo import *

class Sound:
  def __init__(self, freqs):
    self.env = CosTable([(0,0),(50,1),(500,.25),(8191,0)])
    self.wav = SawTable(12)

    self.freqs = []
    for f in freqs:
      self.freqs.append(Freq(f, self.env, self.wav))

  def play(self, freq):
    """Play a note"""
    self.freqs[freq % len(self.freqs)].play()


class Freq:
  def __init__(self, freq, env, wav):
    self.trig = Trig()

    self.trigenv = TrigEnv(input = self.trig, table = env, dur = 0.5)

    self.osc = Osc(table = wav, freq = freq, mul = self.trigenv).out()
    self.osc2 = Osc(table = wav, freq = freq, mul = self.trigenv).out(1)

  def play(self):
    self.trig.play()

s = Server().boot()
s.start()

ss = Sound([311.13, 349.23, 392.0, 415.30, 466.16, 523.25, 587.33])
