x = int (input()) 
y = int (input()) 
n = int (input()) 
print([ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )])