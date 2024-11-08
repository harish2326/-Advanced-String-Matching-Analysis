x = input("Enter the main string: ")
y = input("Enter the string to compare: ")
num = input("Enter numbers separated by space: ")
separation = [int(number) for number in num.split()]

# Reverse of y
revY = y[::-1]
print("Reverse of y:", revY)

# Generate substrings for x, y, and revY
substringsX = [x[start:end] for start in range(len(x)) for end in range(start + 1, len(x) + 1)]
substringsY = [y[start:end] for start in range(len(y)) for end in range(start + 1, len(y) + 1)]
substringsRev = [revY[start:end] for start in range(len(revY)) for end in range(start + 1, len(revY) + 1)]

# Storage for matching substrings
storageY = [ele for ele in substringsX if ele in substringsY]
storageRevY = [ele for ele in substringsX if ele in substringsRev]

# Join matches and count occurrences
substrings = []
count1, count2 = 0, 0
i = 0

while i < len(x):
    match = None
    source = None
    
    # Check for the longest match in substringsY
    for j in range(len(x), i, -1):
        candidate = x[i:j]
        if candidate in substringsY:
            match = candidate
            source = 'substringsY'
            break

    # Check for the longest match in substringsRev (if longer than substringsY)
    for j in range(len(x), i, -1):
        candidate = x[i:j]
        if candidate in substringsRev and (match is None or len(candidate) > len(match)):
            match = candidate
            source = 'substringsRev'
            break

    # Add matches and update counters
    if match:
        substrings.append(match)
        if source == 'substringsY':
            count1 += 1
        elif source == 'substringsRev':
            count2 += 1
        i += len(match)
    else:
        print("No further matches in arrays")
        break

# Calculate final result using counts and separation numbers
if len(separation) >= 2:
    yCal = count1 * separation[0]
    revYCal = count2 * separation[1]
    final_result = yCal + revYCal
else:
    final_result = 0

# Output
print("Selected substrings:", substrings)
print("Substrings from substringsY:", count1)
print("Substrings from substringsRev:", count2)
print("The final answer:", final_result)
























































































# x = input("enter the main string :")
# y = input("enter the string to compare :")
# num = input("enter a number seperated by space :")
# separation = [int(number) for number in num.split()]

# revY = y[:: -1]
# print("reverse :",revY)
# substringsX = []
# substringsY = []
# substringsRev = []
# lengthX = len(x)
# lengthY = len(y)
# lengthRevY = len(revY)
# storageY = []
# storageRevY = []
# # possible output of x
# for start in range(lengthX):
#     for end in range(start+1,lengthX+1):
#         substringX = x[start:end]
#         substringsX.append(substringX)
        
# # print("output of X :",substringsX)
# # possible output of y
# for start in range(lengthY):
#     for end in range(start+1,lengthY+1):
#         substringY = y[start:end]
#         substringsY.append(substringY)
        
# # print("output of Y :",substringsY)

# # possible output of revy
# for start in range(lengthRevY):
#     for end in range(start+1,lengthRevY+1):
#         substringRevY = revY[start:end]
#         substringsRev.append(substringRevY)
# print("output of rev Y :",substringsRev)
# #compare with y
# for ele in substringsX:
#     for eleY in substringsY:
#         if ele == eleY:
#             storageY.append(eleY)
# # print("selected ele from y:",storageY)
# #compare with rev y
# for ele in substringsX:
#     for eleRevY in substringsRev:
#         if ele == eleRevY:
#             storageRevY.append(eleRevY)
# print("selected ele from rev Y:",storageRevY)



# #want to join


# substrings = []
# # Counters for the number of substrings taken from y and revY
# count1, count2 = 0, 0  
# i = 0

# while i < len(x):
#     match = None
#     source = None  

    
#     for j in range(len(x), i, -1):
#         candidate = x[i:j]
#         if candidate in substringsY:
#             match = candidate
#             source = 'substringsY'
#             break

    
#     for j in range(len(x), i, -1):
#         candidate = x[i:j]
#         if candidate in substringsRev and (match is None or len(candidate) > len(match)):
#             match = candidate
#             source = 'substringsRev'
#             break

   
#     if match:
#         substrings.append(match)
#         if source == 'substringsY':
#             count1 += 1
#         elif source == 'substringsRev':
#             count2 += 1
#         i += len(match)  
#     else:
       
#         print("there is no elements in the array")




# for index,number in enumerate(num):
#     if index == 0:
#         yCal = count1*number
#     if index == 1:
#         revY = count2*number

# # Test Case
# print("Selected substrings:", substrings)
# print("Substrings from substringsY:", count1)
# print("Substrings from substringsRev:", count2)
# print("the final answer :",yCal + revY)
# print(count1)
# print(count2)
# print(yCal)
# print(revY)




