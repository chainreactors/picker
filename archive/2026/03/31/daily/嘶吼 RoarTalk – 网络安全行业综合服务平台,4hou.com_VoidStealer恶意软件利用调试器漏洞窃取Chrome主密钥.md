---
title: VoidStealer恶意软件利用调试器漏洞窃取Chrome主密钥
url: https://www.4hou.com/posts/0MlN
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-03-31
fetch_date: 2026-04-01T04:45:10.553113
---

# VoidStealer恶意软件利用调试器漏洞窃取Chrome主密钥

VoidStealer恶意软件利用调试器漏洞窃取Chrome主密钥 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# VoidStealer恶意软件利用调试器漏洞窃取Chrome主密钥

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2026-03-31 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)7449

收藏

导语：这是全球野外实战攻击中，首例采用该底层绕过机制的窃密恶意软件。

一款名为VoidStealer的窃密恶意软件采用新型攻击手段，绕过谷歌浏览器（Chrome）的应用程序绑定加密（ABE）防护机制，非法提取用于解密浏览器本地敏感数据的主密钥。

这项全新破解技术隐蔽性极强，核心原理是利用硬件断点，直接从浏览器内存中读取明文状态的v20\_master\_key万能主密钥（同时负责加密与解密运算），全程无需权限提权或代码注入等高风险操作。

诺顿、Avast、AVG、Avira等安全品牌母公司——Gen Digital发布专项安全报告证实，这是全球野外实战攻击中，首例采用该底层绕过机制的窃密恶意软件。

谷歌于2024年6月发布的Chrome 127版本中，正式上线ABE应用绑定加密功能，专门防护浏览器Cookie缓存及各类核心敏感数据。该机制确保万能主密钥在磁盘中始终处于加密封存状态，普通用户权限无法直接读取还原。

正常合法解密主密钥，必须依托系统最高权限运行的谷歌浏览器权限提升服务，严格校验请求进程身份后方可放行。

![图片17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260324/1774337872446917.png "1774337717117941.png")

ABE如何阻止恶意软件概述

但该防护体系此前已被多款窃密恶意软件家族成功绕过，甚至相关破解逻辑已公开开源工具化。尽管谷歌多次推送补丁迭代加固封堵旧漏洞，新型恶意软件仍能衍生新变种，持续绕过防护窃取密钥。

Gen Digital威胁情报研究员表示：“VoidStealer是野外攻击中首个实战落地的窃密工具，创新依托调试器底层原理绕过ABE加密，精准调用硬件断点，直接从浏览器运行内存中dump读取v20\_master\_key万能主密钥。”

据悉，VoidStealer属于恶意软件即服务（MaaS）黑产平台，最迟自2025年12月中旬起，已在暗网论坛公开售卖推广，其2.0版本正式新增这款全新ABE加密绕过高危机制。

![图片18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260324/1774337877167710.png "1774337775901788.png")

网络犯罪分子在VoidStealer 2.0版本中宣传ABE绕过功能

**主密钥窃取攻击原理详解**

VoidStealer的核心破解漏洞逻辑，是精准捕捉浏览器解密运算瞬间：Chrome的v20\_master\_key会短暂以明文裸奔状态驻留内存，恶意软件精准卡位该极短时间窗口完成窃取。

![图片19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260324/1774337879786211.png "1774337879786211.png")

VoidStealer 的目标字符串

具体攻击流程分为五步：

1. 启动静默挂起、后台隐藏的浏览器进程，以调试器身份绑定注入目标进程；

2. 静默等待浏览器核心动态链接库（chrome.dll/msedge.dll）加载完成；

3. 检索库文件内特定特征字符串及寻址指令，锁定指令地址作为硬件断点触发靶点；

4. 对当前所有运行线程及新建线程全局植入断点，静默监听浏览器启动解密流程；

5. 断点触发瞬间读取寄存器密钥指针地址，调用内存读取接口直接dump明文万能主密钥。

恶意软件最优攻击时机为浏览器开机冷启动阶段：此时程序会批量加载ABE加密防护Cookie缓存，强制触发主密钥解密运算，漏洞攻击成功率最高。

该新型绕过技术并非VoidStealer原创开发，而是直接复刻开源项目ElevationKatz漏洞利用逻辑——该工具隶属ChromeKatz缓存导出套件，专门演示Chrome浏览器加密体系底层缺陷，开源上线至今已超一年。 两款工具代码虽存在少量微调差异，但核心攻击实现逻辑高度同源复用。

文章来源自：https://www.bleepingcomputer.com/news/security/voidstealer-malware-steals-chrome-master-key-via-debugger-trick/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?3Oi5yNop)

#### 你可能感兴趣的

* [![]()

  VoidStealer恶意软件利用调试器漏洞窃取Chrome主密钥](https://www.4hou.com/posts/0MlN)
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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [VoidStealer恶意软件利用调试器漏洞窃取Chrome主密钥](https://www.4hou.com/posts/0MlN)
  2026-03-31 12:00:00
* [蠕虫式XMRig挖矿攻击借BYOVD漏洞规避检测](https://www.4hou.com/posts/kgyK)
  2026-03-11 12:00:00
* [谷歌API密钥安全漏洞曝光：前端暴露密钥可直接访问Gemini并窃取隐私数据](https://www.4hou.com/posts/kgyv)
  2026-03-02 11:49:21
* [思科Catalyst SD-WAN严重认证绕过漏洞遭长期入侵，可植入恶意节点控制网络](https://www.4hou.com/posts/vwNM)
  2026-02-28 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [VoidStealer恶意软件利用调试器漏洞窃取Chrome主密钥](https://www.4hou.com/posts/0MlN)

  胡金鱼
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