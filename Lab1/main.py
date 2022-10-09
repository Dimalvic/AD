from timeit import default_timer as timer
import random



NewTest1 = open("test1.txt",'w')
i = 0
start = timer()
while i < 135000000:
    rnumber = random.randint(-10000000, 10000000)
    NewTest1.write(str(rnumber) + " ")
    i += 1
NewTest1.close()
end = timer()
print( end - start )


def merge_lists(list1,list2):
    new_list = []
    A = len(list1)
    B = len(list2)
    a = 0
    b = 0
    while a < A and b < B:
        if list1[a] <= list2[b]:
            new_list.append(list1[a])
            a += 1
        else:
            new_list.append(list2[b])
            b += 1
    new_list += list1[a:] + list2[b:]
    return new_list

def merge_sort(x):
    Middle = len(x)//2
    left = x[:Middle]
    right = x[Middle:]
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)
    return merge_lists(left,right)





file = input("Enter file name: ")
file2 = open(file)
newlist = []
for line in file2:
    line = line.rstrip()
    numbers = line.split()
    for number in numbers:
        newlist.append(number)
file2.close()
start = timer()
newlist = merge_sort(newlist)
end = timer()
print( end - start )

Endfile = input("Enter file name: ")
Endfile2 = open(Endfile,"w")
for number in newlist:
    Endfile2.write(number + " ")
Endfile2.close()