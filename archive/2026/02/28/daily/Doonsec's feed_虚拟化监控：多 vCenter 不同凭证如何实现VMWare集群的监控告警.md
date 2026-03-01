---
title: 虚拟化监控：多 vCenter 不同凭证如何实现VMWare集群的监控告警
url: https://mp.weixin.qq.com/s/fw9cBAJcWIpraS8ZygMXrA
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:21:56.123165
---

# 虚拟化监控：多 vCenter 不同凭证如何实现VMWare集群的监控告警

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/g74a60gOJFwgaGwZol87kvcic0GYyRGI6v5c89AQuTlIL9AnGHZ1Foblb5g7fc12FouugWWPMmhiaeXaGfHsEcT0hz0WldQVnY1wdbVznuEUg/0?wx_fmt=jpeg)

# 虚拟化监控：多 vCenter 不同凭证如何实现VMWare集群的监控告警

原创

小斐Lab
小斐Lab

网络小斐

![]()

在小说阅读器中沉浸阅读

**大家好，我是小斐呀。**

前面基于 **`VMWare vSphere`** 虚拟化集群做了一些监控适配， 但是有个问题一直没有解决，这次简单的把这个问题解决一下，以适配在采集多 **`VMWare vCenter`** 对象的时候可以基于不同的用户凭证实现采集，下面我就展开聊聊应该如何实现。

采集 **`VMWare vSphere`** 虚拟化指标简单推荐了几个采集器：

* **vmware\_exporter** 利用 **`vmware`** 官方维护的 **`pyvmomi`** 的 **`SDK`** 得到指标数据，但是该项目已不维护
* **Categraf** 和 **Telegraf** 支持采集 **`VMWare vSphere`** 基础指标
* **vmware-exporter** 利用 **`vmware`** 官方维护的 **`govmomi`** 的 **`SDK`** 得到指标数据

这里我继续以 **`vmware-exporter`** 采集器为案例展开说明，这个项目是 **`Fork`** 上游的 **`prezhdarov/vmware-exporter`** 我个人做的一些修改和适配，并生成发布 **`Linux`** 和 **`Windows`** 下的二进制可执行文件。

了解老版本的限制和使用详细可以看之前的一篇文章：

