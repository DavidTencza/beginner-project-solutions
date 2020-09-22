# 99 Bottles
bottles = 99

while bottles > 0:
    if bottles != 1:
        print(bottles, 'bottles of beer on the wall',end='\n')
        print(bottles, 'bottles of beer',end='\n')
    else:
        print(bottles, 'bottle of beer on the wall',end='\n')
        print(bottles, 'bottle of beer',end='\n')       
    bottles -= 1
    print('Take one down, pass it around',end='\n')
    if bottles != 1:
        print(bottles, 'bottles of beer on the wall',end='\n\n')
    else:
        print(bottles, 'bottle of beer on the wall',end='\n\n')     
