---
title: Kraken勒索软件攻击细节曝光 可根据设备性能动态调整加密模式
url: https://www.4hou.com/posts/qozR
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-18
fetch_date: 2025-11-19T03:12:46.016294
---

# Kraken勒索软件攻击细节曝光 可根据设备性能动态调整加密模式

Kraken勒索软件攻击细节曝光 可根据设备性能动态调整加密模式 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Kraken勒索软件攻击细节曝光 可根据设备性能动态调整加密模式

胡金鱼
[技术](https://www.4hou.com/category/technology)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)6253

收藏

导语：Kraken的核心特征是一项罕见能力——通过创建临时文件，在全量数据加密和部分数据加密两种模式间自主选择。

Kraken勒索软件主要针对Windows、Linux/VMware ESXi系统发起攻击，其独特行为是会先对目标设备进行测试，以此确定在不造成系统过载的前提下，数据加密的最快速度。

据思科Talos团队的研究人员介绍，Kraken的核心特征是通过创建临时文件，在全量数据加密和部分数据加密两种模式间自主选择。

该勒索软件于2025年初出现，是HelloKitty勒索软件运营活动的延续，主要以大型企业为攻击目标，通过数据窃取实施“双重勒索”。

在该团伙的泄密网站上，已列出来自美国、英国、加拿大、巴拿马、科威特和丹麦等国家的受害者信息。

Kraken网站上的多处表述，以及赎金通知中的相似内容，均表明其与已停运的HelloKitty勒索软件存在关联。HelloKitty曾在2021年声名鹊起，后因源代码泄露尝试品牌重塑。

除勒索软件运营外，Kraken团伙还推出了一个名为“The Last Haven Board”的新型网络犯罪论坛，号称可提供安全的通信与信息交换服务。

![krakenblog(1).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251117/1763351000203959.jpg "1763350883184140.jpg")

Kraken在暗网上的敲诈门户网站

**Kraken攻击链条**

根据思科的观测，Kraken勒索软件的攻击流程通常如下：

1. 初始渗透：攻击者首先利用暴露在公网的资产中的SMB漏洞发起攻击，获取初始立足点。

2. 权限获取与工具部署：入侵者提取管理员账号凭证，通过远程桌面协议（RDP）重新接入目标环境，并部署Cloudflared和SSHFS工具。

3. 隧道搭建与数据窃取：Cloudflared用于在受害者主机与攻击者基础设施间建立反向隧道，SSHFS则通过挂载远程文件系统实现数据窃取。

4. 横向移动与攻击铺垫：攻击者借助持续存在的Cloudflared隧道和RDP权限，在已入侵网络中横向移动至所有可访问的设备，窃取有价值数据，为部署勒索软件二进制文件做准备。

![Kraken_infection.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251117/1763351003209588.jpg "1763350926148766.jpg")

Kraken感染链

**加密模式动态设定**

研究人员表示，当加密指令发出后，Kraken会对每台目标设备进行性能基准测试：

1. 测试流程：创建含随机数据的临时文件，在计时状态下对其进行加密运算，计算加密效率后删除该临时文件。

2. 模式选择：根据测试结果，勒索软件自动决定对设备数据执行全量加密或部分加密。

![speedcalc.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251117/1763351007577744.jpg "1763350969830744.jpg")

Kraken感染链

3. 设计目的：思科Talos指出，这种设备性能评估机制通常与攻击最后阶段同步快速推进，既能造成最大破坏，又能避免因资源占用过高触发安全警报。

在启动实际加密前，Kraken会删除系统的卷影副本和回收站文件，并停止运行中的备份服务。

**多平台加密模块解析**

**·**Windows版本

思科解释，Windows版Kraken包含四个加密模块：

-SQL数据库模块：通过注册表项识别Microsoft SQL Server实例，定位数据库文件目录并验证路径后，加密SQL数据文件。

-网络共享模块：通过WNet API枚举可访问的网络共享资源，忽略ADMIN$和IPC$共享，加密其他所有可访问共享中的文件。

-本地驱动器模块：扫描可用驱动器盘符，针对可移动磁盘、本地固定磁盘和远程驱动器，通过独立工作线程加密其内容。

-Hyper-V模块：通过内置PowerShell命令列出虚拟机，获取虚拟磁盘路径，强制停止运行中的虚拟机，再加密相关虚拟磁盘文件。

**·**Linux/ESXi版本

该版本会先枚举并强制终止运行中的虚拟机以解锁磁盘文件，随后采用与Windows版相同的基准测试逻辑，执行多线程全量或部分加密。

**攻击善后与赎金要求**

加密完成后，系统会自动执行生成的“bye\_bye.sh”脚本，清除所有日志、Shell历史记录、Kraken勒索软件二进制文件，最终删除脚本本身。

被加密文件会被添加“.zpsc”扩展名，受影响目录中会生成赎金通知文件（文件名“readme\_you\_ws\_hacked.txt”）。

![ransom.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251117/1763351004700528.jpg "1763351004700528.jpg")

Kraken 索赔信

思科透露，在已观测到的案例中，该团伙曾索要100万美元比特币作为赎金。与Kraken勒索软件攻击相关的完整入侵指标（IoCs）可在该GitHub代码库中查询。

文章来源自：https://www.bleepingcomputer.com/news/security/kraken-ransomware-benchmarks-systems-for-optimal-encryption-choice/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?S7PTTlaA)

#### 你可能感兴趣的

* [![]()

  Kraken勒索软件攻击细节曝光 可根据设备性能动态调整加密模式](https://www.4hou.com/posts/qozR)
* [![]()

  XWorm 恶意软件携勒索模块重现 插件数量超 35 个](https://www.4hou.com/posts/W1DW)
* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Kraken勒索软件攻击细节曝光 可根据设备性能动态调整加密模式](https://www.4hou.com/posts/qozR)
  2025-11-18 12:00:00
* [XWorm 恶意软件携勒索模块重现 插件数量超 35 个](https://www.4hou.com/posts/W1DW)
  2025-10-23 12:00:00
* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Kraken勒索软件攻击细节曝光 可根据设备性能动态调整加密模式](https://www.4hou.com/posts/qozR)

  胡金鱼
* [XWorm 恶意软件携勒索模块重现 插件数量超 35 个](https://www.4hou.com/posts/W1DW)

  胡金鱼
* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

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