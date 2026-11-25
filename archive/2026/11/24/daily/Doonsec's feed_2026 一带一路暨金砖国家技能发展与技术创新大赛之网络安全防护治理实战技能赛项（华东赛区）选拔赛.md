---
title: 2026 一带一路暨金砖国家技能发展与技术创新大赛之网络安全防护治理实战技能赛项（华东赛区）选拔赛
url: https://mp.weixin.qq.com/s/8GhqbbcnimIalkdFci1BnQ
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:39:15.328745
---

# 2026 一带一路暨金砖国家技能发展与技术创新大赛之网络安全防护治理实战技能赛项（华东赛区）选拔赛

# 2026 一带一路暨金砖国家技能发展与技术创新大赛之网络安全防护治理实战技能赛项（华东赛区）选拔赛

原创

正在思考ing
正在思考ing

正在思考ing

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

第一次打这种类型的比赛，而且当时还在打数证杯，因此我们在比赛开始的前半个小时都是在平台上盲目乱点，第一道签到题 flag 就在眼前都愣了好久才提交，半个小时后才进入状态开始做题

最大的感受就是找到答案还要算一遍 md5 再提交，都是静态 flag 不懂意义何在。其次就是主办方提供的 windows 主机卡得不行，而且 flag 输出在终端中的时候根本看不清，比赛还没结束眼睛先瞎了

第一部分网络安全设备就是在各种配置 jumpserver，最后一道题我们队怎么 check 也不通过，赛后看了队友的录屏才发现是把命令过滤规则名称里的 `-` 写成了 `_`，可惜了

第二部分资产梳理感觉就是在做 ctf，第 4 题要子域名枚举，没什么时间就没有往下做了

第三部分流量分析，主办方的 windows 主机中提供的 wireshark 追踪 tcp 流都要等半天，做了第一题就没往下做了

第四部分安全加固比较简单，就是在写各种配置文件

第五部分应急响应主要是对一台感染了挖矿木马的主机进行安全审计，最后一题清除邮件痕迹没啥思路

第六部分日志分析主要是第一题要写脚本统计数据，后面题目题干给的提示挺足的，ctrl + f 搜索一下就能找到

最后一部分渗透测试，本来是我们的拿手项目，结果意外爆零了，主要是第一道题问得太模糊了，前前后后找到好几个敏感数据提交都不对

部分题目是看着队友录屏复现的，思路可能有点问题大家轻点打我

有没有哪位师傅渗透有思路的，能不能来教教我们

感觉最近好倒霉啊，干啥都不顺心，可以用下面的 wp 跟大家换一些好运吗

(っ╥﹏╥)っ

## 网络拓扑

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rm4ibHwicPzkYQebdzMl7Bl8IWjAJ5MSzLmJe7LTT1NSuic7zqSLB1eaJPWj815Bm55PHnicPTz9aicm8J4ffdEMQb67NqotiaicLW7Os/640?wx_fmt=webp&from=appmsg)

## 主要设备

---

| 名称 | IP地址 | 系统版本 | 访问方式 | 用户名 | 口令 |
| --- | --- | --- | --- | --- | --- |
| 堡垒机后台 | http://172.16.120.146:18100/web/ | linux | http | admin | Neteq011#Jms |
| 渗透win主机 | 192.168.20.6 | windows | vnc | I | 123456 |
| 渗透win主机 | 192.168.20.189 | windows | vnc | I | 123456 |
| 渗透win主机 | 192.168.20.100 | windows | vnc | I | 123456 |
| 安全加固服务器 | 192.168.20.38 | ubuntu | vnc/xshell | admins | 1qazcde3!@# |
| 应急响应服务器 | 192.168.20.210 | centos | vnc/xshell | root | root |
| 资产梳理服务器 | 172.16.120.198 | linux | 不提供登录 | —— | —— |
| 渗透测试目标服务器 | 172.16.120.158 | linux | 不提供登录 | —— | —— |

**如果XShell注册码过期，请输入：101210-450789-147200**可使用第三方工具CyberChef、蓝队工具箱等来获取md5密文

