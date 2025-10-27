---
title: Kali Linux虚拟机连宿主机代理配置！
url: https://www.secpulse.com/archives/197982.html
source: 安全脉搏
date: 2023-03-22
fetch_date: 2025-10-04T10:14:24.198174
---

# Kali Linux虚拟机连宿主机代理配置！

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

# Kali Linux虚拟机连宿主机代理配置！

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[潇湘信安](https://www.secpulse.com/newpage/author?author_id=37983)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2023-03-21

17,773

|  |
| --- |
| **声明：**该公众号大部分文章来自作者日常学习笔记，也有部分文章是经过作者授权和其他公众号白名单转载，未经授权，严禁转载，如需转载，联系开白。  请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。 |

**0x00 前言**

前段时间看到群里有师傅在讨论如何让虚拟机走物理机的代理流量，或者说让局域网其他主机走某一台主机的代理流量，今天抽空测试了几款常用代理软件的配置方法，分享给有需要的朋友，不喜勿喷！！！

**0x01 宿主机代理设置**

因为是虚拟机要走物理机的代理流量，所以我们得先查看下物理机的内网IP，后边在连接这个代理时要用上。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197982-1679365272.png)

**v2rayN**

我们宿主机用的v2rayN客户端，代理节点大家自己准备，软件界面点击设置中的参数设置选项，勾选“允许来自局域网的连接”即可。

```
项目地址：https://github.com/2dust/v2rayN
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197982-1679365273.png)

这时软件界面的底部会显示局域网的socks/http代理端口socks:10810、http:10811，命令行下可以看到0.0.0.0开启了这两个端口。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197982-16793652731.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197982-1679365274.png)

**Clash**

我们常用的Clash软件也可以设置，配置好代理规则后只需开启“允许局域网连接”即可，默认连接端口7890，可自行更改为其他端口，支持socks和http代理。

```
项目地址：https://github.com/Fndroid/clash_for_windows_pkg
汉化补丁：https://github.com/BoyceLig/Clash_Chinese_Patch
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197982-1679365275.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197982-16793652751.png)

**S-Socks（防和谐）**

SS/SSR节点也可以用S-Socks，在系统任务栏中右键软件图标， 勾选“允许其他设备连入”即可，默认连接端口1080，可自行更改为其他端口。

```
项目地址：https://github.com/shadowsocks/shadowsocks-windows
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197982-1679365276.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197982-1679365277.png)

**0x02 虚拟机连接代理**

Kali或其他Linux可以用ProxyChains，编辑ProxyChains配置文件，输入i进入插入模式，在ProxyList下添加我们的socks5代理，编辑完成后按Esc键退出编辑模式，输入:wq并回车保存即可。

```
项目地址：https://github.com/rofl0r/proxychains-ng
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197982-1679365278.png)

这时可以先用curl命令来确定这个socks5代理是否连接成功，如果没问题再用ProxyChains代理各种常用工具进行安全测试，如：firefox、msf、nmap、sqlmap等，走的都是物理机代理流量。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197982-16793652781.png)

Windows可以用Proxifier、SocksCap，以Proxifier为例，Profile->Proxy Servers->Add，输入物理机内网Socks代理192.168.1.110:10810即可，代理规则自行设置，这里我只是检查通不通。

```
Proxifier：https://www.proxifier.com
SocksCap：https://sourceforge.net/projects/sockscap64
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197982-1679365280.png)

**0x03 手机端连接代理**

手机端可以在连上WI-FI时配置一个http代理，但只有浏览器/公众号/小程序等http相关数据才走物理机代理流量，并不是全局哦，IOS、Android只内置有http，socks需另找其他APP，上P站学习够了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197982-16793652801.png)

找到一个安卓APP（ProxyDroid）可以设置HTTP/SOCKS4/SOCKS5代理，但是在开启全局代理时发现需要root...，我这台测试机不行，大家自己测试下吧，IOS因限制问题可能不太好找...。

```
ProxyDroid：https://github.com/zzzzfeng/proxydroid/releases
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197982-1679365282.png)

**本文作者：[潇湘信安](newpage/author?author_id=37983)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/197982.html**](https://www.secpulse.com/archives/197982.html)

Tags: [HTTP](https://www.secpulse.com/archives/tag/http)、[Kali Linux](https://www.secpulse.com/archives/tag/kali-linux)、[Proxifier](https://www.secpulse.com/archives/tag/proxifier)、[ProxyDroid](https://www.secpulse.com/archives/tag/proxydroid)、[SocksCap](https://www.secpulse.com/archives/tag/sockscap)、[v2rayN](https://www.secpulse.com/archives/tag/v2rayn)、[安卓APP](https://www.secpulse.com/archives/tag/%E5%AE%89%E5%8D%93app)、[虚拟机](https://www.secpulse.com/archives/tag/%E8%99%9A%E6%8B%9F%E6%9C%BA)

点赞：
3
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![API安全基础理论](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image10-300x192.png)

  API安全基础理论](https://www.secpulse.com/archives/200281.html "详细阅读 API安全基础理论")
* [![如何在TG群中获取用户真实IP？这些手段教你轻松实现【附代码】](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199003-1681709551-300x260.png)

  如何在TG群中获取用户真实IP？这些手段…](https://www.secpulse.com/archives/199003.html "详细阅读 如何在TG群中获取用户真实IP？这些手段教你轻松实现【附代码】")
* [![数万台设备已被影响！疑似DDOS团伙Blackmoon再现江湖](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196115-1676871360-300x146.png)

  数万台设备已被影响！疑似DDOS团伙Bl…](https://www.secpulse.com/archives/196115.html "详细阅读 数万台设备已被影响！疑似DDOS团伙Blackmoon再现江湖")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2020/11/12/5abbd29a2ce13702d20784fb420161da-290x290.png)](https://www.secpulse.com/newpage/author?author_id=37983aaa) | [潇湘信安 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)](https://www.secpulse.com/newpage/author?author_id=37983) | |
| 文章数：57 | 积分： 15 |
| 关注微信公众号【潇湘信安】，一起学习网络安全知识！ | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/theme...