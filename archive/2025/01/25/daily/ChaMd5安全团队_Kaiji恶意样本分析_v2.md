---
title: Kaiji恶意样本分析_v2
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247511902&idx=1&sn=5a5087aec514f7b15779c18c089f0108&chksm=e89d8786dfea0e90e92921d5e1165a96c3c07af7d978f5c64f6eb6298ffd10e0112f71c100d4&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2025-01-25
fetch_date: 2025-10-06T20:10:56.984128
---

# Kaiji恶意样本分析_v2

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatujFwW7AUS8NftOmicWicVlss7PrrXg96rzfnGgHC5l94rel1pnGZQk1xtA/0?wx_fmt=jpeg)

# Kaiji恶意样本分析\_v2

原创

YoungReal

ChaMd5安全团队

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

###

# 1.信息收集

## 1.1 目标挑选

使用https[:]//urlhaus.abuse.ch查找存活的可疑网站，可以自定义其他标签，比如文件格式、家族标签，filetype:doc or tag:Mozi。

https[:]//urlhaus.abuse.ch/browse.php?search=url\_status%3Aonline

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatuj0dh67tNqibPXJk3licWYbMer3Dz0kMjp2AmiaiaHaDLiaJk8ZSPNHyKvB6Q/640?wx_fmt=png&from=appmsg)

## 1.2 恶意样本挑选

访问存活的恶意链接，发现攻击者生成了支持多种架构的样本，其中amd64下载点击量最高

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatujh9SYAq8gmClUjDl1VrecicEwgoD9bcxywicFeicfcX7ibByldb1tqfFsyA/640?wx_fmt=png&from=appmsg)

此处选择恶意链接中的amd架构样本进行分析 http[:]//198.251.82.160:20722/b/amd64

在不下载恶意文件的情况下，可以直接通过threatquery计算要分析的样本的SHA256，https[:]//threatquery.com/engines/url.html?value=http%3A%2F%2F198.251.82.160%3A20722%2Fb%2Famd64&type=url

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatuj7KoibtvVHByIfGarQV1nlEO023IpQlx3YLSh1YBnbV6j7cyB5VeV3DA/640?wx_fmt=png&from=appmsg)

```
SHA256: 66d9d837015f3f840418f5b61ce78c7fa8648e9b1b3f949c3c6a0c7d3b28ad75
```

# 2.样本分析

## 2.1公开威胁情报分析

在virustotal上有该样本的分析记录，被多款杀软查杀并且被判定为Kaiji僵尸网络木马；该木马于2020年被MalwareMustDie非盈利白帽安全研究组织发现；2022年，Black Lotus Labs评估Chaos恶意软件是Kaiji的变体；2023年，被奇安信威胁情报中心发现Kaiji与来自中国的Ares巨型僵尸网络租赁团伙有关。从首次发现至今也被trendmicro、intezer、elastic security labs等安全公司进行多次分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatuj7JxQBgtWolDrs9hngQbnaXWialYEwXSR1pDExmyfRV1OcJb2qPIsXSg/640?wx_fmt=png&from=appmsg)

## 2.2 样本分析

此文主要对比分析以下两个版本的区别

| 文件名 | sha256 |
| --- | --- |
| amd64 | 66d9d837015f3f840418f5b61ce78c7fa8648e9b1b3f949c3c6a0c7d3b28ad75 |
| linux\_amd64 | d3965aeab57d429b0cb28a2853e941a0710294b2159755ea354bf32a723fef3a |

### 2.2.1相同点

1.命令劫持

劫持ps、ss、netstat、dir、ls、find、lsof、top命令，并修改文件时戳，以规避检查

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatujcgvDsIRoDYhawvX6z15KTEYMJf6DCZBRf14AEJJ9ltS7EXqZtibkYeQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatujV1NiaGlwBT6tHAribkictQ8RJRsqLBOFbiclJvpGCQqFyt7DGy8CXndS4Q/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatujQL5UGjS9bg2mwic2adUREOPBxZvjSMviapWcJzpicAIncrpDiaEVPkibpWA/640?wx_fmt=png&from=appmsg)

2.自启动

2.1 修改crontab计划任务，每分钟启动/usr/lib/libgdi.so.0.8.2

`echo "*/1 * * * * root /.mod " >> /etc/crontab`

2.2 绕过SELinux安全限制

`cd /boot;ausearch -c 'system.pub' --raw | audit2allow -M my-Systemmod;semodule -X 300 -i my-Systemmod.pp`

