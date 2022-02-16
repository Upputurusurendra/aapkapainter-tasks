str2 = "Army"
str1 = "Mary"

str1 = str1.upper()

str2 = str2.upper()

# check if length is same
if(len(str1) == len(str2)):

    # sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # if sorted char arrays are same
    if(sorted_str1 == sorted_str2):
        print("Yes")
    else:
        print("No")

