# Do you want to be a Python expert ?

很多时候,有些人在介绍 `Python` 的时候会提到 `The Zen of Python` :

```shell
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

但是我不知道你需要多久才能做到 `The Zen of Python` 中说的.

`Python` 真的优雅吗, `Python` 真的简洁吗, 这是当然, 不然 `The Zen of Python` 怎么会添加到标准库中去.

不过在此之前,你需要更加的学习(毕竟不是一上来就什么都会的), 明白 Python 的风格, 或者说需要自己不断锻炼, 让自己写出来的 Python 代码更加的 *pythonic*.

在这里, 我不会讲述类似:

```python
a, b = b, a

l = [x * 2 for x in range(10)]
```

类似这种你本就应该在初学 `Python` 就应该熟练掌握的东西.

#### 我更想讲述的是:

- data model class (dunder methods, protocol).

- metaclass (Base/Derive class)

- Decorators

- Generators

- Context Managers

因为以上的一些feature确实可以让你的代码更加`pythonic`, 而且也是非常重要的.

-----------------------------------------------------------------------

## A problem

在很早很早之前,曾经看到一个群友问了一个问题:

有两个list, 比如: `one = [1, 2, 3], other = [2, 3, 4]`

他想要得到这样的结果,把这两个相加得到: [3, 5, 7], 也就是对应下标的元素相加.

我当时想都没想就回了一句: `return [one[i] + other[i] for i in range(len())]`

看上去不错,是吗?

当然不是. 如果这两个list不相等怎么办?

然后我又给了一个方案: `return list(map(lambda x, y: x + y, one, other))`

不过, 这样又不好了, 如果一个list长,一个list短,这个样子写,长的那个list多出来的数据就会被丢掉了.

所以我又思考了一下, 重新给出了最后结果: `return list(starmap(lambda x, y: x + y, zip_longest(one, ther, fillvalue=0)))`

*你能想到我所说的最后一种方案吗?*

-----------------------------------------------------------------------

## What is Python ?

Python 到底是一种什么样的语言, 说真的, 很难给 Python 下一个定义,因为它的范式实在太多:

- 面向对象

- 过程式

- 面向协议

- 原型

- 也支持函数式的feature

*Python is an interpreted, interactive, object-oriented programming language. (来自Python docs)*

如果你真正理解这些 feature 是什么, 那么非常显然的是, 来告诉我: why and when you use it. (毕竟我更倾向于实用, 我不是学院派)

-----------------------------------------------------------------------

当然,在最后的时候,我也会告诉一些学习途径, 比如看什么书可以最快的提高你的能力, 也比如你应该从哪些地方去获取你需要掌握的知识.
