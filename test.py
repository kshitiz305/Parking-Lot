# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# #
# # Complete the 'processLogs' function below.
# #
# # The function is expected to return a STRING_ARRAY.
# # The function accepts following parameters:
# #  1. STRING_ARRAY logs
# #  2. INTEGER maxSpan
# #
#
# def processLogs(logs, maxSpan):
#     # Write your code here
#     users = {}
#     max_span_user = []
#
#     for i in logs:
#         user_id, timestamp, action = i.split(" ")
#         if user_id not in users:
#             if action == "sign-in":
#                 users[user_id] = (int(timestamp), action)
#             else:
#                 users[user_id] = (int(timestamp), action)
#         elif user_id in users:
#             if action == "sign-out":
#                 if (int(timestamp) - users.pop(user_id)[0]) <= maxSpan:
#                     max_span_user.append(user_id)
#             else:
#                 if (users.pop(user_id)[0] - int(timestamp)) <= maxSpan:
#                     max_span_user.append(user_id)
#     srted_list = sorted([max_span_user])
#     print(srted_list)
#     return (srted_list)
#
#
# if __name__ == '__main__':
#
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     logs_count = int(input().strip())
#
#     logs = []
#
#     for _ in range(logs_count):
#         logs_item = input()
#         logs.append(logs_item)
#
#
#     maxSpan = int(input().strip())
#
#     result = processLogs(logs, maxSpan)
#
#     # fptr.write('\n'.join(result))
#     # fptr.write('\n')
#     #
#     # fptr.close()
#
#
#
#
#
print(1234)
def fun1(func):
    def inner():
        func()
    return inner

def fun(func):
    def inner2():
        print("Entering")
        func()
    return inner2

@fun
@fun1
def printer():
    print("1234")


function_count = 0
def func_count(fun):
    def inner():
        global function_count
        function_count +=1
        print(function_count)
        fun()
    return inner




@func_count
def addNumbers():
    pass

print(addNumbers())
print(addNumbers())

printer()