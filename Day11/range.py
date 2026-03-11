'''
  0 1 2 3 4
0         *
1       * *
2     * * *
3   * * * *
4 * * * * *

  0 1 2 3 4
0 * * * * *       
1 *       *
2 *       *
3 *       *
4 * * * * *




'''


n= int(input('enter the size: '))
for row in range(n*2):
    if row < n:
        print('*'*(row+1))
    else:
         print('*'*(2*n-row))


n= int(input('enter the size: '))
for row in range(n):
    
    if row < n:
        print('*'*(row+1))
    else:
         print('*'*(2*n-row))