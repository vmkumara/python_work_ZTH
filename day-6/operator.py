## Arthematic operator
a = 10
b = 5

sum_result = a + b
difference_result = a - b
product_result = a * b
division_result = a / b

print("sum:", sum_result)
print("difference:", difference_result)
print("product:", product_result)
print("division:", division_result)





## Relational operator
c = 20
d = 15
less_than = c < d
greater_than = c > d
less_than_or_equalto = c <= d
greater_than_or_equalto  = c >= d
equalto = c == d
not_equalto = c != d

print("c < d:", less_than)
print("c > d:", greater_than)
print("c <= d:", less_than_or_equalto)
print("c >= d:", greater_than_or_equalto)
print("c == d:", equalto)
print("c != d:", not_equalto)





## Logical operator
x = True
y = False

and_result = x and y
or_result = x or y
not_result_x = not x
not_result_y = not y

print("x and y:", and_result)
print("x or y:", or_result)
print("not x:", not_result_x)
print("not y:", not_result_y)




## Assignment operator
total = 10

total += 5  # t=10, t= 10+5=15,
total -= 3  # t=15, t= 15-3=12,
total *= 2  # t=12, t= 12*2=24,
total /= 4  # t=24, t= 24/4=6.0.

print("final_total:", total)




## Identity operators
my_list = [1, 2, 3, 4, 5]
a = my_list
b = [1, 2, 3, 4, 5]

is_same_object = a is my_list
is_not_same_object = b is not my_list

print("a is my_list:", is_same_object)
print("b is not my_list:", is_not_same_object)





## Membership operators
my_list = [1, 2, 3, 4, 5]
element_in_list = 3 in my_list
element_not_in_list = 6 not in my_list

print("3 in my_list:", element_in_list)
print("6 not in my_list:", element_not_in_list)
