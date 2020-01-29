import heapq

list_1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list_2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(heapq.nsmallest(3, list_1))
print(heapq.nlargest(3, list_1))
print(heapq.nlargest(2, list_2, key=lambda x: x['price']))
print(heapq.nlargest(2, list_2, key=lambda x: x['shares']))
