---
title: 究极无敌的srcAI-xss手法（快看过来）
url: https://mp.weixin.qq.com/s/VhsWE5aoQ5-epKVaQ6aCMg
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:25:32.726578
---

# 究极无敌的srcAI-xss手法（快看过来）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tlibgKYKL9Ev2eyTAoSDEad8PtAFR7saMUyp8xc6hjHxQNkrBT51kAHJBBuPWxR3XPAVLlmsqEfLczYEbib5PTfJO1uOASXe5vq0ibCSdx8Ngg/0?wx_fmt=jpeg)

# 究极无敌的srcAI-xss手法（快看过来）

原创

洪都第一深情投稿
洪都第一深情投稿

湘安无事

![]()

在小说阅读器中沉浸阅读

**声明：****由于传播、利用本公众号湘安无事所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。如有侵权烦请告知，我们会立即删除并致歉。谢谢！**

ps：poc有些敏感，需要的同学可以关注公众号回复关键词：aixss

首先是团队本质高手——黄毛哥，随便翻翻资产看到了一个ai，于是想出手玩玩，随手打了一个poc

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EunNMYVX82Q9mWDkRZXHbWaAgDJQicOhXwKWjlByn9BdkZJtMK9JRIHHmD1nIw0K7vuqfawOg7LibUDjJBplLBA3FYtEic57l2vDk/640?wx_fmt=png&from=appmsg)

当然黄毛哥出手，肯定就有，此时也是成功弹窗

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EvIZic48UjwkbYaBJ04gQrrav3w6BRFcDibRMpG5DkDRcbE3pHqrq1ibsfYOmmZlFCt3KiaWgVGeq54msIx75RVSfosGVGxVFcgIHs/640?wx_fmt=png&from=appmsg)

此处的ai还允许分享聊天给其他人，于是也是成功从反射型晋升为存储型，黄毛哥爽吃嘿嘿嘿

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Ete7wNu6brCNMc3kKGrnTEh22onvA9TpBkEoVoIichdS7RGX1HrsGnXw74Vo9Ebv15nfAJbopI0WficeohzmwEl41yKGXIx0NO98/640?wx_fmt=png&from=appmsg)

漏洞成因：下面这段js代码存在漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EsZXZwjeISxm4dpjg0ic4T4eQ8dvK7YNt5ARiau44wnB6GgKKIqMnPpGZvKIZTt3sEmkNv5qhNxHEKs3pl8oCDsbAFcEJdia7TCsU/640?wx_fmt=png&from=appmsg)

又赚钱了黄毛哥

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Etv8XHuct4B54a2nctnBSnibfOUcedQniaxHfjcNibrNmwZVDxmEXNr2HU35kLLjnHUfbnMJjYresRrOGomjZw0g2401j6kqm2K1k/640?wx_fmt=png&from=appmsg)

往期文章

