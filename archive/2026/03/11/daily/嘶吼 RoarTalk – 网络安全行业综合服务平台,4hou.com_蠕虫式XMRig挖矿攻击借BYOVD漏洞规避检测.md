---
title: 蠕虫式XMRig挖矿攻击借BYOVD漏洞规避检测
url: https://www.4hou.com/posts/kgyK
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-03-11
fetch_date: 2026-03-12T04:07:00.955172
---

# 蠕虫式XMRig挖矿攻击借BYOVD漏洞规避检测

蠕虫式XMRig挖矿攻击借BYOVD漏洞规避检测 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 蠕虫式XMRig挖矿攻击借BYOVD漏洞规避检测

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2026-03-11 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)6119

收藏

导语：该XMRig变种还包含蠕虫模块，可通过U盘传播，而非仅依靠手动下载。

一场具备蠕虫传播能力的加密货币劫持攻击，正通过盗版软件进行传播，利用BYOVD漏洞部署定制版XMRig挖矿程序。

研究人员发现，该攻击通过捆绑盗版软件传播，投放定制化XMRig挖矿木马。攻击借助BYOVD漏洞利用时间触发逻辑炸弹实现规避检测、最大化挖矿收益。其多阶段感染链以提升加密货币算力为核心，过程中常导致受感染系统运行不稳定。

该攻击通过盗版“付费”软件安装程序传播，释放基于XMRig的复杂挖矿木马。其核心是名为Explorer.exe的控制程序，该程序以持久化状态机形式运行，可通过命令行参数切换角色：安装器、守护程序、主动感染、清理程序。

据了解，Explorer.exe是整个感染流程的核心调度节点。在传统恶意软件设计中，功能通常被拆分为线性执行流程：下载器下载载荷、运行、退出。而Explorer.exe控制程序则以持久化状态机运行。

它根据运行时传入的命令行参数决定行为模式，使单个文件在感染生命周期中承担多种不同角色：安装程序、守护程序、载荷管理器、清理程序。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260225/1771990688144441.png "1771990688144441.png")

该恶意软件将控制逻辑（“大脑”）与载荷（“执行体”）分离，后者包括挖矿程序、守护程序以及用于获取内核权限的漏洞驱动（BYOVD）。

恶意软件滥用一款名为WinRing0x64.sys的合法但存在漏洞的驱动，该技术被称为BYOVD（自带漏洞驱动）。它无需创建恶意驱动，只需加载此老旧但已签名的驱动，即可获得内核级（Ring 0）权限。

获取权限后，它会修改特定 CPU 配置（型号专用寄存器），禁用干扰门罗币RandomX挖矿算法的硬件预取器。由于RandomX依赖随机内存访问，关闭这些功能可减少缓存冲突，将挖矿性能提升15%～50%。

各类载荷被内嵌在程序资源段中，经解压后以隐藏系统文件形式写入磁盘，并伪装成合法软件。

一套环形守护机制确保组件被终止后会互相重启，强行恢复挖矿，甚至会杀死正常的Windows资源管理器进程干扰用户操作。

该恶意软件内置时间触发自杀开关，截止时间为2025年12月23日，到期后将执行可控清理逻辑。

研究人员在sub\_14000D180函数中发现了一个硬编码时间检测逻辑，充当“自杀开关”或“时间炸弹”。该机制获取系统本地时间，并与预设截止日期2025年12月23日对比：

**·**活跃阶段（2025年12月23日之前）：执行标准感染流程，安装持久化模块并启动挖矿。

**·**过期阶段（2025年12月23日之后）：表明该攻击并非长期持续运营，而是“发射后不管”的生命周期。时间点可能与租用的C2基础设施到期、加密货币市场预期变动（特别是门罗币难度调整），或计划切换新版本恶意软件有关。

该XMRig变种还包含蠕虫模块，可通过U盘传播，而非仅依靠手动下载。它通过Windows系统通知静默监听新插入的可移动设备，而非持续轮询扫描。

当U盘插入时，恶意软件会将自身explorer.exe复制到设备中，隐藏在文件夹内，并创建伪装成磁盘图标的恶意快捷方式。当该U盘在其他电脑上打开时，快捷方式即可执行恶意程序，实现进一步扩散。

恶意分子似乎先在小范围系统中测试感染链与持久化功能（包括名为“Barusu”的自杀开关），随后再扩大规模。

根据相关数据显示，曾有一个活跃节点以中等算力运行，2025年11月活动零星，12月8日起出现明显增长，表明新一轮投放或新感染节点被激活。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260225/1771990736171105.png "1771990736171105.png")

该攻击事件的发生正提醒人们，常规恶意软件仍在持续进化。攻击者将社会工程、伪装合法软件、蠕虫式传播、内核级漏洞利用结合，打造出高抗性、高效率的僵尸网络。尤其是BYOVD技术的使用，凸显出现代操作系统安全模型中的一个关键弱点：对已签名驱动的过度信任。

文章来源自：https://securityaffairs.com/188388/malware/wormable-xmrig-campaign-leverages-byovd-and-timed-kill-switch-for-stealth.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?UsRow0du)

#### 你可能感兴趣的

* [![]()

  蠕虫式XMRig挖矿攻击借BYOVD漏洞规避检测](https://www.4hou.com/posts/kgyK)
* [![]()

  谷歌API密钥安全漏洞曝光：前端暴露密钥可直接访问Gemini并窃取隐私数据](https://www.4hou.com/posts/kgyv)
* [![]()

  思科Catalyst SD-WAN严重认证绕过漏洞遭长期入侵，可植入恶意节点控制网络](https://www.4hou.com/posts/vwNM)
* [![]()

  多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险](https://www.4hou.com/posts/mkAn)
* [![]()

  黑客利用 React Native Metro 高危漏洞入侵开发者系统](https://www.4hou.com/posts/DxG5)
* [![]()

  vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码](https://www.4hou.com/posts/qoOk)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [蠕虫式XMRig挖矿攻击借BYOVD漏洞规避检测](https://www.4hou.com/posts/kgyK)
  2026-03-11 12:00:00
* [谷歌API密钥安全漏洞曝光：前端暴露密钥可直接访问Gemini并窃取隐私数据](https://www.4hou.com/posts/kgyv)
  2026-03-02 11:49:21
* [思科Catalyst SD-WAN严重认证绕过漏洞遭长期入侵，可植入恶意节点控制网络](https://www.4hou.com/posts/vwNM)
  2026-02-28 12:00:00
* [多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险](https://www.4hou.com/posts/mkAn)
  2026-02-27 11:59:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [蠕虫式XMRig挖矿攻击借BYOVD漏洞规避检测](https://www.4hou.com/posts/kgyK)

  胡金鱼
* [谷歌API密钥安全漏洞曝光：前端暴露密钥可直接访问Gemini并窃取隐私数据](https://www.4hou.com/posts/kgyv)

  胡金鱼
* [思科Catalyst SD-WAN严重认证绕过漏洞遭长期入侵，可植入恶意节点控制网络](https://www.4hou.com/posts/vwNM)

  胡金鱼
* [多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险](https://www.4hou.com/posts/mkAn)

  胡金鱼
* [黑客利用 React Native Metro 高危漏洞入侵开发者系统](https://www.4hou.com/posts/DxG5)

  胡金鱼
* [vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码](https://www.4hou.com/posts/qoOk)

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