[虚拟化监控：内部VMWare虚拟化集群如何更好的监控运维](https://mp.weixin.qq.com/s?__biz=MzIzNjU5NDE2MA==&mid=2247489538&idx=1&sn=b31ba573b6ef7941e7a1358c2d78618c&scene=21#wechat_redirect)

下面我们基于这个采集器来做一下针对多 **`VMWare vCenter`** 且不同凭证的最佳实践。

## 监控部署

由于 **`vmware-exporter`** 采集器是主动暴露指标，故这里推荐使用 **`vmagent + VictoriaMetrics`** 组合，如果需要告警可以插入夜莺组建（图中并未呈现）。

![](https://mmbiz.qpic.cn/mmbiz_png/g74a60gOJFzfqabEnvjJJLf3zd38QuUl3pohQiaPDCTHTsua3tC4umMg3QqbG1ZHClm4LiajZjQboibmjqLA6g7obXJrm7pUR0QtwAImH9mmew/640?wx_fmt=png&from=appmsg)

所有的组件都部署完成后，就可以开始下载 **`vmware-exporter`** 二进制组件进行安装抓取测试了：

```
# 下载二进制版本
wget https://github.com/robotneo/vmware-exporter/releases/download/v0.1.17/vmware-exporter-v0.1.17-linux-amd64.tar.gz

# 解压到 /opt/vmware-exporter 目录
tar -zxvf vmware-exporter-v0.1.17-linux-amd64.tar.gz -C /opt/vmware-exporter
```

设置 **`system`** 管理服务：

```
cat /etc/systemd/system/vmware-exporter.service

[Unit]
Description=vmware-exporter is a simple prometheus exporter that collects various metrics from a vCenter.
After=network.target

[Service]
Type=simple
Restart=on-failure
RestartSec=5
EnvironmentFile=-/etc/vmware-exporter/vmware.conf
ExecStart=/opt/vmware-exporter/vmware-exporter -http.address=:9169 $ARGS
ExecStop=/bin/kill -s SIGTERM $MAINPID
ExecReload=/bin/kill -HUP $MAINPID
ProtectSystem=full
LimitNOFILE=1048576
LimitNPROC=1048576
LimitCORE=infinity
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=vmware-exporter

[Install]
WantedBy=multi-user.target
```

启动服务：

```
# 服务状态
sudo systemctl status vmware-exporter
# 服务器停止
sudo systemctl stop vmware-exporter
# 服务重启
sudo systemctl restart vmware-exporter
```

## 采集模式

**`vmware-exporter`** 采集器，支持单 **`vCenter`** 模式和多 **`vCenter`** 模式，在采集设置上有几个区别，下面看下都如何设置。

假设服务部署在服务器 **`192.168.10.10`** 地址下，那么我们首先可以在浏览器中打开 **`http://192.168.10.10:9169`** 端口服务，浏览器会显示如下信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g74a60gOJFwX27uTLkMGTOCGiaBfyMMCakeQibLRia0icib9dy84ATEj5wrfKr1ia5fibDNwVicFEpNKlvBcrGhPkf3ZvwOQzJibLJmyM6loJ0GHkuYI/640?wx_fmt=png&from=appmsg)

**单 `vCenter` 模式**：

指标端点默认： **`/metrics`**  用户名和密码需要放在启动参数之中，这里我主要是通过环境变量文件配置项来实现：

```
# 环境变量文件配置项
EnvironmentFile=-/etc/vmware-exporter/vmware.conf

# 编辑 /etc/vmware-exporter/vmware.conf

ARGS="-vmware.username=administrator@vsphere.local -vmware.password=public@123 -vmware.vcenter=172.16.10.1:443 -vmware.insecureTLS=true"

# 单节点 vCenter 的凭证配置好后并开启跳过 vSphere HTTPS 证书校验
# 重启服务
sudo systemctl restart vmware-exporter
```

打开浏览器点击 **`/metrics`** 查看单节点 **`vCenter`** 的指标信息，可以看到很多以 **`vmware_(datacenter/host/cluster/datastore/vm)_*`** 开头的指标数据，如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g74a60gOJFxKOB22sNRIUkkrBiaYpt1anll3ayLWk004N0rj3Ih47HwSIvciaX9d7ia5rLuXSN43wZzWucXKbfuPXeZEA8AYTX6Ueibjgav3ZCE/640?wx_fmt=png&from=appmsg)

那单节点 **`vCenter`** 在抓取的过程中应该如何配置，这里主要以 **`vmagent`** 作为抓取器：

```
scrape_configs:
  - job_name: "vmware-exporter"
    scrape_interval: 20s
    scrape_timeout: 15s
    metrics_path: /metrics
    # metrics_path: /probe
    static_configs:
      - targets:
        - '172.16.10.1'
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: 172.16.10.100:9169
```

**多 `vCenter` 模式**：

如果你有多个 **`vCenter`** 并且每个 **`vCenter`** 凭证还不一样，那我们应该如何应对呢，这里基于多 **`vCenter`** 并且凭证不同的做了一些基础修改，如何使用呢？

多凭证支持：

* 可以在 **`/probe`** 路径上使用 **`target`** 参数指定要抓取的 **`vCenter`** 主机。
* 所有指定的 **`vCenter`** 主机可不共享相同的用户名和密码。

