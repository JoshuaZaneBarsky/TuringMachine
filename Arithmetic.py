from TM import TM

class Add:

    global X_IN, Y_IN, WORK, OUT
    X_IN, Y_IN, WORK, OUT = 0, 1, 2, 3

    def __init__(self, in_1, in_2, work, out):
        self.tm = TM(in_1, in_2, work, out)

    def add(self):
        while self.tm.get_state() != 'halt':
            self.run_addition_program()
            self.print_tapes()

    def print_tapes(self):
        print("--")
        self.tm.print_tapes()

    def run_addition_program(self):
        x, y, w = self.tm.tapes[X_IN][self.tm.position[X_IN]], self.tm.tapes[Y_IN][self.tm.position[Y_IN]], self.tm.tapes[WORK][self.tm.position[WORK]]
        match x, y, w,:
            case '▷', '▷', '▷':                                               self.do_begin_state()
            case b1, b2, '☐' if b1 in [0, 1] and b2 in [0, 1]:                 self.do_running_state1()
            case '☐', '☐', '☐':                                               self.do_running_state2()
            case b1, b2, b3 if b1 in [0, 1] and b2 in [0, 1] and b3 in [0,1]:   self.do_running_state3()
            case '▷', '▷', b if b in [0,1]:                                    self.do_running_state4()

    def do_begin_state(self):
        # READS
        x = self.tm.read(None)
        y = self.tm.read(None)
        w = self.tm.read(None)
        # MOVES
        self.tm.move(X_IN, 'right')
        self.tm.move(Y_IN, 'right')
        self.tm.move(WORK, 'right')
        self.tm.move(OUT, 'right')
        # WRITES
        self.tm.write(WORK, None)
        self.tm.write(OUT, None)
        # END
        self.tm.set_state('running')

    def do_running_state1(self):
        # READS
        x = self.tm.read(None)
        y = self.tm.read(None)
        w = self.tm.read(None)
        # MOVES
        self.tm.move(X_IN, 'right')
        self.tm.move(Y_IN, 'right')
        self.tm.move(WORK, None)
        self.tm.move(OUT, 'right')
        # WRITES
        self.tm.write(WORK, None)
        self.tm.write(OUT, None)
        # END
        self.tm.set_state('running')

    def do_running_state2(self):
        # READS
        x = self.tm.read(None)
        y = self.tm.read(None)
        w = self.tm.read(None)
        # MOVES
        self.tm.move(X_IN, 'left')
        self.tm.move(Y_IN, 'left')
        self.tm.move(WORK, None)
        self.tm.move(OUT, None)
        # WRITES
        self.tm.write(WORK, 0)
        self.tm.write(OUT, None)
        # END
        self.tm.set_state('running')

    def do_running_state3(self):
        # READS
        b1 = self.tm.read(X_IN)
        b2 = self.tm.read(Y_IN)
        b3 = self.tm.read(WORK)
        # MOVES
        self.tm.move(X_IN, 'left')
        self.tm.move(Y_IN, 'left')
        self.tm.move(WORK, None)
        self.tm.move(OUT, 'left')
        # WRITES
        self.tm.write(WORK, int( (b1 and b2) or (b1 and b3) or (b2 and b3) ) )
        self.tm.write(OUT, int( (b1 != b2) != b3 ) )
        # END
        self.tm.set_state('running')

    def do_running_state4(self):
        # READS
        x = self.tm.read(None)
        y = self.tm.read(None)
        w = self.tm.read(None)
        # MOVES
        self.tm.move(X_IN, None)
        self.tm.move(Y_IN, None)
        self.tm.move(WORK, 'left')
        self.tm.move(OUT, 'left')
        # WRITES
        self.tm.write(WORK, None)
        self.tm.write(OUT, None)
        # END
        self.tm.set_state('halt')