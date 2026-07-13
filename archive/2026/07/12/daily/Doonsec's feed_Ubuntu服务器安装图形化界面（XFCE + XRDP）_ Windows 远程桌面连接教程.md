---
title: Ubuntu服务器安装图形化界面（XFCE + XRDP）| Windows 远程桌面连接教程
url: https://mp.weixin.qq.com/s/Z-xHS9n6bG5LUCjJVDIWnA
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:26:31.429249
---

# Ubuntu服务器安装图形化界面（XFCE + XRDP）| Windows 远程桌面连接教程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LtibzcRx8GjXicXGtfibQKcyezeCRkwffBtM2lv9GsaCEFL4LSrtBJMAjUKurcKxJsyPhojBWFTQQk7Wt0icz5Xnc0QQoIZK3IiaNLicvDXFpoRwo/0?wx_fmt=jpeg)

# Ubuntu服务器安装图形化界面（XFCE + XRDP）| Windows 远程桌面连接教程

原创

W不懂安全
W不懂安全

W不懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

很多朋友买完 Ubuntu 云服务器之后，面对的都是一片黑漆漆的命令行。对于习惯图形界面的用户来说，第一次接触 Linux 服务器确实会有些不适应。

其实，Ubuntu 服务器**完全可以安装桌面环境**，并通过远程桌面来管理。

今天这篇文章，就带你在一台 Ubuntu 服务器上，部署一套**轻量、省资源**的桌面方案：

* 🖥️ 桌面环境：**XFCE**（轻量高效）
* 🌐 远程服务：**XRDP**（支持 Windows 远程桌面协议）

部署完成后，你**直接用 Windows 自带的远程桌面连接**就能登上去，像操作本地电脑一样操作你的云服务器。

---

## 这套方案好在哪？

和常见方案对比一下，优势一目了然：

✅ **资源占用极低**
哪怕只有 1 核 1G 的入门云服务器，也能完成部署和基本使用。

✅ **远程体验更好**
使用 Windows 自带的远程桌面协议（RDP），无需额外安装客户端，画面更流畅，延迟更低。

✅ **更适合长期运行**
相比 GNOME 等重量级桌面，XFCE 对 CPU 和内存的占用少得多，跑在服务器上几乎没负担。

✅ **比 VNC 更方便**
省去 VNC 客户端配置步骤，一条 RDP 直连，效率拉满。

---

## 准备工作

在开始之前，请先登录你的 Ubuntu 服务器（我这里以 **Ubuntu 22.04** 为例），并确保你拥有 `root` 或 `sudo` 权限。

---

## 第一步：更新系统软件包

先把软件包列表更新一下，顺便把系统里现有的软件升到最新。

```
sudo apt update && sudo apt upgrade -y
```

这一步根据服务器网络和更新数量，可能要跑一两分钟，耐心等待即可。

---

## 第二步：安装 XFCE 桌面

接下来安装 XFCE 桌面本体，以及配套的实用工具和插件：

```
sudo apt install xfce4 xfce4-goodies -y
```

> ⚠️ 安装中途可能会弹出一个配置界面，让你选择默认的 **显示管理器（Display Manager）**。
> 如果出现 “Default display manager” 选项，用键盘方向键选择 **lightdm**，然后回车确认。
> lightdm 负责图形化登录界面，和 XFCE 配合最好。
> 没弹窗的话就忽略，等待安装完成即可。

---

## 第三步：安装并启用 XRDP

桌面装好了，现在需要一个远程桌面服务，让 Windows 可以连上来。这里我们使用最经典、最稳定的 **XRDP**。

安装 XRDP：

```
sudo apt install xrdp -y
```

启动 XRDP 服务，并设置开机自启：

```
sudo systemctl enable xrdpsudo systemctl start xrdp
```

检查一下服务状态：

```
systemctl status xrdp
```

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVrn3ZZl3WfI9InicPuC7SJ0FbPia7xKE7WiaxRdhzycTIicEOqb7OJYkUuxKy2xbn9nXxr5YtZG99sZTvT9pzNrPawo95jFOfXpP4/640?wx_fmt=png&from=appmsg)

如果看到绿色的 **active (running)** 字样，说明 XRDP 已经正常运行。
如果显示失败，可以检查 3389 端口是否被占用，或重启一次服务试试

---

## 第四步：配置默认桌面会话

现在我们要告诉 XRDP：用户远程登入时，自动启动 **XFCE 桌面**，而不是其他环境。

```
echo xfce4-session > ~/.xsession
```

这条命令会把 `xfce4-session` 写入当前用户目录下的 `.xsession` 文件，指定默认会话为 XFCE。

为了让配置生效，重启一下 XRDP：

```
sudo systemctl restart xrdp
```

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjUOmY1QLphgUVI5IzzTUBDomAa1aZPxDMWU5hqkbaVVI873Hu1ogEZPicLK1losrGnt6EdBdsSJwzLMVlGW4BAgLCWvJgh8Sbwk/640?wx_fmt=png&from=appmsg)

---

## 第五步：远程连接，大功告成

现在回到你的 Windows 电脑上，按下 `Win + R`，输入 `mstsc` 打开 **远程桌面连接**。

📌 在“计算机”一栏填写：

```
你的服务器IP地址:3389
```

例如：`192.168.1.100:3389`

`用户名就填写默认连接服务器的用户名称`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjU7YKfFm97iaoI0ZbhLpDbcOYLfaaTMCjq2pgJJiaxMcpC8VicQ4WIMNSOKp9bArKiasKke2guvSJLiatgRwFxcN5d8pS6uAZBhHdKk/640?wx_fmt=png&from=appmsg)

然后点击“连接”。

---

如果一切顺利，你会看到一个 **XRDP 登录窗口**，这就是成功的标志。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjUBsg14FQX4YefGaDXtybV30XTpAVP0q3mb4bJnwNuribLXZIpKWH0lnyxlQ1cpCPBic1Kv7I8uAoqPrDf1444R1nPQsicKwqrXfQ/640?wx_fmt=png&from=appmsg)

在登录界面上：

* **Session**

  保持默认的 `Xorg` 即可，无需修改
* 输入你 Ubuntu 服务器的 **用户名** 和 **密码**

点击 **OK**，稍等片刻，你就能看到清爽流畅的 **XFCE 桌面**了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjURxghFvujsJbkLRLjpQt3KMMo88GKAJI1FZBPkUC7BjO7u1WYXjX4nsGYWDfTia8x6dnfA18icZicwI3ffDyKWq4hc2ia4yFvNKIU/640?wx_fmt=png&from=appmsg)

从现在开始，这台 Ubuntu 服务器就可以像本地电脑一样操作——打开文件管理器、使用浏览器、安装软件……完全图形化，没有任何门槛。

---

## 最后

这套「**XFCE + XRDP**」方案，尤其适合这几类场景：

☁️ 轻量内网服务器或开发机
☁️ 偶尔需要图形界面的远程办公
☁️ 入门学习 Linux，但又不想纯敲命令
☁️ 1 核 1G 云服务器的“图形化”改造

资源占用小、连接方便、体验流畅，几乎是为云服务器量身定做的轻桌面方案。

如果你也在折腾服务器，不妨照着试一下。

预览时标签不可点

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