2.3 伪装成"quotaon"服务（磁盘配额服务）

```
cd /boot;systemctl daemon-reload;systemctl enable quotaon.service;systemctl start quotaon.service;journalctl -xe --no-pager"
```

### 2.2.2不同点

1.检查相同的进程名称，ksoftirqd/0、rcu\_gp、ksmd，但是新版本的检查逻辑比较复杂

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatujXzv0iaWdnCp6dCPA5JlEiaWOPL2uKRFDG9ibsJbrGwBv0WrcOkoaVzguw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatujow8bBicwGibHry8EQ7Mzc8vQFmyM9GbtcKHopNMQFicjASC1Zdw8bcPKA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatujNqIG0VibRWGe6g6SdzvcagSDsRY4MVCWppCkAuWdKbVlaPKBbJ9jiaxg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatujD3ibyuEbDibeZnBjcGtZrWMp1TC7FvRGMibrZjwibVV6KKRW4xFadZ093w/640?wx_fmt=png&from=appmsg)

2.配置文件操作

配置文件搜索，遍历多个系统路径

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatujwAK0IuU5ZszicO2bqiaWB4XSxq4dSdketibwTjibKic2G7kHJteEpNHY0tg/640?wx_fmt=png&from=appmsg)

读取配置文件/.ffff4444，解密配置文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatujmtugWeqpEOlLHoO4icTL2nZeqcltA53icqibpdFcGPo29kbZugszhXsJw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatujicob6Rz24DzgfMFj3sZLuNL8lBvCib0fh1gR7N3Cokl01mId84USMGfQ/640?wx_fmt=png&from=appmsg)

配置命令以"<F><F><F><F>"为分隔符，配置文件支持8种参数。此前奇安信分析过类似样本，分隔符为"[a=r=e=s]"，配置文件支持5种参数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatujtjQhgIdQoOw3UKq1hfhG0N15tdUuXEJljAMSIAUqFxpeDoUk9fG13Q/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatujKrnDL0VA682O5FsCETEY8tIic6OG6aHGvy25mfoysJP47aRoPk7BibPg/640?wx_fmt=png&from=appmsg)

| 参数名 | 作用 | 判断依据 | 代码位置 |
| --- | --- | --- | --- |
| End | 配置文件结束标记，用于标识配置读取完成 | 解析完成后的处理流程，以及对应的字符串比较操作 | 0x646f94 |
| Pid | 进程ID管理，用于控制和监视目标进程 | 1. 调用strconv\_Atoi转换数字 2. 与Kill系统调用关联 3. 存储在关键内存位置 | 0x646fe6-0x647003 |
| Size | 资源大小限制，控制程序运行资源使用 | 1. 写入全局配置变量 2. 影响内存分配逻辑 3. 用于资源控制检查 | 0x647026-0x647036 |
| Begin | 启动控制标记，影响程序初始化流程 | 1. 影响启动流程 2. 与初始化代码相关 3. 控制功能模块加载 | 0x64708a-0x647096 |
| Thread | 线程数量控制，管理并发执行 | 1. 用于并发控制 2. 影响协程创建 3. 与runtime\_newproc调用相关 | 0x6470f2 |
| Remarks | 附加信息存储，保存额外配置说明 | 1. 存储额外配置信息 2. 无直接功能影响 3. 用于标记或注释 | 0x647158-0x64716a |
| Version | 版本控制，确保功能兼容性 | 1. 版本号比较逻辑 2. 影响特定功能启用 3. 控制程序行为 | 0x6471b4-0x6471c4 |
| Backdoor | 后门功能控制，管理特殊访问权限 | 1. 设置全局标记变量 2. 控制特殊功能启用 3. 影响程序关键行为 | 0x6471f0-0x647218 |

3.通信协议优化

通信协议相关函数

