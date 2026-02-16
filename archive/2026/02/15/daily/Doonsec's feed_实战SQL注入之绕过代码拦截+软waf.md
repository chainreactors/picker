---
title: 实战SQL注入之绕过代码拦截+软waf
url: https://mp.weixin.qq.com/s/Nm9ZikqVEZ-_S9cv9_tvRQ
source: Doonsec's feed
date: 2026-02-15
fetch_date: 2026-02-16T04:16:43.301621
---

# 实战SQL注入之绕过代码拦截+软waf

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/IoMNYSrjhlEEJuusvWRCp2H3XMcbYmVP6HJvtX99sURVRFxW1wYnVwr70rgwqs4HOIesiaibczej5Msx1oSR5hRctWg1JjcXeXJYP0Nf8DAzs/0?wx_fmt=jpeg)

# 实战SQL注入之绕过代码拦截+软waf

原创

做一安全
做一安全

做一不做二

![]()

在小说阅读器中沉浸阅读

最近遇到一个比较有意思的sql注入的案例；

进入今天的主题

当你看到这个数据包你的反应是如何测试的？思考一下

![](https://mmbiz.qpic.cn/mmbiz_png/IoMNYSrjhlEr0q6QZSbmSsAj9DGNVrXz7FwibVzqaOSnaBIgicLhAKBCtIJJfJ0fAuTgs886HKMS0RZSVYLtm1Lpfk9o3Q4gt0ZxlL1Bugribk/640?wx_fmt=png&from=appmsg)

第一反应，userid嘛，肯定是修改一下看一下是否存在越权之类的；

但是这里是没有的；

又或者可以置空看看有没有好东西之类的，但是这里也是没有的；

一筹莫展的时候，不小心按到一个符号，您猜怎么着，报错了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IoMNYSrjhlFxbiazI2MSfeD1O3w2WIAjXQUIdwqKL5RGVN0R2oFSOxJVW7xRa3V6oZEicVoBic68aKYreWzwFGaC5lWFhF96ZicmTeVRdDkZWibM/640?wx_fmt=png&from=appmsg)

获取数据失败，是不是有点那个味道了，sql注入，猜对了

后面测试，确实是存在注入的，还是个mysql的

能发出来的，肯定是没有这么容易拿下的

and，or直接把waf干出来了，老演员了，代码层面的waf；

![](https://mmbiz.qpic.cn/mmbiz_png/IoMNYSrjhlFE72cYtYjTAsv8XSaEPZBDtqWqzwznU6Hkm9UvA6KibNf1TMNp22lQbHkwlUFIsxVHXAicrrMauGIpp0GoCjQBrv6eaZGpyjg4U/640?wx_fmt=png&from=appmsg)

好消息waf不拦了，但是exp710居然是对的，竖杠不起作用？？？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IoMNYSrjhlFmQNo8RfrVZume4s2XaPgVUwXdg7Xicj6nFia7ngHrITStyxz3Vs7o8UN3k7eXBibRIAdTXVZB3m0JKzvXycqDykubByuF9ZENG4/640?wx_fmt=png&from=appmsg)

本来想试试sleep的，直接把另外一个waf干出来了，确认过眼神，疑似宝塔软waf；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IoMNYSrjhlHEf1jBgEvsmGd3LuDicbK2dfeLUv7b1DjVQsoFpZCQic4fNyxrleAuxuCiaXU62pXRn45898ZL49Y1jjA3D0h2fzse7VaQeZdbKk/640?wx_fmt=png&from=appmsg)

脏数据居然不行

![](https://mmbiz.qpic.cn/mmbiz_png/IoMNYSrjhlHnQFwQHdvPxRGGE7GknveJmcNlI5KM3XmFTlRK1uibMLCwVtcRVMekdPb7jWQUaTwAna860eIGEl03qyX1bAicMpf09hgGuYh6g/640?wx_fmt=png&from=appmsg)

那就只能看拦截什么东西了，推倒从来

or 1=1拦截

![](https://mmbiz.qpic.cn/mmbiz_png/IoMNYSrjhlFqtU1s8VpEZnpYt3IpTql83RYgmzs8oXmvUibicTrGytmHgAxwc0jW85tujVaia0iao1G1bOHg7VbknaCw3tfAicdjxfRtfPlG5Lm8/640?wx_fmt=png&from=appmsg)

大小写不行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IoMNYSrjhlHSHc3KhYALYYHvGvl5EvpGqpHA1pOHCtA72TqicLBbgb7upAicn25AicPIpoia4DVK5Pd5n0SlwoOeicYbhn9NicicriadxfmibE5Vtlpg/640?wx_fmt=png&from=appmsg)

%0a直接过了？？？？？我还以为是拦截or，拦截空格？有点意思

![](https://mmbiz.qpic.cn/mmbiz_png/IoMNYSrjhlGPUqJk9EibQvoDTNJiaNBYZ8IDwkYkTptmHHNSMNu5ZzcSicJaZa13YQ2BbOXQz6duoYl4OUPg8EBy75ayv0qzN1b66qWYSnLx8M/640?wx_fmt=png&from=appmsg)

干干，继续看看，又不报错？？？？

![](https://mmbiz.qpic.cn/mmbiz_png/IoMNYSrjhlEh7ibT48p9FjnDmBNHtFJicJ1ibjeWhrE3uJERdr5N96b7N4vNCjkuIhlEKz0GxI9ibGuwN5Ul5NPnd9J5ibgplyryIoibWrDZPJx7E/640?wx_fmt=png&from=appmsg)

就是不报错，函数又是正常

![](https://mmbiz.qpic.cn/mmbiz_png/IoMNYSrjhlHg3xILuMEro1nrHWTsSDh1xXXZJQVbGYyWhiaSRShMFkbGKOG0BXlU1XuZfT6ia1KPDpco2DwIPVBianm5lPw3Rp5eZ2zSDTXvmw/640?wx_fmt=png&from=appmsg)

有点东西的，经过测啊测，本地的sql改了又改，配合%0a、%3d和内联成功拿下了

![](https://mmbiz.qpic.cn/mmbiz_png/IoMNYSrjhlFd5RJ4IwhQYLrTtam8o3uicib5jx2YicARCUFKPHErz6VVcLLcesLicKj1zCLFoYfSXCTT69GW2mgCnBOb0xWRWKictxLpgbJ81k0o/640?wx_fmt=png&from=appmsg)

成功报错，构造成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IoMNYSrjhlFDED61TbA3yow4gja6AqGWyzZdmpSx3Vl29ANB7u6xic6ianypL2ajte8RSRIlxsYAb3dP3vkUjIQl31rQW2Kq5WEFD9R9ddTsk/640?wx_fmt=png&from=appmsg)

最后提前祝各位观众老爷们除夕快乐；

2026年希望自己可以坚持得更久一些，也希望文章可以越写越好！

2026年打算主更一个板块了，多个板块感觉有点杂，欢迎大家投票一下自己喜欢的版本。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIkAGXPaY1cUmnbNpRIfibjryGtRxSosWONFACVz84jGiab8MCe9dMJySjNpTTaOYYnGVubONmtBDXg/0?wx_fmt=png)

做一不做二

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIkAGXPaY1cUmnbNpRIfibjryGtRxSosWONFACVz84jGiab8MCe9dMJySjNpTTaOYYnGVubONmtBDXg/0?wx_fmt=png)

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