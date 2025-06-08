# **********3*******
#crontab -e
#30 6 * * * python path/file.py //6:30am every day

from TicketInit import *
from StubHub import UpdateStubHub
from GameTime import UpdateGameTime
#from TickPick import UpdateTickPick
from VividSeats import UpdateVividSeats

t = time.time()
start()

#UpdateStubHub()
UpdateGameTime()
#UpdateTickPick()
#UpdateTicketMaster()

#UpdateCheapest(time.time()-t)
#save()

