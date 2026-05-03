---
title: Homelable：看着挺麻烦
url: https://mp.weixin.qq.com/s/G-iQ51msGJAV7es1NN51uw
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:24:34.528522
---

# Homelable：看着挺麻烦

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdUO9Fm6K79SZXhtt2a07jcXcMtF38z58eS28l0xvnVHqBibJn8TJ9Bczw3JYGH6WkJzS1cYArvG5YNVUV5FS9ia6csSO7bmpUCU/0?wx_fmt=jpeg)

# Homelable：看着挺麻烦

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 03 安装与使用

部署方式多样，从最简单的Docker到手动编译都有。

docker compose up -d

如果你是Proxmox用户，官方还提供了LXC模板，可以直接导入使用。对于喜欢折腾的开发者，也可以从源代码构建。

细节都写在项目里的INSTALLATION.md文件里了，照着步骤来就行，没啥坑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeCI6QzBWLKkPF2vyBQRKx7XE9wCQo3sIe4LHhjtLaC5GpYEqYVj3kb8NbymnF4tY6wWucwqOOGjl5oQNs55RlnFnMv3ibb5Tx4/640?wx_fmt=png&from=appmsg)

### 网络扫描器：一键发现

手动添加设备太累了。Homelable内置了一个基于Nmap的网络扫描器，这才是它的重头戏。

你只需要在Web界面的侧边栏点击“扫描网络”，它就会根据你配置的CIDR地址段（比如192.168.1.0/24）去探活。

扫描用这条命令：

nmap -sV --open

扫描结果不会直接乱糟糟地堆到画布上，而是先进入一个“待处理设备”队列。你可以在侧边栏里逐一审核、批准添加、隐藏或忽略。这个设计很贴心，避免了误加一堆打印机或手机。

**注意权限问题**：在macOS上，或者某些需要SYN扫描、操作系统检测的场景，Nmap需要root权限。如果前端扫描报权限错误，你需要手动运行脚本：

cd backend
sudo python ../scripts/run\_scan.py 192.168.1.0/24

# 扫多个网段也行
sudo python ../scripts/run\_scan.py 192.168.1.0/24 10.0.0.0/24

扫描结果会直接写入数据库，UI上会实时刷新。

在Linux上有个更优雅的方案，不用整个后台都以root运行，只需给Nmap二进制文件赋予`NET_RAW`能力：

sudo setcap cap\_net\_raw+ep $(which nmap)

### 节点检查：不止是Ping

设备图标摆上去不难，难的是实时知道它是不是还活着。Homelable的监控检查系统（虽然官方标注还在WIP，开发中）做得不错。

它能持续监控节点，并在画布上直接显示实时的状态（在线/离线/未知）。最关键的是，**每个节点都能配置独立的检查方法**，而不是一刀切地用Ping。

方法还挺全：

* **ping**

  ：最基础的ICMP Ping。
* **tcp**

  ：尝试建立TCP连接，端口通了就算在线。
* **http**

  ：发送HTTP GET请求，状态码是2xx或3xx才算成功。
* **https**

  ：同上，但走HTTPS。
* **api**

  ：调用自定义的/health API端点，根据返回的JSON判断。

这样一来，你的Web服务器可以用http检查，数据库用tcp检查5400端口，而自研的微服务则可以用自定义的/health API，非常灵活。

## 04 与Claude AI深度集成

如果说上面的功能是基础配置，那和Claude AI的集成就算是个“魔法”功能了。Homelable提供了一个MCP（Model Context Protocol）服务器。

简单说，你能用**自然语言直接管理你的整个家庭实验室**。

先在Homelable后台启用MCP服务器，它会运行在8001端口，并生成一个API密钥。

# 在.env文件里设置
MCP\_API\_KEY=mcp\_sk\_yourkey

# 启用MCP服务
docker compose --profile mcp up -d

然后配置你的Claude客户端（Claude Code或Claude Desktop），把Homelable添加为一个工具。

配置好之后，你就可以直接对Claude说：

* “现在有哪些节点离线了？”
* “在192.168.1.5添加一个名叫pihole的LXC容器，连到我的交换机上。”
* “扫描192.168.1.0/24网段，把发现的待处理设备给我看看。”
* “给我看看完整的拓扑图。”

Claude会通过MCP协议调用Homelable的接口，帮你执行操作并返回结果。这个玩法把运维的门槛又拉低了一大截。

> 安全提醒：MCP服务器（8001端口）**千万别暴露到公网**，就限定在你的局域网内访问。记得定期轮换API密钥。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcMCc1R4yP9eZdVciazRF6P0JQJK2Hxkgn97tZhtvGEC7ErAs1kftIiamIzRwL9kHQkbicstsH24v7SAoNgJJ614deobq4bNj9trs/640?wx_fmt=png&from=appmsg)

## 05 优缺点与总结

用了段时间，说说真实感受。

**优点很明显：**

* **颜值即正义**

  ：界面确实好看，自定义空间大，导出图片清晰。
* **发现能力强**

  ：内置Nmap扫描器是神器，能自动识别服务，省去大量手工录入。
* **监控实用**

  ：多种健康检查方式，能真实反映服务状态，不是简单的Ping。
* **AI集成是亮点**

  ：MCP协议接入Claude，提供了未来感的交互方式。
* **部署简单**

  ：Docker一把梭，对新手友好。

**缺点和不足：**

* **功能仍在演进**

  ：健康检查等功能官方明确标注WIP，可能还不稳定。
* **资源消耗**

  ：作为常驻服务，会占用一定内存和CPU，树莓派老用户得掂量下。
* **深度定制复杂**

  ：界面好看，但如果你想 deeply 修改布局逻辑，可能需要动代码。

**适合谁用？**

如果你家里跑着超过5台设备（软路由、NAS、服务器、智能家居中枢），各种IP地址、端口号开始记不清，那么Homelable能立刻帮你理清头绪。

它特别适合：

* 家庭实验室/自建服务爱好者
* 喜欢用视觉化方式管理网络的人
* 想尝试AI+运维新型玩法的极客

最后给个推荐指数：**四星半**。扣掉的半星是因为部分功能还在开发中。但就凭它现在这个颜值和自动发现能力，已经值得你花半小时部署一个试试看了。至少，下次再排查网络问题，你有一张漂亮的拓扑图可以看了。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibdu7Osehg7XLJMTiaKun1HlseQCYgKzMxtnVh47CEuTfkS2OkiaXRaqH3kHNGJJP5DAMzr27rVYAmwF9eVDia2NDPRX334dSxDPoE/640?wx_fmt=png&from=appmsg)

**获取方式：私信回复"homelable"获取**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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