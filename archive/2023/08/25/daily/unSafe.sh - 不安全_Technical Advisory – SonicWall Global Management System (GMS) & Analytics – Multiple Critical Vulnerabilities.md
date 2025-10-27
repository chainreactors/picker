---
title: Technical Advisory – SonicWall Global Management System (GMS) & Analytics – Multiple Critical Vulnerabilities
url: https://buaq.net/go-175312.html
source: unSafe.sh - 不安全
date: 2023-08-25
fetch_date: 2025-10-04T11:59:32.384195
---

# Technical Advisory – SonicWall Global Management System (GMS) & Analytics – Multiple Critical Vulnerabilities

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

![]()

Technical Advisory – SonicWall Global Management System (GMS) & Analytics – Multiple Critical Vulnerabilities

Multiple Unauthenticated SQL Injection Issues Security Filter Bypass – CV
*2023-8-24 21:8:34
Author: [research.nccgroup.com(查看原文)](/jump-175312.htm)
阅读量:68
收藏*

---

## Multiple Unauthenticated SQL Injection Issues Security Filter Bypass – CVE-2023-34133

```
Title: Multiple Unauthenticated SQL Injection Issues   Security Filter Bypass
Risk: 9.8 (Critical) - CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N
Versions Affected: GMS Virtual Appliance 9.3.2-SP1 and earlier, GMS Windows 9.3.2-SP1 and earlier, Analytics 2.5.0.4-R7 and earlier
CVE Identifier: CVE-2023-34133
Authors: Richard Warren <richard.warren[at]nccgroup.com>, Sean Morland <sean.morland[at]nccgroup.com>
```

### Description

The GMS web application was found to be vulnerable to numerous SQL injection issues. Additionally, security mechanisms that were in place to help prevent against SQL Injection attacks could be bypassed.

### Impact

An unauthenticated attacker could exploit these issues to extract sensitive information, such as credentials, reset user passwords, bypass authentication, and compromise the underlying device.

## Web Service Authentication Bypass – CVE-2023-34124

```
Title: Web Service Authentication Bypass
Risk: 9.4 (Critical) - CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:H
Versions Affected: GMS Virtual Appliance 9.3.2-SP1 and earlier, GMS Windows 9.3.2-SP1 and earlier, Analytics 2.5.0.4-R7 and earlier
CVE Identifier: CVE-2023-34124
Authors: Richard Warren <richard.warren[at]nccgroup.com>, Sean Morland <sean.morland[at]nccgroup.com>
```

### Description

The authentication mechanism used by the Web Services application did not adequately perform authentication checks, as no secret information was required to perform authentication.

The authentication mechanism employed by the GMS /ws application used a non-secret value when performing HTTP digest authentication. An attacker could easily supply this information, allowing them to gain unauthorised access to the application and call arbitrary Web Service methods.

### Impact

An attacker with knowledge of authentication mechanism would be able to generate valid authentication codes for the GMS Web Services application, and subsequently call arbitrary methods. A number of these Web Service methods were found to be vulnerable to additional issues, such as arbitrary file read and write (see CVE-2023-34135, CVE-2023-34129 and CVE-2023-34134). Therefore, this issue could lead to the complete compromise of the host.

## Predictable Password Reset Key – CVE-2023-34123

```
Title: Password Hash Read via Web Service
Risk: 7.5 (High) - CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
Versions Affected: GMS Virtual Appliance 9.3.2-SP1 and earlier, GMS Windows 9.3.2-SP1 and earlier, Analytics 2.5.0.4-R7 and earlier
CVE Identifier: CVE-2023-34123
Authors: Richard Warren <richard.warren[at]nccgroup.com>, Sean Morland <sean.morland[at]nccgroup.com>
```

### Description

The GMS `/appliance` application uses a hardcoded key value to generate password reset keys. This hardcoded value does not change between installs. Furthermore, additional information used during password reset code calculation is non-secret and can be discovered from an unauthenticated perspective.

