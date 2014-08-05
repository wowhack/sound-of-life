from pyo import *

class Sound:
  def __init__(self):
    self.s = Server().boot()

    self.trig = Trig()

    self.env = CosTable([(0,0),(50,1),(500,.25),(8191,0)])
    self.wav = SquareTable(5)

    self.trigenv = TrigEnv(input = self.trig, table = self.env, dur = 0.250)

    self.osc = Osc(table = self.wav, freq = 440, mul = self.trigenv).out()

    self.s.start()


  def play(self):
    """Trigger a tone, note, signal, whatever"""
    self.trig.play()
