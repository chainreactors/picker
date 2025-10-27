---
title: 2022 47 Open source weekly report
url: https://cloudsjhan.github.io/2022/11/13/2022-47-Open-source-weekly-report/
source: cloud world
date: 2022-11-14
fetch_date: 2025-10-03T22:40:33.677449
---

# 2022 47 Open source weekly report

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 2022 47 Open source weekly report

posted

2022-11-13

|

in

[weekly-report](/categories/weekly-report/)

|

visitors:

|

|

wordcount:

561
|

min2read ≈

2

2022 NO.47 周报

![](https://)

自从 [databend-go](https://cloudsjhan.github.io/2022/10/21/2022-43-Open-source-weekly-report/#more) release 后，最近大部分时间都在与 Python 搏斗😂，太长时间没有正儿八经写 Python 了真是磨合了好几天才找到点感觉。
用了差不多两周，databend 的 Python Deiver [databend-py](https://github.com/databendcloud/databend-py) 以及支持 `SQLAlchemy` 语法的 [databend-sqlalchemy](https://github.com/databendcloud/databend-sqlalchemy) 已经基本可用。不得不说 Python 在数据的生态里还是王者，前几天有用户在使用 go driver 的时候遇到了一个 data type parser 的[问题](https://github.com/databendcloud/databend-go/issues/10)，之前在实现过程中就遇到过类似的类型问题，这种问题在强类型语言里简直就是灾难，但是对于 Python 来说就不存在。所以最后用户还是用了 Python 的 driver 解决了问题，看来后面要认真打磨 databend-py 了。

在使用方面也是 python 占优，pip install 然后 import 直接就是手到擒来：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` pip install databend-py ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` from databend_py import Client client = Client(     host='hostName',     database="default",     user="user",     password="pass") print(client.execute("SELECT 1")) ``` |

不过 `databend-py` 仅是提供了 python 连接到 databend cloud 的桥梁，并不能像使用 ORM 工具一样使用 `cursor.next`、`fetchall` 等方法。在准备实现 [dbt](https://docs.getdbt.com/docs/introduction) adapter 的时候发现需要依赖上面提到的 ORM 的方法，在 Python 生态里 SQLAlchemy 是 Python 中最有名的 ORM 工具，所以就有了 `databend-sqlalchemy` 这个项目。由于时间紧迫，先实现了对接 dbt 必须要用到的 `cursor, description, next, fetch` 方法，在 `databend-py` 的铺垫下，实现起来确实方便很多。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` cursor = connector.connect('http://root:@localhost:8081').cursor()     cursor.execute('select 1')     # print(cursor.fetchone())     print(cursor.fetchall())     print(cursor.description) ``` |

几个字总结一下近期的状态就是：`与 Python 搏斗`，当然接下来可以预见的依然会跟 python 搏斗一段日子，因为最近要搞的 dbt adapter 是一个全新的, 陌生领域，完全就是一头雾水，所以接下来可能会先写几篇关于 dbt 的学习文章吧。

再就是最近开的 repo 有点多，加上实现的时间比较紧，感觉有些疲于应对，很多实现只能草草了事，估计 bug 会比较多，所以后面应该会多抽出一些个人的时间来完善这些项目。

---

-------------The End-------------

Title:[2022 47 Open source weekly report](/2022/11/13/2022-47-Open-source-weekly-report/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2022年11月13日 - 11:11

Last Update:2022年11月13日 - 22:11

Original Link:[https://cloudsjhan.github.io/2022/11/13/2022-47-Open-source-weekly-report/](/2022/11/13/2022-47-Open-source-weekly-report/ "2022 47 Open source weekly report")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

微信支付

![cloud sjhan 支付宝](/images/alipay.jpg)

支付宝

[weekly-report](/tags/weekly-report/)

(>给这篇博客打个分吧<)

[2022 43 Open source weekly report](/2022/10/21/2022-43-Open-source-weekly-report/ "2022 43 Open source weekly report")

[2022 51 Open source weekly report](/2022/12/17/2022-51-Open-source-weekly-report/ "2022 51 Open source weekly report")

![cloud sjhan](/images/avatar.png)

cloud sjhan

[166
日志](/archives/)

[40
分类](/categories/index.html)

[73
标签](/tags/index.html)

[RSS](/atom.xml)

[GitHub](https://github.com/hantmac "GitHub")

E-Mail

Links

* [CSDN](https://blog.csdn.net/u012421976 "CSDN")
* [w3school](http://www.w3school.com.cn/ "w3school")
* [快搜](http://search.chongbuluo.com/ "快搜")

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;