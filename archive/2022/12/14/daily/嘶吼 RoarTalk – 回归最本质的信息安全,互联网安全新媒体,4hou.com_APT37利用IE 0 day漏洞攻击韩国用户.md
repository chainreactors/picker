---
title: APT37利用IE 0 day漏洞攻击韩国用户
url: https://www.4hou.com/posts/pV1Q
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-14
fetch_date: 2025-10-04T01:22:55.494055
---

# APT37利用IE 0 day漏洞攻击韩国用户

APT37利用IE 0 day漏洞攻击韩国用户 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# APT37利用IE 0 day漏洞攻击韩国用户

ang010ela
[新闻](https://www.4hou.com/category/news)
2022-12-13 11:11:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)145524

收藏

导语：​谷歌研究人员发现朝鲜黑客组织APT 37利用IE 0 day漏洞攻击韩国用户。

谷歌研究人员发现朝鲜黑客组织APT 37利用IE 0 day漏洞攻击韩国用户。

今年10月，谷歌TAG研究人员在IE 浏览器Jscript 引擎中发现一个0 day漏洞，漏洞CVE编号CVE-2022-41128。研究人员发现朝鲜黑客组织APT 37利用该漏洞嵌入恶意文档，用于攻击位于韩国的受害者。这也并非APT 37首次利用IE 0 day漏洞利用攻击用户。

**使用office文档作为诱饵**

10月31日，多个位于韩国的用户上传office文档到VirusTotal称其中包含恶意软件。文档名为“221031 Seoul Yongsan Itaewon accident response situation (06:00).docx”，文档是关于10月29日万圣节庆典韩国首尔梨泰院附近发生了大规模踩踏事故。该事件影响很大，因此攻击者利用这一事件作为诱饵。

![Screenshot of the document content](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/9JPcaepMtqjQxUs.max-1000x1000.png)

图 诱饵文档截图

该诱饵文档会下载一个RTF远程模板，模板会取回远程HTML内容。因为office使用IE 来渲染HTML内容，因此也被广泛用于通过office文件传播IE漏洞利用。谷歌研究人员分析发现，攻击者滥用IE Jscript引擎中的0 day漏洞来发起攻击。

**CVE-2022-41128漏洞利用**

该漏洞位于IE Jscript引起中的“jscript9.dll”中，攻击者利用该漏洞可以在渲染攻击者控制的网站时执行任意代码。10月31日，谷歌研究人员将该漏洞提交给了微软，CVE编号为CVE-2022-41128。微软已于2022年11月8日修复了该漏洞。

诱饵文档中有mark-of-the-web标识，表明用户需要在取回远程RTF模板之前禁用保护视图。

![The user has to disable protected view](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/5F3rjvaCqZLGVLj.max-1000x1000.png)

在交付远程RTF时，web服务器会在响应中设置一个唯一的cookie，在远程HTML内容被请求时会再次发送。漏洞利用JS在启动漏洞利用之前也会验证cookie。此外，还在在漏洞利用启动前和漏洞利用成功后向C2服务器报告两次。谷歌研究人员还发现多个利用同一漏洞的文档。

Shellcode使用定制的哈希算法来解析Windows API。Shellcode会通过在下载下一阶段代码前清除所有IE缓存和历史记录来擦除所有漏洞利用痕迹。下一阶段使用之前设置的同一cookie来下载。

漏洞利用PoC代码参见：<https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2022/CVE-2022-41128.html>

本文翻译自：https://blog.google/threat-analysis-group/internet-explorer-0-day-exploited-by-north-korean-actor-apt37/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?yANsWWTl)

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