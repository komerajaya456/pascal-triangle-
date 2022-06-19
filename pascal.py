inp=int(input('enter rows u want:'))
pi=['']

asu=[]

def arran(listin1,y):
	pol=listin1
	x=' '
	for l in range(0,len(listin1)):
		if y%2==0:
			listin1[l]=str(listin1[l])+' '
		else:
			listin1[l]=' '+str(listin1[l])
		x=x+listin1[l]
	
	
	div=len(x)//2
	numsp=80-div
	print(' '*(numsp-10),'Row-',l-1,x,' '*(numsp-4))
	
  



def list(len):
	for i in range(1,len+1):
	
		lis=[0]*(i+2)
		
		
		
		for k in range(0,i):
			one=1
			if i==1:
				lis[one]=1
			else:
				
				lis[k+1]=pi[k+1]+pi[k]
	
		asu.append(lis)

		pi=lis
				
			
list(inp)

for ikl in range(0,len(asu)):
		opp=asu[ikl]
		arran(opp,ikl)
		