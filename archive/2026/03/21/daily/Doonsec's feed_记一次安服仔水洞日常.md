---
title: 记一次安服仔水洞日常
url: https://mp.weixin.qq.com/s/dH2m_Ta8DL4uVkiKwwsnFQ
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:13:38.084695
---

# 记一次安服仔水洞日常

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibRSlrHvGFOlRlEIZjRPxicRCibgUSWAq6CcxZia7s1N2MFCibn5G2nKtpfkNQahjw6kqWIXSGIIE8BPlMz79fIpsI5rJbsWkPDXxXX4icLDP2FibA/0?wx_fmt=jpeg)

# 记一次安服仔水洞日常

原创

Blimey029
Blimey029

N0n4m3 Sec

![]()

在小说阅读器中沉浸阅读

**郑重声明**

任何网络安全测试活动均须事先获得明确授权。本公众号文章的内容源自作者日常积累，未经许可严禁转载。本文所提及的技术漏洞均已完成修复，文中涉及的技术方法仅作教学交流之用，严禁任何非法用途。因不当使用而产生的全部责任均由使用者自行承担。本文讨论的所有案例与技术内容，旨在提升读者的安全防护意识，协助构建更完善的安全防护体系，有效抵御潜在网络威胁。

**前言**

作为一个安服仔，每日挖洞战绩：0高危、0中危、0低危，唯一收获是把目标站的404页面背熟了。别人挖洞：SQL注入、文件上传、RCE一键三连；我挖洞：扫了几天，全是404和WAF，洞没挖到，黑眼圈先挖出来了。

**正文**

领导一大早把我叫到办公室，语重心长拍我肩膀：“这个项目交给你，争取多挖几个高危，给公司长长脸。”

我当场挺胸抬头：“保证完成任务！”然后我转头开始一顿酷酷操作，打开Burp、挂上字典、调好POC，姿势帅得能直接当安全宣传海报，心里已经在脑补挖到RCE、拿下服务器、领导当众表扬的画面了。

结果现实给我浇了盆冰水。不是真挖不到洞，是刚嗅出点 SQL 注入苗头，参数一丢，WAF 直接给我拦到怀疑人生；好不容易摸到个文件上传点，后缀改了八百遍，要么403要么直接拉黑IP；看着似是而非的注入点，手贱一试，WAF比我反应还快，干净利落，半点机会不给。

一顿操作猛如虎，一看战绩0-5。高危没影，中危隐身，连低危都躲着WAF走。眼看交差时间越来越近，再交不出东西，不仅脸长不了，可能我的工位都要不保。

没办法，安服仔最后的体面 —— 只能开始水洞了.......

漏洞1：任意用户接管

前期通过信息收集，依旧登录框起手

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOnB1IkeW1gZXzvuSFZFYtIib4W6bsjrr5cicMNhJXcvkRvpSM4WIXuRK6ovO50tETvAHRichnyzL67BviaLeeQGJcAvk1o8xIYSlKE/640?wx_fmt=png&from=appmsg)

今天试了很多个登录框都无果，刚好这个登陆框有短信验证码，准备大开杀戒尝试短信轰炸、修改响应包，结果刚点击获取验证码，连bp都不用打开，验证码水灵灵地出来了

