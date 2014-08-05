from pyo import *

# Setup sound server
s = Server()
s.boot()

# Scales ??
scls = [[0,4,7,11,13,17,21,25,29,33],
        [0,7,12,14,17,21,24,29,31,34],
        [0,7,10,12,15,19,20]]

# Nice signals
env = CosTable([(0,0),(50,1),(500,.25),(8191,0)])
wav = SquareTable(5)

# Generates isochronous trigger signals.
# A trigger is an audio signal with a value of 1 surrounded by 0s.
met = Metro(time=.125, poly=8).play()

# Triggered X-class midi notes pseudo-random generator.
# Xnoise implements a few of the most common noise distributions. A new value
# is generated each time the object receive a trigger in input. 
# met is the input
note = TrigXnoiseMidi(met, dist="loopsef", x1=1, x2=.2, mrange=(48, 97))

# Snap input values on a user's defined midi scale.
snp = Snap(note, choice=scls[0], scale=1)

curscl = 0
def changeScl():
    # change the scale for snp.choice argument
    global curscl
    curscl = (curscl + 1) % len(scls)
    snp.choice = scls[curscl]
    print snp.choice


metscl = Metro(time=8).play()
tr = TrigFunc(metscl, function=changeScl)

c = TrigEnv(met, table=env, mul=.07)
d = Osc(table=wav, freq=snp, mul=c).out()
d1 = Osc(table=wav, freq=snp*0.999, mul=c).out()
d2 = Osc(table=wav, freq=snp*1.002, mul=c).out()
d3 = Osc(table=wav, freq=snp*0.997, mul=c).out()

# Start playing sounds
s.start()

# Show server gui
s.gui(locals())
