---
title: 光指令注入攻击 | IOT物联网声控设备的噩梦
url: https://www.4hou.com/posts/jBQl
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-04
fetch_date: 2025-10-06T17:40:51.403359
---

# 光指令注入攻击 | IOT物联网声控设备的噩梦

光指令注入攻击 | IOT物联网声控设备的噩梦 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 光指令注入攻击 | IOT物联网声控设备的噩梦

RC2反窃密实验室
[行业](https://www.4hou.com/category/industry)
2024-07-03 14:04:14

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)103468

收藏

导语：关于光指令注入攻击的攻击原理、危害以及防御方式。

2020年，物理威胁也开始进入新的阶段。尤其是在信息/网络安全得到大力发展强化的现在，物理渗透、越位刺探和非常规窃密，也超越社工行为，成为飞速发展的新威胁趋势。

接下来，杨叔就带大家了解下最新的攻击方式：**“利用激光实现对声控系统的音频指令注入攻击”**，简称“光指令注入攻击”。

**01 新的威胁**

**Light Commands（光指令）**是MEMS麦克风的一个漏洞，攻击者可以利用激光将无法听见和看不见的命令远程注入到语音助手，目前已被攻克的有Google助手，Amazon Alexa，Facebook Portal和Apple Siri。

国外研究员们已经成功地利用激光将恶意命令注入到了许多声控设备中，例如远距离穿透玻璃窗，对室内的智能扬声器、平板电脑和智能手机开展攻击。

![1.2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719901012103119.jpg "1719900578162294.jpg")

Tips：这种以光（而非声音）为主要介质将命令传送到麦克风的方式，称之为光指令，即Light Commands。所以，这类攻击就称之为光指令注入攻击，即Light Commands Injection Attack。

![1.3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719901012107719.jpg "1719900605199078.jpg")

根据可以通过语音执行的命令类型，注入未经授权的语音命令，会导致不同程度的危害。

例如，研究员们已经证实了攻击者可以使用注入的语音命令来解锁受害人的智能门锁，而严重的，**甚至定位、解锁和启动各种智能车辆**。

**02 聊聊MEMS麦克风**

首先，什么是MEMS麦克风？先说两个专业词：

MEMS：Micro Electro Mechanical System，微机电麦克风

ECM，Electret Condenser Microphone，驻极体电容麦克风

以前使用的大多数麦克风都是ECM(驻极体电容器)麦克风，这种技术已经有几十年的历史。ECM 的工作原理是利用驻有永久电荷的聚合材料振动膜。

与ECM的聚合材料振动膜相比，MEMS麦克风在不同温度下的性能都十分稳定，其敏感性不会受温度、振动、湿度和时间的影响。

![1.4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719901012134917.jpg "1719900664159860.jpg")

而据报道，MEMS最大的厂商楼氏电子在2017年3月宣布，其MEMS麦克风销量已累积达到100亿颗新里程碑。

![1.5.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719901013681150.jpg "1719900683155098.jpg")

现在，从智能手机到智能设备，再到车载娱乐系统，基本上都在使用MEMS麦克风。**目前国内主流的声控设备绝大部分都使用了MEMS麦克风**。

**03 攻击原理与危害**

MEMS麦克风能将声音转换为电信号。这次漏洞的主要发现是：**除了声音之外，MEMS麦克风还会对照射到它们的光做出反应**。

因此，通过光束强度调制电信号，攻击者就可以诱使MEMS麦克风产生电信号，就像它们正在接收真正的音频一样。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719901013203788.jpg "1719900738131494.jpg")

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719901013349961.jpg "1719900748194447.jpg")

于是，攻击者就可以使用激光穿透窗户，直接照射到智能扬声器、平板电脑或电话的麦克风上，位于远处的攻击者就可以远程发送看不见且可能看不见的指令，然后由Alexa、Portal、Google助手或Siri执行操作指令。

![1.9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719901014522697.png "1719900794334841.png")

更糟糕的是，一旦攻击者获得了语音助手的控制权，攻击者就可以使用它来破坏其他系统。例如，攻击者可以：

**·**控制家用智能设备的开关

