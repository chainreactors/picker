---
title: Stowaway多级代理工具
url: https://mp.weixin.qq.com/s/fET7HrH9iOGJmtCXcFRUQA
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:33:37.037490
---

# Stowaway多级代理工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6409yq12RKF0mTYVx3EoXTr1jc3p2SibAxHHzdpBMCicw88UsvwbMOudg/0?wx_fmt=jpeg)

# Stowaway多级代理工具

原创

白小客
白小客

白小客

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6HusU1ygLb1jNkW3IEWzW0bjWib2pl3hP4JAXInXX3qEBvutCJc1aRrw/640?wx_fmt=png&from=appmsg)

Stowaway多级代理工具

分享一款好用的多级代理工具，不需要修改配置文件，命令也十分简单，代理支持win、linux和mac，各种架构也适配，代理管理十分简单。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6Z2ZAvgJPztugMeSmic60Se6D33vE3TLJBCEQNibyAlJ2CfcrzZVyd0Qg/640?wx_fmt=jpeg&from=appmsg)

1

简介

2

部分命令解释

3

演示环节

#1 简介

**GitHub地址**

```
https://github.com/ph4ntonn/Stowaway/
```

**Stowaway是一个利用go语言编写、专为渗透测试工作者制作的多级代理工具。**

**用户可使用此程序将外部流量通过多个节点代理至内网，突破内网访问限制，构造树状节点网络，并轻松实现管理功能。**

**（缺点：下面node的里面数字只是一个标记，没有代理层级的意思，所以这个代理有一个缺点就是没有拓扑图显示，需要自行记录拓扑。）**

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6HAlsQhKHwAuM6bianwqDmFoiaADhQ90dFSibNZ2psG4fTWHRXn8BLYtZg/640?wx_fmt=png&from=appmsg)

#2 部分命令解释

```
help 可以查看当前窗口下的命令提示back 回退窗口，用于从节点操作（node）回退到代理服务端（admin）。-l 被动模式下的监听地址，指定监听ip和端口，不指定ip默认0.0.0.0。-s 指定通信加密密钥（AES-256-GCM加密），若为空，则代表通信不被加密。-c 主动模式下的目标节点地址，指定连接的节点ip和端口，不指定ip默认0.0.0.0。
# 进入节点后的命令use id 可以对节点进行操作。socks 8888 user pass 设置socks5代理，可加账号密码认证。listen 开启节点监听，用于接收二级代理回连。--reconnect 10 重连时间间隔，此参数仅用在agent，且仅用在主动模式下。
```

#3 演示环节

**基于三个Windows主机进行演示，服务端为Linux系统。对于不同系统，命令都是一样，只是执行的程序不一样。**

**下面是拓扑图。**

```
注意，监听端口不能被防火墙拦截，所以实际攻防中，肯定要给防火墙加端口放行规则或直接关闭防火墙演示的是被动模式，也可以用主动模式，替换l为c，c换l。
Linux攻击机（监听9999端口，开启AES加密）    🡑（NAT：192.168.1.22）    |    |    |（NAT：192.168.1.26）（主动回连Linux攻击机11111端口，同样开启AES加密）一层代理主机win1    🡑（VMnet11：10.0.1.136）（node1节点开启监听端口11111，也就是win1监听11111端口）    |    |    |（VMnet11：10.0.1.135）（主动回win1的11111端口，同样开启AES加密）二层代理主机win2    🡑（VMnet12：10.0.10.100）（node2节点开启监听端口11111，也就是win2监听11111端口）    |    |    | （VMnet12：10.0.10.102）（主动回win2的11111端口，同样开启AES加密）三层代理主机win3
```

**1.先开启服务端。**

```
./linux_x64_admin -l 192.168.1.22:9999 -s 666
```

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX61S7mibB8QD6GmaiaJ5gI1FTf1JKE1bJYnqBAyVnr01A0n1drKHvJVpQA/640?wx_fmt=png&from=appmsg)

**2.一层代理（win1回连Linux攻击机）**

```
.\windows_x64_agent.exe -c 192.168.1.22:9999 -s 666
```

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6qDhmGTiaNcW5rTibl6xJgEdEQsBgr61p0SMAX5ex7Gr5IAVd57TSzhyQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX61bHMoiaq2buOlVz4x4cWvib5ootcP4eQo2nN2fM4XfW3H70ztHrOGTDw/640?wx_fmt=png&from=appmsg)

**可以使用detail命令查看代理节点情况。**

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX65rudFhc3dPequ8D77bUG6pMQGauX2FL13ajc7PchTraGnoLQpx2qUg/640?wx_fmt=png&from=appmsg)

**至于socks5代理搭建，十分简单**

