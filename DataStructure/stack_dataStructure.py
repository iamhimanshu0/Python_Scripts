#
# Himanshu Tripathi   STACK #
#


class stack():
    # initialize the stack
    def __init__(self):
        self.data = []

    # add items to the stack (push)
    def push(self, data):
        return self.data.append(data)

    # delete item for the stack(pop)
    def pop(self):
        return self.data.pop()

    # print the stack
    def print_stack(self):
        print(self.data)

    # get the upper value form the stack (peek value)
    def peek(self):
        print(self.data[-1])


s = stack()
s.push('A')
s.push('B')
s.pop()
s.push('1')
s.push('2')
s.push('C')
s.push('D')

s.peek()

s.print_stack()
