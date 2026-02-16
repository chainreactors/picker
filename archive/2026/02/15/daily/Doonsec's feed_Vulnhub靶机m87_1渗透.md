---
title: Vulnhub靶机m87_1渗透
url: https://mp.weixin.qq.com/s/Bl0ATG8xJeeraOCN_9hQYA
source: Doonsec's feed
date: 2026-02-15
fetch_date: 2026-02-16T04:17:35.336780
---

# Vulnhub靶机m87_1渗透

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DC4TgvRKhOsicrq3gOXmADXNu57CqBQy52JoDiaib4mfPdseA1LtIvTF3ZIPDJhb0mSkfurQWQFWVIGQ6NshMUZ0ZxODtoUZCIbJKozyNIWt70/0?wx_fmt=jpeg)

# Vulnhub靶机m87\_1渗透

OnePanda-Sec

![]()

在小说阅读器中沉浸阅读

**OnePanda-Sec**

**Vulnhub靶机m87\_1渗透**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOuQ12PViaoiaVzMc4rrgyia8xzaP6fzvuvUevKibz8iamicHNm1aRVwWGm8gVbx6FsusrmDhG3icEK1AwqSlCGPwo9LwgrmrtJcNQxtRA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5yFQc47iaibSTKkw5drTicRicCJicBHDXWVibVOVHqZdjOwzPZeUsoItiaiaUMaLpNuibH3w4F7824liaVPMvKd3ic2f8PzzLf6chmvDrjmykabMsfiaF6XA/640?wx_fmt=svg&from=appmsg)

2026

**招新要求**

热爱网络安全，喜欢CTF

拥有CTF比赛经验，有较好比赛成绩的

乐于奉献、热爱分享，愿意提升自己同时帮助他人时间允许参加各类赛事，服从战队管理与安排·各类比赛获奖者、能力出众者视情况考量·未参与其他高校联队

大一同学视情况放宽资历要求

**联系方式**

发送简历于邮箱

·简历邮箱：2638726415@qq.com

![](https://mmbiz.qpic.cn/mmbiz_gif/DC4TgvRKhOsTtdF26WuGSgxLk3DI8ZqR14MoyZT1gw3Xalhk40h7wTDGbsHzq6rcgPORR2rmOCl0x84q8yJ78v8l8TD4f2aPe6jIA15bJrA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOuKavS6XX9X8BVNlH9fEGbmNiaFx3Lt7eTOO5vU3Zgh1w67KxqEKom2ULNudl5kYffM2e2mJftf2DzqMtibwcmjjdpJDoUZeCxicQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4kEX0KsFiaCdVHnTOgaeANw8vMuusQZZKjArbxB3e5AltayskwY3ZMxCBYDk1dm6ehEhanPbiaQxlIuGVSLPW8JtAJ1JSYs8LgLm4Jk2uQYMicg/640?wx_fmt=svg&from=appmsg)

**招新说明**

实验环境

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOtXVUcCc8Z9kwBNlEiathc16yJZV1l228OsNYY6m0ibeMWib7tJHqn0dbdh5E5qcG961E7fwhic3jGFkFiaKYG72ibsoICQvJM8xVvAQ/640?wx_fmt=png&from=appmsg)

信息收集

arp扫描

通过arp进行网络扫描，得到vmware,inc虚拟机名称的主机ip为<192.168.10.26>

