---
title: 【工具推荐】 - ZeroEye3.0自动化找白文件，提升免杀效率，实现降本增效
url: https://mp.weixin.qq.com/s/yPMM01RblL6OvBIlUBkQZQ
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:34:36.193344
---

# 【工具推荐】 - ZeroEye3.0自动化找白文件，提升免杀效率，实现降本增效

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9q9BkLgdQNt3vuSDhMIeFlTAfkVTg8GXrlCU8AjCaADk6bjDZ4Y5E34KxuTh0WumBl0ibm0aiayFYicWoibZiayr1AA/0?wx_fmt=jpeg)

# 【工具推荐】 - ZeroEye3.0自动化找白文件，提升免杀效率，实现降本增效

Polaris安全团队

![]()

在小说阅读器中沉浸阅读

以下文章来源于零攻防
，作者生吃香菜

![](http://wx.qlogo.cn/mmhead/UOlZKghBxaaiavXon4dxWvic2icFBaEptGmXJu6BYDKfrjOr5Ck7I17S2Xk33cibaYJH3600BH1ZtVU/0)

**零攻防**
.

哟，我等你等到花都谢了！

# ZeroEye3.0

## 项目介绍

---

用于扫描 EXE 文件的导入表，列出导入的DLL文件，并筛选出非系统DLL，符合条件的文件将被复制到特定的 binX64 或 binX86 文件夹，并生成 Infos.txt 文件记录DLL信息。自动化找白文件，**灰梭子（关联项目）**好搭档！！！

## 更新介绍

---

**一）、**减少对python的依赖，本次更新抛弃了python的脚本！！！

**二）、**使用c++直接遍历路径，优化检测的速度。

**三）、**保留前版本的功能，可以自定义python脚本获取自己想要的。

## 使用介绍

---

可以搭建一台虚拟机，专门下载一堆软件，然后使用这个工具一直跑，这样你的白文件将永远都用不完。

有些白文件是已经被拉黑了，所以有时候并不是你代码的问题，更换白文件是**最简单，最轻松，最高效**的一种选择。

对于不专门研究免杀的师傅来说会**白加黑**，已经足够在国内环境中使用了！不会也不要紧，配合**灰梭子（关联项目）**，也能快速完成这个操作。

| 项目名 | 备注 |
| --- | --- |
| x64/ZeroEye.exe | 检测x64白进程 |
| x86/ZeroEye.exe | 检测x86白进程 |

```
Usage: ZeroEye [options]
    -h     帮助
    -i    <Exe 路径>    列出Exe的导入表
    -p    <文件路径>    自动搜索文件路径下可劫持利用的白名单

example：
ZeroEye.exe -p c:\             //搜索c盘所有exe是否有劫持的可能
ZeroEye.exe -i aaa.exe         //判断指定exe是否有劫持的可能
```

![](https://mmbiz.qpic.cn/mmbiz_png/9q9BkLgdQNt3vuSDhMIeFlTAfkVTg8GXfDPyU8Kw7pKwYKxpjDDvD9fU9lRnsKXLEm2hbgCNkcVfnIhpKlM1SA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9q9BkLgdQNt3vuSDhMIeFlTAfkVTg8GXkJFX2o93nicaj0KEC5dPwGhfb5Fekob6bbb06EMKoOW7VDZmwCGzGow/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9q9BkLgdQNt3vuSDhMIeFlTAfkVTg8GXIZI3ch1daxe9tvVLkJIKiaVbAMQ4zQQNhL70rchla0Ficvv9DORaN4Ww/640?wx_fmt=png&from=appmsg)

## 项目地址

---

```
https://github.com/ImCoriander/ZeroEye
```

## 关联项目

---

[【工具推荐】 - 比Everything弱一点的自动化白加黑工具（灰梭子）](http://mp.weixin.qq.com/s?__biz=MzkyNDUzNjk4MQ==&mid=2247483925&idx=1&sn=7424113417378915f17155260bdeef67&chksm=c1d51beff6a292f913d25344d3e368ee4291c1faeb9860b2d340b95cd33a2a0478d494daf711&scene=21#wechat_redirect)

[【工具推荐】 - 自动化挖掘白加黑进程，无脑冲！！！](http://mp.weixin.qq.com/s?__biz=MzkyNDUzNjk4MQ==&mid=2247484591&idx=1&sn=50b813e4c626aa967d6c506c4749c032&chksm=c1d51d55f6a294434caea97255438183d3bbc8a86bc1215c2df9140d350ea2f26ed6d91a2655&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/blxFaPuVSrdkdNArXd903euUicWTicXE5ibCTp8abjOreZD4iaiajbWSPpPz2e8PSibcF6WIxfu4JictFR7rwEglVvIyQ/0?wx_fmt=png)

Polaris安全团队

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/blxFaPuVSrdkdNArXd903euUicWTicXE5ibCTp8abjOreZD4iaiajbWSPpPz2e8PSibcF6WIxfu4JictFR7rwEglVvIyQ/0?wx_fmt=png)

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