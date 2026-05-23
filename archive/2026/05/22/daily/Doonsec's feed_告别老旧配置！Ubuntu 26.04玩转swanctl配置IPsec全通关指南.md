---
title: 告别老旧配置！Ubuntu 26.04玩转swanctl配置IPsec全通关指南
url: https://mp.weixin.qq.com/s/GDtCWcI4f4s7TqTPjoHhCw
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:37:37.777485
---

# 告别老旧配置！Ubuntu 26.04玩转swanctl配置IPsec全通关指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9j14GSZeRZY8A1vganuskytfZBzZfkLkUefXooUJibb7NdqQiav2frlV4CQFftrAmUGU7S9vqibZZkxdTOZbwpKSYibZJsn5LhZiaicXjibQ3I2hfc/0?wx_fmt=jpeg)

# 告别老旧配置！Ubuntu 26.04玩转swanctl配置IPsec全通关指南

原创

衡水铁头哥
衡水铁头哥

铁军哥

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

突然间发现，自从我发布了IPsec管理系统之后（[告别IPsec复杂命令行！我做了个Web管理系统，StrongSwan对接H3C只需点点鼠标](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458863119&idx=1&sn=cad31457c4d733d26fee10ea0e512c46&scene=21#wechat_redirect)），我好像对于IPsec的配置介绍的就少了。

其实，从我的视角来看，IPsec的配置整体不算复杂，我们之前发过一个IPsec文章合集（[IPsec](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI4NjAzMTk3MA==&action=getalbum&album_id=1966297991099613185#wechat_redirect)），但是后来一篇文章只能加入到一个合集，后续的文章就添加到VPN合集了（[VPN](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI4NjAzMTk3MA==&action=getalbum&album_id=2228552527535570946#wechat_redirect)）。

配置IPsec的核心部分，我几乎都整合到了基于strongSwan开发的IPsec管理系统中（[从点到网！我们的strongSwan管理系统支持网关模式了，可作中心枢纽互联多分支](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458863332&idx=1&sn=c9a2b594a80e963eada21b3be3668d4f&scene=21#wechat_redirect)）。

念念不忘，必有回响。当然，几年前就有粉丝留言，说我当时用的strongswan-starter已经被淘汰（[对比华三设备配置，讲解Linux主机如何配置strongSwan](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458856223&idx=1&sn=fc0bf5a07315dba127b48efe02c36d30&scene=21#wechat_redirect)），想让我研究一下swanctl。又好几年过去了，目前看来swanctl好像还真就成了配置IPsec的主力，那我就来个虽迟但到，给大家简单介绍一下swanctl的配置。

首先，系统依旧使用我们最新配置的Ubuntu 26.04（[仅占752MB内存！Ubuntu 26.04 Server版上手：这才是服务器该有的样子！](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866714&idx=1&sn=472718aa3cc5c1c23438adceb195dd8b&scene=21#wechat_redirect)），部署时用自动安装即可（[拒绝手搓系统！Ubuntu 26.04自动安装实战：让电脑自己“卷”起来](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866839&idx=1&sn=74a6fac0d6cc8c90635475dea333ebb2&scene=21#wechat_redirect)）。

部署完成之后，我们首先配置中间转发设备ttserver6作为路由器节点，使能系统IPv4转发能力，并为两张互联网卡配置IP地址。

```
sysctl -w net.ipv4.ip_forward=1ip addr add 10.12.1.2/24 dev ens192ip addr add 10.23.1.2/24 dev ens224
```

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZY9In3UETVya2icIRIASYK2RMJ0A6k3rNG7NRM52nXZAdSqYB3X0Gwz7JZicB56ibFSuZ9yCL4XhYEsiabP6qaxFnglmKsmq3hCQq0/640?wx_fmt=png)

然后，我们配置ttserver5端点，配置网卡IP地址，并添加去往对端网段的静态路由，下一跳指向ttserver6。

```
ip addr add 10.12.1.1/24 dev ens192ip route add 10.23.1.0/24 via 10.12.1.2
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZYteYvSKVVKjIN7F2icvFmkvA0IDGvEI0YS4Ngwh9vbod6wFnWNEHAIC6LVyBXogkMZOPogL2Kbk3rcibbqdPZo9VXXeicBgFibns0/640?wx_fmt=png)

ttserver7端点也如法炮制，配置网卡IP地址，并添加去往对端网段的静态路由，下一跳指向ttserver6。

```
ip addr add 10.23.1.3/24 dev ens192ip route add 10.12.1.0/24 via 10.23.1.2
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZYpNu1bA7cAIaozcC5cKpkmNqGgiaFWHBzzl93rMrC9ictVAuVuvHfTS3qK69k8dqKZ7vzVZ3MrbJRGicE0nX5u8auLSY1kLfedoA/640?wx_fmt=png)

万丈高楼平地起，现在两台端点设备可以顺畅沟通了，老规矩，咱们先浅浅地打个基线流摸个底。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZYrH7icPCp0pibf8gw5wPDjsKoqicR8s6mo7CP9wNR6pSUZyEn5nPeJPPGyibvf0HHBS5TUdwBrMZ5ySbk8xwtjkdmpJibBANqV1zug/640?wx_fmt=png)

因为3台设备都是Server版本，性能一般，平均带宽在7 Gbps左右，跟上次的测试数据差不多（[Ubuntu 26.04 转发性能大考：Desktop居然干翻了Server？](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866936&idx=1&sn=910ba33249eb54c9616d78b51519a807&scene=21#wechat_redirect)）。

接下来，我们开始配置strongswan-swanctl。首先，我们在IPsec隧道的两端安装核心组件以及额外的加密插件，避免执行swanctl命令时出现插件缺失报错。

```
apt-get updateapt-get install -y strongswan strongswan-swanctl libstrongswan-extra-plugins libcharon-extra-pluginsapt list strongswan strongswan-swanctl libstrongswan-extra-plugins libcharon-extra-plugins
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZbl7tbOWhqVFiaribotQN8rkrzqvL9icg9y3wq4H1haZxFQnmBiaDYPGLNemTlkCKh9OJ0gdOzqF6BHeFYamM3LueYvj2jpNfa6cVQ/640?wx_fmt=png)

可以看到，依旧有一个agent插件因缺乏特定权限而产生报错日志，一般情况下，如果我们不使用基于SSH-Agent的认证，可以在配置文件/etc/strongswan.conf的末尾追加封印配置，来直接禁用agent插件，强迫症瞬间治愈。

```
cat << 'EOF' >> /etc/strongswan.confswanctl {  plugins {    agent {      load = no    }  }}charon {  plugins {    agent {      load = no    }  }}EOF
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZYkQEQbtibuWib1Lc1MUXIJ50a4Gjeia9MjDbfdpmEMEvDWGlfp0FvnG7cC8LKmofzaLu4LXRDAlMOH9JsdgJAuCQTOWofYt7yySs/640?wx_fmt=png)

接下来，我们就可以配置IPsec配置文件了，整体逻辑跟strongSwan差不多（[strongSwan之ipsec.conf配置手册](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458855778&idx=1&sn=84b7e98e686e3263260f5c4d08c315ef&scene=21#wechat_redirect)）。但最大的区别在于，它舍弃了陈旧的格式，拥抱了类似JSON的结构化配置文件swanctl.conf，同时将连接策略和密钥管理优雅地融为一体（[strongSwan之ipsec.secrets配置手册](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458855783&idx=1&sn=c99fa8e295f051b2bd7a87c0fa232b34&scene=21#wechat_redirect)）。

例如，ttserver5的IPsec配置如下：

```
nano /etc/swanctl/swanctl.confconnections {    74-76 {        version = 1        local_addrs = 10.12.1.1        remote_addrs = 10.23.1.3        proposals = aes128-sha1-modp2048        local {            auth = psk            id = 10.12.1.1        }        remote {            auth = psk            id = 10.23.1.3        }        children {            host2host {                local_ts = 10.12.1.1/32                remote_ts = 10.23.1.3/32                esp_proposals = aes128-sha1                start_action = start            }        }    }}secrets {    ike-psk {        id-s1 = 10.12.1.1        id-s2 = 10.23.1.3        secret = "swan"    }}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZaTyPiajWbFSC9r9SolpymIwM80lYfHrFjUlKXXUW7Knd14YLT1q86g4pnxXlTdmlVib8qsrFKibz1qoU5ap9zwHZ8icTG39MQ3o74/640?wx_fmt=png)

ttserver7设备的配置也是对称呼应：

```
nano /etc/swanctl/swanctl.confconnections {    76-74 {        version = 1        local_addrs = 10.23.1.3        remote_addrs = 10.12.1.1        proposals = aes128-sha1-modp2048        local {            auth = psk            id = 10.23.1.3        }        remote {            auth = psk            id = 10.12.1.1        }        children {            host2host {                local_ts = 10.23.1.3/32                remote_ts = 10.12.1.1/32                esp_proposals = aes128-sha1                start_action = start            }        }    }}secrets {    ike-psk {        id-s1 = 10.12.1.1        id-s2 = 10.23.1.3        secret = "swan"    }}
```

配置完成后，我们重启后台服务，应用strongswan.conf配置中的修改；再使用swanctl命令读取并加载swanctl.conf配置中的策略，拉起IPsec隧道。

```
systemctl restart strongswanswanctl --load-allswanctl --list-conns
```

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZajME7uL5YKFcAUdZp5IDQflB2jQ5YZMaeCWAFEM2piaE6ibGNyOY1QicHnzib6TCUnT0EMy4xOFHRNfBKiaBsagVIicudUe3JdiattP0/640?wx_fmt=png)

这个红色的提示吓了我一跳，不过只是没有配置，不用担心，这只是系统在告诉我们没配证书，完全不是报错。

因为我们配置了start\_action = start，服务重启后，隧道就像定了闹钟一样，已经自动建立起来了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZZEB9Crcgictg5rGLs9dcwtHVkvctdkqlqfUJKEp0EtWx4j0SeBM23IiaicWV3F2VwmEbibhHJlVY86nfZzfehvRJibKXriahcqClib48/640?wx_fmt=png)

可以看到，SA隧道已经协商成功，当前报文数据为零。如果你喜欢掌握主动权，想手工触发SA协商，也可以甩出这条命令：

```
swanctl --initiate --child host2host
```

发几个ping包测试一下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZbqZ1FKYB9kZjh5afyrDBztzSOlHech4SJq7ajAkETGPgMIOpHyCXnkLI89bNejibpnL4WrcjNRDQMlLDc71LMkeNHhKMGAXm8I/640?wx_fmt=png)

回看IPsec SA的隧道状态统计，in和out的报文数精准吻合，说明我们的业务流量已经丝滑地钻进IPsec隧道，被完美加密传输了。

最后，又到了喜闻乐见的压榨性能环节，我们再打个流测试一下性能。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZb1UnBo0IcRU8BMjy481V7JbfayQI4eVCqoHHyXw7HficJFmTPYNLKFmFFqw5Kvg96j9OgEQPcQVD0UxYcrNwKk9yuvLlmNB0u4/640?wx_fmt=png)

在动态省电模式下，平均带宽不足600 Mbps，最高带宽721 Mbps，考虑到加密算法带来的CPU算力开销，这个成绩也算中规中矩了。

从老旧的ipsec.conf到如今结构化、现代化的swanctl.conf，IPsec的配置逻辑正变得越来越清晰易读。对于网络工程师来说，拥抱这些新工具，不仅是为了紧跟技术潮流，更是为了减少排错时的内耗。

\*\*\*推荐阅读\*\*\*

[我们的WireGuard管理系统支持手机电脑了！全平台终端配置，支持扫码连接，一键搞定](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864213&idx=1&sn=ec85efce2a3b76ba244c71ccbdc09347&scene=21#wechat_redirect)

[保姆级教程：一条命令部署OpenVPN管理系统V4版，支持Win/Mac/安卓/iOS全平台接入](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864329&idx=1&sn=32eef6d6ce107136b389e05a4f206060&scene=21#wechat_redirect)

[成本省下99.7%！用40元的腾讯云服务器自建IPsecVPN，成功对接企业级飞塔防火墙](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864080&idx=1&sn=2de5d9d701d53b2c613b0c852329afb2&scene=21#wechat_redirect)

[别再乱选VPN了！实测数据告诉你：为什么L2TP是个...