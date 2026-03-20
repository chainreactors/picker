---
title: 警惕！“养虾”邮件攻击｜一封邮件就让AI沦为黑客
url: https://www.4hou.com/posts/QX35
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-03-19
fetch_date: 2026-03-20T04:07:12.442050
---

# 警惕！“养虾”邮件攻击｜一封邮件就让AI沦为黑客

警惕！“养虾”邮件攻击｜一封邮件就让AI沦为黑客 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 警惕！“养虾”邮件攻击｜一封邮件就让AI沦为黑客

CACTER
[行业](https://www.4hou.com/category/industry)
2026-03-19 11:44:44

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)6467

收藏

导语：你的 “龙虾” 是效率神器还是内鬼？ 龙虾失控 = 邮箱失守，企业邮箱风险剧增！

最近IT圈最火的是什么？不是新手机，不是新显卡，而是"养龙虾"。这只被称为“龙虾”的OpenClaw之所以刷屏，核心是能落地干活——自动发邮件、查资料、操作本地文件，高效又省心。

就在大家争相"领养"时，国家安全部和央视新闻接连拉响警报：这只“能干的龙虾”，很可能变成偷机密的“内鬼”。更值得警惕的是，攻击者甚至不用入侵系统，只需发一封精心设计的邮件，诱导AI执行操作，在不知不觉中把企业敏感信息外发！

![图片1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20260319/1773888499198159.jpg "1773888499198159.jpg")

**一、一封邮件，如何让AI成为“帮凶”？**

在实际使用中，很多企业为提升效率，会给OpenClaw开放更高权限，如访问邮箱、读取文件、自动执行任务等。但也正因如此，**一旦被“利用”，AI可能在“看似正常”的流程中执行异常操作**。而邮件，正是最容易被利用的入口之一。

下面，我们用两起真实案例，看看风险是如何发生的：

**案例1：AI狂删200多封邮件，权限失控=项目停摆**

Meta安全总监Summer Yue，为提升效率给OpenClaw开放全部邮箱权限，本以为设置了安全指令就能高枕无忧，最终AI无视所有叫停指令，疯狂删除邮件。

问题出在哪？：

① 大模型有上下文上限，处理海量邮件时，核心安全指令被冲散

② OpenClaw为追求效率，缺乏强安全设计，默认开放极高权限，相当于“无底线放权”。

后果：200多封核心邮件永久丢失（含合作方案、项目资料），团队花80多小时补救无果，直接导致两个核心项目延误，损失无法挽回。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260319/1773888524804406.png "1773888524804406.png")

**案例2：邮件注入AI提示词陷阱，未点开即被偷密钥**

Archestra.AI的CEO Matvey Kukuy，公开模拟攻击过程——黑客给员工发普通邮件，员工全程未点开，企业核心私钥却被悄悄偷走。

攻击原理：

① 黑客在邮件正文隐藏攻击脚本

② 员工将OpenClaw设为“自动读件回复”，AI误将脚本当系统指令

② 触发“提示词注入”漏洞，攻击从“代码注入”变成“语言催眠”，AI分不清指令与普通内容，盲目执行。

危害：5分钟内，AI按黑客指令搜索私钥、打包发送，员工毫无察觉；企业核心机密泄露，面临致命安全危机。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260319/1773888524804406.png "1773888524804406.png")

**二、国家安全部出手：“龙虾”到底该怎么养？**

针对OpenClaw的邮件安全隐患，国家安全部专门发布“养虾指南”，给所有邮件安全管理员、IT从业者，划出3条红线：：

**1. 全面体检，排查隐患：**重点检查OpenClaw控制界面是否暴露公网、权限是否过高、凭证是否泄露、插件来源是否可信，有严重风险立即隔离、下线。

**2. 严控权限，强化防护：**遵循“最小权限”原则，不让AI接触核心邮件和敏感数据；加密敏感数据、做好操作日志，尽量在隔离环境运行。

**3. 理性使用，不盲跟风：**别把OpenClaw当“玩具”，明确其“数字员工”定位，在合规、安全、可控的前提下使用，避免因小失大。

**三、企业进阶防护：防不住邮件威胁，就别谈安心“养虾”**

