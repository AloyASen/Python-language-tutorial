# what the heck is a class  ?
## the class groups similar features together 

## the init function in the class are the costructors

class Enemy:
    life = 3

    def __init__(self):
        print("Enemy created")

    def attack(self):
        print('ouch')
        self.life -= 1
    def  checklife(self):
        if self.life <=0:
            print('ian dead')
        else:
            print(str(self.life)+ 'life left')


#create an object 
Enemy1 = Enemy()
Enemy1.attack()
Enemy1.checklife()

#class variables are different from instance varibles