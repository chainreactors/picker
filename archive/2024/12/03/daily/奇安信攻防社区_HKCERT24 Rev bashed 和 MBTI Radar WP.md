---
title: HKCERT24 Rev bashed 和 MBTI Radar WP
url: https://forum.butian.net/share/3916
source: 奇安信攻防社区
date: 2024-12-03
fetch_date: 2025-10-06T19:34:44.329850
---

# HKCERT24 Rev bashed 和 MBTI Radar WP

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### HKCERT24 Rev bashed 和 MBTI Radar WP

* [CTF](https://forum.butian.net/topic/52)

周末的时候，打了hkcert24的比赛，里面很多题目设置很有趣，这里挑选其中rev方向的的bashed和MBTI Radar 记录一下wp

这里记录一下周末做hkcert24中做了的两个比较有意思的rev
bashed
------
这个题目初见有点吓人，但是仔细做完以后，发现这个题目里面有很多有趣的bash特性，也有很多有趣的算法（？）
（由于平台限制，这边将emoji替换成了英文/截图）
### 题面基本介绍
题目只有一个文件，叫做`❤️.sh`，这个文件的内容如下
![3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f05541e30dfe28c3ead49455698eaa5b12957a7b.png)
\*初见难免会被满屏幕的emoji吓到\*
题目将我们调用脚本后的第一个参数作为flag，并且检查其是否为以下字符组成，并且长度为87
![4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-fcf73c11dbb29671f6dcd1b642ea05031c03e2c9.png)
之后，程序会使用特别多的emoji进行数据处理，并且在最终检查一个标志位，确认我们输入的flag是否满足要求
![5.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-769ee5387988f62377538fe22e77b67d7d0b58b7.png)
这个题目到处都是emoji，乍一看数据处理起来比较麻烦，但是实际上在pytho3的环境下，可以简单地使用`ord`进行unicode转换
在介绍题面之前，我们需要介绍一些bash特性，其中有一些特性可能只是影响读题，另一些可能会影响做题，所以这里就将这里涉及的特性都记录一下：
### bash 特性一：不严格的函数定义
这个bash使用了非常多的emoji做函数封装。但是同时，这些emoji又会作为参数传入
![6.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d46d495a75aa39de9630395af6990495d63db739.png)
这就是第一个bash既明显又迷惑的特性：bash中所有的数据默认都是字符，例如
```bash
#!/bin/bash
a1=a
echo $a1
```
这里其实会将a视为字符串。
同时，在bash中，一个符号可以同时为变量和函数，例如
```bash
my\_function() {
echo "This is a function."
}
my\_function='This is a string.'
my\_function # 这将输出 "This is a function."
echo $my\_function # 这将输出 "This is a string."
```
当变量同时为函数和变量的时候，函数会优先表达。
而一旦函数写在了参数的位置，例如
```bash
echo my\_function
```
那么此时便会\*\*让函数强制作为字符串翻译\*\*。
在知道这个特性之后，这类函数我们便可理解它的含义
![7.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e23c782f1886dc4662fbd4a5de056867dc2c147b.png)
上述函数的含义，即为\*\*将传入的参数按照特定的顺序打乱\*\*。例如上述的衣服函数，最终的效果是以这样的方式调用柠檬
![8.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f730bf7dc1fdecef5936184e8f07e77df6c23004.png)
### bash特性二：动态更新与执行顺序
关键函数 柠檬 中存在非常重要的逻辑:
![9.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c2032c5ed346041d3f4e596d5704544604285252.png)
其中黑脸表示将参数翻译成整数，而黄脸则会将参数翻译成十六进制表示。所以
![10.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-1dff52327105a29ff7e3be5d9e7b1dc8cea150ec.png)
这一段代码用python翻译一下，可以得到这样的含义
![11.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-69ff3a1ca402eca902e1ef3815136eeeae94910c.png)
然后程序将这段代码计算sha1，并且取出其`sha1\_result[1]`作为比较，确认是否为目标
![12.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-0efa21ce6223de7b76e6bb7ea7b9ba66921c8eb6.png)
之后，程序会尝试从目标url中下载脚本，并且\*\*更新当前脚本为下载内容\*\*
```php
wget https://c22-bashed.hkcert24.pwnable.hk/$4.sh -O $(basename $0) >/dev/null 2>&1;
```
然而实际上，bash每次运行的时候，都是将数据一次性全部读入内存中然后解析，那为什么`wget`会让脚本重新加载呢？实际上，如果这里的指令替换成`cp`，使用另一个脚本覆盖当前脚本，抑或是使用vim编辑器直接修改脚本，或者使用`cat`读取脚本内容后重定向，\*\*均不可触发脚本重加载\*\*。
经过测试发现，`wget`在加上`-O`参数的时候，会使用下列函数打开文件：
```php
openat(AT\_FDCWD, "origin.sh", O\_WRONLY|O\_CREAT|O\_TRUNC, 0666) = 3
write(3, "##!/bin/bash\n\nf1() {\n echo \"f1\""..., 190) = 190
```
这里的`O\_TRUNC`表示\*\*当即将当前文件内容清除，同时读入新数据\*\*。而实际上，`cp`之类的指令并没有直接的修改文件内容，而重定向本身会使得文件内容被清除后再进行数据写入，所以可以猜测，bash\*\*如果发现脚本内容被修改，会在执行的子进程结束后，重新加载一次脚本\*\*。在知道这个特性下，如果将`wget`替换成`curl`，则也能实现类似效果。
那么在利用这个特性的前提下，我们就能做出一些有意思的行为，假如我们的代码如下
```bash
#!/bin/bash
f1() {
echo "f1"
wget http://localhost:8080/new.sh -O $(basename $0)
}
f2() {
echo "f2"
}
f3() {
echo "f3"
}
f1
f2
f3
```
此时打印的数据如下
```php
f1
f2
f3
```
然而，如果我们添加一个转义符:
```bash
f1 \
f2
f3
```
那么此时其实脚本就变成了
```php
f1 f2
f3
```
此时根据特性一，此时的\*\*f2本质上是作为字符串参数，而非函数\*\*。那么此时的输出就变成了
```php
f1
f3
```
那么，接下来假设一开始的脚本逻辑为
```bash
执行-> f1 \
f2
f3
```
当我们正在执行f1的，利用`wget`动态修改代码，使其变成
```bash
执行-> f1
f2
f3
```
此时接下来要执行的逻辑就出现了歧义。对于上述代码，我们有以下两种理解
- （1）因为发生了修改，`\\`消失，此时pc从行号1前进到行号2，于是此时执行f2，并且之后会执行f3
```bash
f1
执行-> f2
f3
```
- （2）原先因为`\\`的存在，pc默认下一个执行的行号为3，于是此时执行f3，跳过f2
```bash
f1
f2
执行-> f3
```
在实测中，我们发现（2）才是实际情况。也就是说，\*\*bash会以行号为执行的下标（PC），其会根据`\\`符号选定下一个执行的行号逻辑\*\*。
在这个基础上，还有一种特殊情况。假设代码如下:
```php
-> 执行 f1 \
f2
f3
f4
```
执行f1的时候，动态的修改代码为
```php
-> 执行 f1 \
f2 \
f3 \
f4
```
此时又会执行什么呢？根据上述分析，我们有三种猜想：
- （1）因为发生了修改，f1、f2、f3均添加`\\`，所以这三行会被当成一行，接下来我们会运行f4
```bash
f1 \
f2 \
f3 \
-> 执行 f4
```
- （2）原先因为`\\`的存在，pc默认下一个执行的行号为3，于是此时执行f3，同时原先没有在f3后有`\\`，所以也执行f4
```bash
f1 \
f2 \
-> 执行 f3 \
f4
```
- （3）原先因为`\\`的存在，pc默认下一个执行的行号为3，于是此时执行f3，跳过f4
```bash
f1 \
f2 \
-> 执行 f3 \
-> 跳过 f4
```
经测试后发现，正确答案是（3）。因为当wget执行以后，【内存的数据已经被替换成了新下载的文件】，此时要以替换后的新文件规则重新考虑换行。
那么，我们就能在特性二下得出一个结论：
> 在动态修改的环境下，下一个PC的地址与行末是否有\\存在密切关联，其会找到下一个执行前，下一个行末不为\\的地址作为下一个PC的位置
### bash特性三：整数溢出
bash最后的判断逻辑为
![5.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-3e858a290718d71bc386437875560973c450f1e3.png)
然而我们回顾这个`$GALF`的变化，只有这里:
![13.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a04898c7fb0d48d2362b24a5a6afdbeec7a77d57.png)
不断相乘的数值真的会导致让其值为0吗？答案是可以的。
bash的整数使用的是64bit，所以其实当数据超过64bit的时候，就会发生溢出。例如
```bash
#!/bin/bash
# 0x7fffffffffffffff
a1=9223372036854775807
a1=$((a1\*2))
# -2 0xfffffffffffffffe
echo $a1
a1=$((a1\*4))
# -8 0xfffffffffffffff8
echo $a1
```
可以看到，随着溢出的发生，\*\*位于低位的bit从1变成了0\*\*，如果乘的越多，这个0就会变得越多。实际上，\*\*只要乘法的两侧有一个是偶数，那么结果必然是呈现左移\*\*，所以`GALF`会在乘法计算的过程中，逐渐逼近0（向着高位）
### 读题：确认考点
分析完上述特性之后，我们可以总结一下这个题目的逻辑
（0）题目中总共出现了87中emoji，算上最初的爱心，总计88个
（1）题面为256行的emoji
![6.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2d357cc7472b052a28fccb9316ead15471371da0.png)
为了方便描述，上述每一行的`emoji`命名为`emoji\_line`，并且将整个256行的emoji叫做`emoji\_table`
（2）每一个`emoji\_line[0]`都定义了一个函数
![14.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7e50fe1687da9295eac80b1a8e9873696ce01dd2.png)
总共也有87个。这里我们将这种映射关系成为`emoji\_mapping`。也就是`emoji\_line[0]`本质上是将`emoji\_line[1:8]`打乱后，作为参数传入柠檬函数
（3）根据柠檬中的代码
![15.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c9040d593f66328aac827031ca5b396ff9434d4e.png)
可知，此时会用`emoji\_line[4]`和`emoji\_line[5]`作为传入。大胆猜测，所以此时肯定有其他87个叫做`{emoji}.sh`的文件。实际上写一个爬虫后，发现确有这样的结论。
（4）由（3）可以知道，总共由88个叫做`{emoji.sh}`的文件，如下
![16.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-3c876bb000a02cd5a0086513805aece6b50818ea.png)
每一个`{emoji.sh}`都很类似，唯一的区别在于\*\*emoji\\_table存在差异\*\*，例如另一个文件中的`emoji\_table`就如下
![17.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8205d1015816fba85d3b7295961b3e289dc0dcff.png)
这里的区别就在于某些行最后的`\\`的位置会变化，然后根据我们前文提到的\*\*特性二\*\*，这里会导致\*\*bash对下一个要运行的行数发生变化\*\*。例如我们执行
![18.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e18078c297da685665269bb5d0370d201324b96d.png)
此时实际上会被bash理解为
![19.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-890d46c624ff7320261c51b23930468c19d49295.png)
那么下一次我们执行的行其实为
![20.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-dbc5ccfe3eaf766eea832aac17bc995a4607eca9.png)
如果用idx描述执行行号，则会在\*\*执行完idx=0之后，转而执行idx=2\*\*。
（5）同样根据柠檬的代码，我们会知道`GALF`的变化与`emoji\_line[6]`和`emoji\_line[7]`相关，并且最终会检测`GALF`值是否为0（根据\*\*特性三\*\*，不断相乘最终会导致其溢出为0）。
于是总结上述题面，我们能够发现这道逆向题的题面本质上为一道类似算法的题目：
- 现在存在88份`emoji\_table`，每一张地图都有256行`emoji\_line`
- 当我们进行访问的时候，`emoji\_line[0]`会将`emoji\_line[1:8]`重排序
- `emoji\_line[1]`和`emoji\_line[2]`会从目标flag中取出对应的字符，计算其hash，并且与`emoji\_line[3]`比较
- 当上述条件相等，则`GALF\*=emoji\_line[6]`，并且前往`emoji\_line[4]`对应的地图
- 当上述条件不相等，则`GALF\*=emoji\_line[7]`，并且前往`emoji\_line[5]`对应的地图
- 程序执行的时候，有一个下标`idx`用于描述行号。每执行一行`emoji\_line`，则idx+=1。如果`emoji\_line`结尾有`\\`，则当前idx会多自增一行。如果下一行末尾也为`\\`，则一直自增，直到最后行末不为`\\`或者到尽头
- ...