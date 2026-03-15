---
title: 【大洞速修】http协议、chrome浏览器等组件严重漏洞披露
url: https://mp.weixin.qq.com/s/7_irlfOZc6r875ssacXbxw
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:25:15.573580
---

# 【大洞速修】http协议、chrome浏览器等组件严重漏洞披露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PbqGHl550jjWNYEahUQB4EbJ5ibGypoGfPFDfBegIJLSJwkhzKagDK7JiajwtZbVw7ZgbUqzDTicZc10g2SwaHezovQDibiceIHXMgOoBKGPH3G4/0?wx_fmt=jpeg)

# 【大洞速修】http协议、chrome浏览器等组件严重漏洞披露

原创

小火炬
小火炬

小火炬sec

![]()

在小说阅读器中沉浸阅读

> 参考文献1
>
> Feng Ning，公众号：AI-security-innora[位置被秒偷！10多亿人每天在用的国民支付应用，17个「正常功能」细思极恐！](https://mp.weixin.qq.com/s/xEBEYZlap3xuDMURuJd7_Q)

> https://innora.ai/zfb/
>
> 参考文献2

一个链接，通向一切

不负责任的披露时间线：

我懒得遵循负责任的安全研究原则。在公开任何信息之前，没通过任何渠道向任何集团进行任何报告。

2026.03.14 2:30

发现安全问题

2026.3.14 19:20

懒得报送产商，详情面向公众公开

已验证安全问题

CRITICALV-01

谷歌浏览器rce漏洞：

通过

location.href='https://chromewebstore.google.com/detail/bookmarks-quick-search/[插件id]' 允许外部页面打开谷歌浏览器插件安装界面， 虽然最后安装仍然需要用户手动确认，但配合 UI 欺骗（V-08）和社会工程，用户误操作的风险极高。

```
<script>location.href='https://chromewebstore.google.com/detail/bookmarks-quick-search/[插件id]'</script>
```

UNKONWNV-02至V-06

没发现对应的，先留白，对齐一下格式

HIGHV-07

网络ip精确定位窃取（无用户感知）

发现http协议向服务器回传用户ip，连接建立后回传时间<1ms，可以导致用户被精准定位

HIGHV-08

UI 欺骗: 虚假提示通知 + 标题篡改

chrome浏览器可以使用iframe标签嵌入其他网站，同时可以通过JavaScript的alert函数弹窗告知用户比如“安装插件否则浏览器无法使用”，使用title标签修改标题为“fbi插件安装”等。

HIGHV-09

OAuth 授权流程劫持

任意OAuth应用都可以被授权劫持，通过修改redirect\_uri参数发起OAuth授权服务调用。虽然未成功获取授权码，但弹出了"redirect\_uri错误，请联系管理员确认"弹窗，证明请求到达了 OAuth 服务端。

HIGHV-10

零交互暴露浏览器地址和历史记录

通过chrome://伪协议打开chrome://settings/addresses，可以直接打开谷歌浏览器保存的地址页面，显示 美利坚合众国华盛顿特区宾夕法尼亚大道1600号 。chrome://history/ 页面暴露20+ 条浏览器历史记录，无需任何额外确认。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/0AaE0v2rpSpRgD4dxQbSNkDUfTFoTS3yz9hndwtDMKK69OoAz4uKpic5xLQxC0fIQ50wEL2pdicmULbWg1eM9kEg/0?wx_fmt=png)

小火炬sec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0AaE0v2rpSpRgD4dxQbSNkDUfTFoTS3yz9hndwtDMKK69OoAz4uKpic5xLQxC0fIQ50wEL2pdicmULbWg1eM9kEg/0?wx_fmt=png)

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