s=[]
sol=[]
i=1
t=0
c=0
case_no=1
with open('input.txt','r') as f:       #to get input from text file 
	for line in f: 				       #to iterate through  every lines
		if i%2!=0:
			a,b=line.split(' ')
			a=float(a)
			b=float(b)
		else :
			l=line.split(' ')
			s=[float(d) for d in l]
			print(s)
			s.sort()
			for term in s:
				if term<=b:
					c+=1
					b-=term
			print('case',case_no,'=',c)
			c=0
			case_no+=1
		i+=1
		






	