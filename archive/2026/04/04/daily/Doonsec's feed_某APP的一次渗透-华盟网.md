---
title: 某APP的一次渗透-华盟网
url: https://mp.weixin.qq.com/s/wimXq3p6KGlJ0bxkw04Wew
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:35:12.674599
---

# 某APP的一次渗透-华盟网

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PAQTLCRhmAbspo2npv9ZzIk6gCycPjicfanhAENxnx1apiaIZiauwvGnSxWbuwxchYnDKlk1wbLJLXqP6ZtUgZGDv1oCNo0QEkq4/0?wx_fmt=jpeg)

# 某APP的一次渗透-

nnsae86
nnsae86

黑白之道

![]()

在小说阅读器中沉浸阅读

来源：

# 本文由掌控安全学院 - **nnsae86 投稿**

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（  https://bbs.zkaq.cn   **）****

# 一、前言

最近项目上遇到很多关于渗透测试的资产为 App 相关的，所以这篇文章主要讲一下 App 挖掘思路和测试方式，下面的案例均为一两年前在项目上的真实漏洞案例，当然肯定还有其他的挖掘测试思路，所以这里只作为参考。
 这里首先就是查看 APK 包是否存在加固问题，如果在做一些安服漏扫相关的测试话其实如果 APK 未加固也可以写上去。
 如下图，使用 APK 查壳工具分析，一般情况都能查的出来，如果没有查出来可能是该 APK 比较强大。
![图片[1]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6Myo382WxaLwoXjZaZrQzu7zFaYRTev10nnINicMIrxW2GtMR2YolO0Tds9Mn6F0uicrO5D1miatzibicpKJSNlXZf3M3gZibW4ZkcC0/640?from=appmsg)
 查壳未加固的话可以直接查看源码信息，可以获取大量接口信息，也可以看看有没有硬编码啥的，这一步其实和前端代码分析有点类似。
![图片[2]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NwuLENdk9s0juKrUoAnybEACulXpoCVHuOOKsDkUdiarpywZEq7bu0icPnYuVpBxRv6iaoyH2s5Hs8uiajMIxibyL87JQGEhwyDDBQ/640?from=appmsg)
 如下，这个 apk 包存在 360 加固，但是这个 360 比较好脱壳，所以直接使用工具梭哈了，但是 frida-dexdump 就脱不了壳，猜测是做了 frida 的特征检测，可能需要使用魔改的 frida 才行。
![图片[3]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PY03BtzsPAZeGibI6vXicNuF8IQK6m36kCvmDiblnsMMVtCWVHbA54OOIYbp2QniasGCicE9MsaHccNsbsPjmglND1blvUGjg3U594/640?from=appmsg)
 这里也不啰嗦，直接使用 fundex 和 lsposed 进行脱壳试试
![图片[4]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NPIcUicHTeUrKpWUQ2yuNLmRyYIoc5AnfC4icJ5ejsPlmibFzK19KpmPkEB7bkXm7zHaIULXS1VKticcDgN5y3F2A29Oun2zsShJk/640?from=appmsg)
 启动 app ，成功脱壳，在 data/data/<包名>下就可以看到脱壳下来的 dex 文件。这里如果不知道包名是多少可以使用下图中的 am monitor 命令进行操作
![图片[5]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6M2A6d46iaicB6G1vlLg5K1fibVr2ztvaAlnlmQG2Coia5fKibOat2hL0UYseEgMLsXLqx3ljtbVDxwLNrak1z2DvANxeBdfkshCVm4/640?from=appmsg)
![图片[6]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MicOwRzPHSJricNGCyiaTL2dBYNlPXAoO5P8oo8X0l6AoHbgHngA1lXWNUIsrcxr2GWibmwggZFFLrGdwTYPXVUUFEf2rApODp00A/640?from=appmsg)
 脱壳后可压缩后下载至电脑本地进行分析
![图片[7]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MwquRYNVtoIYgibBCBuuOQE9OIaORl8CW1RQEw06iabGPXMqPBOT2Ihbp0ESaSCnhc51GSh6tE2sjtrpDwL4zezdyHZU4NYpia0E/640?from=appmsg)
 如下图，成功脱壳获取其代码
![图片[8]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MMy8oG7WMHYkKAv5SLlRNFKrA0ZiaVY9J1UQ301lzYUo1CvEjJsjPqlpeFMN888nOovr0YyNwLu3ajIJ19Zy6Xn0L8MAfyecics/640?from=appmsg)
 后续通过发现和这个 app 打开发现提示 root 检测
![图片[9]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NLiaslhhvMQia0ARkttG5bYZYd3KDrblEqoG2U2lKOhG0G1JKmnP8TmtQKAgTyIK2bxKibtjC8CJcL8aicZn4YwQJ42yAzFiaZ8bp4/640?from=appmsg)
 手机打开 app ，存在 root 检测，直接使用 magisk 插件绕过，一个笑脸插件，名字忘了，网上搜索下应该能找到，挺有名的
![图片[10]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NKWibGh2bw6z7VTBclzHE91oibeR8gn2z7BYdp80YtFIiaHY20ke0tlxnAWf7UmWlkSbecgJGmW79tOzVsauICshiafgg7OZPUZlk/640?from=appmsg)
 成功绕过 root 检测打开 app
