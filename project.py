class Envelope:
    def __init__(self,num):
        self.paper = 0
        self.isTear = False
        self.giver = None
        self.received = None 
        self.num = num
    
    def pack(self,paper, giver, recieved):
        if(self.isTear==False):
            self.paper = paper
            self.giver = giver
            self.received = recieved
            return True
        else:
            return False

    
    def tear(self):
        self.isTear = True
        open = self.paper
        return open
    

envelopes = []

while True:
    option = int(input("Enter 1 - taking an envelope, 2 - packing, 3 - tearing, 4 - exit: "))
    if(option==1):
        envelopeNum = int(input("Enter the number of your envelope: "))
        envelope = Envelope(envelopeNum)
        envelopes.append(envelope)
    elif(option==2):
        envelopeNum = int(input("Enter the number of your envelope: "))
        present = False
        for envelope in envelopes : 
            if(envelope.num == envelopeNum):
                paper = int(input("How many papers would you like to pack? "))
                giver  = input("Name of the giver: ")
                recieved = input("Name of the reciever: ")
                envelope.pack(paper, giver, recieved)
                print("Envelope packed sucessfully!")
                present = True
        if not present : 
            print("Envelope doesn't exist")
    elif(option==3):
        envelopeNum = int(input("Enter the number of your envelope: "))
        present = False
        for envelope in envelopes:
            if(envelope.num == envelopeNum):
                print(envelope.tear())
                print("Package was teared.")
                present = True
        if not present : 
            print("Envelope doesn't exist")
    
    elif option == 4 : break 

    else : print("Invalid input don't use this app please ")
