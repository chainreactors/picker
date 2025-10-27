---
title: 记一次捡漏通杀未授权访问,拿4本CNVD证书
url: https://buaq.net/go-230146.html
source: unSafe.sh - 不安全
date: 2024-03-24
fetch_date: 2025-10-04T12:08:16.220490
---

# 记一次捡漏通杀未授权访问,拿4本CNVD证书

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

![](https://8aqnet.cdn.bcebos.com/e0d5f586e3745fbac4476eb901c356c8.jpg)

记一次捡漏通杀未授权访问,拿4本CNVD证书

CNVD证书获取要求:对于中危及中危以上通用型漏洞（CVSS2.0基准评分超过4.0分），以及涉及党政机关、重要行业单位、科研院所、重要企事业单位（如：中央国有大型企业、部委直属事业单位等）的高危事件
*2024-3-23 23:12:51
Author: [mp.weixin.qq.com(查看原文)](/jump-230146.htm)
阅读量:107
收藏*

---

CNVD证书获取要求:

对于中危及中危以上通用型漏洞（CVSS2.0基准评分超过4.0分），以及涉及党政机关、重要行业单位、科研院所、重要企事业单位（如：中央国有大型企业、部委直属事业单位等）的高危事件型漏洞(后续对事件型漏洞证明颁发标准将参考中央网信办颁布的关键基础设施相关定义和分类)，CNVD将给予原创漏洞证明（即CNVD漏洞证书，电子版），该证明可通过编号在CNVD官方网站进行查询跟踪。时限要求：按周对上一周归档漏洞且满足证书颁发条件的进行批量制作。

这里是H3C路由器的未授权访问

FOFA如下:

![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8pYbq3ObibGg8sTpKvx9hxcxKia0MWTicBNlbFdxr3LUHkOlZGKiaCF5krOdLmu9bFfH9BL4qiaArrhM8g/640?wx_fmt=jpeg)

有这种特征的,点击进去就进入设备了,如下

![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8pYbq3ObibGg8sTpKvx9hxcxR7NnfRWrtEmBYrxZVZt810w1uLObic0Dyia1icKKJS4jku7jne8BpvqRg/640?wx_fmt=jpeg)

那么我们的语法就可以改为:

title="H3C&nbsp;ER3200&nbsp系统管理"

将ER3200替换对应型号

![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8pYbq3ObibGg8sTpKvx9hxcxA8PjSFJ7icW3MeH6ULqsny4m3scQ7hco2kq3FDu6SrdeTDgWOV4Hf4A/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8pYbq3ObibGg8sTpKvx9hxcxFQRiatTq5ib7KIcriar72s9eCWcb8tFnRS8I9xHeD42AQ1OmicblgGvVqA/640?wx_fmt=jpeg)

就这样,随便点击一个就可以直接进入设备

然后在用爱企查看一下注册资本

![](https://mmbiz.qpic.cn/mmbiz_jpg/mia12sBTzp8pYbq3ObibGg8sTpKvx9hxcxIsubXibibSsYpzoKSa66Z3xNhIX1hvVQfKF3nAkib9OCwt7pdXBnKEt7A/640?wx_fmt=jpeg)

超过5000万,有十个以上案例,并且能直接进入设备,那么中危评分就5.0,满足证书发放条件

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

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MzIzMTIzNTM0MA==&mid=2247493931&idx=1&sn=b9672b427b9f4fade9a615d2bd744cfe&chksm=e8a5e348dfd26a5e929e59762c284e381d643e2c74b964276378ee6b92ab392af5f913239426&scene=58&subscene=0#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)