---
title: Linux内核FUSE漏洞
url: https://mp.weixin.qq.com/s/EOMTqw6QBRkPBPILLjZEng
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:07:21.855868
---

# Linux内核FUSE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnsNeY3oOASiadbl2Vl8JWdl5TaQOKm7AkJaFpwx7ibZBqAQPkSrJywqftY6iaylELyahGIFums8uyuBCCqE27YvrF0oa5OibOgLhBE/0?wx_fmt=jpeg)

# Linux内核FUSE漏洞

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJnsqGOQ7ZKjM7Qq4ds2mKicicfOl9iar1EWzow0eqNl6TnXyiahUOrGqAcsj1ksOarUoW1eTe3C1cB1ydibdq354BicQdxAm0qibia9Ftgw/640?wx_fmt=png&from=appmsg)

Linux内核FUSE子系统存在本地提权漏洞，攻击者可通过**由攻击者控制的目录项溢出页缓存获取root权限**。

该漏洞编号为**CVE-2026-31694**，影响内核缓存FUSE readdir结果时所使用的代码路径。

FUSE允许用户空间文件系统通过`/dev/fuse`与内核通信，内核可能缓存目录条目以加速后续读取操作。

Bynario分析显示漏洞存在于`fuse_add_dirent_to_cache()`函数中：内核根据服务器控制的文件名长度计算目录项大小，随后将条目复制到单个缓存页面时**未预先校验该目录项是否超过单页容量**。

关键风险在于，恶意FUSE服务器可在4 KiB页系统上返回序列化大小为4120字节的目录项（超出单页容量24字节）。当内核重置偏移量为零并强制复制该记录时，**额外字节将溢出至相邻内存页**。危险性不仅在于内存损坏，更在于**被破坏数据的具体位置**。

## Linux内核FUSE漏洞

在已验证的攻击场景中，溢出被用于篡改SUID二进制文件（如`/usr/bin/su`）的缓存字节，将可执行代码开头替换为简短payload。该payload在正常流程继续前调用`setuid(0)`和`setgid(0)`。

当这些身份变更系统调用在root属主程序内成功执行后，攻击者即可**绕过常规身份验证检查**并生成root shell。

## 攻击条件

该攻击为本地攻击，攻击者需具备挂载或运行FUSE文件系统的能力，可能通过非特权用户命名空间或`fusermount3`实现。

根据Bynario报告，该漏洞在启用大缓冲区的新版内核上可被利用，且**仅影响使用4 KiB内存页面的系统**。具有更大页面尺寸的系统不受此特定溢出尺寸影响。

## 修复方案

修复方案极为简洁：在缓存目录项前**拒绝所有超出单页容量的条目**。管理员还可通过以下措施降低风险：

* 限制FUSE功能使用范围
* 在非必要场景下移除`fusermount3`的setuid权限
* 适当限制非特权命名空间

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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