## 一、网络安全设备

---

作为企业的网络管理人员，你需要对公司的网络安全设备的策略了若指掌，以协助安全团队对企业的业务进行全面的安全加固。

本套为运维安全专题，全部题目在一台 JumpServer 堡垒机上完成。 初始资产三台：prod-app-01（172.20.10.11）、prod-db-01（172.20.10.21）、test-app-01（172.20.10.101）； 运维人员四个：ops\_zhang（运维组）、dba\_li（DBA组）、dev\_wang（开发组）、audit\_chen（审计员）。

| 名称 | IP地址 | 系统版本 | 访问方式 | 用户名 | 口令 |
| --- | --- | --- | --- | --- | --- |
| 堡垒机后台 | http://172.16.120.146:18100/web/ | linux | http | admin | Neteq011#Jms |

### 1、登录日志研判

安全运营中心在例行巡检时发现，堡垒机的 Web 登录口在前几天遭到过一次 口令爆破。请你从审计日志里把这次爆破定位出来。

任务：在「 系统审计 → 登录日志」中，找出同时满足下面三个条件的 那一组「来源 IP : 被攻击账号」：

* 来源 IP 属于**外部地址**（内网地址段 10.0.0.0/8、172.16.0.0/12、192.168.0.0/16 一律排除）；
* 针对该账号的 失败登录次数 ≥ 6 次；
* 针对该账号 从未出现过成功登录。

提交格式：flag{md5([来源IP:被攻击账号])}（方括号是拼接格式的一部分，IP 与账号之间用 英文冒号分隔，全小写十六进制），例如假设来源IP为198.51.100.1，账号为admin，则拼接为[198.51.100.1:admin]，将其进行md5加密，最终提交flag{70b6d44d6960fdfa61fe492f7cea4aac}

flag{32f8a2dec18cdd1547f000ad1be5de09}

直接看审计台-登录日志页面

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rk1ibtjZKnGYaxvicoMAqu1y8aViabUmFs1XsPYBo7iaAf67hYLOdZyFvBmXLMN1qlgNCicP9pYlI0zAibiafb7XbrPjZm4MLd3I2icWPU/640?wx_fmt=webp&from=appmsg)

发现 ip 为 `203.0.113.45`，用户为 `ops_zhang` 存在多条登录失败记录（根据题干另一个 `10.20.30.15` 的登录记录属于内网 ip，需要排除）

按理说还要进一步筛选确认这条记录有没有登录成功过，但比赛的时候提交直接通过了，就没有进一步去分析

因此本题 flag 为 flag{md5([203.0.113.45:ops\_zhang])}

### 2、命令记录溯源

昨天下午生产库 prod-db-01 上的 orders 表被整表删除，业务中断了 40 分钟。DBA 说不是他干的，开发说只跑过查询。请你从堡垒机的 命令记录里把这次操作定位出来。

任务：在「 会话审计 → 命令记录」中，找出 唯一一条对 prod-db-01 执行了DROP TABLE orders 的记录，提交它的「 操作用户 : 资产名称」。

提交格式：flag{md5([操作用户:资产名称])}

flag{e24d56f59cc37f64670fbca214b8d7f3}

直接来看审计台-会话命令页面

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rmqxt3VNg3aRjYO5cukYQZnOa9Aw6qmKUQxjGRaj9mDDJzgicAfFjicnwBQvwT4t104kXKPYIX2QC3nDTJl7geebmxgqUshFrvkE/640?wx_fmt=webp&from=appmsg)

发现命令 `drop table orders` 的操作用户为 `dba_li`，资产名称为 `prod-db-01`

因此本题 flag 为 flag{md5([dba\_li:prod-db-01])}

### 3、资产纳管与节点编排

公司新上线了一台消息队列服务器，需要纳入堡垒机统一管理，并按机房规范放到「生产环境」下的「中间件」分组里。

任务：在管理台完成两件事（ 节点要先建，资产才能归位）：

