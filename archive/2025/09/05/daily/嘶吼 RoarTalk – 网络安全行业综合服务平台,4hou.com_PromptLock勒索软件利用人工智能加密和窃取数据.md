---
title: PromptLock勒索软件利用人工智能加密和窃取数据
url: https://www.4hou.com/posts/xyMr
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-05
fetch_date: 2025-10-02T19:40:23.067770
---

# PromptLock勒索软件利用人工智能加密和窃取数据

PromptLock勒索软件利用人工智能加密和窃取数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# PromptLock勒索软件利用人工智能加密和窃取数据

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-09-04 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)49388

收藏

导语：该恶意软件借助Lua脚本，可在Windows、macOS及Linux系统上实施数据窃取与加密操作。

近日，安全研究人员发现了首款由人工智能驱动的勒索软件——PromptLock。该恶意软件借助Lua脚本，可在Windows、macOS及Linux系统上实施数据窃取与加密操作。

这款恶意软件通过Ollama API调用OpenAI的gpt-oss:20b模型，依据硬编码提示词动态生成恶意Lua脚本。

**PromptLock的运作机制**

据ESET研究人员介绍，PromptLock采用Golang语言编写，并通过Ollama API访问gpt-oss:20b大型语言模型（LLM）。该语言模型部署在远程服务器上，威胁者需通过代理隧道与其建立连接。

该恶意软件内含硬编码提示词，可指令模型动态生成恶意Lua脚本，这些脚本的功能涵盖本地文件系统枚举、目标文件检查、数据窃取及文件加密等。

![enum.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250828/1756363981614492.jpg "1756363704146163.jpg")

文件枚举提示

研究人员还提到其包含数据销毁功能，但该功能尚未实现。

在文件加密方面，PromptLock采用轻量级的SPECK 128位算法——这对勒索软件而言是相当罕见的选择，该算法通常被认为更适用于RFID应用场景。

![encr.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250828/1756363982696747.jpg "1756363735126311.jpg")

PromptLock的加密逻辑

**目前尚处于演示阶段**

据透露，PromptLock并未出现在其遥测数据中，研究人员是在VirusTotal平台上发现它的。ESET认为，PromptLock目前还只是一个概念验证产品或仍在开发中的项目，并非已在野外活跃的勒索软件。

此外，诸多迹象表明它当前仅是一款概念工具，而非实际威胁。例如，它使用安全性较弱的加密算法（SPECK 128位），内置与中本聪（Satoshi Nakamoto）相关联的比特币地址，且数据销毁功能尚未落地。

ESET发布有关PromptLock的详细信息后，一名安全研究人员声称该恶意软件是其开发的项目，不知为何遭到了泄露。

尽管如此，PromptLock的出现仍具有重要意义：它表明人工智能可被武器化并融入恶意软件工作流程，能带来跨平台能力、操作灵活性、规避检测等优势，同时降低了网络犯罪的入门门槛。

这一演变在7月已现端倪——当时乌克兰计算机应急响应小组（CERT）报告发现了LameHug恶意软件。这是一款由大型语言模型驱动的工具，借助Hugging Face API及阿里巴巴的Qwen-2.5-Coder-32B模型，可实时生成Windows shell命令。

据悉，LameHug由APT28组织的俄罗斯黑客部署，它通过API调用实现功能，而非像PromptLock那样采用代理方式。两种实现方式虽能达成相同的实际效果，但后者更为复杂，且风险更高。

文章翻译自：https://www.bleepingcomputer.com/news/security/experimental-promptlock-ransomware-uses-ai-to-encrypt-steal-data/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?9J1zX1v2)

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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

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

[查看更多](https://www.4hou.com/member/BVMN)

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