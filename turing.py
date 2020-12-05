def fileToMachine(filename, strip, start):
    machineTable = []
    f = open(filename, 'r')

    for line in f:
        line = line.split(',')
        if0 = [line[0], int(line[1])]
        if1 = [line[2], int(line[3])]
        machineTable.append(state(if0, if1))

    track = Track(strip, start)
    machine = TuringMachine(machineTable, machineTable[0], track)
    return machine    
    
class state:
    def __init__(self, ifscan0, ifscan1):
        self.ifscan0 = ifscan0
        self.ifscan1 = ifscan1

    def do(self, scan):
        if scan == 0:
            return self.ifscan0[0], self.ifscan0[1]
        if scan == 1:
            return self.ifscan1[0], self.ifscan1[1]
        
    
class TuringMachine:
    def __init__(self, states, state, track):
        self.states = states
        self.state = state
        self.track = track
        
    def runState(self):
        currentBlock = self.track.strip[self.track.i]
        action, move = self.state.do(currentBlock)

        self.state = self.states[move-1]

        if action == "S0":
            self.track.Erase()
        if action == "S1":
            self.track.Print()
        if action == "R":
            self.track.Right()
        if action == "L":
            self.track.Left()
        if action == "H":
            self.track.Halt()

    def compute(self):
        halt = self.track.halt
        while not halt:
            self.runState()
            self.track.show()
            halt = self.track.halt
    
class Track:
    def __init__(self, strip, i):
        self.strip = strip
        self.i = i
        self.halt = False

    def show(self):
        s = ""
        for t in range(len(self.strip)):
            block = str(self.strip[t])
            if t == self.i:
                block = '|' + block + '|'
            else:
                block = " " + block + " "
            s += block
        print(s)
        
    def Erase(self):
        self.strip[self.i] = 0
    def Print(self):
        self.strip[self.i] = 1
    def Right(self):
        self.i += 1
        if self.i >= len(self.strip):
            self.strip.append(0)
    def Left(self):
        self.i -= 1
        if self.i < 0:
            self.strip.insert(0, 0)
            self.i = 0
    def Halt(self):
        self.halt = True



'''
3.2 Example (Doubling the number of strokes). The machine starts off scanning the left-
most of a block of strokes on an otherwise blank tape, and winds up scanning the leftmost
of a block of twice that many strokes on an otherwise blank tape. The flow chart is shown
in Figure 3-5.
'''

'''
strip = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
i = 11
track = Track(strip, i)

machineTable = [state(["H", 1], ["L", 2]),
                state(["L", 3], ["L", 3]),
                state(["S1", 3], ["L", 4]),
                state(["S1", 4], ["R", 5]),
                state(["R", 6], ["R", 5]),
                state(["L", 7], ["R", 6]),
                state(["L", 8], ["S0", 7]),
                state(["L", 11], ["L", 9]),
                state(["L", 10], ["L", 9]),
                state(["R", 2], ["L", 10]),
                state(["R", 12], ["L", 11]),
                state(["H", 1], ["H", 1])]

turing = TuringMachine(machineTable, machineTable[0], track)
track.show()
turing.compute()
track.show()
'''

