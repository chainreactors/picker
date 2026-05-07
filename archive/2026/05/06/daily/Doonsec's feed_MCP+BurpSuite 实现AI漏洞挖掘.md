---
title: MCP+BurpSuite 实现AI漏洞挖掘
url: https://mp.weixin.qq.com/s/qbVvalyDCVG1GM01LXZxUw
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:26:03.520041
---

# MCP+BurpSuite 实现AI漏洞挖掘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hdDfdnLnPdvpcViaxpuicnOpJfdZrh27wxG8TSpibiccNcc3JBdAjobYD0BewDd9EJKDNJhQCP6iaKfAjoP8RvRVrYGl0icvN4WAzQFN8GghR8Sho/0?wx_fmt=jpeg)

# MCP+BurpSuite 实现AI漏洞挖掘

原创

\_7ingLian
\_7ingLian

偏远酒馆

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hdDfdnLnPdtvzJdBF61sCfrmnJ9GtSibSftPVdCHibiaa4T2Gl3RcU9SN2s3kcticK04albEhia5VdlZnHDWcIdgw1I8UeFheGolFOjGTOkAh77Q/640?wx_fmt=png&from=appmsg)

--->目录<---

0x01——MCP简介

0x02——MCP + Burp 实现AI挖洞

|  |
| --- |
| 0x01、****MCP简介**** |

--->MCP AI"的指挥中心"

MCP（ModelContextProtocol）是由Anthropic开源的一项技术，旨在简化AI与外部工具的交互。通过MCP，AI可以自动访问和操作浏览器、文件系统等，从而提升工作效率。

**--->**

**这里为了方便就直接用Trae的MCP**

![](https://mmbiz.qpic.cn/mmbiz_png/hdDfdnLnPdumSdhsO4umpSyC5CPuLvH8HOGiaJdYk3Gs1DsgTW9yxKSBOdbMBnzS9Vdibnh7TMDhP0IYHhibMQkiaY7kiaLLr3yicS3M3R4XDhAgI/640?wx_fmt=png&from=appmsg)

**手动添加**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hdDfdnLnPdvmkbtbL7Jw0iaibmxVefKSia396CJb3gEPRyqdS90cLjmSmO1sYWzBOZp32JCvptRXu8ibVIibibm44iapfsM54PO54K2ibGR0lTA8IMo/640?wx_fmt=png&from=appmsg)

```
{  "mcpServers": {    "burp": {      "url": "http://127.0.0.1:9876"    }  }}
```

配置简单几行就行了。

![](https://mmbiz.qpic.cn/mmbiz_png/hdDfdnLnPdsrznPkUDwVb6UbOiaxKryMNp51xeZU9UYjqK2ulqQFdIeESerFiajA1PECDTL92J9l2j9fRfC4p9OsdkSzX2B6a9eG1VYhiay538/640?wx_fmt=png&from=appmsg)

确认的时候不报红就说明正常

接下来启动进入burp，搜索MCP插件安装

![](https://mmbiz.qpic.cn/mmbiz_png/hdDfdnLnPds9epSpVy2DDZ45e5q2jxGJm5nMj1WuI0JNo6PNjibrkNzibrPFYxPJz8Y948cQsAxs2yYyY6ZU3Pu0XmuVyf9hAyTpYzJGg3Yrk/640?wx_fmt=png&from=appmsg)

安装好之后，除了勾选启用，其他配置不用动

![](https://mmbiz.qpic.cn/mmbiz_png/hdDfdnLnPds9GI5kTSdibuwEwiaickKuP5Micv1FI3lRgDb4CCV4MwISIQP8jB9EVdRNzCra1P7mdI04EmfTYia8wJialYUVgwqOLvES5PzoicRKb8/640?wx_fmt=png&from=appmsg)

|  |
| --- |
| 0x02、****MCP + Burp 实现AI挖洞**** |

--->

检查各项都没问题

```
curl http://127.0.0.1:9876
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hdDfdnLnPdsF1qgJibCvViaXUrMjwNB4TqX9ZHbqOIMDiaR879dFW1ZBmOK3icG7lO3saUqut53ym6Aia3RCM71wBeBVOaicMZMCAlZs4rC9NZgwg/640?wx_fmt=png&from=appmsg)

在对话框上面选择MCP

![](https://mmbiz.qpic.cn/mmbiz_png/hdDfdnLnPds3UvkpwX2NribHYXoeibdmEaFRYJPbPpibosNic9Q7tpNSy8Qadzs8GoJzRHlVdVVoFsZqF6Ln3ub6UKBqGfdWY0sVRHRT3ThTToc/640?wx_fmt=png&from=appmsg)

模型根据自身需求自行选择

![](https://mmbiz.qpic.cn/mmbiz_png/hdDfdnLnPdtY8J7ESJia9loCOQozA1k9nK7VTmdkvRKsJzCvJNvW6xwUvPoicjoLRljMZtE00qSvYuibBjoC0vZFngic2kmJkzqc1fkJRRWicYsw/640?wx_fmt=png&from=appmsg)

接下来就是测试mcp是否和burp打通了，调出帮助文档

```
“列出所有 Burp MCP 工具及其功能说明”
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hdDfdnLnPdsKmm4xd6RWIYFZ1hbIeicOcdeicRk4P6AZ0GcQe6dIHHEU0nXeVCjMNLAI385jpuS37u2CBXUVoyQyHAvQ39PibDSExuWmlMvs3k/640?wx_fmt=png&from=appmsg)

如果直接问的话可能就触发安全机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hdDfdnLnPdvAVaJmYHbKuQ5OwdPAO0ImMibkia4MR4KA9WFuX13zpiaZFaZG79s62onIyibiaGaXqnDweFuQ4iaXlmDcrmqF8oNmpFf8Jxy6wdnxM/640?wx_fmt=png&from=appmsg)

测试扫描

![](https://mmbiz.qpic.cn/mmbiz_png/hdDfdnLnPdsD12Fhr4u8ntia1WOH6Cg5H60ibyQrylC9M4GUO7gpuDOYeflE6sErQSKfEdY9DEu2sYGf2jiaBq6SH2HuCBLQO51PKIBvWEzvWE/640?wx_fmt=png&from=appmsg)

会弹窗确认，允许即可

![](https://mmbiz.qpic.cn/mmbiz_png/hdDfdnLnPduFGZaPYBSXtUN9oibmtLFQdBstVuYk3Hpau7MS6sfwXZqmia0lkTOmxuGS8rDDcqlK5QlzoUwib8LC8Ca2PIHpkw8zzznLzTWRpw/640?wx_fmt=png&from=appmsg)

end

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6ibqWGD93gcoYQiaQicJQ1VKNg4Kw3XCNqdcvB38Doclzico8wib6AryfObbv5hibibjuOfiahYmF6lqrLiaUbmPntVRdibg/0?wx_fmt=png)

偏远酒馆

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6ibqWGD93gcoYQiaQicJQ1VKNg4Kw3XCNqdcvB38Doclzico8wib6AryfObbv5hibibjuOfiahYmF6lqrLiaUbmPntVRdibg/0?wx_fmt=png)

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