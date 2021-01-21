#2438 -1
t = int(input())

for i in range(t) : 
    print('*'*(i+1))

#2438 -2
i= 0
exec("i+=1;print('*'*i);"*int(input()))



#2439 -1
t = int(input())

for i in range(t) : 
    print(" "*(t-i-1) + ('*'*(i+1)))

#2439 -2
i= 0
t = int(input())
exec("i+=1;print(' '*(t-i) + '*'*i);"*t)

