---
title: 小技巧！利用条码扫描器快速修复CrowdStrike引起的Windows蓝屏
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514362&idx=1&sn=9f9cc70b5a7b47ce792b4aa9e196cdb8&chksm=c144ca47f63343512cc5e9d9808f670effac9b96587a53cdeba382b650e79b9408c7cb3d58ed&scene=58&subscene=0#rd
source: 数世咨询
date: 2024-07-27
fetch_date: 2025-10-06T17:43:23.440020
---

# 小技巧！利用条码扫描器快速修复CrowdStrike引起的Windows蓝屏

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqrXJOcAym9Txd8SXyYpsl5tWw09O8eoXfp2vErbtg3H3P5UgksJlPj1qfPlFB27euzyeibtOTfiaiaAA/0?wx_fmt=jpeg)

# 小技巧！利用条码扫描器快速修复CrowdStrike引起的Windows蓝屏

数世咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqrXJOcAym9Txd8SXyYpsl5tky142MuV2NMutibJHSR1g7T0pfRiaNtlThZV82UU4iaIpnd4ibI78gicIgQ/640?wx_fmt=jpeg&from=appmsg)

上周五，澳大利亚Grant Thornton公司的 Windows 电脑和服务器开始蓝屏死机 。当公司试图解决 CrowdStrike 造成的混乱时，这一知识点变得非常重要。Grant Thornton公司有数百台电脑和不少于100台服务器被 CrowdStrike 错误更新陷入恶性循环。

高级系统工程师Woltz 记起了一个关键的事实：电脑启动时条码扫描器与键盘没有什么不同。而Grant Thornton的所有机器都使用微软的BitLocker 工具进行加密，这意味着恢复时需要先输入48位的BitLocker密钥，然后在进行多步骤修复。

公司优先恢复了服务器，并手动处理了这一任务。IT经理Watson 和Woltz认为，公司电脑数量庞大，不能手动处理，需要自动化的解决方案：

1、自动化措施不能包括分发 BitLocker 密钥——这样做风险太大。

2、不能通过电话或亲自读取密钥，将48位密钥读给蓝屏使用者不是一个好主意。

3、这时，Woltz想起来了条码扫描器的事情。公司拥有所有电脑的BitLocker密钥，于是Woltz和同事编写了一个脚本，将它们转换为条码并显示在一台锁定的管理服务器的桌面上，该脚本会接收主机名并生成必要的条码和LAPS密码以恢复机器。

于是，高级系统工程师Woltz 马上去了一家办公用品店，花了36美元买了一台现成的条码扫描器并插在需要修复电脑上，然后重启电脑在要输入BitLocker密钥时，用条码使机器扫描服务器屏幕上的条码实现自动输入密钥。这比每次手动输入速度大大提升了，而且可以通过笔记本电脑方便地访问服务器的桌面。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqrXJOcAym9Txd8SXyYpsl5t6PqNmaD4jvsML4bSEicGibRUM4PnicjVticJa1QDdibnWxLhQlxuZA6rqHQ/640?wx_fmt=jpeg&from=appmsg)

Woltz、Watson和团队扩大了这一解决方案——意味着在澳大利亚各地的更多办公用品店购买更多扫描器。周一，远程工作人员被告知带着笔记本电脑到办公室并连接到条码扫描器。公司在澳大利亚的所有电脑在午饭前都修复了——每台机器只需三到五分钟，而手动修复服务器每台需要大约20 分钟。

Woltz 对他的想法能快速恢复感到满意，但也有些遗憾没想到用二维码——它们可以编码足够的数据来自动化整个修复过程.IT经理Watson认为Woltz做的非常好了。他在 LinkedIn上称赞Woltz和其团队成员的努力是“在简化工作站恢复方面的显著创新”。

— 【 THE END 】—

🎉 大家期盼很久的#数字安全交流群来了！快来加入我们的粉丝群吧！

🎁 **多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

😄 嘻嘻，我们群里见！

更多推荐

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpMYmic4xkqp3ky3wcian32ndo3MuLV2dqL6RgqTfITGP0SsmRzibUBftDFg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514213&idx=1&sn=fa2d0412dbbce05ec48a9df909b7cfd3&chksm=c144cad8f63343ce0f383fc9d885c2c7ddcb3f3871270abea4c274775307858d350f60db3b54&token=340500352&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrXJOcAym9Txd8SXyYpsl5tMKKKZOkjKCyFF73OcERMobc16eBGprcrFxpXPqf7uBeueamyuxTI9w/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514264&idx=1&sn=34960d59e3146dcce9f986129c3593c2&chksm=c144ca25f633433381c6bb3bc13fe3e8f2c15984de2aa8f072497dc07648f85c713aa1347ba1&token=340500352&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpM6fVpib3ficMmxPXTULy4YxbmwckZnudDYBnPvV3icV1ibdoMWpSS7QzE9g/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514264&idx=1&sn=34960d59e3146dcce9f986129c3593c2&chksm=c144ca25f633433381c6bb3bc13fe3e8f2c15984de2aa8f072497dc07648f85c713aa1347ba1&token=340500352&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp7W2bvNhnMbFqgLhjCicpyyqrSRhdKhMyqf2mNZqwqY5Acaicx7J3grHGNcfZZdPymz8YeHW7EVkeg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514185&idx=1&sn=8015c07a68a5e2b6074efd2c77f20085&chksm=c144caf4f63343e2c9b835748de4471cc7783155e35dd65cb8fcc818f946e8f770ddc30c09ba&token=1439057957&lang=zh_CN&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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