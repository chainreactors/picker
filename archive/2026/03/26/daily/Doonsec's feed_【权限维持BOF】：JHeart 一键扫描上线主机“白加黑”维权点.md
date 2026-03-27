---
title: 【权限维持BOF】：JHeart 一键扫描上线主机“白加黑”维权点
url: https://mp.weixin.qq.com/s/fxMa1ZbKyh9i4aThPTYqRQ
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:28:49.936413
---

# 【权限维持BOF】：JHeart 一键扫描上线主机“白加黑”维权点

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eUY7Vqx9WRytfVJvkCPiaDEHBTB9021MYn1w1MxGm4Or9MenMDzHZWlQ00frXfbuUKz8cXYsUe7rNwDKwPjouGYQHiblsuuUZmqsYLWBMbExk/0?wx_fmt=jpeg)

# 【权限维持BOF】：JHeart 一键扫描上线主机“白加黑”维权点

原创

m1cr0f
m1cr0f

低级可持续性没威胁

![]()

在小说阅读器中沉浸阅读

# 【起因】

当在和国内各种杀软对抗一番能做到免杀后；自然会想到下一步，做权限维持。但是，无论是改注册表、添加计划任务都很难绕过360的检测。

当我在翻各种公开的维权思路的时候，翻到Maoku师傅在他的公众号**【毛酷红队】**分享他在实战攻防中的维权思路。

![](https://mmbiz.qpic.cn/mmbiz_png/eUY7Vqx9WRyOjqSiaNsLY0caDIRah1iakKD95ibDIUaZcBMFBdWosffbukTZD9Bw4h9Zc2icVJgZNOQax4GfOcEVWvhp0DztLorRLnqx1ibOfRKQ/640?wx_fmt=png&from=appmsg)

结合香菜师傅早期版本开源的ZeroEye，便有了想做扫描启动项”白加黑“利用BOF的想法。

# 【实现逻辑】

* • 扫描目标机器启动项程序所在目录的所有程序是否可以“白加黑利用”
* • 该启动项的状态是“已启用”
* • 启动项程序所在目录有可写权限，方便后续写入“黑dll”
* • 白程序需要有签名

# 【效果】

![](https://mmbiz.qpic.cn/mmbiz_png/eUY7Vqx9WRyZ56paheqEYYK4QPCWmdANN2MuoqJ3fQNSYUqnU0eH5LKNRWiasibUgDn8DdXeCwrnY7ticfVvOricNSx27IHtcTQaqMIpo7eBvhw/640?wx_fmt=png&from=appmsg)

```
03/26 18:48:37 beacon> jheart
03/26 18:48:37 [*] Tasked beacon to run JHeart: Scanning for white-app DLL hijacking opportunities ...
03/26 18:48:57 [+] host called home, sent: 6241 bytes
03/26 18:49:00 [+] received output:
[*] JHeart Scanning (Active Items Only) Started...
03/26 18:49:00 [+] received output:
[+] HIJACK: C:\Users\test\AppData\Roaming\baidu\BaiduNetdisk\ShellFolder64.exe (x64) -> Missing: ShellFolderDepend64.dll
    Path: C:\Users\test\AppData\Roaming\baidu\BaiduNetdisk

03/26 18:49:00 [+] received output:
[+] HIJACK: C:\Users\test\AppData\Roaming\baidu\BaiduNetdisk\ShellFolder64.exe (x64) -> Missing: ShellFolderDepend64.dll
    Path: C:\Users\test\AppData\Roaming\baidu\BaiduNetdisk

03/26 18:49:00 [+] received output:
[+] HIJACK: C:\QuarkCloudDrive\quark_cloud_drive.exe (x64) -> Missing: quark_cloud_drive_elf.dll
    Path: C:\QuarkCloudDrive

03/26 18:49:00 [+] received output:
[*] Scan Completed.
```

# 【使用方法】

保持该目录结构，将cna文件添加进CS，beacon交互窗口输入`jheart`即可开启扫描。

![](https://mmbiz.qpic.cn/mmbiz_png/eUY7Vqx9WRy7IhHhIicZeicc4ib3aoUsEPzspFicBe1Sm9JNoFqFPqJeV9p4UZUIR6POYTHYOBaZEyhuWnZibricc2U4Cmia4mDL99rribWdiaHnXaxQ/640?wx_fmt=png&from=appmsg)

# 【下载地址】

https://github.com/m1crofan/JHeart

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eUY7Vqx9WRzdVZ3DDNEB3QKmIDxlUXhHliaAwBLJs4puaeIfYD1PYQ7d76Fz4adc1fuc4QsIkR2Z4lbwTPyBYgUv2KJnrouYdoYZxKnq4Nibk/640?wx_fmt=png&from=appmsg)

# 【鸣谢】

毛裤红队：[https://mp.weixin.qq.com/s/bkeuNgBG-SC2INH2nd4vNw](https://mp.weixin.qq.com/s?__biz=MzkzODY2NzI5NA==&mid=2247483784&idx=1&sn=b19f2a2d8eec4701f64ecdd1022088f8&scene=21#wechat_redirect)

ZeroEye : https://github.com/ImCoriander/ZeroEye

gemini : https://gemini.google.com/

jxx

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/8OJAOZ57w2flia9AapAXiaiculpxiccmyFfmHHy62ibAjD1PUWXlobMrFU8pET8ceQUdgEoy185ibmmfX2W0ovTzPe4w/0?wx_fmt=png)

低级可持续性没威胁

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/8OJAOZ57w2flia9AapAXiaiculpxiccmyFfmHHy62ibAjD1PUWXlobMrFU8pET8ceQUdgEoy185ibmmfX2W0ovTzPe4w/0?wx_fmt=png)

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