An attacker with knowledge of this information could generate their own password reset key to reset the administrator account password. Note that this issue is only exploitable in certain configurations. Specifically, if the device is registered, or if it is configured in “Closed Network” mode.

### Impact

An attacker with knowledge of the hardcoded 3DES key used to validate password reset codes could generate their own password reset code to gain unauthorised, administrative access to the appliance. An attacker with unauthorised, administrative access to the appliance could exploit additional post-authentication vulnerabilities to achieve Remote Code Execution on the underlying device. Additionally, they could gain access to other devices managed by the GMS appliance.

## CAS Authentication Bypass – CVE-2023-34137

```
Title: CAS Authentication Bypass
Risk: 9.4 (Critical) - CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:H
Versions Affected: GMS Virtual Appliance 9.3.2-SP1 and earlier, GMS Windows 9.3.2-SP1 and earlier, Analytics 2.5.0.4-R7 and earlier
CVE Identifier: CVE-2023-34137
Authors: Richard Warren <richard.warren[at]nccgroup.com>, Sean Morland <sean.morland[at]nccgroup.com>
```

### Description

The authentication mechanism used by the CAS Web Service (exposed via /ws/cas) did not adequately perform authentication checks, as it used a hardcoded secret value to perform cryptographic authentication checks. The CAS Web Service validated authentication tokens by calculating the HMAC SHA-1 of the supplied username. However, the HMAC secret was static. As such, an attacker could calculate their own authentication tokens, allowing them to gain unauthorised access to the CAS Web Service.

### Impact

An attacker with access to the application source code (for example, by downloading a trial VM), could discover the static value used for calculating HMACs – allowing them to generate their own authentication tokens. An attacker with the ability to generate their own authentication tokens would be able to make legitimate use of the CAS API, as well as exploit further vulnerabilities within this API; for example, SQL Injection – resulting in complete compromise of the underlying host.

## Post-Authenticated Command Injection – CVE-2023-34127

```
Title: Post-Authenticated Command Injection
Risk: 8.8 (High) - CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
Versions Affected: GMS Virtual Appliance 9.3.2-SP1 and earlier, GMS Windows 9.3.2-SP1 and earlier, Analytics 2.5.0.4-R7 and earlier
CVE Identifier: CVE-2023-34127
Authors: Richard Warren <richard.warren[at]nccgroup.com>, Sean Morland <sean.morland[at]nccgroup.com>
```

### Description

The GMS application was found to lack sanitization of user-supplied parameters when allowing users to search for log files on the system. This could allow an authenticated attacker to execute arbitrary code with root privileges.

### Impact

An authenticated, administrative user can execute code as root on the underlying file system. For example, they could use this vulnerability to write a malicious cron job, web-shell, or stage a remote C2 payload. Note that whilst on its own this issue requires authentication, there were other issues identified (such as CVE-2023-34123) that could be chained with this vulnerability to exploit it from an initially unauthenticated perspective.

## Password Hash Read via Web Service – CVE-2023-34134

```
Title: Password Hash Read via Web Service
Risk: 9.8 (Critical) - CVSS:3.0/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
Versions Affected: GMS Virtual Appliance 9.3.2-SP1 and earlier, GMS Windows 9.3.2-SP1 and earlier, Analytics 2.5.0.4-R7 and earlier
CVE Identifier: CVE-2023-34134
Authors: Richard Warren <richard.warren[at]nccgroup.com>, Sean Morland <sean.morland[at]nccgroup.com>
```

### Description

An authenticated attacker can read the administrator password hash via a web service call.

Note that whilst this issue requires authentication, it can be chained with an authentication bypass to exploit the issue from an unauthenticated perspective.

### Impact

This issue can be chained with CVE-2023-34124 to read the administrator password hash from an unauthenticated perspective. Following this, an attacker could launch further post-authentication attackers to achieve Re...