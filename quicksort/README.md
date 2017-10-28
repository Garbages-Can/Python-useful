<small>quicksort.py</small>
```python
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
```

### 快速排序原理
(这里的快速排序是二路归并)

假设现在对序列:[6, 1, 27, 2, 9, 3, 10, 5, 8]这9个数字排序.
首先需要中轴数(或者叫基准,就是一个名词),比如序列中的数字6.
那么需要做的是,把这个序列中比这个中轴数(数字6)小的放在中轴数左边,比中轴数大的放在中轴数右边.

> 1 5 2 3 **6** 9 10 27 8

类似这样.在最初,6在第0个位置,然后让6移动到中间的一个位置,并且这个位置的左边都比6小,右边都比6大.

如何做到?(这里顺便说一句,这个中轴数,如果是随机的从序列中选择,排序效率会更好)

我们设置两个数组:less和greater.然后遍历序列,如果比中轴小,就放在less中,比中轴大,放在greater中.
由于,less数组和greater数组中的数不一定是排好序的,所以递归的调用qsort函数.