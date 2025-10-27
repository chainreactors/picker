---
title: ThreatHound - Tool That Help You On Your IR & Threat Hunting And CA
url: https://buaq.net/go-150059.html
source: unSafe.sh - 不安全
date: 2023-02-20
fetch_date: 2025-10-04T07:32:07.409615
---

# ThreatHound - Tool That Help You On Your IR & Threat Hunting And CA

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

![](https://8aqnet.cdn.bcebos.com/1df7d5fbb5d4c7dff5f0fb97de7b7b54.jpg)

ThreatHound - Tool That Help You On Your IR & Threat Hunting And CA

This tool will help you on your IR & Threat Hunting & CA. just drop your event log file and
*2023-2-19 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-150059.htm)
阅读量:51
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh0PbkortrdU7llq_qjZXzvDZb6FMFu3NA-W-hEl1YtnzuKUCdaBAWlb8NJ2eQ6DVeunsSxch1C96BAQF8qEBVpQgdqobOCqvINJlxDrR98qVMGttqPAo5HOQINsLYtxalztsqKN3Y-u5-x8hZSYTvTd92ndp3vWhAjSmZLsf4W1qwzuDs-uw4RNi4iOw=w640-h217)](https://blogger.googleusercontent.com/img/a/AVvXsEh0PbkortrdU7llq_qjZXzvDZb6FMFu3NA-W-hEl1YtnzuKUCdaBAWlb8NJ2eQ6DVeunsSxch1C96BAQF8qEBVpQgdqobOCqvINJlxDrR98qVMGttqPAo5HOQINsLYtxalztsqKN3Y-u5-x8hZSYTvTd92ndp3vWhAjSmZLsf4W1qwzuDs-uw4RNi4iOw)

This tool will help you on your IR & [Threat Hunting](https://www.kitploit.com/search/label/Threat%20Hunting "Threat Hunting") & CA. just drop your event log file and anlayze the results.

* support windows (ThreatHound.exe)
* C for Linux based
* new vesion available in C also
* now you can save results in json file or print on screen it as you want by arg 'print' "'yes' to print the results on screen and 'no' to save the results on json file"
* you can give [windows event logs](https://www.kitploit.com/search/label/Windows%20Event%20Logs "windows event logs") folder or single evtx file or multiple evtx separated by comma by arg -p
* you can now give sigam ruels path by arg -s
* add [multithreading](https://www.kitploit.com/search/label/Multithreading "multithreading") to improve runing speed
* ThreatHound.exe is agent based you can push it and run it on multiple servers

* Example:

```
$ ThreatHound.exe -s ..\sigma_rules\ -p C:\Windows\System32\winevt\Logs\ -print no
```

* NOTE: give cmd full promission to read from "C:\Windows\System32\winevt\Logs"
* Linux Based: [![](https://blogger.googleusercontent.com/img/a/AVvXsEh_Wg59jIYaykBbOR5aDJRqLDNQrgGtM1vFswqwyxHps1q_S-HR6NbqqRJ0oufQZwzhjHT8t_6rogyfEBYIbiYdIpHSotR013qsZ0xIaLsPhFn_-Ay3DZrMe4x3PdcU_3zQ-j9njLDmErRsC2dYwyyhS9S_MHv2xprAb7ml5M482dW8n6eIcYc2Ro1SFQ=w640-h98)](https://blogger.googleusercontent.com/img/a/AVvXsEh_Wg59jIYaykBbOR5aDJRqLDNQrgGtM1vFswqwyxHps1q_S-HR6NbqqRJ0oufQZwzhjHT8t_6rogyfEBYIbiYdIpHSotR013qsZ0xIaLsPhFn_-Ay3DZrMe4x3PdcU_3zQ-j9njLDmErRsC2dYwyyhS9S_MHv2xprAb7ml5M482dW8n6eIcYc2Ro1SFQ)
* Windows Based [![](https://blogger.googleusercontent.com/img/a/AVvXsEjNSlJZwKM3CW8bRYDolFZWDlKyG5PI77KKyAHIvNtMW0tgYwPBlHoZXVI1MUhLEvy-4tRr-FCET_mMDyKVb69vgJ8vg5lCTb_pj1kA37TN0BcoxIVUfwGv5vCttuVLWk4zTUdhPhpMIWWx3lSp1Twxl9SN3sRG0EI-PIvGE9z-_nvhtRTZvNYQhWSpbw=w640-h138)](https://blogger.googleusercontent.com/img/a/AVvXsEjNSlJZwKM3CW8bRYDolFZWDlKyG5PI77KKyAHIvNtMW0tgYwPBlHoZXVI1MUhLEvy-4tRr-FCET_mMDyKVb69vgJ8vg5lCTb_pj1kA37TN0BcoxIVUfwGv5vCttuVLWk4zTUdhPhpMIWWx3lSp1Twxl9SN3sRG0EI-PIvGE9z-_nvhtRTZvNYQhWSpbw)

* A dedicated backend to support Sigma rules for python
* A dedicated backend for parsing evtx for python
* A dedicated backend to match between evtx and the Sigma rules

* Automation for Threat hunting, Compromise Assessment, and [Incident Response](https://www.kitploit.com/search/label/Incident%20Response "Incident Response") for the Windows Event Logs
* Downloading and updating the Sigma rules daily from the source
* More then 50 detection rules included
* support for more then 1500 detection rules for Sigma
* Support for new sigma rules dynamically and adding it to the detection rules
* Saving of all the outputs in JSON format
* Easily add any detection rules you prefer
* you can add new event log source type in mapping.py easily

* Support for Sigma rules dedicated for DNS query
* Modifying the speed of algorithm dedicated for the detection and making it faster
* Adding JSON output that supports Splunk
* More features

```
$ git clone https://github.com/MazX0p/ThreatHound.git
```

* Note: glob doesn't support get path of the [directory](https://www.kitploit.com/search/label/Directory "directory") if it has spaces on folder names, please ensure the path of the tool is without spaces (folders names)

[https://player.vimeo.com/video/784137549?h=6a0e7ea68a&amp;badge=0&amp;autopause=0&amp;player\_id=0&amp;app\_id=58479](https://player.vimeo.com/video/784137549?h=6a0e7ea68a&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479 "https://player.vimeo.com/video/784137549?h=6a0e7ea68a&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479")

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjvI_aAt6BSSsAYvBb7EDHki_iAgm7vqJGUaogV7bVNlTbTVsg_Z4t1_WvPdOvVFBcijVEeBCaemdMSiMG7kFO2498YnGVu7K3Gb2xmu2eYuaVH0EAiz1-4wIJOi89e7IO24vU3L9ZrD5xM6IiRzS-N6_k8HkiomkOAWRDy1z-mHKTyJ8SZPav23JBLnQ=w640-h482)](https://blogger.googleusercontent.com/img/a/AVvXsEjvI_aAt6BSSsAYvBb7EDHki_iAgm7vqJGUaogV7bVNlTbTVsg_Z4t1_WvPdOvVFBcijVEeBCaemdMSiMG7kFO2498YnGVu7K3Gb2xmu2eYuaVH0EAiz1-4wIJOi89e7IO24vU3L9ZrD5xM6IiRzS-N6_k8HkiomkOAWRDy1z-mHKTyJ8SZPav23JBLnQ)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgIZzBq_6KK6ZrZMxrR8RJ9hN4ud7jYdJywEL734oR0PrEjrOPomNVmCYmPgtEv3AIEEobeJ0BTrV-AAd1aWIFO8aj8L-1ROXeIvRK1Dnmnv8qcf3kWrJi1BJqWjzy-5YV2r0nC297sX5YFOEniPzg0yVbcsLAE-c5N-Q0gnniQA_yujC5G9H3g0CxBPg=w640-h480)](https://blogger.googleusercontent.com/img/a/AVvXsEgIZzBq_6KK6ZrZMxrR8RJ9hN4ud7jYdJywEL734oR0PrEjrOPomNVmCYmPgtEv3AIEEobeJ0BTrV-AAd1aWIFO8aj8L-1ROXeIvRK1Dnmnv8qcf3kWrJi1BJqWjzy-5YV2r0nC297sX5YFOEniPzg0yVbcsLAE-c5N-Q0gnniQA_yujC5G9H3g0CxBPg)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhvpB6YqPriMy6eD8xY8K0an7JwCk3lDggVmNUHR1WN_AImtxHqKhB-OFYwtKYt0hsfmsXEe4chQUek-_iltO0120Tzu1GqqrDkqUco2U3eG-oBQYPNCEmu4w2SogK685_2wEFbalG0t6zQJb2cy6r_SSRXHFwq--pdClEIEkfw_8eCme6jwImcZJL1eA=w640-h342)](https://blogger.googleusercontent.com/img/a/AVvXsEhvpB6YqPriMy6eD8xY8K0an7JwCk3lDggVmNUHR1WN_AImtxHqKhB-OFYwtKYt0hsfmsXEe4chQUek-_iltO0120Tzu1GqqrDkqUco2U3eG-oBQYPNCEmu4w2SogK685_2wEFbalG0t6zQJb2cy6r_SSRXHFwq--pdClEIEkfw_8eCme6jwImcZJL1eA)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgtmwo9R2QbvBlRc0Ay9vKbpnnef9P8oTYu6kE53puMc_mx7MCxGx3o53cvS9fM-EZ5IRnfBqahpbvIH4NxabpAh7xxt3SqWqPiKcb5wQqyvpf7uWNTUok5NlJ1Ht77zsaMH9MFtTSykvwKjSZ3HVv3hdU0bYzLx1BPOUP2UbcN_CymL7LwLxG0LCbI_Q=w640-h402)](https://blogger.googleusercontent.com/img/a/AVvXsEgtmwo9R2QbvBlRc0Ay9vKbpnnef9P8oTYu6kE53puMc_mx7MCxGx3o53cvS9fM-EZ5IRnfBqahpbvIH4NxabpAh7xxt3SqWqPiKcb5wQqyvpf7uWNTUok5NlJ1Ht77zsaMH9MFtTSykvwKjSZ3HVv3hdU0bYzLx1BPOUP2UbcN_CymL7LwLxG0LCbI_Q)

ThreatHound - Tool That Help You On Your IR & Threat Hunting And CA
![ThreatHound - Tool That Help You On Your IR & Threat Hunting And CA](https://blogger.googleusercontent.com/img/a/AVvXsEh0PbkortrdU7llq_qjZXzvDZb6FMFu3NA-W-hEl1YtnzuKUCdaBAWlb8NJ2eQ6DVeunsSxch1C96BAQF8qEBVpQgdqobOCqvINJlxDrR98qVMGttqPAo5HOQINsLYtxalztsqKN3Y-u5-x8hZSYTvTd92ndp3vWhAjSmZLsf4W1qwzuDs-uw4RNi4iOw=s72-w640-c-h217)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/02/threathound-tool-that-help-you-on-your.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)