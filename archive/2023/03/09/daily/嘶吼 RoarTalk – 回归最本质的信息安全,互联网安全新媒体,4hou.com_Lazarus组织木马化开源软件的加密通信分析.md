---
title: Lazarus组织木马化开源软件的加密通信分析
url: https://www.4hou.com/posts/2J3K
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-09
fetch_date: 2025-10-04T09:00:46.380176
---

# Lazarus组织木马化开源软件的加密通信分析

Lazarus组织木马化开源软件的加密通信分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Lazarus组织木马化开源软件的加密通信分析

北京观成科技
[技术](https://www.4hou.com/category/technology)
2023-03-08 09:02:19

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)167772

收藏

导语：Lazarus组织近期利用社交平台实施新型钓鱼攻击，通过社交平台诱导受害者使用被改造成木马的开源软件，从而获取到受害主机的控制权限。观成科技安全研究团队发现该组织在某次攻击活动中使用了被改造成木马的开源软件UltraVNC。UltraVNC是一款开源的远程管理工具，Lazarus组织在该工具中嵌入了恶意下载器。下载器会从C&C服务器（互联网失陷主机）获取恶意DLL并在内存中加载，与服务器的C&C通

**1、概述**

Lazarus组织近期利用社交平台实施新型钓鱼攻击，通过社交平台诱导受害者使用被改造成木马的开源软件，从而获取到受害主机的控制权限。观成科技安全研究团队发现该组织在某次攻击活动中使用了被改造成木马的开源软件UltraVNC。UltraVNC是一款开源的远程管理工具，Lazarus组织在该工具中嵌入了恶意下载器。下载器会从C&C服务器（互联网失陷主机）获取恶意DLL并在内存中加载，与服务器的C&C通信全程使用HTTPS加密协议，加密载荷里的通信交互数据本身又使用了自定义的加密方式进行二次加密。

**2、通信过程**

表2-1 样本信息表

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230308/1678237194108790.png "1678237194108790.png")

该样本类型为ISO，其中包含两个文件：Amazon\_Assessment.exe、ReadMe.txt。木马化UltraVNC执行后，通过HTTPS加密协议上传系统信息，从C&C服务器下载并执行扩展DLL文件。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230308/1678237194100159.png "1678172525767002.png")

图 2-1 木马化UltraVNC通信过程图

**2.1 上线**

木马化的UltraVNC获取注册表键值”\HKEY\_LOCAL\_MACHINE\HARDWARE\DESCRIPTION\System\BIOS\SystemManufacturer”，即受害主机的生产厂商信息和工作组名称，用“|”符号连接后进行Base64编码并附加在样本中硬编码的URL后面，形如：https://kaonnews.com/wp-admin/network/sitemap.php?2E9AE1F528B27A798D8BE424E4E7A4E6=。然后，URL使用单字节0x89进行异或加密，加密后的信息通过HTTPS加密协议发送给C&C服务器。见图2-1中的①。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230308/1678237195887215.png "1678172535321143.png")

图 2-2 上线包（HTTPS）

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230308/1678237196208997.png "1678172543714351.png")

图 2-3 上线包（HTTPS解密后）

**2.2 解密释放恶意DLL**

攻击者通过社交平台诱导受害者使用木马化的UltraVNC连接ReadMe.txt中记录的IP 54.182.16.65后，见图2-1中的②。UltraVNC中攻击者添加的代码会计算该IP字符串的哈希值，将其作为密钥，循环异或解密样本中包含的恶意Dll文件，并在当前进程中加载运行。

**2.3 上传系统信息**

恶意DLL获取电脑名、系统磁盘信息、用户名、当前进程ID等信息，生成随机数作为通信校验的key（也用于URI生成）。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230308/1678237197532695.png "1678172574847675.png")

图 2-4 DLL中硬编码的通信URL

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230308/1678237197420127.png "1678172587137534.png")

图 2-5 上传信息数据（加密前）

DLL对数据进行ZIP压缩+自定义加密+Base64编码处理后使用HTTPS加密上传到C&C服务器，见图2-1中的③。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230308/1678237198552184.png "1678172595213178.png")

图 2-6  上传系统信息（HTTPS）

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230308/1678237199382466.png "1678172621722421.png")

图 2-7  POST上传系统信息（HTTPS解密后）

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230308/1678237200876447.png "1678172631100601.png")

图 2-8 自定义加密算法

**2.4 URI生成**

DLL除上线包外使用的URI均随机生成，URI参数数量为1到3个。DLL首先生成第一个随机数用来选择不同的参数，参数列表如下图所示，再生成第二个随机数来决定参数的值，参数值可以是随机字符串，也可以是参数字符串与通信检验的Key加法运算后的数据。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230308/1678237201119824.png "1678172640191410.png")

图 2-9 通信随机选取的部分参数列表图

**2.5 下发后续攻击载荷**

该DLL在使用POST请求上传系统信息后，每分钟向目标URL发送无载荷GET请求，用来获取下阶段攻击载荷。C&C服务器下发的数据也经过了ZIP压缩+自定义加密+Base64编码。该DLL接收到下发的数据后解密，解密后的数据包含URL（用来替换样本通信的URL）以及扩展DLL文件，样本会加载运行下载的扩展DLL，作为下阶段攻击载荷，见图2-1中的④。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230308/1678237202263046.png "1678172650583448.png")

图 2-10 模拟服务器下发后续载荷格式图

**3、总结**

Lazarus组织在该款木马化开源工具中硬编码了多个常见的URL参数字段，发送心跳包时，使用随机数来选择参数、生成参数的值，导致了心跳包长度不固定，弱化了加密通信中的数据长度特征。Lazarus组织使用的C&C服务器为失陷主机，TLS通信证书为失陷主机的正常HTTPS业务证书，从而将攻击流量隐藏到了大量的正常HTTPS访问流量之中，阻碍了研究人员对其服务器特征的收集。但是该款木马化开源工具访问失陷主机的TLS客户端指纹和浏览器正常访问失陷主机的TLS客户端指纹是有较大差异的。另外该工具在请求后续载荷的时候有每分钟1次的心跳行为，虽然心跳包长度并不固定，但是长度是在一定范围内变化的，具有一定流行为特征。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?G2olUxJw)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/portraits/46f5700c82281335cc3d60386789cc75.png)

# [北京观成科技](https://www.4hou.com/member/KrJr)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/KrJr)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

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
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)