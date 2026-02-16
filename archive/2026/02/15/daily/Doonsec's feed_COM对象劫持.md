---
title: COM对象劫持
url: https://mp.weixin.qq.com/s/d11gyXiH0WItzVXfmPjSPA
source: Doonsec's feed
date: 2026-02-15
fetch_date: 2026-02-16T04:17:56.454440
---

# COM对象劫持

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5FtPcWDnic0fibuovrXZQaG1ibPC7fZ9byt1vriarl415Hia4eicFK2FsoHvokeR8AaLGoVbxeyntoxjG2yJOnrRxQFgWq4581pJukiczGEq0tDqzY/0?wx_fmt=jpeg)

# COM对象劫持

原创

ybdt
ybdt

卡卡罗特取西经

![]()

在小说阅读器中沉浸阅读

# 0x1 前言

COM对象劫持，公开于大概2014年，和DLL劫持一样不是什么新技术但却是至今有效的，DLL劫持目前多用于初始执行阶段，而COM对象劫持多用于权限维持阶段，最近在回顾各类技术，本篇博客没有什么新技术，只做个记录

# 0x2 COM对象劫持原理

那什么是COM对象劫持？一句话总结就是

```
系统组件在寻找COM对象时，由于COM对象搜索顺序被劫持而加载了我们的COM对象
```

对COM不熟悉的同学可能会懵，什么是COM对象？

在注册表项HKEY\_CURRENT\_USER\SOFTWARE\Classes\CLSID下面，有很多项
![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5FtPcWDnic0e08WIZEBej8uiaRFbalfchJ94u3DsnwcuLvKqSxB4SkFMP5oiaOlHFz0gAXBuYGLF4Ut1yfHicJPNQldPJHC85dQSuUPcGoFqrNk/640?wx_fmt=other&from=appmsg)

image

每一项都是一个CLSID（Class ID），也就是COM对象，那系统组件如何使用这些COM对象呢，就是通过每个CLSID的子项InprocServer32中的默认值指向的dll，加载这个dll来使用这个COM对象，所以在本篇文章中，COM对象 == DLL文件

Windows下系统组件加载一个COM对象时的搜索顺序如下，依次是

1. 1. HKEY\_CURRENT\_USER\Software\Classes\CLSID（所属权限为当前用户的COM对象）
2. 2. HKEY\_CLASSES\_ROOT\CLSID（当前用户COM对象和系统COM对象的合并）
3. 3. HKEY\_LOCAL\_MACHINE\Software\Classes\CLSID（所属权限为系统的COM对象）

大部分系统组件注册COM对象是都注册在HKEY\_LOCAL\_MACHINE下，但是如果攻击者在HKEY\_CURRENT\_USER下创建一个同名的CLSID及InprocServer，则系统组件会优先使用攻击者创建的CLSID中dll，而且在HKEY\_CURRENT\_USER中创建CLSID还不需要额外权限，当前用户权限足以，所以这是一个理想的权限维持方式

# 0x3 常见劫持手法

1、劫持现有CLSID，如上所述，在HKEY\_CURRENT\_USER中创建同名CLSID覆盖HKEY\_LOCAL\_MACHINE中的CLSID，以此劫持现有CLSID

2、劫持缺失CLSID，加载COM对象的不仅是系统组件，还有应用程序，有些应用程序会尝试加载不存在的COM对象，这个时候我们就可以在缺失的位置创建COM对象，以劫持缺失的CLSID

下面的参考文章一部分讲述系统常见组件劫持，一部分讲述任务计划的COM Handler劫持，还有一些工具，可以参考，系统COM对象毕竟是有限的，监控的也是越来越严格，就像DLL劫持一样，后面可能越来越往应用程序的COM对象劫持发展

# 参考文章

https://www.gdatasoftware.com/blog/2014/10/23941-com-object-hijacking-the-discreet-way-of-persistence
https://github.com/3gstudent/COM-Object-hijacking
https://enigma0x3.net/2016/05/25/userland-persistence-with-scheduled-tasks-and-com-handler-hijacking/
https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/
https://www.mdsec.co.uk/2019/05/persistence-the-continued-or-prolonged-existence-of-something-part-2-com-hijacking/
https://blog.virustotal.com/2024/03/com-objects-hijacking.html
https://github.com/nickvourd/COM-Hunter

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6GUJytibkzlaPC9BibnGbtkOsLB2JpGBK0ytS84MUWncFTBYPicJMyRtju9EhxEYo92iaBPicxzdbK9t7aDWUB5dhKA/0?wx_fmt=png)

卡卡罗特取西经

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6GUJytibkzlaPC9BibnGbtkOsLB2JpGBK0ytS84MUWncFTBYPicJMyRtju9EhxEYo92iaBPicxzdbK9t7aDWUB5dhKA/0?wx_fmt=png)

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