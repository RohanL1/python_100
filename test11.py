def revNum(x):
        digit=[]
        sign=1
        lmt=[-(2**31), (2**31) - 1]

        if x<0:
            sign=-1
            x=x*-1
        
        while abs(x) > 0:
            digit.append(x%10)
            x=x//10

        ans=0
        ln=len(digit)
        for i in range(ln-1,-1,-1):
            x=10**(ln-i-1)
            ans=ans+digit[i]*(x)

        ans=ans * sign
        return ans if ans <lmt[1] ans ans > lmt[0] else 0 

x=-11234
revX=revNum(x)
print ("Num : " + str(x) + " Rev Num : " + str(revX))