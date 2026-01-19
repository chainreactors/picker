---
title: 漏洞挖掘实战系列（第14期）：高级SQL注入技巧 WAF绕过+盲注优化+实战案例
url: https://mp.weixin.qq.com/s/ALKYJ1dxxrpYBL1vKIQ1Zg
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:40:20.940229
---

# 漏洞挖掘实战系列（第14期）：高级SQL注入技巧 WAF绕过+盲注优化+实战案例

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaLzURuoralbO2ibJtf2tmhFx7IAcV73qNvybria0YTArrzH1GIq880LglW4iaicXUy2V2EWIrU1ZEorORK6hMMuRaA/0?wx_fmt=jpeg)

# 漏洞挖掘实战系列（第14期）：高级SQL注入技巧 WAF绕过+盲注优化+实战案例

原创

点击关注👉
点击关注👉

网络安全学习室

![]()

在小说阅读器中沉浸阅读

在前13期内容中，我们从基础漏洞挖到业务逻辑漏洞，SQL注入作为Web漏洞的“常青树”，从入门的联合查询、报错注入，到实战中的盲注、WAF绕过，难度逐步升级。很多人卡在“明明有注入点，却被WAF拦截”“盲注耗时太久，拿不到数据”的问题上。

这一期，我们聚焦**高级SQL注入实战**，拆解3大类核心技巧：WAF绕过全方案、盲注高效优化、复杂场景注入（预编译绕过、存储过程注入），每个技巧都搭配可复现案例和Payload，帮你搞定CTF和真实渗透中80%的复杂SQL注入场景！

无论你是被WAF卡壳的CTF选手，还是在真实业务中挖不到注入的渗透工程师，这篇内容都能直接落地使用。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralagtWOApyfnA4Ph5ibXEFeXEz1rG4l9hJd1P5bSP5Rj7pyyeYB001587Z9Cb0APJbDZ2PWCNxzCxrA/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

---

## 一、先搞懂：WAF拦截SQL注入的核心逻辑

要绕过WAF，先明白它是怎么拦截的。常见WAF（如云WAF、服务器WAF、应用层WAF）拦截SQL注入的方式主要有3种：

1. **特征匹配拦截**：检测请求中是否包含敏感关键字（如union、select、and、or、sleep()）、特殊符号（如'、"、#、--），匹配到则直接拦截；
2. **语义分析拦截**：更智能的WAF会分析SQL语句语义，判断是否存在注入逻辑（如“select 字段 from 表 where id=1 and 1=1”），而非单纯匹配关键字；
3. **行为检测拦截**：通过监控请求频率、参数篡改行为（如多次修改id参数值），判断是否为恶意注入攻击，触发拦截机制。

针对不同拦截方式，我们对应不同的绕过策略，核心思路是：**破坏WAF的检测规则，同时保证SQL语句在后端正常执行**。

---

## 二、WAF绕过全方案（实战高频技巧）

### 技巧1：关键字变形绕过（针对特征匹配WAF） ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwqjBoBFOXkF34ibzw5KkWaJnsurmjeB9icvjueQ2ZDegFOmU9RAcPd84xfxlXHLfWCv/640?wx_fmt=svg&from=appmsg)

这类WAF仅拦截固定关键字，通过变形、替换、拆分关键字，可轻松绕过。适用于入门级WAF、自研简易WAF。

#### 1. 常见变形方法 ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwbvR6N2mxgJz1wrdm4iavL2fKicWE44ZlCmbmSqKnmLiaU6Xsz4EpdgzSPPuyBSC51Md/640?wx_fmt=svg&from=appmsg)

* **大小写混淆**：最基础且高效的方法，WAF常只检测小写关键字，后端SQL语句执行不区分大小写。 示例：`SeLeCt * FrOm users WhErE id=1`；
* **关键字拆分/拼接**：用空格、注释、特殊符号拆分关键字，或通过字符串拼接函数构造关键字。 示例1（注释拆分）：`sel/*abc*/ect * from users`（/*abc*/为SQL注释，WAF可能忽略注释内容，后端正常解析）； 示例2（字符串拼接，MySQL）：`concat('sel','ect') * from users`；
* **等价关键字替换**：用功能相同的关键字替换敏感词。 示例：用“&&”替换“and”、“||”替换“or”、“/*!50000union*/”替换“union”（/*!50000...*/为MySQL版本注释，仅5.0.0以上版本执行，WAF可能不识别）；
* **特殊符号逃逸**：在关键字前后加特殊符号（如%00、%20、%09），部分WAF会忽略这些符号，后端自动过滤。 示例：`s%00elect * from users`。

#### 2. 实战案例：大小写+注释绕过入门WAF ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwbvR6N2mxgJz1wrdm4iavL2fKicWE44ZlCmbmSqKnmLiaU6Xsz4EpdgzSPPuyBSC51Md/640?wx_fmt=svg&from=appmsg)

场景：某Web系统id参数存在注入点，输入`id=1 and 1=1`被WAF拦截，提示“存在恶意注入行为”。

