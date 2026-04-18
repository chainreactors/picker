---
title: 告别盲审，用Agent skill代码审计定位高危漏洞
url: https://mp.weixin.qq.com/s/eAkrurVXmoZY4IPjvlaoxQ
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:31:26.884042
---

# 告别盲审，用Agent skill代码审计定位高危漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/niasx7fyic9CM3CyO4GWQYM0QQvZPLzAnx6NuZpkoib3Fxg9MNlOoFk3vR7TzmyTTE5Qsz6c1jSAhoVckRsKiaBjc7xXCVcVSMcgCdu7e7wFLj8/0?wx_fmt=jpeg)

# 告别盲审，用Agent skill代码审计定位高危漏洞

原创

油漆工
油漆工

C4安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前言

这次审计的项目是老版本的 Java OA 项目-华天动力OA。

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COicyYJoqC6YCZ5a5wbr1aGJhTkE6STLvUVqAH07s6wD6sDUxLADz4Vff0Jx8YDtrfOaoQTq0iay7rp2wrsgfSGBWkuLVsDbC9cY/640?from=appmsg)![]()

项目的前端是 JSP，后端源码为JAR包打包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9COxibTtZn61S8jC092rGU7F82yVXceZNRahGpz1NtdsxOsQHFNQ4XDebAHsGncqtciaHK888icx8ibQAD6Ce1iaSq7fpPTHvicftwiaDQ/640?from=appmsg)![]()

这次使用的是优化过的代码审计skill：code-security-audit，吸取了几个代码审计项目的精华。

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CM1ibnpGw3BzXOwnC8PIBV5THsyWia4ISwMXRXpicmQbk9HCo3wR7qVakdibadMXtSeCdpVXmU03bdJRMoGztsvkewxJaIw6aGWtibE/640?from=appmsg)![]()

要提高审计效率，一个成熟的安全审计 skill 需要帮你分拣漏洞点并收集成结论。

下载地址：

```
通过网盘分享的文件：code-security-audit.zip链接: https://pan.baidu.com/s/1GAICnzpymHJFo7OepIUqVg?pwd=vwp7 提取码: vwp7
```

实战测试

在开始测试之前，我还给Agent准备了反编译工具cfr.jar工具

这次审计的任何结果，都按照输入输出进行验证，即 Source -> Transfer -> Sink。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPXNCFUVtcfoowPkJWszib06aRQuV4ibzpVjnsLSuYAs4bXDddqedVcnjgDAJ5BymLwhJAgYcUH6ViaR66t9riauLWTgiatQMETUMrs/640?from=appmsg)![]()

简单来说就是三件事：

* 输入是从哪儿进来的
* 中间经过了哪些传递和处理
* 最后落到了哪个危险代码里

​

在开始代码审计，我们需要让AI首先去审计前端的JSP文件，发现漏洞入口

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPJXYOB0Z6wEWkJZchJKDhAjmZ8T1VgjnjTaRkItXOQtKRCB4WvOnYNojxuzuyhibhznCenVcH1za3Jbj0ktLGTXpp9ibBty1RN0/640?from=appmsg)![]()

前端审计完成，开始审计后端代码补充验证

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CO9lUdGuIqQ227rI6jNsQXsH6y4ib0TJpQ5ibaIHZbBNP4znnOo1YdlLyxOSkqgRnLWYf0aL3ggI5AbGIUic6hP6oJojM5MzgVwOM/640?from=appmsg)![]()

![]()![]()![]()

​

整个流程审计完成后，来看看最终成果的报告

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CN2n4j6bicQ6mYDqHMj9ydibX0rUQvlqzCAtJn4iaM8LbAwEy3x1nvnWYXxt1PbrPics4pguv8AkZJTlBRMficAuoxgicMQEib8nXCbmk/640?from=appmsg)![]()

1. 从“测试页”到“生产可达的反射控制台”

最开始的一组页面：pageTest.jsp、pageTestService.jsp、pageTestMethod.jsp、pageTestResult.jsp。

顺着代码往下看，会发现：

* pageTest.jsp 会列服务类
* pageTestService.jsp 会反射读取方法
* pageTestResult.jsp 会拼参数，再去 invoke

看到这里，最多只能说“疑似测试功能残留”。

继续把对应后端 JAR 反编译了，用 cfr-0.152.jar 去看对应的类 JspFilter。

​

