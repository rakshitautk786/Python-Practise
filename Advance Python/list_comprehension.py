''' print table by list comprehension'''

n=int(input("Enter number"))
table=[ n*i for i in range(1,11)]
print(table)