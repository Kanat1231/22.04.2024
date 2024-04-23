def mutiple(x, y):
    return (x * y)
a = mutiple(4, 4)
print(a)


def mutiple(x, y):
    print(x * y)
a = mutiple(4, 8)
print(a)

def mutiple(x, y):
    pass
a = mutiple(4, 8)
print(a)

def mutiple(x, y):
    print(x*y)
    return x+y
a = mutiple(4, 8)
print(a)

def mutiple(x, y = 10):
    print(x*y)
    return x+y
a = mutiple(4)
print(a)

def check_numbers(x, y):
    if x + y < 100:
        return "100 ден кышы"
    else:
        return "100 ден улкен"
print(check_numbers(58,50))


def finnd_max(list1):
    return max(list1)
print(finnd_max([1,2,3,4,5]))

def find_max(list1):
    my_list_max = list1[0]
    for i in list1:
        if i > my_list_max:
            my_list_max = i
    return my_list_max

print(find_max([1,2,-1,4,5]))

def find_min(list1):
    my_list_min = list1[0]
    for i in list1:
        if i < my_list_min:
            my_list_min = i
    return my_list_min

print(find_min([1,2,1,-2,9]))



def find_max(list1):
    maximum_number = list1[0]
    a=0
    for i in range (len(list1)):
        if list1[i] > maximum_number:
            maximum_number = list1[i]
            total = i
    return total

print(find_max([2,4,11,3,22]))







