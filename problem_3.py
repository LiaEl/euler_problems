#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

x = 13195 

fact = []

def isPrime(n):
  for i in range(2, n):
    if n % i == 0:
      #print(n, "is not prime")
      break
  else:
    print(n, "is Prime")

#isPrime(x)

for i in range(2, x):
  if x % i == 0:
    fact.append(i)

for i in fact:
  isPrime(i)
