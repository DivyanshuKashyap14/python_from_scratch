#Q1
#n=int(input())
#if(n%2==0):
#    print("even")
#else:
#    print("odd")

#Q2
# n=int(input())
#print((n*(n+1))/2)

#Q3
# n=int(input())
#for i in range(1,11):
 #   print(n,"x",i,"=",n*i)

#Q6
#a = int(input())
#b = int(input())
#c = int(input())

#if a > b and a > c:
    #print("a is the largest:", a)
#elif b > a and b > c:
    #print("b is the largest:", b)
#else:
    #print("c is the largest:", c)

# for i in range (1,101):
#     print("Hello World")

# n=int(input("enter the number:"))
# for i in range(0,n):
#     print("Hello world")

# n=int(input("n:"))
# for i  in range (0,n):
#     print(i+1)

# n=int(input("n:"))
# for i in range(n,0,-1):
#     print(i)


# n=int(input("n:"))
# for i in range(0,n+2,2):
#     print(i,end=" ")
# print()
# for j in range(1,n+2,2):
#     print(j,end=" ")

# n=int(input("n:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)  #sum of n terms using for loop 

# n=int(input("n:"))
# fact=1
# for i in range(1,n+1):
#      fact=fact*i
# print(fact) #factorial


# n=int(input("n:"))
# for i in range (1,n+1):
#     if(n%i==0):
#         print(i,end=" ")  #factor


# n=int(input("n:"))
# sum=0
# for i in range (1,n):
#     if n%i==0:
#         sum+=i
# print(sum)
# if(sum==n):
#     print("Number is a perfect number")
# else:
#     print("Number is not a perfect number")  ##perfect number finder


# n=int(input("n:"))
# for i in range(2,n):
#     if(n%i==0):
#         print("number is not prime")
#         break
# else:
#     print("number is prime")


# a="DIVYANSHU"
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# print(b)


# n=(input("n:"))
# b=""
# for i in range(len(n)-1,-1,-1):
#     b=b+n[i]
# if b==n:
#     print("It is a palindrome")
# else:
#     print("not a palindrome")


# a="mc897rt5yt08y432@%$&*"
# char=0
# dig=0
# spchr=0
# for i in a:
#     if i.isdigit():
#         dig+=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr+=1
# print(f"Your digits are {dig}\nYour alphabets are {char}\nYour special char are {spchr}")


# a=256
# while a>0:
#     print(a%10,end=" ")
#     a=a//10


# a=int(input("n="))
# copy=a
# rev=0
# while a>0:
#     rev=rev*10 + a%10
#     a=a//10
# if(copy==rev):
#     print("yes")
# else:
#     print("no")


# import random
# num=random.randint(1,100)
# tries=0
# while True:
#     guess=int(input("guess the number:"))
#     if(num==guess):
#         tries +=1
#         print(f"you won,Total tries={tries}")
#         break
#     elif(num>guess):
#         print("go little higher")
#         tries +=1
#     elif(num<guess):
#         print("go little lesser")
#         tries +=1
#     else:
#         print("try again")    #GAME NUMBER GUESSING

# def sum(a,b):
#     print(f"sum:{a+b}")
# sum(12,45)


# def pallindrome(st):
#     rev=""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]
#     if(rev==st):
#         print("pallindrome")
#     else:
#         print("not a pallindrome")
# pallindrome("NAMAN")
# pallindrome("1234321")
# pallindrome("DIV")


# l=[-1,45,-3,44,-78,98,-97,65,-43,567,-146]
# print("Positive elements are:")
# for i in l:
#     if i>=0:
#         print(i,end=" ")
# print("\n\nNegative elements are:")
# for i in l:
#     if i<0:
#         print(i,end=" ")


# l=[3,5,3,6,7,4,76,89,54,14]
# sum=0
# for i in l:
#     sum+=i
# print(sum/len(l))


# l=[12,54,76,35,80,456,79,245,789,455,4,88,545,678,345]
# largest=l[0]
# index=0
# for i in range(len(l)):
#     if l[i]>largest:
#         largest =l[i]
#         index=i
# print(f"largest number is {largest} at index {index}")