[记一次差点进编制的漏洞测试](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494898&idx=1&sn=9f9c5a3527c8330f2e4312eadf0ce863&scene=21#wechat_redirect)

[新版微信强开f12和新版本微信反编译](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494896&idx=1&sn=ac8ebcaecd5e18d45f79c7b6d8e3b10c&scene=21#wechat_redirect)

[湘安无事2025团队和培训总结-福利抽奖](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494849&idx=1&sn=a7084a23faa401c4fbcb06af4650846a&scene=21#wechat_redirect)

[985证书漏洞越权成为教授 + EDU/RCE漏洞实战解析｜湘安内部平台月榜 TOP3 案例](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494786&idx=1&sn=9ee660a005413f34e6d89f728df59803&scene=21#wechat_redirect)

[服务号存在注入之有意思的edu漏洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494659&idx=1&sn=e357db59d806c93f3a5a36b5c312b335&scene=21#wechat_redirect)

[湘安无事之湘潭大学冬令营总结](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494727&idx=1&sn=1d17ba9ee9bcd5fc4cfabe12d463e4da&scene=21#wechat_redirect)

[赏金src报告分享&&edu证书站漏洞分享](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494759&idx=1&sn=65084c580bb13fa31f82985721147e7e&scene=21#wechat_redirect)

[edu小灶案例之泄露上w敏感信息&有意思的证书站报告案例](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494702&idx=1&sn=5f0d05b6bea8550eda36ed2ce8ddbf7a&scene=21#wechat_redirect)

[学员投稿之edu漏洞的JS逆向解密导致任意密码重置](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494634&idx=1&sn=7cc83a90badea88d7d7d25583bd0c419&scene=21#wechat_redirect)

[最近学员小灶总结之双十二特惠](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494604&idx=1&sn=80f030c8114ee3287036586c670289c9&scene=21#wechat_redirect)

[卡顿页面导致三本edu证书现世之学员案例分享](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494572&idx=1&sn=14c21f1cae87dbdbf2ca5c4b10533f5d&scene=21#wechat_redirect)

[看完这场EDU通杀刷屏，连我自己都沉默了](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494535&idx=1&sn=113dd5e17065def94a5dacad361176b3&scene=21#wechat_redirect)

[edu证书站挖掘之学员分享案例](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494524&idx=1&sn=bff39f27ea27bccb884e832603acda92&scene=21#wechat_redirect)

[如何快速挖掘低微漏洞-项目挖掘总结版](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494500&idx=1&sn=2da7aa0d40075b462eb27695f2da9e83&scene=21#wechat_redirect)

[公众号接管漏洞之偷偷加](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494345&idx=1&sn=6d9ab80cde99e95c4d1ac710e091ffdd&scene=21#wechat_redirect)[小姐姐微信](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494345&idx=1&sn=6d9ab80cde99e95c4d1ac710e091ffdd&scene=21#wechat_redirect)

[辅助学员审计案例-php代码审计](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494284&idx=1&sn=2feaf2786717c2c577fe0b5230cbc58f&scene=21#wechat_redirect)

[学员-补天800赏金报告分享](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494284&idx=2&sn=c54ea91e0b3dc79f48f54f931df413c0&scene=21#wechat_redirect)

[从js逆向到sql注入waf绕过到net审计-edu证书漏洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494171&idx=1&sn=0d589d01dfbb068e53f9ad9c22676d7a&scene=21#wechat_redirect)

[空白页面引起的高危src漏洞-再次绕过](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494082&idx=1&sn=6d1cc92a049d28b5395d417e0a5203a5&scene=21#wechat_redirect)

[空白页面引起的高危src漏洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494061&idx=1&sn=bfb1406138041fcba8286811aa7ac6e1&scene=21#wechat_redirect)

[难忘的优惠劵漏洞(深情哥破防版)](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494035&idx=1&sn=422326cc617c33c78b3d518471e0862d&scene=21#wechat_redirect)

[什么？又日母校？竟然还有表扬](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493987&idx=1&sn=f8edc2f3a113591e6e4cc57fdf821c8f&scene=21#wechat_redirect)[信](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493987&idx=1&sn=f8edc2f3a113591e6e4cc57fdf821c8f&scene=21#wechat_redirect)

[sql server注入靶场搭建](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493947&idx=1&sn=885ee489f74211ba26a4a097f7ba30d6&scene=21#wechat_redirect)

[记一次学校ai沦为我的宠物之拿下e](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493890&idx=1&sn=380e9dd566b29b713993b26f524fe0e4&scene=21#wechat_redirect)[du证书](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493890&idx=1&sn=380e9dd566b29b713993b26f524fe0e4&scene=21#wechat_redirect)

[疯狂星期四两本证书漏洞合集](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493926&idx=1&sn=06ac298909e27d0e37fef90f64b205da&scene=21#wechat_redirect)

[湘安无事之深情哥版edu+src培训](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493855&idx=2&sn=bb025b6a32bc022319f8dc8057a6436d&scene=21#wechat_redirect)

[记两次js逆向拿下985证书站(学员投稿)~](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493855&idx=1&sn=0d507bc1f90b04588393698ee1c2d4b8&scene=21#wechat_redirect)

[重生之我在教育园暴打小朋友](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493410&idx=1&sn=17df8a525145bf062ed5d6ecc3e09539&scene=21#wechat_redirect)

[某医院微信小程序签名机制绕过分析](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493408&idx=1&sn=672ff76188ab6c97bc1b8d688ac7228f&scene=21#wechat_redirect)

[记二次帮学员拿下edu证书站](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493399&idx=1&sn=425e84fa877f789598a2e8afdf8320c6&scene=21#wechat_redirect)

[记一次难忘的net直播审计](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493369&idx=1&sn=e10ae1cd25ece5fe3c3ca4c2b455cb51&scene=21#wechat_redirect)

[记一次小米-root+简易app抓包(新手)](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493374&idx=1&sn=7dea1086256be1d5a2b1a18fa4ab3be0&scene=21#wechat_redirect)

[记一次带学员渗透母校](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493292&idx=1&sn=7b1881174201094a5449fe1400ddc8a6&scene=21#wechat_redirect)

[同学，你试过交edu漏洞交两天两夜嘛](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493292&idx=2&sn=0d706a4064111b3e131f24460b2f2c56&scene=21#wechat_redirect)

[手把手带学员拿下浙大edu证书](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493292&idx=4&sn=cd157b6471a1ab1e63b8dbfe0f62b42e&scene=21#wechat_redirect)

[记一次手把手带学员拿下600赏金](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493151&idx=1&sn=3e1a791a4d14b9ad21d2f0afe8a455a2&scene=21#wechat_redirect)

[深情版edu+src培训讲解(3000)](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494535&idx=2&sn=9dfb9ceda7361c9523471a64d8f16f5b&scene=21#wechat_redirect)

最后总结

感兴趣的可以联系深情哥进群，有公开课会在群里面通知，包括审计和src。edu邀请码获取，咨询问题，hvv渠道推荐，nisp和cisp考证都可以联系深情哥。

**内部edu+src培训，包括src挖掘，edu挖掘，小程序逆向，js逆向，app渗透，导师是挖洞过40w的奥特曼深情哥，edu上千分的带头大哥！！！联系深情哥即可。**

![图片](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EvhicibSicfLHsx32VoXFCUpov9fjNZx9rBo23dnAvdYibpdQakoUrG6y8WG7ZuaTVibGdKlYiaTsqibv1Cp9Zucw1LkLWlSG1Qjniauro/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=wxpi...