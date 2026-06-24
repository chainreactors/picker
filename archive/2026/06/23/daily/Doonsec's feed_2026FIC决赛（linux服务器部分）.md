---
title: 2026FIC决赛（linux服务器部分）
url: https://mp.weixin.qq.com/s/05XRdxpIpYE_KcdjFqKg2Q
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:00:04.510518
---

# 2026FIC决赛（linux服务器部分）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/T5C6icTcSx9NJ56UH6GicRKVewsZbNUxG1icLibWO2V1ET3KXqIqcN8PV1xzc3PS6dZLhyMIW80qQTdWjQJUS4COn4NialJhVibsbLyNxWgPjibibaA/0?wx_fmt=jpeg)

# 2026FIC决赛（linux服务器部分）

原创

Serendipity
Serendipity

Serendipity的小屋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

容器密码：`\/a15f5b1d-a9fbdb79-de9ee6bf-28b9fce1\/`

## linux服务器

> web1为阿里云镜像，web2为腾讯云镜像
> 感觉web1主要就是考网站重构，web2的openclaw辅助web1进行做题

web1有ip和ssh，直接可以连接

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OfiaN7WDIZIbGTBftAqicKpibmSHjeMIolQbA4Z40n0m4FkkCAq4a200Fa4ibppvI9kZ6JcfWboYVJBnrTicOia2fRV0ggBLpLl272c/640?wx_fmt=png&from=appmsg "null")

web2启动之后，没有显示ip，原因是网络配置的mac地址与网卡不匹配会导致获取不到ip，这里修改一下配置文件

`vi /etc/netplan/50-cloud-init.yaml`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MbmGzs0hXAo4jhULuR0LpDxP6I60sL3MD32ickpNBvIjjuibnuGNiaOicjhZRaibDysYX0q6cXlHIchF5cX0tfcYYNDyzdESOHicZZY/640?wx_fmt=png&from=appmsg "null")

将mac地址注释掉即可（vim的语法就不教了，不会的话自己学一下）

重启之后即可

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NGR0XEKOzjYKGpy8Ps8x8saMoVlO6ouX4rqYwfy3GpKdjT6xtBalrhD2kfaNyxujI1beiaNcERC1Y7pnzft6gZUL6hvjqJz5sU/640?wx_fmt=png&from=appmsg "null")

然后finalshell连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9ONnob9fsUpib9KfQSD4W1g0Qw31wgcXCn2ooKa1DugvZjv8Xkn0rZtNYRqiaOIic0pB2g6KATsg0picNXac6GCPDNvlDOQialkU6lU/640?wx_fmt=png&from=appmsg "null")

### 1 分析服务器检材，找出来自阿里云的服务器镜像，其源盘SHA256值为

### 【参考格式：ABC】

**119FCF5D8F8F69336656B8E93A4C00838BC5A6C1FD82878F9C8EDFA1FE437F0D**

将web1仿真之后可以看到阿里云的标识

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9M5UbxNcNKLoUZ0Pq2Qm5l6sowsfzZLXDb1ro3nRq2pvvVicuj7kR2wvjuRTXwLddSIzajNIXCbdWMlbWOLgtpk6dT1aMMRLrp8/640?wx_fmt=png&from=appmsg "null")

也可以搜aliyun，搜到一堆文件![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9ODPytP6vYOx6GltWk4VibVWy9fE1FUIiafRibIiafTYIfzrpuQbaSW1fib1Z9PRK6Olte9VsLPwzsQQibN6V3AFP8icf70fkToHGiaRaw/640?wx_fmt=png&from=appmsg "null")计算源盘SHA256

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9N6w8VL2vQtr6v7wic1XBRDrv4N36m1y1iaVK223LCesUTVnKdiaJE6TxIsqaciaLcoldM8OtOVxuAZtV7BEADvyw9wLEUnB4IyDqI/640?wx_fmt=png&from=appmsg "null")

得到答案

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9Pz5SdWFtIKic8JgfuLjibfZOhibNWWGXnGgfxzqlCfkmNhVic90hRcMBl0OwYgBlfMlrAEL3Ds8wcY6jhEALbhz4gPMfwXF2rXjRc/640?wx_fmt=png&from=appmsg "null")

### 2 分析服务器检材，“星球商城”网站使用的 React 服务端渲染应用框架为？

**Next.js**

在火眼看到有个faka的docker镜像

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NuzDQGSw7IwYA41pqBznr5F2wIgmibjpL4zAG2j0e29L7icwAeNoe7jQ3cBkuVeIEsicP3OibpW4ibIx4XjV1Tm2y4A9yZRUA3XmsA/640?wx_fmt=png&from=appmsg "null")

