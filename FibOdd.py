inp = int(input("Enter a range-number for Fibonacci numbers in Odd Positions:"))
x,y =0,1
list = [ x,y]
for i in range(1,2*inp-1):
    f = x + y
    x =y
    y =f
    list.append(f)
print([list[x] for x in range(2*inp) if x%2 ==0])