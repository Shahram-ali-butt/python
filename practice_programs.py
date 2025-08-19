num_list = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
str_list = ["apple", "orange", "dragon fruit", "banana", "guava", "apple"]
total = 0
n = 10
num = 3931
is_prime  = True
my_str = "python is a very powerfull language!"
inverted_string = ""

# ************  Total number of negative numbers in a list ****************
# for elem in num_list:
#     if elem < 0:
#         total += 1
# print("Total number of negative numbers in given list is:", total)

# ************ Table of a given number except 5th iter *******************
# for i in range(1, n+1):
#     if i == 5:
#         continue
#     else:
#         print(f"{num} X {i} = {num*i}")

# ************************* Inverting a string ***************************
# for char in my_str:
#     inverted_string =  char + inverted_string
# print(inverted_string)

# ************* First non-repeating character in a string ****************
# for char in my_str:
#     if my_str.count(char) == 1:
#         print("The first non repeating character is:", char)
#         break

# *********************** Evaluating user input **************************
# while True:
#     user_int = int(input("Enter any number from 1 to 10: "))
#     if(1 <= user_int <= 10):
#         break

# ********************** Evaluating a prime number ***********************
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num ,"is divisible by", i,". Hence is not prime.")
#             is_prime = False
#             break
# if is_prime:
    #  print(f"{num} is prime")

# *************** Checking first duplicate in a list ********************
# unique_set = set()
# for item in str_list:
#     if item in unique_set:
#         print("Dupicate Item: ",item)
#         break
#     unique_set.add(item)

# ************** Different ways of handeling precision ******************
# print("{:.3f}".format(2.3456789))
# print('%.3f' % 2.3456789)
# print(f"{2.3456789:0,.3f}")
# print(round(2.3456789, 3))

# ************* Generator Function (Yields enven numbers) ***************
# def evennumbers(limit):
#     for i in range(2, limit + 1, 2):
#         yield i
# for i in evennumbers(20):
#     print(i)

# **************** Taking variable number of parameters *****************
# def allsum(*args):
#     return sum(args)
# print(allsum(1,2,3,4,5,6,7,8,9,10))

# *************** Giving named parameters using **kwargs ****************
# def define_character(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
    # for key in kwargs.keys():
    #     print(f"{key}")
    # for value in kwargs.values():
    #     print(f"{value}")

# define_character(Name = "superman", Powers = "Laser eyes, super strong", Weaknesses = "Kryptonight")
# define_character(Name = "Batman", Powers = "Rich", Weakness = "self doubt", )

# ************************* Closures and scope ***************************
# my_var = 2
# def f1(someVar):
#     def f2(someOtherVar):
#         return someOtherVar ** someVar
#     return f2
# calc_square = f1(2)
# calc_cube = f1(3)
# print(calc_square(my_var), calc_cube(my_var))

