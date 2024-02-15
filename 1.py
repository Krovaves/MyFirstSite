nums = [0,1,2,2,3,0,4,2]
val = 2
n = 0
for i in range(len(nums)):
    try:
        nums.remove(val)
        n += 1
    except ValueError:
        pass

print(n)
print((nums))
