---
title: 跟着红队笔记打靶：PWNOS1.0
url: https://mp.weixin.qq.com/s/0c6MiLydSBSlqYEAhT54Lw
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:04:30.359417
---

# 跟着红队笔记打靶：PWNOS1.0

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hAugh98lMaRKL7ERIu2lVXZ716vSUEianGe1oHyTBSD4fOBibcbK3SSYIfm1v3gibUU3zPOQBVWZicFWddW1xJkKMrnWdB4wXicXMj6cUrXBNwQs/0?wx_fmt=jpeg)

# 跟着红队笔记打靶：PWNOS1.0

原创

网安热爱者week
网安热爱者week

week的杂货铺

![]()

在小说阅读器中沉浸阅读

靶场地址：
https://www.vulnhub.com/entry/pwnos-10,33/

大佬的视频：

【「红队笔记」靶机精讲：pWnOS1.0 - 在Perl CGI架构下构造反弹shell，你可以吗？】https://www.bilibili.com/video/BV1Rv4y1D771?vd\_source=3caf2dac9c9273de4d9b0fead4712250

【「红队笔记」靶机精讲：pWnOS1.0 - 选择hard模式再次用完全不同的方法实现这台靶机的渗透测试。】https://www.bilibili.com/video/BV1yG4y1b7FQ?vd\_source=3caf2dac9c9273de4d9b0fead4712250

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaRKYTYo2JeOguYe6zZEL8vEjRk82bpGng59eMnH2VI85KqnXDetUHFbdWg6ibCES3JpyeUUWW5hrialSXsFH1nI1VCD8hEbzhN60/640?wx_fmt=png&from=appmsg)

下载解压好之后，双击这个vmx

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaTkE8W0wPmZzjGPs8xy5GGE85EVVATdu6OA98pRMh8sKkbicITIZ7HYxia2A75SjMkpdjxaZGiazG7QagLOq0AP0DShfdEX3d8w9s/640?wx_fmt=png&from=appmsg)

vmware会自动导入一个pwnos虚拟机

直接运行这个虚拟机

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSp3o32ibib8ia96KHP2o1icJmUwL6lg5YXcxMbnFFQgRwMJyibtQRdzsgqwWSMlJJGwJhCgpfBFwmLhBic2z85fYTBaz0icjxNsoAVZs/640?wx_fmt=png&from=appmsg)

一定要点击这个【我已移动该虚拟机】！！！

否则这个虚拟机会获取不到ip

等到虚拟机开机之后

更改它的网络适配器 改成nat模式

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaS5mMnHlQqU64In7kjeyr3mfmKib5icMPrHWJm7w7rFiczDy0eETIEjibIdicfxMHDP62XicjS9Xdks6ZxficssdYQ0Z3Ztndz1CefF0g/640?wx_fmt=png&from=appmsg)

然后重启这个靶机。

就可以获取到它的ip了。

# 1. 信息搜集：

## 1.1. 主机发现：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQAibKjIQI0wXliaaBoOEzIqOEPe1R5FXzondQ1tOAjiaR93AXHhTX2puPicibarAALJVyBcSUhZIawb1y992YcJckcribOvIuAlaLpM/640?wx_fmt=png&from=appmsg)

129是靶机

## 1.2. 端口扫描：

TCP：
![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaRkK9XpJU9VWKXubn5DN9zv25uB29DGicKESccv6KB0UwaLBpLmicPFpzuW5lZmN5R22EbXm5d0gx6JID9YWpkQ3O5PC9WvE8nfw/640?wx_fmt=png&from=appmsg)

UDP：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaTCvUKJacCl945t7UccnjPBU9HTL2C5MFQYOk66ycyvpicHia2AhE0qXODPeMhhlxO0EOqJsDtRO8DJM1XJIRic0P0bPibFbl9sKs8/640?wx_fmt=png&from=appmsg)

## 1.3. 详细扫描：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaTeJMqjOjfFy63rjplibHQibsT7JBGbdaSqq3SyUz1A9uqdrxVzpDia3IHwKyPQSJX1lI6mYsI6LcsAiaNTFBbEPuqtmx24dtNmXEk/640?wx_fmt=png&from=appmsg)

nmap自带脚本扫描：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQ75wWibe6lHJFvdRJII7qlzCLObCicN29I2hGypXQIIlKvLCYBiac2NfgJnYkWiak10lVKkOBa0fkj1tKmdS5HghLYgkbNG6cNCF4/640?wx_fmt=png&from=appmsg)

这里有一个CVE 后面要用到。

