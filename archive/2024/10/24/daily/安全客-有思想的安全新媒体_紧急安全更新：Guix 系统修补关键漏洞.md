---
title: 紧急安全更新：Guix 系统修补关键漏洞
url: https://www.anquanke.com/post/id/301175
source: 安全客-有思想的安全新媒体
date: 2024-10-24
fetch_date: 2025-10-06T18:46:12.237513
---

# 紧急安全更新：Guix 系统修补关键漏洞

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 紧急安全更新：Guix 系统修补关键漏洞

阅读量**52105**

发布时间 : 2024-10-23 15:12:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/urgent-security-update-guix-system-patches-critical-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![guix-daemon vulnerability]()

在广泛使用的 Guix 系统中发现了一个严重的安全漏洞，尤其影响到 guix-daemon。该漏洞可使本地用户的权限升级，从而在多用户环境中篡改编译输出。

问题的核心在于 guix-daemon 对构建输出的处理，尤其是在构建失败时。根据该公告，“guix-daemon 已在构建容器中的相同位置提供了失败的派生构建输出，这很有帮助”。虽然这一功能在某些情况下非常有用，但它也带来了安全风险。

攻击者可以利用这一机制，启动派生构建，生成具有 setuid 或 setgid 位的二进制文件，从而授予特殊权限。如果构建失败，攻击者就会获得二进制文件的访问权限，然后就可以通过升级权限来执行二进制文件。该公告警告说：”攻击者或合作用户可以执行二进制文件，获得权限，然后使用信号和 procfs 组合冻结生成器，通过 /proc/$PID/fd 打开生成器已打开的任何文件，并随心所欲地覆盖文件。

这一漏洞在多用户系统中尤其危险，因为它允许攻击者操纵任何用户启动的构建程序，有可能对广泛使用的程序产生被破坏的输出结果。公告指出，该漏洞也会影响成功的构建，在权限、所有权和时间戳尚未规范化的情况下，会引入一个小的机会窗口。这使得该漏洞更加令人担忧。

为帮助用户确定其系统是否存在漏洞，我们提供了一个概念验证脚本。

```
(use-modules (guix)
             (srfi srfi-34))

(define maybe-setuid-file
  ;; Attempt to create a setuid file in the store, with one of the build
  ;; users as its owner.
  (computed-file "maybe-setuid-file"
                 #~(begin
                     (call-with-output-file #$output (const #t))
                     (chmod #$output #o6000)

                     ;; Failing causes guix-daemon to copy the output from
                     ;; its temporary location back to the store.
                     (exit 1))))

(with-store store
  (let* ((drv (run-with-store store
                (lower-object maybe-setuid-file)))
         (out (derivation->output-path drv)))
    (guard (c (#t
               (if (zero? (logand #o6000 (stat:perms (stat out))))
                   (format #t "~a is not setuid: your system is not \
vulnerable.~%"
                           out)
                   (format #t "~a is setuid: YOUR SYSTEM IS VULNERABLE.

Run 'guix gc' to remove that file and upgrade.~%"
                           out))))
      (build-things store (list (derivation-file-name drv))))))
```

运行

```
guix repl -- setuid-exposure-vuln-check.scm
```

guix repl — setuid-exposure-vuln-check.scm
该脚本会告知用户其 guix-daemon 是否存在漏洞，因此对系统管理员和用户来说都是至关重要的工具。

为缓解这一漏洞，我们引入了两个重要的修复程序：

* **清理失败构建的权限：** 现在会对失败的编译输出进行消毒，以确保在将任何 setuid/setgid 位移至存储区之前将其删除。这可防止攻击者访问不受信任的二进制文件。
* **对成功构建的权限进行规范化：** 只有在权限完全规范化后，成功的构建输出才会被移至存储区，从而进一步降低了攻击面。

这些修复是近期提交的一部分，建议用户将其 guix-daemon 升级到这些版本。此外，运行 guix gc 将有助于清理可能仍然存在的失败构建输出。

Guix 项目强烈建议所有用户立即升级 guix-daemon。升级程序因使用 Guix 的方式而异，但对大多数用户来说，升级过程简单明了。Guix 系统用户可使用以下命令进行升级：

```
guix pull
sudo guix system reconfigure /run/current-system/configuration.scm
sudo herd restart guix-daemon
```

对于在其他发行版上使用 Guix 作为软件包管理器的用户，升级过程包括提取最新更改并重启 guix-daemon 服务：

```
sudo --login guix pull
sudo systemctl restart guix-daemon.service
```

该公告还提到了确保守护进程套接字仅限受信任用户使用的重要性，尤其是那些使用 -disable-chroot 的用户。

本文翻译自securityonline [原文链接](https://securityonline.info/urgent-security-update-guix-system-patches-critical-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301175](/post/id/301175)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/urgent-security-update-guix-system-patches-critical-vulnerability/)

如若转载,请注明出处： <https://securityonline.info/urgent-security-update-guix-system-patches-critical-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)