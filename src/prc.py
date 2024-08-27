#input list 
numbers_list=list(map(float,input("Enter the list:").split()))

#sum
def sum(list):
    init_sum=0
    for i in list:
        init_sum=init_sum+i
    return init_sum
#avg
def avg(list):
  return  sum(list)/len(list)
#max
def max(list):
   max=list[0]
   for num in list: 
      if num>max:
          max=num
   return max

#min
def min(list):
   min=list[0]
   for num in list:
      if num<min:
          min=num
   return min

print(sum(numbers_list))
print(avg(numbers_list))
print(max(numbers_list))
print(min(numbers_list))