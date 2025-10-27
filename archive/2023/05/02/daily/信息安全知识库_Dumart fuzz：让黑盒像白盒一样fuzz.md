---
title: Dumart fuzz：让黑盒像白盒一样fuzz
url: https://vipread.com/library/topic/3909
source: 信息安全知识库
date: 2023-05-02
fetch_date: 2025-10-04T11:37:22.140602
---

# Dumart fuzz：让黑盒像白盒一样fuzz

[![logo](/static/logo_light.png)
![logo-dark](/static/logo_light.png)](/)

[VIPREAD 导航](/)

* [主页](/index)
* [书架](/library/category)
* [议题](/library/datas)
* [附件](/library/attachment)
* [成员](/library/authors)
* [搜索](/library/search)
* [**打赏**](/donate)
* [我要分享](/share/submit)

* [登录](/auth/login)
* [Dark](/setmode/black)

##### [主页](/) / [看雪·第六届 安全开发者峰会（2022 SDC）](/library/cid/441) / Dumart fuzz：让黑盒像白盒一样fuzz

![](https://archive1.vipread.com/covers/2023/05/topic/migration_3909_1682919283_c35ff3ba.jpg)

* 标题

  [Dumart fuzz：让黑盒像白盒一样fuzz](/library/topic/3909)
* 作者

  陈振宇 个人安全研究员
* 标签

  [Fuzzing](/library/tags/Fuzzing)
  [黑盒asan](/library/tags/%E9%BB%91%E7%9B%92asan)
  [漏洞挖掘](/library/tags/%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98)
  [安全研究](/library/tags/%E5%AE%89%E5%85%A8%E7%A0%94%E7%A9%B6)
* 简介

  + 背景：黑盒fuzz的困难
  + 状态机：是什么，为什么麻烦
  + 背景：如何能做一个最简单的黑盒fuzz
  + 状态机：如何简单地获取状态机，提高效率
  + 状态机：注入原理
  + 状态机: 为什么不在原进程fuzz
  + Fuzzer: 快照，快照的作用
  + Fuzzer: 保存快照，怎么保存
  + Fuzzer: 崩溃检测
  + Fuzzer: 路径反馈是什么
  + Fuzzer: 路径反馈
  + ASAN：是什么
  + ASAN：编译器实现
  + 黑盒ASAN
  + Fuzzer框架

  fuzzing是一种最常用的漏洞挖掘方法。在有源码的情况下，现有的fuzzing工具已经非常完善了。可以实现路径反馈，asan。当然某些复杂场景下状态机的构造也是非常麻烦的。
  但是在无源码的情况下，现有的fuzzing工具限制很大。比如peach等没有路径反馈和ASAN，没法有效地fuzz深层次的代码；基于模拟执行做的fuzz，如qemu,unicorn，有路径反馈，但是状态机的模拟很困难，而且效率较低。本次峰会介绍一种fuzzing方法。可有效解决无源码fuzz的所有缺陷，包括路径反馈，ASAN，以及方便地获得被测程序的状态机，并且更重要的是效率很高。
* 援引

  https://www.hackinn.com/index.php/archives/808/
* 提示

  本站仅做资料的整理和索引,转载引用请注明出处

###### 相关推荐

* [![](https://archive1.vipread.com/covers/2021/11/topic/migration_3586_1636340060_8d19ae9d.jpg)](/library/topic/3586)

  [高级攻防演练下的Websh](/library/topic/3586)

  2021-11-08 10:54:20.011580
* [![](//cdn.cdnjson.com/tvax3.sinaimg.cn/large/006vnxPsly1fyenn8is7xj30fz0kodws.jpg)](/library/topic/1488)

  [《信息安全研究》2016年](/library/topic/1488)

  2017-12-11 11:06:11
* [![](https://archive1.vipread.com/covers/2021/12/topic/migration_3690_1640306934_f9f846a8.jpg)](/library/topic/3690)

  [Ransomware al](/library/topic/3690)

  2021-12-24 08:48:54.854530
* [![](https://archive1.vipread.com/covers/2020/08/topic/migration_2874_1598080516_baf32dc3.jpg)](/library/topic/2874)

  [《信息安全研究》2020年](/library/topic/2874)

  2020-08-22 15:15:16.656878

[![](https://archive1.vipread.com/images/ad/flag_3.gif)](https://www.flagify.com/?ref=https://vipread.com)

###### 附件下载

* ![](/static/images/icons/file-pdf.svg)

  ###### Dumart.fuzz：让黑盒像白盒一样fuzz.pdf

  时间:  2023-05-01T13:34:47Z

  大小:
  1.55 M

  下载:  79

  [登录下载](/auth/login)

##### 附件下载

![validate_code](#)

输入验证码
刷新验证码？

提交

错误信息

###### R2直链下载:

点击下载

###### 百度网盘:提取码(svip)

正在同步,稍等片刻

###### 蓝奏云盘:

正在同步,稍等片刻

关闭

错误信息

**分享文档请发送到 [[email protected]](/cdn-cgi/l/email-protection) ,感谢支持**

© 2014-2024 [信息安全知识库](//vipread.com)
[吉ICP备15005112号-2](https://beian.miit.gov.cn/)

* [**打赏支持**](/donate)
* [友情链接](/friends)
* [服务条款](/terms)
* [RSS](/rss)
* QQ交流群: 825629062