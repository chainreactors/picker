---
title: BitUnlocker：利用Windows恢复环境提取BitLocker密钥
url: https://mp.weixin.qq.com/s/Usji6ETshYvPF2saiBtLTA
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:28:52.533889
---

# BitUnlocker：利用Windows恢复环境提取BitLocker密钥

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdXWOeFEfQywkKC1B69GPARMjU9K844EBXicPfibkGGsuz2bSCMzlY68VdpnbnicIJAx4vaPQBEMg1ibSHsmIKP0QT8I281YWUps2E/0?wx_fmt=jpeg)

# BitUnlocker：利用Windows恢复环境提取BitLocker密钥

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 微软STORM团队在2025年Black Hat和DEF CON上公开了利用Windows恢复环境（WinRE）绕过BitLocker保护的全新攻击方式。研究人员找到了WinRE在解析Boot.sdi、ReAgent.xml和BCD文件时的四个逻辑漏洞，让攻击者能在未授权状态下自动解锁OS卷，直接提取加密密钥。这些漏洞已在2025年7月补丁日修复，攻击者需要物理接触设备。

## 引言

Windows的数据保护基石是BitLocker，一种全卷加密技术，专门用来保护磁盘上的敏感数据。就算攻击者拿到设备实物，数据依然是安全、不可读的。

任何数据保护功能，其恢复能力都极其关键。为了支持BitLocker恢复，Windows Recovery Environment（WinRE）做了大量设计改动。这就引出一个核心问题：这些改动会不会给BitLocker引入新的攻击面？

我们团队在2025年Black Hat USA和DEF CON 33上首次发布了这项研究——探索WinRE中影响BitLocker的攻击面，寻找新漏洞、开发利用、实现修复，最终加固WinRE和BitLocker。研究发现了WinRE及其启动流程中的多个新漏洞，大部分属于逻辑漏洞。

这篇博文会完整展示研究过程：先介绍WinRE架构，再回顾BitLocker引入后暴露的攻击面，接着讲我们如何高效研究并利用这些攻击面。还会揭露我们找到的新漏洞和开发出的利用方法，以及如何绕过BitLocker提取受保护数据。

最后给出你现在就能用的加固措施，以及我们对后续安全工作的承诺。

## BitLocker概述

BitLocker是Windows的安全功能，提供磁盘卷的静态数据保护。基于全卷加密（FVE）技术，启用后加密目标卷，保护其上所有数据。用户可以根据需要选择加密哪些卷。默认情况下，BitLocker加密OS卷，确保OS环境内的数据安全。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcsCCpia86WDINyGEeJUzr985Wz2hSnqTmkBQmh65by4rYibh9at5l2u7o8QaxGibB0V7cKHk74c4kdYzLDFnicucS1pVdhmTYTzTo/640?wx_fmt=png&from=appmsg)

▲ 卷布局与BitLocker加密

### BitLocker威胁模型

BitLocker的设计目标是防御盗窃场景——小偷拿走你的笔记本，想提取敏感信息、破坏机器甚至植入后门。因此，BitLocker的威胁模型假设攻击者是一个普通小偷：

* 完全物理访问
* 没有高级凭证（用户名、密码等）

BitLocker是少数几个明确将物理攻击者纳入威胁模型的Windows功能。防御物理攻击者大大提高了对抗措施的难度，因为他们的能力远强于远程攻击者。

### 隐藏的攻击面——Windows恢复环境（WinRE）

理所当然，BitLocker的攻击面受限于威胁模型内攻击者可访问的接口。在检查各种接口时，WinRE格外显眼。任何BitLocker攻击者都可以在登录界面按住Shift键同时点击“重启”来直接进入WinRE。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfQjmhDpiaO8oKjWR08w3hC2wFlBLWqORqsfGJTuIUNicv19JhZNEYkOqBN3qjPKdqRXs9dCuh0EIo0OyOG2G3BuFmsibicD1kJTss/640?wx_fmt=png&from=appmsg)

▲ 从登录界面启动WinRE

考虑到WinRE符合BitLocker威胁模型、缺乏前期研究、且漏洞潜力大，我们决定对其做一次安全审查：找漏洞、做利用、修漏洞，并通过缓解常见漏洞和利用模式来加固WinRE。最终目标是提升WinRE和BitLocker的安全性与韧性。

