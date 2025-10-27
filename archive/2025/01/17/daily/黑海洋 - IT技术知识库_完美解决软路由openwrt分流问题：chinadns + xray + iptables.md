---
title: 完美解决软路由openwrt分流问题：chinadns + xray + iptables
url: https://blog.upx8.com/4665
source: 黑海洋 - IT技术知识库
date: 2025-01-17
fetch_date: 2025-10-06T20:10:57.493414
---

# 完美解决软路由openwrt分流问题：chinadns + xray + iptables

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 完美解决软路由openwrt分流问题：chinadns + xray + iptables

发布时间:
2025-01-16

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
91895

在过去，我选择使用 ssrp 插件来实现代理上网。但在实际使用过程中，总会遇到一些特定网站无法正常访问的情况，无奈之下只能临时在浏览器中手动设置代理，以此来解决访问问题，可这着实麻烦。

后来，我了解到像 passwall、openclash 等较为新颖的方案，理论上能够更高效地解决代理相关问题。然而，由于我使用的软路由设备较为老旧，系统和硬件都存在一定局限性。这些新方案对环境依赖较多，在我的软路由上安装时会面临重重困难，很可能因依赖不兼容而无法成功。同时，刷机操作也存在巨大风险，一旦刷机失败，就可能导致设备炸机，进而出现断网的情况，给我的网络使用带来极大不便。权衡再三，我决定不再进行这些复杂的尝试 。

于是，我另辟蹊径，通过 iptables 自行创建规则来设置代理并实现分流。没想到这个方法不仅成功解决了我的网络问题，还拥有更高的自由度，能根据自己的实际需求灵活调整网络访问策略，极大地提升了我的网络使用体验。

       首先介绍我想最终达到的目的，以便判断能否和你需求匹配。再去简单介绍下所用的程序。

**大陆 IP/网站直连 + 海外域名/IP 全部走代理 + 部分海外白名单域名直连**

* 大陆网站/IP 直连：无论是通过域名解析的大陆 IP，还是某些应用程序硬编码的 IP 或者其他方式下发的大陆 IP 进行直连。
* 海外域名/IP 全部走代理：无论在不在 gfwlist 的域名，包括任何海外 IP 走代理。
* 部分海外白名单域名直连：包括 pt tracker 域名、需要直连的服务器域名，即使 IP 在海外也能够直连。(和上条冲突，例外)

这里就不一步步写我的测试和部署逻辑了，直接附上最终可用的成果，过程中遇到的问题将在最后问题列表追加解析。

## chinadns

我的 dns 解析程序选择使用 chinadns 来处理国内域名和海外域名，通过设置两个不同的 DNS 解析服务器，分别解析来避免得到污染过的 IP 地址。

国内域名可以以最快的速度从 dnspod 拿到有效解析，海外域名也能够从 1.1.1.1 拿到正确没有污染的 IP 地址。

选用它，是因为配置文件比 smartdns 简单，单文件体积也小很多。

只是这个程序作者写的文档不是很明白，处于初次接触的人很难快速搞明白解析逻辑和配置文件的逻辑，后面我将以简单的方式告知你。

下载，可根据你的实际情况选择对应的二进制文件

