---
title: SQL注入实战——HTTP Header注入，新的注入思路
url: https://mp.weixin.qq.com/s/IVLi0Ze1f9ilw4XlgkR_qw
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:36:26.835822
---

# SQL注入实战——HTTP Header注入，新的注入思路

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VFf46TKXLVGVqYdzL2x8ydcsCUj1oeG2sFehJUweVicsoLwt7zbtEdIzcJCBRrz6SY82farDwAPafoSOllc3EUg/0?wx_fmt=jpeg)

# SQL注入实战——HTTP Header注入，新的注入思路

原创

武文学网安

武文学网安

![]()

在小说阅读器中沉浸阅读

大家好，我是武文。

今天继续挑战学习sqli-labs。当遇到 **第 18 关** 时，会发现一个明显的变化：前面那些屡试不爽的方法，突然全部失效了。不管是：

* 在 `username` 输入框里加单引号、双引号
* 在 `password` 中构造 `or 1=1`
* 甚至抓包后修改 POST 参数

**页面都没有任何异常回显，也没有登录状态变化。**

我在这里尝试了大约半小时，始终无法判断：

* 闭合方式是什么？
* 是否存在注入点？
* 是显错、盲注，还是根本没有漏洞？

我的内心是这样的—>![崩溃表情包纯文字- 抖音](https://mmbiz.qpic.cn/mmbiz_jpg/VFf46TKXLVGVqYdzL2x8ydcsCUj1oeG2C8rKDLIszIzmWUfya4ZJ4pnO8L2DmgHVoqCYu9WGXmibOiaKyibDEdx2g/640?wx_fmt=other&from=appmsg)

看来老办法行不通，这一关并非之前的“参数注入”，是时候去学习新的注入思路了。

## 一、为什么第 18 关“参数注入”全部失效？

在前 1～16 关中，我们做的事情本质上是：控制 SQL 语句中的用户输入参数。比如：

```
SELECT * FROM users WHERE username='输入值' AND password='输入值';
```

所以我们能通过：闭合引号、构造逻辑条件、UNION / 报错 / 盲注等方法来影响 SQL 的执行结果。

### 但第 18 关不一样，第 18 关的核心特点是：用户名和密码参数是“安全的”，但程序额外记录了访问信息，如图所示为正确输入账户密码dumb,dumb。

![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVGVqYdzL2x8ydcsCUj1oeG242IMtZicDu7iadQICpZPgvsf4S9mGUHCZxvQAJym8u8QCa6zmytwMOHQ/640?wx_fmt=png&from=appmsg)

### 这里注意，与前面关卡不同，这里记录了：Your IP ADDRESS is: 172.17.0.1 Your User Agent is: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36

这里记录了 User-Agent。这些信息并不是我们在表单中填写的，而是来自 **HTTP 请求头（Header），而这些Header，同样是用户可控的**。

二、理论篇：什么是 HTTP Header 注入？

### 2.1 HTTP Header 是什么？

当我们访问一个网站时，浏览器发送的不只是 URL 和参数，还包括一堆“附加信息”，例如：

Content-Type ：Content-Type 参数用于指明请求或响应的内容类型。

Accept  ：Accept 参数用来告诉服务器客户端能接受的数据格式。

User-Agent  ：User-Agent 参数用于标识发起请求的客户端类型，如浏览器或应用程序。这有助于服务器了解请求的来源，并根据不同的客户端做出相应的处理。

Cookie ：Cookie 参数用于在请求中传递客户端的 Cookie 信息，通常用于保持会话状态或保存用户设置。

这些信息通常被用来：记录访问日志，统计来源，分析用户行为，安全审计。

### 2.2 问题出在哪？

**很多开发会把 Header 信息直接写入数据库**，例如：

```
INSERT INTO logs (username, ip, useragent)VALUES ('admin', '127.0.0.1', 'User-Agent内容');
```

如果开发 **没有对 Header 做过滤**，而我们又能控制它——
那么：SQL 注入点，就从“参数”转移到了“请求头”。

这就是 **HTTP Header 注入**。

三、实操篇：sqli-labs 第 18 关注入思路

前面已经试过在页面上什么都测不出来，现在我们通过Burp Suite抓包在header上进行注入尝试。

3.1 Burp Suite抓包

1.浏览器代理设置，打开Burp Suite

2.开启Proxy->Intercept ON

3.随便输入登录名和密码点击登录

4.在Burp中拦截请求

5.选择对应链接发送到Repeater中

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVGVqYdzL2x8ydcsCUj1oeG2O8ETIOd1p6uNcZSafcGHduvBjWkoEvTiaRRXSr5tiaDqX6Tx6N0Vq7Pg/640?wx_fmt=gif&from=appmsg)

我们可以看到这样的请求格式：

![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVGVqYdzL2x8ydcsCUj1oeG282nRwn9LraLWbdY2DicAia1bPjmia2JsBNk1piaUfUHzfWEgv2iaQKK0EVA/640?wx_fmt=png&from=appmsg)

3.2 手动验证Header是否存在注入

在Burp中，直接修改User-Agent:

```
User-Agent: '
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVGVqYdzL2x8ydcsCUj1oeG2vO6ZkibM2kunpIuicIcs7ichicQmnWbJ7SQT00dVXWAw7or8Z6tLoDx66A/640?wx_fmt=gif&from=appmsg)

可以看到，结果有语法错误

![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVGVqYdzL2x8ydcsCUj1oeG2dwCXdJAbEeHH1YaGFpWMUGyoFOnzZQ8CEDV2Ziag6uqfib1X5ticglczQ/640?wx_fmt=png&from=appmsg)

这时可以基本确认User-Agent被拼接进了SQL语句。

可以确认存在注入。

3.3 分析注入方式

接着尝试：

```
User-Agent:' and 1=1 #User-Agent:' and 1=2 #
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVGVqYdzL2x8ydcsCUj1oeG2Ou2XkUPhD3axq5S8sHeRbg98puIXgkaLOcmtggzuJ4bel42zb51pCQ/640?wx_fmt=gif&from=appmsg)

