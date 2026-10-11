---
title: 高频业务：一种IP网段判断重叠的算法（其二）
url: https://blog.nsfocus.net/%e9%ab%98%e9%a2%91%e4%b8%9a%e5%8a%a1%ef%bc%9a%e4%b8%80%e7%a7%8dip%e7%bd%91%e6%ae%b5%e5%88%a4%e6%96%ad%e9%87%8d%e5%8f%a0%e7%9a%84%e7%ae%97%e6%b3%95%ef%bc%88%e5%85%b6%e4%ba%8c%ef%bc%89-2/
source: 绿盟科技技术博客
date: 2026-10-10
fetch_date: 2026-10-11T08:02:42.818147
---

# 高频业务：一种IP网段判断重叠的算法（其二）

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
* 高频业务：一种IP网段判断重叠的算法（其二）

# 高频业务：一种IP网段判断重叠的算法（其二）

[0](https://blog.nsfocus.net/%E9%AB%98%E9%A2%91%E4%B8%9A%E5%8A%A1%EF%BC%9A%E4%B8%80%E7%A7%8Dip%E7%BD%91%E6%AE%B5%E5%88%A4%E6%96%AD%E9%87%8D%E5%8F%A0%E7%9A%84%E7%AE%97%E6%B3%95%EF%BC%88%E5%85%B6%E4%BA%8C%EF%BC%89-2/#comments)

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=40&d=identicon&r=g) [NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "written 2026-10-1014:30") 发布于 1 天前

