def twonumsum(array, targetsum):
    for i in range(len(array)-1):
        firstsum = array[i]
        for j in range(i+1, len(array)):
             secondsum = array[j]
             if firstsum + secondsum = targetsum:
                return [firstsum, secondsum]
    
    return[]

    
