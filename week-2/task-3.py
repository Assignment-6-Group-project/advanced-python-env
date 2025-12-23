eq = input("Input: ").replace(" ", "")
a_val = eq[0]
op = eq[1]
b_val = eq[2]
equal = eq[3]
c_val = eq[4]

def to_int(char):
    if char != "x":
        return int(char) 
    else:
        return None

a = to_int(a_val)
b = to_int(b_val)
c = to_int(c_val)

if a_val == 'x':
    if op == '+':
        x = c - b
    else:  # op == '-'
        x = c + b
elif b_val == 'x':
    if op == '+':
        x = c - a
    else:  # op == '-'
        x = a - c
elif c_val == 'x':
    if op == '+':
        x = a + b
    else:  # op == '-'
        x = a - b

print("x =", x)