绕过步骤：

1. 尝试大小写混淆：`id=1 AnD 1=1`，仍被拦截（WAF已适配大小写检测）；
2. 添加注释拆分：`id=1 A/*x*/ND 1=1`，成功绕过WAF，后端执行正常，页面返回与id=1一致；
3. 进一步构造注入语句：`id=1 A/*x*/ND 1=2`，页面无数据返回，确认注入点有效。

#### 3. 注意事项 ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwbvR6N2mxgJz1wrdm4iavL2fKicWE44ZlCmbmSqKnmLiaU6Xsz4EpdgzSPPuyBSC51Md/640?wx_fmt=svg&from=appmsg)

注释拆分需结合后端数据库类型（MySQL支持/*...*/，Access支持'--'），避免注释格式错误导致SQL执行失败。

### 技巧2：参数污染绕过（针对应用层WAF） ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwqjBoBFOXkF34ibzw5KkWaJnsurmjeB9icvjueQ2ZDegFOmU9RAcPd84xfxlXHLfWCv/640?wx_fmt=svg&from=appmsg)

部分应用层WAF仅检测第一个参数值，通过重复提交参数，让WAF拦截第一个参数，后端执行第二个参数，实现绕过。

#### 1. 原理 ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwbvR6N2mxgJz1wrdm4iavL2fKicWE44ZlCmbmSqKnmLiaU6Xsz4EpdgzSPPuyBSC51Md/640?wx_fmt=svg&from=appmsg)

例如请求`id=1 and 1=1&id=2`，WAF可能仅检测第一个id参数（id=1 and 1=1）并拦截，但部分后端框架（如PHP）会取最后一个参数值（id=2）执行，此时可构造恶意参数放在后面。

#### 2. 实战案例：参数重复绕过WAF ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwbvR6N2mxgJz1wrdm4iavL2fKicWE44ZlCmbmSqKnmLiaU6Xsz4EpdgzSPPuyBSC51Md/640?wx_fmt=svg&from=appmsg)

场景：某系统请求`http://target.com/list?id=1`存在注入点，输入`id=1 union select 1,2,3`被拦截。

绕过步骤：

1. 构造参数污染请求：`http://target.com/list?id=1&id=1 union/*x*/select 1,2,3 from users`；
2. WAF检测第一个id参数（id=1）无异常，放行请求；后端取最后一个id参数执行，成功执行注入语句，页面返回字段位置（2为可显字段）；
3. 后续可正常读取数据：`id=1&id=1 union/*x*/select 1,username,password from users`。

### 技巧3：编码绕过（针对URL/参数编码检测WAF） ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwqjBoBFOXkF34ibzw5KkWaJnsurmjeB9icvjueQ2ZDegFOmU9RAcPd84xfxlXHLfWCv/640?wx_fmt=svg&from=appmsg)

通过对注入语句进行URL编码、Unicode编码、ASCII编码，破坏WAF的特征匹配，后端接收后自动解码执行。适用于对编码解析不完整的WAF。

#### 1. 常见编码方式 ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwbvR6N2mxgJz1wrdm4iavL2fKicWE44ZlCmbmSqKnmLiaU6Xsz4EpdgzSPPuyBSC51Md/640?wx_fmt=svg&from=appmsg)

* **URL双重编码**：对敏感字符进行两次URL编码（如'的URL编码为%27，双重编码为%2527），部分WAF仅解码一次，无法识别恶意字符；
* **Unicode编码**：将关键字转换为Unicode编码（如select的Unicode编码为\u0073\u0065\u006c\u0065\u0063\u0074）；
* **ASCII编码（MySQL）**：用ASCII码表示字符（如'a'的ASCII码为0x61），适用于拦截字符串关键字的场景。

#### 2. 实战案例：URL双重编码绕过WAF ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwbvR6N2mxgJz1wrdm4iavL2fKicWE44ZlCmbmSqKnmLiaU6Xsz4EpdgzSPPuyBSC51Md/640?wx_fmt=svg&from=appmsg)

场景：输入`id=1'`被WAF拦截，提示“存在非法字符”。

绕过步骤：

