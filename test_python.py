# import module sys to get the type of exception
import sys

randomList = [1,'a', 0, 2]

# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 1/int(entry)
#         # break
#     except Exception as e:
#         print("Oops!", e.__class__, "occurred.")
#         print("Next entry.")
#         print()
# print("The reciprocal of", entry, "is", r)

for element in randomList:
    try:
        print("Element: ", element)
        r = 1/int(element)
        print(r)
    except:
        pass
    # except (ValueError, ZeroDivisionError):
    #     print("Value should be a number and greater than '0'")