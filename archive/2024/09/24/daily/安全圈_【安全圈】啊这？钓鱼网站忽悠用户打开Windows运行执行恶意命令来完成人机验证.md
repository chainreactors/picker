---
title: 【安全圈】啊这？钓鱼网站忽悠用户打开Windows运行执行恶意命令来完成人机验证
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064619&idx=4&sn=60f7215bac0b36b350fcb79097c2c815&chksm=f36e672bc419ee3d625b6a49838a945d9486fbda0d9fc554ef5e74a900cf8681290013afc04f&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-24
fetch_date: 2025-10-06T18:28:24.219909
---

# 【安全圈】啊这？钓鱼网站忽悠用户打开Windows运行执行恶意命令来完成人机验证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhjvmwBHtTYHpyBYkicGjdiapbiaiaIsl3tJffAVh6TtTibvwnqArAIIKrFZxWE8H0CznDZuTPrZrwcAsA/0?wx_fmt=jpeg)

# 【安全圈】啊这？钓鱼网站忽悠用户打开Windows运行执行恶意命令来完成人机验证

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

网络钓鱼

有时候不得不佩服黑客这脑洞也是真够大的，竟然忽悠用户打开 Windows 运行然后在 PowerShell 执行命令来完成所谓的人机验证。

这个问题最初来自 Github，从上周开始不少 Github 用户收到电子邮件，邮件标题是他们的项目代码中存在严重的安全漏洞，点击链接可以查看详细信息。

当用户点击链接时 (钓鱼网站地址：hxxps://github-scanner.com) 钓鱼网站会自动弹出类似于 Google CAPTCHA 验证程序的提示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhjvmwBHtTYHpyBYkicGjdiapz6wX6eTjF6QLDLESjVBT7XsfHWl4ILXpHIuvxBMwaU5Kfub2H49h7A/640?wx_fmt=png&from=appmsg)

**如果点击我不是机器人选项，则网页弹出验证步骤：**

* 按 Windows 徽标键 + R (这是用来打开运行的)
* 按 Ctrl+V (此时钓鱼网站的恶意代码已经被复制到剪切板中，按 Ctrl+V 就是粘贴)
* 按回车 (用来执行恶意代码)

简单来说黑客通过这个钓鱼网站将预先安置的恶意代码放在脚本中，当用户打开网站时可以自动复制到剪切板 (还有这种权限？)，当用户按照步骤进行操作时实际上是在 Windows 中执行恶意代码。

这串恶意代码会打开 Windows PowerShell 并执行，然后下载名为 l6e.exe 的恶意文件，该恶意文件在 Virustotal.com 上能够检索到，属于 Lumma Stealer 恶意软件家族。

如果代码被执行则这个恶意软件会窃取 Windows 上存储的各种凭据，看起来黑客是想盗窃凭据来登录受害者的各种账户看看有没有具有利用价值的信息。

不过这种钓鱼方式能不能骗到用户是个问题，毕竟 Github 上很多都是开发者，开发者们显然知道 Win+R 以及 Ctrl+V 后输入框自动填写一堆代码的潜在后果，所以这个骗局估计也没骗到多少开发者。

来源：啊这？钓鱼网站忽悠用户打开Windows运行执行恶意命令来完成人机验证 – 蓝点网 (landiannews.com)

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhjvmwBHtTYHpyBYkicGjdiapgJiavpv5eqcRrRWGpN0xoQHXXBQpmoQqEJFScQuddpiaticbqlFlTO3TQ/640?wx_fmt=jpeg)[【安全圈】黑客声称对戴尔公司进行了数据泄露，曝光超过10,000名员工信息](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064597&idx=1&sn=b660f4bc1475f86930a2ea1dc89e683f&chksm=f36e6715c419ee0309ef48753b04421c6f6fe0e73e6820245171281b20d2f216648eac7e7c7d&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgiaaXeNGKfYJo9KNnBhco0Dr4y9Qha5HnpujmVqzrCskyLV4qQUMEFDdTeRZqbTo7n6Dhz80Xh84w/640?wx_fmt=png)[【安全圈】朝鲜 APT 在网络间谍攻击中绕过 DMARC 电子邮件策略](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064597&idx=2&sn=a3278f6d575dc09eb6874e7ec2d6bcdf&chksm=f36e6715c419ee0389ebda2affdd83addfd3cb93eaf29bb92ba15cb0fdb022e3ad9dbf4b2e59&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgiaaXeNGKfYJo9KNnBhco0DfViaolehrE0SLhFzVv5to0UbE4tlDmkibsOKGiaI44LubqLcdz7cK9ia4w/640?wx_fmt=jpeg)[【安全圈】警惕新网络钓鱼手法：虚假 CAPTCHA 页面诱骗用户安装 Lumma Stealer 恶意软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064597&idx=3&sn=10396f2711c45e64515ea2d5aeb8b048&chksm=f36e6715c419ee03936d3da0cdb3d3a6f96afe8fdaa6173dcaf004c1dce37846a39fa14a1220&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgiaaXeNGKfYJo9KNnBhco0DlQpAE9wbaGsQzLJNORNYLWKibH2xZ7XRicVFW209BYOiaSwjekSib0jHBQ/640?wx_fmt=png)[【安全圈】代号「神谕的黄鹂」Ubuntu 24.10测试版发布 将在10月10日推出正式版(非LTS)](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064597&idx=4&sn=f37b2475fd9a6fa85f486098df940ec6&chksm=f36e6715c419ee03e661e1699d1e0942843e1294495386adfb91f728bfc61a1dfebe49070ddd&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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