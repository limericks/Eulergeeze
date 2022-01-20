previous = 0
num = 1
num_list = []
while previous < 4000001:
    current = num + previous
    num = previous
    previous = current
    num_list.append(num)

num_sum = 0
for number in num_list:
    if number % 2 == 0:
        num_sum += number

print(num_list)
print(num_sum)
