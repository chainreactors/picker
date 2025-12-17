---
title: 勒索软件团伙滥用Shanya可执行文件打包器隐匿EDR禁用工具
url: https://www.4hou.com/posts/GApr
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-16
fetch_date: 2025-12-17T03:17:45.809095
---

# 勒索软件团伙滥用Shanya可执行文件打包器隐匿EDR禁用工具

勒索软件团伙滥用Shanya可执行文件打包器隐匿EDR禁用工具 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 勒索软件团伙滥用Shanya可执行文件打包器隐匿EDR禁用工具

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8926

收藏

导语：目前已确认使用该服务的勒索软件团伙包括Medusa、Qilin、Crytox及Akira，其中Akira是该打包服务的最频繁使用者。

多个勒索软件团伙正借助一款名为Shanya的打包即服务平台，为其恶意载荷进行封装，以便在受害设备上禁用终端检测与响应解决方案。

打包服务可为网络犯罪分子提供专用工具，其核心作用是对恶意载荷进行封装处理，通过混淆恶意代码的方式，规避多数主流安全工具及杀毒引擎的检测。

据Sophos Security的遥测数据显示，Shanya打包服务于2024年末开始出现，此后使用率大幅攀升，采用该服务的恶意软件样本已在突尼斯、阿联酋、哥斯达黎加、尼日利亚、巴基斯坦等国被监测到。

目前已确认使用该服务的勒索软件团伙包括Medusa、Qilin、Crytox及Akira，其中Akira是该打包服务的最频繁使用者。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251210/1765352473258701.png "1765352361683851.png")

在勒索软件攻击中使用的Shanya打包器

**Shanya打包服务的工作机制**

威胁者需先将其恶意载荷提交至Shanya平台，平台会返回经定制化封装的“打包版”载荷，该过程会同时采用加密与压缩技术。

该服务主打生成载荷的唯一性，其宣传内容强调自身具备非标准模块内存加载、系统加载器桩函数独立封装能力，且每位客户在购买后，均可获得专属（相对）独立的桩函数及独特的加密算法。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251210/1765352478168574.png "1765352433700067.png")

加载器中的垃圾代码

具体来看，恶意载荷会被植入Windows系统DLL文件shell32.dll的内存映射副本中。尽管该DLL文件的可执行区段与文件大小看似合规，文件路径也无异常，但其文件头与.text区段已被解密后的恶意载荷覆盖。

值得注意的是，载荷在打包文件内处于加密状态，而在执行阶段，它会在内存中完成解密与解压，随后直接注入shell32.dll副本，全程不会写入磁盘，以此降低被检测的概率。

研究人员还发现，Shanya会通过在无效上下文下调用RtlDeleteFunctionTable函数，对终端检测与响应解决方案进行探测。这一操作会在用户态调试器环境中触发未处理异常或程序崩溃，从而在载荷完全执行前干扰自动化分析流程。

**对EDR系统的禁用流程**

勒索软件团伙通常会在攻击的数据窃取与加密阶段前，先禁用目标设备上运行的EDR工具，其执行流程一般通过DLL侧加载实现：将合法Windows可执行文件（如consent.exe）与经Shanya打包的恶意DLL（如msimg32.dll、version.dll、rtworkq.dll或wmsgapi.dll）进行组合加载。

根据Sophos的分析，这款EDR禁用工具会释放两款驱动程序：

1.  一款是由TechPowerUp签名的合法驱动ThrottleStop.sys（又称rwdrv.sys），该驱动存在可实现任意内核内存写入的漏洞；

2.  另一款是未签名的hlpdrv.sys驱动。其中，签名驱动用于实现权限提升，而hlpdrv.sys则会根据用户态下发的指令，对各类安全产品实施禁用操作。其用户态组件会先枚举当前运行的进程及已安装的服务，再将结果与内置的庞大硬编码列表进行比对，一旦匹配成功，便会向恶意内核驱动发送“终止”指令。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251210/1765352486150425.png "1765352486150425.png")

目标服务的部分列表

除了专注于禁用EDR的勒索软件操作者外，研究人员近期还监测到ClickFix攻击活动也在利用Shanya服务对CastleRAT远控木马进行封装。勒索软件团伙往往依赖打包服务来实现EDR禁用工具的隐蔽部署。

文章来源自：https://www.bleepingcomputer.com/news/security/ransomware-gangs-turn-to-shanya-exe-packer-to-hide-edr-killers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?DTZ26Jwi)

#### 你可能感兴趣的

* [![]()

  勒索软件团伙滥用Shanya可执行文件打包器隐匿EDR禁用工具](https://www.4hou.com/posts/GApr)
* [![]()

  新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户](https://www.4hou.com/posts/jBoY)
* [![]()

  Predator间谍软件采用新型攻击载体实施零点击攻击](https://www.4hou.com/posts/yzKz)
* [![]()

  AI安全元年 | 盘点2025年AI与安全的“相爱相杀”](https://www.4hou.com/posts/Eynm)
* [![]()

  勒索软件利用EDR工具隐秘执行恶意代码](https://www.4hou.com/posts/KGwl)
* [![]()

  Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露](https://www.4hou.com/posts/gylZ)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [勒索软件团伙滥用Shanya可执行文件打包器隐匿EDR禁用工具](https://www.4hou.com/posts/GApr)
  2025-12-16 12:00:00
* [新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户](https://www.4hou.com/posts/jBoY)
  2025-12-15 12:00:00
* [Predator间谍软件采用新型攻击载体实施零点击攻击](https://www.4hou.com/posts/yzKz)
  2025-12-12 12:00:00
* [AI安全元年 | 盘点2025年AI与安全的“相爱相杀”](https://www.4hou.com/posts/Eynm)
  2025-12-11 14:17:49

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [勒索软件团伙滥用Shanya可执行文件打包器隐匿EDR禁用工具](https://www.4hou.com/posts/GApr)

  胡金鱼
* [新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户](https://www.4hou.com/posts/jBoY)

  胡金鱼
* [Predator间谍软件采用新型攻击载体实施零点击攻击](https://www.4hou.com/posts/yzKz)

  胡金鱼
* [AI安全元年 | 盘点2025年AI与安全的“相爱相杀”](https://www.4hou.com/posts/Eynm)

  山卡拉
* [勒索软件利用EDR工具隐秘执行恶意代码](https://www.4hou.com/posts/KGwl)

  胡金鱼
* [Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露](https://www.4hou.com/posts/gylZ)

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