[https://github.com/zfl9/chinadns-ng/releases](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3pmbDkvY2hpbmFkbnMtbmcvcmVsZWFzZXM)

```
wget https://github.com/zfl9/chinadns-ng/releases/download/2024.12.22/chinadns-ng+wolfssl@x86_64-linux-musl@x86_64_v2@fast+lto
mv chinadns-ng+wolfssl@x86_64-linux-musl@x86_64_v2@fast+lto /usr/bin/chinadns
chmod +x /usr/bin/chinadns
```

/etc/chinadns/config.conf

```
# 监听地址和端口
bind-addr 0.0.0.0
bind-port 5335

# 国内上游、可信上游
china-dns 119.29.29.29
trust-dns tcp://1.1.1.1

# 域名列表，用于分流
chnlist-file /etc/chinadns/chnlist.txt
gfwlist-file /etc/chinadns/gfwlist.txt
# chnlist-first

group white
group-dnl /etc/chinadns/white.txt
group-upstream 1.0.0.1
group-ipset whiteip

# 收集 tag:chn、tag:gfw 域名的 IP
add-tagchn-ip chnip,chnip6
add-taggfw-ip gfwip,gfwip6

# 用于测试 tag:none 域名的 IP (国内上游)
ipset-name4 chnroute
ipset-name6 chnroute6

# dns 缓存
cache 4096
cache-stale 86400
cache-refresh 20

# verdict 缓存 (用于 tag:none 域名)
verdict-cache 4096

no-ipv6 tag:none@ip:non_china
no-ipv6 tag:gfw
```

white.txt

```
tracker.m-team.cc
daydream.dmhy.best
```

### 配置解析

china-dns 119.29.29.29 配置大陆域名解析上游、trust-dns tcp://1.1.1.1 配置 gfwlist 域名和**其他域名**解析上游

**大陆域名、gfw 域名来源是什么？**

答： chnlist-file /etc/chinadns/chnlist.txt 来源于这个配置文件，同样 gfwlist.txt 是 gfw 域名来源。

**海外域名、其他域名来源是什么?**

答：不在大陆域名列表的网站、不在 gfwlist 的域名有非常之多，所以当域名都不在上述列表时，将通过两台服务器分别查询。

* 如果 IP 在大陆，则 DNS 回答响应大陆 IP。

* 如果 IP 在海外，则 DNS 回答响应 海外 IP。
* 如果两台服务器解析都不一样，则以海外输出的 IP 为准，以避免大陆 DNS 污染的问题，这也就是配置项为什么是 trust-dns（信任的 DNS 上游） 。

**收集 IP 功能是什么？**

比如配置中的 add-tagchn-ip chnip,chnip6，是将大陆域名的解析结果存入 ipset 中，如果是 IPV4 则存进 chnip，如果是 IPV6 则进 chnip6.

add-taggfw-ip 同理。

**需要注意：add-tagchn-ip 和 add-taggfw-ip 这两个参数项是固定用法，不是可变的，比如 add-tagwhite-ip 这个是错误的。**

将 IP 收集起来后，你就可以使用 iptables 进行一些代理或者放行操作。

**ipset-name 是什么？**

ipset-name4 chnroute 和 ipset-name6 chnroute6 所配置的值都是一个 ipset 集合名字。

它预设了一些大陆的 IP 段，程序将域名解析成 IP 后，要通过与这个 chnroute 集合匹配，如果匹配上了则代表这是大陆的 IP，如果没有匹配上则它就是海外 IP，来决定是否将这个 IP 写入 chnip ，进而去分流。

**tag:是什么？**

比如 tag 是程序内置的一种标签集合表达方式

固定的有：

* tag:gfw 来源于 gfwlist-file 配置的域名列表
* tag:chn 来源于 chnlist-file 配置的域名列表。
* 还有 tag:none 是即不属于任意 tag 的域名列表。

可变的有：

* tag:white 比如上文配置中 white 就是由 group {name} 去配置的名字，才能在后面配置中引用。属于自定义组/tag 配置。

**no-ipv6 如何配置？**

这里配置的是想要忽略 ipv6 解析的规则列表。

大陆域名希望直连，哪怕 IPV6 速度也不慢，也为了能够远程连接穿透等需求这里希望能够正确返回 IPV6。所以这里不能配置 no-ipv6。

海外域名希望屏蔽 IPV6，因为海外 IPV6 路由很差劲，二者服务器也不一定能够支持 IPV6，所以在这里全部屏蔽。

白名单域名希望能够直连，因为这里是 pt tracker 希望服务端能够正确识别到本机的 IPV4 和 IPV6 而不是代理服务器，但这里实际 IP 又是海外的，所以有一些冲突。

最终的配置解答

* no-ipv6 tag:gfw 忽略 gfw 域名中所有 IPV6 解析。
* no-ipv6 tag:none@ip:non\_china 忽略 none 域名列表中且 IP 解析是非大陆的 IP。

tag:none 是一个特殊的组/tag，它是不存在于任何预设组的列表，即不存在于（chnlist, gfwlist, white.txt）的组。

这里的逻辑是反向的，理解起来有点别扭。

原本需求和配置的关系变成了：

海外所有 IP 忽略 IPV6 (但 white.txt 例外) = gfwlist + none (海外 IP)

**到这一步，先忽略后面的代理和路由。域名匹配都能够完成正确解析。**

举例说明：

* 查询 taobao.com 响应大陆 IP 和 大陆 IPV6，通过 dnspod 解析，后续也会直连。
* 查询 google.com 响应海外 IP，没有 IPV6，通过 1.1.1.1 解析，因为在 gfwlist 中，被 no-ipv6 忽略。
* 查询 tracker.m-team.cc 响应海外 IP 和海外 IPV6，通过 1.1.1.1 解析，后续也会直连，因为在 white.txt 配置了，没有经过 no-ipv6 处理。

### 启动服务

/etc/init.d/chinadns

```
#!/bin/sh /etc/rc.common
START=01
STOP=90
USE_PROCD=1
PROG=/usr/bin/chinadns
start_service(){
         procd_open_instance [chinadns]
         procd_set_param command /usr/bin/chinadns # service executable that has to run in **foreground**.
         procd_append_param command --config /etc/chinadns/config.conf # append command parameters

         procd_set_param respawn ${respawn_threshold:-3600} ${respawn_timeout:-5} ${respawn_retry:-5}

         procd_set_param limits core="unlimited"  # If you need to set ulimit for your process
         procd_set_param file /etc/chinadns/config.conf # /etc/init.d/your_service reload will restart the daemon if these files have changed
         procd_set_param stdout 1 # forward stdout of the command to logd
         procd_set_param stderr 1 # same for stderr
         procd_set_param user root # run service as user nobody
         #procd_set_param user nobody # run service as user nobody
         procd_set_param pidfile /var/run/chinadns.pid # write a pid file on instance start and remove it  on stop
         procd_set_param term_timeout 60 # wait before sending SIGKILL
         procd_close_instance
}
```

启动和开机自启

```
chmod +x /etc/init.d/chinadns
/etc/init.d/chinadns start
/etc/init.d/chinadns enable
```

## xray

很强的多合一代理程序，不必多介绍。这里主要是讲解客户端的使用方式，服务器你可以使用任意常见稳定的代理程序，两边都是 xray 也可以。

我的分流规则也都是参考 xray 来的，客户端粘性很高。

下载 xray

```
mkdir /etc/chinadns/xray
cd /etc/chinadns/xray && wget https://github.com/XTLS/Xray-core/releases/download/v24.12.18/Xray-linux-64.zip
unzip Xray-linux-64.zip
```

/etc/chinadns/xray/config.json

```
{
    "log": {
        "loglevel": "warning",
        "access": "none",
        "error": "error.log"
    },
    "routing": {
        "domainStrategy": "AsIs",
        "rules": [{
                "type": "field",
                "inboundTag": ["all-in"],
                "port": 53,
                "outboundTag": "dns-out"
            }, {
                "type": "field",
                "ip": [
                    "geoip:private"
                ],
                "outboundTag": "block"
            }, {

                "type": "field",
                "domain": [
                    "geosite:category-ads-all"
                ],
                "outboundTag": "block"
            }

        ]
    },
    "inbounds": [{
            "port": 12345,
            "protocol": "dokodemo-door",
            "settings": {
                "network": "tcp,udp",
                "followRedirect": true
            },
            "streamSettings": {
                "sockopt": {
                    "tproxy": "tproxy"
                }
            }
        }, {
            "tag": "http2",
            "port": 5556,
            "listen": "0.0.0.0",
            "protocol": "http",
            "sniffing": {
                "enabled": true,
                "destOverride": [
                    "http",
                    "tls"
                ]
            },
            "settings": {
                "auth": "noauth",
                "udp": true,
                "allowTransparent": false
            }
        }, {
            "tag": "socks",
            "port": 5555,
            "listen": "0.0.0.0",
            "protocol": "socks",
            "sniffing": {
                "enabled": true,
                "destOverride": [
                    "http",
                    "tls"
                ]
            },
            "settings": {
                "auth": "noauth",
                "udp": true,
                "allowTransparent": false
            }
        }
    ],
    "outbounds": [{
            "tag": "proxy",
            "protocol": "vmess",
            "settings": {
                "vnext": [{
                        "address": "...