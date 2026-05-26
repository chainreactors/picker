---
title: 内网拿到数据库还在一个个表翻找吗？这个工具帮你自动化识别，提取，文末速取！
url: https://mp.weixin.qq.com/s/kNNGuq5WhTOA5p3t6Np_5g
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T05:59:51.152872
---

# 内网拿到数据库还在一个个表翻找吗？这个工具帮你自动化识别，提取，文末速取！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IGws6hSXN0zusFJGt4ZygSP63UTsk1uXL550fY9MiaciccKuLYX8kRXClRWWdleVcGEgHicNubEED7Ehh63m8AiaMOfJTUjBOwvE3T1fjoIF9uc/0?wx_fmt=jpeg)

# 内网拿到数据库还在一个个表翻找吗？这个工具帮你自动化识别，提取，文末速取！

FL\_Clover
FL\_Clover

网络安全007

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

很多师傅在打内网的时候，总是会弱口令或者密码喷洒获得很多数据库的权限，但是一个个表去翻找里面的数据就很让人困恼，这个工具可以自动化进行敏感信息识别。（文末附下载地址）

一、工具介绍

    database\_scan 是一个 Go 编写的数据库敏感信息检索工具，用于检查开发数据库中是否存在手机号、身份证、地址、账号、密码、邮箱、银行卡、token/secret 等敏感信息。默认终端表格输出。

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yJV2icFibaE4ibec8Sj0sjNQuA1UdmIQLCfnpmrFvJg4ic1Pgk9TQq8NunhpBu77VzhPNVVdYciaYe7jkdPPNIQY755ejuJDicKcD8Q/640?wx_fmt=png&from=appmsg)

二、工具支持能力

* 数据库：MySQL/MariaDB/TiDB、MSSQL、PostgreSQL、Oracle，以及多种 MySQL/PostgreSQL 协议兼容国产数据库
* 代理：直连、SOCKS5、HTTP CONNECT
* 认证：命令行密码或隐藏交互输入
* 输出：连接信息、按表分组的敏感字段、存在行数和类似 SQL 查询结果的整行真实样例值

* 检索模式：

* field-content：根据表/字段名定位敏感字段，再检索字段内容
* field-name：只检索敏感表名/字段名
* content：扫描字段内容
* all：执行全部模式

* 敏感级别：

* high：身份证、密码/密钥、银行卡
* medium：手机号、邮箱
* low：地址、用户名/账号
* all：全部级别，默认值

三、工具参数

* --type：数据库类型，见下方支持列表
* --host / --port：目标地址和端口，端口不填时使用默认端口；也支持 --host host:port 或位置参数 host:port
* --user / --password：账号密码；密码不填时交互输入；Redis 可只传 --password
* --database：指定要扫描的单个数据库；Redis 中表示 DB 编号，例如 --database 2
* --table：只扫描指定数据库中的某一张表，需要同时指定 --database；支持 Users 或 dbo.Users
* --fscan result.txt：解析 fscan v2.1.2 / 1.8.4 扫描结果中的 MySQL、MariaDB、MSSQL、PostgreSQL、Oracle、Redis 凭据，并逐个接入扫描；同一结果文件可包含多个地址、端口、账号或密码，支持终端输出和保存结果文件
* --proxy socks5://...|http://...：代理地址
* --mode field-content|field-name|content|all：检索模式，默认 field-content
* --level all|high|medium|low：按敏感级别检索，默认 all；high 只检索身份证、密码/密钥、银行卡等最高敏信息
* --limit：每张命中表最多展示整行样例数量，默认 15
* --include-system：包含系统库
* --mask：样例值脱敏显示
* --no-color：关闭敏感字段和值的颜色标记，适合复制到报告或重定向到文件
* --no-banner：关闭启动随机颜文字 banner
* --no-progress：关闭运行状态/扫描进度输出
* --output result.xlsx：将扫描结果写入 Excel 文件；每个命中表一个 Sheet，上方是敏感字段清单，下方是整行样例数据，敏感字段和值会按风险颜色标记
* --split-output：配合 --fscan 和 --output 使用，除总表外按每个数据库凭据额外生成独立 Excel 文件
* --workers：按表并发扫描数量，默认 1，即不启用并发；例如 --workers 4
* --timeout：单查询超时，默认 15s
* --sql：执行自定义 SQL；按需求原样执行，不限制为只读

四、支持数据库类型

* 原生支持：mysql、mariadb、mssql、sqlserver、postgres、postgresql、oracle、go-ora、redis
* MySQL 协议兼容：tidb、oceanbase、oceanbase-mysql、polardb-mysql、doris、starrocks、gbase-mysql
* PostgreSQL 协议兼容：opengauss、gaussdb、kingbase、kingbasees、highgo、polardb-postgres
* 默认端口：MySQL 协议族 3306，MSSQL 1433，PostgreSQL 协议族 5432，Oracle 1521，Redis 6379
* Redis 会按 SCAN 枚举 key，并按类型读取 string、hash、list、set、zset 的样例内容。终端和 Excel 使用 Redis 专用输出结构，列为 Target、DB、Key、Type、TTL、Path/Field、Value、命中类型、敏感级别、判断依据；Excel 会生成 Redis 汇总 和 Redis Keys 两个 Sheet。