1. 在「 资产管理 → 节点」中，于 生产环境 之下新建子节点 中间件；
2. 在「 资产管理 → 资产列表」中新增一台主机资产，字段严格如下：

| 字段 | 要求 |
| --- | --- |
| 名称 | prod-mq-01 |
| 地址 | 172.20.10.31 |
| 平台 | Linux |
| 协议 | SSH，端口 22 |
| 节点 | 中间件 |
| 激活 | 是 |

配置完毕后，在cmd或powershell中执行渗透win主机桌面网络安全设备校验/check.exe --host 172.16.120.146 --asset。若配置正确，程序末行会输出一个 flag 信息，将 flag 提交。

flag{Ab3Nv7Kd2Qx}

根据题意，首先在资产列表的 `生产环境` 下新建子节点 `中间件`

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rnPFPlusQHHf18su79Q7e5FKFy9LbpX9ElAXzrzwW4sHJrDeXyZicdnwIJAv5YJ1ricry8tiaKJBAn1hL7y114gKEsiaImxG5cSWiaQ/640?wx_fmt=webp&from=appmsg)

随后按照要求创建一个新的资产

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rkJPFTNn29PnTyQcCMg9EmUdYu3P0B9f21Ziaj3k9RKlxuN5XN0PYUf19gYcanklgtn7MKf5csda262QYp47edcZBicSWXTAKibus/640?wx_fmt=webp&from=appmsg)

`节点` 字段要选择刚刚创建的 `中间件`

配置完成后 check 即可拿到 flag

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rn2oJvRrBCqG6TtRDEujpCG68sDmoKibUvQVNZO7gwGlML1pNPVRWGJk9DQZjMQBhQTlBEZsyyBQDEXCVmABOu0QiaUk8jDHhnnw/640?wx_fmt=webp&from=appmsg)

### 4、账号分级托管

生产库要接入新的运维流程，需要把两个数据库账号纳入堡垒机托管，并按权限级别分开管理：变更用的高权限账号、只读查询用的普通账号。

任务：为资产 prod-db-01 新增 两个账号：

| 用户名 | 是否特权账号 | 说明 |
| --- | --- | --- |
| dbadmin | 是 | 用于变更操作，需要高权限 |
| dbreadonly | 否 | 用于只读查询 |

密码类型选「密码」，密码按企业规范自行设置（ 不参与判分）； 两个账号都要 启用。

配置完毕后，在cmd或powershell中执行渗透win主机桌面网络安全设备校验/check.exe --host 172.16.120.146 --account。若配置正确，程序末行会输出一个 flag 信息，将 flag 提交。

flag{Db5Wq9Hf4Lz}

资产列表 - 选择资产 prod-db-01 - 新建账号

按照要求新建上述两个账号即可，密码自行设置即可

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rnuFa2kDhOr1Dp30M6laiaKmPsw1eofiaxjnIw2PGUb2UcfibaJu9RgFRay6WRs36ibegSyUDNnhRM3n5336F0H5AzjbG4XF8mAavk/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rlazrpEcaJbjuodHytMJia4bIjZROuhAwPqHKgFiclBuhskhEkbNjsaJiaN08ovGJRCoIo1PiajA80MaSdRm8R9ib2iasITs9dzm6F3g/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rnFEmG5k8rDS3uBibn8ntT78SFW8N14bRJDp0SCprgVRSdk03PUiblicCBqwkhZf4vlm1g83rvb1I7YOxXSF8qu2Ck2ibemPzZgNiaQ/640?wx_fmt=webp&from=appmsg)

创建后 check 即可拿到 flag

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rnaJAgHsDw3ETByRlPgJLA6ql7myALhpfOxDX0JtLAiaCrmficUgQDbmTVseYTicL2UaMhNqDQo4117URxdwGbhkUeterJdRP2SCc/640?wx_fmt=webp&from=appmsg)

### 5、最小权限授权

审计发现堡垒机现在的授权是”一把梭”—— 有一条 ALL-ACCESS 规则把 所有用户组、所有资产、所有账号、全部动作都放开了。这明显不符合最小权限原则。

