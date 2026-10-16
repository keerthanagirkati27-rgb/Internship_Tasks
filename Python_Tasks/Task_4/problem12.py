# find average of list after converting into a set

def average(array):
    new=set(array)
    
   
    average=sum(new)/len(new)
    return average
