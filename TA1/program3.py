print('Program 3')

print('\nA.')
rows = 5  

for i in range(1, rows + 1):  
    for j in range(rows - i):  
        print(" ", end="")  
    for k in range(1, i + 1):  
        print(k, end="")  
    print()
    
print('\nB.')
n = 1  

while n <= 5: 
    count = 1  
    
    while count <= n:
        print(n, end="")  
        count += 1  
        
    print()  
    n += 2  

n = 6 
count = 1
while count <= n:
    print(n, end="")
    count += 1
print()
    
n = 7
count = 1
while count <= n:
    print(n, end="")
    count += 1