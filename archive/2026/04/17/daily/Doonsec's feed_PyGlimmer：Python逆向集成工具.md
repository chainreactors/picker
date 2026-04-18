---
title: PyGlimmer：Python逆向集成工具
url: https://mp.weixin.qq.com/s/x5PdxArjEiVBp1LriSJthw
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:24:54.348891
---

# PyGlimmer：Python逆向集成工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicJUHkm0QTgm4K1XTTlazibVib503aZptcZfv3FxibYS5OiapnEdUdpF9qJKbmptIQKccGeeWwq53LoYZMOZvReslH4EB0O4v05lOOk/0?wx_fmt=jpeg)

# PyGlimmer：Python逆向集成工具

原创

网安工具库
网安工具库

网安工具库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[ClarityJS：一款轻量级JavaScript解混淆工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487053&idx=1&sn=1eba92a83267ab8c8a2ef8db834a4586&scene=21#wechat_redirect)

·[Burp AI Agent：集成AI能力的Burp Suite安全测试扩展](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487028&idx=1&sn=03f00c9e9169d54f5d4de1187726cc98&scene=21#wechat_redirect)

·[Ai工具辅助CTF小白 自动化做Web题目 Windows可用](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487021&idx=1&sn=1733aea27dba4cf495a521590eb18e42&scene=21#wechat_redirect)

·[Auto-SSRF+SSRFmap：构建SSRF自动化利用链](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487017&idx=1&sn=f5b69619acc08b55db5609767690e077&scene=21#wechat_redirect)

·[蓝队应急响应工具箱](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486994&idx=1&sn=2a9a0e9377d8a6360721c67977ef070e&scene=21#wechat_redirect)

·[JWTAuditor：本地部署的JWT安全测试工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486978&idx=1&sn=4345453987a990934b09e1f3a071e788&scene=21#wechat_redirect)

**背景分析**

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIqCArNCX0umALx1Tvz2qrbIJFcqTHeKONBiaoIRPTtGLXOibJmIKMewpSIVbpTOQEOiaJ2BRcpBJ66ULzWCVreXLickQY0VWFvmIg/640?wx_fmt=png&from=appmsg)

当前`Python`程序常通过`PyInstaller`、`Pyarmor`进行打包加密保护，针对这类程序的逆向分析需求持续存在，传统逆向工具存在功能分散、操作繁琐、批量处理能力不足、跨版本适配性差等问题，无法高效完成`pyc`反编译、加密文件解密、打包程序解包等一体化操作。`PyGlimmer`作为一站式`Python`逆向集成工具，整合了主流逆向处理引擎，优化了跨`Python`版本处理逻辑，支持批量文件处理与自动参数配置，以界面化形式降低操作门槛，能够快速完成`PyInstaller`解包、`pyc`反编译、加密`pyc`解密等逆向任务，有效解决传统逆向工具碎片化、效率低的问题。

**安装介绍**

```
●●●

地址：https://github.com/yoruak1/PyGlimmer
```

基础环境配置与启动步骤：

```
●●●

git clone https://github.com/yoruak1/PyGlimmer.git
cd PyGlimmer
pip install -r requirements.txt
python PyGlimmer.py
```

扩展功能配置：如需支持新版`Python`文件反编译，可安装`PyLingual`并将其配置到系统环境变量中。

工具启动后加载图形操作界面，即代表安装与运行环境配置成功。

功能介绍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJfr9nSktPbCib922LegmYy6ZicBxRtYdqhiawPcIcp2hv9IW621GdXRWfB7TgEcGlk6iaAhEfHiciauwR4JZQz1K5CqqibWAmZHUia08g/640?wx_fmt=png&from=appmsg)

`PyGlimmer`采用图形界面操作，无需手动输入复杂命令，通过界面选择对应功能即可完成处理，工具支持单文件与批量文件处理，处理完成后会自动分类存放输出结果文件。

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKt4qN9e8uia9lZrCnKpbQhyxZx2K1XcGgALyb9iaSGa7Rnm0AKvSFQXVQL87jdV28jQ6JotYm97Fd9RqicUTwcjgUnuBtV4dverY/640?wx_fmt=png&from=appmsg)

多引擎`pyc`反编译是核心功能之一，集成`uncompyle6`、`decompyle3`、`pycdc`、`pycdas`、`PyLingual`五大反编译引擎，支持对单个`pyc`文件或批量`pyc`文件执行反编译操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicK9w4RnQEfViafRu72rqOJM6NWkeFSB4N9ibaiakc9QnEOhMicZVmQG9RFUt9qBQjlSQ5IXPibI0HcaOJqSLh9EBvM1ItiawgBcV9sFk/640?wx_fmt=png&from=appmsg)

`PyInstaller`解包功能针对`PyInstaller`打包生成的程序进行解包处理，优化了跨`Python`版本解包逻辑，可适配不同版本`Python`打包的程序，提升解包成功率。

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKmHqc03IInSicX2ty6rCzetGdoBOsWePQxSqaIiaYYmcq3ElnmLaItfS6Px7nxax097OVDUx6ZbvxA1tsVicrRc46zBNGrKRMFibo/640?wx_fmt=png&from=appmsg)

加密`pyc`解密功能可处理`PyInstaller`、`Pyarmor`加密生成的`.pyc.encrypted`文件，支持`PyInstaller 4.0`以下版本的`CFB`加密方式与4.0及以上版本的`CTR`加密方式，工具可自动配置解密参数，无需手动设置。

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLNfD6ElpoCzaanVujkXtLW9Gqd45yx2k1ZHlCYy1853ADYznhC41Rv149G7ou2Fn4FdYib0I4X23JrTpMaibnuxovHsrqHuBQE8/640?wx_fmt=png&from=appmsg)

工具内置多项辅助分析功能，支持对目标文件进行字节码查看、十六进制查看、文本查看，同时提供`PYC`魔数头修复、`PYC`隐写分析、`Python`版本检测能力，全方位满足逆向分析需求。

所有功能处理结果会自动分类保存，用户可在对应输出目录中查看反编译源码、解包文件、解密后的`pyc`文件、分析报告等内容，无需手动整理文件。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJVRBMdib7K3ZtqZv8Yl8uRmgwoJjcDRPibW9TfdiaaibJnTboUxTXo5C0iacxMHS0JnjVbGextpYnIfUquG9E3icJmibOWcPSVNJOOIk/0?wx_fmt=png)

网安工具库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJVRBMdib7K3ZtqZv8Yl8uRmgwoJjcDRPibW9TfdiaaibJnTboUxTXo5C0iacxMHS0JnjVbGextpYnIfUquG9E3icJmibOWcPSVNJOOIk/0?wx_fmt=png)

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