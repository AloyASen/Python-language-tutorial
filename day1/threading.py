#sendin and receiving messages --app1

import threading
class BuckysMessanger(threading.Thread):
    def run(self):
        # this _ variable is not at all required later 
        #therrefore in python and golang
        for _ in range(10):
            print(threading.current_thread().getName())

x=BuckysMessanger(name='send out messages')
y= BuckysMessanger(name='receive messages') 
x.start()
y.start()