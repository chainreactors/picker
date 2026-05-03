---
title: Cobalt Strike 4.5二开过火绒、eset内存扫描
url: https://mp.weixin.qq.com/s/Tk0t6rHDPaVWa8nQif2CzQ
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:24:26.674197
---

# Cobalt Strike 4.5二开过火绒、eset内存扫描

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icm4tzB0NhkhWKr9Rl4AGW5q296icAhjZg41k922d0iaPJJ1yk2SibQguzIbTW3rwibkujYFFgTfsjAmmf2bA6IL7bvSFlRmISk1gYjd7Txc76pY/0?wx_fmt=jpeg)

# Cobalt Strike 4.5二开过火绒、eset内存扫描

原创

词不达意
词不达意

词不达意安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### cs4.5

`可以遐想`师傅去年把cs4.5 beacon源代码公开了，当时保存了一份到本地，想着有空折腾下，写下了记录内容。

### 本地环境

本次二开我的环境如下：

* • windows10
* • Visual Studio 2012
* • IntelliJ IDEA 2023.3.2

### cobaltstrike客户端

`cobaltstrike.jar`的java层反编译，网上很多文章，我这里就讲下我主要修改的地方。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkia9ib1biaTFNCmia88kndL9RBzhBowLHHX0Q2cMN3PibCzMRKLW1N0uFkj5cOhmjWW1mSDGp7fIEvNrjFMeOBalXS7vrdheA8uiapCw/640?wx_fmt=png&from=appmsg)

#### 去除暗桩

有很多处注释或者修改就行
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkiapiaXL0gmWeHJeADfpLFgmC0g9bCtTQkrlKY7rjM9R5nPeZE3MLaVQDgv1l0s2KdDCR2mgqH8LXAADSF7tREpPMibc9tMYRA8UY/640?wx_fmt=png&from=appmsg)

#### 修改默认密钥

修改为多字节密钥
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkjLcSQa40UcnBPSEWibTLxnHOEXibibJkxPMhw4BRg5NRaprhM7whkJJYZZpZ6IU6O6AxibhBh96YW25yErreVIuaKYSrLA4cz0m30/640?wx_fmt=png&from=appmsg)
不修改的话，例如微步沙箱可以通过默认密钥获取你的beacon信息，还有网络上各种bot扫描cs配置，给你打上标签，假上线。![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkjIkjTtZLGvOFOKROxiaSqYuIShZrZ5Lgn3WltichytbyRoSAW1Kh7GrS1f74VnFzTU96N2fVlPFpNGRtfeicW4EFialmlpE34Q6UE/640?wx_fmt=png&from=appmsg)

### Beacon修改

公开的源码解压到目录下
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0Nhkia5HdVRcSqlrWdBFbSV02V9oSnxF257aWVHJFHGdXycXL7LduunxZlBHbJkUqIHcPCArOHGrEib9SVVST9H9hiaSMpssl23foUBM/640?wx_fmt=png&from=appmsg)

#### 编译依赖

使用vs2012编译好如下依赖，在目录下新建lib文件夹

* • LibTomMath
* • LibTomCrypt

![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkjibzykyAc8h1Xia5m9vXNItC7TGtPZuLOcynibemkbJMbIoe668vt8vLcf16GkcDw4iacWfftjicKEt6QZriaLR6foNXqIGXibTTMP48/640?wx_fmt=png&from=appmsg)
链接器-常规-附加库目录 选择lib目录
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0Nhkjp0Ppw4mvBtbZvy45C2kV0Z9XKYdiaRPciaLA4XhjicULJqrV4tFc07O6s1L9HZu3VtPctOY3cevMibUCLPxj2c9cTnP52zlVGTac/640?wx_fmt=png&from=appmsg)
然后选择beacon，成功编译beacon.x64.dll
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkjYo6nDcZibbWO3ZW7t29ngpGxicBiadX5EuG72LTuyofCBTteK0ia26aRtwmHFjmOsMvIyvZ0CiacSjNVrZMxJr4FFyPebFSnugEoM/640?wx_fmt=png&from=appmsg)

#### 去除暗桩