这里发现依然是产生语法错误。这里是一个让很多人都会懵逼的地方，因为哪怕报错知道了这里应该是单引号+括号的闭合方式，去尝试的时候依然有问题。

```
User-Agent:') and 1=1 #User-Agent:') and 1=2 #
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVGVqYdzL2x8ydcsCUj1oeG2XnbBFhGTMIBXJtySBtzoWKUSazcRsKYftIrLW8fUKStibLK3yUt9XdA/640?wx_fmt=gif&from=appmsg)

核心原因：我们在 INSERT 语句里，`#` 不好使。

我们现在的注入场景是：

```
INSERT INTO ... VALUES(...)
```

而不是

```
SELECT * FROM USERS WHERE ...
```

### INSERT 语句里发生了什么？

当前的 SQL 逻辑大致是：

```
INSERT INTO logs (ip, useragent, username)VALUES ('172.17.0.1', 'PAYLOAD', 'admin');
```

而当使用User-Agent:') and 1=2#时报错，You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'and 1=2 #', '172.17.0.1', 'admin')' at line 1

当我们注入后，SQL实际就变成了：

```
INSERT INTO uagents (uagent, ip_address, username)VALUES (') and 1=2 #', '172.17.0.1', 'admin');
```

这就是在VALUES里写WHERE条件语法。`and 1=2` 在 INSERT VALUES 中是非法的，AND 只能用于：WHERE、HAVING、ON，而不能用在VALUES。而且 `#` 注释掉的是“字符串外的内容”，不是 SQL 结构，现在的#是写在字符串里，就没被当成注释符，只是一个普通字符，MySQL不会当成注释，后面的', '172.17.0.1', 'admin') 仍然解析。所以这里不能用and 1=2来判断真假。

正确思路：

能不能在VALUES的一个字段里构造一个会报错，并把数据拼进错误信息的表达式？

所以，我们要写的就是：

```
VALUES ('【一个会报错的表达式】', 'ip', 'user')
```

而不是：

```
VALUES ('') and 1=2 #', ...
```

所以现在我们构造INSERT场景下的payload：

```
User-Agent:' and updatexml(1,concat(0x7e,database(),0x7e),1) and '
```

为什么两边都要单引号？因为我必须要闭合当前的字符串，再补回一个字符串让当前的VLAUES语法完整

这里的SQL语句就相当于

```
INSERT INTO uagents (uagent, ip_address, username)VALUES ('' and  updatexml(1,concat(0x7e,database(),0x7e),1) and '', '172.17.0.1', 'admin');
```

下面进行实验：

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVGVqYdzL2x8ydcsCUj1oeG2oWyXuEBVDx9LLRdUGrRRU8BXicg9GYwLURAQLlQm1j29wNkwgzGDrGA/640?wx_fmt=gif&from=appmsg)

能够成功获取到database()的信息为security。

3.4 sqlmap注入

将burp suite捕获到的请求体保存为req.txt，再使用sqlmap注入

```
python sqlmap.py -r "‪C:\Users\demon\Desktop\security\req.txt" --batch -p User-Agent --level=5 --risk=3
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVGVqYdzL2x8ydcsCUj1oeG2LZ235NtC2IRaKTRJr7XDxWDmCdIXXa7vvvpHic6E9Uah4hqTgoKp3MA/640?wx_fmt=gif&from=appmsg)

这里判断出的注入方式，与我们尝试的一致，error-based

![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVGVqYdzL2x8ydcsCUj1oeG2tY35VDyLTHoVNoCvcJjqlS0A39esHJGjpMPNeUkH5kJAYaYQkAX3NQ/640?wx_fmt=png&from=appmsg)

至此完成第18关的http Header注入实战。

### 结语：第 18 关真正教会我的是什么？

第 18 关并不难，但它**非常“坏”**。
坏在于：
它不会告诉你“你错了哪里”，
只会用**完全沉默的页面**逼你反思自己的方法。

在这一关中，我第一次清晰地意识到：

* SQL 注入并不等于“改参数”
* 注入点也不一定存在于表单输入框
* **HTTP 请求中的任何用户可控字段，都可能成为攻击入口**

更重要的是，这一关让我完成了一次关键的思维转变：从“构造真假条件”转向“分析 SQL 语句结构”

当 SQL 从 `SELECT ... WHERE` 变成 `INSERT ... VALUES`，payload 的构造思路就必须随之改变。
再继续机械地使用 `and 1=1`，只会让自己越试越乱。

通过手动分析 INSERT 场景下的注入方式，并利用 `updatexml` 构造错误回显，最终成功验证了 Header 注入的存在；随后再使用 sqlmap 指定 `User-Agent` 参数进行自动化验证，也进一步印证了前面的判断。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVHNrxMtj4Y4Z6hGFDSYQ5Yu9VzwW1HJsVo4INnWEgrG57pkjsa8GN5zyNrbSAxgjYEzXVOtVWGcAQ/0?wx_fmt=png)

武文学网安

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVHNrxMtj4Y4Z6hGFDSYQ5Yu9VzwW1HJsVo4INnWEgrG57pkjsa8GN5zyNrbSAxgjYEzXVOtVWGcAQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过