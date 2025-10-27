---
title: 击穿HW | 来自物理安全的重拳
url: https://www.4hou.com/posts/MKRG
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-04
fetch_date: 2025-10-06T17:40:50.437132
---

# 击穿HW | 来自物理安全的重拳

击穿HW | 来自物理安全的重拳 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 击穿HW | 来自物理安全的重拳

RC2反窃密实验室
[行业](https://www.4hou.com/category/industry)
2024-07-03 15:15:18

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)98968

收藏

导语：希望HW期间，防守方能重视物理安全，尽快封堵物理安全风险。

公安部研究制定的《贯彻落实网络安全等保制度和关保制度的指导意见》，明确指出网络安全工作“三化六防”的措施，即实战化、体系化、常态化的思路，以及动态防御、主动防御、纵深防御、精准防护、整体防控、联防联控的措施。实践证明，**网络安全保护已全面进入实战化阶段**。

而随着HW攻击手段的愈发刁钻，防守方也是头疼不已。本期，杨叔梳理了一些可能被忽视的物理安全防御死角，给大家再加点料。

![图6.1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240424/1713926444134729.jpg "1713921720657758.jpg")

注：以下内容仅代表杨叔个人经验和建议，仅供红蓝队参考。

**01 关于战果定义的狭隘**

这几年看了很多HW的案例分享和战术总结，颇有些感慨。

比如：总觉得对于战果的定义有些狭隘和片面。

引用一个来自网上的蓝队防护工作指导图：

![图6.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240424/1713926445948059.png "1713922237192008.png")

杨叔相信很多蓝队的防护思维与此类似，试问一下：

既然说是重视实战，那么

**·**难道实战中，只有出现扫描、种马、溢出等行为才算是攻击吗？

**·**只有攻入内网，拿到管理员或者数据库权限才算是攻击成功吗？

**·**那些获取到企业今年的战略规划、内部决策会议信息、投资内幕的情况，算不算获取到企业核心机密？

**·**拿到企业高层大佬们开会视频录像，算不算企业关键信息泄露？

**02 常见的物理防守死角**

讲一个案例，虽然是真实的，但大家也可以当做故事听：

某大型企业内部信息安全体系建设日臻完善，总裁觉得安全已无需再做大投入，但CSO觉得有必要开展下外部黑盒测试。

于是在授权下，一个渗透小组开始从外围寻找攻击的可能性。经过了长期的测试和试探，他们找到了突破点：**保安室的WiFi网络**。

![图6.3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240424/1713926446263151.jpg "1713922346929245.jpg")

尽管很多企业都要求不得私自搭建无线网络，但总有人为了自己方便，会在内网上连接一个无线路由器，这个保安室就是这样。

于是，他们用WiFi万能钥匙轻松拿到了WiFi密码，当然，也可以试试高速破解之类，但大家都知道，大部分安保从业者的文化水平并不是很高，对于网络安全的概念基本无从谈起。所以首选万能钥匙，是正确的思路。

于是，通过这个WiFi，攻击小组成功绕过各种防护设备，直接渗透进内网。

大多数企业的内网安全，比想象的糟糕太多。这个小组最后找到了摄像头的控制台，成功地拿到了内部摄像头的权限，对，就是那个在房间角落顶部安装的那个。

![图6.4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240424/1713926447360492.jpg "1713923817414423.jpg")

最有意思的是，他们拿到了总裁会议室摄像头的权限。于是，为了证明内部安全确实存在较大隐患，在CSO的亲自监督下，录制了一次内部总裁会议的全过程。

第二天，CSO在总裁面前播放了这个视频。

从此以后，每年定期的内部安全整治工作，就成为了常态

PS：是的，可能你也会奇怪，总裁会议室怎么会有监控？其实，大部分是会议系统的WiFi无线摄像头，但也有个别是安防摄像头（后者确实有些奇怪？比如下图里你能看到什么？）

![图6.5.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240424/1713926448187485.jpg "1713924449182414.jpg")

类似地，这样的防守死角广泛出现在保安室、保洁休息室、物业办公室、后勤部门、食堂休息区等地方。

**03 最大的物理渗透盲区**