# l=[23,56,24,456,354,47,46,654,756]
# largest=l[0]
# sec_largest=l[0]
# for i in l:
#     if i>largest:
#         sec_largest=largest
#         largest=i
# print(sec_largest)


# l=[2,6,3,1,4,8,5,7,9,0]
# for i in range(len(l)-1):
#     if l[i]<l[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("list is sorted")


# l= [1,2,1,3,1,4,3,5,4,6,4,3,3,5,4,2,3,1,3,2]
# d={}
# for i in l:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)


# a=int(input("n:"))
# try:
#     print(10/a)
# except Exception as err:
#     print(f"sorry there is an error as{err}")
# print("ok, i have done the division")


# a=23
# b=14
# temp=a
# a=b
# b=temp

# print(f"a={a},b={b}")

# n=int(input("temp in C="))
# print((n*1.8)+32)


# n=int(input("n:"))
# fact=1
# for i in range (1,n+1):
#     fact*=i
# print(fact)

# n=int(input("n:"))
# sum=0
# for i in range (0,n+1):
#     sum+=i
# print(sum)


# n=(int(input("n:")))
# rev=0
# while n>0:
#     digit=n%10
#     n=n//10
#     rev=rev*10+digit
# print(rev)


# n = int(input("n: "))
# count = 0

# while n > 0:
#     n //= 10
#     count += 1

# print(count)


# n=int(input("n:"))
# if n<=1:
#     print("not prime")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")


# for num in range(2, 101):

#     is_prime = True

#     for i in range(2, num):

#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num,end=" ")


# n=int(input("n:"))
# a=0
# b=1
# for i in range (0,n):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c

# a="ABCD"
# print(a[::-1])


# a="DIVYANSHU"
# a = a.lower()
# vowels=0
# consonants=0
# for ch in a:
#     if ch in "aeiou":
#         vowels+=1
#     else:
#         consonants+=1
# print(vowels)
# print(consonants)



# a=(input("n:")) 
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# if b==a:
#     print("palindrome")
# else:
#     print("not a palindrome")


# n=input("n:")
# freq={}
# for ch in n:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# print(freq)


# n=input("n:")
# n=n.upper()


# a="Hello world"
# result=""
# for ch in a:
#     if ch != " ":
#         result += ch
# print(result)


# a=("i am a good boy")
# words=a.split()
# longest = ""
# for word in words:
#     if len(word) > len(longest):
#         longest=word
# print(longest)


# a=("divyanshu")
# result=""
# vowel=['a', 'e', 'i', 'o', 'u']
# for i in a:
#     if i in vowel:
#         result+="*"
#     else:
#         result+=i
# print(result)


# a="divyanshu plays football and he is a right winger"
# a=a.split()
# print(len(a))


# l=[12,45,23,78,54,76,90,91]
# largest=l[0]
# for i in l:
#     if i>largest:
#         largest=i
# print(largest) 


# l=[12,45,23,78,54,76,90,91]
# largest=l[0]
# secondlargest=l[0]
# for i in l:
#     if i>largest:
#         secondlargest=largest
#         largest=i
#     elif i>secondlargest and i!=largest:
#         secondlargest=i
# print(secondlargest)



# l=[23,65,354,57,3,556,23,354,3,556]
# list=[]
# for i in l:
#     if i not in list:
#         list.append(i)
# print(list)


# a=[12,34,65,23,4,5,34,12,67,43]
# a.sort()
# print(a)


# l=[12,34,65,23,4,5,34,12,67,43]
# for i in range (len(l)):
#     for j in range(i+1,len(l)):
#         if l[j]<l[i]:
#             temp = l[i]
#             l[i] = l[j]
#             l[j] = temp
# print(l)


# l=[1,2,3,4,5]
# m=[6,7,8,9,0]
# merge=[]
# for i in l:
#     merge.append(i)
# for i in m:
#     merge.append(i)
# print(merge)


# l1 = [1,2,3,4,5,6]
# l2 = [1,7,3,9,0,6]
# new = []
# for i in l1:
#     if i in l2:
#         new.append(i)
# print(new)



# l=[1,2,3,4,5]
# l2=[]
# for i in l[::-1]:
#     l2.append(i)
# print(l2)