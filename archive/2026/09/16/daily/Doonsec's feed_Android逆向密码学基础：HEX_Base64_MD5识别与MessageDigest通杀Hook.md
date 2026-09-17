---
title: Android逆向密码学基础：HEX/Base64/MD5识别与MessageDigest通杀Hook
url: https://mp.weixin.qq.com/s/C0YObLaoWTFZjXZRkCZ4kA
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:57:20.637120
---

# Android逆向密码学基础：HEX/Base64/MD5识别与MessageDigest通杀Hook

# Android逆向密码学基础：HEX/Base64/MD5识别与MessageDigest通杀Hook

哆啦安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于零基础学逆向
，作者凉子不会玩

![](https://wx.qlogo.cn/mmhead/qd3u5IHSYT9vxYOhWfqJkRYX5LeKbQWOTIhqib7e1YZDgj7GtKmxeiavRypfUia9zemqV45BSdCCb4/0)

**零基础学逆向**
.

凉子✨分享逆向学习日记✨

[APK逆向分析工具V1.2](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247500004&idx=1&sn=2f5e5c2dd1083c8f194ba35633b4e358&scene=21#wechat_redirect)

[APP逆向分析工具V4.5](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499437&idx=1&sn=d16d6e56aece786a75b2783c0ad2fd7b&scene=21#wechat_redirect)

[APK安全加固平台V5.2](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499425&idx=1&sn=f92ff3d7add367c335b2164d2408912a&scene=21#wechat_redirect)

[Android so逆向分析工具](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247500228&idx=1&sn=cffe1fc82ba058401d8309b1f0a918dd&scene=21#wechat_redirect)

[Python逆向分析工具V2.5](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499173&idx=1&sn=5d01c14376a5507ca8cd6513d73c9544&scene=21#wechat_redirect)

[Unity手游无Root注入工具](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499408&idx=1&sn=5260012899e6425667e8d24a354dd9d7&scene=21#wechat_redirect)

[Android病毒分析工具V3.2](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499561&idx=1&sn=caaed291dda8a9f4fd43a7dd7104c8f0&scene=21#wechat_redirect)

[APK逆向智能分析工具V1.3](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247500133&idx=1&sn=593805278f71b91e022570c4d92f5874&scene=21#wechat_redirect)

[App涉诈取证溯源分析V1.5](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247500406&idx=1&sn=fb5917edcf9ffea159647ebbbe1794d3&scene=21#wechat_redirect)

[Android智能取证系统V1.1.8](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499290&idx=1&sn=20c1ede489fa06badb12657eecb2cd0d&scene=21#wechat_redirect)

[Android逆向智能分析工具V1.4](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247500224&idx=1&sn=a40dc241928ac2c2d28ac9106856df3d&scene=21#wechat_redirect)

[Android智能调试分析工具V7.5](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499445&idx=1&sn=f96192373e9e1b97cf3f3ccaa342542d&scene=21#wechat_redirect)

[Android逆向智能分析工具V1.5](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247500654&idx=1&sn=ab2480065c850964245138264a9007e2&scene=21#wechat_redirect)

[Android安全智能分析工具V5.4](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247500712&idx=1&sn=27ae652deec44f7f7829c17ba02d198d&scene=21#wechat_redirect)

[Android病毒智能检测分析工具V3.6](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247500576&idx=1&sn=b985155458d76f30d3fefd8209488dcb&scene=21#wechat_redirect)

[Python字节码反编译工具(逆向分析)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247498440&idx=1&sn=f7261eba6f21742ca4e1da1e2da4ce3c&scene=21#wechat_redirect)

[Python字节码反编译逆向分析(高级篇)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247498532&idx=1&sn=1120b97fcd9f69afff065d31956e6ab7&scene=21#wechat_redirect)

[Android Apk逆向分析工具(jadx-ai-mcp)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499459&idx=1&sn=f2d28d2957373ad15deb88a321038162&scene=21#wechat_redirect)

[逆向交流群|Android智能调试工具(下载地址)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499472&idx=1&sn=0b0a5245ce898f0a53aaa6a36bdd4a6b&scene=21#wechat_redirect)

[Smali/AAR/JAR/DEX/APK逆向分析转换工具V2.5](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499404&idx=1&sn=4557961adf884684f5d71f7761fabdce&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Wxusn17ibicDYgiaULGpK9eo1ytSYicb5E970ecZsIG9aKE15krN0aT5xibvrN9zaYtU5rrublwo8VqBLyfJ4TlJjTYX8TPCn9ponZmoSyqGGBFs/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

[iOS三种越狱方案](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247501254&idx=1&sn=473b5f486697be5d7bf0563200fefcac&scene=21#wechat_redirect)

[ChatGPT或Claude官方套餐IOS渠道直充服务](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247501303&idx=2&sn=f537651500c84b8161666e5e5c21593d&scene=21#wechat_redirect)

[iPhone 8 Plus越狱终极指南：A11芯片全版本方案与避坑指南](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247501310&idx=1&sn=6eb0502a2ccfa4f730ca029fc6967375&scene=21#wechat_redirect)

[Ubuntu20.04通过libimobiledevice工具链连接iPhone 8 Plus](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247501303&idx=1&sn=44c83c42faf02af96fb5ff7ddd23fc67&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Wxusn17ibicDakmp0ZCTxFLSfu817JJGP9BJenibIXtsGY0rDSYsUXBWxvyHUSoUXQhdSISSQL0fiam7twQd1yVU0cVy1QjWJP94RAYEPxVNRKY/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

[ChatGPT官方套餐直充VIP服务](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247501180&idx=1&sn=f8e3fb2b0c4336b08818c76fb6208635&scene=21#wechat_redirect)

[ChatGPT或Claude官方套餐IOS渠道直充服务](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247501242&idx=2&sn=d1d258b01a06cee3eebe4a030320842e&scene=21#wechat_redirect)

[ChatGPT和Claude官方套餐IOS直充(操作方法)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247501198&idx=1&sn=f2665eb9efb60eaf18c8898d135fcd5c&scene=21#wechat_redirect)

逆向工程密码学（一）

密码学基础与通杀：HEX、Base64、MD5、MessageDigest

抓包分析中，未知参数的生成逻辑通常分为三类：随机数、标准密码学算法（编码/摘要/加解密）、开发者自定义实现。在未确认算法类型前直接对函数名逐个 Hook，效率低且容易遗漏。正确路径是先依据码表特征与输出长度识别算法类型，再在 MessageDigest 的 update/digest 上部署通杀 Hook 截获明文。本文系统梳理 Android 逆向所需的密码学基础：HEX 与 Base64 的识别特征、摘要算法的长度判定、MD5 实操与加盐处理，最终落地到 update/digest 全重载通杀方案。

[Android安全隐私合规智能检测工具V5.6](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247501350&idx=1&sn=1b6710f29c7f34f13c4908237fa67347&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/5apd3cOqaW3AF5rzBiaRJnK3bP1qhibFURTpgg93R897bWVM6NVXKYug121RcnJLrdCQAJjWkLB6TlKCKNMbREnvc8YvqYRuOJLtEe9W1eeMI/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/5apd3cOqaW0Gthjwwtjqz7QyR2wZGvuLUia87rrAqJmASCtONCPWAkXB5tCL4yGbtQv4VI58p4qiadnS5lJDTUd79GDDa4ggew9EHmVPjzuCs/640?wx_fmt=jpeg)

一、为什么要学密码学

客户端到服务端的数据包里，总有参数你不知道怎么来的。三类可能：随机生成、标准算法加密/摘要、开发者自写逻辑。认不清类型，后面 Hook 再猛也像盲人摸象。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5apd3cOqaW0MqGickiap45Hhd8FvC2FRZzqbnBWPhBCK5yJGhR58aotwkaMgf5Q8usf2ETkyGNO2DB6uibtKTxwlmVuBXrV4W0SZnm2HwdzzFs/640?wx_fmt=jpeg)

二、加密落在哪一层

Android 上常见三条线：

Java：有系统 API，方法名相对固定，适合按名字定位。
Native（so / C/C++）：没有统一系统 API，可自实现或接模块，名字还能混淆——更要靠算法特征识别。
JavaScript：同样没有现成系统 API，多用 CryptoJS、jsencrypt 等第三方库。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5apd3cOqaW2TPsBqqG8zibtanRPMSo5E4ibONMfAc1XuKNCyT66uDvQurrNc8lOvHPMRzvt7fot4gTrUXm2ichTcQ48zoXz87wlDtiaBruCTRZQ/640?wx_fmt=jpeg)

三、密码学里先学哪些

消息摘要（Hash）：MD5、SHA、MAC。
对称加密：DES、3DES、AES。
非对称加密：RSA。
数字签名：MD5withRSA、SHA1withRSA、SHA256withRSA 等。

标准算法在各语言里的实现结果应当一致——Java 算出来的，和 JavaScript 按同一标准算出来的，应对得上。这对「本地复现 / 对照验证」很关键。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5apd3cOqaW0FciaF0Nt13YbgaH8QAzbLujCRaTEPwIN2DWpOMNPbMYQdUrNmVzVugIyRfjtV5NfJfLNMtu1jXROQCQ5CULIWFBYX0wnEHsgs/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5apd3cOqaW138t10mexDFoTPEXdnZwnEIzc87UaAH6fERW9Libcu4x5DQdQibV6kPORoJVxWgb9GLfvT4dbaIKFzoztXn8gH4HtbksyQRF1to/640?wx_fmt=jpeg)

四、标准 HEX 与非标准码表

摘要、密文算完往往是字节数组，要给人看或传输，常编码成 HEX。标准码表就是：0-9、a-f（或大写 A-F）。实现上常见一张 16 格字符表，按半字节查表拼出字符串。

非标准 HEX：把表改掉，例如前几位换成 q、w、r、t、y……逻辑还是「半字节查表」，但肉眼不像十六进制。逆向时看到怪字符「编码结果」，先搜码表，别一上来当私有加密。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5apd3cOqaW1Wnmdcu7FbRlkbtseMpITeX8WDIgvgOeIfJicdYScUBxCJ3EBsNPO0WusMPVacO7aq1pg9cZvibssVWZaJ3NK6wtNDkKQiaTyCkA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/5apd3cOqaW0WVhGRmwcYkws0Ult4FqwCqClrxZtsiaqJias025xezRt3CWLrChZKWdN8m7cTicpKSf3M6iaa068icMDdsPvcphaVEiakOPYZA1C4w/640?wx_fmt=jpeg)

五、Base64：编码，不是加密

Base64 用 64 个可打印字符表示任意二进制：A-Z、a-z、0-9、+、/，以及填充 =。它是编码，不是加密——可逆、易解码，不适合当「保密手段」。

RSA 密钥、密文字节、图片等含不可见字符，直接当文本传容易乱码、截断。Base64 把它们变成安全文本。细节上：每个字符约对应原数据 6 bit；编码后长度常是 4 的倍数；原字节数是 3 的倍数时可不填充。

Android / Java：android.util.Base64、java.util.Base64（高版本）；OkHttp/Okio 里 ByteString 也有 base64()。Java 层可按方法名快速定位；so 层更多靠输入输出和码表特征认。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5apd3cOqaW2bVY9IibW2mGWM51e1Nx5RBibFRvpzVYLLqffYEjU2xbgtxpBNBQiab0wg05ml3ywpOakeZB3x0XQv2h1awqjQlMXjBicqeHicLEiaM/640?wx_fmt=jpeg)

六、URL 场景下的 Base64

标准 Base64 里的 + 和 /，走 URL 时容易被弄成空格或歧义。...