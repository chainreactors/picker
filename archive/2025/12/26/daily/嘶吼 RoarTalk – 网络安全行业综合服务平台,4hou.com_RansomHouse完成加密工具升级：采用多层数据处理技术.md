---
title: RansomHouse完成加密工具升级：采用多层数据处理技术
url: https://www.4hou.com/posts/kgAr
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-26
fetch_date: 2025-12-27T03:22:50.971688
---

# RansomHouse完成加密工具升级：采用多层数据处理技术

RansomHouse完成加密工具升级：采用多层数据处理技术 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# RansomHouse完成加密工具升级：采用多层数据处理技术

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9182

收藏

导语：RansomHouse是运营时间较长的RaaS平台之一，但攻击规模仍处于中等水平。

RansomHouse勒索软件即服务（RaaS）近期完成了加密工具的升级，将原本相对简单的单阶段线性加密技术，替换为更复杂的多层加密方法。

实际应用中，此次升级带来了更强的加密效果、更快的加密速度，以及在现代目标环境中更稳定的运行表现，让威胁组织在加密完成后的谈判环节拥有更大的筹码。

RansomHouse于2021年12月以数据勒索网络犯罪组织的形式成立，后续在攻击中引入了加密工具，并开发出名为MrAgent的自动化工具，可同时锁定多台VMware ESXi虚拟机监控程序。

此前有报道称，该威胁组织曾针对日本电商巨头Askul公司，同时使用了多款勒索软件家族的工具发起攻击。

根据研究人员发布的新报告显示，最新的加密工具变种代号为“Mario”。

**新型“Mario”加密工具**

RansomHouse的这款最新加密工具变种，将原本的单轮文件数据转换方式，改为基于双密钥的两阶段转换方式——分别使用一个32字节的主密钥与一个8字节的副密钥。

该方式提升了加密的熵值，增加了部分数据恢复的难度。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251222/1766390605838054.png "1766390567125867.png")

Mario生成两个加密密钥

第二项重要升级是引入了新的文件处理策略：以8GB为阈值设置动态数据块大小，同时采用间歇式加密。

由于该策略具备非线性特征、通过复杂算法确定处理顺序，且会根据文件大小采用不同的处理方式，静态分析的难度被大幅提升。

Mario的另一项值得关注的升级是优化了内存布局与缓冲区组织方式，同时提升了复杂度：现在每个加密阶段或功能模块都有独立的专用缓冲区。

最后，与仅会声明任务完成的旧版本相比，升级后的加密工具会输出更详细的文件处理信息。

该新型变种仍以虚拟机文件为攻击目标，会将加密后的文件重命名为带.emario后缀的格式，并在所有受影响的目录中留下勒索信《How To Restore Your Files.txt》。

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251222/1766390615163636.png "1766390615163636.png")

最新RansomHouse变种掉落的赎金信

RansomHouse的加密工具升级情况令人担忧，这标志着“勒索软件发展的危险趋势”：解密难度有所提升，静态分析与逆向工程的难度也进一步加大。

RansomHouse是运营时间较长的RaaS平台之一，但攻击规模仍处于中等水平。其持续开发高级工具的行为，表明该组织采取了更注重攻击效率与规避检测、而非扩大攻击规模的策略，对于人们来说更需警惕对待。

文章来源自：https://www.bleepingcomputer.com/news/security/ransomhouse-upgrades-encryption-with-multi-layered-data-processing/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?KgdqV1mz)

#### 你可能感兴趣的

* [![]()

  RansomHouse完成加密工具升级：采用多层数据处理技术](https://www.4hou.com/posts/kgAr)
* [![]()

  Clop勒索软件发起数据窃取攻击：Gladinet CentreStack成目标](https://www.4hou.com/posts/jBzY)
* [![]()

  新型ConsentFix攻击：借助Azure CLI劫持微软账户](https://www.4hou.com/posts/ZgP2)
* [![]()

  新一轮OAuth钓鱼攻击来袭：微软365账户成攻击目标](https://www.4hou.com/posts/gywZ)
* [![]()

  快手平台深夜遭黑灰产攻击，平台紧急修复并报警](https://www.4hou.com/posts/mkDE)
* [![]()

  新型恶意软件DroidLock锁定安卓设备窃取多类敏感数据](https://www.4hou.com/posts/RXEz)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [RansomHouse完成加密工具升级：采用多层数据处理技术](https://www.4hou.com/posts/kgAr)
  2025-12-26 12:01:00
* [Clop勒索软件发起数据窃取攻击：Gladinet CentreStack成目标](https://www.4hou.com/posts/jBzY)
  2025-12-26 12:00:00
* [新型ConsentFix攻击：借助Azure CLI劫持微软账户](https://www.4hou.com/posts/ZgP2)
  2025-12-25 12:00:00
* [新一轮OAuth钓鱼攻击来袭：微软365账户成攻击目标](https://www.4hou.com/posts/gywZ)
  2025-12-24 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [RansomHouse完成加密工具升级：采用多层数据处理技术](https://www.4hou.com/posts/kgAr)

  胡金鱼
* [Clop勒索软件发起数据窃取攻击：Gladinet CentreStack成目标](https://www.4hou.com/posts/jBzY)

  胡金鱼
* [新型ConsentFix攻击：借助Azure CLI劫持微软账户](https://www.4hou.com/posts/ZgP2)

  胡金鱼
* [新一轮OAuth钓鱼攻击来袭：微软365账户成攻击目标](https://www.4hou.com/posts/gywZ)

  胡金鱼
* [快手平台深夜遭黑灰产攻击，平台紧急修复并报警](https://www.4hou.com/posts/mkDE)

  山卡拉
* [新型恶意软件DroidLock锁定安卓设备窃取多类敏感数据](https://www.4hou.com/posts/RXEz)

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