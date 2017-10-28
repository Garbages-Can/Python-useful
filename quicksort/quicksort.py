def qsort(array: list) -> list:
    if len(array) <= 1:
        return array

    less, greater = [], []
    pivot = array.pop()
    for x in array:
        if x < pivot:
            less.append(x)
        else:
            greater.append(x)
    return qsort(less) + [pivot] + qsort(greater)


def main():
    arr = [6, 1, 27, 2, 9, 3, 10, 5, 8]
    arr = qsort(arr)
    print(arr)


if __name__ == '__main__':
    main()
