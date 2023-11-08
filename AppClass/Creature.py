from random import randint

class creature:
    
    def __init__(self, name, health, attack, defence, damage):
        self.name = name
        self.health = health
        self.full = health
        self.attack = attack
        self.defence = defence
        self.damage = damage
        self.state = True
        
    def IsAlive(self):
        print('chack')
        if(self.health < 0):
            print('dead')
            return False
        return True
        
    def LookAt(self):
        pass
    
    def AttackRoll(self, roll, damage, name):
        if(self.state == True):
            if(roll > self.defence):
                print('##')
                print(combatText.txt['attack'][ randint(0, len(combatText.txt['attack'])-1)])
                self.health -= damage
                print(self.health)
                self.state = self.IsAlive()
        print('gaws at a corps')

    def MakeAttacks(self, target):
        print(self.name + 'is attacking ' + target.name)
        for n in range(self.attack):
            number = randint(0, 5)
            print(number)
            target.AttackRoll(number, self.damage, self.name)


class combatText():  
    txt ={
        'dead':['rips out there gut', 'stompson there head untill it expodes like a zit',
              'Rip there arm of and beat them to death with the wet end', 'Rips out the gugluer with there teath',
              'rams the hand down the thought', 'Kicks the stomic out though there spine'],
        'corps':['Start eating the corps', 'They start to have.. No that is just wrong',
               'They rip the corps a part', 'They pay to the dark gods',
               'Tea bacging', 'They dance on the corps'],
        'attack':['Attack with hate in there eyes','Attack with lust. What',
                'Bool curdling scream','Gaw',
                'Bite','The lafd maniclay']}
    


def main():
    
    
    creatureArray = []
    creatureArray.append(creature('Frodo', 10, 5, 3, 3))
    creatureArray.append(creature('Sam', 10, 1, 2, 2))
    creatureArray.append(creature('Merry', 10, 1, 3, 2))
    creatureArray.append(creature('Pippin', 10, 1, 3, 2))
    print(creatureArray[0].name + ' is attacking ' +creatureArray[1].name)
    creatureArray[0].MakeAttacks(creatureArray[1])
    creatureArray[0].IsAlive()
    print(creatureArray[1].state)
    creatureArray.pop(1)
    
    print(creatureArray[1].name)

    

if __name__== '__main__':
    main()
            
        
            
        
