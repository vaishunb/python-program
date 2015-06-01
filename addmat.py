"""Program for Matrix addition"""
n1=int(raw_input('Enter how many row'))
n2=int(raw_input('Enter how many columns'))
a=[[0 for i in range(n1)]for j in range(n2)]
print "Enter Matrix A Elements"
for i in range(0,n1):
	for j in range(0,n2):
		a[i][j]=int(raw_input('Enter the number'))
b=[[0 for i in range(n1)]for j in range(n2)]
print "Enter Matrix B Elements"
for i in range(0,n1):
        for j in range(0,n2):
		b[i][j]=int(raw_input('Enter the number'))
c=[[0 for i in range(n1)]for j in range(n2)]
for i in range(0,n1):
	for j in range(0,n2):
		c[i][j]=a[i][j]+b[i][j]
print "The Addition of Two Matrix"
for i in range(0,n1):
        for j in range(0,n2):
		print '{:2}'.format(c[i][j]),
	print