启动一下docker，启动faka镜像，看到了Next.js

```
systemctl start dockerdocker imagesdocker run faka
```

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NR5ht1x9ykGoekhldZHkViaEibInRsYykUCgeUcxVnFUCqL0d6rErONiaAzeaZibWTurIGVHKhiaqLCqjwJnaaCeBjcuIMUj3Ge00Y/640?wx_fmt=png&from=appmsg "null")

### 3 分析服务器检材，“星球商城”网站管理员密码所用的盐为？

### 【参考格式：ABC】

**Honglian2026FIC**

可以直接去找相关文件，但是费时费力，不建议

`/var/lib/docker/overlay2/jr0hxl8wnzf9weogwginrefta/diff/app/src/lib/auth.ts`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MAfeNltY80OKibmRRHLmTGdLrKiaKJkUHicMDeXxtIl6Qia231acD86VK1UrlkDVOBHjHUZLSiaYGYRp0ccDWvGeDFy5PT4y9Dkp2I/640?wx_fmt=png&from=appmsg "null")

也可以进入faka容器

查看所有容器`docker ps -a`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NceicQUibtuSUuVNicDsY1u9ToXicKKzgtsyZEDicV5xmiaKSzDJ9EweLeljY56eFvUnHfxNw1lib6WEfC3p98RbribRpia4yA257YB2Vo/640?wx_fmt=png&from=appmsg "null")

启动该容器`docker start clever_napier`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OlL0SeYQJ9SxDibV9CcsMWLZiakEn8d4eEyOFwE4GEYX2dzOhO3YvJPoibmiap6fA1VtqWPLMnbiaTrBDk6S0AWDeo0DrAr7SR2zib8/640?wx_fmt=png&from=appmsg "null")

进入容器`docker exec -it clever_napier /bin/sh`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9PQBPykwvibMQ2YlmNTor92UvxOMVLoHGR5RCPmfv1Ba26jmFT5V68P3rsfialVCLvUN1zrm02ibL2NrRv6xjX1FNwiawmFKqZTt9c/640?wx_fmt=png&from=appmsg "null")

查看package.json

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9Mb0mHnhF9FutozFLhicib4bSF5Fia9xMkGyia7NJA6YkGmMicnE8RjHCVrpGKJCoSpZT1Yn7iaO9KoXqywgWfRwrDkLI71kxUCWhf6Y/640?wx_fmt=png&from=appmsg "null")

看到了一个seed.ts，那大概率盐值可能都在这个文件里了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NwbPokemxFx7d6ksRxclfnGWfZuEAE4hZObJQo5CBqYfKYKBZvNGkUemslYL8JPSFsFvryrAv9Hib1uCSReJtAMn08icnibp9B8E/640?wx_fmt=png&from=appmsg "null")

### 4 分析服务器检材，“星球商城”网站备份的数据库加密后文件名为？

### 【参考格式：abc.abc.abc】

**fkdb\_20260507.sql.gpg**

在web1中找了好久，没看到备份文件，想起来是两个服务器，可能和另一个服务器有关，在web2的`/data/bakup/`目录下找到加密备份文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OrjBtJLdyGanBaibjTq92BLr1saoTcRWnPaibPXx8ro6ocUq4aFssnVfjxBtJWBZXCkZMQ81eIkorePibXd21e1c4k5n6UxQWLFU/640?wx_fmt=png&from=appmsg "null")

### 5 分析服务器检材，“星球商城”网站使用了NOWPayments作为支付接口，其api\_key为？

**934P23T-FZVMBDE-Q1R06NJ-4E6HZTM**

刚连上服务器就在root目录下看到.env文件

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OicscQlzjtNFeA25pFyBQz0wMa7ib87NkNBkPWcP7fuJzjEcmMrW3KticprcFibNxqk1h81tSxMf7hjJ9x2Ie7g6AqCm03eYFCfr0/640?wx_fmt=png&from=appmsg "null")

打开就可以看到

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OxdIrMzicWEIQ2zSKHyLD0NsibiazzlYaGhc5OWNCGZ3GyyKQFXRnRz446ibaMbyPNRmibhxcHlQBk9k70IuxwdTvy4UNwDjEcGVEY/640?wx_fmt=png&from=appmsg "null")

### 6 “星球商城”网站已成功交易的订单总金额是多少？

### 【参考格式：10】

**130**

