---
title: 实战SRC|某交友APP一分钱买会员漏洞
url: https://buaq.net/go-227134.html
source: unSafe.sh - 不安全
date: 2024-03-10
fetch_date: 2025-10-04T12:07:55.536999
---

# 实战SRC|某交友APP一分钱买会员漏洞

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/227aba04687b8dbf0e15b7376f1e421d.jpg)

实战SRC|某交友APP一分钱买会员漏洞

某交友APP一分钱买会员漏洞前言：本文中涉及到的相关技术或工具仅限技术研究与讨论，严禁用于非法用途，否则产生的一切后果自行承担，如有侵权请联系。由于微信公众号推送机制改变了，快来星标不再迷路，谢谢大家
*2024-3-9 22:51:11
Author: [mp.weixin.qq.com(查看原文)](/jump-227134.htm)
阅读量:29
收藏*

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY28ybNsfr9Riaxc0y93IXwic9Kxv0LpFzdUIFbchGWMicCV1I4OwLZqAteIpgyibgKe5XuBGostfDhw/640?wx_fmt=png)

**某交友APP一分钱买会员漏洞**

前言：本文中涉及到的相关技术或工具仅限技术研究与讨论，严禁用于非法用途，否则产生的一切后果自行承担，如有侵权请联系。

由于微信公众号推送机制改变了，快来星标不再迷路，谢谢大家！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY28ybNsfr9Riaxc0y93IXw76WJ8b9VW6YdH36D6T8J0bA0aqmn9PjlvcTQXL6s2ia8sHib601iaOSWg/640?wx_fmt=png)

**漏洞详情：**

某交友APP存在逻辑缺陷，用户可以通过修改会员价格用一分钱购买价值388元的会员(玩的就是白嫖~)。

发挥会员钞能力还怕找不到npy，解锁无限畅聊，右滑喜欢不受限![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_14@2x.png)

**发现过程：**

首先在点点数据看下app的下载量，一千多万次的下载量，实际使用用户应该还是挺多的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVKjwYmumMd7bmiceb9eibPDlqfSy3jxV1iamq3zVODaLcbo7Lfeenric0SSvWO2JmImAtVALtiaiaPuezQ/640?wx_fmt=png)

在模拟器中安装好后登录，到开通会员界面，选择价值388的会员套餐（要买就买最贵的![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DicRqXXQJ6fVKjwYmumMd7bmiceb9eibPDl1e47ynmvT6E8ZzlhMlVsljbtCcvVciahWF7Fwr4icHbFIZuthkkLDxZQ/640?wx_fmt=other&from=appmsg)），抓到下面这个数据包，price参数代表的是价格。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVKjwYmumMd7bmiceb9eibPDlT2bpcTWuDVKyduPZSEV30AxQGOEoSiaxG0iac7KjcAicKRStHd9uz9uBA/640?wx_fmt=png)

经过了各种尝试，最终发现价格最低只能到0.01，再低就会创建订单失败，看来不能零元购了![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVKjwYmumMd7bmiceb9eibPDlqZ9gibD4DCPpk6LMibibrrr1MPgqjzybCIq7q0E7F4RMHxLogPs4M8IDA/640?wx_fmt=png&from=appmsg)。

修改价格为0.01后放包、支付。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVKjwYmumMd7bmiceb9eibPDlN9CKQGibgUNyKxQg5voRsp95N2nQM6xPvhNibuD5IHUTQendLVhXCQlw/640?wx_fmt=png)

支付一分钱后就成功买到价值388一年的会员了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVKjwYmumMd7bmiceb9eibPDlqBgzOiatTskoibiaYgjhDmMvyrPZf1CADjBKUh7SFXQ6icECc3uiaYbdjNw/640?wx_fmt=png)

最后来看看会员的特权都有什么，这么多的特权一分钱拿到，岂不是美滋滋。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DicRqXXQJ6fVKjwYmumMd7bmiceb9eibPDllH9YvGLa2VzvK8dt5mBGWrnxHicL5s9PJf5ZMvaeqhNYyoFuRvDRoFA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVKjwYmumMd7bmiceb9eibPDlYYDejVCCZpxibXVrVuxickJIUfmDeNqWf9uRPpOCKfoqtyty0aNClYyw/640?wx_fmt=png)

漏洞已报送相关单位且已修复。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款
前面有同学问我有没优惠券，这里发放100张100元的优惠券,用完今年不再发放

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj7N5nMaJbtnMPVw96ZcVbWfp6SGDicUaGZyrWOM67xP8Ot3ftyqOybMqbj1005WvMNbDJO0hOWkCaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MzIzMTIzNTM0MA==&mid=2247493809&idx=1&sn=5dd53565883e5ea283fecd371d80aa4a&chksm=e8a5e2d2dfd26bc4ed9ec04aa634aa0713eeb7b751b348e94703d8f2cf2c8a3aa2567686baed&scene=58&subscene=0#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)