这两个方法的返回值都要改为`FALSE`，因为会用 teamserver 端发过来的水印值进行校验，不符合就退出
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkjickcSruRGsUTWpYlUTMma94BETReibkCmZF8drTicg2GfjXmfbU6w15ebozvqFzxAAeYaJUUvJY39ib6JoFVsbouIHcfbUaR4CnQ/640?wx_fmt=png&from=appmsg)

#### 修改默认密钥

![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0Nhkja2XC8SWgHYVVZWudHv8jt1t8cRpkwSmkT6iauNlv8ribgykAns6Gp2RZn1bSZRxrN3JkuwuQiblLVvLX8fg0N1CXosias7tj1ZQw/640?wx_fmt=png&from=appmsg)

#### 修改bof默认slot槽位

默认为32修改为1024
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkgMEEhV8RicXRsOyukZ2LMTlaLKcxjLapcibic945CD6HSc6EuTvSibh9ztugWuzaRl5GRf9bzc0Kagf0U7Jgic9ic9V3VMA7luUsZa0/640?wx_fmt=png&from=appmsg)

#### 修改默认Sleepmask

修改原先加密逻辑
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkh2sxwibc5kkZkDCAiad0yMQnOvNbNNEXyMlvymbniajt9y2wdhFBibicL5nob5eCqwAtibhMXv9aVOWLlkKk5NwZ72Qib2btiaxwsHYmA/640?wx_fmt=png&from=appmsg)

#### 替换dll

编译好的dll放在Decode解密文件下，使用命令进行加密
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkjLWXBUML02FXl5icGgRbRibREjpWuaWx2MecVYv90icEteASZeqiaHy6m0cyhlpXroGHQwiauibCLJichdibVynszd8005tPtPRkCyDjk/640?wx_fmt=png&from=appmsg)
到Encode加密文件夹下复制dll文件
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkj8siaeLzpXpws2ufM2ic9XaEMzwAQexZ2KSqEjg2VKicicnUiaN6HuS3Ymfjx7Y6UHp7CXYFjVUoJCsmOcNn46KIwYPwFqNjsmTD5Q/640?wx_fmt=png&from=appmsg)
然后通过压缩包或者idea直接替换dll文件到cobaltstrike文件里
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkgHVwBpbTJn2G5yVb4grYB1WooUWdtR5gVLunzhkQkk9OIRQQAREMO52PUyicPBTeRMMEgNHRLibj1R2EOlOvJXcZuoN5wEUibiccQ/640?wx_fmt=png&from=appmsg)

#### 上线测试

因为修改原因，只支持导出Raw格式上线
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkiaAUpFdJ4nmNyudItTia0JNBcibuUl2ibdaC4VCrpJ6yuDGeUNtr7GYp6IEFMrFHYLRKCHALpObdsfzZF2icufdlx1D4JkVqL5ibZjc/640?wx_fmt=png&from=appmsg)使用导出的.bin文件，生成免杀马
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0Nhkiae5gvh3mlQzqzIZ6tLygTM83eRkiaEqicMMrXiab9mS1OREUJ3ISxCNiaVssjgVnGoJSibUqMn0iavrusH51aialVW7JIeDZWBzCtYgA/640?wx_fmt=png&from=appmsg)
正常上线
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkgNyADDprLo1glcuPqd5jjRy6lFYxm4ncASY0icrOmtGhg57LTROWxZ72H2ukpNchCIqyXtPC3CEKyhgTWnr80duBLt9Fe2MUEY/640?wx_fmt=png&from=appmsg)

### 内存扫描

