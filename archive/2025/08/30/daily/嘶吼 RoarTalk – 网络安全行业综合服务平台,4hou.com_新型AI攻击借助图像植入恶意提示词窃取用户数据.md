---
title: 新型AI攻击借助图像植入恶意提示词窃取用户数据
url: https://www.4hou.com/posts/l0w6
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-30
fetch_date: 2025-10-07T00:17:17.901901
---

# 新型AI攻击借助图像植入恶意提示词窃取用户数据

新型AI攻击借助图像植入恶意提示词窃取用户数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型AI攻击借助图像植入恶意提示词窃取用户数据

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-08-29 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)61368

收藏

导语：该方法借助高分辨率图像实现，这些图像所承载的指令对人眼而言是不可见的，但当通过重采样算法降低图像质量时，指令便会显现出来。

近日，一种新型攻击手段开始出现，其通过在人工智能系统处理的图像中植入恶意提示词，再将图像传输至大型语言模型，从而窃取用户数据。

该方法借助高分辨率图像实现，这些图像所承载的指令对人眼而言是不可见的，但当通过重采样算法降低图像质量时，指令便会显现出来。

**攻击的运作方式**

当用户将图像上传至人工智能系统时，为兼顾性能与成本效益，系统会自动将图像降采样至更低质量。

依据系统的不同，图像重采样算法可能会采用最近邻插值、双线性插值或双三次插值的方式来减小图像体积。若原始图像是为此目的专门设计的，那么所有这些方法都会产生混叠伪像，进而使隐藏图案在降采样后的图像上显现。

在Trail of Bits公司的案例中，当使用双三次降采样对恶意图像进行处理时，图像中特定的深色区域会变为红色，隐藏的黑色文本也随之显现。

![example.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250826/1756194798115163.jpg "1756194791921946.jpg")

在缩小的图像上显示隐藏信息的示例

人工智能模型会将这些文本视作用户指令的一部分，并自动将其与合法输入相结合。 从用户的角度来看，一切似乎都正常，但实际上，模型已执行了隐藏指令，这可能会导致数据泄露或引发其他危险行为。

在一个涉及Gemini CLI的案例中，研究人员借助Zapier MCP，在“trust=True”的设置下，无需用户确认即可批准工具调用，进而成功将谷歌日历数据泄露至任意邮箱地址。

Trail of Bits公司解释称，需根据每个人工智能模型处理图像时所使用的降采样算法，对该攻击手段进行相应调整。不过，研究人员已证实，他们的方法对以下人工智能系统有效：

**·**谷歌Gemini CLI

**·**Vertex AI Studio（采用Gemini后端）

**·**Gemini的网页界面

**·**通过llm CLI访问的Gemini API

**·**安卓手机上的谷歌助手

**·**Genspark

由于这种攻击向量分布广泛，其影响范围可能远不止于已测试的工具。此外，为了证明他们的发现，研究人员还开发并发布了Anamorpher（目前处于测试阶段）——这是一款开源工具，能够针对上述每种降采样方法生成相应图像。

**缓解与防御措施**

Trail of Bits公司的研究人员建议，人工智能系统在用户上传图像时应实施尺寸限制。若必须进行降采样，应向用户提供传输给大型语言模型的图像结果预览。

他们还认为，对于敏感的工具调用，应获取用户的明确确认，尤其是在检测到图像中包含文本时。

研究人员表示：“最有效的防御措施是实施安全的设计模式和系统性防御手段，以缓解包括多模态提示词注入在内的各类具有影响的提示词注入攻击。” 他们还引用了6月发表的一篇关于构建能够抵御提示词注入攻击的大型语言模型设计模式的论文。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-ai-attack-hides-data-theft-prompts-in-downscaled-images/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?fpj0Za8G)

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