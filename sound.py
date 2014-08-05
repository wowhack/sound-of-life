from pyo import *

# Setup sound server
s = Server()
s.boot()

# Scales ??
scls = [
        [32, 32, 33]]

# Nice signals
env = CosTable([(0,0),(50,1),(500,.25),(8191,0)])
wav = SquareTable(5)

# Generates isochronous trigger signals.
# A trigger is an audio signal with a value of 1 surrounded by 0s.
met = Metro(time=.500, poly=1).play()

# Triggered X-class midi notes pseudo-random generator.
# Xnoise implements a few of the most common noise distributions. A new value
# is generated each time the object receive a trigger in input. 
# met is the input
# http://ajaxsoundstudio.com/pyodoc/api/classes/triggers.html#trigxnoisemidi
note = TrigXnoiseMidi(met, dist="triangular", x1=1, x2=.2, mrange=(48, 97))

# Snap input values on a user's defined midi scale.
snp = Snap(note, choice=scls[0], scale=1)

curscl = 0
def changeScl():
    # change the scale for snp.choice argument
    global curscl
    curscl = (curscl + 1) % len(scls)
    snp.choice = scls[curscl]
    print snp.choice


# time is time between triggers in seconds
metscl = Metro(time=2).play()
# calls function every time input sends a trigger
tr = TrigFunc(metscl, function=changeScl)

# reads table for 1 second when met triggers
c = TrigEnv(met, table=env, mul=.07)

# Osc reads a waveform from table 
d = Osc(table=wav, freq=snp, mul=c).out()
#d1 = Osc(table=wav, freq=snp*0.999, mul=c).out()
#d2 = Osc(table=wav, freq=snp*1.002, mul=c).out()
#d3 = Osc(table=wav, freq=snp*0.997, mul=c).out()

# Start playing sounds
s.start()

# Show server gui
s.gui(locals())
