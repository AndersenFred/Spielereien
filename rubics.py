
class Rubics_two():

    def __init__(self):
        self.front = ('o','o','o','o')
        self.right = ('w','w','w','w')
        self.up = ('b','b','b','b')
        self.left = ('y','y','y','y')
        self.back = ('r','r','r','r')
        self.bottom = ('g','g','g','g')

    def turn(self):
        front_after = (self.bottom[0],self.right[1],self.front[2],self.bottom[3])
        Right_after = (self.back[0],self.back[1],self.right[2],self.right[3])
        up_after = (self.right[0], self.up[0],self.up[1],self.front[3])
        left_after = (self.front[1],self.left[2], self.left[3], self.front[0])
        back_after= (self.left[0], self.up[2],self.up[3], self.back[3])
        bottom_after = (self.back[2], self.bottom[1],self.bottom[2], self.left[1])
        self.front = front_after
        self.right = Right_after
        self.up = up_after
        self.left =  left_after
        self.back = back_after
        self.bottom = bottom_after

    def origin(self):
        if (self.front[0]==self.front[1]==self.front[2]==self.front[3]):
            if (self.right[0]==self.right[1]==self.right[2]==self.right[3]):
                if (self.up[0]==self.up[1]==self.up[2]==self.up[3]):
                    if (self.left[0]==self.left[1]==self.left[2]==self.left[3]):
                        if (self.back[0]==self.back[1]==self.back[2]==self.back[3]):
                            if (self.bottom[0]==self.bottom[1]==self.bottom[2]==self.bottom[3]):
                                return True
        return False

    def go(self):
        i=0
        while(True):
            i+=1
            self.turn()
            if(self.origin()):
                return i
                break

    def print_front(self):
        print(self.front)

    def print_all(self):
        print('Front: ', self.front)
        print('right: ', self.right)
        print('up: ', self.up)
        print('left: ', self.left)
        print('back: ', self.back)
        print('bottom: ', self.bottom)
        print('\n')


class Rubics_three():

    def __init__(self):
        self.front   = ('o','o','o','o','o','o','o','o','o')
        self.right   = ('w','w','w','w','w','w','w','w','w')
        self.up      = ('b','b','b','b','b','b','b','b','b')
        self.left    = ('y','y','y','y','y','y','y','y','y')
        self.back    = ('r','r','r','r','r','r','r','r','r')
        self.bottom  = ('g','g','g','g','g','g','g','g','g')

    def origin(self):
        if (self.front[0]==self.front[1]==self.front[2]==self.front[3]==self.front[4]==self.front[5]==self.front[6]==self.front[7]==self.front[8]):
            if (self.right[0]==self.right[1]==self.right[2]==self.right[3]==self.right[4]==self.right[5]==self.right[6]==self.right[7]==self.right[8]):
                if (self.left[0]==self.left[1]==self.left[2]==self.left[3]==self.left[4]==self.left[5]==self.left[6]==self.left[7]==self.left[8]):
                    if (self.up[0]==self.up[1]==self.up[2]==self.up[3]==self.up[4]==self.up[5]==self.up[6]==self.up[7]==self.up[8]):
                        if (self.back[0]==self.back[1]==self.back[2]==self.back[3]==self.back[4]==self.back[5]==self.back[6]==self.back[7]==self.back[8]):
                            if (self.bottom[0]==self.bottom[1]==self.bottom[2]==self.bottom[3]==self.bottom[4]==self.bottom[5]==self.bottom[6]==self.bottom[7]==self.bottom[8]):
                                return True
        return False

    def turn(self):
        front_after = (self.bottom[0],self.bottom[1],self.right[2],self.bottom[3],self.bottom[4],self.right[5],self.bottom[6],self.bottom[7],self.front[8])
        Right_after = (self.back[0],self.back[1],self.back[2],self.back[3],self.back[4],self.back[5],self.right[6],self.right[7],self.right[8])
        up_after = (self.right[0],self.right[1], self.up[0],self.right[3],self.right[4],self.up[1],self.front[6],self.front[7],self.up[2])
        left_after = (self.front[2], self.front[5], self.left[8], self.front[1], self.front[4],self.left[7],self.front[0],self.front[3],self.left[6])
        back_after= (self.left[0],self.up[5], self.up[8],self.left[3],self.up[4],self.up[7],self.back[6],self.up[3],self.up[6])
        bottom_after = (self.back[8],self.back[7],self.bottom[2],self.left[5],self.left[4], self.bottom[5],self.left[2],self.left[1],self.bottom[8])

        self.front = front_after
        self.right = Right_after
        self.up = up_after
        self.left =  left_after
        self.back = back_after
        self.bottom = bottom_after

    def print_all(self):
        print('Front: ', self.front)
        print('right: ', self.right)
        print('up: ', self.up)
        print('left: ', self.left)
        print('back: ', self.back)
        print('bottom: ', self.bottom)
        print('\n')

    def go(self):
        i=1
        self.turn()
        print(self.origin())
        while(not self.origin()):
            self.turn()
            i+=1
        return i
