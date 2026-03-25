---
title: 新型网络攻击InstallFix曝光：伪装CLI工具安装指令，诱导执行恶意命令
url: https://www.4hou.com/posts/2X6A
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-03-24
fetch_date: 2026-03-25T04:16:00.650226
---

# 新型网络攻击InstallFix曝光：伪装CLI工具安装指令，诱导执行恶意命令

新型网络攻击InstallFix曝光：伪装CLI工具安装指令，诱导执行恶意命令 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型网络攻击InstallFix曝光：伪装CLI工具安装指令，诱导执行恶意命令

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-03-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)11711

收藏

导语：二者的区别仅在于macOS与Windows系统（PowerShell、命令提示符）下的安装指令，伪造指令会从攻击者控制的服务器端下载恶意程序。

网络攻击者正在使用一种名为InstallFix的新型社工攻击手法，该手法是ClickFix技术的变种，其以安装合法命令行工具（CLI）为借口，诱骗用户执行恶意指令。

这种新型攻击手段利用了当下开发者群体中的常见习惯：直接通过curl-to-bash这类命令从网络源下载并执行脚本，而未事先仔细检查内容。 研究人员发现，攻击者借助全新的InstallFix技术，克隆多款主流CLI工具的官方页面，并在页面中投放恶意安装命令。

当前安全模型“本质上仍停留在‘信任域名’阶段”，且越来越多非技术人员开始使用原本仅面向开发者的工具，这使得InstallFix可能演变为更大规模的安全威胁。

日前，Push Security披露了一个克隆自Anthropic旗下代码助手Claude Code的伪造安装页面。该页面在布局、品牌标识与文档侧边栏等方面，均与官方来源完全一致。

二者的区别仅在于macOS与Windows系统（PowerShell、命令提示符）下的安装指令，伪造指令会从攻击者控制的服务器端下载恶意程序。

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260309/1773043296292317.png "1773043239157734.png")

合法页面（上）和恶意页面（下）

研究人员指出，除安装指令外，伪造页面上的其余链接均会跳转到Anthropic官方网站。受害者进入页面并按照伪造指令操作后，仍可正常继续后续流程，完全意识不到已遭遇攻击。

攻击者通过谷歌广告中的恶意广告活动推广这些伪造页面，使得在搜索“Claude Code安装”“Claude Code CLI”等关键词时，恶意广告会出现在搜索结果中。

经证实，此类恶意网站仍在通过谷歌搜索的推广链接进行投放。搜索“install claude code”时，第一条结果即为Squarespace域名（claude-code-cmd.squarespace[.]com），页面与Claude Code官方文档几乎完全一致。

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260309/1773043301828891.png "1773043270467649.png")

谷歌搜索推送虚假的 Claude 安装网站

**部署Amatera信息窃取木马**

根据分析，InstallFix攻击所投递的载荷为Amatera窃密木马，该恶意软件旨在从受感染设备中窃取加密货币钱包、账号凭证等敏感数据。

针对macOS的恶意InstallFix命令中，包含经过Base64编码的指令，用于从攻击者控制的域名下载并执行二进制程序。其中一起案例中，攻击者使用的域名为wriconsult[.]com，目前该域名已下线。

针对Windows用户，恶意命令利用系统合法工具mshta.exe拉取恶意程序，并触发conhost.exe等额外进程，为最终载荷Amatera窃密木马的执行提供支撑。

![图片7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260309/1773043303100755.png "1773043303100755.png")

克隆版 Claude 安装指南（含恶意命令）

Amatera是一款较新的恶意软件家族，基于ACR Stealer开发，以订阅式服务（MaaS，恶意软件即服务）的形式向网络犯罪分子出售。

该恶意软件近期还出现在其他ClickFix攻击活动中，攻击者滥用Windows App-V脚本实现载荷投递。它可窃取浏览器中存储的密码、Cookie与会话令牌，采集系统信息，同时规避安全工具检测。