PSTI即Physical Security Threat Intelligence，物理安全威胁情报，讲述了目前大多数企业都在面临的窃密风险点，也是很多安全人员的盲区之一。

目前绝大多数大型企业，为了方便，都是采用第三方绿植供应商的服务，如定期上门更换绿植，或者定期上门维护等。

这些绿植，被大范围地部署在企业高管办公室、集团会议室、总裁办、研发部门、财务室等等核心甚至敏感的位置。而在第三方服务人员将绿植搬入高管办公室时，也不会有任何形式的安全检测。令人遗憾的是，上述这些情况目前在大企业里非常普遍。

换句话说：**存在非常严重的物理安全威胁隐患**。

![图6.6.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240424/1713926448380753.jpg "1713924533866931.jpg")

攻击队完全可以在绿植里布置无线发射装置、远程录音器材、无线WiFi中间人设备等等，实现对内部网络的跳转、关键内容的录音等等。

手持金属探测器会是一个好选择，不过不推荐那些网红畅销款。

**04 信号屏蔽的契机**

我们都知道，对4G网络使用BTS伪基站或其它主动式攻击时，手机信号会出现不稳定，甚至断线的情况，这个场景非常容易被识别和发现。

不过，希望通过屏蔽或干扰手机信号，来迫使企业员工使用WiFi来进行数据交互，也是常见的**WiFi钓鱼攻击方式之一**。

![图6.7.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240424/1713926449829516.jpg "1713924595117702.jpg")

2013年，杨叔曾在某企业授权开展过针对启用了802.1X认证架构的企业无线网络钓鱼，原理就是使用VMware搭建RADIUS认证服务器，伪造认证证书，再与自行搭建的无线路由器做授权关联，这样，在干扰掉合法的802.1X架构的无线AP后，就可以对内部员工开展钓鱼WiFi攻击。

实施起来确实有点麻烦，要求对Linux下的FreeRADIUS、Windows下RADIUS服务器和802.1X体系都非常了解。回到本节开始说的干扰手机信号，其实干扰的契机还是有的，比如每年一些重要的考试期间，考场附近都会开启大功率信号屏蔽仪，可能导致周边的手机信号频繁掉线、通话断断续续、上网缓慢等情况。

最近大家都收到类似的短信了吧？

![图6.8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240424/1713926450140090.png "1713924662199363.png")

那么，攻击队完全可能利用6月至7月的各类社会考试期间，对考点附近区域的企业开展不定期的信号干扰+钓鱼攻击......

必须牢记：大功率信号干扰器涉嫌违法，可能会引发考场无线电管理委员会的关注与溯源，及运营商基站监控方面的告警，甚至引发司法处置。

![图6.9.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240424/1713926450108757.jpg "1713924694167536.jpg")

**05 更加隐蔽的模式**

无论是蓝队在内部开部署会，还是企业自己的高层内部会议，会议室里还有一件物品，同样也是被忽视的典型盲区。

那就是：**会议室无线话筒，或无线麦克风**

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240424/1713926451171370.jpg "1713924773117171.jpg")

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240424/1713926452172766.jpg "1713924777210098.jpg")

由于市面在售的会议室无线电通信设备大部分是非保密性的通信方案，只要使用频谱仪或者同一类接收设备，甚至直接用对讲机调频到其工作频率上进行监听，就可以偷听到全部的会议内容。

从产品外观上很难看出区别，大的品牌相对好点，但也不能保证一定包含了加密芯片设计，类似下图这样，明确说明启用了数字话音保密技术的话筒或解决方案，才可以避免偷听泄密的可能性。

![图6.12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240424/1713926453190675.png "1713924839616236.png")

建议应安排专人检查内部会议室的无线话筒设备，测试下信号有无加密。

如果没有加密功能，要么建议行政更换话筒设备，比如临时过渡为蓝牙话筒+音箱组合，要么改成有线话筒。

欢迎大家参加「Level-2商业秘密保护课程」，学习交流物理安全防护知识与设备操作技能~

![图6.13.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240424/1713926453507268.jpg "1713924972148755.jpg")

最后，希望HW期间，防守方能重视物理安全，尽快封堵物理安全风险。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Kmte9rbe)

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

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou...