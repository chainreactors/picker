---
title: Charles安装与功能介绍
url: https://www.secpulse.com/archives/190626.html
source: 安全脉搏
date: 2022-11-09
fetch_date: 2025-10-03T22:04:09.004321
---

# Charles安装与功能介绍

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# Charles安装与功能介绍

[工具](https://www.secpulse.com/archives/category/tools)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-08

12,027

# 0x01 介绍

Charles是在PC端常用的网络封包截取工具，除了可以在开发中调试端口外，Charles也可以用于分析第三方应用的通讯协议，配合Charles的SSL功能，还可以分析HTTPS协议。

BurpSuite在渗透测试中常用，Charles相比BurpSuite更易上手、简单直观。Charles是收费软件，可以免费试用30天。试用期过后，未付费仍可继续使用，但是每次使用时间不可超过30分钟，并且启动时将会有10秒的延迟，所以为了以后使用起来不麻烦还是选择付费或者...（你懂的）。

**Charles主要功能：**

• 截取http和https网络数据包；

• 支持重发网络请求，方便后端调试；

• 支持修改网络请求参数；

• 支持网络请求的截获并动态修改；

• 支持模拟慢速网络等。

# 0x02 下载与安装

官网 https://www.charlesproxy.com/latest-release/download.do

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190626-1667883876.png "null")

找到对应操作系统版本下载，下载成功后根据提示安装即可。

Charles激活码：

Registered Name: https://zhile.io License Key: 48891cf209c6d32bf4 （转自CSDN：blog.csdn.net/qq\_25821067…） Charles的logo是一个漂亮的瓷花瓶。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190626-1667883879.png)

# 0x03 Charles菜单介绍

## 主界面介绍

主界面如下图

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190626-1667883883.png)

**菜单栏中的常用工具：**

①：清除捕获到的所有请求；

②：红色代表正在捕获请求，灰色代表目前没有捕获请求；

③：停止SSL的代理；

④：灰色代表未开启网速节流，绿色代表开启；

⑤：灰色代表没有开启断点，红色代表开启；

⑥：编辑修改请求，点击后可以修改请求的内容；

⑦：重复发送请求，点击后选中的请求会被再次发送；

⑧：验证选中的请求响应；

⑨：购买许可证，会跳转至官网；

⑩：常用功能，包含Tools菜单中的常用功能；

⑪：常用设置，包含Proxy菜单中的常用设置。

**查看数据包视图**

Charles主要提供Structure和Sequence两种查看数据包的视图。

Structure：将网络请求按访问的域名分类；

Sequence：将网络请求按访问的时间排序；

使用时可以来回切换，Charles还提供了Filter功能，可以输入关键字快速筛选网络请求。

## 会话右键支持的功能

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190626-1667883886.png "null")

Repeat、Repeat Advanced 重复执行请求，Repeat Advanced可以指定重复的遍数，这样可以选中多会话，在右侧的chart查看请求的时间等性能。

**Focus** 当前选中的域名会被放在顶部，没有Focus的域名统一放到下面的Other Hosts下，也可在View-->Focused Hosts中统一编辑。

**Block List** 黑名单中的域名不可联网。

**Export** 导出会话Session保存到本地，下次就可通过File-->Open Session打开本地的Session。

**Compare** 左侧列表中选择两个Session，右键时会出现该选项，可以对比两个请求的入参和出参。

**Compose** 与工具栏中的钢笔图标一样，编辑请求然后执行。

**Map Remote** 重定向到另一个请求的返回值当作自己的返回值，可以在Session上右键Map Remote设定规则，或Tools-->Map Remote来管理所有的Map Remote，再勾选Enable Map Remote启用。

**Map Local** 使用本地的一个文件的内容作为返回值 可以在Session上右键Map Local设定规则，或Tools-->Map Local管理所有的Map Local，勾选上Enable Map Local启用。

## Proxy菜单

Charles是一个http和socks代理服务器。代理请求和响应使Charles能够在请求从客户端传递到服务器时检查和更改请求，以及从服务器传递到客户端时的响应。

Charles的主菜单有：File、Edit、View、Proxy、Tools、Windows、Help，用的最多的是Proxy和Tools。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190626-1667883888.png)

**Proxy 菜单包含以下功能：**

Start/Stop Recording：开始/停止记录会话。

Start/Stop Throttling：开始/停止节流。

Enable/Disable Breakpoints：开启/关闭断点模式。

Recording Settings：记录会话设置。

SSL Proxying Settings：SSL 代理设置。

Throttle Settings：节流设置。

Breakpoint Settings：断点设置。

Reverse Proxies Settings：反向代理设置。

Port Forwarding Settings：端口转发。

Proxy Settings：代理设置。

Access Control Settings：访问控制设置。

External Proxy Settings：外部代理设置。

Web Interface Settings：Web 界面设置。

### Recording Settings-记录会话设置

Recording Setting和Start/Stop Recording配合使用，在Start Recording的状态下，可以通过Recording Setting配置Charles的会话记录行为。

Recording Settings 有 Options、Include、Exclude 三个选项卡：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190626-1667883890.png "null")

• **Options**：通过Recording Size Limits限制记录数据的大小。当Charles记录时，请求、响应头和响应体存储在内存中，或写入磁盘上的临时文件。有时，内存中的数据量突然增多，Charles会提示并停止录制。这时应该清除会话释放内存，再开始录制。在录制设置中，可以限制Charles录制的大小，这样不会影响浏览，Charles指挥停止录制。

• **Include**：只有与配置的地址匹配的请求才会被录制；

• **Exclude**：只有与配置的地址匹配的请求将不会被录制。

Include和Exclude操作相同，选择Add，填入需要监听的Procotol、Host、Port等信息即可。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190626-1667883891.png "null")

或者右击网址选择Focus，其他的请求就会被放置到Other Host分类中，也可达到过滤的目的。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190626-1667883892.png)

### Throttle Settings-节流设置

Throttle Settings和Start/Stop Throttling配合使用，在Start Throttling的状态下，可以通过Throttle Settings配置Charles的网速模拟配置。

勾选Enable Throttling启用网速模拟配置，在Throttle Preset下选择网络类型即可，具体设置可以根据实际情况自行设置。如果只想模拟指定网站的慢速网络，可以再购选上Only for selected hosts项，再在对话框的下半部分设置中增加指定的hosts项即可。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190626-1667883895.png)

### Breakpoint Settings-断点设置

Breakpoint Settings和Enable/Disable Breakpoints配合使用，在Enable Breakpoints的状态下，可以通过Breakpoint Settings配置Charles的断点模式。

勾选上Enable Breakpoints启用断点模式，选择Add，填入需要监控的Scheme、Procotol、Host和Port等设置断点，再观察或者修改返回的内容，但是要注意请求超时时间问题。或者可以在某个想要设置断点的请求网址上右击选择Breakpoint设置断点。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190626-1667883904.png)

### Reverse Proxies Settings-反向代理设置

反向代理在本地端口上创建Web服务器，该端口透明的将请求代理给远程Web服务器。反向代理上所有的请求和响应都可以记录在Charles中。

创建原始目标Web服务器的反向代理，然后将客户端应用程序连接到本地端口，反向代理对客户端应用程序是透明的，可以查看Charles之前可能无法访问的流量。选中Enable Reverse Proxies进行Add添加即可。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190626-1667883908.png)

### Port Forwarding Settings-端口转发

可以将任何TCP/IP或UDP端口配置为使用Port Forwarding工具从Charles转发到远程主机，这样可以调试Charles中的任何协议。还可以使用Charles作为Socks代理，所以无需设置端口转发。配置与Reverse Proxies Settings类似，Add添加即可。

### macOS Proxy-记录计算机上的所有请求

抓取电脑端的请求，勾选macOS Proxy即可，如果只抓取移动端请求，则取消勾选这个选项。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190626-1667883913.png "null")

### Proxy Settings-代理设置

默认代理端口为8888（可以自行修改）。填写上端口、勾选上Enable transparent Http proxying，就完成了Charles的代理设置。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190626-1667883915.png)

### SSL Proxy Settings- SSL代理设置...