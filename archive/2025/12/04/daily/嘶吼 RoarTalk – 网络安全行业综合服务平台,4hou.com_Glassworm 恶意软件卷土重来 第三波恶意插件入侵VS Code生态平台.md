---
title: Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台
url: https://www.4hou.com/posts/qoyR
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-04
fetch_date: 2025-12-05T03:16:57.403554
---

# Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台

Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10099

收藏

导语：开发者一旦在开发环境中安装该恶意插件，其GitHub、npm、OpenVSX账户凭证，以及49款扩展工具中的加密货币钱包数据都将面临被盗风险。

10月首次现身OpenVSX与微软Visual Studio应用市场的Glassworm攻击活动已演进至第三波，目前两大平台新增24款恶意插件。

OpenVSX与微软Visual Studio应用市场均为支持VS Code兼容编辑器的插件仓库，开发者可通过这两个平台安装语言支持包、框架工具、主题模板及其他提升开发效率的附加组件。其中，微软应用市场是Visual Studio Code的官方插件平台，而OpenVSX作为开源、厂商中立的替代方案，主要服务于无法或不愿使用微软专有商店的编辑器用户。

Glassworm恶意软件最早由Koi Security于10月20日披露，其核心技术手段是利用“不可见Unicode字符”隐藏恶意代码，规避平台审核机制。开发者一旦在开发环境中安装该恶意插件，其GitHub、npm、OpenVSX账户凭证，以及49款扩展工具中的加密货币钱包数据都将面临被盗风险。

此外，该恶意软件还会部署SOCKS代理，通过受害者设备中转恶意流量，并安装HVNC客户端，为攻击者提供隐蔽的远程控制权限。

尽管平台方曾清理首批恶意插件，但Glassworm很快通过新的插件包和发布者账户重新入侵两大市场。此前，OpenVSX曾宣布事件已完全受控，并已重置泄露的访问令牌。

此次第三波攻击的重现由Secure Annex研究员发现，恶意插件的命名显示其攻击范围广泛，涵盖Flutter、Vim、Yaml、Tailwind、Svelte、React Native、Vue等热门开发工具与框架。

![fake.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251202/1764661822160262.png "1764661739914270.png")

合法（左）和假冒（右）的软件包

**Secure Annex已确认第三波攻击涉及以下插件：**

**微软Visual Studio应用市场**

1.iconkieftwo.icon-theme-materiall

2.prisma-inc.prisma-studio-assistance

3.prettier-vsc.vsce-prettier

4.flutcode.flutter-extension

5.csvmech.csvrainbow

6.codevsce.codelddb-vscode

7.saoudrizvsce.claude-devsce

8.clangdcode.clangd-vsce

9.cweijamysq.sync-settings-vscode

10.bphpburnsus.iconesvscode

11.klustfix.kluster-code-verify

12.vims-vsce.vscode-vim

13.yamlcode.yaml-vscode-extension

14.solblanco.svetle-vsce

15.vsceue.volar-vscode

16.redmat.vscode-quarkus-pro

17.msjsdreact.react-native-vsce

**OpenVSX应用市场**

1.bphpburn.icons-vscode

2.tailwind-nuxt.tailwindcss-for-react

3.flutcode.flutter-extension

4.yamlcode.yaml-vscode-extension

5.saoudrizvsce.claude-dev

6.saoudrizvsce.claude-devsce

7.vitalik.solidity

攻击流程呈现明显的隐蔽性：恶意插件在通过平台审核后，发布者会推送包含恶意代码的更新包，随后人为刷高下载量，营造“合法可信”的假象。这种刷量行为还能操控搜索结果排序，使恶意插件排名靠前，与所仿冒的正规项目高度接近，增加开发者误装风险。

![search-results.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251202/1764661825156440.jpg "1764661793993468.jpg")

混淆的搜索结果

技术层面，Glassworm已实现升级迭代，目前采用基于Rust语言开发的植入程序封装在插件中，部分场景下仍保留“不可见Unicode字符”的隐藏手段。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251202/1764661857163549.png "1764661857163549.png")

有效负载

文章翻译自：https://www.bleepingcomputer.com/news/security/glassworm-malware-returns-in-third-wave-of-malicious-vs-code-packages/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?6uvjunIH)

#### 你可能感兴趣的

* [![]()

  国家计算机病毒应急处理中心检测发现69款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/nlvY)
* [![]()

  Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台](https://www.4hou.com/posts/qoyR)
* [![]()

  国家网络安全通报中心：重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/l0q7)
* [![]()

  恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本](https://www.4hou.com/posts/kgqY)
* [![]()

  Mixpanel遭网络攻击 OpenAI用户数据或面临泄露风险](https://www.4hou.com/posts/l0rJ)
* [![]()

  Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改](https://www.4hou.com/posts/VW39)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [国家计算机病毒应急处理中心检测发现69款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/nlvY)
  2025-12-05 10:28:08
* [Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台](https://www.4hou.com/posts/qoyR)
  2025-12-04 12:00:00
* [国家网络安全通报中心：重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/l0q7)
  2025-12-04 10:45:47
* [恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本](https://www.4hou.com/posts/kgqY)
  2025-12-02 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [国家计算机病毒应急处理中心检测发现69款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/nlvY)

  胡金鱼
* [Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台](https://www.4hou.com/posts/qoyR)

  胡金鱼
* [国家网络安全通报中心：重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/l0q7)

  胡金鱼
* [恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本](https://www.4hou.com/posts/kgqY)

  胡金鱼
* [Mixpanel遭网络攻击 OpenAI用户数据或面临泄露风险](https://www.4hou.com/posts/l0rJ)

  胡金鱼
* [Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改](https://www.4hou.com/posts/VW39)

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