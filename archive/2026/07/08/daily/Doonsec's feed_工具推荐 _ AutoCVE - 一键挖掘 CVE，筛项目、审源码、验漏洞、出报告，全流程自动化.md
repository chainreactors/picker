---
title: 工具推荐 | AutoCVE - 一键挖掘 CVE，筛项目、审源码、验漏洞、出报告，全流程自动化
url: https://mp.weixin.qq.com/s/hB1ujYgFqht99IutS_u3jQ
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T06:02:12.656233
---

# 工具推荐 | AutoCVE - 一键挖掘 CVE，筛项目、审源码、验漏洞、出报告，全流程自动化

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g1pTgnczBiaF2nBicJwibzL9RMWpPPacYeiags2kIG5tREsPibykZdibnoaKphKAiclTQcwAlia0hyCIounKtHYkeMcgqXpH5k96nZgq5BBbPNlia6o8/0?wx_fmt=jpeg)

# 工具推荐 | AutoCVE - 一键挖掘 CVE，筛项目、审源码、验漏洞、出报告，全流程自动化

larlarua
larlarua

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

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaFGFQyB15xYtzhKxzKplmSvmLNB9FBWUahIvdzdkD9s0Ej0Vugr3uEl2bnOzasl6LpgblL49ict1j10yicGIRqm0r7ndkIzVzjz4/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&watermark=1&tp=webp#imgIndex=2)

***工具介绍***

AutoCVE是一款可以一键挖掘 CVE，筛项目、审源码、验漏洞、出报告，全流程自动化的自动化工具。

## ✨ 核心能力

### 🚀 一键完成 CVE 挖掘

实现从项目筛选、仓库导入、审计任务创建、Agent 漏洞挖掘到 CVE 申报报告生成的全流程自动化。用户仅需复制报告内容并提交，即可完成后续 CVE 申请。

### 🤖 Multi-Agent 协同审计

通过 Orchestrator 统一调度 Recon、Scan、Triage、Finding 和 Verification 等 Agent，协同完成信息收集、工具扫描、误报过滤、漏洞深挖与动态验证。

### 🧩 三种审计模式

根据不同审计目标灵活选择增强扫描、智能审计或综合审计，兼顾扫描效率、挖掘深度与审计覆盖范围。

| 审计模式 | 核心 Agent | 适用场景 |
| --- | --- | --- |
| ⚡ **增强扫描** | Scan → Triage | 快速分析工具扫描结果并过滤误报 |
| 🧠 **智能审计** | Finding | 深度挖掘高价值漏洞，适用于 CVE 和 0Day 研究 |
| 🔍 **综合审计** | Scan → Triage + Finding | 融合工具扫描与源码分析，开展全量审计 |

### 🎯 面向 CVE 挖掘的专用 Agent

Finding Agent 是 AutoCVE 的核心审计能力，专为 CVE 挖掘场景设计。它可直接分析项目源码，并结合 ReAct Loop、专项工具调用、Nudge 纠偏及 `FinalizeFinding` 结构化终止机制，最终产出符合 CVE 申报条件的高价值漏洞。

CVE 成果明细

![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaE73tjCeBt1eOsAUr61VERGrkibTEic48wfstDQorR4LzcMwrh7IeszJ61icBLxsbxiaXdXafTQ5TRLicwPK6IaccwWjwcXc99Zf8fM/640?wx_fmt=png&from=appmsg)

工具截图

![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaEwYabHhjROoR6nHkAGibJPvNvfA9LKticuCUDibmnJy5almR5KTPkylibNIicaCylg9c61zKmhCPOjhWbJdrf5UWdGxzH6gmAvuX40/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaE15NDQ3xrlibsIbn8Pke9J73nVicIF3kK5FAer5d3IWYa0v3ib8hID3HJ7jSiaMVyNH80vaI8Ja9o17UvTvOxIdGBOZHmIglkgkPE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaGzO7j8Yty1I9yUVNS4o5227viaXnEZ5SEgR84blSiblvxEfd8OlVtkE9mr9f1Xn5LlicaPTwKlsYhicGiaNYJdGUrVAiaenoHiaicuRiaA/640?wx_fmt=png&from=appmsg)

***相关地址***

****关注微信公众号后台回复“****入群****”，即可进入星落安全交流群！****

关注微信公众号后台回复“20260708**”，即可获取项目下载地址！**

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

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaGvpkjxUH1uic0E7ibw7icOdKPEaQEnwB5FHwytF04BasW4Z7UrzMmBMYfUoJYPPUUVcPx4Z3ct9DE1HJNdHAs6MyB5icD2ibUSMkPk/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=13)

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