发现这个过滤器根本不是鉴权过滤器。它只是把参数里的 <、>、" 编码一下，然后就进行 chain.doFilter() 了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CP5GLkfjjNuTiau58DLqGoGdC7lbpRkSFhPwLpSibffCDYucRyfn3EoK8U198NgTtZzN0dxtklUURJ3xUJJaJg5UGZia43tysARM8/640?from=appmsg)![]()

到这一步，可以明确把这个漏洞写进报告里了。

​

2. 文件上传漏洞

第二个这个是真实存在的漏洞，网上也有公开的漏洞利用信息了。

前端 JSP 能看到存在多个 ntkoupload.jsp。继续往下看会发现表单里直接带着 newFileName 这类字段。再跟到后端处理逻辑查看，服务端逻辑基本就是：

* 接收 newFileName
* new File(newFileName)
* fileItem.write(...)

先把文件写到临时目录，再根据请求里的 filePath 调 moveFile(...) 复制文件过去。

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CODQ52QDicvsb68x1nD70v97CGm2edXSXbY4d7IcpzhrQuA0ibu2icSTMVqMVY2DxRN0TFdf3jUAzOmryGxMibHL2RFcLuf7sN8yeo/640?from=appmsg)![]()

3. 疑似漏洞

第三个漏洞是移动端的文件预览，利用前提是需要知道文件ID，但是其实利用难度很大了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CN2ibD6Tz91d7v76CsaBXxMI6MhAMfm61NoA9BDxrS21XI9qibNZIiaUOYQpDUmhkqZlbxsUbfgAzReibnr6YHekjic2NibL6JjwRs8E/640?from=appmsg)![]()

前端的 oapubptviewfile.jsp 接收 filePath 参数，然后按 pdf/doc/xls/html 走不同的预览逻辑。

整个功能的流程如下：

* htmlToHtml(filePath) 会按传入路径去处理文件
* pictureToHtml(filePath, fileType) 也是一样
* pdfDatToPdf(filePath) 也是一样

按用户传进来的服务器路径读文件。

继续往上追踪代码，HtEntranceService 有 token 处理，再看看 HtFileService.getFileTempPath，结果发现它甚至没有真正利用传入的 userInfo 去做约束，很多逻辑只认传入的 fileTempId。

总结

这次审计发现的漏洞比较典型的是下面几类：

* 生产环境残留反射式测试控制台
* 上传接口信任客户端传入的服务器路径，导致任意文件写入
* 移动端文件预览接受物理路径，导致任意本地文件读取
* 多个查看和下载接口缺少对象级鉴权
* 多处未转义输出导致 XSS
* .p12、.keystore 这类敏感证书文件直接放在 Web 根目录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPfKWAVR9VqichcJ5xa4rUN7YwzibCDc8dr3U9UezaTXticJfCNgMQMicias6tsHtuzRVbf3ibWxvv1hTf8STJ26cjUqDQHkraP5ba7k/640?from=appmsg)![]()

感兴趣的师傅可以公众号私聊我进团队交流群，咨询问题，hvv简历投递，nisp和cisp考证都可以联系我

内部src培训视频，内部知识圈，可私聊领取优惠券，加入链接：https://wiki.freebuf.com/societyDetail?society\_id=184
安全渗透感知大家族

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CM2ia325A0dvxuiaP7ZkTtzVficzWPRjE9Y5QXKTqZDowoA5quwnBbOw4PQDO6nZW4SkZ59DgyKSibLgTbKgJj1sahuANz59CAl6jU/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=25)![]()

（新人优惠券折扣20.0￥，扫码即可领取更多优惠）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9COSia7AROqpgDSO5lYYNmyypvhpYfYQpxheibfSAEbGhMtpibNvjgqddcliaykon74LkPnRsdcqB72pIQvCFM99WrEo8n6lprmAohA/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=27)![]()

![]()![]()

加入团队、加入公开群等都可联系微信：yukikhq，搜索添加即可

END

![]()![]()

​

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQiaZKk16p8ASnxuOUZiaJWeVzm5jndulrhBy63D46ic8H6lq8tpJfXTCNEhUeq9LckNiaObB9Auiaicp2Q/0?wx_fmt=png)

C4安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQiaZKk16p8ASnxuOUZiaJWeVzm5jndulrhBy63D46ic8H6lq8tpJfXTCNEhUeq9LckNiaObB9Auiaicp2Q/0?wx_fmt=png)

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