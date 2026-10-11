---
title: 高频业务：一种IP网段判断重叠的算法（其三）
url: https://blog.nsfocus.net/%e9%ab%98%e9%a2%91%e4%b8%9a%e5%8a%a1%ef%bc%9a%e4%b8%80%e7%a7%8dip%e7%bd%91%e6%ae%b5%e5%88%a4%e6%96%ad%e9%87%8d%e5%8f%a0%e7%9a%84%e7%ae%97%e6%b3%95%ef%bc%88%e5%85%b6%e4%b8%89%ef%bc%89-2/
source: 绿盟科技技术博客
date: 2026-10-10
fetch_date: 2026-10-11T08:02:44.262300
---

# 高频业务：一种IP网段判断重叠的算法（其三）

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)
* [登录](https://blog.nsfocus.net/wp-login.php)

* [首页](https://blog.nsfocus.net)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)
* 高频业务：一种IP网段判断重叠的算法（其三）

# 高频业务：一种IP网段判断重叠的算法（其三）

[0](https://blog.nsfocus.net/%E9%AB%98%E9%A2%91%E4%B8%9A%E5%8A%A1%EF%BC%9A%E4%B8%80%E7%A7%8Dip%E7%BD%91%E6%AE%B5%E5%88%A4%E6%96%AD%E9%87%8D%E5%8F%A0%E7%9A%84%E7%AE%97%E6%B3%95%EF%BC%88%E5%85%B6%E4%B8%89%EF%BC%89-2/#comments)

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=40&d=identicon&r=g) [NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "written 2026-10-1014:28") 发布于 1 天前

![](https://blog.nsfocus.net/wp-content/uploads/2026/07/6.png)

阅读： 32

#### **1、引言**

在高频业务：一种IP网段判断重叠的算法（其二）中，我们完善了利用数轴进行IP重叠判断的算法。

本篇博客中，笔者讨论拓展该算法的应用面。

#### **2、应用面的拓展**

首先思考，进行IP重叠的判断，本质上是拿一个一串IP序列（即一连串数轴上的段或点），在一个数轴上进行“碰撞”的过程。如果碰撞成功，那么说明存在重叠。

那么碰撞除了带给我们“重叠”的信息，还有什么额外的信息呢，经过思考可以得知，当我们得出重叠的段时，可以获取到：

1. 重叠的IP所在的数轴区域
2. 重叠的IP究竟被什么IP所覆盖（碰撞）

看上去好像并没有什么用，但是当我们给每个IP加上一些维度标签时，事情就发生了变化。想象存在以下场景：

已知一些攻击事件的源IP段，分布在数轴上。需要判断另一批源IP是否命中了其中的攻击事件。

这看似于计算重叠无关，但本质上仍然是在计算重叠！因为我们已将IP抽象与数组之上，任何针对IP维度的属性标签的碰撞需求，本质上都是在计算重叠。

那我们的算法就可以应用到以下场景了：

1. 筛选存在与僵尸网络A的源IP相同的源IP
2. 筛选曾经出现在美国，且处于攻击组织B的常用肉鸡的源IP
3. ….

#### **3、数据结构的改造**

那么我们首先需要对数组进行改造，这里以ipv6为例，因为ipv4仍然是整数形成的数组，只是每个段增加了“属性”标签。

ipv6较为特殊，转化为整数时更大，要考虑溢出问题。它的长度达到128位。

使用

type u128 struct {

hi uint64

lo uint64

}

表示128位整数。其中hi表示高64位，lo表示低64位

这样可以：

1.避免使用 big.Int

2.避免动态内存分配

3.降低GC压力

4.提高比较速度

现在采用一种统一的方式，表达一个IP段。

通过一个三元组（start, end, length）表示一个ip段，length表示这个ip段是多长。

对于单IP，1.1.1.1，会转换为 start = end = 16843009，此时区间长度为1

start = 16843009

end = 16843009

length = 1

[16843009, 16843009]

对于IP段的情况，

1.1.1.0/24

得到

start = 16843008

end = 16843263

length = 256

那么以ipv6为例我们有以下表达：

![](https://blog.nsfocus.net/wp-content/uploads/2026/10/1-300x91.png)

至于属性，则是在字典里，可以任意进行定义。

#### **4、需要解决的问题**

但是当我们定义上后，新的问题出现了。

问题1：考虑以下情况：

![](https://blog.nsfocus.net/wp-content/uploads/2026/10/2-300x112.png)

显而易见，更小的段，行业应该继承大段（金融），再包括自身的小段（农业）。

问题2：在考虑一种更复杂的情况：

![](https://blog.nsfocus.net/wp-content/uploads/2026/10/3-300x122.png)

我们设计上显然要避免这种情况，否则就会出现多段交叉的情况。此时的属性继承既依赖前，又依赖后。无法进行高效的统计。

#### **5、方案设计**

因此我们有以下设计：

1. 所有的输入均为IP段，IP段在数学上映射到数轴之后，有一个非常神奇的性质，就是小段始终被大段包裹，并且小段和小段之间不会重叠。这解决了问题2
2. 我们通过扫描线算法，在建表时以O（N）的时间成本，读取<ip, 业务标签>建立数轴即可。

下面介绍扫描线算法：

笔者将该算法执行的过程，称之为维度聚合。在维度聚合过程中。线段上的所有单IP或IP段，他们的业务标签属性被逐步修正为正确值。

原始数据可能存在，同一个IP段，对应多条记录。

例如

1.1.1.0/24   [金融]

1.1.1.0/24   [信息技术]

需要聚合为

1.1.1.0/24   [金融, 信息技术]

采用如下结构

type triplet struct {

ip string

ci int16

val string

}

ip表示ip段，ci表示维度列编号，val表示维度值

例如(1.1.1.0/24, industry, 金融)

所有数据被展开为(ip, col, value)

例如

1.1.1.0/24   industry 金融

1.1.1.0/24   industry 信息技术

1.1.1.0/24   app     网银

使用sort.Slice(…)进行排序，排序后，相同IP，相同维度，相同值会连续排列。

随后通过线性扫描算法，完成去重，聚合。

下面详细介绍sweep line线性扫描的应用

该算法用来解决CIDR嵌套继承。

假设以下数据

1.0.0.0/8   云服务

1.1.0.0/16  金融

1.1.1.0/24  银行

这是一个典型的嵌套场景，1.1.1.0/24需要继承，云服务和金融。因为它的段更小。被大段所包括。

1.0.0.0/8

└── 1.1.0.0/16

└── 1.1.1.0/24

假设下列三条线

/8 : ───────────────────────────────

/16 : ───────────────

/24 : ─────

有一根扫描线，不断向右移动，当扫描线进入某个CIDR（线段），说明当前CIDR开始生效，当扫描线离开某个CIDR时，说明当前CIDR结束。

为了实现扫描，每个CIDR会被拆为两个事件，一个表示进入事件，一个表示离开事件。

例如1.1.0.0/16

对应[16842752, start], [16843007, end]

系统在扫描过程中，会维护一个active集合，他表示正在覆盖扫描位置的所有CIDR（因为CIDR会有嵌套，扫描线位于某一点时，可能属于多个CIDR段）

开始扫描时，系统会按照数轴从左到右扫描所有事件。例如

(10, START)

/8开始

(20, START)

/16开始

(30, START)

/24开始

(40, END)

/24结束

(50, END)

/16结束

(60, END)

/8结束

当扫描到start事件时，存在两种情况，一种是刚刚进入该扫描段，另一种是在进入它之前，已经进入过其他扫描段（但还没退出）。

第二种情况时，active集合不为空，此时系统立刻知道，该扫描段，被active集合中的扫描段所包含。

然后系统会把active的维度，复制到当前扫描的段内。完成维度聚合。

这里还有一个问题，如何保证父CIDR一定出现在active集合中？

答案是首先对事件进行特殊排序（pos, isEnd, length)

先按照位置从小到大扫描

同一位置，start优先于end

同一位置 同类型的事件，更大的CIDR优先处理

当扫描到end事件时，说明该CIDR不再覆盖后续区域，因此需要移除出active集合。

该方案的优势：

1.以O（N）的复杂度解决了地质正确性中讨论的问题

2.能够任意扩展业务维度标签，子段继承父段的操作几乎没有开销

3.速度非常快，即使在100万个/24段的情况下仍然能在60秒内完成整个扫描与结果输出。

通过这种方式，现在我们拓展了我们算法的应用面，让他能够被应用于业务维度的碰撞之中。笔者在下一篇博客中将介绍这种算法一种工程化实现。

最后修改日期: 2026-10-10

### 作者

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=96&d=identicon&r=g)

[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/)

## 最新发布

* [议程速递 | 绿盟科技集结群贤，邀您共赴驭智之约](https://blog.nsfocus.net/%E8%AE%AE%E7%A8%8B%E9%80%9F%E9%80%92-%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E9%9B%86%E7%BB%93%E7%BE%A4%E8%B4%A4%EF%BC%8C%E9%82%80%E6%82%A8%E5%85%B1%E8%B5%B4%E9%A9%AD%E6%99%BA%E4%B9%8B%E7%BA%A6/)
* [传统BOT防护不够用？意图分析才是未来](https://blog.nsfocus.net/%E4%BC%A0%E7%BB%9Fbot%E9%98%B2%E6%8A%A4%E4%B8%8D%E5%A4%9F%E7%94%A8%EF%BC%9F%E6%84%8F%E5%9B%BE%E5%88%86%E6%9E%90%E6%89%8D%E6%98%AF%E6%9C%AA%E6%9D%A5/)
* [高频业务：一种IP网段判断重叠的算法（其四）](https://blog.nsfocus.net/%E9%AB%98%E9%A2%91%E4%B8%9A%E5%8A%A1%EF%BC%9A%E4%B8%80%E7%A7%8Dip%E7%BD%91%E6%AE%B5%E5%88%A4%E6%96%AD%E9%87%8D%E5%8F%A0%E7%9A%84%E7%AE%97%E6%B3%95%EF%BC%88%E5%85%B6%E5%9B%9B%EF%BC%89-2/)
* [高频业务：一种IP网段判断重叠的算法（其二）](https://blog.nsfocus.net/%E9%AB%98%E9%A2%91%E4%B8%9A%E5%8A%A1%EF%BC%9A%E4%B8%80%E7%A7%8Dip%E7%BD%91%E6%AE%B5%E5%88%A4%E6%96%AD%E9%87%8D%E5%8F%A0%E7%9A%84%E7%AE%97%E6%B3%95%EF%BC%88%E5%85%B6%E4%BA%8C%EF%BC%89-2/)
* [高频业务：一种IP网段判断重叠的算法（其三）](https://blog.nsfocus.net/%E9%AB%98%E9%A2%91%E4%B8%9A%E5%8A%A1%EF%BC%9A%E4%B8%80%E7%A7%8Dip%E7%BD%91%E6%AE%B5%E5%88%A4%E6%96%AD%E9%87%8D%E5%8F%A0%E7%9A%84%E7%AE%97%E6%B3%95%EF%BC%88%E5%85%B6%E4%B8%89%EF%BC%89-2/)

## 文章导航

[上一篇文章 直播预告 | 数据悄悄流出，行为悄悄越界？企业里的智能体，该管起来了](https://blog.nsfocus.net/%E7%9B%B4%E6%92%AD%E9%A2%84%E5%91%8A-%E6%95%B0%E6%8D%AE%E6%82%84%E6%82%84%E6%B5%81%E5%87%BA%EF%BC%8C%E8%A1%8C%E4%B8%BA%E6%82%84%E6%82%84%E8%B6%8A%E7%95%8C%EF%BC%9F%E4%BC%81%E4%B8%9A%E9%87%8C/)

[下一篇文章 高频业务：一种IP网段判断重叠的算法（其二）](https://blog.nsfocus.net/%E9%AB%98%E9%A2%91%E4%B8%9A%E5%8A%A1%EF%BC%9A%E4%B8%80%E7%A7%8Dip%E7%BD%91%E6%AE%B5%E5%88%A4%E6%96%AD%E9%87%8D%E5%8F%A0%E7%9A%84%E7%AE%97%E6%B3%95%EF%BC%88%E5%85%B6%E4%BA%8C%EF%BC%89-2/)

著作权 © 2026 **[绿盟科技技术博客](https://blog.nsfocus.net/)**. 保留一切权利。 本站采用的布景主题为 [Mynote](https://terryl.in/).