# 2. 渗透测试：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaT0u8WM92oFhYE9gWvPz2aJbxcN6VpwvtGb8GSRLxKc223FW3V6iaWsqWdt45CnUCsBN9IEC3uqibtm5GGbbD5ouiaOqghoNhYzCo/640?wx_fmt=png&from=appmsg)

点击next之后：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQl2n2zkAYTEOKjYjeGno5try8EGkEpJUPw0EENs480LEH8ACTNFl6k7B97rlfCTWbhaMP5e6VjznGPzqbu9QSnahBX1rerakU/640?wx_fmt=png&from=appmsg)

随便选一个之后：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaT9peoicN3yOo0PMj1M0yLbW1UpXyWDHhkY6QmBjLiafpTUqAV0SuchFcXPicN43Kd3iaJnbphYO08uibmN7wksglugT2ZEUbVPQDYI/640?wx_fmt=png&from=appmsg)

点want to try again 又会回到index1.php

还有一个php目录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaRWyvgrC4iccw1EmbPc8RZjd3XVItDvXdjic1yiajzjT7EpnAKF9viaugm49tCGicf8QM4uycsBg9LS6d2La9LMkt40EEmnh3dGE1lY/640?wx_fmt=png&from=appmsg)

但是phpMyAdmin需要账密才能进行访问

这里暂时没办法。

在index1.php页面 试了一下把两个true改成false:
![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaRgsBoAvz3t4jSy7qsricHiaLD2eux9XX2I1HibTS2GnLkk0TB1lSsIYxicjQEQMx7flwyWDicWqXGq46lpbiaTJMBtWjtiagiciaORTsZA/640?wx_fmt=png&from=appmsg)

include的文件包含报错...

最后发现是connect是导致报错的参数。

尝试包含index.php：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaRBg4lFUEVkzPqkib0TTo1icFOlxpalHmrcCYoGlhYLibj2UuO2wbXOwTpspu8a4cZtFouxibPfAKWBke8YVuJxa9Oib7N9kO5Ohl0Y/640?wx_fmt=png&from=appmsg)

成功~~

/etc/passwd

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaSOfBeEpbo8MbwuAtvswYRuEJiaBMAXUrjxhI3If4nY1aDcxh6EETXQlPZv08jFG94GsCFFfibib7JxUUDY5fhwRg3bsGgDJE7sJw/640?wx_fmt=png&from=appmsg)

10000端口：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaTYJbicI2ewJkLiacLaaAY967CLdRcdXrCVJ5OKFtONkO2XZ9ia3VDScFnQ2AUkjk7xEkiby1App6nq6Xr1UDcU8sAME39O64uBmRE/640?wx_fmt=png&from=appmsg)

这里也扫了目录 应该是webmin自带了目录保护

会重定向到这个页面 让你输入账密。。。

查一下历史漏洞：这里whatweb看不到版本。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaTSQpGIF4d9hOZdDYqV4AtZmKt3sqYFNoECktmCDMIkiayEjULNG4iaYia1IXcEYNadQf8lEibFPIa4MgcP2eY1icxTrjtpH1o4iaZKs/640?wx_fmt=png&from=appmsg)

用2017这个

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaTMbQgPMu64n9icEMiaSkxzAhPbxVI4becTI6snPVr8Hb1NXQnQGjHIyjtjQImic8t7jccwtOoicziaYU3QOzn6ahqjkayYXiaq8brRM/640?wx_fmt=png&from=appmsg)

竟然可以直接看到shadow:

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSZt2XN4TSpZIOMXQyvqotpQCwymibbhO7yAYU7hM0yyicic4ibicYJ0Bsrkc16GHsUtBdh6iaqPiaPp5YMXCgcMsP5seAvGh6cHQnMMw/640?wx_fmt=png&from=appmsg)

john进行一下解密：
vmware h4ckm3

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQ8vm4db5ps0SMWqfmCxV6kj4dfOjGTLAFqCh6ribsuicr9SnD7vTa3IgFVWOvjMrvLyibYRmZPjCOZLfUaSxw6xFJFykXp6LmicEk/640?wx_fmt=png&from=appmsg)

看了计划任务 没东西

sudo -l  不让跑

这里其实有点茫然了 但是用webmin的漏洞又能读到/etc/shadow

说明这个webmin应该运行的权限不低

实际上webmin这个漏洞会有另一个问题：
如果使用这个漏洞访问.cgi文件的话

会导致这个.cgi文件直接执行

【一般情况下 在网页运行的/cgi-bin/目录下面写入.cgi会更稳定。】

先复制一个kali自带的shell文件

```
cp /usr/share/webshells/perl/perl-reverse-shell.pl ./shell.pl
```