**·**打开智能车库门

**·**进行网上购买

**·**远程解锁并启动某些车辆

**·**通过暗中强行强制用户的PIN码来打开智能门锁

由于语音助手本质上依赖语音与用户交互，那么通过向麦克风发射特定激光，攻击者就可以劫持语音助手，并将无法听见的命令发送到Alexa、Siri、Portal或Google Assistant**（均已测试成功）**。

**04 深入了解“光指令注入攻击”**

**攻击有效距离**

虽然光的传播距离理论上是没有限制的，但是激光瞄准器的局限性和聚焦的高要求都会影响到攻击距离。

目前，安全研究员们已经在110米长的走廊中验证了攻击有效性。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719901014895869.png "1719900852184699.png")

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719901014178464.jpg "1719900857273698.jpg")

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719901015147652.jpg "1719900878732448.jpg")

**如何使用激光瞄准**

确实需要仔细瞄准和激光聚焦才能发送光指令。要将激光聚焦在远距离，可以使用市售的远焦镜头，再配合使用带齿轮的三脚架进行瞄准，就可以极大提高精度。

同时，攻击者可以使用望远镜或双筒望远镜来远距离查看设备的麦克风端口。

![1.13.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719901015942608.jpg "1719900911142119.jpg")

**有哪些设备受到影响**

研究员们已经测试了最受欢迎的语音识别系统（包括Amazon Alexa、Apple Siri、Facebook Portal和Google Assistant）。

同时对多种设备（例如智能扬声器、电话和平板电脑以及具有内置语音识别功能的第三方设备）完成了基准测试。

下图点击放大看（左边是受影响的设备）：

![1.14.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719901015784568.jpg "1719900942805791.jpg")

**其他语音控制系统是不是都这么脆弱**

尽管目前安全研究员的研究集中在Alexa、Siri、Portal和Google Assistant上，但Light Commands利用的基本漏洞来自MEMS麦克风中的设计问题。

也就是说，任何使用MEMS麦克风设计在没有额外用户确认的情况下会进行数据操作的系统都可能受到攻击。

**如何检测是否有人对自己使用了Light Commands攻击**

尽管通过光/激光进行的命令注入没有声音，但是细心的用户可以注意到攻击者在目标设备上反射的光束。

或者，可以尝试观察语音设备的言语响应和灯光模式变化，这两者都可以视为命令确认。

**攻击效果取决于激光的颜色或波长吗**

在实验过程中，安全研究员们已经证实效果与颜色和波长无关。尽管蓝光和红光在可见光谱的其他边缘上，但注入的音频信号的电平在相同范围内，频率响应曲线的形状也相似。

**攻击者可以使用其他光源实现么**

原则上，任何足够明亮的、支持长距离直射的光都可以用来发起攻击。

![1.15.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719901016708548.jpg "1719900981278512.jpg")

**05 如何防御**

尽管看起来似乎很难防御，但是还是有这样几种方法可以规避或弱化风险。

**方法一：增加身份验证次数可以有效地减轻攻击**

比如，由于攻击者无法获取设备的响应，所以完全可以在命令执行之前，让智能设备向用户询问一个简单的随机问题，这可能是阻止攻击者让设备成功执行命令的有效方法。

**方法二：制造商可使用传感器融合技术**

例如，改为从多个麦克风获取音频。因为当攻击者使用单个激光时，将只有一个麦克风接收信号，而其他麦克风则什么也没有。因此，制造商可以尝试忽略此类单麦克风注入的命令，来检测此类异常情况。

**方法三：设置屏障来减少到达麦克风振膜的光量**

可以在麦克风孔的顶部，安装一个不透明的覆盖物以衰减麦克风的光量。

但是，此类物理屏障仅在一定程度上有效，因为攻击者完全可以增大激光功率，以补偿覆盖物导致的衰减，当然也可以直接灼烧覆盖物，以创建新的光路。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?5R9ytxPX)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/182735b0219b1d7a63869aa0c554f245.png)

# [RC2反窃密实验室](https://www.4hou.com/member/33jn)

专注TSCM，物理安全和隐私保护~

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/33jn)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024...