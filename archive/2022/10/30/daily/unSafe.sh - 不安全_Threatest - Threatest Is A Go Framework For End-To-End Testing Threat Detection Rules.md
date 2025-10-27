---
title: Threatest - Threatest Is A Go Framework For End-To-End Testing Threat Detection Rules
url: https://buaq.net/go-133248.html
source: unSafe.sh - 不安全
date: 2022-10-30
fetch_date: 2025-10-03T21:17:23.038877
---

# Threatest - Threatest Is A Go Framework For End-To-End Testing Threat Detection Rules

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/900f425202e8e23ad32e035c3a4e05bb.jpg)

Threatest - Threatest Is A Go Framework For End-To-End Testing Threat Detection Rules

Threatest is a Go framework for testing threat detection end-to-end. Threatest allows you t
*2022-10-29 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-133248.htm)
阅读量:31
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMUhm2uT2ltnEQvEcgG6dWPNcos-X4Lda7bnmLlvFMXDG7KPRiGxhBI3PH-pTApjJtheZ16SYXEKzrm-aK7Hd-qBxyj40Ui3i1s8UFNc5hws554S4VDnQndYceZTHDjBTsgIeSP9XaY90GU6vh-74gdCTmfc_itmh3kDOMSDojd_1MYZBpb1ZhTouGrw/w640-h374/go_threat.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMUhm2uT2ltnEQvEcgG6dWPNcos-X4Lda7bnmLlvFMXDG7KPRiGxhBI3PH-pTApjJtheZ16SYXEKzrm-aK7Hd-qBxyj40Ui3i1s8UFNc5hws554S4VDnQndYceZTHDjBTsgIeSP9XaY90GU6vh-74gdCTmfc_itmh3kDOMSDojd_1MYZBpb1ZhTouGrw/s1400/go_threat.png)

Threatest is a Go framework for testing [threat detection](https://www.kitploit.com/search/label/Threat%20Detection "threat detection") end-to-end.

Threatest allows you to **detonate** an attack technique, and verify that the alert you expect was generated in your favorite security platform.

Read the announcement blog post: [https://securitylabs.datadoghq.com/articles/threatest-end-to-end-testing-threat-detection/](https://securitylabs.datadoghq.com/articles/threatest-end-to-end-testing-threat-detection/ "https://securitylabs.datadoghq.com/articles/threatest-end-to-end-testing-threat-detection/")

## Concepts

### Detonators

A **detonator** describes how and where an attack technique is executed.

Supported detonators:

* Local command execution
* SSH command execution
* Stratus Red Team
* AWS detonator

### Alert matchers

An **alert matcher** is a platform-specific integration that can check if an expected alert was triggered.

Supported alert matchers:

* Datadog security signals

### Detonation and alert correlation

Each detonation is assigned a UUID. This UUID is reflected in the detonation and used to ensure that the matched alert corresponds exactly to this detonation.

The way this is done depends on the detonator; for instance, Stratus [Red Team](https://www.kitploit.com/search/label/Red%20Team "Red Team") and the AWS Detonator inject it in the user-agent; the SSH detonator uses a parent process containing the UUID.

## Sample usage

See [examples](https://github.com/DataDog/threatest/blob/main/examples "examples") for complete usage example.

### Testing Datadog Cloud SIEM [signals](https://www.kitploit.com/search/label/Signals "signals") triggered by Stratus Red Team

```
threatest := Threatest()

threatest.Scenario("AWS console login").

assert.NoError(t, threatest.Run())
```

### Testing Datadog Cloud Workload Security signals triggered by running commands over SSH

```
ssh, _ := NewSSHCommandExecutor("test-box", "", "")

threatest := Threatest()

threatest.Scenario("curl to metadata service").
  WhenDetonating(NewCommandDetonator(ssh, "curl http://169.254.169.254 --connect-timeout 1")).
  Expect(DatadogSecuritySignal("EC2 Instance Metadata Service Accessed via Network Utility"))

assert.NoError(t, threatest.Run())
```

Threatest - Threatest Is A Go Framework For End-To-End Testing Threat Detection Rules
![Threatest - Threatest Is A Go Framework For End-To-End Testing Threat Detection Rules](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMUhm2uT2ltnEQvEcgG6dWPNcos-X4Lda7bnmLlvFMXDG7KPRiGxhBI3PH-pTApjJtheZ16SYXEKzrm-aK7Hd-qBxyj40Ui3i1s8UFNc5hws554S4VDnQndYceZTHDjBTsgIeSP9XaY90GU6vh-74gdCTmfc_itmh3kDOMSDojd_1MYZBpb1ZhTouGrw/s72-w640-c-h374/go_threat.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/10/threatest-threatest-is-go-framework-for.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)