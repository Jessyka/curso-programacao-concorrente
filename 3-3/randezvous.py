#Desafio: Rendezvous
#Puzzle: Generalize the signal pattern so that it works both ways. 
# Thread A has to wait for Thread B and vice versa. In other words, given this code:
#Thread A                       Thread B
#1 statement a1                 1 statement b1
#2 statement a2                 2 statement b2
#we want to guarantee that a1 happens before b2 and b1 happens before a2. 
#In writing your solution, be sure to specify the names and initial values of your semaphores (little hint there).

import threading

#Thread A
def a_task(a1_action, b1_action):
    print("\nStatement a1 ")
    b1_action.release()
    a1_action.acquire()
    print("\nStatement a2")

#Thread B
def b_task(a1_action, b1_action):
    print("\nStatement b1")
    a1_action.release()
    b1_action.acquire()
    print("\nStatement b2")


def main():
    #Instanciando Semaforos
    a1_action = threading.Semaphore(0)
    b1_action = threading.Semaphore(0)

    #Instanciando Threads
    a = threading.Thread(target=(a_task), args=(a1_action, b1_action))
    b = threading.Thread(target=(b_task), args=(a1_action, b1_action))

    a.start()
    b.start()

main()
