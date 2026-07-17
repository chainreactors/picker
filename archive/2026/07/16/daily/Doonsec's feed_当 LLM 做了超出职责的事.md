---
title: 当 LLM 做了超出职责的事
url: https://mp.weixin.qq.com/s/uMIVkBC0z4Fe0FCS2UlKzA
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:58:34.442328
---

# 当 LLM 做了超出职责的事

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSia8gObsw6iahjiakLDnwywTSNk7OtvkJDLHfunjEicns17wFsZTIXzcownnhGjBm6O1YtVOxcIHIa2NBHHOP3T3jSy4tjCWbfoXIs/0?wx_fmt=jpeg)

# 当 LLM 做了超出职责的事

nytrosecurity
nytrosecurity

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://nytrosecurity.com/2026/07/14/when-llms-do-more-than-they-have-to/ | nytrosecurity |

围绕 LLM 及其能力的炒作可谓铺天盖地。诸如"Mythos"之类的模型被捧为当代神明。开发者们完全依赖基础提示词来完成工作，迅速将多年积累的技能抛诸脑后。企业在 token 上投入数以亿计的资金，而其中大部分都在缺乏实际用途的情况下被浪费掉了。但眼下发生的一切真的都那么美好吗？还是说有些问题值得人们警惕？虽然我深知 LLM 的强大之处，但我也看到了它的局限性——人们似乎轻易地忽视了这些局限，而这可能引发糟糕的后果。

## **我想要的**

一个简单的 HTML 文件。我让 Claude Code 帮我生成一个 HTML 文件。思路非常简单：查找一些产品的文档，然后给我写一个简单的 HTML 文件。仅此而已。

> 我想向公司的新同事介绍公司产品，包括简要的产品详情和功能特性。我想展示功能及其使用方式的照片/截图，但由于产品众多，只需高层级概览即可。我也想涵盖桌面端产品。请查阅公司产品的文档以及其他详情页面，为我制作一份可分享的文档（例如标记语言格式），覆盖大部分产品并包含简要信息：它是什么、重要功能、如何运作，但要简短。

而这是它的回复：

> 好的——HTML Artifact、真实嵌入的截图、完整目录。这个组合有一个硬性技术约束需要我先解决：Artifact 在严格的 CSP 下运行，会阻止所有外部图片，因此每张截图都必须下载、压缩并嵌入为 data: URI。在正式投入这条流水线之前，让我先探测一下环境，确认能否可靠地获取和处理图片。

Claude Code 使用 Opus 4.8 和"Ultracode"，试图帮助我，它需要打开一些网站并查找最新文档——它确实做到了。但遗憾的是，它多做了一些事。也许让它包含图片这个要求有点过了……

## **我得到的**

Claude 似乎是个乐于助人的助手，总是超出预期。

```
Environment: curl ✓, node v24 ✓, but no Python/ImageMagick/sharp. Let me set up image processing (install sharp for resize/compress) and test the end-to-end screenshot pipeline on one product before scaling to the full catalog.

sharp installed ✓ and WebFetch surfaced real CDN image URLs. Let me verify I can actually download and process one (the URLs point to images.ctfassets.net, Company's CDN).
```

"sharp"到底是什么？它也许是个开发工具，但真的有必要安装它吗？在"Auto"模式下运行是不是太过头了？"Environment: curl ✓, node v24 ✓"这行输出看起来也不太妙。

它利用已安装的 NodeJS 运行一些工具并构建了 HTML。很好！来看看结果：

```
Created a file, ran a command, used 2 tools
file:// isn't accepted by the browser tool. Let me serve the scratchpad over local HTTP and view it there.

running
Starting static server in background
```

这看起来有点可疑。为一个 HTML 文件开启 Web 服务器？这真的有必要吗？来看看：

```
C:\Windows\System32>netstat  -abnp tcp
...
  TCP    0.0.0.0:8791           0.0.0.0:0              LISTENING    [node.exe]

C:\Windows\System32>netstat -abnp tcpv6
...
  TCP    [::]:8791              [::]:0                 LISTENING    [node.exe]
```

现在我的机器上运行着一个 NodeJS 服务器，监听所有 IP 地址，而不是仅限 localhost。太好了！能出什么岔子呢？

来看看提供 HTML 服务的代码：

```
consthttp=require('http'), fs=require('fs'), path=require('path');
constroot=__dirname;
http.createServer((req, res) => {
letf=decodeURIComponent(req.url.split('?')[0]);
if (f==='/') f='/company-platform-guide.html';
constp=path.join(root, f);
fs.readFile(p, (e, d) => {
if (e) { res.writeHead(404); res.end('nf'); return; }
constext=path.extname(p).slice(1);
constt= {html:'text/html', js:'text/javascript', json:'application/json', webp:'image/webp'}[ext] ||'application/octet-stream';
res.writeHead(200, {'content-type': t});
res.end(d);
    });
}).listen(8791, () =>console.log('serving on http://localhost:8791'));
```

你不需要是代码审计专家就能注意到：

```
constroot=__dirname;
letf=decodeURIComponent(req.url.split('?')[0]);
constp=path.join(root, f);
fs.readFile(p, (e, d) => {
...
```

这是一个目录遍历漏洞。

![文章截图](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjYM1yRicHKckhh5ffbwBerNBChtOvStpTSS441J1UCxpxcWSvxEYZpVCUwRBWLg4FoFVYUoR0OicklAdiawC33eQWf7IQoLJtPx8/640?wx_fmt=png&from=appmsg)

文章截图

## **结论**

LLM 默认可能不会生成安全代码，这对开发者和安全团队来说是个问题。但还有一些情况是，LLM 做的比你要求的多了一点，这可能导致各种各样的问题。虽然我的情况不算高度严重——我只是想要一个该死的 HTML 文件，而 Claude 却让我的机器可以被远程（同一 VNET 内）利用。这不是我想要的。

我的两点建议：始终审查你的 Agent / LLM 做了什么。

---

> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过