---
title: Linux内核常用保护和绕过技术
url: http://blog.topsec.com.cn/linux%e5%86%85%e6%a0%b8%e5%b8%b8%e7%94%a8%e4%bf%9d%e6%8a%a4%e5%92%8c%e7%bb%95%e8%bf%87%e6%8a%80%e6%9c%af/
source: 天融信阿尔法实验室
date: 2023-02-17
fetch_date: 2025-10-04T06:52:36.230431
---

# Linux内核常用保护和绕过技术

[![天融信阿尔法实验室](http://alphalab1-wordpress.stor.sinaapp.com/uploads/2018/11/2018111607001998_Alpha-logo-V0.1.png)](https://blog.topsec.com.cn/ "天融信阿尔法实验室")

Browse
Search

* [首页](http://blog.topsec.com.cn/)
  + [天融信官网](http://www.topsec.com.cn/)
* [漏洞分析](https://blog.topsec.com.cn/category/%E6%BC%8F%E6%B4%9E%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90/)
* [技术文章](https://blog.topsec.com.cn/category/%E6%8A%80%E6%9C%AF%E6%96%87%E7%AB%A0/)
* [样本分析](https://blog.topsec.com.cn/category/%E6%BC%8F%E6%B4%9E%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/%E6%A0%B7%E6%9C%AC%E5%88%86%E6%9E%90/)
* [人才招聘](https://blog.topsec.com.cn/%E4%BA%BA%E6%89%8D%E6%8B%9B%E8%81%98/)
* [关于](https://blog.topsec.com.cn/%E5%85%B3%E4%BA%8E/)

## [停机维护通知](https://blog.topsec.com.cn/shutdown/ "停机维护通知")

访客您好：

10月9日起，本站将进行停机维护，预计持续一个月（自2025年10月9日至2025年11月8日）。维护结束后，将重新开启服务。感谢您的理解与支持。

天融信阿尔法实验室

2025年9月30日

* 本文作者： 天融信安全应急响应中心
* |
* 2025年9月30日
* |
* [未分类](https://blog.topsec.com.cn/category/uncategorized/ "未分类")
* |

## [大模型组件漏洞与应用威胁安全研究报告](https://blog.topsec.com.cn/security-research-report-on-vulnerabilities-and-application-threats-of-large-model-components/ "大模型组件漏洞与应用威胁安全研究报告")

近年来，大模型呈现出蓬勃发展的态势，为人工智能行业的技术进步源源不断地注入创新活力。然而，在大模型开发者致力于提升模型效果、拓展模型能力的同时，大模型的安全性问题也不容忽视，亟待给予高度关注。

随着大模型架构复杂性持续提升，其面临的攻击面不断增多。**究其根本，导致缺陷与漏洞频发的主要原因，或是因为AI技术的快速发展与部分开发者“功能优先、安全滞后”的观念。**

其一，AI模型作为高度复杂的代码系统，其庞大的参数规模和交互接口为潜在攻击者提供了丰富的攻击面。

其二，在激烈的市场竞争压力下，许多开发团队将研发速度置于安全考量之上，直接导致安全防护[......]

[Read more](https://blog.topsec.com.cn/security-research-report-on-vulnerabilities-and-application-threats-of-large-model-components/)

* 本文作者： 天融信安全应急响应中心
* |
* 2025年3月17日
* |
* [技术文章](https://blog.topsec.com.cn/category/%E6%8A%80%E6%9C%AF%E6%96%87%E7%AB%A0/ "技术文章")
* |

## [XZ Utils（CVE-2024-3094） 供应链投毒深度分析](https://blog.topsec.com.cn/xz-utils%EF%BC%88cve-2024-3094%EF%BC%89-%E4%BE%9B%E5%BA%94%E9%93%BE%E6%8A%95%E6%AF%92%E6%B7%B1%E5%BA%A6%E5%88%86%E6%9E%90/ "XZ Utils（CVE-2024-3094） 供应链投毒深度分析")

## 事件概述

近日，微软一名软件工程师Andres Freund公开披露，其观察到liblzma库存在一些奇怪的现象，包括在用ssh远程登录异常及内存错误。经过分析，其确认在liblzma上游组件xz-utils中存在后门代码，后门或可导致攻击者能够在ssh登录认证前，执行攻击者指定的任意代码，可对Linux服务器安全造成严重影响。

综合情况看，这是一起开源软件供应链投毒攻击事件。攻击者伪装成开发者，借更新之名，秘密的向xz-utils中加入后门代码，导致xz-utils中的liblzma易受攻击。

OpenSSH用于SSH登录，广泛部署于基于Linux发行的操作系统中。其默认不依赖[......]

[Read more](https://blog.topsec.com.cn/xz-utils%EF%BC%88cve-2024-3094%EF%BC%89-%E4%BE%9B%E5%BA%94%E9%93%BE%E6%8A%95%E6%AF%92%E6%B7%B1%E5%BA%A6%E5%88%86%E6%9E%90/)

* 本文作者： 天融信安全应急响应中心
* |
* 2024年7月17日
* |
* [技术文章](https://blog.topsec.com.cn/category/%E6%8A%80%E6%9C%AF%E6%96%87%E7%AB%A0/ "技术文章")
* |

## [电子支付漏洞专题报告](https://blog.topsec.com.cn/%E7%94%B5%E5%AD%90%E6%94%AF%E4%BB%98%E6%BC%8F%E6%B4%9E%E4%B8%93%E9%A2%98%E6%8A%A5%E5%91%8A/ "电子支付漏洞专题报告")

目录

1.  电子支付的现状

1.1  电子支付的定义

1.2  电子支付在我国的应用

1.3  电子支付的主要形式

1.4  电子支付相关漏洞的统计

1.5  电子支付的安全风险

1.5.1  线下支付安全风险

1.5.2  线上支付安全风险

2.  电子支付原理与实现

2.1  简述

2.2  线下支付

2.2.1  线下支付概念

2.2.2  线下支付一般流程

2.2.3  线下支付技术分类

2.3  线上支付

2.3.1  线上支付概述

2.3.2  线上支付一般流程

2.3.3[......]

[Read more](https://blog.topsec.com.cn/%E7%94%B5%E5%AD%90%E6%94%AF%E4%BB%98%E6%BC%8F%E6%B4%9E%E4%B8%93%E9%A2%98%E6%8A%A5%E5%91%8A/)

* 本文作者： topsec\_support
* |
* 2023年12月6日
* |
* [未分类](https://blog.topsec.com.cn/category/uncategorized/ "未分类")
* |

## [EvilParcel漏洞分析](https://blog.topsec.com.cn/evilparcel%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90/ "EvilParcel漏洞分析")

### **引言**

今年年初，国内独立研究机构DarkNavy发表文章，指出某知名购物APP中存在漏洞攻击行为。这引起了广泛的关注和讨论。值得注意的是，其中涉及到一个已被编号为CVE-2017-13315的Android系统漏洞，这个漏洞在我们的研究中引起了浓厚的兴趣。CVE-2017-13315是一个已知的Android系统漏洞，其利用了Parcelable对象的序列化和反序列化过程中的不一致性。这种不一致性可能导致任意代码执行的风险，从而绕过手机系统的保护机制，实现对用户设备的潜在攻击。该漏洞的危害性较高，攻击者可以利用它隐蔽地安装和卸载恶意应用程序，对用户的隐私和安全造成严重威胁。

早在201[......]

[Read more](https://blog.topsec.com.cn/evilparcel%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90/)

* 本文作者： topsec\_support
* |
* 2023年11月29日
* |
* [未分类](https://blog.topsec.com.cn/category/uncategorized/ "未分类")
* |

## [Linux内核常用保护和绕过技术](https://blog.topsec.com.cn/linux%E5%86%85%E6%A0%B8%E5%B8%B8%E7%94%A8%E4%BF%9D%E6%8A%A4%E5%92%8C%E7%BB%95%E8%BF%87%E6%8A%80%E6%9C%AF/ "Linux内核常用保护和绕过技术")

###

* 1、内核是什么？
* 2、内核漏洞
* 3、Linux内核保护与绕过
  + 3.1、KASLR 保护
  + 3.2、SMEP&SMAP保护
  + 3.3、KPTI保护
* 4、新内核漏洞利用方法
  + 4.1、pipe管道技术
  + 4.2、kernel5.x版本和kernel4.x版本的不同
* 5、总结

### 1、内核是什么？

内核是操作系统的核心部分。内核负责管理计算机的硬件资源，并实现操作系统的基本功能。内核是操作系统中最重要的部分，它是操作系统与硬件之间的桥梁。内核可以被看作是操作系统的“心脏”，负责控制和管理计算机系统的所有硬件和软件资源。不同的操[......]

[Read more](https://blog.topsec.com.cn/linux%E5%86%85%E6%A0%B8%E5%B8%B8%E7%94%A8%E4%BF%9D%E6%8A%A4%E5%92%8C%E7%BB%95%E8%BF%87%E6%8A%80%E6%9C%AF/)

* 本文作者： 天融信安全应急响应中心
* |
* 2023年2月16日
* |
* [技术文章](https://blog.topsec.com.cn/category/%E6%8A%80%E6%9C%AF%E6%96%87%E7%AB%A0/ "技术文章")
* |

## [DedeCMS文件上传漏洞分析](https://blog.topsec.com.cn/dedecms%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90/ "DedeCMS文件上传漏洞分析")

# 前言

前段时间看到有篇文章是关于DedeCMS后台文件上传(CNVD-2022-33420)，是绕过了对上传文件内容的黑名单过滤，碰巧前段时间学习过关于文件上传的知识，所以有了这篇文章，对DedeCMS的两个文件上传漏洞(CVE-2018-20129、CVE-2019-8362)做一个分析。

# 简介

DedeCMS简介
DedeCMS由上海卓卓网络科技有限公司研发的国产PHP网站内容管理系统；具有高效率标签缓存机制；允许对类同的标签进行缓存，在生成 HTML的时候，有利于提高系统反应速度，降低系统消耗的资源。众多的应用支持；为用户提供了各类网站建设的一体化解决方案，在本版本中，增加了分类[......]

[Read more](https://blog.topsec.com.cn/dedecms%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90/)

* 本文作者： 天融信安全应急响应中心
* |
* 2022年5月31日
* |
* [漏洞分析](https://blog.topsec.com.cn/category/%E6%BC%8F%E6%B4%9E%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90/ "漏洞分析")
* |

## [CVE-2022-21882 Win32k内核提权漏洞深入分析](https://blog.topsec.com.cn/cve-2022-21882-win32k%E5%86%85%E6%A0%B8%E6%8F%90%E6%9D%83%E6%BC%8F%E6%B4%9E%E6%B7%B1%E5%85%A5%E5%88%86%E6%9E%90/ "CVE-2022-21882 Win32k内核提权漏洞深入分析")

* 1、漏洞介绍
* 2、漏洞影响版本
* 3、分析环境
* 4、背景知识
* 5、漏洞成因
* 6、利用漏洞的流程
  + 6.1、触发用户态回调
  + 6.2、HOOK回调函数
  + 6.3、修改窗口模式为模式1
  + 6.4、回调返回伪造偏移量
  + 6.5、泄露内核窗口数据结构
  + 6.6、如何布局内存
* 7、EXP分析调试
* 8、两种提权方式
  + 8.1、设置token
  + 8.2、修改Privileges
* 9、补丁分析
* 10、参考链接

CVE-2022-21882漏洞是Windows系统的一个本地提权漏洞，微软在2022年1月份安全更新中修补此漏洞。[......]

[Read more](https://blog.topsec.com.cn/cve-2022-21882-win32k%E5%86%85%E6%A0%B8%E6%8F%90%E6%9D%83%E6%BC%8F%E6%B4%9E%E6%B7%B1%E5%85%A5%E5%88%86%E6%9E%90/)

* 本文作者： 天融信安全应急响应中心
* |
* 2022年4月18日
* |
* [技术文章](https://blog.topsec.com.cn/category/%E6%8A%80%E6%9C%AF%E6%96%87%E7%AB%A0/ "技术文章")
* |

## [CVE-2021-33742：Internet Explorer MSHTML堆越界写漏洞分析](https://blog.topsec.com.cn/cve-2021-33742-analysis_of_internet_explorer_mshtml_heap_out-of-bounds_write_vulnerability/ "CVE-2021-33742：Internet Explorer MSHTML堆越界写漏洞分析")

* 1、漏洞背景
* 2、漏洞简介
* 3、分析环境
  + 3.1、提取漏洞模块
  + 3.2、关闭ASLR
* 4、漏洞复现
* 5、Internet Explorer DOM树的结构
  + 5.1、以文本为中心的设计
  + 5.2、增加复杂性层次结构
  + 5.3、原来的DOM没有经过封装
* 6、漏洞原理分析
  + 6.1、逆向mshtml.dll中此漏洞的相关类
    - 6.1.1、CSpliceTreeEngine
    - 6.1.2、CTreeNode
    - 6.1.3、CTreePos
    - 6.1.4、CTreeDataPos
      * 6.1.4.1、Tree::Te[......]

[Read more](https://blog.topsec.com.cn/cve-2021-33742-analysis_of_internet_explorer_mshtml_heap_out-of-bounds_write_vulnerability/)

* 本文作者：
* |
* 2022年1月24日
* |
* [技术文章](https://blog.topsec.com.cn/category/%E6%8A%80%E6%9C%AF%E6%96%87%E7%AB%A0/ "技术文章")
* |

## [CVE-2021-22204 GitLab RCE之exiftool代码执行漏洞深入分析（二）](https://blog.topsec.com.cn/cve-2021-22204-gitlab-rce%E4%B9%8Bexiftool%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E6%B7%B1%E5%85%A5%E5%88%86%E6%9E%90%EF%BC%88%E4%BA%8C%EF%BC%89/ "CVE-2021-22204 GitLab RCE之exiftool代码执行漏洞深入分析（二）")

## 目标导读

* 1 前言
* 2 前置知识
  + 2.1 JPEG文件格式
  + 2.2 Perl模式匹配
* 3 exiftool源码调试到漏洞分析
  + 3.1 环境搭建
  + 3.2 漏洞简介
  + 3.3 exiftool是如何解析嵌入的0xc51b标签
  + 3.4 exiftool是如何调用parseAnt函数
  + 3.5 parseAnt函数分析
  + 3.6 parseAnt漏洞分析
* 4 漏洞利用
  + 4.1 DjVu文件生成
  + 4.2 JPG文件生成
* 5 漏洞修复
* 6 总结

## 前言

安全研究员`vakzz`于4月7日在hackerone[......]

[Read more](https://blog.topsec.com.cn/cve-2021-22204-gitlab-rce%E4%B9%8Bexiftool%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E6%B7%B1%E5%85%A5%E5%88%86%E6%9E%90%EF%BC%88%E4%BA%8C%EF%BC%89/)

* 本文作者：
* |
* 2022年1月19日
* |
* [未分类](https://blog.topsec.com.cn/category/uncategorized/ "未分类")
* |

[Older Posts →](https://blog.top...