```
┌──(root㉿Luistin)-[~]└─# arp-scan -lInterface: eth0, type: EN10MB, MAC: 00:0c:29:97:4a:77, IPv4: 192.168.10.141Starting arp-scan 1.10.0 with 256 hosts (https://github.com/royhills/arp-scan)192.168.10.1    9c:47:82:cd:76:ff       (Unknown)192.168.10.2    9c:47:82:9b:05:5a       (Unknown)192.168.10.3    9c:47:82:9b:14:c9       (Unknown)192.168.10.4    9c:47:82:c3:b5:48       (Unknown)192.168.10.20   48:e7:da:f6:21:1d       AzureWave Technology Inc.192.168.10.26   00:0c:29:7e:44:f3       VMware, Inc.192.168.10.24   7e:04:54:cf:f5:9c       (Unknown: locally administered)192.168.10.7    e6:f6:75:6f:6f:95       (Unknown: locally administered)192.168.10.11   f4:6a:dd:7a:0d:eb       Liteon Technology Corporation192.168.10.10   f4:26:79:75:76:96       Intel Corporate192.168.10.17   3c:55:76:dd:01:43       CLOUD NETWORK TECHNOLOGY SINGAPORE PTE. LTD.192.168.10.8    82:b5:4f:41:85:1a       (Unknown: locally administered)192.168.10.16   66:19:92:c3:3e:dd       (Unknown: locally administered)192.168.10.28   3c:55:76:dd:01:43       CLOUD NETWORK TECHNOLOGY SINGAPORE PTE. LTD.192.168.10.57   3c:55:76:dd:01:43       CLOUD NETWORK TECHNOLOGY SINGAPORE PTE. LTD.192.168.10.13   6a:03:77:68:98:5d       (Unknown: locally administered)18 packets received by filter, 0 packets dropped by kernelEnding arp-scan 1.10.0: 256 hosts scanned in 1.991 seconds (128.58 hosts/sec). 16 responded
```

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOsBg5jgwQZ8yOVOgzwQ8XHv5I5RRyE08zSIFgcIsDe0O0tC5hVAJiby8amyAJjhXo5JC2ZaspXViaiadl9m3HJJJ4PPKF5BHMNBwo/640?wx_fmt=png&from=appmsg)

无影扫描结果

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ID | Host | Port | Protocol | Target | Banner |
| 1 | 192.168.10.26 | 143 | IMAP | 192.168.10.26:143 | UnKnown |
| 2 | 192.168.10.26 | 80 | HTTP | http://192.168.10.26:80 | Apache/2.4.38 (Debian),Apache-HTTP-Server/2.4.38,CentOS-WebPanel,Telos-Alliance-Omnia-MPX-Node,Redash-Setup-Configuration,jQuery,Apache-Web-Server |
| 3 | 192.168.10.2 | 9090 | HTTP | http://192.168.10.26:9090 | Apache-Struts2 |

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOuxicBQ6luRnUCZ0sVo4iagToTjNjyNSOPlb2sl12LicL4XQzPm7AmYdIFQybvhWpBqmp1qZCTFDdAjIzM93aV7ylXtoHlV1HEag0/640?wx_fmt=png&from=appmsg)

fscan扫描结果

