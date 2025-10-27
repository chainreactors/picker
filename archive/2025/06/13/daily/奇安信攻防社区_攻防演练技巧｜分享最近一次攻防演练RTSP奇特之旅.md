---
title: 攻防演练技巧｜分享最近一次攻防演练RTSP奇特之旅
url: https://forum.butian.net/share/4401
source: 奇安信攻防社区
date: 2025-06-13
fetch_date: 2025-10-06T22:47:49.190679
---

# 攻防演练技巧｜分享最近一次攻防演练RTSP奇特之旅

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 攻防演练技巧｜分享最近一次攻防演练RTSP奇特之旅

* [渗透测试](https://forum.butian.net/topic/47)

师傅们在攻防演练中，可以看看这篇文章，打视频监控系统拿权限分，下面就来介绍下这个RTSP漏洞。

声明
--
本文章所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.
作者：routing
原文链接：<https://zone.huoxian.cn/d/2989-rtsp>
0x1 RTSP奇特之旅前言
--------------
### 浅谈
哈咯，师傅们，好久不见！
已经很久没有写文章了，这次简单写一个蛮有意思的案例，也是在最近攻防演练中遇到的。
其实在最初开始晚没有特别的去想着去利用这个漏洞——RTSP协议漏洞，因为之前有看过文章简单了解过，主要就是打弱口令和未授权访问漏洞，然后一般就是比较敷衍的使用爆破工具爆破下，有无弱口令，或者使用字典目录遍历下。
像下面的我就喜欢使用无影tools的爆破模块
把目标导入即可，然后选择RTSP的554端口进行爆破，字典可以选择内置的字典
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
其次一般像RTSP的弱口令和未授权在我以前感觉用处不是很大，且平常挖src漏洞之类的，也不怎么碰的到。但是这次攻防演练嘛，有些东西在平常可能没多大的利用的价值，但是打攻防说不定就是可以打分打权限的那种，下面就来介绍下这个RTSP漏洞。
其中主要还是在网上看了很多的打法和文章资料，在网上尝试了蛮多的工具，发现一款GitHub上面的新利用RTSP漏洞一键利用的工具，然后结合这次资产刚好有，就利用起来了。
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
然后这次我开始也是简单的爆破下，因为这次是攻防演练嘛，然后是某单位的资产，且有好多下级部门的厂商视频监控管理系统，所以对应的监控大都是RTSP协议的，集群远程管理。
且这次的攻防演练目标资产比较多，范围比较广，只要是属于该市的资产都可以，还有一些企业的都可以，像很多的监控系统都带有远程管理操作，所以有部分都是RTSP协议的，且这个漏洞在平常接触比较少，就比如我平常挖src对这个漏洞基本上没有太多的操作。
下面是我简单收集的一些资产表格如下：
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
0x2 众测捡钱小技巧（拓展）
---------------
### 一、浅谈
上面既然介绍到了我们平常挖企业src中一些不怎么会收的漏洞，比如我这里要讲的RTSP漏洞，这个漏洞的话主要是在攻防演练中，我们可以对目标资料中的一些监控管理系统进行拿监控管理权限的分，因为在攻防演练中主要是通过拿数据分和权限分，特别是你打进内网，像这样的监控系统肯定很多，这样就可以帮助你拿比较多的权限分。
这里给师傅们看下某些评分标准：
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
下面我来给师傅们讲下众测中，我一般第一先测试的漏洞——SPF邮件伪造漏洞。
具体的测试方法，我下面有很详细的测试手法，其实网上也有很多的批量跑SPF邮件伪造漏洞的脚本，其中我自己也是利用这些脚本去测试的，因为在众测中，得拼手速了，具体的脚本我这里就不放上去了，因为脚本内容因人而异，最好自己修改下。
其实在攻防演练中也是可以利用SPF邮件伪造漏洞的，可以使用SPF邮件伪造去钓鱼，收集目标资产的邮箱，然后去钓鱼攻击，也是一种方法，在护网期间，钓鱼攻击是特别常态且使用特别多的一种方式。
### 二、SPF邮件伪造漏洞
针对师傅们对于SPF邮件伪造漏洞的拓展，师傅们可以看我之前写的那篇原创文章：<https://xz.aliyun.com/news/14752>
这里就引用这篇文章的SPF邮件伪造漏洞，写的蛮详细的，师傅们可以参考学习下，然后后面在众测项目上去赚点漏洞赏金。
#### 1、spf邮件伪造漏洞简介：
SPF 记录是一种域名服务（DNS）记录，`用于标识哪些邮件服务器可以代表您的域名发送电子邮件`。
SPF 记录的目的是为了防止垃圾邮件发送者在您的域名上，使用伪造的发件人地址发送邮件。
原理:未设置spf导致的邮件任意伪造，可以用来钓鱼社工，本身就是高危
若您未对您的域名添加 SPF 解析记录，则黑客可以仿冒以该域名为后缀的邮箱，来发送垃圾邮件。
#### 2、漏洞危害：
可以用未进行安全配置的网站域名，发送邮件。
比如：www.baidu.com有这个漏洞，你就可以伪造HR@baidu.com给受害人发邮件进行钓鱼。
src收的少，但是重测和渗透测试项目可以交。
- \\*\\*注意：\\*\\*如果没有`v=spf1`或者`没spf`就存在邮件伪造漏洞。
- -all 不能伪造，~all可以伪造
#### 3、测试漏洞
我们直接拿baidu.com的域名来给大家演示下，用kali的nslookup 工具测试下
可以看到下面的回显，存在spf记录，是-all参数，说明不能任意伪造。
```php
┌──(root-kali)-[~]
└─# nslookup -type=txt baidu.com
```
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
还可以使用dig -t命令来测试
```php
┌──(root-kali)-[~]
└─# dig -t txt baidu.com
```
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
#### 4、\*\*SPF解析不当导致绕过\*\*
把下面的spf配置记录复制下来
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
\*\*测试地址如下：\*\*
<https://www.kitterman.com/spf/validate.html>
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
这里显示spf解析配置正确
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
下面拿一个存在spf解析错误的案例来演示下：
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
SPF记录报错，在这条SPF记录中，存在多个IP段，但只有开头的一段ip用了ipv4，这就导致了语法错误。因为这个错误，将导致整个SPF记录完全失效，因为SPF无效，邮件接收方的SPF检测功能也就失效了。
#### 5、swaks 测试
使用kali自带工具swaks 测试
```php
swaks --body "helloword" --header "Subject:testT" -t 自己的邮箱 -f test@baidu.com
body为内容
Subject为标题
-t为目标邮箱
-f为伪造的发送方，这里我们伪造加了cn字眼，这里伪造改不明显字眼等都会进垃圾箱
```
我们先申请一个临时邮箱：
<http://24mail.chacuo.net/>
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
然后我们使用kali自带的swaks 工具进行测试，结果如下
```php
┌──(root-kali)-[~]
└─# swaks --body "【2024年8月1日】 检测到您教务系统长时间未修改密码，请及时修改密码确保账户安全 手机管家@163.com
【该邮件自动监测请勿回复】" --header "Subject:vivo" -t vioxzs43016@chacuo.net -f customers@alexz.com
```
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
看到这里，我们要是对标题和内容进行改进，那么我们是不是就可以尝试钓一波鱼了呢？
0x3 RTSP协议漏洞介绍
--------------
### 一、协议分析
- RTSP（实时流协议）是一个网络控制协议，设计用于娱乐和通信系统中控制流媒体服务器。该协议用于建立和控制媒体会话中的时间同步流。RTSP 提供了一个可扩展框架，使得能够实现对实时数据，如音频和视频的控制。与HTTP不同，RTSP提供了对流数据的实时控制功能，比如可以随意快进或倒退。
- \*\*RTSP 主要用于以下场景：\*\*
1、视频监控系统，会议视频
2、IP摄像头监控(企业、大街、工厂的监控头)
3、媒体播放器与媒体服务器之间的交互
4、智能家居设备，比如：门铃、智能汽车行车仪等
- RTSP 协议通常运行在 TCP 或 UDP 协议之上，使用的端口是554，不同厂商可能是8554端口。它允许客户端发送播放、暂停和停止等控制指令，以及进行实时播放位置的调整。
### 二、RTSP认证方式
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
#### 1、Basic认证（基本认证）
基本认证是HTTP 1.0 提出的认证方案，其消息传输不经过加密转换因此存在严重的安全隐患。
服务端在未认证时返回401Unauthorized，并带上WWW-Authenticate: Basic realm="RTSP Server"头，要求客户端提供凭据。
\*\*1） 客户端发送 DESCRIBE 请求\*\*
```php
DESCRIBE rtsp://192.168.1.55:554/11 RTSP/1.0\\r\\n CSeq: 1\\r\\n
Accept: application/sdp\\r\\n
User-agent: Realplayer\\r\\n\\r\\n
```
\*\*2）服务端发出 WWW-Authenticate 认证响应\*\*
服务端返回401错误码，发出 WWW-Authenticate 认证响应告诉客户端需要进行认证。
```php
RTSP/1.0 401 Unauthorized\r\n
CSeq: 1\r\n WWW-Authenticate: Basic realm="RTSPD"\r\n\r\n
```
\*\*3）客户端再次发出 DESCRIBE 请求\*\*
此时客户端程序弹出密码认证窗口 ，提示输入用户名，密码等认证信息，并根据服务端返回的响应消息中进处理，如果发现是 Basic认证则携带认证信息发送如下报文：
```php
DESCRIBE rtsp://192.168.1.55:554/live/1/video.sdp?token=A00453FR805a54C8 RTSP/1.0\r\n CSeq: 2\r\n
Accept: application/sdp\r\n
User-Agent: RealMedia Player HelixDNAClient/12.0.1.647 (win32)\r\n Authorization: Basic YWRtaW46YWRtaW4=\r\n\r\
```
其中 “YWRtaW46YWRtaW4=” 是通过 username:password 进行 base64 编码所得。因为其具有唯一性等价于账号和密码，明文发送泄漏后存在安全风险。
#### 2、Digest认证（摘要认证）
摘要认证是http 1.1提出的基本认证的替代方案，其消息经过MD5哈希转换因此具有更高的安全性。
避免了直接明文传输密码的风险。但是 MD5 哈希较弱，仍然可以通过 彩虹表等方式破解。
### 三、RTSP认证流量监测
首先，这里你去了解RTSP认证流量，得先安装两款工具，工具是使用Wireshark和VLC视频播放工具。
#### \*\*1、Wireshark下载地址\*\*
<https://www.wireshark.org/download.html>
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
#### \*\*2、VLC视频播放工具\*\*
[https://www.videolan.org/vlc/index.zh\\_CN.html](https://www.videolan.org/vlc/index.zh\_CN.html)
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
\\*\\*因为我的电脑上macbook，所以打开VLC和使用如下操作（windows的操作也是差不多的） \\*\\*
1、默认下载下来是英文的，直接可以设置中文的
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
选择Language，然后选择简体中文，重启软件就好了
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
2、打开 VLC 主界面，选择\*\*File &gt; OpenNetwork\*\*（中文版为\*\*媒体 &gt; 打开网络串流\*\*）
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
3、在弹出的对话框输入直播流播放地址，然后点击打开即可查看监控视频画面了
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
#### 3、认证流量监测
使用Wireshark和VLC视频播放工具
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
获取rtsp协议认证方式，可以发送options和describe请求进行，如下图所示，获取到认证方式为401 Basic和Digest, 如果返回的状态码为200，说明存在未授权访问。
![](%E5%9B%BE%E7%89%87%E8%A7%A3%E6%9E%90%E4%B8%8A%E4%BC%A0%E5%A4%B1%E8%B4%A5)
0x4 RTSP漏洞攻击
------------
### 一、主流摄像头安全问题汇总
1、警卫视摄像头
```php
型号：qs-qy
连接密码：密码默认为空
rtsp连接地址:
rtsp://admin@IP:554/live/ch00\_1
```
2、乐橙摄像头
```php
型号:LC-S2D
rtsp密码：摄像头底部安全码
rtsp连接地址:
rtsp://admin:L2C3F848@IP:554/cam/realmonitor?channel=1&subtype=0
```
3、tp-link摄像头
```php
设备型号:TL-IPC44AW
rtsp密码：默认为空
rtsp连接地址:
rtsp://admin@IP:554/stream1
```
4、萤石摄像头
```php
设备型号：CS-C6
rtsp密码：摄像头底部安全码
rtsp连接地址:
rtsp://admin:RMETAA@IP:554/h264/ch1/main/av\_stream
```
5、乔安智联摄像头
```php
设备型号：JA-C10E
rtsp密码：空密码
rtsp连接地址:
rtsp://admin@IP:554/live/ch00\_1
```
6、帝防摄像头
```php
设备型号：JA-C10E
rtsp连接地址:
rtsp://admin:admin11@IP:554/onvif1
```
7、Cubetoou摄像头
```php
设备型号：Q88
rtsp连接地址:
rtsp://admin:123a123a@IP:554/onvif1
```
8、 icam3...