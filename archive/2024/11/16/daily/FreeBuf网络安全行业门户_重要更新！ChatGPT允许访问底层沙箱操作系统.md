---
title: 重要更新！ChatGPT允许访问底层沙箱操作系统
url: https://www.freebuf.com/news/415367.html
source: FreeBuf网络安全行业门户
date: 2024-11-16
fetch_date: 2025-10-06T19:17:51.321201
---

# 重要更新！ChatGPT允许访问底层沙箱操作系统

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

重要更新！ChatGPT允许访问底层沙箱操作系统

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

重要更新！ChatGPT允许访问底层沙箱操作系统

2024-11-15 14:47:13

所属地 上海

ChatGPT平台提供了对大型语言模型（LLM）沙盒的高度访问权限，允许用户上传程序和文件、执行命令以及浏览沙盒的文件结构。![](https://image.3001.net/images/20241115/1731654732_6736f44c37a7e25eb3097.png!small)

ChatGPT沙盒是一个隔离的环境，允许用户安全地与之交互，同时与其他用户和主机服务器隔离。它通过限制对敏感文件和文件夹的访问、阻止互联网访问以及尝试限制可能用于利用漏洞或潜在突破沙盒的命令来实现这一点。

Mozilla公司安全研究人员Marco Figueroa发现，可以获取对沙盒的广泛访问权限，包括上传和执行Python脚本，以及下载LLM的“剧本”。在ChatGPT上进行Python项目工作时，Figueroa收到了一个“目录未找到”错误，这使他发现了ChatGPT用户可以与沙盒进行交互。该环境允许对沙盒进行大量访问，允许上传和下载文件、列出文件和文件夹、上传程序并执行它们、执行Linux命令以及输出沙盒内存储的文件。

使用命令如“ls”或“列出文件”，研究人员能够获取底层沙盒文件系统的所有目录列表，包括包含配置和设置信息的'/home/sandbox/.openai\_internal/'。![](https://image.3001.net/images/20241115/1731654748_6736f45c9bd384649ec6c.png!small)

在ChatGPT沙盒中列出文件和文件夹

接下来，他尝试了文件管理任务，发现他能够将文件上传到/mnt/data文件夹，也可以从任何可访问的文件夹下载文件。值得注意的是，沙盒不允许访问特定的敏感文件夹和文件，如/root文件夹和各种文件，如/etc/shadow。然而，研究人员发现他还可以上传自定义Python脚本并在沙盒内执行它们。例如，Figueroa上传了一个简单的脚本，输出文本“Hello, World!”并执行它，输出出现在屏幕上。

![](https://image.3001.net/images/20241115/1731654806_6736f49662cc452b7cc8c.png!small)在沙盒上执行Python代码

由于法律原因，研究人员说他无法上传可能用于尝试突破沙盒或执行更恶意行为的“恶意”脚本。但值得注意的是，尽管上述所有操作都是可能的，但所有操作都限制在沙盒的边界内，因此环境看起来是适当隔离的，不允许“逃逸”到主机系统。

Figueroa还发现，他可以使用提示工程下载ChatGPT的“剧本”，该剧本规定了聊天机器人在一般模型或用户创建的小程序上的行为和响应方式。研究人员表示，访问剧本提供了透明度，并与其用户建立了信任，因为它说明了答案是如何创建的，它也可以用来揭示可能绕过防护栏的信息。

Figueroa进一步解释，“虽然教学透明度是有益的，但它也可能揭示模型的响应是如何构建的，潜在地允许用户逆向工程防护栏或注入恶意提示。配置有保密指令或敏感数据的模型如果用户利用访问权收集专有配置或洞察力，可能会面临风险 。”

![](https://image.3001.net/images/20241115/1731654893_6736f4ed5c55bc3f9f6ca.png!small)访问ChatGPT剧本

虽然Figueroa展示了与ChatGPT的内部环境交互是可能的，但这些交互并没有引起直接的安全或数据隐私问题。OpenAI的沙盒看起来是充分安全的，所有操作都限制在沙盒环境中，与沙盒交互的可能性可能是OpenAI的设计选择的结果。

此外，访问配置细节可能使恶意行为者更好地了解AI工具的工作原理以及如何绕过防御使其生成危险内容。“剧本”包括模型的核心指令和其中嵌入的任何定制规则，例如专有细节和安全相关指南，可能打开逆向工程或针对性攻击的途径。

参考来源：<https://www.bleepingcomputer.com/news/artificial-intelligence/chatgpt-allows-access-to-underlying-sandbox-os-playbook-data/>

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)