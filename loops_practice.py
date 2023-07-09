# def alpha(user_rows, user_columns):
#
#     columns = 1
#     k = 1
#     while columns <= user_columns:
#         rows = 1
#         while rows <= user_rows:
#             print(chr(64+k), end=" ")
#             k = k + 1
#             rows += 1
#
#         print(" ")
#         columns += 1
#
# alpha(4,4)

# def astrisk(user_rows, user_columns):
#
#     columns = 1
#
#     while columns <= user_columns:
#         rows = 1
#         while rows <= user_rows:
#             if columns >= rows:
#                 print("*", end="")
#
#
#             rows += 1
#
#         print("")
#         columns += 1
#
# astrisk(4,4)
#
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

# def astrisk(user_rows, user_columns):
#
#     columns = 1
#     increase = 1
#     while columns <= user_columns:
#         rows = 1
#         while rows <= user_rows:
#             if columns >= rows:
#                 print(increase, end=" ")
#                 increase += 1
#
#             rows += 1
#
#
#         print(" ")
#         columns += 1
#
#astrisk(4,4)

# def astrisk(user_rows, user_columns):
#     columns = 1
#     increase = 1
#     while columns <= user_columns:
#         rows = 1
#         while rows <= user_rows:
#             if columns >= user_rows+1-rows:
#                  print(" *", end=" ")
#             else:
#                 print("", end=" ")
#
#
#
#             rows += 1
#
#
#         print(" ")
#         columns+=1
#
#
#
# astrisk(4,4)
#
#


