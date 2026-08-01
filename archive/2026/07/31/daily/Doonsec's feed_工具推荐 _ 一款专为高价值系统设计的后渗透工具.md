---
title: 工具推荐 | 一款专为高价值系统设计的后渗透工具
url: https://mp.weixin.qq.com/s/RrnBnUA-YbNTULiSqxWEyQ
source: Doonsec's feed
date: 2026-07-31
fetch_date: 2026-08-01T05:11:39.761365
---

# 工具推荐 | 一款专为高价值系统设计的后渗透工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rlSBJ0flllmdfUL1BfQv9AkD944ShKwpAKYwMO9ecnoFKgKiay6fdXx4KdxtWdZSuk99xWYnXqpMq1nbgOPZ8dQ/0?wx_fmt=jpeg)

# 工具推荐 | 一款专为高价值系统设计的后渗透工具

Skay
Skay

星落安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_png/spc4mP9cfo75FXwfFhKxbGU93Z4H0tgt4O9libYH9mKfZdHgvke0CeibvXDtNcdaqamRk3dEEcRQiaWbGiacZ2waVw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

点击上方蓝字关注我们

![图片](https://mmbiz.qpic.cn/mmbiz_png/WN0ZdfFXY80dA2Z4y8cq7zy2dicHmWOIib5sIn8xAxRIzJibo2fwVZ3aicVBM8RnAqRPH5Libr4f02Zs5YnMLBcREnA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

现在只对常读和星标的公众号才展示大图推送，建议大家能把**星落安全团队**“**设为星标**”，否则可能就看不到了啦！

【声明】本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统以及盈利等目的，一切后果由操作者自行承担！！！

![图片](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllGQA0HEl1gKC4eKZBd7ibwzK4FBiceIj3Y6EIAwOfAe2gZPfh3U8liaSSOU726NQhrrMybGGiccgicoYw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&watermark=1&tp=webp#imgIndex=2)

***工具介绍***

XPost是一款专为高价值系统定制的红队攻防人员后渗透工具，旨在协助实际攻击中的渗透测试，实现更全面、隐蔽和持久的后渗透信息收集，以及横向移动渗透。目前支持的应用程序：zimbra、confluence、zoho

* # **应用方向: 电子邮件服务器、网关设备、文档、企业知识管理和协作平台、单点登录平台、缺陷跟踪平台、IT运营管理软件、域名管理团队建设、代码存储库管理等。**
* **工具能力: 包括但不限于：邮件检索、明文密码记录、操作数据获取、获取未知密码下的任意登录凭证、域控信息检索、单点登录劫持、痕迹清理等操作。**
* 工具优势: 数据回调流量实现了流量隐身持久化，服务器重启或补丁更新后无文件落地，后门依然无法被察觉。

***使用方法和场景***

1. 该工具依赖Godzilla Webshell管理工具，以插件形式部署，Godzilla下载链接：

```
https://github.com/BeichenDream/Godzilla
```

**2.**成功获取目标系统的访问权限后，大多数场景是通过漏洞远程攻击获取权限，当然，通过其他方式获取目标权限也是有可能的。无论哪种方式，都需要一个可以执行代码的环境。我们将内存型webshell成功植入内存中，并以webshell为loader，进一步执行内存中其他工具的函数（payload），获取所需数据并执行其他操作。

当漏洞本身支持代码执行时，例如confluenceCVE-2023-22527模板注入漏洞，我们可以通过优化漏洞利用方式，直接注入内存型webshell。当漏洞类型涉及文件上传或命令执行时，请参考以下方法注入内存型 Webshell。

**Zimbra**

**1. 将“injec.jsp”文件上传到目标系统的**

上传目录：

```
/opt/zimbra/jetty_base/webapps/zimbra/public/
```

**2. 访问inject.jsp向系统注入内存后门，注入后，删除inject.jsp，但后门仍交将保留。**

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllndIYiaTnSREPmCr0IUgYhRTaTVdZFoPpZicic8iaQ0CwNia53wqPCiaj4uzLuVY8Ihic2xug4kDAXcBygDg/640?wx_fmt=png&from=appmsg#imgIndex=3)

成功删除“inject.jsp”并建立与内存后门的连接。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rlSBJ0flllndIYiaTnSREPmCr0IUgYhRTO8vrpXtDQu4eTYeicUM9TvmdAqtsO71D9GJic9cJeYPKHL4DuljShHwg/640?wx_fmt=jpeg&from=appmsg#imgIndex=4)

**3. 后门持久性**

通过替换zimbra-license.jar插件，防止在重启时清除内存驻留后门。将恶意的zimbra-license-success.jar替换掉原始系统jar文件，实现后门持久化。

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllndIYiaTnSREPmCr0IUgYhRTciaRsn2HlBG77x66ZGKFiaWaBy3qPhonTKS0R6QEVQ1mu0Asc7GejcFw/640?wx_fmt=png&from=appmsg#imgIndex=5)

**4. 清除日志**

利用“zimbraplugin ClearLog”功能清除恶意 JSP 访问的日志。

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllndIYiaTnSREPmCr0IUgYhRT959nmUBvvHMbZQInCPMZicOkX6DGL257xB5MCtmicemibd5IbT1XicHFjA/640?wx_fmt=png&from=appmsg#imgIndex=6)

**5. 功能性有效载荷**

根据需要使用特定功能，单击相应功能后，payload 将被发送到服务器后门，并在内存中执行相应的 payload。

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllndIYiaTnSREPmCr0IUgYhRTxAq612Ec92gCwr4H6ceS1LOl1nyiadHF6x1oubOXmB6VPfV200Via0Pw/640?wx_fmt=png&from=appmsg#imgIndex=7)

**6. Traffic流量**

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllndIYiaTnSREPmCr0IUgYhRTFMibXzGyRjaXzicIuCMYUV8eyYp5WB6ibAIbkeO2yfVpoGpTBpfeRWClw/640?wx_fmt=png&from=appmsg#imgIndex=8)

**7. 测试版本**

```
9.0.0_GA_4583
```

**Zoho**

**1. 上传shell.jar，以在运行时向目标系统注入后门**

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllndIYiaTnSREPmCr0IUgYhRTGLYia9J8oFhLicFCtz8jgQk0uMZw4Kia0ibOSQZCz7N6k29r6eX2IvzVjQ/640?wx_fmt=png&from=appmsg#imgIndex=9)

后门已成功注入；删除shell.jar。

**2. 后门持久性**

为了防止系统重启后后门丢失，可以通过替换 AdventnetADSMStartUp.jar 来修改启动逻辑。

**3. 功能性有效载荷**

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllndIYiaTnSREPmCr0IUgYhRTPugXOGYlwgaPD0Waicnq0qiaJGSiahVQgB9KtdqAXPecBRwBbGoBQgyAw/640?wx_fmt=png&from=appmsg#imgIndex=10)

**4. Traffic流量**

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllndIYiaTnSREPmCr0IUgYhRTQ3x8PrMoMLquGXSBPBl0PHsVnuohUTxXOibgtlQJiaicdMnTzyMw7ppKg/640?wx_fmt=png&from=appmsg#imgIndex=11)

**5. 测试版本**

```
ManageEngine_ADManager_Plus_7222_64
```

**Confluence**

**1. 上传inject.jsp，注入内存后门。**

上传路径：

```
/opt/atlassian/confluence/synchrony-proxy/
```

**2. 访问inject.jsp，注入内存后门。**

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllndIYiaTnSREPmCr0IUgYhRTtdTXSuymHoiaYOU0VSbyLficSTtmS08IsibLUvHict9RBaptoPic6UQD9rA/640?wx_fmt=png&from=appmsg#imgIndex=12)

成功注入后门后，删除inject.jsp。

**3. **功能性有效载荷****

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllndIYiaTnSREPmCr0IUgYhRTemhZJPjsCAAia0icXZsdIeZxydLsvp0U9LR4qYTlo80cECiczlCJ4e5lw/640?wx_fmt=png&from=appmsg#imgIndex=13)

**4. Traffic流量**

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllndIYiaTnSREPmCr0IUgYhRT732TdNkibWibq5XoH89T6mwoicIElE46SJrdSoI3aLpalPXlK1IuSTFHw/640?wx_fmt=png&from=appmsg#imgIndex=14)

**5. 测试版本**

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllndIYiaTnSREPmCr0IUgYhRT4fXPYIbvvQJohvdJj3ibpxPXDFANiaAUl5Tv3e60F2MZft7nRmjIU49w/640?wx_fmt=png&from=appmsg#imgIndex=15)

***相关地址***

****关注微信公众号后台回复“****入群****”，即可进入星落安全交流群！****

关注微信公众号后台回复“20260731**”，即可获取项目下载地址！**

***圈子介绍***

博主介绍：

目前工作在某安全公司攻防实验室，一线攻击队选手。自2022-2024年总计参加过30+次省/市级攻防演练，擅长工具开发、免杀、代码审计、信息收集、内网渗透等安全技术。

目前已经更新的免杀内容：

* 部分免杀项目源代码
* 星落安全内部免杀工具箱1.5
* GoCobaltStrike星落专版2.5.1

* 一键击溃windows defender
* 一键击溃火绒进程
* CobaltStrike免杀加载器
* 数据库直连工具免杀版
* aspx文件自动上线cobaltbrike
* jsp文件自动上线cobaltbrike
* 哥斯拉免杀工具 XlByPassGodzilla
* 冰蝎免杀工具 XlByPassBehinder
* 冰蝎星落专版 xlbehinder
* 正向代理工具 xleoreg
* 反向代理工具xlfrc
* 内网扫描工具 xlscan

* Todesk/向日葵密码读取工具
* 导出lsass内存工具 xlrls
* 绕过WAF免杀工具 ByPassWAF
* 等等...

![图片](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=9)

目前星球已满1100人，价格由208元调整为218元(交个朋友啦)，1200名以后涨价至268元。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaGjMhaZibMoAQMjU1mRl2EuxiawpXybDiadhibWh16GCuMR2EY3CPqfpziaKcRlmP2icEGkZiba5EAsTevoswKbSKCzFqtw5qUeRdoGa0/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=13)

![图片](https://mmbiz.qpic.cn/mmbiz_png/MuoJjD4x9x3siaaGcOb598S56dSGAkNBwpF7IKjfj1vFmfagbF6iaiceKY4RGibdwBzJyeLS59NlowRF39EPwSCbeQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11)

往期推荐

1.[加量不加价 | 星落免杀第二期，助你打造专属免杀武器库](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247495969&idx=1&sn=d3379e8f69c2cefb6d0564299e13d579&scene=21#wechat_redirect)

2.[【干货】你不得不学习的内网渗透手法](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247489483&idx=1&sn=0cbeb449e56db1ae48abfb924ffd0b43&scene=21#wechat_redirect)

3.[新增全新Web UI版本，操作与管理全面升级 | GoCobalt Strike 2.0正式发布！](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247497899&idx=1&sn=018f02ef4064930cbcb40d6b0495e136&scene=21#wechat_redirect)

4.[【免杀】原来SQL注入也可以绕过杀软执行shellcode上线CoblatStrike](http://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247489950&idx=1&sn=a54e05e31a2970950ad47800606c80ff&chksm=c0e2b221f7953b37b5d7b1a8e259a440c1ee7127d535b2c24a5c6c2f2e773ac2a4df43a55696&scene=21&token=458856676&lang=zh_CN#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=12)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllT7yxybzslhp8mC8ibaTia9STZtOXaUjfJbHfLJzPAAs44YKKbWvBj9YPicLA34xgAFpXMfB3SaUnUQ/0?wx_fmt=png)

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