```
D:\Tools\Sec\Web\Cobalt_Strike_4.7\plugin\OLa\scripts\Intranet_scan\fscan\x64>fscan.exe -h 192.168.10.26___                              _/ _ \     ___  ___ _ __ __ _  ___| | __/ /_\/____/ __|/ __| '__/ _` |/ __| |/ // /_\\_____\__ \ (__| | | (_| | (__|   <\____/     |___/\___|_|  \__,_|\___|_|\_\fscan version: 1.8.1start infoscan(icmp) Target 192.168.10.26   is alive[*] Icmp alive hosts len is: 1192.168.10.26:80 open192.168.10.26:9090 open[*] alive ports len is: 2start vulscan[*] WebTitle:http://192.168.10.26      code:200 len:1322   title:M87 Login Form[*] WebTitle:https://192.168.10.26:9090 code:200 len:46690  title:Loading...2026/02/11 10:31:46 Unsolicited response received on idle HTTP channel starting with "0\r\n\r\n"; err=<nil>2026/02/11 10:31:46 Unsolicited response received on idle HTTP channel starting with "0\r\n\r\n"; err=<nil>已完成 2/2[*] 扫描结束,耗时: 12.5736678sD:\Tools\Sec\Web\Cobalt_Strike_4.7\plugin\OLa\scripts\Intranet_scan\fscan\x64>
```

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOv39cRuCMMyBicdqlntb0LDYE0KQeeNV2zcTkSlsp4xzAJSDN0JqO4CsQ9zKwlQqHNpGtHK1biaqU7bmkrxDURktu0nudRUAPUKs/640?wx_fmt=png&from=appmsg)

Kimi总结（AI赋能）

目标主机信息

|  |  |
| --- | --- |
| 项目 | 内容 |
| IP地址 | 192.168.10.26 |
| MAC地址 | 00:0c:29:7e:44:f3 (VMware虚拟机) |
| 操作系统 | Debian (CentOS Web Panel环境) |

开放端口与服务

|  |  |  |  |
| --- | --- | --- | --- |
| 端口 | 服务 | 指纹信息 | Web标题 |
| 80 | HTTP | Apache/2.4.38, CentOS-WebPanel, jQuery | M87 Login Form |
| 9090 | HTTPS | Apache-Struts2 | Loading… |

关键发现

1.Web管理面板暴露：80端口运行 CentOS Web Panel (CWP)，标题为"M87 Login Form"

* Apache 2.4.38版本较旧，可能存在已知漏洞
* CentOS Web Panel是Linux服务器管理面板，默认凭据风险高

2.Apache Struts2暴露：9090端口检测到 Apache Struts2 框架

* 高危风险：Struts2历史上存在多个严重RCE漏洞（如CVE-2017-5638等）
* 需进一步确认具体版本

3.网络环境：该主机位于VMware虚拟化环境中，属于内网资产

后续建议测试方向

* CWP面板：尝试默认/弱口令登录，检查CVE-2022-44877等CWP漏洞
* Struts2：使用工具检测具体版本，测试OGNL表达式注入
* Apache 2.4.38：检查是否存在CVE-2021-41773等路径穿越漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOuhp23MlVVhnYg4XHbJVPHLTuiaGib3ToABrR4zNgaPTVwx129wnhXOleaZbsZibOsdhCCSAR7fGUF4wXofzDp9cRS1IV3kb0MriaI/640?wx_fmt=png&from=appmsg)

Web界面

http://192.168.10.26/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOtkJvicKKEiawicRJH28Mfj9czABNw2ZtTE1l3Q2ic4bQI0XC9GcQUVtWjy2mLxpBoy5pDzSS3oibQ3wwOM6NegJCmN1MkOOnPUxU0w/640?wx_fmt=png&from=appmsg)

https://192.168.10.26:9090/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOtABSgicSqBh6Ufee7foaIYK8PaTx8Pias0m10SVwQaicn2II3WrxHUm3nugrb2V5chwzE1Q5UDEpuVKptqJWhgYz5wU0g6ectyWQ/640?wx_fmt=png&from=appmsg)

目录扫描

```
┌──(root㉿Luistin)-[~]└─# dirsearch -u http://192.168.10.26/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.htmlfrom pkg_resources import DistributionNotFound, VersionConflict_|. _ _  _  _  _ _|_    v0.4.3(_||| _) (/_(_|| (_| )Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460Output File: /root/reports/http_192.168.10.26/_26-02-11_10-37-36.txtTarget: http://192.168.10.26/[10:37:36] Starting:[10:37:37] 403 -  278B  - /.ht_wsr.txt[10:37:37] 403 -  278B  - /.htaccess.bak1[10:37:37] 403 -  278B  - /.htaccess.orig[10:37:37] 403 -  278B  - /.htaccess.sample[10:37:37] 403 -  278B  - /.htaccess_orig[10:37:37] 403 -  278B  - /.htaccess_extra[10:37:37] 403 -  278B  - /.htaccessBAK[10:37:37] 403 -  278B  - /.htaccessOLD2[10:37:37] 403 -  278B  - /.htaccessOLD[10:37:37] 403 -  278B  - /.htm[10:37:37] 403 -  278B  - /.htaccess_sc[10:37:37] 403 -  278B  - /.htaccess.save[10:37:37] 403 -  278B  - /.htpasswd_test[10:37:37] 403 -  278B  - /.htpasswds[10:37:37] 403 -  278B  - /.httr-oauth[10:37:37] 403 -  278B  - /.html[10:37:37] 403 -  278B  - /.php[10:37:40] 301 -  314B  - /admin  ->  http://192.168.10.26/admin/[10:37:40] 200 -  811B  - /admin/[10:37:40] 200 -  820B  - /admin/backup/[10:37:40] 200 -  811B  - /admin/index.php[10:37:44] 301 -  315B  - /assets  ->  http://192.168.10.26/assets/[10:37:44] 200 -  444B  - /assets/[10:37:53] 200 -    1KB - /LICENSE[10:37:59] 200 -    1KB - /README.md[10:38:00] 403 -  278B  - /server-status[10:38:00] 403 -  27...