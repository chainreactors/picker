---
title: 【海外SRC指南】5750美元赏金的IDOR奇妙之旅
url: https://mp.weixin.qq.com/s/y19ZiG5GjJ3d7F2ef2bHhQ
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:34:41.376296
---

# 【海外SRC指南】5750美元赏金的IDOR奇妙之旅

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1nbqyYvGrhI5qz9azQRw4hkqBicTE2gXUp0oDFUsW8TibAk6cZrwib9dklf4EGMI93cicUMicoc7DXI8Be8KoHyFpicNUCVx2Ie4Ux5CpvmFRwFUc/0?wx_fmt=jpeg)

# 【海外SRC指南】5750美元赏金的IDOR奇妙之旅

白安全组

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于ForOne安全
，作者ForOne安全

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7bXWCYF8Uudo6XxrwTQkMslFH8Frq6r7El5FLBGrvYdQ/0)

**ForOne安全**
.

关注网络安全相关知识，欢迎一起讨论并成长

# 原创实战笔记系列

## 前言

> 嗨，大家好，我是ForOne团队的西瓜，分享一个之前在Bugcrowd实战挖洞过程中遇到的经历，强烈建议师傅们去监控JS更新情况~
>
> 主题：【一时不恰当的修复+JS监控≈产生更多bug】
>
> 750美元 ≈ 5k RMB 如何变成 750+2500+2500=5750美元 ≈ 4w RMB？

## 挖洞过程

1. 1. 选择了一个较为活跃的公开厂商，拿到scope，\*.domain.com，使用subfinder/findomain/crt.sh/google/dnsgen等方法进行子域名recon,合并去重获得subs.txt【此处并非重点，在此就不赘述了】

2. 2. 用httpx测活子域名搜集结果subs.txt，设置允许重定向并记录Location，通过观察Location是否厂商sso页面，方便判断是否有登录功能以优先测试【也得看具体厂商是否适用】如：

```
选项： -follow-redirects -location
```

