from functools import reduce

nums = [1,2,3,4,5]

sum = reduce(lambda el,sum:sum+el,nums,0)

print(sum)