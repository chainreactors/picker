---
title: 【漏洞通告】OpenJDKxa0Java4Shellxa0远程代码执行漏洞
url: https://mp.weixin.qq.com/s/PHqI4XIMVNfbVBPWsCzkGA
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:43:51.958109
---

# 【漏洞通告】OpenJDKxa0Java4Shellxa0远程代码执行漏洞

# 【漏洞通告】OpenJDK Java4Shell 远程代码执行漏洞

云鼎实验室
云鼎实验室

云鼎实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 概述

OpenJDK（全称 Open Java Development Kit）是 Java 平台标准版（Java SE）的免费开源实现。

腾讯云安全中心监测到，OpenJDK 被披露其存在内存破坏导致的远程代码执行漏洞，漏洞编号 **CVE-2026-114938**，代号 "Java4Shell"。可导致未经身份验证的远程攻击者通过向 Base64 解码器提交特制的畸形输入，触发堆内存越界写入，进而导致内存泄露或远程代码执行等危害。

为避免您的业务受影响，腾讯云安全建议您及时开展安全自查，如在受影响范围，请您及时进行更新修复，避免被外部攻击者入侵。

## 漏洞详情

| 字段 | 内容 |
| --- | --- |
| 漏洞名称 | OpenJDK "Java4Shell" 内存破坏远程代码执行漏洞 |
| 漏洞编号 | **CVE-2026-114938** |
| 危害等级 | 高风险 |
| 漏洞类型 | 内存破坏（堆越界写入） |
| 影响范围 | OpenJDK >= 17.0.6；Oracle Java SE / GraalVM 多个版本（见「影响版本」） |

在 OpenJDK 17.0.6 及以上版本的 x86-64 Base64 解码器 intrinsic 中，由于其在处理带填充符的尾部输入时，对输出长度的计算存在缺陷：当输入为 64 个 'A' 后跟一个 '='（共 65 字节）时，处理填充符会使 output\_len 下溢为负值，随后 bzhiq 指令使 output\_mask 变为全 1（-1u64）。在使用 evmovdqub（AVX-512 指令）执行写入时，全 1 掩码会导致完整的 64 字节写入，而实际分配的结果缓冲区仅 50 字节，从而从偏移 48 处开始造成越界写入。攻击者可利用该定值越界写入覆盖相邻对象的长度字段，将其转换为可控的线性写原语，并结合堆布局控制泄露堆内存，最终实现远程代码执行。

该漏洞的影响范围极为广泛，在默认配置下即可在众多广泛部署的 Java 应用中实现远程代码执行。其中，无需认证即可触发 RCE 的应用包括 Keycloak、Atlassian Jira、Atlassian Confluence、JFrog Artifactory、Jenkins 和 PingFederate；需认证后可触发 RCE 的应用包括 Apache Kafka Broker、Apache Solr、Elasticsearch、Gerrit 和 Spinnaker。此外，基于 Apache Struts 和 Spring Boot 等常用框架构建的示例应用同样可被利用，而认证、文件上传等常规功能也可能暴露易受攻击的 Base64 解码器，使潜在影响远超上述已测试的产品。即便是不对外提供任何服务的 Java 程序，只要它向恶意服务器发起 TLS 连接，也可能在客户端侧遭到攻击。

## 漏洞风险

未经身份验证的远程攻击者利用该漏洞可导致 Java 堆内存泄露（可能包含 PII、私钥、令牌等敏感信息），并可进一步实现远程代码执行，导致目标服务器完全失陷等危害。

## 影响版本

**受影响版本：**

* OpenJDK >= 17.0.6。
* Oracle Java SE 8u511b33-perf。
* Oracle Java SE 17.0.21.0.3。
* Oracle Java SE 21.0.13.0.3。
* Oracle Java SE 25.0.5.0.3。
* Oracle Java SE 27.0.1.0.3。
* Oracle GraalVM for JDK 17.0.21.0.3。
* Oracle GraalVM for JDK 21.0.13.0.3。
* Oracle GraalVM Enterprise Edition 21.3.20.0.3。

**官方修复后的安全版本：**

* 官方发布的安全补丁（公告未提供具体版本号，请以官方安全公告为准）。

## 处置建议

**官方修复方案：**官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，升级至安全版本。

* 官方安全公告：https://www.oracle.com/security-alerts/cspunov2026.html。

**缓解措施：**

* 在 x86-64 主机上通过启动参数 `-XX:-UseBASE64Intrinsics` 禁用硬件加速的 Base64 编码/解码，或使用 `-XX:UseAVX=2` 禁用 AVX-512（注意：ARM 平台不支持该参数，会导致启动失败）。
* 检查 CPU 是否支持 AVX-512 VBMI 指令集：执行 `grep -m1 '^flags' /proc/cpuinfo | tr ' ' '\n' | grep -E '^(avx512f|avx512bw|avx512vbmi|bmi2)$'`，输出需包含全部四个标志。
* 评估应用中对 Base64 解码的使用场景，避免在安全敏感路径中处理不可信输入。

**注：**建议您在升级前做好数据备份工作，避免出现意外。

## 参考链接

* https://openjdk.org/groups/vulnerability/advisories/2026-11-17
* https://www.oracle.com/security-alerts/cspunov2026.html
* https://cloud.tencent.com/announce/detail/2581

END

更多精彩内容点击下方扫码关注哦~

关注云鼎实验室，获取更多安全情报

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NNSr7XSrt0miaxYvNtxDpUF6cHu3RxDXicIEQ8f8tephDpMFS0sczGA1vwwZKyT2sEjgwh1D5yxVxLRoalY8x2ZA/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过