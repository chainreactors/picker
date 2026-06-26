---
title: Jenkins综合漏洞利用工具
url: https://mp.weixin.qq.com/s/BrEi4W3plsnveOcQotGgIA
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:06:39.797272
---

# Jenkins综合漏洞利用工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVkpMcknXn88rMpGRgw0hAckxHRCiaEhZ6KOyj1ENJUCgpBiaNQyO9ACGDbDWudf5a5CYLWpiasxUtZydob6RJv04JWe6rD1YknEZU/0?wx_fmt=jpeg)

# Jenkins综合漏洞利用工具

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 251，阅读大约需 2 分钟

## JenkinsExploit-GUI

一款 Jenkins 综合漏洞利用工具

项目地址：https://github.com/TheBeastofwar/JenkinsExploit-GUI

![78ddada7bd5b1e3dae4acdddbd86f602.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnbouedWz71p9b09Vo3Otg41W9vic7Us4ESUicJXp7cqpbAWNDAcZkJu6CicvA8icOYaZkVNO5zFlxOA8Rq0OjiakkktflCDge2q4f0/640?from=appmsg "null")

78ddada7bd5b1e3dae4acdddbd86f602.png

### 支持检测:

* • CVE-2015-8103/CVE-2016-0788 Jenkins 反序列化远程代码执行 https://github.com/Medicean/VulApps/tree/master/j/jenkins/1
* • CVE-2016-0792 Jenkins XStream 反序列化远程代码执行 https://github.com/jpiechowka/jenkins-cve-2016-0792
* • CVE-2017-1000353 Jenkins-CI 远程代码执行漏洞 https://github.com/vulhub/CVE-2017-1000353
* • CVE-2018-1000600 Jenkins GitHub SSRF+信息泄露
* • CVE-2018-1000861 Jenkins 绕过 Groovy 沙盒未授权命令执行漏洞 https://github.com/orangetw/awesome-jenkins-rce-2019
* • CVE-2018-1999002 Jenkins 任意文件读取 [https://mp.weixin.qq.com/s/MOKeN1qEBonS8bOLw6LH\_w](https://mp.weixin.qq.com/s?__biz=MzI1NzI2Mzg1Ng==&mid=2247483895&idx=1&sn=4a520f9f7a5e26dd615e583884d9fc37&scene=21#wechat_redirect)
* • CVE-2019-1003000 Jenkins 远程代码执行 https://github.com/adamyordan/cve-2019-1003000-jenkins-rce-poc
* • CVE-2019-1003005/CVE-2019-1003029 远程代码执行(Script Security Plugin 沙箱绕过) https://github.com/orangetw/awesome-jenkins-rce-2019
* • CVE-2024-23897 Jenkins CLI 接口任意文件读取漏洞 https://github.com/vulhub/vulhub/blob/master/jenkins/CVE-2024-23897

## CVE-2024-43044-jenkins

项目地址：https://github.com/convisolabs/CVE-2024-43044-jenkins

```
Exploit Usages:
    java -jar exploit.jar mode_secret <jenkinsUrl> <nodeName> <nodeSecretKey>
    java -jar exploit.jar mode_attach <jenkinsUrl> <cmd>
    java -jar exploit.jar mode_attach <cmd>
```

![59ed0948d3b3e467f8c2896c257d3039.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmwqErE919Fu1bCzUG2xX36MYibsFIJIbFKGAQb2zt7iaymQPZOZQic5ux2qohVZzicrTrsEqGBiandql29PaE247aYht6Nf2GFkcaA/640?from=appmsg "null")

59ed0948d3b3e467f8c2896c257d3039.png

## Jenkins 靶场

docker 靶场
https://github.com/vulhub/vulhub/tree/master/jenkins

![532a8e0c7b2a7dc3a48de9d2f2e2a78b.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVniaEo1u5Aicjjxr6rtCKBQCKoxtr31tFI3L1ibjl6RLibtMZgJQk4WwFXAgqa1kGNqnhPKlAC6bKcJs4YkeRKxB5TXf5RDdA14je0/640?from=appmsg "null")

532a8e0c7b2a7dc3a48de9d2f2e2a78b.png

## 扩展

* • Jenkins CLI 风险与利用姿势 [https://mp.weixin.qq.com/s/Wy-1qqj\_\_PCtZ0C68TGzBQ](https://mp.weixin.qq.com/s?__biz=MzU2MzY1NjU3Ng==&mid=2247485924&idx=1&sn=6950e6d9d6a2586ef33f63af0a722c70&scene=21#wechat_redirect)
* • 记一次 Jenkins 后台注入内存马测试 [https://mp.weixin.qq.com/s/szFks8-YdlrOsv8LfKE-xQ](https://mp.weixin.qq.com/s?__biz=MzI4OTQ5Njc2Mw==&mid=2247484711&idx=1&sn=b7888d61c79ea47fa0956194bbc974fb&scene=21#wechat_redirect)
* • 浅谈 jenkins 后渗透 [https://mp.weixin.qq.com/s/q5A4APOPnGNo4zjulv0ugQ](https://mp.weixin.qq.com/s?__biz=MzkwNjUwNTg0MA==&mid=2247490445&idx=1&sn=c478ed3ebc151a98bab105967b0522e6&scene=21#wechat_redirect)
* • https://blog.convisoappsec.com/en/analysis-of-cve-2024-43044/
* • 实战 Jenkins 到 AD 域控 [https://mp.weixin.qq.com/s/0J7uOWqPTF-u2qZUar1NCg](https://mp.weixin.qq.com/s?__biz=MzkzMTM3OTA0NQ==&mid=2247483744&idx=1&sn=06c27f50f8c6d2f9641f691c558cd602&scene=21#wechat_redirect)
* • 漏洞分析｜死磕 Jenkins 漏洞回显与利用效果 [https://mp.weixin.qq.com/s/pKXKasKwHhOFM10mI0yoWA](https://mp.weixin.qq.com/s?__biz=MzI4MzcwNTAzOQ==&mid=2247528988&idx=1&sn=ce221e6ef302aa68a7a50b5946aab1ad&scene=21#wechat_redirect)

## 总结

* • https://github.com/TheBeastofwar/JenkinsExploit-GUI
* • https://github.com/convisolabs/CVE-2024-43044-jenkins

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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