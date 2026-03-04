---
title: 记一次差点进编制的漏洞测试
url: https://mp.weixin.qq.com/s/bxuTgsrQLUxYr7WSX1czfw
source: Doonsec's feed
date: 2026-03-03
fetch_date: 2026-03-04T04:01:35.379508
---

# 记一次差点进编制的漏洞测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kA6wmJJAxibcm8bBDkw4B5icB4Vrsz0lCntU7Q0m9splQPQexLRPM7oCicavQV0huGzmTOgo4k7SnvnwziacaCkBPPtPcvJWhaoLibCK4lYropPU/0?wx_fmt=jpeg)

# 记一次差点进编制的漏洞测试

湘安无事

![]()

在小说阅读器中沉浸阅读

编者荐语：

学员写的点点关注

以下文章来源于植物人学安全
，作者qfbsz

![](http://wx.qlogo.cn/mmhead/r48cSSlr7jjudR2bxdaMicDvqSF9BB4wCHKNpZbb8SYo515Qf1NZNGMugwzhT6rnwdicx3Aua1huU/0)

**植物人学安全**
.

面试经验分享、web安全知识分享、src、渗透测试、测试工具、个人学习记录

**免责声明**

|  |
| --- |
| 本文仅用于网络安全技术学习与交流，**严禁将文中技术用于任何非法入侵、未授权测试、数据窃取等违法违规行为**。因擅自使用本文内容进行非法操作、或传播本文所造成的一切法律责任与经济损失，均由使用者自行承担，与本公众号及作者无关。如有内容侵权，请及时联系我们处理 |

**漏洞测试**

微信上面找到一个服务号

![e1ed0937fe1b5420eb51cd4c5a6fcb6e.png](https://mmbiz.qpic.cn/mmbiz_png/kA6wmJJAxibfb0HSuTTkFkg2pvyeIJ0OaPn5OjsOSymN6lmLVHOoicGQSAFJCqVJHyYOzAXyP8QMAIQoicXHYJD0jUxQ1Dv7yMA35VdZfczdicw/640?from=appmsg)

点击校园车辆有一个小程序资产

![image.png](https://mmbiz.qpic.cn/mmbiz_png/kA6wmJJAxibeicfV2Qp2fcic3VibMfF7erROMOXZfODDyXqN3hc9CELZBUJkxicqksvJUed9VttbicDBrb9KbXkCZRMUDvOhrjp804KxNVvQJcPFM/640?from=appmsg)

点击车辆用户--->违规记录

发现可以看到不属于自己的违规信息，这有点越权的意思，但是没什么信息

![37748c8191bd3a8295f98ee1026f8c81.png](https://mmbiz.qpic.cn/sz_mmbiz_png/kA6wmJJAxibfXGd7QqFQwNo8TnfibicI0SjbaRgUGSoSLSK0RCksblylkJHJgJJZvNnibSk5ofp3HLCaKCLZy7ZW9IbQNniazjjqQtJibQ6T1kIHw/640?from=appmsg)

一般有小洞就有大洞，抓包查看信息

![be2d3b9a8f02dacd480c31fcfc447a41.png](https://mmbiz.qpic.cn/mmbiz_png/kA6wmJJAxibdKCwe4wL2Uz4os1BTiaAkAa5Ghx2vUSM3stAcKqjCicoQAyMg6W2NL0keI0OPr7IHaXibiccycofG1iaDqPQ5SeXJxCtA3SZrbLpCg/640?from=appmsg)

发现全加密了，这我测个damn啊，直接下机！！！

                                ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/kA6wmJJAxibdtCpyuubdrjV505hIl2JBo09UhxVqJF4ZUFqIyDKMibRYicEHtm0gaicQia5HCuJdWpWEo5ebicq8ZKsNntzEqfFg4yNtUXMUXiaGVA/640?from=appmsg)

没办法，开始反编译小程序

全局搜索encrypt。发现加密函数

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/kA6wmJJAxibfXJtibV4emOSmic5ib1K6DR8jCqaanCoFLSto01oYDtK2ZlWq0URrCicM9lq89Kll1bKDz8MfxtUA2DiaicdibSiaIVU9hRKFQz4iahN6A/640?from=appmsg)

定位到相关文件，大概率是个aes，这种没混淆的js就直接把整个文件扔个deepseek，碰上混淆的就没办法了，只能调试

![image.png](https://mmbiz.qpic.cn/mmbiz_png/kA6wmJJAxibc3yAAgn9rO5Z2tPxnxyfmjc6cfAzqKxPUHLibCbs8JobytFvlBicvEsZsVZNfQPePdP4e2vUScOug7WgBba0SnC4nYhQE2fXqG4/640?from=appmsg)

ai给出脚本后解密成功

![54d3bcb52afacd3d2b30cbebb8c4b4db.png](https://mmbiz.qpic.cn/mmbiz_png/kA6wmJJAxibfr1Jicn0Vpq5IXicibdl8v1uPPoecdicFKI7dnDGiayZyPjMbAsJTEWkibicvibTNp25X2yj9lY0ocVnCHmZso9iayCLdyM1M8kB5CTQkc/640?from=appmsg)

在某个文件中发现大量接口

![image.png](https://mmbiz.qpic.cn/mmbiz_png/kA6wmJJAxibdRZzsicCI342Mh7KibdzpVghWJZib8IJUnfZeVxQb5EpvYe8jiaia3aj5KxyqW8Y3ENoE0YibFrGGPjaQMCEbTcnvnBjC2zFQlicSPic4/640?from=appmsg)

越权点一

/schoolUser/list

这个接口可以查看所有老师的信息直接构造数据包后发包

![c879f44e12ca657cb8594f1fada205fa.png](https://mmbiz.qpic.cn/mmbiz_png/kA6wmJJAxibeA7Bfl4icCF3mu7D5AI7Rh3o0FAQDEVe6zRPKtHmmDWWJO7qR1jV2qaAPIFQEHljvlVDP0aN7ySyUa6Ql31QicPL3zttJDr1Fbc/640?from=appmsg)

![9f9cccf8a688d1030be738c28eacbd6a.png](https://mmbiz.qpic.cn/mmbiz_png/kA6wmJJAxibdQTYgegQu0wBppic2R6hU0Niak2nsVE7jWUk2hDbqW2xU4vplYxzqg7B8vicddc5hiboEtN0xQl7LZlVIbI7Dys3MsEQb7XaZbeMg/640?from=appmsg)

越权点二

/schoolUser/save

这是一个保存接口，此时的我还没意识到事情的严重性

直接随便构造id参数为123后发包了

![2a92b141ddfd45283f23ac3e9b52e29d.png](https://mmbiz.qpic.cn/mmbiz_png/kA6wmJJAxibdbu0s0eyd8Tpn2VknPviaaB17CUghAI82zDOqC7ls4SNctdgK3D6C8CWEfxOLzuHPZePwhclZibp9lia1DPJEWgMX2vM2r0A3XO8/640?from=appmsg)

解密响应包后发现内容是请求成功

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/kA6wmJJAxibfibN6Bs8j3NcZRstHrfsXugaWG5f8jVwSaEyJuR6VYRXImAnVjXVhUnAf8DQFKvB3je4c3emHWt2sYMLWm3fXx0q8Sp37yzEiaI/640?from=appmsg)

这时用/schoolUser/list查看，发现成功保存

![e32e6e6f845c3c675634ebf79742bf75.png](https://mmbiz.qpic.cn/mmbiz_png/kA6wmJJAxibeQic4RIA4XVsPuVJhqnd4FHajj08xhHguOP3cUBXnzjWrlWCEibLpz9CZJR9tZOdgtV1WNpfxzJbibUYBMia67LzLhxZAicKcdOhbs/640?from=appmsg)

嗯，成功保存......嗯？不对啊，我是不是把老师信息给覆盖了

                    ![](https://mmbiz.qpic.cn/mmbiz_gif/kA6wmJJAxibekD2bKz7Q1lPpicgUaW0AEwPDW0O7QyAQO95z33p9vPJZkoWWMAOhydzuZZ7M6T0lRs13hFzaePvnBkVxaiczE3SX4kCOkSKZ3k/640?from=appmsg)

给我吓得赶紧找审核说明

最后建议删除接口，保存接口谨慎测试，万一不小心造成破坏那就是直接进编制

             ![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/kA6wmJJAxibdYTpDic9eHrYbD0jKnUmdgEJe9phAIv4SgglutMPpXyRPAdUJzQic5HUJ0dDyzAoUaCYnUabQlwcX5FNEv9ZOJXKpe1ObKsSZWw/640?from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/S2ssjS1jNYubgVXbDj7a7yLrWSj5wn049MAa2YWQTaTu73p6JyYibAWgEutX21IZfH06RGOd7D6JXYJrckcC4QA/0?wx_fmt=png)

湘安无事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/S2ssjS1jNYubgVXbDj7a7yLrWSj5wn049MAa2YWQTaTu73p6JyYibAWgEutX21IZfH06RGOd7D6JXYJrckcC4QA/0?wx_fmt=png)

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