火绒内存保护，扫描灵敏度设置为高
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkgj92uVjofly98VpzzSu1PdTv5QTtYIIpKlo5ssLtUd5H3czHmjFkaJNzEQxhFFCrBIiaxz0KgSWBVWWW8gAUtUp5m0IRKygHSo/640?wx_fmt=png&from=appmsg)
点击文件上线，快速扫描进程
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkh1AxBHeVFfD6bPPuKibqgJrR5ysJPECmQdkPV4EYNfZTGicqfvyAlX44E0oP00I1AicXwUickXFW9pEMZY5UPcBVYzmcZns8W2xCw/640?wx_fmt=png&from=appmsg)
未发现风险，正常上线![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0Nhkia3oNRN3qOMoXlv7OUARP27xibnkTjP6FDiaXfhCzGX27azHuehot87a6tmmMcwciaKkoTXAMibsGfLF1E2l43XDN1GXrmUE1FkjQI/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkgcYK46TkjsSDXHRsPZzl4cpJrf8MPiarROPqwXhYmUw7OtD5UauaXWJqUibpnXeOr9rkiaTNrRS0KYY2dIxVbrrIZgoI7Lh2Km7o/640?wx_fmt=png&from=appmsg)eset扫描未查杀
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkiaicdficGwMPAibxFoGq25t4vraoOcrba8kSibEtIrhID6ibHvFeE3qIHKRNnLHvibdcnufqlPVEfV2hAk2reMpic9khh5nsGfw6n2o4o/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkhiaUfrGXH0RtK6LRsS6Tyhm7JUIKNeDELtgONM2Nib1lEu8ammDxpr8iay9jBv4Sv2N7VjVm5pPeNxEHpHughRBU2VjCQVvb6bLA/640?wx_fmt=png&from=appmsg)

Bitdefender使用白影2.0工具挖掘白加黑稳定上线

![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkiaaSruJhY7K0hHmGibleslibTUsrCWWValo8R6cibWXT6kJNcm3YBI1gkCyGVIlzx8iatGmTpO0RI7JAnrpdLOcibMz5kKbDyde4wfo/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkgicySkKMxjE3QekOUgYW45PEpJz90ovlxWtNREj1lyVzDQt7aWbprNetY3WUzb7icibbgu5kdEhqbuoyHEF093qeXAicsRIJYdXZI/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkjnic2CbJH2dFtiaiaWSklC9dV6U4P4bc28pdcy1nQnmxhkGZz5szxZnIyCZX37tLhib7gCXM9uQuApCGXRdt6hcg3adO71yiaWJ3D0/640?wx_fmt=png&from=appmsg)卡巴斯基内存扫描寄了会查杀，没改彻底有兴趣的可以折腾下，完整源代码加入纷传获取
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkgcBuJyp4oYc2QbV5x3gkRzEpTjpu301omTI8OUAT1ibvZOF03noyAI6ZWnONzzhwXFO6lfAlfYvyObxmW60vgicHIXNSqRQj4Uk/640?wx_fmt=png&from=appmsg)

### 纷传介绍

工具文件加入纷传获取，圈子专注红队终端安全对抗、社工钓鱼、免杀冲锋马、内网/域渗透。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkjMRacVozp3PLhTQ309BjUwic6CdV86f9OO4wlmF5rgFSWy0DuiapZBdl8fmyEM2FW71qY3xZlIXRic5fWQov0Hwz53qTtGbn4gtQ/640?wx_fmt=png&from=appmsg)

### 圈子往期文件内容如下

* •冲锋马一键生成工具（一键生成免杀loader）
* •lnk文件一键生成工具（一键生成免杀钓鱼lnk文件）
* •bypass内存扫描插件（可绕过火绒、卡巴斯基等杀软内存扫描cs插件）
* •暗涌在线免杀平台（白文件patch免杀loader（分离、单文件）一键生成平台、支持反沙箱）
* •bypass任务计划工具（普通权限可添加、钓鱼快速免杀维权）
* •后渗透工具免杀（petobin，分离加载避免静态落地被秒）
* •BYOVD攻击一键结束赛门铁克进程
* •BinPatch免杀工具过国内主流杀软
* •白影(whiteShadow)自动化白加黑免杀工具v1.0
* •白影(whiteShadow)自动化白加黑免杀工具v2.0
* •Windows恶意软件常见API一览（PDF）
* •Maldev Academy 恶意软件开发完整课程（源码+VM镜像）
* •SplitRun一款exe免杀工具v1.0
* •cs4.5二开过火绒内存扫描

### 参考文章

```
https://red-team.tips/post/KbHZkszOlP/
https://mp.weixin.qq.com/s/ayk4yJEg0cvjUN2PyxkbMw
```

### 重要声明

本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，一切后果由使用者自行承担，禁止用于任何非法渗透测试，以及无授权违法测试，请遵守中华人民共和国网络安全法。

预览时标签不可点

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