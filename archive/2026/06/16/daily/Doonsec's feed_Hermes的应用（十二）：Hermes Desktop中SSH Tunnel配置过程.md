---
title: Hermes的应用（十二）：Hermes Desktop中SSH Tunnel配置过程
url: https://mp.weixin.qq.com/s/U_H7Pjma5-SRyjn_tMWo0g
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:00:14.192182
---

# Hermes的应用（十二）：Hermes Desktop中SSH Tunnel配置过程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2PhZXrB0gN5fWXFj1gPmOb7HVDA6ZuLnh80Wsox6KsJ5kzCibMTyxSdqTgfv0sWJiaYAHHcpmgK063ZLr98AkmVKic8dNTuujHwNSUvibkZpHMs/0?wx_fmt=jpeg)

# Hermes的应用（十二）：Hermes Desktop中SSH Tunnel配置过程

原创

MicroPest
MicroPest

MicroPest

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Hermes官方出了个Desktop程序，晚上用了下，有个ssh Tunnel的连接方式有点坑，网上资料没找到，现将步骤过程分享如下：

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN58kvCyh5lHjeDibL03J10FTTdeAJPfLvXsQQYul2AfpdvoL9NAUuzT6QNcANhibDDOzWGwUF5uDmnc3vptTCW98hUZ8fFrQCc5A/640?wx_fmt=png&from=appmsg)

照上图这么填。

1、ssh-keygen -t rsa ，win下生成密钥对；

将id\_rsa.pub的内容放入到：echo "粘贴公钥内容" >> /home/kali/.ssh/authorized\_keys中，在kali中运行此命令，生成authorized\_keys；

2、SSH 服务对 `~/.ssh` 和 `authorized_keys` 的权限要求非常严格。在 Kali 上执行：

chmod 700 /home/kali/.ssh

chmod 600 /home/kali/.ssh/authorized\_keys

同时确保 `/home/kali` 目录的权限不是 777（一般 755 即可，执行 `chmod 755 /home/kali`）。

3、检查 Kali 的 SSH 服务器配置是否允许公钥认证

在 Kali 上查看 `/etc/ssh/sshd_config`：

sudo grep -E "PubkeyAuthentication|AuthorizedKeysFile" /etc/ssh/sshd\_config

确保输出为：

PubkeyAuthentication yes

AuthorizedKeysFile .ssh/authorized\_keys

如果不是，请修改sshd\_config的具体对应项。

4、在kali中打开8642端口

```
hermes config set platforms.api_server.enabled true
```

```
hermes config set platforms.api_server.host 0.0.0.0
```

```
hermes config set platforms.api_server.port 8642
```

5、**在本地电脑的终端**（不是 Kali）执行：

ssh -i c:\users\用户名\.ssh\id\_rsa kali@kali-ip

如果不用输入密码就登录成功，说明可以无密登录，可以使用Hermes Desktop的 ssh Tunnel了。

应该就可以通过 ssh Tunnel 连接上kali下的hermes了。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

MicroPest

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

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