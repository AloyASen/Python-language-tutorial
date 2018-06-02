### similar to the functionality of 
# multiple inheritance in c++
class Mario:
    def move():
        print('I am moving')
class Shroom():
    def eat_shroom():
        print('now I am big')
class BigMario(Mario, Shroom):
    # pass --- if you need a line but not do anything 


bm= BigMario()
bm.move()
bm.eat_shroom()