![image.png](https://mmbiz.qpic.cn/mmbiz_png/ibRSlrHvGFOk7zUTzZS0orzicdticamX4F2CwITUJLiccyvYyqThlQofcGO8yYeibBzZcVLAuhduhVprgVQIgspL29OXIBbBiaYjn0st2AsHn7KFc/640?wx_fmt=png&from=appmsg)

最后成功登录，也就是说对任意手机号都可以直接登录，从而造成任意用户接管，水洞到手+1

![image.png](https://mmbiz.qpic.cn/mmbiz_png/ibRSlrHvGFOlJiaLSFxUHvSIiaicAzoqeNClnYO5wRBFIkk763Sglt2TttEgzZoTHY3CZvpZEWBRcP3kxZ9PxNCmdDTgEGgkYNNlB62cCTRskpA/640?wx_fmt=png&from=appmsg)

漏洞2：xss-pdf

登录后点击更改头像

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOnfa3Yq6bENYS43U1xW52IpENaBeLsX2n73dw8IomF27A7WmunGA3rOtQnlwyJsw1eqIJVUcx9iathxYcSGm1Rr8FNUg9IX78a8/640?wx_fmt=png&from=appmsg)

修改后缀为php，心心念念的waf还是来了，尝试脏字节填充、大小写等绕过都一一无果

![image.png](https://mmbiz.qpic.cn/mmbiz_png/ibRSlrHvGFOmbOn4qczxXJdfOhwdQeRiboLU7HZLFqNfeDicvSDRtL3VfmIToxsfKavCqnF8fcT8qJlEv1VibIJyrbpeQAFnA8Al7Bxc7zNGmRQ/640?wx_fmt=png&from=appmsg)

尝试上传其他xss文件，html上传后返回文件类型无效

![image.png](https://mmbiz.qpic.cn/mmbiz_png/ibRSlrHvGFOmKn5uaZLWOy1hYyE2rGzIQLfCS0PdvibZj5bfJ1SOzULeN1dgfh7JicbjUrDmNIwf1EdCJHcKMN9e1iaNBdNAQC2uvOmeCWLt5Rw/640?wx_fmt=png&from=appmsg)

能上传svg

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOnsaCpEse7eYNqXIIJJNLSDTZPUibzqzstSEbSLKrV4z6nhIPgv070tHWyYapV3CaEsJpEFiaMnMpUsHkjnUHmhyica9z55l0RZwc/640?wx_fmt=png&from=appmsg)

但是不解析

![image.png](https://mmbiz.qpic.cn/mmbiz_png/ibRSlrHvGFOm5AibiahhmIkDLiaqKdj5ja4En2tfwU4ex4BR8vmLCnxPtl2U3mYwBMJSjhqiapdbLVblZcp9e9E1NnmHCaqmu5P2HOQSBeBgoAq4/640?wx_fmt=png&from=appmsg)

尝试pdf，没出问题

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOkrtngicsky9gdFPoTGlCDpUcJTpmokS4JxM4gCoWbJhgIRYO5ick48lrXNTiaNx1Hp0saeZ8X48DMMrpmWyrHPkVmGLLw1JnUcbw/640?wx_fmt=png&from=appmsg)

通过ai生成pdf正常文件的内容，再让ai插入xss

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOlrLgg5aVfhGUTGQhjfWyHnZ83OsqyJsJtjibn1wQ4eXdHkwDzOdiaEfypqIichey97iayfEibYjdE8Ap9YaiaaH2UQg578ktKLmnZDM/640?wx_fmt=png&from=appmsg)

不会吧，这水洞都被拦截了，安服仔的道心快碎了，好在还有ai陪伴着我，直接让ai来一手绕过，字符串拆分拼接，上传成功嘿嘿~

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOlmnKf6j17pRp3tjibVDGZu5scpxZq7cqq5J9CxjvO9qUNBbkjm5OEDWKjOxBjGOTl7d7Mw24iaUo7bPK2JfFjqmvkeHiaiar6rXKE/640?wx_fmt=png&from=appmsg)

成功弹窗，水洞到手+2

![image.png](https://mmbiz.qpic.cn/mmbiz_png/ibRSlrHvGFOn3MiaNxGVIcMFuBOtwtWYPLbd6d7mGOQWmoicZOIDQ32UnCyAo5JEHF771cxhUnk24NJwckgUyM0UJ9QjPFpNEwdYKjDIuklBtw/640?wx_fmt=png&from=appmsg)

漏洞3：oracle弱口令

干到下午，没啥精神了，直接工具开干

使用dddd对目标域名进行信息收集：

dddd.exe -t xxx.xxx.cn -sd

嘿嘿出货了，弱口令到手

![image.png](https://mmbiz.qpic.cn/mmbiz_png/ibRSlrHvGFOnHwzUnAnIerklwjH7ic9ede4HlL8ibYI39G9s3tpdKptSeywuFqakqaRTmodia9ibvnqnhlqzqicXSCAdW4VwBwkZDevVuueNJic49E/640?wx_fmt=png&from=appmsg)

用oracleshell工具连接，system权限到手，水了一天洞，最终踩到一次狗屎运了~嘿嘿，溜了溜了。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ibRSlrHvGFOkQcMpb2XbYAbr2tSRibuZp2cgMicgTxcM2XpWfiaUkfpBLwVUyujMs7zvQ5HVJlJc16Sg67aMlN4DaFnhFxh8iamI7kqjO2uCepgA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibRSlrHvGFOk4vKLXTWjrIZPKEo0tbM0ibmwqZMCfV8JoGO0uyRfwWHWlGvmEpwSwJLershUuqfNIJRhiafl9WQzIibFqUbtPDrGRehJtMahic40/640?wx_fmt=png&from=appmsg)

end

![](https://mmbiz.qpic.cn/mmbiz_png/ibRSlrHvGFOlk16e6bfu7VSzs36gXeXFZPCXaeU2U1CKujS5NeQXg7Wo3iamDibYBYo0D5U0CPF8KpI3KibXt30rdDwqxiaGnvxG5REgp8y4jYd4/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/8icmwDsB6dCoTibvjCxRlW0T8NO6ocVKrG61WUHkavD7Y3prcxc6uZpluD4GLs5CngzYfrxN2pAQ2utVw1ATFdlA/0?wx_fmt=png)

N0n4m3 Sec

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/8icmwDsB6dCoTibvjCxRlW0T8NO6ocVKrG61WUHkavD7Y3prcxc6uZpluD4GLs5CngzYfrxN2pAQ2utVw1ATFdlA/0?wx_fmt=png)

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