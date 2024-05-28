            # Question 4 // Soru 4

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#Palindromik bir sayı her iki şekilde de aynı şeyi okur. 2 basamaklı iki sayının çarpımından elde edilen en büyük palindrom 9009 = 91*99.
#Üç basamaklı iki sayının çarpımından elde edilen en büyük palindromu bulun.

largest_palidrom = 101
for i in range (100,1000):
    for j in range(100,1000):
        asd = i*j
        if str(asd) == str(asd)[::-1]:
            check_palidrom = asd
            if check_palidrom > largest_palidrom:
                largest_palidrom = check_palidrom
                a = i
                b = j

print(largest_palidrom)
print(a,b)





