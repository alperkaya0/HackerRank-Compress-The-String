# Enter your code here. Read input from STDIN. Print output to STDOUT

nums = list(map(lambda x: int(x),list(input())))

indices = []
for x in range(1,len(nums)):
    if (nums[x-1] != nums[x]) and (nums[x-1] != "," and nums[x] != ","):
        indices.append(x)

plus = 0
for x in indices:
    nums.insert(x+plus,",")
    plus = plus + 1

temp = ""

for x in nums:
    temp += str(x)

temp = temp.split(",")

for idx,x in enumerate(temp):
    temp[idx] = "("+str(len(x))+", "+x[0]+") "

string = ""

for x in temp:
    string += x
string = string.strip()
print(string)
