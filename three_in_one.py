# Describe how you could use a single array to implement three stacks.

class ThreeStacks:
    def __int__(self,size):
        self.size = size
        self.lst = [None] * 3 * size
        self.top = [0,0,0]

    def push(self,data,stacknum):
        if stacknum < 3 and stacknum >= 0:
            lst[stacknum * size + top[stacknum]] = data
            top[stacknum] ++

    def pop(self,stacknum):
        if stacknum <3 and stacknum >= 0:
            temp = lst[top[stacknum]]
            lst[top[stacknum]] = None
            top[stacknum]--
            return temp

    def size(stacknum):
        return top[stacknum]