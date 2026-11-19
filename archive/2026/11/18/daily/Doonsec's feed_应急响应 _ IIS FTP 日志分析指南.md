---
title: 应急响应 | IIS FTP 日志分析指南
url: https://mp.weixin.qq.com/s/-S7F2mRYU_dOazJ4fNOiuA
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:41:45.980292
---

# 应急响应 | IIS FTP 日志分析指南

# 应急响应 | IIS FTP 日志分析指南

原创

火星来的小男孩
火星来的小男孩

篝火信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

在攻防场景下，常常会遇到FTP服务被攻击的情况，这时需要对FTP 日志进行分析，它是排查文件传输问题、审计用户操作、发现异常访问的重要依据。

本篇文章主要讲解 IIS FTP 日志的日志配置、字段含义、命令关键字、状态码解读以及常见问题的排查方法。

![](https://mmbiz.qpic.cn/mmbiz_gif/CQf7uHzmVb1a36bBqjd11w2NQk1tzN9l3lG0z0TXCnVnQQNCVxIM3OWnmTR6lfLib2xQqps6Zub34WHdJbKQNQQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/prEia0ibIXVVtTuZV45p4UvYibwuzhB4pt42PRDq36DficibhS3fFalgBX3RgSl9RvicMSNiaiawUWPnERGZq6auh9Qu6aZ5TvqkIGHeEjUI3Z7MhHo/640?wx_fmt=png&from=appmsg)

一、IIS FTP日志的存储位置

IIS 部署的 FTP 服务器默认使用 W3C 扩展日志格式记录活动。

IIS FTP 日志默认保存在：

C:\inetpub\logs\LogFiles

该目录下通常会有类似 FTPSVC2、MSFTPSVC1或站点 ID 对应的子目录。

日志文件命名格式为：

u\_exYYMMDD.log

例如：

u\_ex261103.log

如果日志记录按本地时间滚动，文件名会按北京时间生成；但日志内容里的时间字段仍然是 UTC 时间。

![](https://mmbiz.qpic.cn/mmbiz_png/prEia0ibIXVVtpdMLB4nXSzlBicAPOexguGLpkjkibqn5SfL5EIGCx2j8U1Ibicw1Z4licLmicanKSe1ht9IrUOCcAj9UhZrKlWe3Biao8B9mkicJqvI/640?wx_fmt=png&from=appmsg)

二、时间字段不是北京时间

这是分析 IIS FTP 日志时最容易踩坑的地方。

W3C 格式日志中的 time 字段默认记录的是 UTC 时间。如果服务器位于中国，本地时间是东八区，那么日志时间通常比北京时间少 8 小时。

例如日志显示：

2026-11-03 06:20:15

对应的北京时间大约是：

2026-11-03 14:20:15

IIS 中有一个选项叫 “使用本地时间进行文件命名和滚动更新”，它只影响日志文件何时生成新文件，不会把日志内容里的时间改成北京时间。

因此，排查问题时建议统一将日志时间 +8 小时 再与业务时间对照。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/prEia0ibIXVVs0dmpg3Omfs9EsQze7Whq3HoBu33zQ6PKlS64Kmg6dxoPoXeL8B9Bg6f0s7mynYbLhAJFMtsPuBhbctVh4Zqic0W2Z6ia3WxYCY/640?wx_fmt=png&from=appmsg)

三、日志字段怎么看

打开日志文件后，第一行通常是字段定义，它决定了后面每一列数据的含义。

例如：

#Fields: date time c-ip cs-username s-ip s-port cs-method cs-uri-stem sc-status

![](https://mmbiz.qpic.cn/sz_mmbiz_png/prEia0ibIXVVuaDukUc46sBEJwaAZYrJ9yPZ0Q1VzdsEXDBH8Wx6mzZQQJdYXOKvgcqvvdq5D3Kp0PfQBObmcPNLGo1zCiaJRGK7SYLFyoYVQY/640?wx_fmt=png&from=appmsg)

IIS FTP 日志常用 W3C 字段如下：

|  |  |  |
| --- | --- | --- |
| **字段** | **含义** | **分析用途** |
| date | 请求日期 | 定位问题发生日期 |
| time | 请求时间 | 注意默认为 UTC |
| c-ip | 客户端 IP | 判断访问来源 |
| cs-username | 登录用户名 | 定位操作账号 |
| s-ip | 服务器 IP | 多网卡时区分访问入口 |
| s-port | 服务器端口 | 通常为 21 |
| cs-method | FTP  命令 | 判断用户做了什么 |
| cs-uri-stem | 文件或目录路径 | 判断访问了哪些资源 |
| sc-status | FTP  状态码 | 判断操作是否成功 |
| sc-win32-status | Windows  状态码 | 辅助判断系统层错误 |
| sc-bytes | 服务器发送字节数 | 评估下载流量 |
| cs-bytes | 服务器接收字节数 | 评估上传流量 |
| time-taken | 操作耗时 | 判断传输是否异常 |
| x-fullpath | 完整路径 | 更准确定位文件位置 |

如果日志里缺少 cs-method、cs-uri-stem、sc-status，分析价值会明显下降。建议在 IIS 管理器中进入对应 FTP 站点的 FTP 日志记录 → 选择 W3C 字段，补上这些字段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/prEia0ibIXVVtXxBicL46ibY1jKxQWtsZFVicmwKBwRp8ciamguRMZ8Ush0RhhSSP0RwNHV40oDWCNtF0sV7ibrI5cvGERwNLjS1flx88Fuqt8MrfY/640?wx_fmt=png&from=appmsg)

四、FTP 命令关键字含义

FTP 日志中的 cs-method 字段记录的是客户端发送给服务器的 FTP 命令。

1. 登录相关

|  |  |  |
| --- | --- | --- |
| **命令** | **含义** | **日志表现** |
| USER | 发送用户名 | 登录开始 |
| PASS | 发送密码 | 登录认证 |
| QUIT | 退出会话 | 会话结束 |

典型登录成功流程：

USER zhangsan   331

PASS \*\*\*\*\*\*     230

其中 331 表示需要密码，230 表示登录成功。

2. 目录浏览相关

|  |  |  |
| --- | --- | --- |
| **命令** | **含义** | **说明** |
| CWD | 切换目录 | 进入指定目录 |
| CDUP | 返回上级目录 | 相当于cd .. |
| PWD | 显示当前目录 | 确认当前位置 |
| LIST | 列出目录详情 | 常见目录浏览 |
| NLST | 列出文件名 | 轻量目录枚举 |
| MLSD | 标准化目录列表 | 程序化客户端常用 |
| MLST | 查询单个对象信息 | 获取文件属性 |

如果某个账号登录后连续执行大量 LIST、NLST、CWD，并且访问了多个敏感目录，可能是在进行目录探测。

3. 文件传输相关

|  |  |  |
| --- | --- | --- |
| **命令** | **含义** | **说明** |
| RETR | 下载文件 | 从服务器获取文件 |
| STOR | 上传文件 | 向服务器写入文件 |
| APPE | 追加文件 | 向远程文件尾部追加 |
| SIZE | 查询文件大小 | 常用于断点续传前判断 |
| REST | 设置续传偏移 | 配合 RETR/STOR 续传 |
| STOU | 唯一文件名存储 | 避免覆盖已有文件 |

典型下载流程：

PASV 227

RETR /data/report.zip 226

典型上传流程：

PASV 227

STOR /upload/backup.zip 226

如果日志中只有 RETR 或 STOR，但没有后续 226，说明传输可能未完成。

4. 文件管理相关

|  |  |  |
| --- | --- | --- |
| **命令** | **含义** | **说明** |
| DELE | 删除文件 | 重点关注 |
| RNFR | 重命名旧名称 | 重命名第一步 |
| RNTO | 重命名新名称 | 重命名第二步 |
| MKD | 创建目录 | 新建远程目录 |
| RMD | 删除目录 | 删除远程目录 |

例如：

DELE /pub/config.ini   250

表示文件删除成功；如果返回 550，则可能因为文件不存在或权限不足。

5. 传输模式相关

|  |  |  |
| --- | --- | --- |
| **命令** | **含义** | **说明** |
| PASV | 被动模式 | 客户端让服务器开放数据端口 |
| PORT | 主动模式 | 客户端告知服务器连接自己的端口 |

FTP 传输文件、列出目录时都需要建立数据连接。被动模式由服务器开放端口，主动模式由客户端开放端口。

如果日志中频繁出现 425 或 426，常见原因是防火墙、NAT 或端口协商失败，导致数据连接无法建立。

五、状态码怎么看

FTP 状态码记录在 sc-status 字段中，首位数字决定类别：

|  |  |  |
| --- | --- | --- |
| **类别** | **含义** | **常见码** |
| 1xx | 操作已开始 | 150  准备传输 |
| 2xx | 操作成功 | 200、226、230、250 |
| 3xx | 需要补充信息 | 331  需要密码 |
| 4xx | 暂时性失败 | 425、426、450 |
| 5xx | 永久性失败 | 530、550、552 |

重点状态码：

* 220：服务就绪；
* 226：传输完成；
* 227：进入被动模式；
* 230：登录成功；
* 331：用户名正确，需要密码；
* 425：无法打开数据连接；
* 426：连接关闭，传输中止；
* 452：磁盘空间不足；
* 530：未登录或认证失败；
* 550：文件不可用、无权限或未找到；
* 552：超出存储配额。

六、典型问题分析方法

1. 暴力破解与口令爆破

这是 FTP 最常见的入侵入口。筛选 sc-status=530（登录失败）与 230（登录成功），重点看三点：

* 同一 c-ip 在短时间内是否产生大量 USER/PASS + 530；
* 是否出现字典式用户名（如基于公司域名构造的账号列表）；
* 失败之后是否紧跟一次 230 成功。"大量失败 + 随后成功"是爆破成功的典型特征。

定性依据是时间-次数比例：正常用户不会在几秒内产生几十次失败。

2. 爆破成功后的行为还原

一旦确认某 IP 登录成功，立刻以该 IP 和账号为线索，按时间顺序拉出完整会话，重点看：

|  |  |
| --- | --- |
| **命令** | **应急意义** |
| LIST / NLST / MLSD | 是否大规模枚举目录，为数据窃取做准备 |
| CWD | 是否访问了业务无关的敏感目录 |
| RETR | 是否下载了敏感文件，结合sc-bytes 评估数据外流量 |
| STOR | 是否上传了后门、webshell、挖矿程序 |
| DELE / RMD | 是否删除日志或业务文件（反取证） |

判断上传/下载是否真正完成，看是否有 150 → 226 的完整闭环。

3. 非授权与异常账号排查

关注 cs-username 为空、为 anonymous/ftp/guest 的记录，以及离职人员账号、业务方不认识的账号的登录行为。若发现匿名登录成功，说明匿名访问未关闭，属于高危配置缺陷。

七、用 PowerShell 快速过滤日志

在 Windows 服务器上可以直接用 PowerShell 分析日志。

查找某个 IP 的记录：

Select-String -Path "C:\inetpub\logs\LogFiles\FTPSVC2\u\_ex261103.log" -Pattern "192.168.1.100"

筛选登录失败：

Select-String -Path "u\_ex261103.log" -Pattern "PASS" | Select-String -Pattern "530"

统计上传记录：

Select-String -Path "u\_ex261103.log" -Pattern "STOR"

统计下载记录：

Select-String -Path "u\_ex261103.log" -Pattern "RETR"

查找删除操作：

Select-String -Path "u\_ex261103.log" -Pattern "DELE"

八、总结

分析 FTP 日志时，建议按以下顺序还原会话：

1. 谁来的：看 c-ip、cs-username；
2. 什么时候来的：看 date、time，注意 UTC 转本地时间；
3. 做了什么：看 cs-method 和 cs-uri-stem；
4. 结果如何：看 sc-status；
5. 是否异常：关注重复登录失败、异常路径、大量删除、非工作时间操作；
6. 是否完整：检查是否有 150 + 226 的完整传输闭环。

FTP 日志分析的关键不是孤立地看某一条记录，而是把登录、目录浏览、文件传输、状态码串起来，还原一次完整的会话过程。这样既能排查上传下载失败，也能发现越权访问、暴力登录和异常删除等安全问题。

![](https://mmbiz.qpic.cn/mmbiz_gif/CQf7uHzmVb1a36bBqjd11w2NQk1tzN9lWGhsCxEo5MQ9FERnsRc00tLlOpTHQ8bicSWic2omFnFUsFstuXyabtDA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/CQf7uHzmVb1ibZHu1GGPhASBxFgzNZaS0OzicLMib0enpI59Wic0hgLW7BhlsGXSeGeo3o2IlxQgc1ekO2mCJ9Dt4g/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/CQf7uHzmVb1ibZHu1GGPhASBxFgzNZaS0juZN1fHqMNvGrUeqNzhVaR0W5HWpbmOfZAoPiaXjnX93hibm7iaHvZ5KA/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

**如果您觉得内容还不错的话，请关注我吧！**

**建议把公众号“篝火信安”设为星标，否则可能就看不到啦！因为公众号现在只对常读和星标的公众号才能展示大图推送。**

**操作方法：点击公众号页面右上角的【...】，然后点击【设为星标】即可。**

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/CQf7uHzmVb0EIJ0ELczkKSQrgZ1wuessmpgrvoBoc0mRN89FJMbDeXJQ0pGuUBicR84xicvbJe5iaqtVcpBuWMl4w/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过