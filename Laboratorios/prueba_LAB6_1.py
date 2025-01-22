from Laboratorio_6.stack import Stack

if __name__ == "__main__":
    
    stack = Stack()
    
    for num in [2, 4, 6, 8, 10]:
        stack.push(num)

    while not stack.isEmpty():
        print(stack.pop())
        
    #if not stack.isEmpty():
    #    print(stack.top())