![图片[11]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NyIO0Z5vMoU4yvnRDx0WcxKoiaYibRJ0J7q8X6JDQbL5CKzjkJQ8uICtSic08Zqx49VicrHvV5CBhVnhG4HCHDvljBSOshT83VEdY/640?from=appmsg)
 一般 APP 由四大组件构成，这里可以搜索一下 APP 文件相关结构文章，这里不在描述，如下图，逆向 APK 文件后，会有一个 AndroidManifest.xml 配置文件，一般在 activity 标签中就是 APP 使用的组件配置，如果组件配置 android:export 为 true 的话那么就是可以导出组件信息，比如下面，均配置为 true
![图片[12]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MUkdLVV5nicA7Asv76gA1rT03BbgQ8qPwoebQbdmu5V1YRctUKO3qBERCSrahlzXpYEylpfeMRia38GYbQib6tOZFhkuuhHjK8h0/640?from=appmsg)
 如下图，当我没有登录时是无法访问 APP 里面的其他页面的，但是当组件配置为可导出的话就可以直接在未进行校验的情况下调用该组件信息，相当于如果我想模仿生成一个 APP 或者生成钓鱼一些社会工程学的操作就会存在危害
![图片[13]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6Pw7fDaGrcGJcXBDV5LACH5Q4pP6cBaeMonDEAww1icZaWUKXtsiapf7osDibhVWafLLIiaEKictbn0Nl3D2sQ7xwM18BiczmK1cc9Dk/640?from=appmsg)
 如下图，直接使用下面语句
 adb shell am start -n com.xx.apps.xxx/com.xxx.apps.xxx.ui.profile.Change[敏感信息已移除]
 成功在未登录的情况下调用修改密码页面，因此可以写一个恶意 App ，未授权调用该正版 App 组件进行钓鱼工具
![图片[14]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MjqrQHDicou5MenmjIz8bthRvHkBVo4uQ4BtHGc9HOiaiaPWEDu3S8pPNIXYQm0wibYstibeSXME62TjQUub32GCL6XpUicQsxLiaN4c/640?from=appmsg)
 除此之外还存在文件数据备份配置错误，当配置为 true 的话可以直接导出该 APP 用户已登录的数据信息，例如账号，密码，凭据等存储在本地的数据
![图片[15]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6P0mqJx2b1ZTsnicSqs1Q3oib8KdHQ9In4Z9T5G8z6Zg1toGZO4KSV9DWYoZD1FS8o1RGrppnibzA62GYcbwbx8iaicun69cybgibtVY/640?from=appmsg)
 adb backup -noapk com.xxx.apps.xxxx -f es\_backup.ab 导出数据
![图片[16]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NW4doPiae0OcaoAp10ibBkOmyGmiciaAReBrgclV82ocU5CEsqeOMQ3S4TkGR52uGnkLVblfSCHXic9INPCM8TTp8To57ZVppeiaxo8/640?from=appmsg)
 当我们删除 app 删除数据时，在下载 app 回来时，我们可以直接恢复备份数据，再不需要重新输入账号密码的前提下即可登录 app 账号，甚至于拿另一个未下载 app 的手机一样使用恢复备份操作直接登录别人账号
 很多 APP 会把账号密码信息明文存储在本地，并没有做加密处理，或者说都是一些弱加密，例如 base64 ， md5 啥的，很容易能够获得明文信息。
 如下图，我们可以获取 APP 的明文信息，一般本地 db 文件存放在/data/data/包名/下面
 这里可以发现某个 xxx1\_5.db 数据库文件中存在一个 useraccount 表，这里可以发现用户名，密码，手机号， ID 等敏感信息，密码是 MD5 加密的，所以是可以通过撞库方式破解的
![图片[17]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6P37AgHOATtkcLMyWthIeM0eT3TNHWRAbc8ueibQLtus0CNsSKcicl2URIb83qmIdqDhkyhp346gRGlLTKVV6zTv2icnhMnUvPNl8/640?from=appmsg)
 泄漏明文日志信息，同样的操作步骤。
![图片[18]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PkdOACPFq9svmsT0y0aO0uPCxFGnsvwJD9AszdOicyDzNwW1geAyBMyDNRjdyvn2W99x57iapIG6AC6l3UrrJqMh3kXIT9vE0U4/640?from=appmsg)
 除了上述 APP 独有的测试以外，剩下的其实和 web 测试差不多，这里简单说一个案例，其实 APP 测试起来会比 web 更加轻松一点，当然是该 APP 没有加固没有做任何的签名的情况下，如果存在签名加固等措施的情况下可能还需要进行逆向。
 这个完全没有难度，上传功能点任意上传文件，这里发现某个 oss 临时凭据泄漏
![图片[19]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MpCiaC3hXorHEekribl810yHM1vz0j7Tyr2u1kBs9LMflAGPD4Shg3ibZTE2l7Z7hEiaicCyawwBtnrmIkb65Hu8pgic24StW6agicGg/640?from=appmsg)
 可以直接通过临时凭据泄漏登录 oss 存储桶，里面很多的桶
![图片[20]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PaP4pqyCibRybDq4qSuEMhWZH5j7mXKP5iaX0DNuk8O6XubOUNHvYU6UBBDxET3VhOt5xoybj7ZKq3QNibBJK0dV1oWz6Sc0weJ8/640?from=appmsg)
![图片[21]-某 APP 的一次渗透-华盟网](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6N9cjAiaB6ibsgxib1agsDM4e0bDesAIS36xibfzIxnQ40QpRLGqaib37I5TaPeEiaqIqGMBl2C9hdb2jQBUNqgOCpzM01zBC2m4SOpI/640?from=appmsg)
 申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，
 所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.
 来源：**（  https://bbs.zkaq.cn   ）**

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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