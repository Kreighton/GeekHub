# 3. Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
#        Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
#        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

def remove_empties(implist):
    newlist = []
    for i in range(len(implist)):
        if implist[i]:
            newlist.append(implist[i])
    return newlist


listOfTuples = [(), (), ('Fill', '', 'This'), (), (' ',), ('Tuples',), (5, 6, 7), ('?')]

print(f"Test input: {listOfTuples}")
print(f"Result: {remove_empties(listOfTuples)}")
