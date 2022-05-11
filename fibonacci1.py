#program to display the fibonacci sequence
nterms=int(input("how many terms"))
n1=0
n2=1
count=0
if terms<=0
     print("please enter a positive integer")
#if there is only one term ,return n1
elif nterms==1:
     print("fibonacci sequence upto",nterms,":")
     print(n1)
#generate fibonacci sequence     
else:
     print("fibonacci sequence:")
     while count<nterms:
         print(n1)
         nth=n1+n2
         #update the values
         n1=n2
         n2=nth
         count+=1
