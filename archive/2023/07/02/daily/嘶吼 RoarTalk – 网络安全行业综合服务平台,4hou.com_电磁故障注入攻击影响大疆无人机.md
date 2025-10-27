---
title: 电磁故障注入攻击影响大疆无人机
url: https://www.4hou.com/posts/9A3z
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-02
fetch_date: 2025-10-04T11:51:22.336517
---

# 电磁故障注入攻击影响大疆无人机

电磁故障注入攻击影响大疆无人机 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 电磁故障注入攻击影响大疆无人机

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-07-01 11:50:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)130024

收藏

导语：​电磁故障注入攻击大疆无人机固件更新过程，可接管无人机。

电磁故障注入攻击大疆无人机固件更新过程，可接管无人机。

近日，IOActive研究人员发布白皮书分析了无人机行业的安全态势。IOActive研究人员探索使用非入侵的方式在商用无人机上实现代码执行，比如电磁侧信道攻击和电磁故障注入攻击。

**无人机攻击面分析**

无人广泛应用于各个领域，如军事、商业。与其他技术一样，无人机也易受到各种类型的攻击。无人机的攻击面包括：（1）后端、（2）移动端、（3）无线频谱通信、（4）物理设备。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230629/1688023811613810.png "1688023712443491.png")

图 无人机攻击面

**电磁故障注入攻击**

考虑到非入侵的攻击本质，IOActive使用电磁辐射和电磁故障注入来实现攻击。在研究中，主要使用Riscure作为工具。

第一个方法是使用电磁辐射来窃取加密密钥，并解密固件。首先，使用强电磁辐射信号来找到无人机的PCB区域，以放置探针和记录信息以提取密钥。在获取最强信号位置后，研究人员分析如何绕过固件的签名验证。经过大量的测试和数据分析，研究人员发现绕过签名的成功率小于0.5%。因此，密钥恢复的可能性很小，无法用于现实攻击中。

第二个方法是使用电磁故障注入。Riscure提出使用glitch来使得一个指令变成另一个指令，并获得PC寄存器的控制权限。下图是攻击环境搭建：包括一个笔记本电脑、一个电源、Riscure Spider、示波器、电磁故障注入脉冲生成器。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230629/1688023812170006.png "1688023772155710.png")

图 攻击环境

在识别PCB上的区域后，研究人员修改的glitch的形状后，就可以得到成功的结果。目标进程被破坏，Payload出现在多个寄存器中。下图是分段错误发生的指令：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230629/1688023811165492.png "1688023811165492.png")

成功引发内存破坏后，下一步就是设计payload来实现代码执行。攻击者使用这样的漏洞利用可以完全控制目标设备、泄露所有敏感内容、实现ADB访问和泄露加密密钥。

白皮书下载地址：https://ioac.tv/3N005Bn

本文翻译自：https://labs.ioactive.com/2023/06/applying-fault-injection-to-firmware.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Q3ENbyjG)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/e7OO)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

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