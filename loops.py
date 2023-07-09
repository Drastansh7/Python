# num = 1
# while num <= 10:
#
#     print(num)
#     num = num + 1




# num = 1
# sum = 0
#
# while num <= 10:
#     sum += num
#     num += 1
# print(sum)



# user_num = int(input("Enter a num: "))
#
# num = 1
# sum = 0
#
# while num <= user_num:
#     print(num)
#     sum += num
#     num += 1
#
# print(sum)

# user_num = int(input("Enter a number: "))
#
# n = 1
#
# while n <= user_num:
#     print(n**3)
#     n += 1


# user_num = int(input("enter a number: "))
#
# n = 1
# while n <= 10:
#     print(str(user_num) + ' X ' + str(n) + ' = ', user_num*n)
#     n = n+1

# i = 1
# k=1
#
# while i <= 4:
#     j = 1
#     while j <= 4:
#         print(chr(96+k), end=" ")
#         k=k+1
#         j = j + 1
#
#
#     print(" ")
#     i = i + 1




i = 1
k = 1


while i <= 4:
    j = 1
    while j <= 4:
        if i >= j:
            print(k, end=" ")
            k = k + 1
        else:
            print(" ", end=" ")

        j = j + 1


    print(" ")
    i = i + 1







# def astrisk():
#
#     i = 1
#
#     while i <= 6:
#         j = 1
#         while j <= 6:
#             if i >= j:
#                 print('*', end=" ")
#
#
#
#             j = j + 1
#
#         print(" ")
#         i = i + 1
#
# astrisk()



# def astrisk(columns , rows):
#
#     columns_i = 1
#     while columns_i <= columns:
#         rows_j = 1
#         while rows_j <= rows:
#             if columns_i >= rows_j:
#
#                 print("*", end=" ")
#             rows_j = rows_j + 1
#
#         print(" ")
#         columns_i = columns_i + 1
#
# astrisk(4,4)

















