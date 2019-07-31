def bubble_sort(origin_items, comp=lambda x, y: x > y):
    items = origin_items[:]
    for i in range(len(items)-1):
        swapped = False
        print('j1', range(i, len(items)-1-i))
        for j in range(i, len(items)-1-i):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                print(j, j+1, items)
                swapped = True
        if swapped:
            print('j2', range(len(items)-2-i, i, -1))
            swapped = False
            for j in range(len(items)-2-i, i, -1):
                if comp(items[j-1], items[j]):
                    items[j], items[j-1] = items[j-1], items[j]
                    print(j-1, j, items)
                    swapped = True
        if not swapped:
            break
    return items


if __name__ == '__main__':
    l = [5, 4, 8, 6, 9, 7, 3, 2, 1, 10]
    l = bubble_sort(l)
    print(l)