| 函数名 | 位置 | 主要功能 | 特征 | 判断依据 |
| --- | --- | --- | --- | --- |
| main.Http | 645760 | HTTP协议实现 | - 设置HTTP请求头(User-Agent、Accept等) - 构造HTTP请求 - 处理响应 | 1. 设置HTTP头部特征字符串(UA、Accept) `649EDB`处设置请求头 2. 调用net\_url\_Parse解析URL `6457C5` 3. 使用`WriteMessage`发送HTTP消息 |
| main.Tcp\_Keep | 64DA80 | TCP持久连接 | - 创建TCP socket - 设置socket选项 - 保持连接活跃 | 1. 调用syscall.socket创建socket `64AE43` 2. 调用syscall\_Connect进行连接 `64B061` 3. 存在socket保活代码 |
| main.Udp | 64AC60 | UDP协议实现 | - 创建UDP socket - 设置UDP头 - 发送/接收UDP数据包 | 1. UDP socket创建 `64AE43` 2. UDP头部构造代码段 `64AE56-64AF00` 3. 使用sendto发包逻辑 |
| main.Raw | 649DC0 | 原始套接字实现 | - 创建原始socket - 直接操作IP头 - 可用于IP欺骗 | 1. 原始socket创建标志 `64A000` 2. IP头部手动构造代码 `64A0E2` 3. 直接操作网络层数据 |

TLS/加密相关函数

| 函数名 | 位置 | 主要功能 | 特征 | 判断依据 |
| --- | --- | --- | --- | --- |
| main.Tls\_Keep | 64E7E0 | TLS持久连接 | - 建立TLS会话 - 维持加密通道 - 处理证书验证 | 1. TLS Config配置 `64E834` 2. 调用tls握手函数 `64E950` 3. 保持TLS会话代码 |
| main.Tls | 64E2A0 | TLS基础实现 | - TLS握手 - 加密通信 - 会话管理 | 1. TLS握手代码 `64E2A0` 2. 加密通信实现 `64E3D9` 3. 会话状态管理代码 |
| main.Ws\_Keep | 651000 | WebSocket保持连接 | - WebSocket握手 - 保持连接 - 心跳机制 | 1. WebSocket握手实现 `6510B5` 2. 连接保持逻辑 `651021` 3. 心跳检测代码 |

数据处理函数

| 函数名 | 位置 | 主要功能 | 特征 | 判断依据 |
| --- | --- | --- | --- | --- |
| main.Ws\_Read | 651680 | WebSocket数据读取 | 读取WebSocket帧 处理分片消息 | 1. WebSocket帧解析 `651680` 2. 处理分片消息代码 `6516E0` |
| main.Tcp\_Read | 64E120 | TCP数据读取 | 读取TCP数据 缓冲区管理 | 1. TCP读取循环 `64E156` 2. 缓冲区管理代码 `64E190` |
| main.Tls\_Read | 64F160 | TLS数据读取 | 读取加密数据 解密处理 | 1. TLS读取实现 `64F160` 2. 解密处理逻辑 `64F1B3` |

网络攻击功能

| 函数名 | 位置 | 用途 | 特征 | 判断依据 |
| --- | --- | --- | --- | --- |
| main.Raw | 649DC0 | 原始数据包注入 | 可构造任意IP包 可用于DDoS攻击 | 1. 可自定义IP头 2. 高速发包循环 `649F94-649FE0` 3. 无协议限制 |
| main.Udp | 64AC60 | UDP flooding | 快速发送UDP包 可用于UDP flood | 1. UDP快速发包循环 2. 最小化错误处理 3. 并发发包设计 |
| main.Http | 645760 | HTTP flooding | 批量HTTP请求 可用于CC攻击 | 1. 批量请求逻辑 2. 资源耗尽型设计 3. 并发请求实现 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTiaFnaCGZ8j4sjFUiaw7iatuj8ibDmpQxJteqx78DRw7z2tyjn6oqjWGMDiaPCtIWQDTMYZr8we35Uy5A/640?wx_fmt=png&from=appmsg)

使用any.run分析样本的C2地址为app[.]r727.ru

# 4.防范建议

尽管更新的样本做了不少优化，但是对系统的持久化控制上没有太大变化，建议定期检查crontab、rc.local、init.d、systemd、profile.d、SELinux策略。

## 5.IOCs

SHA256: 66d9d837015f3f840418f5b61ce78c7fa8648e9b1b3f949c3c6a0c7d3b28ad75

app[.]r727.ru

198[.]251.82.160

# 6. 参考资料

https://urlhaus.abuse.ch

https://threatquery.com

https://www.virustotal.com

https://any.run

https://cujo.com/blog/reverse-engineering-go-binaries-with-ghidra/

https://x.com/malwaremustdie/status/1256977666084761602

https://intezer.com/blog/research/kaiji-new-chinese-linux-malware-turning-to-golang/

https://blog.lumen.com/chaos-is-a-go-based-swiss-army-kn...