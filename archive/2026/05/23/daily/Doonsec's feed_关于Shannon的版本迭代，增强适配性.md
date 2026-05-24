---
title: 关于Shannon的版本迭代，增强适配性
url: https://mp.weixin.qq.com/s/JaBDhMg0oRa9RI69emz-fg
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:56:32.518617
---

# 关于Shannon的版本迭代，增强适配性

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ptxZESUjfTGleBS877ia0BsbGDGibe5tuSr09nZCWHEnXH6Zso4q76jergXDrtkAaJS7F6qNwAbncwsLkRTiarjBiblFyiaJ46lncUGJTKo8e4z4/0?wx_fmt=jpeg)

# 关于Shannon的版本迭代，增强适配性

原创

【白】
【白】

白安全组

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

原本Shannon的设计是给行业中相对来说较为专业的人士去使用的，所以需要大家自己将源码搭建起来，然后使用的时候是通过命令行启动，给两个参数过去，一个是源代码，一个是我们本地搭建的访问地址。

但是我个人感觉我们测试不同的框架的时候，还需要配置各种不同的环境，就会很麻烦，所以我这里按照个人思路进行了几个小点的修改。

首先是将所有操作放到可视化web界面中，包括API的配置等，考虑到部分可能部署公网的需求，后续增加登录的安全性。

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTEsCYibDdCNPJXp9je74jHvHyWECWytZfdXaJxPJkWVMbckzicn6ImhQTN1ViaZmt01muUibuDrRDw9vzI1vqn42hCLI4mRcib8HE9Q/640?wx_fmt=png&from=appmsg)

第二点，针对部分测试目标搭建的问题，我新增了一个智能体，用于针对用户上传的代码进行自动化部署。这里的思路我将测试方式分为三种，第一种就是仅针对源代码进行审计，不进行其余的测试。第二种选择是自己搭建好了环境或者有公网可访问的，自己填写对应的IP。第三种就是提供一个Linux的虚拟机，然后智能体自动针对这个源代码进行解读，根据用户提交的Linux的IP，用户名和密码进行连接，在虚拟机上搭建网站环境，返回给测试框架虚拟机的网址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ptxZESUjfTFqFjmsYIQ8aqrABxrib0IGEdY6RP3zshXO7aZbvCJJK3CDUEkEIUt3xetrHJ2lWps7FI5O8JZh6lDXg5xWSlNSMXK9158hTccw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ptxZESUjfTHl1GdTMcDPL1MMsj9TPRPzu7EMoYE3Uy0DohfYUOn9xWibiaEQtibNVjWooH9YqD0Al6XV1HPYVyXlMU3MBmBWZhicn97IDAQWWtE/640?wx_fmt=png&from=appmsg)

目前还是有一些小bug的，自己运行本地是需要安装docker的，不然模拟测试是跑不起来的。

后续我会根据自己的使用持续做一些改进，大家可以提出一些意见

关注公众号发送

```
shannon
```

获取工具地址

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