此类攻击具有较强的隐蔽性，原因之一是恶意站点托管于Cloudflare Pages、Squarespace、EdgeOne等正规平台。

在近期的一次攻击活动中，攻击者同样使用InstallFix技术，伪造托管在GitHub仓库中的OpenClaw安装程序，并通过必应AI增强搜索结果进行推广。

用户如需安装Claude Code，务必从官方网站获取安装指令，屏蔽或跳过谷歌搜索中的所有推广结果，并将常用软件下载入口添加至书签。

文章来源自：https://www.bleepingcomputer.com/news/security/fake-claude-code-install-guides-push-infostealers-in-installfix-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?wKVAQegI)

#### 你可能感兴趣的

* [![]()

  从假新闻刷屏看清“认知安全”：AI时代网络安全的新边疆](https://www.4hou.com/posts/nlMp)
* [![]()

  Trivy漏洞扫描器遭入侵，攻击者通过GitHub Actions分发窃密恶意软件](https://www.4hou.com/posts/9jxz)
* [![]()

  嘶吼安全动态｜国家数据局：我国AI日均Token调用量破140万亿 LiteLLM遭供应链投毒，数千企业面临数据泄露风险](https://www.4hou.com/posts/mkL3)
* [![]()

  新型网络攻击InstallFix曝光：伪装CLI工具安装指令，诱导执行恶意命令](https://www.4hou.com/posts/2X6A)
* [![]()

  嘶吼安全动态｜工信部部署2026年信息通信业安全生产和网络运行安全工作 Copilot及Cursor等AI编码助手曝规则文件注入漏洞](https://www.4hou.com/posts/7MvB)
* [![]()

  嘶吼安全动态｜国家级电力AI中试基地启用，华为、百度入驻筑牢能源AI安全 OpenWebUI服务器遭攻击，被植入挖矿与信息窃取恶意代码](https://www.4hou.com/posts/2XnA)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [从假新闻刷屏看清“认知安全”：AI时代网络安全的新边疆](https://www.4hou.com/posts/nlMp)
  2026-03-25 12:01:00
* [Trivy漏洞扫描器遭入侵，攻击者通过GitHub Actions分发窃密恶意软件](https://www.4hou.com/posts/9jxz)
  2026-03-25 12:00:00
* [嘶吼安全动态｜国家数据局：我国AI日均Token调用量破140万亿 LiteLLM遭供应链投毒，数千企业面临数据泄露风险](https://www.4hou.com/posts/mkL3)
  2026-03-25 11:50:00
* [新型网络攻击InstallFix曝光：伪装CLI工具安装指令，诱导执行恶意命令](https://www.4hou.com/posts/2X6A)
  2026-03-24 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [从假新闻刷屏看清“认知安全”：AI时代网络安全的新边疆](https://www.4hou.com/posts/nlMp)

  山卡拉
* [Trivy漏洞扫描器遭入侵，攻击者通过GitHub Actions分发窃密恶意软件](https://www.4hou.com/posts/9jxz)

  胡金鱼
* [嘶吼安全动态｜国家数据局：我国AI日均Token调用量破140万亿 LiteLLM遭供应链投毒，数千企业面临数据泄露风险](https://www.4hou.com/posts/mkL3)

  胡金鱼
* [新型网络攻击InstallFix曝光：伪装CLI工具安装指令，诱导执行恶意命令](https://www.4hou.com/posts/2X6A)

  胡金鱼
* [嘶吼安全动态｜工信部部署2026年信息通信业安全生产和网络运行安全工作 Copilot及Cursor等AI编码助手曝规则文件注入漏洞](https://www.4hou.com/posts/7MvB)

  山卡拉
* [嘶吼安全动态｜国家级电力AI中试基地启用，华为、百度入驻筑牢能源AI安全 OpenWebUI服务器遭攻击，被植入挖矿与信息窃取恶意代码](https://www.4hou.com/posts/2XnA)

  山卡拉

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