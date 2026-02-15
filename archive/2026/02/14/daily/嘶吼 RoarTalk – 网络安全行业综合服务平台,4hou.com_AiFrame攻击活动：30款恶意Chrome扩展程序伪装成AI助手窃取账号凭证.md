---
title: AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证
url: https://www.4hou.com/posts/5M6A
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-14
fetch_date: 2026-02-15T04:25:32.758200
---

# AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证

AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-02-14 11:59:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10788

收藏

导语：研究人员发现这一恶意扩展攻击活动后将其命名为 AiFrame。

超30万的用户安装了共计30 款的恶意 Chrome 浏览器扩展程序，它们伪装成AI助手形式以窃取用户账号凭证、邮件内容与浏览信息。其中部分扩展目前仍上架于 Chrome 应用商店，另有部分扩展安装量相对较小。

研究人员发现这一恶意扩展攻击活动后将其命名为 AiFrame。经分析，所有涉事扩展均归属同一攻击团伙控制，为同一域名 tapnetic.pro 下的攻击基础设施通信。

据研究人员介绍，AiFrame 活动中最流行的扩展为 Gemini AI Sidebar（ID：fppbiomdkfbhgjjdmojlogeceejinadg），用户量达 8 万，目前已从 Chrome 应用商店下架。

但仍有多款用户量达数千的同类恶意扩展继续留在谷歌 Chrome 扩展商店中。值得注意的是，这些扩展名称可能不同，但核心标识一致，包括：

**·**AI Sidebar（gghdfkafnhfpaooiolhncejnlgglhkhe）——7 万用户

**·**AI Assistant（nlhpidbjmmffhoogcennoiopekbiglbp）——6 万用户

**·**ChatGPT Translate（acaeafediijmccnjlokgcdiojiljfpbe）——3 万用户

**·**AI GPT（kblengdlefjpjkekanpoidgoghdngdgl）——2 万用户

**·**ChatGPT（llojfncgbabajmdglnkbhmiebiinohek）——2 万用户

**·**AI Sidebar（djhjckkfgancelbmgcamjimgphaphjdl）——1 万用户

**·**Google Gemini（fdlagfnfaheppaigholhoojabfaapnhb）——1 万用户

研究人员指出，30 款扩展共用相同的内部结构、JavaScript 逻辑、权限配置与后端基础设施。

这些恶意浏览器插件并未在本地实现任何 AI 功能，而是通过全屏 iframe 加载远程域名内容，以此对外提供所谓“AI 服务”。

这种模式本身就存在极高风险：攻击者可随时修改扩展逻辑，无需推送更新即可改变行为（类似微软 Office 插件机制），从而绕过应用商店的重新审核。

在后台，这些扩展利用 Mozilla 的 Readability 库，从用户访问的网页中提取内容，包括敏感的登录认证页面。其中15 款扩展专门针对 Gmail 数据，通过在 mail.google.com 页面加载阶段（document\_start）运行专用脚本并注入界面元素，实现窃取行为。

该脚本直接从 DOM 读取可见邮件内容，并通过 .textContent 持续提取邮件会话文本。研究人员强调，even 邮件草稿也可被完整窃取。

当用户触发 AI 辅助回复、摘要生成等 Gmail 相关功能时，提取到的邮件内容会传入扩展逻辑，并上传至攻击者控制的第三方后端服务器。这将导致邮件正文及相关上下文数据被传出设备，脱离 Gmail 安全边界，上传至远程服务器。

这些扩展还内置远程触发的语音识别与转录功能，通过 Web Speech API 实现录音并回传结果。根据获取的权限不同，扩展甚至可以窃取受害者所处环境的对话内容。

研究人员为此发出安全建议：建议用户及时进行自查，如确认设备已被感染，应立即重置所有账号密码。

文章来源自：https://www.bleepingcomputer.com/news/security/fake-ai-chrome-extensions-with-300k-users-steal-credentials-emails/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ik5NwLrT)

#### 你可能感兴趣的

* [![]()

  新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信](https://www.4hou.com/posts/VWYO)
* [![]()

  AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证](https://www.4hou.com/posts/5M6A)
* [![]()

  AI真的能取代人类吗？提升效率利用AI辅助写代码，真的靠谱吗？](https://www.4hou.com/posts/1M2G)
* [![]()

  2025年全球加密货币网络犯罪激增，黑客与勒索攻击事件持续高发](https://www.4hou.com/posts/EyJ4)
* [![]()

  黑客团伙滥用Hugging Face平台传播数千款安卓恶意软件变种](https://www.4hou.com/posts/wxXz)
* [![]()

  八问+一图，读懂《汽车数据出境安全指引（2026版）》](https://www.4hou.com/posts/MXRR)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信](https://www.4hou.com/posts/VWYO)
  2026-02-14 12:00:00
* [AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证](https://www.4hou.com/posts/5M6A)
  2026-02-14 11:59:00
* [AI真的能取代人类吗？提升效率利用AI辅助写代码，真的靠谱吗？](https://www.4hou.com/posts/1M2G)
  2026-02-13 12:01:00
* [2025年全球加密货币网络犯罪激增，黑客与勒索攻击事件持续高发](https://www.4hou.com/posts/EyJ4)
  2026-02-11 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信](https://www.4hou.com/posts/VWYO)

  胡金鱼
* [AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证](https://www.4hou.com/posts/5M6A)

  胡金鱼
* [AI真的能取代人类吗？提升效率利用AI辅助写代码，真的靠谱吗？](https://www.4hou.com/posts/1M2G)

  山卡拉
* [2025年全球加密货币网络犯罪激增，黑客与勒索攻击事件持续高发](https://www.4hou.com/posts/EyJ4)

  胡金鱼
* [黑客团伙滥用Hugging Face平台传播数千款安卓恶意软件变种](https://www.4hou.com/posts/wxXz)

  胡金鱼
* [八问+一图，读懂《汽车数据出境安全指引（2026版）》](https://www.4hou.com/posts/MXRR)

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