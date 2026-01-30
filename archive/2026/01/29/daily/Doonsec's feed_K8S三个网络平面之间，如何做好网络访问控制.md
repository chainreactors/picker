---
title: K8S三个网络平面之间，如何做好网络访问控制
url: https://mp.weixin.qq.com/s/SMP8gS58Tq3tPqT5VcDdaw
source: Doonsec's feed
date: 2026-01-29
fetch_date: 2026-01-30T04:01:44.196095
---

# K8S三个网络平面之间，如何做好网络访问控制

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cuBApO3XWpRYX75dT2RcCjxl9BtuXWiaDF0BCXLFOZqZInyoVxTibpvJk8jwsV0ibEl3JxXPNrIf954IMWABxcypA/0?wx_fmt=jpeg)

# K8S三个网络平面之间，如何做好网络访问控制

原创

Hash先生
Hash先生

倬其安

![]()

在小说阅读器中沉浸阅读

#

#

在K8s集群中，宿主机、节点、Pod三个网络平面的“独立隔离”是安全基础，但业务运行离不开必要的跨平面通信。核心原则是：**先明确平面边界，再按“最小必须”开通互访策略**——既保障业务连通性，又阻断非必要访问，从源头减少攻击面。

## 一、三个网络平面的核心区别与联系

### （一）核心区别：从4个维度划清边界

| 对比维度 | 宿主机网络平面 | 节点网络平面（虚拟机/物理机） | Pod网络平面 |
| --- | --- | --- | --- |
| 定位与载体 | 物理服务器的原生网络，底层硬件网络 | K8s计算单元的网络，载体是虚拟机/物理机 | 容器的逻辑网络，载体是K8s的Pod |
| 网段规划 | 物理网络独立网段（如192.168.1.0/24），静态分配 | 虚拟化/物理网络独立网段（如10.0.0.0/16），由虚拟化平台/K8s分配 | CNI插件专属网段（如172.16.0.0/12），按节点划分子网 |
| 核心组件 | 物理网卡（eth0/eth1）、iptables、路由表 | 虚拟网卡（vNIC）/物理网卡、虚拟交换机（OVS）、kube-proxy | CNI网桥（cni0）、veth pair、Pod网络命名空间 |
| 隔离边界 | 物理层隔离，与上层网络通过虚拟化/路由隔离 | 逻辑层隔离（VLAN/子网），介于宿主机和Pod之间 | 容器层隔离（NetworkPolicy），Pod间默认互通（需手动限制） |
| 通信对象 | 其他宿主机、物理网络设备（交换机/路由器） | 同一宿主机内其他节点、宿主机、Pod网络平面 | 同一节点内其他Pod、节点网络、外部网络（经节点转发） |

### （二）核心联系：层级依赖+流量转发链路

三个平面是“底层支撑→中间转发→上层应用”的层级关系，流量跨平面必须按固定路径流转，不可跳过中间层：

1. 依赖关系：Pod网络依赖节点网络（Pod需通过节点的网络栈对外通信），节点网络依赖宿主机网络（节点需通过宿主机物理网卡接入物理网络）；
2. 流量转发路径（跨平面示例）：
   `Pod A → Pod网络（veth pair→CNI网桥） → 节点网络（虚拟网卡→kube-proxy） → 宿主机网络（物理网卡→路由表） → 外部网络`
   反向流量同理，必须逐层转发，无法直接“Pod→宿主机”“Pod→物理网络”跨层通信。

## 二、最小权限访问控制策略：按场景开通互访

核心逻辑：**默认拒绝所有跨平面通信，仅针对“业务必需”的场景，开通“源IP+目标IP+端口+协议”四要素限定的策略**，避免宽权限放行。

### （一）策略前置准备：明确基础隔离规则

1. 网段严格隔离：确保三个平面的网段无重叠（如宿主机192.168.1.x、节点10.0.x.x、Pod172.16.x.x），避免IP冲突和路由混乱；
2. 开启默认拒绝：

* Pod层：通过NetworkPolicy配置“默认拒绝所有入站/出站流量”；
* 节点层：虚拟机节点的防火墙（如firewalld）默认拒绝非必要端口；
* 宿主机层：iptables默认拒绝Pod网段、节点网段的主动访问。

### （二）分场景开通跨平面互访策略（按优先级排序）

#### 1. 必需场景1：Pod ↔ 节点网络平面（业务核心通路）

**通信目的**：Pod访问节点上的服务（如kube-proxy、容器运行时），或通过节点网络访问外部网络。
**允许策略**：

* 方向1：Pod → 节点（限定端口/协议）

+ 允许Pod访问节点的“业务必需端口”（如kubelet的10250端口、容器运行时的containerd.sock对应的端口）；
+ 禁止Pod访问节点的敏感端口（如22 SSH、6443 K8s API、3306数据库端口）；
+ 配置示例（NetworkPolicy）：

  ```
  apiVersion: networking.k8s.io/v1
  kind:NetworkPolicy
  metadata:
  name:pod-to-node-allow
  namespace:default
  spec:
  podSelector:
      matchLabels:# 仅允许业务Pod（如web）访问
        app:web
  policyTypes:
  -Egress
  egress:
  -to:
      -ipBlock:
          cidr:10.0.0.0/16# 节点网段
      ports:
      -protocol:TCP
        port:10250# 仅允许访问kubelet端口
  ```