**邮件是攻击者利用AI入侵企业的主要入口，企业仅靠规范“养虾”不够，必须上一道“技术锁”才能将风险牢牢防住**。对此，CACTER给出了一套双保险"防护组合:

**第一招：入口拦截，识别“催眠指令”**

OpenClaw的核心漏洞之一是“提示词注入”，攻击者会将恶意指令伪装成普通内容藏在邮件正文中，AI读取后误以为是系统命令，从而被执行，进而引发安全风险。

针对这一问题，CACTER大模型邮件安全网关内置语义深度理解能力，专门针对这类AI“催眠指令”进行检测，能精准识别邮件中隐藏的“越权请求”、“敏感路径探测”、“外发文件”等风险意图。一旦检测到此类内容，直接在入口处拦截，从根源上阻止攻击脚本触达邮箱内部。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260319/1773888524804406.png "1773888524804406.png")

**第二招：出口管控，防止数据外泄**

如果OpenClaw已被“策反”，开始打包机密往外发送，CACTER EDLP会守住最后一道防线。它不受发件人限制——**无论是员工手动发件，还是AI自动发件，只要邮件中包含“密钥”、“合同”、“源代码”等敏感内容，系统立即检测并阻断，确保数据无法流出企业**。

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260319/1773888535212034.png "1773888535212034.png")

OpenClaw带来的办公便利不可否认，但其安全漏洞带来的邮件安全、数据安全风险更不容忽视，国家安全部的警示绝非危言耸听。对邮件安全管理员、IT从业者而言，规范“养虾”是前提，专业防护是关键。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Hk5AZyaJ)

#### 你可能感兴趣的

* [![]()

  警惕！“养虾”邮件攻击｜一封邮件就让AI沦为黑客](https://www.4hou.com/posts/QX35)
* [![]()

  360龙虾卫士上线：九大能力专治OpenClaw“裸奔”](https://www.4hou.com/posts/OG1E)
* [![]()

  企业邮箱防钓鱼攻击：邮件安全网关的3大核心技术](https://www.4hou.com/posts/LGXv)
* [![]()

  新窃密技术预警：现代光学鼠标窃密](https://www.4hou.com/posts/Aryj)
* [![]()

  杰克·伦敦的另一面 | 匪夷所思](https://www.4hou.com/posts/zA02)
* [![]()

  再获认可！梆梆安全蝉联中金联盟 “2025年度优秀会员单位” ，以反诈创新赋能行业实践](https://www.4hou.com/posts/EyNl)

![](https://img.4hou.com/portraits/789873803bbe1d5cf9b06a0859e2af0b.png)

# [CACTER](https://www.4hou.com/member/64Y9)

国内领先企业级邮件安全解决方案提供商，提供一站式防护。

#### 最新文章

* [警惕！“养虾”邮件攻击｜一封邮件就让AI沦为黑客](https://www.4hou.com/posts/QX35)
  2026-03-19 11:44:44
* [360龙虾卫士上线：九大能力专治OpenClaw“裸奔”](https://www.4hou.com/posts/OG1E)
  2026-03-18 14:49:39
* [企业邮箱防钓鱼攻击：邮件安全网关的3大核心技术](https://www.4hou.com/posts/LGXv)
  2026-03-17 17:26:09
* [新窃密技术预警：现代光学鼠标窃密](https://www.4hou.com/posts/Aryj)
  2026-03-17 14:56:40

[查看更多](https://www.4hou.com/member/64Y9)

# 相关热文

* [警惕！“养虾”邮件攻击｜一封邮件就让AI沦为黑客](https://www.4hou.com/posts/QX35)

  CACTER
* [360龙虾卫士上线：九大能力专治OpenClaw“裸奔”](https://www.4hou.com/posts/OG1E)

  企业资讯
* [企业邮箱防钓鱼攻击：邮件安全网关的3大核心技术](https://www.4hou.com/posts/LGXv)

  CACTER
* [新窃密技术预警：现代光学鼠标窃密](https://www.4hou.com/posts/Aryj)

  RC2反窃密实验室
* [杰克·伦敦的另一面 | 匪夷所思](https://www.4hou.com/posts/zA02)

  RC2反窃密实验室
* [再获认可！梆梆安全蝉联中金联盟 “2025年度优秀会员单位” ，以反诈创新赋能行业实践](https://www.4hou.com/posts/EyNl)

  梆梆安全

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