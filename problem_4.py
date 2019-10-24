#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of 
#two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product 
#of two 3-digit numbers.

#num = [a, b, c, d, e, f]
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
isP = True

for i in range(999, 100, -1):
  for j in range(999, 100, -1):
    k = i * j
    #isPalindrom(k)
    if (100000 < k < 1000000) and isP:
      f = k % 10
      e = int(((k - f) / 10) % 10)
      d = int(((k - f - e * 10) / 100) % 10)
      c = int(((k - f - e * 10 - d * 100) / 1000) % 10)
      b = int(((k - f - e * 10 - d * 100 - c * 1000) / 10000) % 10)
      a = int(((k - f - e * 10 - d * 100 - c * 1000 - b * 10000) / 100000) % 10)
      
      if (a == f) and (b == e) and (c == d) and (a == 9):
        print("===============")
        print(k)
        print(a, b, c, d, e, f)
        print(i, j)

