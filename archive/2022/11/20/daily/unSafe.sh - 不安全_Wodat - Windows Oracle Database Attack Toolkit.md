---
title: Wodat - Windows Oracle Database Attack Toolkit
url: https://buaq.net/go-136387.html
source: unSafe.sh - 不安全
date: 2022-11-20
fetch_date: 2025-10-03T23:16:29.425376
---

# Wodat - Windows Oracle Database Attack Toolkit

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

![](https://8aqnet.cdn.bcebos.com/b33f807588096f6be4af5280937b3af8.jpg)

Wodat - Windows Oracle Database Attack Toolkit

Simple port of the popular Oracle Database Attack Tool (ODAT) (https://github.com/quentinhar
*2022-11-19 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-136387.htm)
阅读量:38
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjWBsK1FDSGn29qobntdhLkUloSryP8erp2XFXgrlfw_84qfz1V6L0KVQM0fNDmXwW_WbgKFs_WBatpPUg7Rw98tb5shHXlJDPN8Gi912Y0Qutes-XeR2_ZT-zOtl1EAwExW6R48oajvOpmImcN07WYpBin1IrSTJJHIpgnZFir3vQgIr0oDUGF4dR6VQ=w640-h258)](https://blogger.googleusercontent.com/img/a/AVvXsEjWBsK1FDSGn29qobntdhLkUloSryP8erp2XFXgrlfw_84qfz1V6L0KVQM0fNDmXwW_WbgKFs_WBatpPUg7Rw98tb5shHXlJDPN8Gi912Y0Qutes-XeR2_ZT-zOtl1EAwExW6R48oajvOpmImcN07WYpBin1IrSTJJHIpgnZFir3vQgIr0oDUGF4dR6VQ)

Simple port of the popular Oracle Database Attack Tool (ODAT) ([https://github.com/quentinhardy/odat](https://github.com/quentinhardy/odat "https://github.com/quentinhardy/odat")) to C# .Net Framework. Credit to [https://github.com/quentinhardy/odat](https://github.com/quentinhardy/odat "https://github.com/quentinhardy/odat") as lots of the functionality are ported from his code.

* Perform password based attacks e.g. username as password, username list against given password, password list against given username, username:pass combolist.
* Test if a credential/connection string is working against target
* Brute force attacks to discover valid SID/ServiceNames
* Perform discovery of valid TNS listeners against provided target file or CIDR range
* More to come, I hope!

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh-qUtg6hZiRmXhSuPE0j6sRLfBD_7vxQ2am_Otpvp1Bc7sFSfEO786ScAr4pc4VDifWpfnO4_uL478IERFg5e99m5Bz8fsK_JwVY-iZ8J_UJttjtu4lGBr7RcbdOR-TlZ6KAurEZLypdqhcTEDzf9i2wKtBmYPytnQWr2iNxraVIwnjiqPN_n4nzEJqg=w640-h152)](https://blogger.googleusercontent.com/img/a/AVvXsEh-qUtg6hZiRmXhSuPE0j6sRLfBD_7vxQ2am_Otpvp1Bc7sFSfEO786ScAr4pc4VDifWpfnO4_uL478IERFg5e99m5Bz8fsK_JwVY-iZ8J_UJttjtu4lGBr7RcbdOR-TlZ6KAurEZLypdqhcTEDzf9i2wKtBmYPytnQWr2iNxraVIwnjiqPN_n4nzEJqg)

## Disclaimer

I take not responsibility for your use of the software. Development is done in my personal capacity and carry no affiliation to my work.

## Usage

The general [command line](https://www.kitploit.com/search/label/Command%20Line "command line") arguments required are as follow:

```
wodat.exe COMMAND ARGGUMENTS
```

To test if a specific credential set works.

```
wodat.exe TEST -server:XXX.XXX.XXX.XXX -port:1521 -sid:XE -user:peter -pass:pan
```

See the outline on modules for further usage. The tool will always first check if the TNS listener that is targeted works.

## Modules

#### BRUTESID

Module performs wordlist SID guessing attack if not successful will ask for [brute force](https://www.kitploit.com/search/label/Brute%20Force "brute force") attack.

```
wodat.exe BRUTESID -server:XXX.XXX.XXX.XXX -port:1521
```

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg43eKBomV61NkSoKLktOxPw-FAxLyu9hU6Th9wc-jWKg3S5w-opvRqyrn36cDFIhFgVopj1WraymEUDM8kTLRmZUhwq_qSq0YbUbNr4YNVtJ9IyRY6Mxej_V9EuAsYqi50tdI1AuMXW9mzwmbW6teTfqgAy61N-97FujyIlVQjkawqGk5E1bGLHpnkjw=w640-h208)](https://blogger.googleusercontent.com/img/a/AVvXsEg43eKBomV61NkSoKLktOxPw-FAxLyu9hU6Th9wc-jWKg3S5w-opvRqyrn36cDFIhFgVopj1WraymEUDM8kTLRmZUhwq_qSq0YbUbNr4YNVtJ9IyRY6Mxej_V9EuAsYqi50tdI1AuMXW9mzwmbW6teTfqgAy61N-97FujyIlVQjkawqGk5E1bGLHpnkjw)

#### BRUTESRV

Module performs wordlist ServiceName guessing attack if not successful will ask for brute force attack.

```
wodat.exe BRUTESRV -server:XXX.XXX.XXX.XXX -port:1521
```

#### BRUTECRED

Module performs wordlist password based attack. The following options exist:

```
A - username:password combolist with no credentials given during arguments
B - username list with password given in arguments
C - password list with username given in arguments
D - username as password with username list provided
```

To perform a basic attack with a given file that has username:password combos.

```
wodat.exe BRUTECRED -server:XXX.XXX.XXX.XXX -port:1521 -sid:XE
```

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjWBsK1FDSGn29qobntdhLkUloSryP8erp2XFXgrlfw_84qfz1V6L0KVQM0fNDmXwW_WbgKFs_WBatpPUg7Rw98tb5shHXlJDPN8Gi912Y0Qutes-XeR2_ZT-zOtl1EAwExW6R48oajvOpmImcN07WYpBin1IrSTJJHIpgnZFir3vQgIr0oDUGF4dR6VQ=w640-h258)](https://blogger.googleusercontent.com/img/a/AVvXsEjWBsK1FDSGn29qobntdhLkUloSryP8erp2XFXgrlfw_84qfz1V6L0KVQM0fNDmXwW_WbgKFs_WBatpPUg7Rw98tb5shHXlJDPN8Gi912Y0Qutes-XeR2_ZT-zOtl1EAwExW6R48oajvOpmImcN07WYpBin1IrSTJJHIpgnZFir3vQgIr0oDUGF4dR6VQ)

#### TEST

Module tests if the given connection string can connect successfully.

```
wodat.exe TEST -server:XXX.XXX.XXX.XXX -port:1521 -sid:XE -user:peter -pass:pan
```

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgrvq_YFeSUaJVxtQ18Ydc40rKS7b1A376N6TX_P_o7E6NtVAQ-xOnfjXd8Gzf-AiqP3a619c70KXkyhH45s_6kyEUH0FoimCp5PwF31Woc_UYbL9n1IlhwHAWPuW2q6RxsxMdAe_GIwL_RAyQPTks_L22d1DSbVOKz9vwnQRlu_YseLS_zkLMlCWycrA=w640-h114)](https://blogger.googleusercontent.com/img/a/AVvXsEgrvq_YFeSUaJVxtQ18Ydc40rKS7b1A376N6TX_P_o7E6NtVAQ-xOnfjXd8Gzf-AiqP3a619c70KXkyhH45s_6kyEUH0FoimCp5PwF31Woc_UYbL9n1IlhwHAWPuW2q6RxsxMdAe_GIwL_RAyQPTks_L22d1DSbVOKz9vwnQRlu_YseLS_zkLMlCWycrA)

#### DISC

Module will perform discovery against provided CIDR range or file with instances. Note, only instances with valid TNS listeners will be returned. Testing a network range will be much faster as it’s processed in parallel.

Instances to test must be formatted as per the below example `targets.txt`:

```
192.168.10.1
192.168.10.5,1521
```

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjmyUvncpVe6yvmUyfpjnniv7ikgyM6R_7z-p9lZlvZZP1QCo91QEmdFxwrk0bYG5tykcsrHxbL2Gv4yWgZGsTGDohlgogZf3nSJ_aLkH4kpw_Zg4XOfvCAidRoJjU74hkFfcN-qy5Wi81AlgXBtprsWJeSkTY79ts77Oq94E_hMcz6X7QV-ZbRRkk3xQ=w640-h164)](https://blogger.googleusercontent.com/img/a/AVvXsEjmyUvncpVe6yvmUyfpjnniv7ikgyM6R_7z-p9lZlvZZP1QCo91QEmdFxwrk0bYG5tykcsrHxbL2Gv4yWgZGsTGDohlgogZf3nSJ_aLkH4kpw_Zg4XOfvCAidRoJjU74hkFfcN-qy5Wi81AlgXBtprsWJeSkTY79ts77Oq94E_hMcz6X7QV-ZbRRkk3xQ)

### ALL

Not implemented yet.

#### RECON

Not implemented yet.

## Setup and Requirements

You can grab [automated](https://www.kitploit.com/search/label/Automated "automated") release build from the GitHub Actions or build yourself using the following commands:

```
nuget restore wodat.sln
msbuild wodat.sln -t:rebuild -property:Configuration=Release
```

Some general notes: The `Oracle.ManagedDataAccess.dll` library will have to be copied with the binary. I'm looking at ways of embedding it.

## Todo

* Handle SYSDBA and SYSOPER connections
* Implement outstanding modules
* Various validation, error handling code still needs to be done
* Some minor known bugfixes
* Add options to check against built in lists for SID, ServiceNames or common credentials

Wodat - Windows Oracle Database Attack Toolkit
![Wodat - Windows Oracle Database Attack Toolkit](https://blogger.googleusercontent.com/img/a/AVvXsEjWBsK1FDSGn29qobntdhLkUloSryP8erp2XFXgrlfw_84qfz1V6L0KVQM0fNDmXwW_WbgKFs_WBatpPUg7Rw98tb5shHXlJDPN8Gi912Y0Qutes-XeR2_ZT-zOtl1EAwExW6R48oajvOpmImcN07WYpBin1IrSTJJHIpgnZFir3vQgIr0oDUGF4dR6VQ=s72-w640-c-h258)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/11/wodat-windows-oracle-database-attack.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)