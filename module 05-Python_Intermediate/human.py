class Head:
    pass
class Torso:
    def __init__(self,head,right_arm,left_arm,right_leg,left_leg):
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        self.head = head
class Arm:
    def __init__(self,hand):
        self.hand = hand
class Hand:
    pass
class Leg:
    def __init__(self,feet):
        self.feet = feet
class Feet:
    pass
class Human:
    def __init__(self,torso):
        self.torso = torso
        
def main ():
    rigth_hand = Hand()
    rigth_arm = Arm(rigth_hand)
    rigth_feet = Feet()
    rigth_leg = Leg(rigth_feet)
    letf_hand = Hand()
    letf_arm = Arm(letf_hand)
    letf_feet = Feet()
    letf_leg = Leg(letf_feet)
    head = Head()
    torso =Torso(head,rigth_arm,letf_arm,rigth_leg,letf_leg)
    human = Human(torso)
    human.torso.left_arm.hand
    print(human.torso.left_arm.hand is letf_hand)

    
    



if __name__ == "__main__":
    main()


