---
title: bypass任务计划维权
url: https://mp.weixin.qq.com/s/KKGifxCZ3rQFmVvD7kXvog
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:17:49.951606
---

# bypass任务计划维权

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icm4tzB0NhkgjQw2Ez9kiavWia2N7HRdUMqTGLNKHzmr9XPaicvgic40WhLAs3icAf5j60ibl9CnCicibdbiczic3LbN9SloXK7OE2Ka0ppvSYoxkBPTT0/0?wx_fmt=jpeg)

# bypass任务计划维权

原创

词不达意
词不达意

词不达意安全团队

![]()

在小说阅读器中沉浸阅读

> 声明本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，一切后果由使用者自行承担，禁止用于任何非法渗透测试，以及无授权违法测试，请遵守中华人民共和国网络安全法。

### 前言

Windows下任务计划权限维持工具，应对在社工钓鱼场景下，针对个人PC、域环境下快速维权。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkh2Bp96Ps01iaWQje2ONANHRn5DPkKHLjRZhJ5vJ9YEQ7wUVHm1jB1B1q8SJiamaSYQKOvvBU9gfg8PrGZiayDvlCqBRbDBrg1XYw/640?wx_fmt=png&from=appmsg)

### SchedukeTask工具维权

SchedukeTask工具`普通用户权限`即可添加任务计划，无需管理员权限

```
SchedukeTask.exe
 Usage:
        [+] ADD SchedukeTask.exe C:\Users\Public\calc.exe TaskName
        [+] RM SchedukeTask.exe rm TaskName
        [+] Time: Execute every 10 min (default)
```

![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkgR0icza8bnKmjMskpaX1IJialU1v0jiaHDZ7n8c3IJzhHHiaklTKrZWggeicyjjUZrT4OKPHXATB25xUDiaJNaLtWJ8TmtPrMGbaXls/640?wx_fmt=png&from=appmsg)
每10分钟执行一次
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkiaVzWGTTiaDDk8boUTZF9fRB3wlIZmmpCIdF3Yugh4xnPu7tiaxicSo8sZJ4IZfyYF7q2DbUdcYrAUwWXFSmWzgicodP5eby3Bvlr4/640?wx_fmt=png&from=appmsg)
火绒未拦截
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkh7oBeCoMF9ibAhILay9SlsrD52IFPc4v1nVbubM5UrS10QBYWHhgaJ2FpibamiamkuOEGn1vzOOVJ6ZKFeOrHlpbY8qoiaCPibibEho/640?wx_fmt=png&from=appmsg)
卡巴斯基未拦截
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkhaibTPZ7YuviafP1IiaDC0ugtbTiaLJicBrfeOlO1ibo7HlC15GlpWJhicYt2gBaPI33r8A7VWZLxX9jVVdiaPW7kZcdeeKMdMTI8Ghfw/640?wx_fmt=png&from=appmsg)
赛门铁克未拦截
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkjlVTGVGbyf4HdSJ6bbup2A6cAbcvfpGOFTTGlhvhO1mDIoD33VVAlf8ChBIxiaRNiamJd1PD2dftibHtAlssFUkJtKPrQtib8yjMw/640?wx_fmt=png&from=appmsg)

### 滥用白文件维权

通过逆向分析，`滥用带有正规签名的白文件添加任务计划`
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkhbexxkYyXXTQZ0AFU6bbp812MjictXibibRP3T2BOAcfhtnGFzFMgsaBwsuTW9ricRfp6bKe8SXeI4HFJgf9WZSqcqVeMUNLAO0SU/640?wx_fmt=png&from=appmsg)
无需管理员权限，`普通用户权限`运行命令创建计划任务，核晶未拦截，因为是正规签名程序添加理论上杀软都不会拦截![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkiatYq4VAt8LXoovG4Pw6k3ZeL54hvEhicbZlDMDXulicEuyP4trWDicxoqhX3rVgKYJyW6icNQicph3NFAI7ZZ2HsNZicwMpFjfiae9MM/640?wx_fmt=png&from=appmsg)

### 纷传介绍

加入纷传获取，圈子专注红队终端安全对抗、社工钓鱼、免杀冲锋马、内网/域渗透，目前纷传价格`200`

![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkjafqdbheJPtPGyWnaFefajAan8CXtanxSicJeavcDYduIuGzPH2aDjfKdvbrxfsfpFe82o9eml42OmViczcc0zBXrjMRpAP6JVo/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkjvB3SevDf7ItNpeI0C2Yawp85tSFSSKB7HqNKzslK0YWnIopvHC9iazLibJgYDHMNkxDB2ZsVUU7F9ib8M6DkLOWPMZticGTNU5iaU/640?wx_fmt=png&from=appmsg)

预览时标签不可点

作者提示: 内容由AI生成

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/fQ2Bdxy1C5nUgyJyyHvl33mCCUsSib26NxViaiamWM5qOT7NAVcjlGAkGlkBYQF4j3dSHMprGM9aRTxjQ7ThqugRQ/0?wx_fmt=png)

词不达意安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fQ2Bdxy1C5nUgyJyyHvl33mCCUsSib26NxViaiamWM5qOT7NAVcjlGAkGlkBYQF4j3dSHMprGM9aRTxjQ7ThqugRQ/0?wx_fmt=png)

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