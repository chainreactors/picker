---
title: 安全防护之路——Suricata部署与测试
url: https://www.freebuf.com/articles/es/353548.html
source: FreeBuf网络安全行业门户
date: 2023-02-01
fetch_date: 2025-10-04T05:20:55.842070
---

# 安全防护之路——Suricata部署与测试

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

安全防护之路——Suricata部署与测试

* ![]()
* 关注

* [企业安全](https://www.freebuf.com/articles/es)

安全防护之路——Suricata部署与测试

2023-01-31 15:21:27

所属地 北京

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

[Suricata](https://suricata.io/)是一种网络流量识别工具，它使用社区创建的和用户定义的**signatures**签名集（规则）来检查和处理网络流量。当检测到可疑数据包时，Suricata 可以**触发警报或者丢弃流量**。

默认情况下，Suricata 用作入侵检测系统 (IDS)，以扫描服务器或网络上的可疑流量，生成并记录警报以供进一步调查。

同时，Suricata还可以配置为主动入侵防御系统 (IPS)，可以阻断符合特定规则的网络流量。

我们也可以在网络中核心网关上部署 Suricata 来扫描来自其他主机的所有流量。下面是本节的内容概述

* 在 Ubuntu 20.04 上安装 Suricata，并进行一些设置
* 导入 Suricata 的签名集（规则集）
* 测试 Suricata 配置，测试Suricata是否正常工作

> 配置需求：检查的流量越多，需要分配给 Suricata 的资源就越多。在生产环境中计划至少使用 2核CPU 和4~8GB 的内存，硬盘至少40G。

## 安装Suricata

将开放信息安全基金会 (OISF) 的软件存储库到Ubuntu 系统apt源里，运行以下命令：

```
sudo add-apt-repository ppa:oisf/suricata-stable
```

安装`suricata`软件包:

```
sudo apt install suricata
```

现在软件包已安装，启用`suricata.service`配置程序自启动

```
sudo systemctl enable suricata.service
```

如果收到如下输出，表明该服务已启用：

```
Outputsuricata.service is not a native service, redirecting to systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable suricata
```

在修改 Suricata 配置之前，先停止服务`systemctl`：

```
sudo systemctl stop suricata.service
```

## 配置 Suricata

OISF 存储库中的 Suricata 包附带了一个配置文件，该文件涵盖了各种用例。Suricata 的默认模式是 IDS 模式，因此不会拦截任何流量。

将 Suricata 配置并集成到真实的环境中时，可以考虑选择打开 IPS 模式。

* 启用社区流 ID

Suricata 可以在其 JSON 输出中包含社区 ID字段，以便将单个事件记录与**其他工具**生成的数据集中的记录进行匹配。（类似现在的态势感知，聚合分析）

编辑`/etc/suricata/suricata.yaml`的第 120 行`# Community Flow ID`其设置`true`为启用设置：

```
# Community Flow ID
      # Adds a 'community_id' field to EVE records. These are meant to give
      # records a predictable flow ID that can be used to match records to
      # output of other tools such as Zeek (Bro).
      #
      # Takes a 'seed' that needs to be same across sensors and tools
      # to make the id less predictable.

      # enable/disable the community id feature.
      community-id: true
```

现在，事件将具有类似`1:S+3BA2UmxxxxxFTtQ=`的 ID ，可以使用它来关联不同工具中的记录。

* 确定要使用的网卡

OISF Suricata 软件包附带的配置文件默认检查名为`eth0`. 如果使用不同的网卡，或者想检查多个网卡上的流量，则需要更改此值。

要确定默认网卡的设备名称，可以使用`ifconfig`或者`ip -p -j route show default`查看机器的网卡

```
[ {
        "dst": "default",
        "gateway": "192.168.xxx.254",
        "dev": "eno1",
        "protocol": "dhcp",
        "metric": 100,
        "flags": [ ]
    },{
        "dst": "default",
        "gateway": "192.168.xxx.1",
        "dev": "wlp3s0",
        "protocol": "dhcp",
        "metric": 600,
        "flags": [ ]
    } ]
```

可以看到我这台机器有`eno1`和`wlp3s0`两块网卡。编辑 Suricata 的配置，更改网卡名称。`/etc/suricata/suricata.yaml`

```
# Linux high speed capture support
af-packet:
  - interface: eth0
    # Number of receive threads. "auto" uses the number of cores
    #threads: auto
    # Default clusterid. AF_PACKET will load balance packets based on flow.
    cluster-id: 99
. . .
```

如果还想要检查其他接口上的流量，可以添加更多`- interface: eth...`YAML 对象。要添加一个新接口，将其插入到该`-interface: default`部分之前

```
#  For eBPF and XDP setup including bypass, filter and load balancing, please
    #  see doc/userguide/capture-hardware/ebpf-xdp.rst for more info.

  - interface: enp0s1
    cluster-id: 98

  - interface: default
    #threads: auto
    #use-mmap: no
    #tpacket-v3: yes
```

* 配置规则实时加载

Suricata 支持实时规则重新加载，这样无需重新启动正在运行的 Suricata 进程，就可以试试生效。要启用实时重新加载选项，在配置文件的底部并添加以下行：

/etc/suricata/suricata.yaml

```
. . .

detect-engine:
  - rule-reload: true
```

## 更新 Suricata 规则集

* 添加初始免费规则集

如果直接启动 Suricata，可能日志中收到如下警告消息，这表明还没有加载规则：

```
Output<Warning> - [ERRCODE: SC_ERR_NO_RULES(42)] - No rule files match the pattern /var/lib/suricata/rules/suricata.rules
```

Suricata 包含一个名为`suricata-update`的工具，可以从外部获取规则集。运行`sudo suricata-update`为 Suricata 服务器下载最新的规则集：

```
19/10/2021 -- 19:31:07 - <Info> -- Testing with suricata -T.
19/10/2021 -- 19:31:32 - <Info> -- Done.
```

以上的回显表示`suricata-update`已获取免费的Open Rules，并将它们保存到 Suricata 的`/var/lib/suricata/rules/suricata.rules`文件中。

* 添加规则集

`suricata-update`工具可以从各种免费和商业规则集提供者那里获取规则。某些规则集（例如已添加的 Open 集）可免费使用，而其他规则集则需要付费订阅。

可以使用`sudo suricata-update list-sources`列出默认的规则提供程序集，返回示例：

```
7/11/2022 -- 17:08:58 - <Info> -- Using data-directory /var/lib/suricata.
7/11/2022 -- 17:08:58 - <Info> -- Using Suricata configuration /etc/suricata/suricata.yaml
7/11/2022 -- 17:08:58 - <Info> -- Using /etc/suricata/rules for Suricata provided rules.
7/11/2022 -- 17:08:58 - <Info> -- Found Suricata version 6.0.6 at /usr/bin/suricata.
Name: et/open
  Vendor: Proofpoint
  Summary: Emerging Threats Open Ruleset
  License: MIT
Name: et/pro
  Vendor: Proofpoint
  Summary: Emerging Threats Pro Ruleset
  License: Commercial
  Replxces: et/open
  Parameters: secret-code
  Subscription: https://www.proofpoint.com/us/threat-insight/et-pro-ruleset
. . .
```

例如，如果想包含`tgreen/hunting`规则集，可以使用以下命令启用源：

`sudo suricata-update enable-source tgreen/hunting`

然后再运行`suricata-update`，将新添加的规则集导入到本地。

## 测试 Suricata 的配置文件

Suricata 有一个内置的测试模式，它将检查配置文件和任何包含的规则的有效性。`-T`使用标志在测试模式下运行 Suricata验证您在上一节中所做的更改。`-v`标志将打印一些附加信息，`-c`标志告诉 Suricata 在哪里可以找到其配置文件：

```
sudo suricata -T -c /etc/suricata/suricata.yaml -v
```

测试花费的时间具体取决于分配给 Suricata 的 CPU 数量和添加的规则数量。使用默认的Open 规则集，应该会收到如下输出：

```
7/11/2022 -- 17:10:18 - <Info> - 1 rule files processed. 27200 rules successfully loaded, 0 rules failed
7/11/2022 -- 17:10:18 - <Info> - Threshold config parsed: 0 rule(s) found
7/11/2022 -- 17:10:18 - <Info> - 27203 signatures processed. 1280 are IP-only rules, 4612 are inspecting packet payload, 21107 inspect application layer, 108 are decoder event only
7/11/2022 -- 17:10:24 - <Notice> - Configuration provided was successfully loaded. Exiting.
7/11/2022 -- 17:10:24 - <Info> - cleaning up signature grouping structure... complete
```

如果配置文件中有错误，那么测试模式将生成一个特定的错误代码和消息，可以用来帮助排除故障。

Suricata 测试模式运行成功完成，就可以进入下一步，启动 Suricata。

## 运行 Suricata

现在 Suricata 配置和规则集都OK了，可以启动 Suricata 服务器。运行：`sudo systemctl start suricata.service`

可以使用`sudo systemctl status suricata.service`命令检查服务的状态：

如下输出：

```
● suricata.service - LSB: Next Generation IDS/IPS
     Loaded: loaded (/etc/init.d/suricata; generated)
     Active: active (running) since Tue 2022-08-30 16:27:51 CST; 2 months 8 days ago
       Docs: man:systemd-sysv-generator(8)
      Tasks: 22 (limit: 18766)
     Memory: 2.7G
     CGroup: /system.slice/suricata.service
             └─35050 /usr/bin/suricata -c /etc/suricata/suricata.yaml --pidfile /var/run/suricata.pid --af-packet -D -vvv
```

与测试模式命令一样，Suricata 需要一两分钟来加载和解析所有规则。现在 Suricata 正常运行了，下一步是检查 Suricata 是否检测到测试 URL 的请求并生成警报。

## 测试 Suricata 规则

前面下载的Open 规则集包含超过 30000 条规则。[Suricata 快速入门](https://suricata.readthedocs.io/en/latest/quickstart.html#alerting)建议使用`curl`发一些包，来触发`2100498`规则。

运行`curl http://testmynids.org/uid/index.html`生成一个 HTTP 请求，该请求将返回一个匹配 Suricata 警报规则的响应：

```
Outputuid=0(root) gid=0(root) groups=0(root)
```

此示例响应数据会触发警报，假装返回通过 webshell 在受感染的远程系统上运行`id`命令的输出。

现在可以检查 Suricata 的日志，看看有没有触发告警。默认 Suricata 配置启用了两个日志。第一个是在`/var/log/suricata/fast.log`，第二个是json的`/var/log/suricata/eve.log`。

**/var/log/suricata/fast.log**

输入`grep 2100498 /var/log/suricata/fast.log` 检查报警日志

```
Output10/21/2021-18:35:57.247239  [**] [1:2100498:7] GPL ATTACK_RESPONSE id check returned root [**] [Classificatio...