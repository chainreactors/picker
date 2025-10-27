---
title: Zerotier + Openwrt异地组网高阶配置
url: https://zgao.top/zerotier-openwrt%e5%bc%82%e5%9c%b0%e7%bb%84%e7%bd%91%e9%ab%98%e9%98%b6%e9%85%8d%e7%bd%ae/
source: Zgao's blog
date: 2025-02-10
fetch_date: 2025-10-06T20:32:33.357087
---

# Zerotier + Openwrt异地组网高阶配置

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# Zerotier + Openwrt异地组网高阶配置

* [首页](https://zgao.top)
* [Zerotier + Openwrt异地组网高阶配置](https://zgao.top:443/zerotier-openwrt%E5%BC%82%E5%9C%B0%E7%BB%84%E7%BD%91%E9%AB%98%E9%98%B6%E9%85%8D%E7%BD%AE/)

[2月 9, 2025](https://zgao.top/2025/02/)

### Zerotier + Openwrt异地组网高阶配置

作者 [Zgao](https://zgao.top/author/zgao/)
在[[安全运维](https://zgao.top/category/%E5%AE%89%E5%85%A8%E8%BF%90%E7%BB%B4/)](https://zgao.top/zerotier-openwrt%E5%BC%82%E5%9C%B0%E7%BB%84%E7%BD%91%E9%AB%98%E9%98%B6%E9%85%8D%E7%BD%AE/)

![](https://zgao.top/wp-content/uploads/2025/02/image-1024x653.png)

和朋友一起协同开发，需要打通双方的局域网互访，所以考虑到vpn的场景。一开始考虑frp+openvpn的实现。frp实现点对点穿透，openvpn负责组网。但是感觉这样配置较为繁琐，双方都需要部署frp和openvpn，体验不是很友好。

探索了多种方案最终选择了Zerotier，一个自带P2P打洞的vpn，同时满足需要。只需要自建一台有公网ip的moon服务器就可以高效实现各个zerotier节点之间的打洞。

文章目录

[ ]

* [注册Zerotier](#%E6%B3%A8%E5%86%8CZerotier "注册Zerotier")
* [部署Zerotier Moon服务器](#%E9%83%A8%E7%BD%B2Zerotier_Moon%E6%9C%8D%E5%8A%A1%E5%99%A8 "部署Zerotier Moon服务器")
* [客户端加入Zerotier网络并连接Moon](#%E5%AE%A2%E6%88%B7%E7%AB%AF%E5%8A%A0%E5%85%A5Zerotier%E7%BD%91%E7%BB%9C%E5%B9%B6%E8%BF%9E%E6%8E%A5Moon "客户端加入Zerotier网络并连接Moon")
* [进阶玩法：Openwrt安装Zerotier](#%E8%BF%9B%E9%98%B6%E7%8E%A9%E6%B3%95%EF%BC%9AOpenwrt%E5%AE%89%E8%A3%85Zerotier "进阶玩法：Openwrt安装Zerotier")
* [OpenWrt 上配置 ZeroTier 网络间路由](#OpenWrt_%E4%B8%8A%E9%85%8D%E7%BD%AE_ZeroTier_%E7%BD%91%E7%BB%9C%E9%97%B4%E8%B7%AF%E7%94%B1 "OpenWrt 上配置 ZeroTier 网络间路由")
* [ZeroTier 管理界面配置路由](#ZeroTier_%E7%AE%A1%E7%90%86%E7%95%8C%E9%9D%A2%E9%85%8D%E7%BD%AE%E8%B7%AF%E7%94%B1 "ZeroTier 管理界面配置路由")
* [在没有安装Zerotier的设备上实现局域网路由转发](#%E5%9C%A8%E6%B2%A1%E6%9C%89%E5%AE%89%E8%A3%85Zerotier%E7%9A%84%E8%AE%BE%E5%A4%87%E4%B8%8A%E5%AE%9E%E7%8E%B0%E5%B1%80%E5%9F%9F%E7%BD%91%E8%B7%AF%E7%94%B1%E8%BD%AC%E5%8F%91 "在没有安装Zerotier的设备上实现局域网路由转发")
* [树莓派成功加入网络但是没有networks显示](#%E6%A0%91%E8%8E%93%E6%B4%BE%E6%88%90%E5%8A%9F%E5%8A%A0%E5%85%A5%E7%BD%91%E7%BB%9C%E4%BD%86%E6%98%AF%E6%B2%A1%E6%9C%89networks%E6%98%BE%E7%A4%BA "树莓派成功加入网络但是没有networks显示")
* [如何更换设备的zerotier 节点ID？](#%E5%A6%82%E4%BD%95%E6%9B%B4%E6%8D%A2%E8%AE%BE%E5%A4%87%E7%9A%84zerotier_%E8%8A%82%E7%82%B9ID%EF%BC%9F "如何更换设备的zerotier 节点ID？")
* [查看zerotier各个节点之间的情况](#%E6%9F%A5%E7%9C%8Bzerotier%E5%90%84%E4%B8%AA%E8%8A%82%E7%82%B9%E4%B9%8B%E9%97%B4%E7%9A%84%E6%83%85%E5%86%B5 "查看zerotier各个节点之间的情况")
* [Zerotier的优缺点](#Zerotier%E7%9A%84%E4%BC%98%E7%BC%BA%E7%82%B9 "Zerotier的优缺点")

## 注册Zerotier

<https://my.zerotier.com/network>

![](https://zgao.top/wp-content/uploads/2025/02/image-2-1024x544.png)

创建一个网络后，记下network ID。后面其他zerotier的客户端需要先加入这个ID才能进入这个vpn网络中。

![](https://zgao.top/wp-content/uploads/2025/02/image-11-1024x638.png)

可以根据需要自行修改，不然每次要登录官网同意才行。

## 部署Zerotier Moon服务器

因为Zerotier官方的根服务器是在国外的，如果不自建Moon服务器，P2P打洞的效率会非常低。这里随便开一台有公网ip的云服务器部署zerotier Moon服务即可。

```
# 安装
curl -s https://install.zerotier.com | sudo bash

# 启动服务
sudo systemctl start zerotier-one
sudo systemctl enable zerotier-one

# 生成随机的 root 身份令牌
sudo zerotier-idtool generate identity.secret identity.public
```

配置 controller

```
# 创建配置目录
sudo mkdir -p /var/lib/zerotier-one/controller.d

# 配置身份信息
sudo cp identity.secret /var/lib/zerotier-one/
sudo cp identity.public /var/lib/zerotier-one/

# 启用 controller 功能
echo '{"settings":{"primaryPort":9993},"controller":true}' | sudo tee /var/lib/zerotier-one/local.conf

# 重启服务
sudo systemctl restart zerotier-one
```

创建Moon配置

```
cd /var/lib/zerotier-one
sudo zerotier-idtool initmoon identity.public > moon.json
```

编辑上一步生成的 `moon.json` 文件中的 `roots` 部份，向 `roots.stableEndpoints` 部份添加当前云服务器的公网ip和端口信息。

![](https://zgao.top/wp-content/uploads/2025/02/image-12-1024x379.png)

```
sudo zerotier-idtool genmoon moon.json
sudo mkdir moons.d
sudo mv *.moon moons.d/
systemctl restart zerotier-one
zerotier-cli info
```

![](https://zgao.top/wp-content/uploads/2025/02/image-4-1024x489.png)

注意：zerotier默认是9993端口，需要在云控制台放行这个端口。

## 客户端加入Zerotier网络并连接Moon

<https://www.zerotier.com/download/>

![](https://zgao.top/wp-content/uploads/2025/02/image-5-1024x570.png)

以Linux / Macos 命令行为例。先在ZeroTier官网获取该网络的16位网络ID，加入网络。

```
zerotier-cli join <16位网络ID>
```

让客户端连接到我们自建的moon服务器。这里使用moon ID两次是正确的。

```
zerotier-cli orbit <MoonID> <MoonID>
```

如何判断有没有加入成功？大概等待10s左右执行命令。

```
zerotier-cli listmoons
zerotier-cli listpeers
```

![](https://zgao.top/wp-content/uploads/2025/02/image-6-1024x583.png)

```
ifconfig
```

![](https://zgao.top/wp-content/uploads/2025/02/image-7-1024x691.png)

## 进阶玩法：Openwrt安装Zerotier

在单台主机上安装Zerotier只能实现两个远程局域网中的节点互相通信，怎么才能实现两个局域网的所有主机互相访问呢？

![](https://zgao.top/wp-content/uploads/2025/02/image-8-1024x599.png)

然后在界面中输出之前的network ID，但是界面上是不支持添加MoonID的。

![](https://zgao.top/wp-content/uploads/2025/02/image-9-1024x742.png)

需要打开openwrt的ssh，通过命令行添加。

```
zerotier-cli orbit <MoonID> <MoonID>
```

## OpenWrt 上配置 ZeroTier 网络间路由

首先启用 IP 转发（OpenWrt 默认已启用）。

```
cat /proc/sys/net/ipv4/ip_forward
```

如果输出为 1 则说明已启用。添加正确的防火墙区域和转发规则。

```
# 添加 ZeroTier 区域
uci add firewall zone
uci set firewall.@zone[-1].name='zt_network'
uci set firewall.@zone[-1].network='zthnhcbyru'
uci set firewall.@zone[-1].input='ACCEPT'
uci set firewall.@zone[-1].output='ACCEPT'
uci set firewall.@zone[-1].forward='ACCEPT'
uci set firewall.@zone[-1].masq='1'

# 添加转发规则
uci add firewall forwarding
uci set firewall.@forwarding[-1].src='zt_network'
uci set firewall.@forwarding[-1].dest='lan'

uci add firewall forwarding
uci set firewall.@forwarding[-1].src='lan'
uci set firewall.@forwarding[-1].dest='zt_network'

# 提交更改
uci commit firewall

# 重启防火墙
/etc/init.d/firewall restart
```

检查防火墙状态和查看当前的 nftables 规则。

```
/etc/init.d/firewall status
nft list ruleset
```

## ZeroTier 管理界面配置路由

在 “Managed Routes” 添加路由：

* Destination: 192.168.3.0/24
* Via: 10.242.250.229 ( OpenWrt 的 ZeroTier IP)

![](https://zgao.top/wp-content/uploads/2025/02/image-10-1024x577.png)

```
# 从其他 ZeroTier 设备尝试 ping OpenWrt 的 LAN IP
ping 192.168.3.199
```

在openwrt上和Zerotier的官网上同时完成路由转发规则的配置后，就可以在对端局域网访问当前局域网中所有的ip资源了，而不是单纯的节点之间的点对点访问。

## 在没有安装Zerotier的设备上实现局域网路由转发

文章首页的图里面，我在家中使用树莓派安装Zerotier作为中转的设备，而不是在macbook上安装Zerotier，这个时候理论上只有树莓派才可以访问对端的局域网，而我的macbook是不行的。

但也可以实现，需要在树莓派上配置 IP 转发和防火墙规则，让它作为网关转发流量。

在树莓派上启用 IP 转发

```
# 临时启用
echo 1 > /proc/sys/net/ipv4/ip_forward

# 永久启用，编辑 /etc/sysctl.conf 添加
net.ipv4.ip_forward=1

# 应用更改
sysctl -p
```

在树莓派上添加 iptables 规则。

```
# 允许从本地网络到 ZeroTier 网络的转发
iptables -A FORWARD -i eth0 -o zthnhcbyru -j ACCEPT

# 允许从 ZeroTier 网络返回到本地网络的流量
iptables -A FORWARD -i zthnhcbyru -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT

# 启用 NAT
iptables -t nat -A POSTROUTING -o zthnhcbyru -j MASQUERADE
```

保存 iptables 规则，下次重启仍然生效。

```
apt-get install iptables-persistent
netfilter-persistent save
```

在 macbook 上添加路由（需要管理员权限）。

```
sudo route add -net 192.168.3.0/24 10.242.36.70
```

这样配置后，macbook 就可以通过树莓派访问到对端的 192.168.3.0/24 网段了。

## 树莓派成功加入网络但是没有networks显示

![](https://zgao.top/wp-content/uploads/2025/03/image-29-1024x550.png)

`/dev/net/tun` 存在吗？ 如果没有，需要在 linux 内核中加载 TUN/TAP 模块，可能需要通过

```
sudo modprobe tun
```

对于树莓派不会在开机加载这个，就会导致失败。需要手动执行一次。

## 如何更换设备的zerotier 节点ID？

```
# 停止ZeroTier服务
sudo systemctl stop zerotier-one

# 删除身份文件
sudo rm /var/lib/zerotier-one/identity.public
sudo rm /var/lib/zerotier-one/identity.secret

# 重启ZeroTier服务
sudo systemctl start zerotier-one

# 验证是否生成新ID
zerotier-cli info
```

注意事项：

* 这将生成一个新的节点ID
* 所有已加入的网络需要重新授权
* 现有的网络连接会断开

## 查看zerotier各个节点之间的情况

```
 # zerotier-cli peers
200 peers
<ztaddr>   <ver>  <role> <lat> <link>   <lastTX> <lastRX> <path>
0a93d3c438 1.14.2 LEAF      37 DIRECT   10142    10142    183.14.134.157/24353
44921b0ca0 1.14.2 LEAF      69 DIRECT   11430    11362    2408:8278:c985:46b0:6b:e77f:fa0a:8d1b/21208
5f21a301bf 1.14.2 MOON      16 DIRECT   1319     1303     1.99.188.70/9993
61e104917e 1.14.2 LEAF      -1 RELAY
7511d5519a 1.14.2 LEAF      -1 RELAY
778cde7190 -      PLAN...