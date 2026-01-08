---
title: 一台服务器搭建矩阵代理池，一个端口绑定一个住宅IP，实现矩阵式代理
url: https://mp.weixin.qq.com/s/VeTFryH7rkvlUKnENlCzkA
source: Doonsec's feed
date: 2026-01-07
fetch_date: 2026-01-08T03:27:20.880253
---

# 一台服务器搭建矩阵代理池，一个端口绑定一个住宅IP，实现矩阵式代理

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y4PrZUSw1T9T8ObYzibZibhXqWFTwFvYzF6xibtwrBL75OGibTS9ibEfMjJ4dFH803ycGAC5O4hec3wgVcVDO6ux2ow/0?wx_fmt=jpeg)

# 一台服务器搭建矩阵代理池，一个端口绑定一个住宅IP，实现矩阵式代理

原创

W不懂安全

W不懂安全

![]()

在小说阅读器中沉浸阅读

本期目标：

* VPS服务器作为中转服务器
* 每个本地端口对应一个住宅IP（Socks5协议）
* 出站流量通过对应的端口转发至对应的住宅IP
* 能实现多端口、多住宅IP的矩阵式代理

为什么选择sing-box，而不是gost/redsocks等。

|  |  |  |
| --- | --- | --- |
| 对比项 | gost | sing-box |
| 多端口矩阵 | ✔ | ✔✔✔ |
| 指纹浏览器支持 | ✔ | ✔✔✔ |
| 内部加密 | ❌ | ✔ |
| 单端口单出口隔离 | ⚠️ | ✔✔✔ |
| 崩溃自动恢复 | ❌ | ✔ |
| 配置文件化 | ⚠️ | ✔✔✔ |
| 风控风险 | 中 | 低 |

**sing-box 是现在很多代理商「住宅 IP 中转」的实际用法。**

**🏗️ 架构图**

```
指纹浏览器   ↓ SOCKS5（无 TLS，完全兼容）VPS :10001  ──▶ 住宅IP #1VPS :10002  ──▶ 住宅IP #2VPS :10003  ──▶ 住宅IP #3...
```

* **每个端口固定一个住宅 IP**
* **出问题只影响一个端口**
* **无 TLS 坑**
* **无 iptables**
* 无 bash 拼命令

一次性服务端搭建👇

安装sing-box：

```
curl -fsSL https://sing-box.app/install.sh | bash
```

安装完成之后验证一下是否安装成功：

```
sing-box version
```

当出现版本号，则证明安装成功。

接着创建配置文件：

```
mkdir -p /etc/sing-boxnano /etc/sing-box/config.json
```

将以下内容粘贴到配置文件中，我写的配置文件示例三个住宅IP，可以在这个基础上无限扩展增加：

```
{  "log": {    "level": "info"  },
  "inbounds": [    {      "type": "socks",      "tag": "in_1",      "listen": "0.0.0.0",      "listen_port": 10001,      "users": [        { "username": "u1", "password": "p1" }      ]    },    {      "type": "socks",      "tag": "in_2",      "listen": "0.0.0.0",      "listen_port": 10002,      "users": [        { "username": "u2", "password": "p2" }      ]    },    {      "type": "socks",      "tag": "in_3",      "listen": "0.0.0.0",      "listen_port": 10003,      "users": [        { "username": "u3", "password": "p3" }      ]    }  ],
  "outbounds": [    {      "type": "socks",      "tag": "out_1",      "server": "住宅IP_1",      "server_port": 1080,      "username": "res_user_1",      "password": "res_pass_1"    },    {      "type": "socks",      "tag": "out_2",      "server": "住宅IP_2",      "server_port": 1080,      "username": "res_user_2",      "password": "res_pass_2"    },    {      "type": "socks",      "tag": "out_3",      "server": "住宅IP_3",      "server_port": 1080,      "username": "res_user_3",      "password": "res_pass_3"    }  ],
  "route": {    "rules": [      { "inbound": "in_1", "outbound": "out_1" },      { "inbound": "in_2", "outbound": "out_2" },      { "inbound": "in_3", "outbound": "out_3" }    ]  }}
```

如果你要无限扩展，你只需：

1️⃣复制一个 inbound：

```
{  "type": "socks",  "tag": "in_4",  "listen": "0.0.0.0",  "listen_port": 10004,  "users": [    { "username": "u4", "password": "p4" }  ]}
```

2️⃣ 复制一个 outbound

```
{  "type": "socks",  "tag": "out_4",  "server": "住宅IP_4",  "server_port": 1080,  "username": "res_user_4",  "password": "res_pass_4"}
```

3️⃣ 加一条 route

```
{ "inbound": "in_4", "outbound": "out_4" }
```

规则永远是：

```
in_N  →  out_N10000 + N  →  住宅IP_N
```

启动sing-box

```
sing-box check -c /etc/sing-box/config.jsonsystemctl restart sing-box
```

查看sing-box状态：

```
systemctl status sing-box
```

当Active处显示绿色文字：active (running)，则表示配置没有问题，且已经成功启动。

测试：

```
curl --socks5 u1:p1@127.0.0.1:10001 ifconfig.mecurl --socks5 u2:p2@127.0.0.1:10002 ifconfig.me
```

每一个测试命令的端口，测试出来的要是对应的住宅IP。

字段解释：

|  |  |
| --- | --- |
| 字段 | 含义 |
| server | 住宅IP地址 |
| server\_prot | 住宅代理端口 |
| username | 住宅代理账号 |
| password | 住宅代理密码 |
| 例：u1 | 是后期你要用指纹浏览器等工具连接时，所要输入的用户名 |
| 例：p1 | 是后期你要用指纹浏览器等工具连接时，所要输入的密码 |
| listen\_prot | 要给住宅IP分配的端口号，后期要用工具连接时要输入这个端口 |

到这里搭建就结束了。

指纹浏览器的配置：

```
代理类型：SOCKS5地址：VPS_IP端口：10001 #根据实际情况修改用户名：u1 #根据实际情况修改密码：p1 #根据实际情况修改
```

* 不需要TLS
* 不需要证书
* 不需要SSH
* 所有指纹浏览器都支持

安全性为什么"足够且不翻车"？

* SS5用户名密码
* 单端口单隔离
* systemd自动恢复
* 无复杂的NAT/iptables
* 无明文TLS误配置风险
* 不容易被滥用

这是“商业代理池中转”的标准做法。

你用指纹浏览器最终实现的效果是：

* 代理信息写的都是服务器的ip和端口，但是检测出来的是住宅IP的IP
* 使用不同的端口，测出来的是不同的住宅IP
* 每个IP都是单独的，不会相互关联。

本期内容到此结束。

三连加关注，追文不迷路。![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_02.png)

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9T8ObYzibZibhXqWFTwFvYzFKPIQL2bRr6Pu9zLLqNvF4zr8zusIITLOkNhhe81yOWkF3SQy5h1mqw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

W不懂安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

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