A = {'a', 'b', 'g', 'd', 'f', 'c'}
B = {'l', 'm', 'o', 'b', 'c', 'h'}
C = {'h', 'i', 'j', 'k', 'c', 'd', 'f'}

union_A_B = A | B 
print(f"a. How many elements are there in set A and B: {len(union_A_B)}")

only_in_B = B - (A | C)
print(f"b. How many elements are there in B that is not part of A and C: {len(only_in_B)}")

print("\nc. Show the following using set operations")

list_i = list(C - A)
list_i.sort()
print("i.", list_i)

list_ii = list(A & C)
list_ii.sort()
print("ii.", list_ii)

list_iii = list((A & B) | (B & C))
list_iii.sort()
print("iii.", list_iii)

list_iv = list((A & C) - {'c'})
list_iv.sort()
print("iv.", list_iv)

list_v = list(A & B & C)
list_v.sort()
print("v.", list_v)

list_vi = list(B - (A | C))
list_vi.sort()
print("vi.", list_vi)