* 协议兼容数据库会复用 MySQL 或 PostgreSQL 的连接协议、代理拨号和元数据扫描方式。达梦 DM、GBase 8s、神通等需要专用驱动、ODBC、CGO 或无法确认代理拨号能力的数据库暂不内置，避免破坏当前多平台发布包。

五、工具使用

1.常规使用

```
./database_scan --type mysql --host 127.0.0.1 --port 3306 --user root --password pass也可以把地址和端口写在一起，--host 192.0.2.10:1433 或直接把目标作为位置参数：./database_scan --type mssql 192.0.2.10:1433 --user sa --password pass如果不希望数据库密码出现在 shell 历史记录中，可以省略 --password，程序会提示隐藏输入：./database_scan --type mysql --host 127.0.0.1 --port 3306 --user root./database_scan --type postgres --host 198.51.100.10 --user dev --password pass --mode content --limit 15
```

2.扫描 Redis key/value 中的敏感信息

```
./database_scan --type redis --host 127.0.0.1 --port 6379 --password pass --limit 20 --output redis-scan.xlsx
```

3.解析 fscan 扫描结果中的数据库凭据，并对所有命中的数据库一键接入扫描

```
./database_scan --fscan fscan-result.txt --workers 4 --limit 5 --output fscan-database-scan.xlsx
```

4.同时生成总表和每个数据库凭据的独立表格文件：

```
./database_scan --fscan fscan-result.txt --workers 4 --limit 5 --output fscan-database-scan.xlsx --split-output
```

六、工具使用预览效果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IGws6hSXN0yiaribrlxibylQ1swx17AfjKUjcbNgic89LrMUPzhRcG9IjGnlwmG8pKVicfl7M6BbAWGW56gvwol8MqX3XwOHSkKElOKSLpbntAoQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yl8wuNJ07tdM6QH2yaNplsYLTrl5J1uEQeUYQcNlA7UDBvawR0HZsd0UK0Mx2ibFCibHxukGXnKicRnicetX87o7VrJcSsOMQdibMQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IGws6hSXN0wdFdPY2ZbHRFxfiam21W5KZsTPe9gdIkicw0QDwicVib7BO0L2qO7ZS9QeQ9cTRljWdUUPlASSILITucD96OUTKJ8NMKaMQAicmGao/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IGws6hSXN0zsVtdLZ1iaSSibCyCRGWsicoPibYAgQxXibJQz10qqicbiciaiawqaWce7Qbfct94zNLpn1iariaR1jjibnNVdO6jdGWZxKUVmP9mMXxBgg6Y/640?wx_fmt=png&from=appmsg)

七、工具获取

**关注公众号后台回复“0525****”均可获取下载链接**

【广告时间】

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IGws6hSXN0wrllZpa6Jibd7mS3HML58S7y79RPF3e89QYPgdabgmfqibm3GFfDtR2hzZExtygLNrE7HNWUmf4onFqkloayASyNibXDEEDL0jt0/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

**免责声明：**

 本文章仅做网络安全技术研究使用！另利用网络安全007公众号所提供的所有信息进行违法犯罪或造成任何后果及损失，均由**使用者自身承担负责**，与网络安全007公众号**无任何关系**，也不为其负任何责任，**请各位自重！**公众号发表的一切文章如有侵权烦请私信联系告知，我们会立即删除并对您表达最诚挚的歉意！感谢您的理解！**让我们一起为中国网络安全事业尽一份自己的绵薄之力！**

---推荐阅读---

[攻防演习系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4480577090483748870#wechat_redirect)

[渗透技术文章系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4483666897053253633#wechat_redirect)

[未授权漏洞系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4483456618323345413#wechat_redirect)

[HW专项系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4483461171911426059#wechat_redirect)

[应急响应系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=2735815599062548484#wechat_redirect)

[工具推荐系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4483471065368592394#wechat_redirect)

写作不易，分享快乐

期待你的 **分享**●**点赞●在看**●关注**●收藏******

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yC4UvVZTh0GWblmLs0dtN1Sfnf88e3vkpokovgdsQAfPI16CnM3C7S6uNVNGHtnsiaFU1via2Bibo92ria29FVIMstgj6wQDg9XbI/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yhaJkO4MOgVsUQPeanvrkvkicst8BvPqz4WUDrjRDYugcOD44S3qjpgr5MvZzZBiaEggxoicGmeNfiaZGxW2x20MHp2WxNZpKFbVQ/0?wx_fmt=png)

网络安全007

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yhaJkO4MOgVsUQPeanvrkvkicst8BvPqz4WUDrjRDYugcOD44S3qjpgr5MvZzZBiaEggxoicGmeNfiaZGxW2x20MHp2WxNZpKFbVQ/0?wx_fmt=png)

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