任务：

（一）新建一条收窄的授权规则

| 字段 | 要求 |
| --- | --- |
| 名称 | OPS-DB-READONLY |
| 用户 | 无 |
| 用户组 | 只选 DBA 组 |
| 资产 | 不直接选资产，改为只选择节点数据库 |
| 账号 | 所有账号 |
| 动作 | 只勾「连接」（上传/下载/剪贴板/分享都 不要勾） |
| 激活中 | 是 |

（二）停用过宽的旧规则

把 ALL-ACCESS 规则 停用（不是删除）。

配置完毕后，在cmd或powershell中执行渗透win主机桌面网络安全设备校验/check.exe --host 172.16.120.146 --permission。若配置正确，程序末行会输出一个 flag 信息，将 flag 提交。

flag{Pm8Ry2Gt6Xw}

首先按照要求创建资产授权

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rmpdU0IePpry8vA3H10fPwp0sXYbWLqUyu3icpzEibic4SicIUpzew6icbNlibRKEJcvV7v1EwzryDVUp2mS5OkXbzibnSczibPbTO1icg8/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rkReNKruk2L3Bq09LQdynx4rC7fr6mHAbOacZponGSpCLib7bykKhbEQS8rfbHNzbOlIuVIsYge6DSmEtqqAWpRHftydy4FDxsg/640?wx_fmt=webp&from=appmsg)

再把原有的 ALL-ACCESS 规则取消激活

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rnbGEseS33SPfhtdYqTKLwVlpl1Yiak5pMuwSFiaYJsr0GxT5yFh3Yebrn2OB1dBdfHGENwy8EFJD3BzfTJFwa2mNcE8t0h47EgM/640?wx_fmt=webp&from=appmsg)

配置完成后 check 即可拿到 flag

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rnmMoV8uavoSZRWPQKxB6r84BzwX5e5plp8MkDTMTRQSr82enWT6u9iaVjbQEz7iapGE9gCTRsO5P6Gyibib0maYicNXfibicytZdicP68/640?wx_fmt=webp&from=appmsg)

### 6、高危命令过滤

描述：上周的误删事件之后，安全部要求给生产库加一道”命令闸门”：把几条 不可逆的高危命令拦在会话里，不允许真正执行。

任务：

（一）新建命令组

| 字段 | 要求 |
| --- | --- |
| 名称 | DANGEROUS-CMD |
| 类型 | 正则表达式 |
| 内容 | 四行，每行一条：rm -rf / mkfs / dd if= / shutdown |
| 忽略大小写 | 勾选 |

（二）新建命令过滤规则

| 字段 | 要求 |
| --- | --- |
| 名称 | BLOCK-DANGEROUS |
| 命令组 | DANGEROUS-CMD（只绑这一个） |
| 用户 | 所有用户 |
| 资产 | 只指定 prod-db-01（ 不要选“全部资产”） |
| 账号 | 所有账号 |
| 动作 | 拒绝 |
| 优先级 | 10 |
| 激活中 | 是 |

配置完毕后，在cmd或powershell中执行渗透win主机桌面网络安全设备校验/check.exe --host 172.16.120.146 --filter。若配置正确，程序末行会输出一个 flag 信息，将 flag 提交。

flag{Cm4Jk9Zd3Vb}

新建命令组：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rmO2PAKmJBzyzCk3sko5tf2pddOYcmefhJmRMbibNdpeNa1nzKAicslDsRQulIPgcVQnr9qa24LZa6uoRz1wzDaTjDJIyA3vwNiag/640?wx_fmt=webp&from=appmsg)

新建命令过滤规则：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rlib9XU5jiah4rH5aGo1iakicVBXjKaC0XLhicmYeVCqBG38UFfOsa8sbFf99LfLUsqic05RLU90ibnLhnbtEfNa5HibhYkJAf5BUgO7QE/640?wx_fmt=webp&from=appmsg)

下面 `其他设置` 要勾选 `激活中`，选...