```
# 进入节点use 0# socks5设置（注意：这个端口指的是vps的端口）socks 1111（注意记录这个socks5设置情况，程序没有显示的地方，所以这也是一个缺点，不过有一个记录信息功能，我觉得一般）
```

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6P0R52BeYLJNDrMRlbLotEj2pu48eU9JiaYTrZrq6cCy7qIbj1Jicv9Lg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6xecLQcF2SCqMIicRic6RSYDzFFaMleDpIibaMicS5ov3OHLDr0WibWqBHhg/640?wx_fmt=png&from=appmsg)

**3.二层代理（win2回连win1）**

**先在win1上开启监听11111**

```
# 进入节点use 0# 监听设置listen选择1 Normal passive设置监听ip和端口10.0.1.136:11111
```

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6xSDhdHrjQKAVqMBBicHvvAGxxuh8dHh1G3m9ZIkJpqrPHx4OYsdNFMg/640?wx_fmt=png&from=appmsg)

**[\*] 请注意！如果您选择 IPTables 复用或 SO 复用，\*\*必须确认您要控制的节点是通过对应方式启动的！\*\***

**[\*] 当您选择 IPTables 复用或 SO 复用时，节点将使用「启动时的初始配置」来实现端口复用！**

**[\*] 请选择模式（1.普通被动模式 / 2.IPTables 复用模式 / 3.SO 复用模式）：**

**1: Normal passive：普通被动模式，使用独立的自定义端口通信，无复用需求。**

**2: IPTables Reuse：基于 Linux 系统 IPTables 防火墙规则的端口复用技术，仅适用于 Linux。**

**3: SOReuse：基于TCP/IP套接字选项（SO\_REUSEADDR/SO\_REUSEPORT）的跨平台端口复用技术，支持 Windows/Linux。**

**win2回连win1**

```
.\windows_x64_agent.exe -c 10.0.1.136:11111 -s 666
```

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6kRDajMenjOsL0IibNvgf13CY3bmo05fKefDEX4iaG0C2EdgfDQ4Sia8fQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6DpPXH67CCA60VPfkMgudia67TpE0CuXveiava0Ah1bRhVfPgMWGm3gYw/640?wx_fmt=png&from=appmsg)

**回车即可，这样二层代理就搭建好了**

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6mQgfmvThic0tXaibCPjyS1eD8kRg8bTMhomx8kNIk5vicMOnoUD1oIiaMg/640?wx_fmt=png&from=appmsg)

**4.三层代理（win3回连win2）**

**先在win2上开启监听11111**

```
# 进入节点use 1# 监听设置listen选择1 Normal passive设置监听ip和端口10.0.10.100:11111
```

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6nLg9d1FMSXGmKfKrcAHndorcP1QekibxBzpVvkIL9FUskVGIH8zMdXQ/640?wx_fmt=png&from=appmsg)

**win3回连win2**

```
.\windows_x64_agent.exe -c 10.0.10.100:11111 -s 666
```

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX60TbxTSVkiaVP2gBGHtJceZVJVNGyWp2NX1dj885eFwNic9Mm22h0J1XQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6oDMzU1l8q1JaWQrY1ViaorTm8ea6wUE7q4baG5vibvM4T1U8MAOFyYcg/640?wx_fmt=png&from=appmsg)

**回车即可，这样三层代理就搭建好了**

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6g69OlX98DX1viaK5pKbPpu3OkdicxsObGlILu2e80ZiboicaTYAl7aibxqw/640?wx_fmt=png&from=appmsg)

**还可以通过shell命令获取终端，不过觉得没什么用，实际攻防也不大用的到。**

**如果遇到乱码，shell后执行chcp 65001，将当前终端的字符编码页切换为UTF-8编码，Windows系统是GBK编码。**

**当然了，这只是展示了三层win主机代理搭建，实际攻防肯定有Linux，不过命令都一样，换个程序罢了。**

**再附上一张图，盖程序不会报毒。**

![](https://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8d1dFqN6Phj1iaoXELBkbTX6QDQrUQuFxiaGUGXIvpyPKNia5J75hGPg65AhTg8ReFoLnwIKAicDSI0tw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8f9ok6SMKpw7wGXDv2h6Frj3Q0fJHfFRmLcuuYrWv6bKyev4G8iafEicO0JCzNQWCTJpcRbCpEvxiaXg/0?wx_fmt=png)

白小客

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5iaiaDSymCt8f9ok6SMKpw7wGXDv2h6Frj3Q0fJHfFRmLcuuYrWv6bKyev4G8iafEicO0JCzNQWCTJpcRbCpEvxiaXg/0?wx_fmt=png)

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