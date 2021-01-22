#1110
origin = n= int(input()) 
count = 0

while True : 
    a = n//10 + n%10 #십의자리수 + 일의자리수
    new = (n%10)*10 + a%10 #(n의 일의자리수 -> 십의자리수) + a의 일의자리수
    n = new #update n
    count +=1 #사이클 길이를 구하기 위해
    if new == origin :
        print(count)
        break

