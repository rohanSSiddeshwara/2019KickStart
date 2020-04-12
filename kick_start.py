s=[]
sol=[]
i=1
t=0
c=0
case_no=1
with open('input.txt','r') as f:       #to get input from text file 
	for line in f: 				       #to iterate through  every lines
		if i%2!=0:
			a,b=line.split(' ')		   #to get input where a=number of houses ,b=dollars
			a=float(a)				   #to convert string to float 
			b=float(b)
		else :
			l=line.split(' ')
			s=[float(d) for d in l]	   #to convert each end every element into float  points 	
			print(s)
			s.sort()
#----------------------------------- actual logic starts from here
			for term in s:
				if term<=b:
					c+=1
					b-=term
			print('case',case_no,'=',c)
			c=0
			case_no+=1
		i+=1
		






	