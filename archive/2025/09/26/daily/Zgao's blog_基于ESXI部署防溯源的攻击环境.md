---
title: 基于ESXI部署防溯源的攻击环境
url: https://zgao.top/%e5%9f%ba%e4%ba%8eesxi%e9%83%a8%e7%bd%b2%e9%98%b2%e6%ba%af%e6%ba%90%e7%9a%84%e6%94%bb%e5%87%bb%e7%8e%af%e5%a2%83/
source: Zgao's blog
date: 2025-09-26
fetch_date: 2025-10-02T20:41:05.571422
---

# 基于ESXI部署防溯源的攻击环境

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 基于ESXI部署防溯源的攻击环境

* [首页](https://zgao.top)
* [基于ESXI部署防溯源的攻击环境](https://zgao.top:443/%E5%9F%BA%E4%BA%8Eesxi%E9%83%A8%E7%BD%B2%E9%98%B2%E6%BA%AF%E6%BA%90%E7%9A%84%E6%94%BB%E5%87%BB%E7%8E%AF%E5%A2%83/)

[9月 25, 2025](https://zgao.top/2025/09/)

### 基于ESXI部署防溯源的攻击环境

作者 [Zgao](https://zgao.top/author/zgao/)
在[[红蓝对抗](https://zgao.top/category/%E7%BA%A2%E8%93%9D%E5%AF%B9%E6%8A%97/)](https://zgao.top/%E5%9F%BA%E4%BA%8Eesxi%E9%83%A8%E7%BD%B2%E9%98%B2%E6%BA%AF%E6%BA%90%E7%9A%84%E6%94%BB%E5%87%BB%E7%8E%AF%E5%A2%83/)

![](https://zgao.top/wp-content/uploads/2025/09/image-7-1024x803.png)

最近这几年攻防对抗愈演愈烈，攻击队被溯源反制的案例也越来越多。我本身从事应急响应，想站在蓝队的视角，基于ESXI实现一套防溯源的攻击环境，本文的所有操作只需要在ESXI和Openwrt上配置。实现在隔离网段中创建的新机器无需任何配置，开机即用的效果。

文章目录

[ ]

* [需求分析](#%E9%9C%80%E6%B1%82%E5%88%86%E6%9E%90 "需求分析")
* [实现思路](#%E5%AE%9E%E7%8E%B0%E6%80%9D%E8%B7%AF "实现思路")
* [ESXI 虚拟设备配置](#ESXI_%E8%99%9A%E6%8B%9F%E8%AE%BE%E5%A4%87%E9%85%8D%E7%BD%AE "ESXI 虚拟设备配置")
  + [创建隔离虚拟交换机](#%E5%88%9B%E5%BB%BA%E9%9A%94%E7%A6%BB%E8%99%9A%E6%8B%9F%E4%BA%A4%E6%8D%A2%E6%9C%BA "创建隔离虚拟交换机")
  + [创建隔离网段端口组](#%E5%88%9B%E5%BB%BA%E9%9A%94%E7%A6%BB%E7%BD%91%E6%AE%B5%E7%AB%AF%E5%8F%A3%E7%BB%84 "创建隔离网段端口组")
  + [配置攻击网段中的OpenWrt](#%E9%85%8D%E7%BD%AE%E6%94%BB%E5%87%BB%E7%BD%91%E6%AE%B5%E4%B8%AD%E7%9A%84OpenWrt "配置攻击网段中的OpenWrt")
    - [Openwrt配置上网](#Openwrt%E9%85%8D%E7%BD%AE%E4%B8%8A%E7%BD%91 "Openwrt配置上网")
    - [安装依赖](#%E5%AE%89%E8%A3%85%E4%BE%9D%E8%B5%96 "安装依赖")
    - [部署 passwall2](#%E9%83%A8%E7%BD%B2_passwall2 "部署 passwall2")
    - [配置 passwall2](#%E9%85%8D%E7%BD%AE_passwall2 "配置 passwall2")
  + [Interface 配置](#Interface_%E9%85%8D%E7%BD%AE "Interface 配置")
  + [Firewall 配置](#Firewall_%E9%85%8D%E7%BD%AE "Firewall 配置")
    - [General Settings](#General_Settings "General Settings")
    - [Traffic Rules](#Traffic_Rules "Traffic Rules")
  + [端口转发](#%E7%AB%AF%E5%8F%A3%E8%BD%AC%E5%8F%91 "端口转发")
* [快照创建和还原](#%E5%BF%AB%E7%85%A7%E5%88%9B%E5%BB%BA%E5%92%8C%E8%BF%98%E5%8E%9F "快照创建和还原")
* [测试防溯源效果](#%E6%B5%8B%E8%AF%95%E9%98%B2%E6%BA%AF%E6%BA%90%E6%95%88%E6%9E%9C "测试防溯源效果")
  + [网段中添加新的虚拟机](#%E7%BD%91%E6%AE%B5%E4%B8%AD%E6%B7%BB%E5%8A%A0%E6%96%B0%E7%9A%84%E8%99%9A%E6%8B%9F%E6%9C%BA "网段中添加新的虚拟机")
  + [出口ip测试](#%E5%87%BA%E5%8F%A3ip%E6%B5%8B%E8%AF%95 "出口ip测试")
  + [PING & DNSLog](#PING_DNSLog "PING & DNSLog")
  + [webrtc泄露测试](#webrtc%E6%B3%84%E9%9C%B2%E6%B5%8B%E8%AF%95 "webrtc泄露测试")
* [总结](#%E6%80%BB%E7%BB%93 "总结")

## 需求分析

* 目的: 防溯源, 保证安全性。即便攻击主机被反制，也无法突破隔离网段。
* ESXI 划分隔离网段作攻击段 (10.10.10.1/24)
  + 攻击段(10.10.10.1/24) 禁止向生产网(192.168.5.1/24) 访问
  + 生产网白名单机器可访问攻击段
  + 要求新建机器无感配置，开机即用
  + 攻击段流量全部通过代理出网 + Fake DNS
  + 能在外网远程通过 zerotier rdp/ssh 到攻击段的机器
* 追求原生且性能
* 定期还原攻击机快照

## 实现思路

* **vSwitch-ISO** (虚拟交换机) 上联不绑定任何物理网卡 (完全隔离).
  + **vSwitch-ISO** 下端口组 **sword-ISO** 分配给攻击机群
* **vSwitch-Dev** 上联物理网卡
  + 端口组 **Dev-exit** 分配给生产机群
  + 端口组 **sword-exit** 分配给攻击机群出口网关 SwordTower2 (OpenWrt)
* 攻击网段流量出口顺序:
  + ESXI [攻击机器(NerworkAdapter: **sword-iso**) → SwordTower (→ Passwall2) → (sword-exit)] → vmnic0 → Internet

## ESXI 虚拟设备配置

### **创建隔离虚拟交换机**

新建一块虚拟交换机: **vSwitch-ISO**

* 修改如图安全设置, 适配安全环境
* 删除上联物理网卡

![](https://zgao.top/wp-content/uploads/2025/09/image-8.png)

> * 混杂模式(Promiscuous): 允许虚拟机看到所有流量，对于隔离网段应该拒绝，防止嗅探其他VM的流量。
> * MAC address changes (MAC地址更改): 某些虚拟机可能需要更改 MAC 地址 (如运行嵌套虚拟化或某些安全工具)
> * Forged transmits(伪造传输): 允许虚拟机发送源MAC地址与其配置MAC不同的帧

### **创建隔离网段端口组**

* 为刚新建的 vSwitch-ISO 创建端口组: sword-ISO
  + vlan: 0
  + 安全策略继承交换机
* 从 dev 出网交换机 vSwitch-Dev 创建端口组: sword-exit
  + vlan: 0
  + 安全策略继承交换机

![](https://zgao.top/wp-content/uploads/2025/09/image-9.png)

### 配置攻击网段中的OpenWrt

为保证安全性，本文选用Openwrt官方原生镜像，手动安装所需的插件。避免第三方Openwrt带来的不确定性安全问题。

#### Openwrt配置上网

为openwrt配置上网。暂时配一下. DHCP 或者静态配置，编辑 /etc/config/network。

```
config interface 'lan'
    option device 'eth0'
    option proto 'static'
    option ipaddr '192.168.3.209'
    option netmask '255.255.255.0'
    option gateway  '192.168.3.1'
    option dns      '8.8.8.8'
```

(可选步骤) 配置代理， 前提局域网中有一台可直接使用代理服务器。

```
export http_proxy="http://192.168.5.199:7893"
export https_proxy="http://192.168.5.199:7893"
export ftp_proxy="http://192.168.5.199:7893"
export all_proxy="socks5://192.168.5.199:7893"
```

#### 安装依赖

基本功能包

```
opkg update
opkg install opkg update && opkg install bash ca-bundle curl wget-ssl openssh-sftp-server htop nano vim unzip tar gzip bzip2 xz-utils coreutils coreutils-base64 diffutils file findutils grep sed gawk less lsof tcpdump ip-full ethtool rsync tmux screen block-mount e2fsprogs f2fsck mkf2fs fdisk parted lsblk blkid resize2fs dosfstools kmod-fs-ext4 kmod-fs-vfat kmod-fs-exfat dnsmasq-full firewall4 iptables-nft kmod-nft-tproxy kmod-nft-socket kmod-nft-nat kmod-tcp-bbr kmod-lib-zstd ds-lite ppp ppp-mod-pppoe bridge-utils netstat-nat luci luci-base luci-compat luci-app-firewall luci-app-package-manager luci-app-upnp luci-app-log-viewer luci-app-filemanager luci-lib-fs luci-lib-ipkg luci-proto-wireguard kmod-usb3 zram-swap
```

主题 (美观, UI 方便交互)

```
opkg install luci-compat
opkg install luci-lib-ipkg
wget --no-check-certificate https://github.com/jerrykuku/luci-theme-argon/releases/download/v2.3.2/luci-theme-argon_2.3.2-r20250207_all.ipk
opkg install luci-theme-argon*.ipk
```

![](https://zgao.top/wp-content/uploads/2025/09/image-10.png)

#### 部署 passwall2

> 对有一定用户基数的 op 透明代理插件搜集和研究后, 决定使用 passwall2 作为本文情景下的选项
>
> * 几乎所有主流协议
> * 高效, 速率, 稳定, 资源占用低, 支持透明代理
> * 对于高并发扫描等场景适配性好

passwall2 相关依赖在前文已经安装。特别注意 passwall2 需要 `dnsmasq-full`, 而 op 默认安装 `dnsmasq` 若后续查看到日志相关报错, 执行 `opkg install dnsmasq-full --force-overwrite`

```
# 启用服务
/etc/init.d/passwall2 enable

# 启动服务
/etc/init.d/passwall2 start

# 重启 uhttpd 以刷新 LuCI
/etc/init.d/uhttpd restart
```

#### 配置 passwall2

添加订阅地址，也就是机场的节点，作为攻击主机的出口ip。

* [Services] → [Passwall 2] → [Node Subscribe]
* 添加订阅链接后手动更新
  + 现在能看到 [Node List] 中显示节点并自动进行 TCP Ping 存活验证

![](https://zgao.top/wp-content/uploads/2025/09/image-11.png)

Other Settings, 设置透明代理和劫持

* [Passwall 2] → [Other Settings]
* 如图设置
  + 配置透明代理
    - 配置 ping 劫持
    - 更换 iptables 为 nftables (支持新 features 且性能更高)

![](https://zgao.top/wp-content/uploads/2025/09/image-12.png)

**注意：即使节点不支持 ipv6 也勾选. 防止 ip 泄露！**

勾选开关, 开启 passwall2

* [Services] → [Passwall2] → [Basic Settings]

![](https://zgao.top/wp-content/uploads/2025/09/image-13.png)
> 测试时发现 Localhost Proxy 勾选上后无法正常获取订阅, 后续也没有 OP 需要代理上网的场景; 故直接将选项取消了。
>
> 默认规则是 **[Xray\_shunt: 分流总节点]**, 当前场景下仅需要代理全流量. 可以直接选择单个节点作为出口

DNS防泄漏

* [Passwall 2] → [Other Settings]
* 作用:
  + op 作为攻击机的 DNSServer
  + 对 FakeDNS 进行设置, 防止外泄记录

![](https://zgao.top/wp-content/uploads/2025/09/image-14-1024x543.png)

### Interface 配置

* [Network] → [Interface] → [Interface]
* [General Settings] 中配置基本设置
  + 确保 [DHCP Server] 中, “Ignore interface” 取消勾选
    - 令其成为攻击机群 DHCP 服务器

![](https://zgao.top/wp-content/uploads/2025/09/image-15.png)
![](https://zgao.top/wp-content/uploads/2025/09/image-16-1024x681.png)

### Firewall 配置

* [Network] → [Firewall]

#### General Settings

配置如图：

![](https://zgao.top/wp-content/uploads/2025/09/image-17.png)

#### Traffic Rules

这里完成黑白名单等规则配置 为了方便区分, 用户自行添加规则前缀命名为 `Gandalf`。按照顺序进行添加 最先添加的规则将被排列到最后。

`Gandalf-DenyIN-ISO`: 阻止攻击网段通联生产段 + 阻止一般生产网段访问攻击网段

![](https://zgao.top/wp-content/uploads/2025/09/image-18.png)

`Gandalf-AllowIN-ISO`: 白名单; 允许生产网白名单机器 (图例: 192.168.5.99) 访问攻击网

![](https://zgao.top/wp-content/uploads/2025/09/image-19.png)

`Gandalf-AllowSSH-Tower`: 生产段白名单机器可访问攻击段 OP

![](https://zgao.top/wp-content/uploads/2025/09/image-20.png)

`Gandalf-DenyIn-ISO_22` & `Gandalf-DenyIn-ISO_80`: 黑名单, 禁止攻击段访问攻击段 OP 的 80 和 22

落地生产环境建议白名单做最小化开放, 让攻击段仅能访问 OP dns 等服务端口。

![](https://zgao.top/wp-content/uploads/2025/09/image-21.png)

### **端口转发**

这一步实现远程通过 zerotier → mstsc/ssh 连接到攻击机 远程机器 → 攻击段 OP [端口转发] → VM-ATT

![](https://zgao.top/wp-content/uploads/2025/09/image-22.png)

到这一步所有功能实现完成。

## 快照创建和还原

为尽可能保证攻击主机的环境干净，...