```
scrape_configs:
  - job_name: 'vmware-vcenter'
    scrape_interval: 60s
    scrape_timeout: 55s
    metrics_path: /probe
    file_sd_configs:
      - files:
        - /etc/victoriametrics/vmagent/vmware_targets.yml
        # refresh_interval: 5m
    # 默认参数（可选）
    params:
      schema: ['https']
      insecure: ['true']
      collect[]: ['all'] # 启用所有 collectors
      # collect[]: ['datacenter', 'host', 'vm']  # 只监控主要指标
    relabel_configs:
      # 从标签中提取 username 并设置为 URL 参数
      - source_labels: [__meta_username]
        target_label: __param_username
      # 从标签中提取 password 并设置为 URL 参数
      - source_labels: [__meta_password]
        target_label: __param_password
      # 可选：从标签中提取 schema
      - source_labels: [__meta_schema]
        target_label: __param_schema
      # 可选：从标签中提取 insecure
      - source_labels: [__meta_insecure]
        target_label: __param_insecure
      # 将 target 设置为 vCenter 地址
      - source_labels: [__address__]
        target_label: __param_target
      # 设置 instance 标签
      - source_labels: [__param_target]
        target_label: instance
      # 将实际抓取地址设置为 exporter 地址
      - target_label: __address__
        replacement: 172.17.40.25:9169
      # 保留其他有用的标签（移除 __meta_ 前缀）
      - source_labels: [__meta_env]
        target_label: env
      - source_labels: [__meta_datacenter]
        target_label: datacenter
```

**`vmware_targets.yml`** 示例：

```
- targets:
  - 172.16.10.10
  # - vcenter1.example.com
  labels:
    __meta_username: 'administrator@vsphere.local'
    __meta_password: 'public@12345'
    __meta_schema: 'https'
    __meta_insecure: 'true'
    __meta_env: 'prod'  # 可删除
    __meta_datacenter: 'dc01' # 可删除

- targets:
  - 192.168.10.10
  # vcenter2.example.com
  labels:
    __meta_username: 'administrator@vsphere.local'
    __meta_password: 'public@54321'
    __meta_schema: 'https'
    __meta_insecure: 'true'
    __meta_env: 'prod'  # 可删除
    __meta_datacenter: 'dc02' # 可删除
```

这是基础配置，如果使用的是 **`Categraf`** 的话可以这样采集：

```
interval = 15

[[instances]]
  vcenter = "https://172.17.10.10"  # 这里不可带 /
  username = "administrator@vsphere.local"
  password = "public@54321"
  timeout = "60s"
  use_tls = true
  insecure_skip_verify = true

  ...

[[instances]]
  vcenter = "https://172.17.20.10"  # 这里不可带 /
  username = "administrator@vsphere.local"
  password = "public@12345"
  timeout = "60s"
  use_tls = true
  insecure_skip_verify = true

  ...
```

使用 **`categraf`** 采集的时候，采集指标配置可以根据需要采集，一般默认即可，单如果是多个 **`vCenter`** 就可以分多个 **`[[instances]]`** 即可。

## 可视化

面板可视化，都可以基于 **`Grafana`** 来实现，不管你是使用那个架构，最终我都推荐使用 **`Grafana`** 呈现：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g74a60gOJFyAic2zficOjc69ialB6xLQZewxPvJA5FpWmIibtgNog0XINIdqAt09OJsicMSibWasUuTRuOeH0ppmMKf2MeVRxwbNBbicEMhCwlBKjs/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/g74a60gOJFwMcqLaRaw2JH34TrMLoRntVgsKJJ9Wm27IJkIibZuyOA2Aibp9wmAibmoozxOvBsm6YJ6D5a4BZict9rPclqluPcCkLfzqrQriaxgY/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/g74a60gOJFxDZZrAEDVaG0iaAxiaVZ6ykqicr4qrES6bDz4f9hia6frWERkU6DEAQJCwUHLzYJAHN18oBkUXNl2VphPUuN9D12bzBrAg1ia28XRc/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/g74a60gOJFyTHHVGOOUG1IfzwgCnPlgKRzDwFlictibwyp5m3vU8T9emUVoh6xPicLUssryeHEibeVJJ9bicziaCDGa5LyI5eIUqkUicRZl6gdLSFU/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/g74a60gOJFyQPNqmTZzQ27EVcNpNqlDhCrjWHdkeNQzkibicOTrUuNmsziaylFwS5FRXa1BS3H5xamwibt8hmmM2JaRsZLn0rAHPqTIJicWFibaKc/640?wx_fmt=png&from=appmsg)

如果你是使用 **`Categraf`** 的话，可以基于我网盘中的面板修改对应的指标名称呈现即可，基本上指标名称都是一致的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g74a60gOJFwZFVWsZRJXU4XjoPicG683bgEdmRzibxgXD8dIicNN...