from Laboratorio_6.queue import Queue

if __name__ == "__main__":
    
    queue = Queue()
    
    for num in [2, 4, 6, 8, 10]:
        queue.enqueue(num)

    while not queue.isEmpty():
        print(queue.dequeue())
        
    #if not queue.isEmpty():
    #    print(queue.First())