好了，开始讲研究旅程。

## WinRE概述

### WinRE介绍

WinRE是Windows的恢复平台——用于从严重系统问题中恢复，比如启动失败、持续崩溃、BitLocker错误等。

举个例子，如果机器崩溃了，WinRE负责分析问题、识别损坏并用恢复工具修复。

如果你用Windows，大概率碰到过WinRE几次。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeH6U6KSO1F2iaxf7YkmIKsh9iaMvDXUAgtbGgm6fUP9cQ7MRvbYjmKzUyyNLTicMd0qyHDpuy13dlwZqiaLr7Lm8SnN0Ge1lldq3U/640?wx_fmt=png&from=appmsg)

▲ WinRE界面

### WinRE架构

从架构上看，WinRE运行在自己的独立操作系统（恢复OS）中。恢复OS是Windows的精简版，带有恢复专用定制。

恢复定制包括一组独特的恢复工具，集成在熟悉的蓝屏恢复UI中。暴露的恢复工具有启动修复、系统重置、系统还原等。

存储方面，整个恢复OS（包括所有可执行文件、DLL和驱动）被压缩成一个WIM文件（WinRE.wim），存在磁盘上。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfvnMyb2IicoVY1qNJwMIAicfpOWKtdMw3yBvVYHrTzRBoB7tlyHn7u9zpnbT2gbRvaNzJNQJOhnUj6tXW43Pr0tBdXml8GTHl2E/640?wx_fmt=png&from=appmsg)

▲ 恢复OS压缩为WinRE.wim

WinRE启动时，整个WIM文件从磁盘解压到RAM中，创建一个临时RAM磁盘，托管恢复OS运行环境。该环境内的任何更改都不会写回原始的WinRE.wim文件，因此恢复OS运行环境本质上是易失的——修改在重启后丢失。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcISBnR6ib4N8aHMuywzGTY32zOIupicfWZZKNISJfyFGxMvF91QsCfcIyAWXyKGNCfF1LKwUyMplR8bfMr80XxTgdnY0lhGFp4I/640?wx_fmt=png&from=appmsg)

▲ WinRE.wim RAM磁盘启动

### WinRE的BitLocker设计变更

当BitLocker首次推出时，WinRE必须进化以支持BitLocker相关故障的恢复。这带来了若干架构和设计变更。快速过一下。

### 设计变更#1：WinRE.wim迁移

第一个设计变更关于压缩恢复OS（WinRE.wim）的位置。该文件从OS卷（现在被BitLocker加密了）移到了专用的未加密恢复卷。

这个变更是必须的，因为WinRE在BitLocker故障时必须保持可访问。如果OS卷被BitLocker加密并且由于解密问题变得不可读，把WinRE放在那个卷上会阻塞恢复。由于WinRE是关键组件且必须可用，所以被移到了独立的恢复卷。这样即使OS卷不可访问，WinRE也能工作。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibejVUCulOyncgElF0BD1dMLlVYUiam8Dbp3Pr5ibC6wwaOFUuRicpPjXnialGvonGxwYZ5Id7be6icKibembvRAs7XlrDqIq5JHOxoPo/640?wx_fmt=png&from=appmsg)

▲ WinRE.wim迁移

### 设计变更#2：可信WIM启动

第二个设计变更聚焦WinRE.wim文件的完整性。为了支持完整性验证，引入了“可信WIM启动”（Trusted WIM Boot）功能。它通过将WinRE.wim的哈希值与已知可信哈希比对来验证完整性。

哈希匹配 → OS卷自动解锁。哈希不匹配 → OS卷保持锁定。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfEqAqTlJSacKzumRTT5MB7pVx0lRtY52PHvXDEfXT5whzdFsWibNYPycTYjjMBBUcZicTJMp8LEsNJibUsj5EADibBu6Lv0PZo7x8/640?wx_fmt=png&from=appmsg)

▲ 可信WIM启动哈希比对

两种状态（自动解锁和锁定）决定了WinRE对主OS的访问级别。自动解锁状态下，WinRE拥有完全访问权限；锁定状态下则完全无法访问。

