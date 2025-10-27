---
title: Ollama AI模型发现六大漏洞，能导致DoS攻击、模型中毒
url: https://www.freebuf.com/news/414559.html
source: FreeBuf网络安全行业门户
date: 2024-11-07
fetch_date: 2025-10-06T19:18:09.613252
---

# Ollama AI模型发现六大漏洞，能导致DoS攻击、模型中毒

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

Ollama AI模型发现六大漏洞，能导致DoS攻击、模型中毒

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Ollama AI模型发现六大漏洞，能导致DoS攻击、模型中毒

2024-11-06 11:37:27

所属地 上海

据The Hacker News消息，网络安全研究人员披露了 Ollama 人工智能模型中的六个安全漏洞，攻击者可能会利用这些漏洞执行各种操作。

![](https://image.3001.net/images/20241106/1730864264_672ae48847ae6a3f58cf9.png!small)

Ollama 是一个开源应用程序，允许用户在 Windows、Linux 和 macOS 设备上本地部署和操作大型语言模型 （LLM）。迄今为止，该模型在 GitHub 上的项目存储库已被分叉 7600 次。

研究员在一份报告中指出，这些漏洞可能允许攻击者通过单个 HTTP 请求执行广泛的恶意操作，包括拒绝服务 （DoS） 攻击、模型中毒、模型盗窃等。

这 6 个漏洞的简要描述如下 -

* **CVE-2024-39719**（CVSS 评分：7.5）：攻击者可以使用 /api/create 端点利用该漏洞来确定服务器中是否存在文件（已在版本 0.1.47 中修复）
* **CVE-2024-39720**（CVSS 评分：8.2）：越界读取漏洞，可通过 /api/create 端点导致应用程序崩溃，从而导致 DoS 情况（已在 0.1.46 版本中修复）
* **CVE-2024-39721**（CVSS 分数：7.5）：在将文件“/dev/random”作为输入传递时，重复调用 /api/create 端点时，会导致资源耗尽并最终导致 DoS 的漏洞（已在 0.1.34 版本中修复）
* **CVE-2024-39722**（CVSS 分数：7.5） ：api/push 端点中的路径遍历漏洞，暴露了服务器上存在的文件以及部署 Ollama 的整个目录结构（已在 0.1.46 版本修复）
* 无 CVE 标识符，未修补 漏洞：可通过来自不受信任的来源的 /api/pull 终端节点导致模型中毒
* 无 CVE 标识符，未修补 漏洞： 可能导致通过 /api/push 终端节点向不受信任的目标进行模型盗窃

对于上述两个未解决的漏洞，Ollama 的维护者建议用户通过代理或 Web 应用程序防火墙过滤哪些端点暴露在了互联网上。

研究人员称，发现了 9831 个运行 Ollama 面向互联网的独特实例，其中大多数位于美国、中国、德国、韩国、中国台湾、法国、英国、印度、新加坡和中国香港。其中有四分之一的服务器被认为容易受到这些漏洞的影响。

另外，云安全公司Wiz在四个多月前披露了一个影响Ollama的严重漏洞（CVE-2024-37032），该漏洞可被利用来实现远程代码执行。

研究人员表示，因为Ollama 可以上传文件，并具有模型拉取和推送功能，因此将未经授权的Ollama暴露在互联网上，就相当于将Docker套接字暴露在公共互联网上，从而容易被攻击者利用。

**参考来源：**

> [Critical Flaws in Ollama AI Framework Could Enable DoS, Model Theft, and Poisoning](https://thehackernews.com/2024/11/critical-flaws-in-ollama-ai-framework.html)

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