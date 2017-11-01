<small>connectMySQL.py</small>
```python
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='hello')

cur = conn.cursor()

try:
    cur.execute('SELECT * FROM test.users')
    print(cur.fetchall())
finally:
    cur.close()
    conn.close()
```

需要的东西有：

> MySQL数据库, 和Python第三方库： pymysql

Pycharm集成了一些数据库的链接GUI：

![connect mysql](http://img.vim-cn.com/76/18da9cbe63f5da40baae4434b43a416cea575a.png)

![create database and table](http://img.vim-cn.com/49/fe26357d6a798d3f79cc9cc60e16ea47537674.png)


```mysql
CREATE DATABASE test;

CREATE TABLE test.users (
  id       INT(11) PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
  username VARCHAR(64) UNIQUE  NOT NULL,
  password VARCHAR(64)         NOT NULL
);
```

执行这些SQL语句来创建数据库和表。简单点这个表的名字叫users,
里面就三个字段:id, username, password.

可以看到右侧是有我们的表的信息的:
![](http://img.vim-cn.com/c5/f85054abe0b9800b3fb834cc6b76bb747892b4.png)

先在数据库里面插入两条语句:
```mysql
INSERT INTO test.users (username, password) VALUE ('hello', 'world');
INSERT INTO test.users (username, password) VALUE ('foo', 'bar');

SELECT *
FROM test.users;
```
![](http://img.vim-cn.com/26/1dc06e7b1e23076563eab6b8b6b4d6a74c0654.png)


## 说明一下Python链接数据库

这段程序有两个对象:连接对象(conn)和光标对象(cur).

连接/光标模式是数据库编程中常用的模式.
一个光标跟踪一种状态信息,比如跟踪数据库的使用状态。通过调用光标函数,比如cur.fetchall(),可以获取查询结果.

用完光标和连接之后,千万记得把它们关闭.如果不关闭就会导致**连接泄漏**,造成一种未关闭连接现象,即连接已经不再使用,但是数据库却不能关闭,因为数据库不能确定你还要不要继续使用它,这种现象会一直耗费数据库的资源,所以用完数据库之后一定要关闭链接.

![](http://img.vim-cn.com/67/17a3974a4314d5c2f83110db563448e2b493fc.png)
通过pycharm的自通补全可以看到,有三个类似的获取查询方法.
通过这三个方法我简单说明光标的一个作用.
```python
    def fetchone(self):
        """Fetch the next row"""
```
这是fetchone方法的源码中的代码.
数据库中的表，不就像一个excel表格那样子,光标就好像是一个箭头,最开始的时候指在表格的第一行.
fetchone(拿来一个数据),当执行这个方法之后,我们会获取数据库表中的一行结果(也就是第一行结果),这个时候,光标向下走一格,指在第二行那里,然后再执行fetchone,就会获得第二行的结果.
```python
    def fetchmany(self, size=None):
        """Fetch several rows"""
```
fetchmany(),它有一个参数,size,你可以通过指定size的大小,开获取size行的数据.当然获取的数据是从光标的位置开始的.
```python
    def fetchall(self):
        """Fetch all the rows"""
```
fetchall(),这个方法是获得所有的数据,虽然是获得所有的数据,那也是从光标的那个位置开始,到最后的.
```python
cur.fetchon()
print(cur.fetchall())
```
比如执行这两行代码,你会发现,第一行的数据没有打印出来,因为cur.fetchon()让光标向下走了一格.

> 如果有人较真的话,看到注释的内容"""Fetch the next row"""，就要跟我说是返回的光标下一行的数据的话，其实主要是你能理解就好.

数据库常用的无非就是增删改查了,只需要一条语句就足够了,
cur.execute(sql),把那个你要做的sql语言放进去,然后就会执行了.就这么简单.


最后说一下,我那个代码中
```python
cur.execute('SELECT * FROM test.users')
```
我的表的名字是全的,就是说test(数据库名).users(表名),如果你不习惯的话.
```python
    cur.execute('USE test')
    cur.execute('SELECT * FROM users')
```
换成这个样子就好了.