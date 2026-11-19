---
title: 干渗透需要会逆向吗？平常网上提到的“JS逆向”到底是干啥？我们从中又能得到什么信息？
url: https://mp.weixin.qq.com/s/QvC6bHLjxhZgkZ-fDSKzpw
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:44:48.471731
---

# 干渗透需要会逆向吗？平常网上提到的“JS逆向”到底是干啥？我们从中又能得到什么信息？

# 干渗透需要会逆向吗？平常网上提到的“JS逆向”到底是干啥？我们从中又能得到什么信息？

原创

是老A
是老A

老A搞安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/G9k4hwPicmFQnax8vwSEBozW9kTQxVCUVCJ6lN1lZW8kelM5IJ5AUgF8ek1xQk5vV42mPDvVibZbDGb0NTvPmvvkCjM5xS4K0CSAial3QNqjKk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G9k4hwPicmFRxM0kDCFMDKqngNO1HZibjVAKoVes7XkPAfpc8BvtbZx9IKuDR3A5ATStqzEydSM2oPakAAVlDJFrnSibPibbicntW2W5Ow4PZRiaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/G9k4hwPicmFSI9Pp0F1xib54FgrVDOZYHVdYyTN6R5M3uaAL90LXMFFOD1NbG5zlSyUSzyicBmYunnQyy1ztbjYq68LvZQn1UjlTwOjVAJb5GA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/G9k4hwPicmFSFIhR73HE6mBuREMiaCvU13pxSnyIxAmIvkjq6wEec2uRm1lfw6ibyA6DznHfxedWIaSCDcVukfXMSEuttoicLHGibvsXP5L9Jnqs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/G9k4hwPicmFTMKnkwbERAC7KliaZKvzBZEjeLdvxUia4dCp1eSF6fIWYHuAQiadL3bNHve26dUz0cH2zmvsf9CQBblCYtt9Tl94cM8CyCTK7Oiac/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/G9k4hwPicmFRTPfvJMYibXhiaXib2GEgsXycXzOwSH89blLhSJqxeNP2HBhR88NibPRYrtIgbrP5l3VJIkiciaPljAuibx0SvR9cpK0ElzUT99GuelI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G9k4hwPicmFQdsQVNtGvQhs2TTC1iaf5jWMtPKCLCmRYAJPlsNOicgs4VvhRy3ic6mYU7zOu1j75gFQnqEHxCibvlcShAQch4xKkuRCFUgrVpvNE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G9k4hwPicmFRiay3ONIfLzMrP0hfDQgicqBJEDXpMyWnPUM0ByoUE4AFsxvwD68xcR5ichXOF89pXRVLsrDaG6B4Z7vhCNZiajI8tC0v57W4d4pA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G9k4hwPicmFRjE52Eiand1bZ1WxyNSWuiazdvxnSskRcc8h9vvODtbIyQ6nB3baiaMpibogWXTDj38BCC8jDQdS4Xm0eEStKNa2eribvNiaVbYSQZI/640?wx_fmt=png&from=appmsg)

一位深耕网络安全的老兵，目前是一家安全公司的技术分管，擅长渗透测试及安全培训方向，老A的愿望是大家没烦恼，一切顺心！

![](https://mmbiz.qpic.cn/mmbiz_jpg/G9k4hwPicmFQ80LAD1ia5s5jZIQLIuktzRlEDItVicKzJUdW6vib2mdHFpKNTmD1TFlzQfu0vdI8JKh9OsmFPZfRglpCdF7PH8XjDSCKqdkXlS4/640?wx_fmt=jpeg)

REA逆向辅助工具，近期比较火的开源项目，估计大家都有在关注！我们团队也有在研究，刚好近期有伙计问了逆向相关的一些疑惑，借着这个问题，来说说那个经常被提及的“JS逆向”究竟能帮我们挖出什么宝贝

对于渗透工程师来说，逆向是绕不开的必修课！

渗透测试大致分两个大方向：Web安全和二进制安全

搞Web渗透的， 以前写个脚本跑跑SQL注入、传个WebShell就能拿分，确实不太需要逆向。但现在很多业务越来越复杂，防御越来越深，“JS逆向”已经是Web渗透的核心竞争力之一了

现在稍微有点安全意识的后台，接口全加了密、请求全带了签名（Sign），你连包都改不了，还测个锤子？

搞二进制安全的，那逆向就是你的饭碗。不管是PC端的exe、DLL，还是移动端的App，或者现在的车联网、IoT设备，你得把程序拆开，看懂它的底层逻辑，找出内存溢出、逻辑漏洞等等

所以呢，干渗透不是“必须”会逆向，但会逆向的渗透工程师，往往能打到别人打不到的地方

对于“JS逆向”，很多人脑子里浮现的就是满屏幕的汇编代码、十六进制数字

额……好像是这样，但又不全是！

其实JS逆向非常接地气。它针对的就是我们平时访问的网站、小程序、H5页面里那些前端代码，像.js文件这样的

所以呢，JS逆向就是扒开前端的伪装，看看开发者在浏览器里到底写了什么“小秘密”

前端的代码最终是要在用户的浏览器里运行的，这就意味着它是公开的、可被下载的、无秘密可言的。开发者为了不让别人轻易看懂，或者为了拦截普通人的抓包，会进行“混淆”、“加密”、“反调试”。而我们做的事情，就是把这些伪装脱掉

然后，从代码里扒出这些对渗透极具价值的信息，例如：

1、加密算法与签名逻辑

抓包时，经常看到 sign=8a7f3c... 或者密码被加密成一串乱码。不搞定这个，你连正常的请求都发不出去。找到生成 sign 的算法（MD5、AES、RSA等），把硬编码的 key、iv、salt 抠出来。有了这个，你就能用Python自己复刻一套算法，想怎么发包就怎么发包。越权、爆破、遍历，大门彻底向你敞开

2、挖出深藏的“隐藏接口”

扫描器字典再大，也跑不全人家自己写的内部接口，所以直接在前端代码里搜索 api/、admin/ 等关键字。那些在页面上没有入口的“测试接口”、“管理后台接口”、“导出接口”，全都在代码里躺着。拿着这些地址去测未授权访问，一打一个准

3、发现硬编码密钥

开发者图省事，经常把一些敏感信息写死在前端开发者图省事，经常把一些敏感信息写死在前端。这时，我们可以提取云服务器AK/SK、短信接口密钥、数据库连接字符串。如果运气好拿到一个权限没配好的云厂商AK，整个云资产可能直接沦陷

4、戳穿前端校验

前端限制你上传文件只能传 .jpg，限制你手机号只能输入11位。JS逆向能让你看清楚这些校验只是前端做个样子，还是后端真做了拦截。如果是后者，直接绕过前端发原始请求，说不定就能搞出任意文件上传或者超长数据溢出

JS逆向，确实能够给我们找到更多的突破口！这对于渗透工程师来说，这不得两眼放光啊……

所以，这部分的知识点，值得大家深入研究！！！

⚠️ 法律声明：以上内容仅供安全学习和授权测试使用。未经授权的漏洞利用属于违法行为，请勿对未经授权的目标进行测试

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yRlVX6hokHTD0R0IqVL5NIibwRtGVDicfvibw9BUUibTKx8iardZgXZIyNwGfu9uYnlic69ppKSe4lEmdEYZ8eGtgozw/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过