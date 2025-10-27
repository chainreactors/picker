---
title: 一次非常规功能点的存储XSS
url: https://forum.90sec.com/t/topic/2292
source: 90Sec - 最新话题
date: 2023-08-17
fetch_date: 2025-10-04T11:58:40.871879
---

# 一次非常规功能点的存储XSS

[90Sec](/)

# [一次非常规功能点的存储XSS](/t/topic/2292)

[账号审核](/c/account/11)

[Kn1vre](https://forum.90sec.com/u/Kn1vre)

2023 年8 月 16 日 02:20

1

一般XSS点是在留言、新增项等等地方，一般也都需要登录

本文记录的试一次渗透中碰到的非常规的XSS功能点，无需登录

所以也可以说是未授权XSS，并且直取admin

漏洞功能点位于【**系统日志**】处

[![WPS图片(1)](https://forum.90sec.com/uploads/default/optimized/2X/2/2033f024bce7b3b58953ac9cfb6e5d2cc12923a5_2_690x278.png)

WPS图片(1)1427×577 30.4 KB](https://forum.90sec.com/uploads/default/original/2X/2/2033f024bce7b3b58953ac9cfb6e5d2cc12923a5.png "WPS图片(1)")

此处记录并审计登录行为

发现用户在登录时，用户名、IP等信息会被记录在此处，用户名可以根据POST请求包中的【username】字段进行改动，但是在测试过程中发现系统对该字段有进行特殊字符的限制，所以无法实现XSS

但是后面发现对**IP字段**的输入却没有进行限制，在POST请求头中加入【x-forwarded-for】就可以任意自定义修改此处对应的【操作IP】

[![WPS图片(2)](https://forum.90sec.com/uploads/default/optimized/2X/b/b8ad5e6f06002a0f70ca055e59af9d183d36ff5a_2_690x351.png)

WPS图片(2)1239×632 87.5 KB](https://forum.90sec.com/uploads/default/original/2X/b/b8ad5e6f06002a0f70ca055e59af9d183d36ff5a.png "WPS图片(2)")

插入成功，管理员来到审核页面的时候就会触发XSS

[![WPS图片(3)](https://forum.90sec.com/uploads/default/optimized/2X/6/6638aa0d05553b2764be9178dc51682af76ddba9_2_690x356.png)

WPS图片(3)1213×626 36 KB](https://forum.90sec.com/uploads/default/original/2X/6/6638aa0d05553b2764be9178dc51682af76ddba9.png "WPS图片(3)")

这个系统对所有插入的数据几乎都做了编码、限制、替换，找了好久才找到这个位置

所以测试或者说漏洞修复过程中，除了注意用户GET、POST的数据外，还需注意请求Header头里面的参数

1 个赞

* [首页](/)
* [类别](/categories)
* [准则](/guidelines)
* [服务条款](/tos)
* [隐私政策](/privacy)

由 [Discourse](https://www.discourse.org) 提供技术支持，启用 JavaScript 以获得最佳体验