* 方向2：节点 → Pod（按需允许）

+ 仅允许节点上的“安全组件”（如HIDS、容器安全产品）访问Pod，用于监控/审计；
+ 配置示例（iptables，节点上执行）：

  ```
  # 允许节点的HIDS进程（PID 1234）访问Pod网段的8080端口
  iptables -A OUTPUT -p tcp --dport 8080 -d 172.16.0.0/12 -m owner --pid-owner 1234 -j ACCEPT
  ```

#### 2. 必需场景2：节点 ↔ 宿主机网络平面（网络出口通路）

**通信目的**：节点通过宿主机物理网卡访问外部网络（如拉取镜像、调用第三方API），宿主机管理节点（如虚拟化平台控制节点）。
**允许策略**：

* 方向1：节点 → 宿主机（限定功能）

+ 允许节点访问宿主机的“虚拟化管理端口”（如VMware的902端口），用于节点生命周期管理；
+ 允许节点的NAT转发流量（Pod对外通信经节点转发至宿主机物理网卡）；
+ 配置示例（宿主机iptables）：

  ```
  # 允许节点网段（10.0.0.0/16）访问宿主机的虚拟化管理端口
  iptables -A INPUT -s 10.0.0.0/16 -p tcp --dport 902 -j ACCEPT
  # 允许节点的NAT转发流量通过宿主机物理网卡
  iptables -A FORWARD -s 10.0.0.0/16 -o eth1 -j ACCEPT
  ```

* 方向2：宿主机 → 节点（严格限制）

+ 仅允许宿主机的“运维工具”（如Ansible、监控agent）访问节点的管理端口（如22 SSH，建议用密钥登录+端口映射）；
+ 禁止宿主机主动访问节点的业务端口（如80、8080）。

#### 3. 限制场景3：Pod ↔ 宿主机网络平面（尽量禁止，特殊场景放行）

**风险提示**：Pod直接访问宿主机网络是容器逃逸的常见路径，默认完全禁止，仅运维排查等特殊场景临时开通。
**允许策略（临时授权）**：

* 仅允许指定Pod（如运维Pod）在限定时间内访问宿主机的“排查端口”（如22 SSH）；
* 配置示例（宿主机iptables，临时生效，重启失效）：

  ```
  # 仅允许Pod A的IP（172.16.1.10）访问宿主机SSH端口，有效期1小时
  iptables -A INPUT -s 172.16.1.10 -p tcp --dport 22 -j ACCEPT
  sleep 3600 && iptables -D INPUT -s 172.16.1.10 -p tcp --dport 22 -j ACCEPT
  ```

#### 4. 可选场景4：跨节点网络平面（同一宿主机内）

**通信目的**：同一宿主机内不同节点的业务交互（如跨节点Pod通信经节点转发）。
**允许策略**：

* 按业务隔离：用VLAN标签划分节点（如电商业务节点VLAN 10，支付业务VLAN 20），仅允许同一VLAN内的节点通信；
* 配置示例（宿主机虚拟交换机OVS）：

  ```
  # 仅允许VLAN 10的节点互访
  ovs-vsctl add-flow br0 "in_port=1,dl_vlan=10,actions=output:2"
  ovs-vsctl add-flow br0 "in_port=2,dl_vlan=10,actions=output:1"
  ```

### （三）策略优先级与冲突处理

1. 优先级顺序：宿主机iptables > 节点防火墙 > NetworkPolicy（Pod层）；
2. 冲突原则：“更严格策略生效”（如NetworkPolicy允许Pod访问节点80端口，但节点防火墙拒绝，则最终禁止）；
3. 审计要求：所有策略变更需记录日志（如iptables日志、K8s事件），便于溯源。

## 三、核心安全原则与落地建议

1. 权限最小化：开通策略时，严格限定“源、目标、端口、协议”，不使用“0.0.0.0/0”（全网段）、“任意端口”等宽权限；
2. 分层控制：Pod层用NetworkPolicy（K8s原生），节点/宿主机层用iptables/虚拟交换机规则，不跨层配置策略；
3. 动态调整：定期审计策略有效性，业务下线后立即删除对应策略，避免“僵尸权限”；
4. 监控告警：部署流量监控工具，实时检测跨平面的异常流量（如Pod突然访问宿主机22端口、节点跨VLAN通信），触发告警。

##

```
![](https://mmbiz.qpic.cn/mmbiz_png/5GBRKfKXqpv3UEdyCDhgj2ic0QiclGDzdWASGcLAG8Fzl9ibicVC64tSKz3I4kg4dBg3WiaurszKZlzT3I0mYHVMaJA/640?wx_fmt=png)

「倬其安」分享一线实战中的故障洞察与架构思考。

提升安全认知，筑牢防护体系！

“倬其安，然无恙”。
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/cuBApO3XWpTChgJchdueibKX2iciaqzuic0We7tgfiaiaL0U6TCYzicibKbg15SaK0aZacf3gb1YWmB522VO9fAYQRicYmA/0?wx_fmt=png)

倬其安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/cuBApO3XWpTChgJchdueibKX2iciaqzuic0We7tgfiaiaL0U6TCYzicibKbg15SaK0aZacf3gb1YWmB522VO9fAYQRicYmA/0?wx_fmt=png)

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