> 这个题一看就是在网站里，要不就数据库里，正好前几道题有个数据库备份文件，就继续看看openclaw中有什么可以用到的

在openclaw会话日志`/root/.openclaw/agents/main/sessions/`中看到有个文件特别大

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NiajtkajmVPqEdGeoayyLNPbsUmgKdCs7UJ98h11BZiaWiboOl8YST3wMa4qhvFHShl8Yh3tZyIUpXQtwmARgJGAsEJIfV6WsuO0/640?wx_fmt=png&from=appmsg "null")

打开日志文件搜索fkdb\_20260507.sql.gpg或者密码可以看到数据库密码为`Honglian@Fic2026Password`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9Oicmm1ppxBFZK9VxKMBpJ95PicvJicG4l8zBuhanJLgStOsABWK5xibBqAOk5dNRGMcS4gZDWBEowRWTwibZOQ2icZtTdZuxlHlRCxE/640?wx_fmt=png&from=appmsg "null")

同时还有解密的命令，解密一下`gpg -d -o decrypted.sql fkdb_20260507.sql.gpg`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OsKelD26bczPDWIORmcSaMcdPZ4CmXhBy46icks0QdmPRFy1mam7xamTTqpzE15VXy5o6USpxRJghoLH5yHYxjiaL6Q0sChV3rA/640?wx_fmt=png&from=appmsg "null")

输入密码后成功解密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NJhLeWNjKg46tCLfnLGyvclKJDqmc7MDAsJb4BPk0vic9hYDIuDhxYUiakjj9b1NQfg9c23UOmmiarXsJS2rTBJ5lZib8NyF75AtM/640?wx_fmt=png&from=appmsg "null")

这里也可以启动openclaw`openclaw gateway --port 18789`

新开个窗口查看 仪表盘服务`openclaw dashboard`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OAJUfWBpuoyanKz62FicfhsdMTZMm7lKW52LSIz86U1icesiaOfXmqeaVBW5t7x1zUVEd0mbTpxvYvqX3GUqsuswFvc9OwmLzBIE/640?wx_fmt=png&from=appmsg "null")

本地cmd输入`ssh -N -L 13501:127.0.0.1:13501 root@192.168.50.129`

接着打开浏览器查看历史对话即可（不知道为什么我看不到）
`127.0.0.1:13501/y6zscy/#token=43e3d23a5038fc58bff147f96c152b19d3e8c980710b8b62`

接下来把解密后的数据库还原到postgres中，在web1启动数据库容器

`docker run -d -p 5432:5432 --name psql -e POSTGRES_USER=fk -e POSTGRES_PASSWORD=Honglian@2026fic -e POSTGRES_DB=fkdb postgres:16`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9PDdqEUGz150Y3qGRvWAwB2DZM9zkjhUpN1nGbv3ibqeicQVt5AK5flgicQicEBXPg4KwZTTpkED0ngtCp5msfJpYqAYUhFhFGe3KU/640?wx_fmt=png&from=appmsg "null")

将解密的备份数据库文件传入web1中（IP根据自己的web1写）

`scp decrypted.sql root@192.168.50.128:/data/postgres`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NQ2hlibIHaYWv0XvjpUGpH9yBF6ao1UYgFOndgbq9rut6VFnJ1gSeRsDfHlgzMTDPibvSoBaswMd65ZmggyKibkqvVUDJyX8nmUM/640?wx_fmt=png&from=appmsg "null")

然后在容器中执行还原命令`docker exec -i psql psql -U fk -d fkdb < /data/postgres/decrypted.sql`

数据库连接url在刚刚root目录下的env文件中可以知道

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NVoydicWE0CMhqmqR81CQur6Ivu9EUSJ8NqVuwqPTyTULyKHcJg42r5E8Ye6Q5SdBwzYS0dc7qFcxDxia2XRw1WHzrN9jliaTNVw/640?wx_fmt=png&from=appmsg "null")

navicat连接一下postgresql

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9Nc8icptulU2ibkPUVqkM8ibOrysWRvBgsU7TZS8snuYgmiaP6s2olIsko12VIwicvPia913g1kSYDw9Dt7LCibzegtqMdKefwFERdLKY/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9Oq9vBmibBtzvoIIplgNbTqHlqiaBB9KXrmiare6SicjicibX1mpBj7ic5rmRNTOGiau6RcNohiaKmY0JY4Z8DibAVa3RMspp4EnqXZIg6ew/640?wx_fmt=png&from=appmsg "null")

查看有卡号的

![](https://mm...