nums = []
for i in range(1, 6):
    num = int(input("Enter number " + str(i) + ":"))
    nums.append(num)

total = sum(nums)
avg= total / 5
larg = max(nums)
small = min(nums)

print("Total :", total)
print("Average :", avg)
print("Largest:", larg)
print("Smallest :", small)


