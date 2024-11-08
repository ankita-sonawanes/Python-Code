#[1] write a program that prints the numbers from 1 to 100
#for i in range(1,101):
 #   print(i)
#[2] for multiples of '3' print "fizz" instead of the number
# and for the multiples of '5' print "buzz".
for i in range(1,101):
    if i%15==0:  #disible by 15 reminder 0
        print("FIZZBUZZ")
    elif i%3==0:
        print("FIZZ")
    elif i%5==0:
        print("BUZZ")
    else:
        print(i)
