---
title: ClickFix 攻击借仿冒 Windows 更新界面推送恶意软件
url: https://www.4hou.com/posts/RX30
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-27
fetch_date: 2025-11-28T03:12:19.376082
---

# ClickFix 攻击借仿冒 Windows 更新界面推送恶意软件

ClickFix 攻击借仿冒 Windows 更新界面推送恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/loginIng)
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

# ClickFix 攻击借仿冒 Windows 更新界面推送恶意软件

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9625

收藏

导语：由于攻击成功率极高，ClickFix已被各层级网络犯罪分子广泛采用，且不断迭代进化，所用诱骗手段的技术复杂度与迷惑性也日益提升。

研究人员发现，ClickFix攻击出现新变体：攻击者通过全屏浏览器页面展示高度逼真的Windows更新动画诱骗用户，并将恶意代码隐藏在图像文件内。

ClickFix本质是一种社会工程学攻击，其核心手法是诱使用户在Windows命令提示符中粘贴并执行特定代码或指令，最终导致恶意软件在目标系统中运行。

由于攻击成功率极高，ClickFix已被各层级网络犯罪分子广泛采用，且不断迭代进化，所用诱骗手段的技术复杂度与迷惑性也日益提升。

**全屏浏览器页面的诱骗逻辑**

自10月1日起，研究人员观察到ClickFix攻击的两种主要诱骗借口：一是谎称“需完成关键Windows安全更新的安装”，二是更常见的“人机验证”。

虚假更新页面会引导受害者按特定顺序按下快捷键，而这些操作会自动粘贴并执行攻击者预设的指令——此前攻击者已通过页面中运行的JavaScript代码，将恶意指令复制到用户系统剪贴板。

![ClickFix_attack.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251125/1764041832519701.png "1764041303480597.png")

假的Windows安全更新屏幕

托管安全服务提供商Huntress发布的报告指出，这些ClickFix新变体最终会释放LummaC2与Rhadamanthys两款信息窃取恶意软件。

具体来看，其中一种攻击变体使用“人机验证”页面作为诱饵，另一种则依托仿冒的Windows更新界面；但无论采用哪种方式，攻击者均通过隐写术将最终的恶意软件载荷编码隐藏在图像文件中。

攻击者并非简单地将恶意数据附加到文件中，而是将恶意代码直接编码到PNG图像的像素数据内，借助特定颜色通道在内存中重构并解密恶意载荷。

**恶意载荷的投递与执行流程**

恶意载荷的投递始于调用Windows原生二进制文件mshta.exe，通过该程序执行恶意JavaScript代码。

整个攻击过程分为多个阶段，涉及PowerShell代码与一个.NET程序集（即“隐写加载器”Stego Loader）——后者负责将加密状态下隐藏在PNG文件中的最终恶意载荷重构出来。

在Stego Loader的清单资源中，存在一个AES加密的数据块，该数据块本质是一个隐写PNG文件，其中包含的shellcode（外壳代码）需通过自定义C#代码进行重构。

研究人员还发现，攻击者采用了一种名为“ctrampoline”的动态规避技术：入口点函数会调用10000个空函数，以此干扰安全检测。

![trampoline.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251125/1764041835146249.jpg "1764041340717407.jpg")

Trampoline调用链

隐藏信息窃取恶意软件的shellcode从加密图像中提取后，会通过Donut工具进行加壳处理——该工具支持在内存中直接执行VBScript、JScript、EXE、DLL文件及.NET程序集，进一步提升攻击隐蔽性。

脱壳完成后，Huntress研究人员成功提取出恶意软件，在此次分析的攻击案例中，涉及的正是LummaC2与Rhadamanthys。

下图直观展示了整个攻击流程的技术细节：

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251125/1764041838334398.png "1764041544156999.png")

攻击概述

**攻击溯源与执法干预**

早在10月，研究人员就已发现采用“Windows更新”诱饵的Rhadamanthys攻击变体；随后在11月13日，Operation Endgame执法行动摧毁了该恶意软件的部分基础设施。

Huntress报告指出，此次执法行动的直接成效是：尽管仿冒Windows更新的恶意域名仍处于活跃状态，但已无法再投递恶意载荷。

为防范此类ClickFix攻击，研究人员建议采取两项核心防护措施：一是禁用Windows“运行”对话框；二是监控可疑进程链，例如“explorer.exe衍生出mshta.exe”或“explorer.exe衍生出PowerShell”的异常进程关系。

此外，在调查网络安全事件时，分析人员可检查“RunMRU”注册表项——该注册表项会记录用户在Windows“运行”对话框中输入过的指令，可为攻击溯源提供关键线索。

文章来源自：https://www.bleepingcomputer.com/news/security/clickfix-attack-uses-fake-windows-update-screen-to-push-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?GEDa3fLF)

#### 你可能感兴趣的

* [![]()

  ClickFix 攻击借仿冒 Windows 更新界面推送恶意软件](https://www.4hou.com/posts/RX30)
* [![]()

  九国联合行动摧毁千余台恶意软件服务器](https://www.4hou.com/posts/xyKn)
* [![]()

  “ShadowRay 2.0”全球攻击活动：利用旧漏洞劫持Ray集群构建自传播挖矿僵尸网络](https://www.4hou.com/posts/J13l)
* [![]()

  Cloudflare将本周大规模服务中断事件归咎于数据库问题](https://www.4hou.com/posts/MX3B)
* [![]()

  公安部计算机信息系统安全产品质量监督检验中心检测发现40款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/Dx3Y)
* [![]()

  Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具](https://www.4hou.com/posts/omLN)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [ClickFix 攻击借仿冒 Windows 更新界面推送恶意软件](https://www.4hou.com/posts/RX30)
  2025-11-27 12:00:00
* [九国联合行动摧毁千余台恶意软件服务器](https://www.4hou.com/posts/xyKn)
  2025-11-25 12:00:00
* [“ShadowRay 2.0”全球攻击活动：利用旧漏洞劫持Ray集群构建自传播挖矿僵尸网络](https://www.4hou.com/posts/J13l)
  2025-11-24 12:00:00
* [Cloudflare将本周大规模服务中断事件归咎于数据库问题](https://www.4hou.com/posts/MX3B)
  2025-11-21 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [ClickFix 攻击借仿冒 Windows 更新界面推送恶意软件](https://www.4hou.com/posts/RX30)

  胡金鱼
* [九国联合行动摧毁千余台恶意软件服务器](https://www.4hou.com/posts/xyKn)

  胡金鱼
* [“ShadowRay 2.0”全球攻击活动：利用旧漏洞劫持Ray集群构建自传播挖矿僵尸网络](https://www.4hou.com/posts/J13l)

  胡金鱼
* [Cloudflare将本周大规模服务中断事件归咎于数据库问题](https://www.4hou.com/posts/MX3B)

  胡金鱼
* [公安部计算机信息系统安全产品质量监督检验中心检测发现40款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/Dx3Y)

  胡金鱼
* [Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具](https://www.4hou.com/posts/omLN)

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