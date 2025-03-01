A = {'a', 'b', 'g', 'd', 'f', 'c'}
B = {'l', 'm', 'o', 'b', 'c', 'h'}
C = {'h', 'i', 'j', 'k', 'c', 'd', 'f'}

union_A_B = A | B 
print(f"a. How many elements are there in set A and B: {len(union_A_B)}")

only_in_B = B - (A | C)
print(f"b. How many elements are there in B that is not part of A and C: {len(only_in_B)}")

print("\nc. Show the following using set operations")

print(C - A)    
print(A & C)  
print(A & B | B & C) 
print((A & C) - {'c'})
print(A & B & C) 
print(B - (A | C)) 