1. 对单引号（'）进行URL编码：%27，构造请求`id=1%27`，仍被拦截（WAF识别URL编码后的单引号）；
2. 对%27进行二次URL编码：%2527，构造请求`id=1%2527`；
3. WAF仅解码一次，得到%27，未识别为单引号，放行请求；后端自动二次解码，得到'，执行SQL语句`select * from users where id=1'`，页面报错，注入点确认。

### 技巧4：语义混淆绕过（针对语义分析WAF） ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwqjBoBFOXkF34ibzw5KkWaJnsurmjeB9icvjueQ2ZDegFOmU9RAcPd84xfxlXHLfWCv/640?wx_fmt=svg&from=appmsg)

语义分析WAF能识别完整注入逻辑，需通过打乱SQL语句结构、添加无效逻辑，混淆WAF的语义判断，同时保证后端正常执行。

#### 1. 常见方法 ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwbvR6N2mxgJz1wrdm4iavL2fKicWE44ZlCmbmSqKnmLiaU6Xsz4EpdgzSPPuyBSC51Md/640?wx_fmt=svg&from=appmsg)

* **添加无效逻辑**：在注入语句中加入无意义的计算、函数，不影响结果但打乱语义。 示例：`id=1 and (1=2 or 3=3) and sleep(5)`（WAF可能误判为普通逻辑判断，后端执行sleep(5)，产生延迟）；
* **利用SQL函数变形**：用等价函数替换敏感函数。 示例：用“benchmark(1000000,md5('a'))”替换“sleep(5)”（MySQL中benchmark函数重复执行指定操作，产生延迟效果，部分WAF不拦截）；
* **子查询嵌套**：将注入语句嵌套在子查询中，混淆语义。 示例：`id=1 and (select 1 from (select count(*),concat((select username from users limit 1),floor(rand(0)*2))x from information_schema.tables group by x)a)`。

---

## 三、盲注高效优化（告别“耗时久、易中断”）

盲注（布尔盲注、时间盲注）是实战中最常用的注入方式，但默认逐字符猜解效率极低，甚至因请求频率过高被拦截。以下优化技巧能让盲注效率提升10倍以上。

### 技巧1：批量猜解（一次猜解多位字符） ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwqjBoBFOXkF34ibzw5KkWaJnsurmjeB9icvjueQ2ZDegFOmU9RAcPd84xfxlXHLfWCv/640?wx_fmt=svg&from=appmsg)

默认盲注一次猜解1位字符，通过SQL的位运算、字符串函数，可一次猜解4位、8位字符，大幅减少请求次数。

#### 1. 实战案例：MySQL布尔盲注批量猜解 ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwbvR6N2mxgJz1wrdm4iavL2fKicWE44ZlCmbmSqKnmLiaU6Xsz4EpdgzSPPuyBSC51Md/640?wx_fmt=svg&from=appmsg)

场景：id参数存在布尔盲注，需猜解users表中username字段值，默认逐位猜解需多次请求。

优化前（逐位猜解）：`id=1 and substring((select username from users limit 0,1),1,1)='a'`（每次猜解第1位字符，需26次请求确认字母）；

优化后（一次猜解4位字符，利用ASCII码）：`id=1 and (ascii(substr((select username from users limit 0,1),1,1)) & 0xF0) = 0x60`；

原理：用&（位与运算）提取ASCII码的高4位，先确定高4位值，再猜解低4位，每次请求可缩小范围至16种可能，请求次数减少60%以上。

### 技巧2：调整延迟时间（时间盲注专属） ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwqjBoBFOXkF34ibzw5KkWaJnsurmjeB9icvjueQ2ZDegFOmU9RAcPd84xfxlXHLfWCv/640?wx_fmt=svg&from=appmsg)

时间盲注常用sleep()函数，默认延迟5秒，可根据网络环境调整延迟时间（如2秒），减少总耗时；同时避免延迟过短（如0.5秒），导致误判。

优化示例：`id=1 and if((substring(username,1,1)='a'),sleep(2),0)`（正确则延迟2秒，错误无延迟）；

进阶：用benchmark函数替代sleep，避免sleep被WAF拦截。`id=1 and if((substring(username,1,1)='a'),benchmark(1000000,md5('a')),0)`。

### 技巧3：脚本自动化（批量执行+异常重试） ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwqjBoBFOXkF34ibzw5KkWaJnsurmjeB9icvjueQ2ZDegFOmU9RAcPd84xfxlXHLfWCv/640?wx_fmt=svg&from=appmsg)

手动盲注效率极低，用Python+requests编写自动化脚本，实现批量猜解、异常重试、请求频率控制，避免手动操作失误和WAF拦截。

#### 1. 自动化脚本示例（MySQL时间盲注） ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwbvR6N2mxgJz1wrdm4iavL2fKicWE44ZlCmbmSqKnmLiaU6Xsz4EpdgzSPPuyBSC51Md/640?wx_fmt=svg&from=appmsg)

#### 2. 脚本优化技巧 ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwbvR6N2mxgJz1wrdm4iavL2fKicWE44ZlCmbmSqKnmLiaU6Xsz4EpdgzSPPuyBSC51Md/640?wx_fmt=svg&from=appmsg)

* 添加请求头伪装（User-Agent、Referer），模拟正常浏览器请求；
* 设置代理IP池，避免单一IP请求频率过高被封禁；
* 加入异常捕获机制，请求失败时自动重试，保证脚本稳定运行。

---

## 四、复杂场景SQL注入实战

### 场景1：预编译语句绕过（MySQL/PostgreSQL） ![](https://mmbiz.qpic.cn/mmbiz_svg/icXtjp9jsR5Q5PM60xMjQq9cfcV9Z8zXwqjBoBFOXkF34ibzw5KkWaJnsurmjeB9icvjueQ2ZDegFOmU9RAcPd84xfxlXHLfWCv/640?wx_fmt=svg&fro...