然后改一下里面的反连地址：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaR8C6SIpiconiahxl5wt2CDlYPiaFic7LDCv5UMchQZppb7vznriblWuDicAg6FX3HodqeS5wbfaEQ1kmtgDgUdQnjdADyBH9srQfn6s/640?wx_fmt=png&from=appmsg)

这里尝试了直接上传.pl文件 没能成功执行 改后缀为.cgi就成功了

应该是有安全策略拦截了。

在shell.cgi所在的目录开一个临时http服务：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaRfCC9631iaqZSsfBju1xteC2LaibWIRhzRbm6HQShsGwMrNA9CeR8ZMtauSyZ8EJd2Pok9eyTbucHAHJuapqusKq1VLZDYJNyc4/640?wx_fmt=png&from=appmsg)

在ssh里面使用wget下载下来，然后chmod给一个执行权限。

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaRzsZvesEyL8ia5Pc1y48OMz1mXz7sZz2CqJcYr6N9ovPIKTcibGvg65FfcTCThVQmUoB8OJBnkYXHKhDtiaNnzHlTqmQ9XQMKmOE/640?wx_fmt=png&from=appmsg)

利用漏洞的利用脚本 让webmin访问/tmp/shell.cgi

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQx7Sd43f0RgaVuxiam6NY6QB17gicfFRSlKEQJeFMVa0ib5icpPDJeMyqxnbUJIY7lQ1Y7EeevTIrDkz2kyqiacib0GstLCxibhCx5ZM/640?wx_fmt=png&from=appmsg)

因为webmin运行时的权限很高，

所以它访问shell.cgi并执行时，

返回的终端也会是一个高权限终端：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSgFaBX9UJ8FsclVkDDgdHibnibibibFeOiakYel5H4l5raTricRdm8X3yZmzVumVlibRBzatOowX7hiaT9TwqEGJ5P6uKZeBgpibFIAZ9Q/640?wx_fmt=png&from=appmsg)

root~~

cgi是一个已经被现在的web抛弃的组件

并发的支持很差 开发困难 安全性不好

目前已经基本见不到了

大佬也给了另一种解法：
已经可以看到/etc/passwd

那么就可以试着去看这些用户的ssh文件

ssh公钥：/.ssh/authorized\_keys

这里已经获得了公钥 可以去尝试生成一个私钥

```
searchsploit prng
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaRVmw4WwdazebiaVJy8wAaFfibbpk3DAKOrZfY8ODIrfbGYMqn3VibMHkwgt99QEP4ZTJ3UpOUA4lIXiazkcgbNdd6gwC9pwn78wPw/640?wx_fmt=png&from=appmsg)

利用openssl的伪随机进行私钥的碰撞

这个文档让我们下载一个压缩包，然后解压

里面是成对的ssh公钥和私钥

可以去查找和服务器相同的公钥 然后使用配对的私钥直接进行登录。

逐个用户尝试后 发现obama这个用户的公钥有了匹配。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQfHhoiayGMZB5RPowdSeBTH5y7uMicEmhHannvKVy1YDibH6hef5ILEuW67FE5UOxY7LORdfoqibnq5KKic89KA8HA4blApDQGicuqc/640?wx_fmt=png&from=appmsg)

这里去找相同文件名的私钥就可以了：

```
find ./ -name "dcbe2a56e8cdea6d17495f6648329ee2-4679"*
```

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaTEaiapicDQqKLYRVImpRGqf52s1Adtwf9AhUETDjiaDPvfQ8RN1EMjvZhB8pbxAiboXG18KYzYQWaZxv7Eo7c5HVu1HJGhz4nic4Os/640?wx_fmt=png&from=appmsg)

然后复制到当前目录下：

```
sudo cp ./rsa/2048/dcbe2a56e8cdea6d17495f6648329ee2-4679 ./dcbe2a56e8cdea6d17495f6648329ee2-4679
```

使用免密方式进行登入 发现失败了 依旧让输入password

这里使用-vv查看所有的流程：

```
sudo ssh -oKexAlgorithms=+diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-rsa -i dcbe2a56e8cdea6d17495f6648329ee2-4679 obama@192.168.137.129 -vv
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaS1gzzfhlKwLzgI4vD3PIp3Czdt57FwQ4S7q3zs0MclqIMr8Ll3sibfFulvIRXbLibiaabhZWmfiauynlxEGWVJwjNfIJicYHCibicxS4/640?wx_fmt=png&from=appmsg)

没有对publickey的类型进行指定

```
sudo ssh -oKexAlgorithms=+diffie-hellman-group1-sha1,diffie-hellman-group14-sha1 -oHostKeyAlgorithms=+ssh-rsa -o...