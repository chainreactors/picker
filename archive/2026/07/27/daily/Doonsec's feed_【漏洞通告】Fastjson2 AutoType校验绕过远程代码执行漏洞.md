---
title: 【漏洞通告】Fastjson2 AutoType校验绕过远程代码执行漏洞
url: https://mp.weixin.qq.com/s/K9tzMuWWhMA_2Ls9JF4qIg
source: Doonsec's feed
date: 2026-07-27
fetch_date: 2026-07-28T04:54:38.963000
---

# 【漏洞通告】Fastjson2 AutoType校验绕过远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4S21m309ZryXJ56Z346LSMTo3L4ibAhsVxuRXvmSEf1fBQQcmbwQwbFQdfR3ovKDHgKicicuviaNuicfibHz8emviawSgj9AqLluicN3UzicXuQNAwWg/0?wx_fmt=jpeg)

# 【漏洞通告】Fastjson2 AutoType校验绕过远程代码执行漏洞

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## **一****、漏洞概述**

|  |  |  |  |
| --- | --- | --- | --- |
| 漏洞名称 | Fastjson2 AutoType校验绕过远程代码执行漏洞 | | |
| CVE   ID | 暂无 | | |
| 漏洞类型 | RCE | 发现时间 | 2026-7-27 |
| 漏洞评分 | 9.8 | 漏洞等级 | 严重 |
| 攻击向量 | 网络 | 所需权限 | 无 |
| 利用难度 | 低 | 用户交互 | 不需要 |
| PoC/EXP | 未公开 | 在野利用 | 未发现 |

Fastjson2是阿里巴巴开源的高性能Java JSON解析库，是Fastjson系列的重构升级版本，提供JSON序列化、反序列化以及丰富的数据处理能力。该组件广泛应用于Java企业应用、微服务系统、接口服务、数据交换平台等场景，具有高性能、低延迟和易集成等特点。

2026年7月27日，启明星辰安全应急响应中心（VSRC）监测到Fastjson2 AutoType校验绕过远程代码执行漏洞。该漏洞存在于Fastjson2的AutoType类型解析流程中，由于默认配置下AutoType校验逻辑对输入类型名称进行FNV-1a哈希匹配时，仅验证哈希结果而未充分校验实际类型名称，攻击者可构造特殊JSON数据绕过类型白名单限制，使恶意类型进入类加载流程并执行任意代码。攻击者无需认证即可通过控制JSON请求触发漏洞，可能导致服务器被完全控制、敏感数据泄露、业务系统被入侵，并对企业数据安全及合规要求造成严重影响。

## **二、影响范围**

Fastjson2 <= 2.0.62（根据互联网公开信息）。

## **三****、****安全****措施**

### **3.1 升级版本**

PR #7695并非正式修复提交，已关闭且未合并至主干，当前已发布版本均不包含修复。建议持续关注官方安全公告，待正式修复版本发布后及时升级。

下载链接：

https://github.com/alibaba/fastjson2/

### **3.2****临时****措施**

在官方修复版本发布前，建议开启SafeMode禁用AutoType功能（-Dfastjson2.parser.safeMode=true），阻止不可信类型自动解析；同时避免对外部输入的JSON数据进行直接反序列化，对包含@type字段的请求进行过滤，并通过WAF、API网关等安全设备拦截异常JSON请求，以降低漏洞被利用风险。

### **3.3 通用建议**

* 定期更新系统补丁，减少系统漏洞，提升服务器的安全性。
* 加强系统和网络的访问控制，修改防火墙策略，关闭非必要的应用端口或服务，减少将危险服务（如SSH、RDP等）暴露到公网，减少攻击面。
* 使用企业级安全产品，提升企业的网络安全性能。
* 加强系统用户和权限管理，启用多因素认证机制和最小权限原则，用户和软件权限应保持在最低限度。
* 启用强密码策略并设置为定期修改。

### **3.****4****参考链接**

https://github.com/alibaba/fastjson2/pull/7695

https://github.com/alibaba/fastjson2/issues/7702

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

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