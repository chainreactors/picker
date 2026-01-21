---
title: 记某edusrc证书站的挖掘
url: https://mp.weixin.qq.com/s/tXfpCclQ0hQxlvyT_MZSnQ
source: Doonsec's feed
date: 2026-01-20
fetch_date: 2026-01-21T03:31:18.098073
---

# 记某edusrc证书站的挖掘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVdWCIX5d52zniba3Wf3RltialqtEqJuA6xzE5UpmBEibELSRn8f9CfMvsA/0?wx_fmt=jpeg)

# 记某edusrc证书站的挖掘

Z2O安全攻防

![]()

在小说阅读器中沉浸阅读

以下文章来源于陌笙不太懂安全
，作者陌笙

![](http://wx.qlogo.cn/mmhead/00GYaClAoOqSkSWsPkTEhU6ic0ic8cNicGJAhxIoic8nZWiaN2XB86rA2icMNaHicNt6Dd0sE7mR7Cpq0k/0)

**陌笙不太懂安全**
.

web安全知识分享,渗透测试,SRC,CTF,等优质内容分享学习！

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

漏洞案例

```
某位师傅投稿，xx证书站支付漏洞，有实力我是真没挖到过。。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5J9rgazIew7ziakXRuoGt3NEDAVqLWtnBsOBMQiaeicRqWCm9Zibf2F4jQlkFpEiaz1vNcyyZTJU1Zxxg/640?wx_fmt=png&from=appmsg)

点击小程序进行一键登录，登录之后，来到商品购买页面

选择购买商品后，发起提交订单购买请求

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5J9rgazIew7ziakXRuoGt3NUwegmictPKp2WX9APicjWQOvAgaHKfVibhpuBj0l9zIYgSfhsgcWbVib0Q/640?wx_fmt=png&from=appmsg)

抓支付包发现客户端直接提交的金额，修改金额为1后，成功发起微信支付，微信支付金额为 1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5J9rgazIew7ziakXRuoGt3Ns6Jqh6yQAicfT7oKnOpr3ibz6eicyR5ADgicm2nhricJKuXaTtKeMfjXzNQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5J9rgazIew7ziakXRuoGt3NhiaoVz9GiaPUMFkXqbcoAHE7Mlzzum5jnvHR0kzBPaUx0dZFzoGea81g/640?wx_fmt=png&from=appmsg)

可以正常支付

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5J9rgazIew7ziakXRuoGt3Ne4cGsX89UsLYLsbGib5nk1xta53Xt5FRNuibb6EMu96xJkLcv8oHmvzQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5J9rgazIew7ziakXRuoGt3Nib8iaeA0pBAWoFQHg2NR7hjwczvQWAGX5nAMuCPfSKBzkhfJPAnc5pQA/640?wx_fmt=png&from=appmsg)

常见支付漏洞测试思路（仅供参考）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5J9rgazIew7ziakXRuoGt3NpZMmiahrM1cfd1icKHgZgaWZib3fWfU3x6iaMLABU0WTSC4p9Uf0HPyjkg/640?wx_fmt=png&from=appmsg)

案例2

xxx某职业技术大学漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5J9rgazIew7ziakXRuoGt3NuzTCkJl5W70QCkXJ4nGiabUmAk4iaULm1jD200ET9XKPNYqaL1ibvy8hA/640?wx_fmt=png&from=appmsg)

点击办事大厅跳转到浏览器，使用账号密码xxx/xxx进行登录

登录之后可以看到具体事务

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO5J9rgazIew7ziakXRuoGt3NuxftT96iat4ZgyQiaN4l782jB1Q0OichBibDaibX5KrNgakj9GicEBK5D2SA/640?wx_fmt=png&from=appmsg)

点击我的代办

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVRSibIgOJN3qo9HZchZQ5BLgWvZeeibxRzt0AgrIMw1hHyN2XYePymQicA/640?wx_fmt=png&from=appmsg)

然后点击我的申请

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVNswpiaCsGYf6sjGosAQE71XKKHeB5gAJXUTaIdEcjSQYmJblX156WHw/640?wx_fmt=png&from=appmsg)

然后进行上传，先上传图片，上传之后修改后缀进行上传

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVLByIDFRXF35QlyxT9iaX5Zzy0gXKdCZKxJdU1ODZH9Q8kbrm4obFYsA/640?wx_fmt=png&from=appmsg)

拼接之后进行访问，成功弹窗

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAV2aLHb34lzGMVDFShiaopdTRh7ToLOYAMxicTqQ8YbnfOqPiajGiamF48sA/640?wx_fmt=png&from=appmsg)

看了看其他功能，有的泄露了自己家庭成员的一些身份信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVqGOYc1rFquyfQomtiaPC9sRicDKqknmtxJUTWbdC9LjePS3HicY8Wk8Sg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVG1bIjMJPyo1AHu0cAGs6UD8Rc4hQ4qSabbyaGZc39rvbOBcheicGmDg/640?wx_fmt=png&from=appmsg)

抓取数据包尝试进行越权

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVGPxblDe2tnib4Dpa0EbEu65ZgnHJgpbIRLTLd7u9wWU83sic5Tia6AE9w/640?wx_fmt=png&from=appmsg)

直接提示，请勿水平越权，我丢

只能看看 其他功能了

回到主页面，点击移动接诉平台

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVnxRAua5627I8oXWT2qjiahuryzlwbiaZnB7U4tJRLfbicianZ1aniawfcCw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVORJicW9iaBOB1gSabLVibY1ttH4VgviapZzcf0BIkrwibkXibtcGz34q0ftg/640?wx_fmt=png&from=appmsg)

发现依旧可以进行上传图片，但是payload不能用太明显的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVmsaCqwkACAHK6ng7JjSl5Nxc7HmRib53iaG37qTRsOiaAe6ic33f2uLExA/640?wx_fmt=png&from=appmsg)

拼接访问成功弹窗

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAV9MgXERTyAmkria2okicbQn0kOKu6icqLkgPpxgythoic4bFbmBL4gImJcQ/640?wx_fmt=png&from=appmsg)

简单水两个跑路

浏览器插件推荐-AntiDebug-breaker

在碰到vue框架的时候用来测试未授权挺好用的

拿到站点的时候，先通过这个确定是vue

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAV383Aiayt4wf507qZ72iaOwLp30VCTWUYFSMNpruClx6waNdZh1A3X1BA/640?wx_fmt=png&from=appmsg)

然后插件选择vue模块

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAViauju22uNjlsMPMHJ0bSSaqbvcfFVBaWQWHyLd59sp8JSW2YYOemfKw/640?wx_fmt=png&from=appmsg)

像我这样配置，之后刷新页面即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVAMoTzRgNFHRfbmOcBDMqNG2cMmZ71LA2BcK7evxHuzhy5ew4wick9cQ/640?wx_fmt=png&from=appmsg)

实战测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVGMwq1ZeHiaxmm2GrmWneXCrsibTmkYzySXnHdREKISice7lDmYJic2MnibA/640?wx_fmt=png&from=appmsg)

拿到vue站点，用上面的方法操作后，这里就会出现很多url

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVM64VuuwIRA2eLdz5rewFN2oFA3vGKxoHfDsjQWfF7DgaB7iagY0lhPg/640?wx_fmt=png&from=appmsg)

点击打开即可看到对应页面，这里发现一个未授权上传日志页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVY5pOwhibkv8ibZQTRltmk7hwZgxia9jiaViarxBAXria9ExLLYIRMll1iby1A/640?wx_fmt=png&from=appmsg)

点击上传测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAVaPebnoibfQU5MUTFSpxqa6S3AKwyKtUzL9CcHkdFp10hM11dsDDniaKQ/640?wx_fmt=png&from=appmsg)

发现上传成功

插件地址

```
https://github.com/0xsdeo/AntiDebug_Breaker
```

建了个src专项圈子，内容包含**src漏洞知识库**、**src挖掘技巧**、**src视频教程**等，一起学习赚赏金技巧，以及专属微信群一起挖洞

圈子专注于更新src相关：

```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例2、分享src优质视频课程3、分享src挖掘技巧tips4、小群一起挖洞
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg41LkR0ezBlmjJY4Lwgg8mr1A5efwqe0yGE9KTQwLPJTe9zyv3wgYnhA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOXg868PqXyjsACp9LhuEeyfB2kTZVOt5Pz48txg7ueRUvDdeefTNKdg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=24)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuZDDDv3NsbJDuSicLzBbwVDCPFgbmiaJ4ibf4LRgafQDdYodOgakdpbU1H6XfFQCL81VTudGBv2WniaDA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=25 "null")

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOApVm8H605qOibxia5DqPHfbWD6lmcweDjGv4DLl45waD068ugw2Iv2vg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=26)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWr5g7s0TNF4tBZqNbdewPNswTDOfvN6PkggCqz8j3mib6Vf3z4ia83asg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=27)

图片

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4Bd1oBmTkA5xlNwZM5fLghYeibMBttWrf57h8sU7xDyTe5udCNicuHo8w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=28)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYrUoo5XZpxN9Inq87ic71D6aUeMdaWrKXgYYia2On8nMA7bqWDySa8odAq1a0kkp3WFgf0Zp0Eut0A/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=29)图片![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4KKlic4yiafWTpLdejicQe3MllEQc24ypeI3anaK7IjJDVyq1WVQN2yKBA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=30)

图片

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWHjP3FUnZpXdrOicRWrCf9MibaglQia7WesCVs0ibtBhC4c2XiaT9HibE1Drg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=32)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWXytl9Ioah3X7tw7EMlWV96wWXEHFEM4m6NwlvvkcmEcPqcxcE9MQDg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=33)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaDpuFU7U9TMK5eIpY8iaJcXCicmTB6fsRd8icmH7K1X99YbC07GaJbCRReocORsnDGNU7H7PeqcysIA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=20)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuaDpuFU7U9TMK5eIpY8iaJcXzeTsials9fwTK9lb0iavN5ya2KJAT9sXIBShtRdfRWHNUpgPKjmEnpsA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=21)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](ht...