这个变更是必要的，因为WinRE现在位于未加密的恢复卷上，不能再盲目信任。有了可信WIM启动，任何对WinRE.wim的未授权修改都会破坏其信任，有效阻止篡改。

### 设计变更#3：卷重新锁定

第三个设计变更聚焦于限制那些对BitLocker存在固有风险的恢复工具。例如，暴露的恢复工具里有命令提示符。为了防止攻击者滥用命令提示符访问BitLocker保护的数据，WinRE加入了卷重新锁定功能。每次选择有风险的恢复工具时，该功能会触发并重新锁定OS卷。要再次获得OS卷的访问权，用户必须手动输入BitLocker恢复密钥——否则所有内容完全不可访问。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfribHj9AyIvaN626A5E5kek8eKVyjNqE4NdU02XvbJVOOaGZGPIfD1xuYgLdPubBGS2nJO7YZ08tqicoICLKoUVicQMeIOMcweYc/640?wx_fmt=png&from=appmsg)

▲ WinRE UI卷重新锁定功能

例如，如果攻击者启动命令提示符恢复工具而未插入BitLocker恢复密钥，访问BitLocker加密卷将被拒绝，出现以下锁定错误：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdSeM9LGwmY47jzCrc7icDAnv8N6GViatgqkicvwibPsJ3UoYtbMic1Iz05LfcicJ9gswLfyvXdAEGzfJgibpMpyqM1X1VLhP1ME6bGdA/640?wx_fmt=png&from=appmsg)

▲ WinRE UI卷重新锁定演示

### 设计变更总结

总结设计变更的影响：只要WinRE.wim是可信的，且没有触发有风险的恢复工具，OS卷就会自动解锁，WinRE无需用户干预即可恢复。反之，如果WinRE.wim被未授权修改或触发了有风险的工具，OS卷会被重新锁定，阻止WinRE访问。

## 暴露的攻击面

那么关键问题来了——这些设计调整是否暴露了攻击面？

结果发现，在自动解锁状态下，WinRE会从不受保护的卷（特别地，EFI卷和恢复卷）解析文件。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfzDiakv1Kj7UYSo9nYPdRWU3k0CMSdt7thicoOUCngcKzt4qkRwFWb4G3ajG3Bdib6mOOm0dA0oRJd2xbluBJpcvlibFbWcxLhVFk/640?wx_fmt=png&from=appmsg)

▲ WinRE从不受保护的卷解析文件

这个解析呈现了一个非常有趣的攻击面，在BitLocker引入之前没什么价值去探索——因为没有安全边界需要跨越。在BitLocker之前，即使在WinRE内获得完全代码执行，物理攻击者也无法获得新能力。而有了BitLocker，任何在自动解锁状态下于WinRE内的代码执行都可以用来绕过BitLocker并提取所有受保护的秘密。

## 本篇博文重点

这篇博文将聚焦探索以下3个外部文件：

* Boot.sdi – 位于恢复卷
* ReAgent.xml – 位于恢复卷
* Boot Configuration Data (BCD) store – 位于EFI卷

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeOYnM28PKicERv7D6bdEpGcNVYafFn3RG5ZkAmr40s98JGte4Wp7dWV5LNDibOiatP7AecOicm7cREMon1wNwZQTtSNWqaMGJOkFo/640?wx_fmt=png&from=appmsg)

▲ 本篇博文聚焦的文件

剩余部分将专注于攻击这些文件的解析器。

## 攻击Boot.sdi解析

SDI是System Deployment Image的缩写。SDI文件在从RAM磁盘启动时可选用。

RAM磁盘启动是从静态操作系统镜像中提取并创建基于RAM的磁盘的过程。与传统启动场景（OS磁盘在物理存储上）不同，这里OS磁盘完全在RAM中。随后磁盘I/O请求被路由到RAM磁盘而非物理存储。

RAM磁盘启动的一个例子是WinRE启动——其中WinRE.wim是静态OS镜像。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfpjQ0mB0dr2BHdQibe5dXNpibV9Ue9kZuDRc5O427SQbpNlSVztKOpMV4TicSf7zCgrRWYyxvOFuibeia0eiaIa3Og5kGw8eWDhW8qM/640?wx_fmt=png&from=appmsg)

▲ RAM磁盘启动演示

