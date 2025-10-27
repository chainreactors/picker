---
title: 【安全圈】朝鲜黑客利用FASTCash恶意软件从多个国家ATM机中窃取资金
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065278&idx=2&sn=7eb9ab34e56b92451d197500dbbb7e2f&chksm=f36e61bec419e8a8410d2f446b260c1a7cc5d4421d20c19de7419bf2fd43c4ae8b617b059452&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-17
fetch_date: 2025-10-06T18:52:20.112707
---

# 【安全圈】朝鲜黑客利用FASTCash恶意软件从多个国家ATM机中窃取资金

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt4KA6uAWiaNKtF8x1ZtsPibwAttnWbEbxaxhIKGpxYoGmsSGY4liauVrfdQ/0?wx_fmt=jpeg)

# 【安全圈】朝鲜黑客利用FASTCash恶意软件从多个国家ATM机中窃取资金

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

恶意软件

据The Hacker News消息，与朝鲜相关的恶意软件 FASTCash正利用针对Linux的新变体实施攻击，目的是窃取资金。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt43aXTBzRm2VyWol82jR5d3vYo6xzjHXrEkgu1ZT0jaEAORfVz8LNOgQ/640?wx_fmt=jpeg&from=appmsg)

研究人员表示，这种恶意软件安装在被入侵网络中处理银行卡交易的支付交换机上，以实施未授权的自动取款机提现交易。

美国相关机构于2018 年 10 月首次记录了 FASTCash，称至少自 2016 年底以来，有朝鲜背景的黑客组织Hidden Cobra就利用该恶意软件将非洲和亚洲地区的银行ATM作为攻击目标。在2017年的一起攻击事件中，该组织成功对位于 30 多个不同国家/地区的 ATM 机成功实施了攻击；2018年，同样的攻击又在 23 个不同国家的 ATM 机中上演。

虽然之前的 FASTCash仅适用于微软Windows系统和和 IBM AIX，但最新调查结果显示，新版本的恶意软件已经能够适用于Linux 系统，相关样本于 2023 年 6 月中旬首次提交到了 VirusTotal 平台。

该恶意软件为Ubuntu Linux 20.04 编译的共享对象（“libMyFc.so”）形式，攻击手法为篡改预定义的持卡人账号因资金不足而被拒绝的交易信息，并允许他们提取随机金额的土耳其里拉，每笔金额从 12000 到 30000 里拉（350 美元到 875 美元）不等 。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt4TjredhVXUWM2vdXZlZktVAG89icG1Os9bnCG5loA8fpsZ6xBB5so8Hw/640?wx_fmt=jpeg&from=appmsg)

Linux 变体的发现进一步强调了对足够强大的检测能力的需求，而 Linux 服务器环境中通常缺乏这些功能，建议对借记卡实施芯片和 PIN 要求、要求并验证发卡机构金融请求响应信息中的信息验证码，并对芯片和 PIN 交易执行授权响应加密验证。

参考来源：New Linux Variant of FASTCash Malware Targets Payment Switches in ATM Heists

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt4CXVmRwO0HzswbGreUgwkHmAEC93T7DmNgBK449saQaiaKc0tNY9JJ2Q/640?wx_fmt=jpeg)[【安全圈】揭秘美国政府机构实施的网络间谍和虚假信息行动](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065256&idx=1&sn=085b852f0b04266b8ba28e0b651a0bf4&chksm=f36e61a8c419e8be214d26a2f67be192a532f1876d65421950e658ca8c9951daa71cd8d375cf&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XvnzjMsl2uqO3khdTVNxlYGBrTle1mMLwCD83I7ZYFicUuK2IctqgOlaCibU2XZoHA3Aw9GxHFM0Gkmzw41fkrWA/640?wx_fmt=other)[【安全圈】乡镇公交车系统信息泄露漏洞复现](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065256&idx=2&sn=980220c27c207e4156417e7e6a6c2657&chksm=f36e61a8c419e8beda8644a1da99eb23c6b4b5bc49fe59673a854f6c38bdd77c924120e00ea7&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljhP5K1N0lvmFx8KzoW6LVPBWOsH7O11ryx7HIN1yiactgrH6lGpB0q0pZ0X18dibMX9R3BhZs4sicHw/640?wx_fmt=jpeg)[【安全圈】TrickMo 安卓银行木马新变种利用虚假锁屏窃取密码](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065256&idx=3&sn=db9a05a7cb472260591425ee387b49ef&chksm=f36e61a8c419e8be43d4f3953b52b2ac31136bd4bd05c846f86a8083c861da3244bea490f740&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt45eUsqWTUVGEG69AnDyJzSBKdkic5jNGZYcJ5sQnyXuLwE6lFdKofjCA/640?wx_fmt=jpeg)[【安全圈】思科再遭数据泄露，数家大厂跟着遭殃](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065256&idx=4&sn=7ab2859ef0f27a3bc8c16d699d7af1e8&chksm=f36e61a8c419e8bed1286695e270c19e4657f32c0a8ad0ff3c1f3e364bd783d3bbd6a8bdfab6&scene=21#wechat_redirect)

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