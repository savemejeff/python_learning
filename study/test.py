import time


def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def main():
    start = time.time()
    origin_items = [10, 50, 25, 5, 600]
    origin_items = select_sort(origin_items)
    end = time.time()
    for item in origin_items:
        print(item)
    time_cost = end - start
    print('time_cost:'+str(time_cost))


if __name__ == '__main__':
    main()