关于SDI的用法：如果指定，SDI文件会被预置到分配的RAM磁盘内存区域内的虚拟磁盘中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeN0VeHib8Bomd82nPBV4Bopb3IJFbvU2x3iab5J8jkic5LmqwAGIc8GHicHlVjWncSrbjmBRZReiaGicq8gYKKvxA9ScblTBJqzHJAg/640?wx_fmt=png&from=appmsg)

▲ 包含SDI文件的RAM磁盘缓冲区布局

SDI文件格式主要由二进制blob组成，通过一个“blob表”组织，该表保存每个blob的元数据，包括类型、大小和文件内的相对偏移。我们不会深入完整的SDI格式，只关注用于启动WinRE.wim时指定的特定blob：

* WIM blob – 描述WIM镜像的blob
* NTFS blob – 描述NTFS卷的blob

下面是整个RAM磁盘缓冲区布局的演示。首先，SDI文件包含一个指向WinRE.wim文件的WIM blob，以及一个指向空NTFS卷的NTFS blob。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdIsu0NSTmosZYKmC6oeZOraia6y4Be1qDwN5Zdfs0lgOObY5ibniahXhRaCURlIBIHib5k53oib18JmBamfYZq8JnxAmt2OQsvdrNQ/640?wx_fmt=png&from=appmsg)

▲ WinRE.wim启动时的RAM磁盘缓冲区布局

你可能会问，为什么需要一个空的NTFS卷？这是为了保持与Windows组件的兼容性，这些组件无法直接在WIM卷作为OS卷的情况下工作。空的NTFS卷允许WIM卷以标准NTFS卷的形式呈现，从而能与无法直接在WIM卷上操作的Windows组件无缝交互。

对SDI文件和整个RAM磁盘启动过程有了更好理解后，我们来看看负责加载RAM磁盘的代码。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfECwWSicEcQ5Mz0oarq4iaX0jsyg0E4XKcN37iaEBGrjBovBCQOPklo6qeficicgFvwMVkMXjCZnmRFc9pjUh8XG4JWAvsYUjMopto/640?wx_fmt=png&from=appmsg)

▲ RAM磁盘加载伪代码

代码首先分配足够大的RAM磁盘缓冲区来容纳SDI和WIM文件。然后，将SDI文件加载到分配的缓冲区中。接着，将WIM文件加载到缓冲区中，跟在SDI之后。加载API会计算已加载WIM文件的哈希，这个哈希稍后用于可信WIM启动完整性验证。最后，通过将SDI中WIM blob指定的偏移量加到RAM磁盘缓冲区起始地址来计算要启动的WIM的地址。值得注意的是，已验证哈希的WIM与启动的WIM之间没有任何关联。缺乏关联允许任意设置WIM偏移量。

由于我们可以任意设置WIM偏移量，因此可以将不受信任的WIM附加到SDI文件中，并相应地调整WIM偏移量。

因为可信WIM启动哈希验证使用磁盘上存储的WIM的哈希，而不是SDI WIM偏移量指示的WIM，所以哈希验证会成功——因为磁盘上的可信WIM没有改变。然而，系统将使用SDI WIM偏移量指定的不受信任WIM启动。

下面是利用场景中整个RAM磁盘缓冲区布局的演示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibe9JEPfgpDoqJFZrbxIricffpmgJuBZck6kSkdQHy1mfrHTk1peibEtBM3LWcu4pBUDF7eDbcx9ibKKkWfWy0XhzUbdujJRCYduYg/640?wx_fmt=png&from=appmsg)

▲ 利用场景中的RAM磁盘缓冲区布局

这个漏洞允许绕过可信WIM启动验证——我们可以将不受信任的WIM作为可信WIM启动，并让我们的不受信任WIM享受自动解锁功能，从而绕过BitLocker并提取秘密。

为了演示秘密提取，我们创建了一个WinRE.wim的克隆，并将其启动应用程序改为命令提示符（而不是恢复环境程序）。然后将这个WIM附加到Boot.sdi，验证偏移量正确，并启动进入WinRE。结果是命令提示符在自动解锁状态下启动。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibejagpZZH9t47Qbg2iasGnG1SMdRjQXPJUrJt8Iwody3drAoK81gicZib0JY9XvaWlNRsPiatXe1xI...