![](https://blog.nsfocus.net/wp-content/uploads/2026/06/封面-1.jpg)

阅读： 42

#### **1、引言**

在<https://blog.nsfocus.net/ip-cal/> 这篇博客中，笔者讲述了一种通过将IP映射到数轴上，进而判断其是否重叠的算法。

我们首先回顾一下上一篇的内容。

![](https://blog.nsfocus.net/wp-content/uploads/2026/10/11-300x190.png)

![](https://blog.nsfocus.net/wp-content/uploads/2026/10/22-300x78.png)

本文是这篇文章延续，该博客完整的讨论从一个算法落地为工程化的实现步骤。这是第二篇内容。对算法的实现进行扩展。

#### **2、特殊情况的讨论**

在第一篇博客中。我们考虑了将IP range解析为int，但有两例特殊情况我们没有讨论过。

第一类特殊情况是ipv6，众所周知，ipv6转化成数字后非常大。与ipv4位数不是一个量级。

举例来说:

“`

# Python 中 IPv6 转成的大整数

ipv6\_int = 2\*\*128 – 1

# 最大 IPv6 地址

# 浮点运算导致精度丢失

result = ipv6\_int + 0.1print(result)

# 输出类似 3.402823669209385e+38，已不是精确整数

“`

因此我们可以考虑将算法并行化，设计两个数轴，分别存放ipv4，ipv6。用分治的思想，同时处理它们。算法伪代码如下：

“`

def build\_ip\_axis(iparr):

check\_conflict(iparr)

def check\_conflict\_both(iparr):

“””    分治处理 IPv4 和 IPv6 的冲突检测    “””

ipv4\_ranges = []

ipv6\_ranges = []

for ip in iparr:

if is\_ipaddr\_v6(ip):

ipv6\_ranges.append(ip)

else:

ipv4\_ranges.append(ip)    # 分别检测，互不干扰

ok\_v4, err\_v4 = check\_conflict(ipv4\_ranges)

ok\_v6, err\_v6 = check\_conflict(ipv6\_ranges)

return ok\_v4 and ok\_v6, err\_v4 + err\_v6

“`

第二类特殊情况，是浮点运算。在计算机中，浮点运算是误差的。在第一篇博客中。我们有源代码如下

“`

if start == end:

start -= 0.1

end += 0.1

“`

我们这段代码的目的是让start/end相同的点展开一个极其“微弱”的距离（0.2），作为一个段参与整个运算。在ipv4下自然没问题。但是在ipv6下，由于计算机的浮点运算误差，它隐藏了一个偶发的问题：（补全此处）

因此我们需要修改代码，将数轴扩大，最小单位变为1，而不是0.1，以下为原始代码

“`

def check\_conflict5(inets, src\_inets=None, error\_all=False):

“””

edit by pantianyou@intra.nsfocus.com

所有ip范围映射到数轴，遍历一遍求和，无重叠的情况下数轴形如1,-1,1,-1,1,-1…，其他情况则说明有重叠

inets: 可能存在重叠iprange的iprange数组

src\_inets: 原始的ipranges数组，当需要判断重叠的ipranges是否存在于某个集合中，可以把该集合传入src\_inets

error\_all: 是否发现所有重叠错误，为False则发现一处就会返回False

return: True无重叠, False有重叠

error\_list为发生重叠冲突的ip范围集合

对于Ipv6来说，

Ipv6会被转化为大整数，在此大整数上做加减浮点数时会返回科学计数法的值，无法算出精确数字。

此时会影响效果。

因此采用变换坐标的形式，进行等比例缩放。

原IP段假设1~10，则有10个IP，每个数代表一个IP，

假设两个数代表一个IP，则1~20，共有10个IP。

放大比例尺。放大两倍（避免溢出）

“””

error\_list = list()

if inets is None or len(inets) == 0:

return True, []

int\_ranges = {}

ip\_finds = {}

for ip in inets:

start, end = split\_ipsegment\_int(ip)

is\_v6 = is\_ipaddr\_v6(ip)

if is\_v6:

start \*= 2

end \*= 2

if start == end:

# 说明是单个ip

if is\_v6:

start -= 1

end += 1

else:

start -= 0.1

end += 0.1

if start not in int\_ranges.keys():

int\_ranges[start] = 0

ip\_finds[start] = []

if end not in int\_ranges.keys():

int\_ranges[end] = 0

ip\_finds[end] = []

int\_ranges[start] += 1

int\_ranges[end] -= 1

ip\_finds[start].append(ip)

ip\_finds[end].append(ip)

temp\_sum = 0

\_sorted = sorted(int\_ranges)

for index in range(0, len(\_sorted)):

k = \_sorted[index]

v = int\_ranges[k]

temp\_sum += v

if (v > 1 or v < -1) or (v == 1 and temp\_sum > 1) or (v == -1 and temp\_sum != 0):

# 1. 重叠的开始/结束

# 2. 是一个开始点，但是之前也有开始点

# 3. 是一个结束点，但经历结束点后和并没有变为0

error\_list.extend(ip\_finds[k])

if index – 1 >= 0:

# 把之前出问题的点也加上

# error\_list.extend(ip\_finds[\_sorted[index – 1]])

pass

if not error\_all:

break

error\_list = set(error\_list)

if src\_inets is not None and len(src\_inets) > 0:

if not isinstance(src\_inets, set):

if isinstance(src\_inets, list):

src\_inets = set(src\_inets)

error\_list = error\_list.intersection(src\_inets)

else:

error\_list = error\_list.intersection(src\_inets)

error\_list = list(error\_list)

if len(error\_list) != 0:

return False, error\_list

return True, error\_list

“`

通过以上的修改，我们修复了两个问题：

1. ipv4/v6在同一数轴上遍历的问题
2. ipv6的精度丢失问题。

下一篇博客将讨论利用扫描线算法进一步拓展数轴的在ip属性搜索的方案。

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

[上一篇文章 高频业务：一种IP网段判断重叠的算法（其三）](https://blog.nsfocus.net/%E9%AB%98%E9%A2%91%E4%B8%9A%E5%8A%A1%EF%BC%9A%E4%B8%80%E7%A7%8Dip%E7%BD%91%E6%AE%B5%E5%88%A4%E6%96%AD%E9%87%8D%E5%8F%A0%E7%9A%84%E7%AE%97%E6%B3%95%EF%BC%88%E5%85%B6%E4%B8%89%EF%BC%89-2/)

[下一篇文章 高频业务：一种IP网段判断重叠的算法（其四）](https://blog.nsfocus.net/%E9%AB%98%E9%A2%91%E4%B8%9A%E5%8A%A1%EF%BC%9A%E4%B8%80%E7%A7%8Dip%E7%BD%91%E6%AE%B5%E5%88%A4%E6%96%AD%E9%87%8D%E5%8F%A0%E7%9A%84%E7%AE%97%E6%B3%95%EF%BC%88%E5%85%B6%E5%9B%9B%EF%BC%89-2/)

著作权 © 2026 **[绿盟科技技术博客](https://blog.nsfocus.net/)**. 保留一切权利。 本站采用的布景主题为 [Mynote](https://terryl.in/).