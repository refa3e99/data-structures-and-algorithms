from hashtable.hashtable import HashTable

h1 = HashTable()
h1.set('abdulrahman', 22)
h1.set('ahmed', 29)
h1.set('asaad', 19)
h1.set('malik', 23)

h2 = HashTable()
h2.set('abdulrahman', 'python')
h2.set('ahmed', 'JAVA')
h2.set('asaad', 'JavaScript')
h2.set('Roaa', 'PHP')


def left_join(h1, h2):
    keys1 = h1.key()
    keys2 = h2.key()
    table = []
    for i in keys1:
        table.append([i, str(h1.get(i))])
    for i in range(len(keys2)):
        if keys2[i] in keys1:
            table[i].append(h2.get(keys2[i]))
        else:
            table[i].append(None)
    return table


if __name__ == '__main__':
    print(left_join(h1, h2))
