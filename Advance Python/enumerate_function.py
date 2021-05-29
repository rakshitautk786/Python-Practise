''' Print 3rs 5th and 7th element of list'''
l=[1,2,3,4,5,6,7,8,9,10]
for index,item in enumerate(l):
    if index==2 or index==4 or index==6:
        print(f"the {index+1}th element is  {item}")