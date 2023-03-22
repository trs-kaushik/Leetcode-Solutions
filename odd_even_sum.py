m,k = 47,3
s = ['azbde','abcher','acegk']
sum = 0

for i in s:
        prev_pwr = 1
        for char in i:
                pwr = ord(char)**m
                value = pwr*prev_pwr
                prev_pwr = value
        sum+=prev_pwr
        
        
if sum % 2 ==0:
        print("EVEN")
else:
        print("ODD")
        
