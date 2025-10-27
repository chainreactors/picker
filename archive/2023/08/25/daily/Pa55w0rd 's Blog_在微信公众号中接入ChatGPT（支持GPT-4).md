---
title: 在微信公众号中接入ChatGPT（支持GPT-4)
url: http://www.pa55w0rd.online/wechatmp-chatgpt/
source: Pa55w0rd 's Blog
date: 2023-08-25
fetch_date: 2025-10-04T12:01:50.385074
---

# 在微信公众号中接入ChatGPT（支持GPT-4)

# [Pa55w0rd 's Blog](/)

## [记录](/)

[首页](/)
[归档](/archives)
[威胁情报](/threat-broadcast)
[关于我](/about)
[留言](/comments)
[公益404](/404.html)

[2023-08-24](/wechatmp-chatgpt/)

[note](/categories/note/)

# 在微信公众号中接入ChatGPT（支持GPT-4)

文章导航

×
**文章目录**

1. [1. 引言](#%E5%BC%95%E8%A8%80)
2. [2. 为什么要将ChatGPT接入微信公众号私信呢](#%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E5%B0%86ChatGPT%E6%8E%A5%E5%85%A5%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7%E7%A7%81%E4%BF%A1%E5%91%A2)
3. [3. 如何使用](#%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8)
4. [4. 我是如何接入的](#%E6%88%91%E6%98%AF%E5%A6%82%E4%BD%95%E6%8E%A5%E5%85%A5%E7%9A%84)
5. [5. 总结一下](#%E6%80%BB%E7%BB%93%E4%B8%80%E4%B8%8B)

## 引言

ChatGPT是由OpenAI开发的一种基于大型语言模型的对话系统。它可以回答各种问题并进行交流，为用户提供实时的帮助与解答。而微信公众号是一个非常受欢迎的社交媒体平台，许多企业和个人在其中运营和提供服务。本文将介绍如何将ChatGPT接入微信公众号，让用户可以通过私信与ChatGPT进行交流。

## 为什么要将ChatGPT接入微信公众号私信呢

首先，这可以为你的公众号增加一个全新的互动方式。你可以让ChatGPT回答读者的问题，提供更个性化的答案和建议。这样，你的读者不再只是被动地阅读你的文章，而是真正与你的公众号进行互动。

接入ChatGPT也能够为你的公众号带来更多的亮点。想象一下，你的读者可以发送私信给ChatGPT，询问各种问题，不仅限于你之前发布的内容。无论是技术问题、生活琐事还是搞笑段子，ChatGPT都可以给出非常有趣的回答。这样一来，你的公众号将成为读者心中的好玩伙伴，增加用户粘性和留存率。

不过，我们也要注意一点。虽然ChatGPT可以提供智能的回答，但它毕竟是一个机器学习模型，在某些情况下可能会给出不准确或不合理的回答。所以，在使用ChatGPT的同时，你也要进行一定的监控和过滤，确保回答的质量和可靠性。

## 如何使用

1. 关注公众号`Pa55w0rd`
   ![1692869717320.png](https://yanxuan.nosdn.127.net/4548872160382ce121f6bac7287b6076.png)
2. 直接给公众号发送消息即可
   默认使用`gpt-3.5-turbo-0613`模型，可以通过`#set_gpt_model gpt-4-0613`命令切换gpt-4-0613模型（GPT-4比较慢，也不保证可用），通过`#reset_gpt_model`重置默认模型，通过`#gpt_model`查看当前模型，通过`#reset`重置会话
3. 由于受订阅号限制，回复内容较短的情况下 (15s内)，可以立即完成回复，但耗时较长的回复则会先回复一句 “正在思考中”，后续需要用户输入任意文字主动获取答案
   ![1692869926985.png](https://yanxuan.nosdn.127.net/fb5789d744eaf842c142163776434331.png)

## 我是如何接入的

使用[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)项目，按照接入文档操作，写的很详细，我是3月21日接入微信，因为微信平均一周掉线一次，到6月16号选择接入公众号，运行很稳定，微信小号也是老号，未发现封号、限制添加好友问题

项目介绍
`Wechat robot based on ChatGPT, which using OpenAI api and itchat library. 使用ChatGPT搭建微信聊天机器人，基于 GPT3.5/GPT4.0/文心一言 模型，支持个人微信、公众号、企业微信部署，能处理文本、语音和图片，访问操作系统和互联网，支持基于知识库定制专属机器人。`

## 总结一下

通过将ChatGPT接入微信公众号私信，你可以为你的读者带来更加生动、有趣的互动体验。这不仅能够增加用户的参与度，还能够提高用户粘性和留存率。当然，合理使用ChatGPT的同时，也要注意回答质量和准确性的监控。让我们一起探索，为微信公众号注入无限可能吧！

分享到
[留言](https://www.pa55w0rd.online/wechatmp-chatgpt/#gitalk-container)

* [ChatGPT](/tags/ChatGPT/)
* [GPT-4](/tags/GPT-4/)
* [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/)
* [私信互动](/tags/%E7%A7%81%E4%BF%A1%E4%BA%92%E5%8A%A8/)

[**← 上一篇**

通过宜搭流程表单完成JumpServer自动化授权](/jumpserver-yida/)

Please enable JavaScript to view the [comments powered by Disqus.](http://disqus.com/?ref_noscript)

### 近期文章

* [在微信公众号中接入ChatGPT（支持GPT-4)](/wechatmp-chatgpt/)
* [通过宜搭流程表单完成JumpServer自动化授权](/jumpserver-yida/)
* [JumpServer堡垒机部署与运营](/jumpserver/)
* [jetbrains产品免费食用方法-\_-](/jetbrains-use/)
* [SPA & fwknop & SDP & Pomerium & IAP & Traefik & KeyCloak & Casbin & ORY Oathkeeper](/zer-trust-security-model/)

### 分类

* [note](/categories/note/)45
* [web安全](/categories/web%E5%AE%89%E5%85%A8/)14
* [安全建设](/categories/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/)31
* [应急响应](/categories/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)4
* [开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)7
* [移动安全](/categories/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/)3

### 标签云

[Android - 安全测试 - 工具使用](/tags/Android-%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95-%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [ChatGPT](/tags/ChatGPT/) [DevSecOps](/tags/DevSecOps/) [GPT-4](/tags/GPT-4/) [HTTPS](/tags/HTTPS/) [PHPstudy](/tags/PHPstudy/) [SDL](/tags/SDL/) [TRS](/tags/TRS/) [algolia](/tags/algolia/) [checklist](/tags/checklist/) [docker](/tags/docker/) [hexo](/tags/hexo/) [iam](/tags/iam/) [jsonp劫持](/tags/jsonp%E5%8A%AB%E6%8C%81/) [linux](/tags/linux/) [mongodb](/tags/mongodb/) [note](/tags/note/) [sql](/tags/sql/) [sql注入](/tags/sql%E6%B3%A8%E5%85%A5/) [web安全](/tags/web%E5%AE%89%E5%85%A8/) [windows 审计工具](/tags/windows-%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7/) [xunfeng](/tags/xunfeng/) [zero-trust](/tags/zero-trust/) [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [分析](/tags/%E5%88%86%E6%9E%90/) [基础](/tags/%E5%9F%BA%E7%A1%80/) [基础知识](/tags/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) [备忘录](/tags/%E5%A4%87%E5%BF%98%E5%BD%95/) [威胁情报](/tags/%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5/) [安全建设](/tags/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/) [安全开发](/tags/%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91/) [安全漏洞](/tags/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/) [安全防护](/tags/%E5%AE%89%E5%85%A8%E9%98%B2%E6%8A%A4/) [安装使用](/tags/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8/) [工具](/tags/%E5%B7%A5%E5%85%B7/) [工具使用](/tags/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [平台建设](/tags/%E5%B9%B3%E5%8F%B0%E5%BB%BA%E8%AE%BE/) [应急响应](/tags/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/) [开发安全](/tags/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/) [开源](/tags/%E5%BC%80%E6%BA%90/) [开源工具](/tags/%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7/) [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/) [技巧](/tags/%E6%8A%80%E5%B7%A7/) [操作记录](/tags/%E6%93%8D%E4%BD%9C%E8%AE%B0%E5%BD%95/) [数据安全](/tags/%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8/) [数据库](/tags/%E6%95%B0%E6%8D%AE%E5%BA%93/) [未授权访问](/tags/%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE/) [渗透测试](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [漏洞利用](/tags/%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8/) [漏洞管理](/tags/%E6%BC%8F%E6%B4%9E%E7%AE%A1%E7%90%86/) [私信互动](/tags/%E7%A7%81%E4%BF%A1%E4%BA%92%E5%8A%A8/) [移动安全](/tags/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/) [编程基础](/tags/%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/) [蜜罐](/tags/%E8%9C%9C%E7%BD%90/) [解决方法](/tags/%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/) [记录](/tags/%E8%AE%B0%E5%BD%95/) [资产扫描](/tags/%E8%B5%84%E4%BA%A7%E6%89%AB%E6%8F%8F/) [迁移](/tags/%E8%BF%81%E7%A7%BB/) [运维安全](/tags/%E8%BF%90%E7%BB%B4%E5%AE%89%E5%85%A8/) [速查表](/tags/%E9%80%9F%E6%9F%A5%E8%A1%A8/) [零信任](/tags/%E9%9B%B6%E4%BF%A1%E4%BB%BB/)

### 归档

* [2023年08月](/archives/2023/08/)1
* [2022年03月](/archives/2022/03/)5
* [2021年12月](/archives/2021/12/)2
* [2021年09月](/archives/2021/09/)1
* [2021年08月](/archives/2021/08/)5
* [2021年07月](/archives/2021/07/)1
* [2021年06月](/archives/2021/06/)1
* [2021年05月](/archives/2021/05/)5
* [2019年11月](/archives/2019/11/)3
* [2019年10月](/archives/2019/10/)2
* [2019年09月](/archives/2019/09/)1
* [2019年08月](/archives/2019/08/)1
* [2019年07月](/archives/2019/07/)6
* [2019年06月](/archives/2019/06/)1
* [2019年05月](/archives/2019/05/)3
* [2019年04月](/archives/2019/04/)1
* [2019年03月](/archives/2019/03/)2
* [2019年01月](/archives/2019/01/)3
* [2018年12月](/archives/2018/12/)10
* [2018年11月](/archives/2018/11/)12
* [2018年10月](/archives/2018/10/)23
* [2018年09月](/archives/2018/09/)15

### 链接

### 友情链接『不分先后』

* [firexun](https://firexun.github.io)
* [Weiho](http://www.weiho.xyz)
* [pirogue](http://pirogue.org)
* [Cotton's Blog](http://www.mianhuage.com)
* [超级菜鸟](https://www.lovesec.com)
* [超级大熊猫](https://my.oschina.net/9199771)

© 2023 Pa55w0rd
Powered by [Hexo](http://hexo.io/)
.
Theme by [Landscape-x](https://github.com/HipHopCoderS/Landscape-x)

我的网站的访问总数:次

[首页](/)
[归档](/archives)
[威胁情报](/threat-broadcast)
[关于我](/about)
[留言](/comments)
[公益404](/404.html)

![](/img/betop.png)