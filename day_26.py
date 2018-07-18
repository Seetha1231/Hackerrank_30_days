da,ma,ya=map(int,input().split())
de,me,ye=map(int,input().split())
val=0
if ye<ya:
    val+=10000*(ya-ye)
elif me<ma:
    val+=500*(ma-me)
elif de<da:
    val=15*(da-de)
if(ya<=1582 and ye<=1582):
    val=10000
elif(ya<=1582):
    val=0
if(ye>ya):
    val=0

    

print(val)
