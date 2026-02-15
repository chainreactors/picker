---
title: 自动化爬取并自动测试所有swagger接口
url: https://mp.weixin.qq.com/s/lZUcOrvjfKIZhiSEQ-CYjA
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:23:32.899314
---

# 自动化爬取并自动测试所有swagger接口

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Wo0LwcudtziaIM0XnyWiaTsh6re5w5JT0T3fTEX7OLd8HAZQbvLFdCJEfIYothuRBZRw1x0yBEkibKKuhiaHaRmw5s7ewmeuLLNI2l2qDRtTc7Y/0?wx_fmt=jpeg)

# 自动化爬取并自动测试所有swagger接口

原创

jayus0821
jayus0821

W小哥

![]()

在小说阅读器中沉浸阅读

**免责声明**

文章内容**仅限授权测试**或**学习使用**请**勿进行非法的测试**或攻击，利用本账号所发文章进行直接或间接的非法行为，均由**操作者本人负全责**，W小哥及文章对应作者将不为此承担任何责任。

文章来自互联网或原创，如有侵权可联系我方进行删除，深感抱歉。

# Swagger-hack 2.0

在测试中偶尔会碰到swagger泄露 常见的泄露如图： ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wo0Lwcudtzhy47pQ0Grh6a7ho7icxcK7cOsFu1fFK4SvUfhxicocm0iam31Ho9RkD9nfEkNqvdGmabiclLSm6icLicIakqIjGHWeD4siaL0CyAbtao/640?wx_fmt=png) 有的泄露接口特别多，每一个都手动去试根本试不过来 于是用python写了个脚本自动爬取所有接口，配置好传参发包访问

**第一个版本仅适配了一个版本的swagger，不同版本见差距比较大，后续又调查了很多版本的swagger，将脚本的适配性增强了很多**

优化：

·适配多个版本swagger

·添加多进程

·增强了程序的健壮性

·优化了控制台显示，生成日志文件

单链接形式： ![](https://mmbiz.qpic.cn/mmbiz_png/Wo0LwcudtzhwStFAl0jXPgiaKPCp1D8ricSOxqBao2XazD1H45ZWjgMG9XBWBwPCUz1LZLQ8LaBy2GZBD1EJu6X7rjpicFk0y90b3h7wEiaPUic0/640?wx_fmt=png) 文件形式： ![](https://mmbiz.qpic.cn/mmbiz_png/Wo0LwcudtzjpjGotLD1ia47kbLPm0g97XFDbGorU6m2oiccvSzibNib06ibviaRbob411EqMXD7YXBUvmeg4L3PSUjXDzVGcDoFdagwRHWViastIpU/640?wx_fmt=png)

最终结果： ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wo0LwcudtziagiaeGTNuibSNMA7jchPXyXJcn48IxW6UTOhx4MvibYvmyLT6dWa26ccuMickibTqcTXHnOETXCdJWuyyxcwMNhxicVT24ovbkFFoiaI/640?wx_fmt=png)

关注公众号回复“20260214”获取工具地址。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUzKsSv7UficCMvNU3C1Khiayp4iabicKicKVePCZbMlUKFfStk6mX3Hpf6kh5Zl6vcUoOqGcELngiazX8rg/0?wx_fmt=png)

W小哥

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUzKsSv7UficCMvNU3C1Khiayp4iabicKicKVePCZbMlUKFfStk6mX3Hpf6kh5Zl6vcUoOqGcELngiazX8rg/0?wx_fmt=png)

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