from pyo import *

class Sound:
  def __init__(self):
    self.s = Server().boot()
    self.env = CosTable([(0,0),(50,1),(500,.25),(8191,0)])
    self.wav = SquareTable(5)
    self.s.start()

    self.freqs = {}

    self.addfreq(440)

  def addfreq(self, freq):
    self.freqs[freq] = Freq(freq, self.env, self.wav)

  def play(self, freq):
    """Trigger a tone, note, signal, whatever"""
    self.freqs[freq].play()


class Freq:
  def __init__(self, freq, env, wav):
    self.trig = Trig()

    self.trigenv = TrigEnv(input = self.trig, table = env, dur = 0.250)

    self.osc = Osc(table = wav, freq = freq, mul = self.trigenv).out()
    self.osc2 = Osc(table = wav, freq = freq, mul = self.trigenv).out(1)

  def play(self):
    self.trig.play()

s = Sound()
