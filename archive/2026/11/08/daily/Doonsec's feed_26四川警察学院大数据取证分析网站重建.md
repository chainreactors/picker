---
title: 26四川警察学院大数据取证分析网站重建
url: https://mp.weixin.qq.com/s/jHWGrXVKVOUjp25W8mUBcw
source: Doonsec's feed
date: 2026-11-08
fetch_date: 2026-11-09T08:52:18.772843
---

# 26四川警察学院大数据取证分析网站重建

# 26四川警察学院大数据取证分析网站重建

老皮的碎碎念念

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

继续昨晚，上了岁数，绕了很多弯路，记一下流水账。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbwuaNj1PtHWK5V4C9IGrNDib3SWuAOGSSSaibFBvRboxunpcqCustUIfsl80PJXZxvBT8JDviagxaSw0rPVO6cEYbFbe2jo7G92ibU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbybmqWiaUhIWayphvS7de5L2o9Za5L1ZxQRq5ObsvRjBMhoqr4CibsFvjCp39rGZbXpCIp1g0A23yIXVxBush3iaoor7748PJ6Tbk/640?wx_fmt=png&from=appmsg)

火眼重组raid

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbwcoUjHfDrAYhicicK7HQ6rW6CBff0hh1jDmpCha6Pt7RiatJszVE6ZdzkDicjb6GEB55muqsFfhLfa8oeSQiad52KnBGZ2axNKmEKc/640?wx_fmt=png&from=appmsg)

挂载磁盘仿真

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbxACHMcV3VZXjvIuc5rvpiaepEEdgAfVicMBvua6S2x56j9sKxBKNdG3xJ5Yjov3pPRSWYgNTWnTnFicGApPKf0XhTHiaNAHJUnq7o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/SVAhggk0wbwm2TjsvW0MLQv6pB47dhbQdZCPMJqibo8s7Z9jENY9UfSdD99zoibib8qYKaRhfHp4u6pSA6kqicAsYy7vQlwUEM5MrPDfSGOeMjI/640?wx_fmt=png&from=appmsg)

mount /dev/sdb /myshop #把虚拟盘挂到myshop目录

systemctl restart mysqld #重启mysql服务

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbwecibrmTTwa8k5N0SicIqYPMaPrr21bm1M62sRTiaCEOoaF9byavRFKyEbazFYbE6Bk6qSTNxPYWNhWGdmwwKKdjZicuZe6g9hTRQ/640?wx_fmt=png&from=appmsg)

修改hosts

![](https://mmbiz.qpic.cn/mmbiz_png/SVAhggk0wbx97hUZkRv5dM0lb6T8sbjobVFh4BzdRfia6TAVFiaLyVnUeoDqmojFCxGTfm1VFxvgjCwuXMB7bNIxwOibKd79rxBGlV4qQPR79w/640?wx_fmt=png&from=appmsg)

打开报错

检查\var\shop\public\core.php

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbw4bd5KxvSvquO87LKkyUR9psfEvibM0Cvic4M1T2lzswWZKyLwsoRqMH4xnIF3mwWdvo4IMStjBHWeTxwcZfjzJBbRE4iaE9rmaI/640?wx_fmt=png&from=appmsg)

将第二行改为 $check=true;

保存，刷新页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbypwcNicN81LGkytRufz1DZpyqr1dKvlEKQlYEQFUoszbNOqAPiaZCibg84gkyA4Cz9YTLFHcic3yFeibn7jia2IgQ2GcGIWsudNqSC0/640?wx_fmt=png&from=appmsg)

把=后面的字符copy下来，到cyberchef里转换，注意这是个url和base64结合的字符串，当时傻解了半天

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbwSgs3iaCWQ9tjib96HT8et9iamn8UekAZGbNpvhhRYpy6VTiaAjaefMBTOKPSo7GhUqdmpMm0bVWcFPRpEKAguGx04Cib99HhbHvsA/640?wx_fmt=png&from=appmsg)

用解出的内容替换\var\shop\config\database.php

保存，刷新

![](https://mmbiz.qpic.cn/mmbiz_png/SVAhggk0wbwRzDzY32aic2iaqEOPYG2odptayJn6UvPB4OfZE12vK5WcZgoVPoVlj6o9fwG7L9kLsfPUCtHZP33aansWZddv4KHDtsuxYRCF0/640?wx_fmt=png&from=appmsg)

查找后门，这个也是傻找了半天

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbysNefbUxsOmkajtnWiaic9Lf2j0nhV6lREHtPTYCdsibKiaKbk4LFia9A1rmLCnKgBWCZhCOMDKbPOfIujDZAOcLGrUE5N7UTfcjdA/640?wx_fmt=png&from=appmsg)

http://www.shopx789.com/Readme.php?s=/index/index.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbyH2TEibWjgo08yfygMBLicCMTlhDGSZX0Fe5MOzwTX4F3YHiacAaDkceetbe2RzpbDxyvKtUfYcEUpic43qiaFIGiclkPH3AaiahsiaJU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/SVAhggk0wbx2WKoIsGMQmUuknv9AGfibTQiaia7rNmt16mD25icoFrRibheiaJJpQBHic0f47jU6AGwOR8z9OdDWUX5nz3x4lmPTnMFJXOzNFZjcZo/640?wx_fmt=png&from=appmsg)

使用ssh隧道连接数据库

![](https://mmbiz.qpic.cn/mmbiz_png/SVAhggk0wbyTKw8mXEZc3pdEg2azA4nZbRCSn1GOdkjddaOyzoM8MdrKYDsdibStedjdAEZGNPRCsZYBzxrciaS1bB099FudFtIjIicLPS6m3E/640?wx_fmt=png&from=appmsg)

修改admin的login\_pwd和login\_salt

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbxMnWqoDv62z6sMiag9oBIy8Iib0d0umWWvwicRONrb0OPD6ed5VyGDLhrT6TNnysC9xXmySMXFKEiaglSLv8CkyXM8GolcusR8lwY/640?wx_fmt=png&from=appmsg)

登陆进后台

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EsNNx0KLiawZLgs5PZVjW3EsyTjiafk5PickpBNicuMRqgDjnPdYNwfQ0duxXZJs9FNYeD4jX506YtCD09pBEoK9ibQ/0?wx_fmt=png)

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