1. ![](https://mmbiz.qpic.cn/mmbiz_png/1nbqyYvGrhLnJoJLEPLfdbwEtxjewMhZMESOxwluHuLkTFJo3PJH8QEgGtAzSyC9xjaV7iaCNISxKoMyQAsDWib235phBJOA4xsMHhMYRMZNc/640?wx_fmt=png&from=appmsg)

1. 3. 选取其中一个可登录子站，注册登录后，挂着burp熟悉功能，发现功能并不多，搜id= 发现几乎都是加密ID，看不出是什么加密方式，替换成数字ID尝试fuzz后，也无果

1. 4. 使用时光机发现有视频字段的url出现，感觉像静态资产，出于谨慎，还是打开看看，但发现居然有可点击的分享按钮，如图。点击一下，突然跳转到room创建，新发现！

![](https://mmbiz.qpic.cn/mmbiz_png/1nbqyYvGrhLgauwboYt26wqJmDGFyyOM4fsJzLcBFXMiaX92aGGVbkMIj1qQ4NfwUUm2iaflnoJib7JZegq85jia9iasvLcnTvOtSFhSiaTffP0dk/640?wx_fmt=png&from=appmsg)

1. 5. room的ID是uuid格式，暂时看不到其他用户创建的rooms，接着测功能，大多还是加密ID，测试删除room发现只需roomID，但uuid格式没法遍历，测试一轮后找到一个api接口，直接替换成数字ID后遍历ID可泄露所有room评论者emails及其评论内容的，发现都是厂商员工邮箱，越权可查看敏感信息，提交之后很快triaged，审核复现成功，定级p3并获得750美元≈5k RMB
2. ![](https://mmbiz.qpic.cn/mmbiz_png/1nbqyYvGrhJIkgWeSGJjAj01WXCV6DYGQu9ONxPklFH7ruuFCSpzibZ3ZktC2YaZsAdHPU7Ov174zEvLbJcMq0wbVR6W8I7MahWWB0xR7GZI/640?wx_fmt=png&from=appmsg)

1. ![](https://mmbiz.qpic.cn/sz_mmbiz_png/1nbqyYvGrhIla0KR68n2mnteiaZGxMTBLyhsZL9RtAicEJM5xy83YVNQfF54iaj7svmHrwR5ND59Bn2GianY15w1u1icjgoxWhSRra4gYNHHNXLs/640?wx_fmt=png&from=appmsg)

1. 6. 后来想查看开发修复情况，所以用Jsmon去监控JS，过了2天突然JS多了一个接口，当天再次测试，发现之前泄露的信息都被加密了，而这个接口可以解密出所有加密字段的明文，解密后原来加密ID很多是数字ID及其以;的组合，如123;471041这样，试了几个不同加密ID，后确认几乎整个子站的加密ID都能解密，除了uuid类的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1nbqyYvGrhJPm3XXhn8peMdjr1PpjJz1ic8BMETcBIc7SudrHlt5cXRoaFibVhqnlS2VdPGq0FNPibFJkPpcbiao5jxwXoyZe5py6VgspfM6icHg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/1nbqyYvGrhJc5hHP3gf3EmV2fHAnfq1Ugh4Kn3hYXlPAxHfpPfQ9jDytz2Q3Ef2DhvRGYjljEbuahCTqQDdEXMlCusnVIsTQA6AibefI1YAY/640?wx_fmt=png&from=appmsg)

1. 7. 但第二天JS里这个解密接口又被删除了，然而解密接口仍旧可用，通过fuzz发现一个更新room设置的api接口可遍历可修改其他所有rooms的敏感信息如rooms的标题/内容/rooms关键设置等【注意弄两个账号测试越权即可，所以知道具体ID值更容易验证且测试不违规】

1. 8. 这个接口同时会直接泄露敏感信息如room拥有者emails，也都是员工邮箱，甚至还有访问日志，记录访问过该room编辑页面的用户邮箱，甚至还有该room的uuid，这就能获取所有room的uuid用以越权删除其他用户的rooms

![](https://mmbiz.qpic.cn/mmbiz_png/1nbqyYvGrhL562RypnVxX5PXHCzwu828mjhXoVfBfH3yLr3WMVLMHmRFMIHvjgVY97L3rUCFJGtw5VtvsypvaDUibtONxBpxnb2t2C287RXo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1nbqyYvGrhKUqicHz3maNia3ic81XlXtGMR798X15ChEjx2VFjWrhTJSzpRQjMjEBOxVRM8TPIz7bzHIqBLJD67nCEbB9avTRhKJZfkDpQMMXk/640?wx_fmt=png&from=appmsg)

1. 9. 提交上去，附上python复现脚本和视频，标注P1，得到极快的响应，第三天triaged，16天后，收获2500刀≈17500 RMB

![](https://mmbiz.qpic.cn/mmbiz_png/1nbqyYvGrhJ0vdM5V8Wwl3dCG1gmlj9OFKtLZib8Ull2IXKJ04N5WfALHyvqHkxTdj6vSboUUGXMZcecZHt7t4Xtz62YIoETicVqFdE46MtmE/640?wx_fmt=png&from=appmsg)

1. 10. 等了蛮久，之前的报告resolved，测试还是可以用解密接口，同时发现多了一些功能，比如删除评论的功能等，还是加密ID，用解密接口后，Fuzz越权删除成功，合并报告view/modify敏感信息，提交定级P1，又是一笔2500美元≈17500 RMB

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1nbqyYvGrhKrdcaJIszSdGOnSTpuky8KqUflPed4mfdLoibfchQjB1nVmz1ibq5V84fwgsaVGOoFaoS5C7YRsAzSDODrtAY5Libqr9gc5nBfr4/640?wx_fmt=png&from=appmsg)

---

## 总结

* • 遇到加密ID/UUID先别焦虑，尝试直接替换成数字进行Fuzz，再不行如有泄露不可遍历ID的接口最终也可实现遍历ID达成危害升级；
* • JS监控很有必要，可以捕捉到很多有意思的更新点，也更快速定位到容易出洞的点，或者出过洞的点；
* • 看似静态资产也可能有可测点，哪怕是已经出洞的点，修复过程中也许会有弄巧成拙的修复方案，哪怕转瞬即逝也可能是另一个漏洞的启发点；还是要时常关注修复结果，万一还可以绕过

---

想了解

海外漏洞赏金猎手专属社群【猎手小屋】

【更多课程信息】

参与本公众号粉丝抽奖活动

可咨询助教，二维码如下

![](https://mmbiz.qpic.cn/mmbiz_jpg/1nbqyYvGrhIoMXzq5QqPA3iczicA420gbq4CXUdTY5F7Uc4jkY0fNEEr2ffX6kHmhUIqDBXricbK6hn833BS1GldFPnrYmOZyC6HCbONWricHJY/640?wx_fmt=jpeg&from=appmsg)

欢迎关注公众号 **【ForOne安全】**

获取更多后续原创实战技术文章

期待在安全江湖里，遇见更多满怀热忱、并始终前行的伙伴。

感谢大家的支持～

#海外SRC #笔记 #指南

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUZSEBicgombkkXIIVoES3iaEpiaicDuJSgjHcRFuKy7L7Nhs9ib6CrB1p6CEQ0GWATuKoiagCCdSsoFfJ1w/0?wx_fmt=png)

白安全组

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUZSEBicgombkkXIIVoES3iaEpiaicDuJSgjHcRFuKy7L7Nhs9ib6CrB1p6CEQ0GWATuKoiagCCdSsoFfJ1w/0?wx_fmt=png)

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