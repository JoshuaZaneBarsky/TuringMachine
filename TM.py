# Turing machine object

global STATE

class TM:

    def __init__(self, x, y, w, o):
        self.tapes = [x, y, w, o] # [x, y, work, out]
        self.position = [0,0,0,0] # head positions
        self.set_state('begin')

    # -- move head -- #
    def move(self, i, direction):
        if direction == 'right':
            self.move_right(i)
        elif direction == 'left':
            self.move_left(i)
        else:
            return
        
    def move_right(self, i):
        if i == None:
            return None
        self.position[i] += 1

    def move_left(self, i):
        if i == None:
            return None
        self.position[i] -= 1
    
    # -- read and write -- #
    def read(self, t):
        if t == None:
            return None
        return self.tapes[t][self.position[t]]
    
    def write(self, t, data=None):
        if data == None:
            return None
        self.tapes[t][self.position[t]] = data

    # -- set and get state -- #
    def set_state(self, state):
        global STATE
        STATE = state
    
    def get_state(self):
        global STATE
        return STATE
    
    # -- print -- #
    def print_tapes(self):
        global STATE
        first = len(str(self.tapes[0]))
        second = len(str(self.tapes[1]))
        third = len(str(self.tapes[2]))
        fourth = len(str(self.tapes[3]))
        longest = self.get_longest_string(first, second, third, fourth)
        print("Program state: " + STATE)
        print(str(self.tapes[0])  + self.adjust_spacing(longest - first) + " Position: " + str(self.position[0])) 
        print(str(self.tapes[1])  + self.adjust_spacing(longest - second) + " Position: " + str(self.position[1])) 
        print(str(self.tapes[2])  + self.adjust_spacing(longest - third) + " Position: " + str(self.position[2])) 
        print(str(self.tapes[3])  + self.adjust_spacing(longest - fourth) + " Position: " + str(self.position[3]))

    def adjust_spacing(self, n):
        return " "*n 

    def get_longest_string(self, a, b, c, d):
        return max(a,b,c,d)




    