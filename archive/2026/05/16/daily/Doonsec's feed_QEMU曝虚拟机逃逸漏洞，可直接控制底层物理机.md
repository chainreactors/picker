---
title: QEMU曝虚拟机逃逸漏洞，可直接控制底层物理机
url: https://mp.weixin.qq.com/s/8fRMQKdKux7iyAziVvdEcg
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:44:56.723694
---

# QEMU曝虚拟机逃逸漏洞，可直接控制底层物理机

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lQ1jXOMq3d0hhwyicK5EVB0mkMYG9WaJ7VDHxGCTQfn65BiamgRiaqZw8FA3mic78zRB16RxkaejYiaicib6j3LwhV5AsFiaeSYPFE4k0gshBXibicFiaE/0?wx_fmt=jpeg)

# QEMU曝虚拟机逃逸漏洞，可直接控制底层物理机

原创

网空闲话
网空闲话

网空闲话plus

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

QEMU CXL Type-3设备仿真模块被曝出名为“QEMUtiny”的漏洞链。具备 Guest系统Root权限的攻击者，可利用该漏洞实现虚拟机逃逸，获取宿主机进程甚至宿主机Root权限，风险较高（暂无 CVE 编号）。

漏洞原理

该漏洞链源于 CXL mailbox 逻辑（hw/cxl/cxl-mailbox-utils.c）中的两个致命缺陷：

1. 越界读（GET\_LOG）：指针运算错误，导致泄露宿主机内存地址。

2. 越界写（SET\_FEATURE）：边界检查缺失，允许破坏设备对象字段，进而劫持程序执行流。

影响范围

仅影响启用了 CXL 支持（启动参数含 cxl=on、cxl-type3等）且向 Guest 暴露了该设备的 QEMU 实例。普通 QEMU 虚拟机及物理 CXL 硬件不受影响。

安全建议

1. 排查参数：检查 QEMU 启动配置，移除不必要的 CXL 相关参数。

2. 切断暴露：严禁向不可信的 Guest 虚拟机暴露 CXL Type-3 设备。

3. 隔离降险：临时禁用该仿真功能，或仅在严格隔离的测试环境中使用。

![](https://mmbiz.qpic.cn/mmbiz_jpg/lQ1jXOMq3d2czib5nWUicH8dLktbu0yzMoD4a4icaoT9Tkls8VbUVOdSmZ1RsseIm8fuW8N2iaVJDTfBeggIRHgudtDjIBytK3Wzzr8SvmzWxiaQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lQ1jXOMq3d3mMXhupqY5guhnXic70leqwia5PcdUHcIEYsoz9VTuNQuDrbsLbFQ4otRfsn1VAAxlV57c0UI0x6BJPO4cDdUhic2RbYcG4Zn7SU/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lQ1jXOMq3d3qicXnouj9tdD0JrG4icicyb5NLPDtgwcPoemroInJGhWjKVcsVicDHCkb5aia6jJN4iaPFOrnBxSBvJufNJW3NZFtp3DZn75UpAictU/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/lQ1jXOMq3d0afCDm0pjOSibgm4FUd7PLzsOQVmuhaPpibVvlK6Ep9ibOrKqJO8sJJGbGHOQ5Zeia3StIpt07Ttnr5uLq3bFJDY0Brza5pa0N9cc/640?wx_fmt=jpeg)

初步分析表明，该漏洞可使已获取Guest 系统Root权限的攻击者，利用CXL仿真模块的越界读泄露宿主机内存地址，再通过越界写劫持程序执行流，最终实现虚拟机逃逸并直接控制底层物理机（获取宿主机进程甚至Root权限）。攻击成功后，可读取宿主机敏感数据、植入后门或横向渗透。危害程度高，但仅影响启用了 CXL Type-3设备暴露的特定QEMU实例。

—— LoopDNS 、 GitHub

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

网空闲话plus

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

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