---
title: WebRTC的隐私泄露风险：基于ping0.cc的IP收集机制分析
url: https://blog.upx8.com/WebRTC-ping0-cc-IP
source: 黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-04-04
fetch_date: 2026-04-05T04:38:23.472203
---

# WebRTC的隐私泄露风险：基于ping0.cc的IP收集机制分析

# [黑海洋 | Wiki](/ "黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# WebRTC的隐私泄露风险：基于ping0.cc的IP收集机制分析

发布时间:
2026-04-04 New Article

分类:
[系统安全/Os\_sec](https://blog.upx8.com/os_security)

热度:
2288

# ![WebRTC的隐私泄露风险：基于ping0.cc的IP收集机制分析](https://cdn.skyimg.net/up/2026/4/4/804cf6f3.webp)

# ping0.cc WebRTC IP 泄露机制分析

## 0x00 背景

本文对 `https://ping0.cc/` 的前端代码进行抓包与逆向分析，重点关注其是否存在收集用户真实 IP 及浏览器指纹的行为。

---

## 0x01 抓包发现可疑请求

使用 **Reqable** 工具抓包，过滤请求体中含有 IP 地址的请求，发现如下可疑端点：

```
POST https://ping0.cc/ip/peer HTTP/2

{
  "ip": "xxx.xxx.xxx.xxx",   // 用户真实公网 IP
  "size": "879-769"           // 浏览器窗口尺寸
}
```

```
HTTP/2 204
```

通过 Chrome DevTools 的 Initiator 追踪，请求来源为：

```
https://cdn.ping0.cc/js/check.js
```

---

## 0x02 JS 逆向分析

下载 `check.js`，发现经过 **jsjiami.com.v7** 混淆处理。以下为混淆后的原始关键方法片段：

```
'peer'() {
    const _0x240196 = _0x35e62e,
    _0x4a0fc3 = {
        'qnArj': function(_0x1b0c8c, _0x599205) { return _0x1b0c8c === _0x599205; },
        'CfeTI': _0x240196(0x2a1, '&]9^'),
        'uxcbk': function(_0x47aa75, _0xb926d0) { return _0x47aa75 === _0xb926d0; },
        'saKfi': _0x240196(0x1bf, 'l5GL'),
        'KxNbH': function(_0x3ad146, _0x30d0ae) { return _0x3ad146 + _0x30d0ae; },
        'Ahaer': _0x240196(0x208, 'EHcf'),
        'FCfGW': _0x240196(0x23f, 'p7Wb'),
        'gpjRN': function(_0x1758b5, _0x5b3737) { return _0x1758b5 === _0x5b3737; },
        'DrvIp': _0x240196(0x2a8, 'H@6r')
    },
    _0x213f70 = window[_0x4a0fc3[_0x240196(0x2b7, 'H)5x')]];
    if (_0x4a0fc3[_0x240196(0x1ef, '2RVF')](_0x213f70, undefined)) {
        this[_0x240196(0x1c9, 'nGax')] = window[_0x240196(0x1a3, '[1jt')];
        return;
    }
    const _0x475906 = new _0x213f70({ 'iceServers': [{ 'urls': _0x4a0fc3[_0x240196(0x2b6, 'fr9d')] }] });
    _0x475906[_0x240196(0x239, 'M0YP')] = _0x365e93 => {
        const _0x507ee3 = _0x240196;
        if (_0x365e93[_0x507ee3(0x1ad, 'YS0[')]) {
            if (_0x4a0fc3[_0x507ee3(0x1f1, '4Qn*')](_0x4a0fc3[_0x507ee3(0x2a7, 'tqEz')], _0x4a0fc3[_0x507ee3(0x29a, 'J^P0')])) {
                const _0x22ec76 = _0x365e93[_0x507ee3(0x1c7, 'nGax')][_0x507ee3(0x2b1, 'H)5x')][_0x507ee3(0x1ff, 'ni%P')](' ')[0x4];
                if (_0x4a0fc3[_0x507ee3(0x252, '3LK)')](_0x22ec76[_0x507ee3(0x1a5, '[1jt')](_0x4a0fc3[_0x507ee3(0x248, '#IR7')]), -0x1) && !this[_0x507ee3(0x2a3, '$aHF')](_0x22ec76)) {
                    const _0x13b720 = _0x4a0fc3[_0x507ee3(0x1e0, '*qsc')](_0x4a0fc3[_0x507ee3(0x28c, 'l5GL')](window[_0x507ee3(0x1e1, '[1jt')], '-'), window[_0x507ee3(0x2b3, 'iMDv')]);
                    axios[_0x507ee3(0x1d3, '4Qn*')](_0x4a0fc3[_0x507ee3(0x23e, 'ZAzr')], { 'ip': _0x22ec76, 'size': _0x13b720 });
                }
            } else _0x2588e5[_0x507ee3(0x213, 'SZ(Q')](_0x390073);
        }
    };
    _0x475906[_0x240196(0x1b6, 'f01U')]({ 'offerToReceiveAudio': !![] })[_0x240196(0x1b2, 'H)5x')](_0x2c7a44 => _0x475906[_0x240196(0x24b, 'J^P0')](_0x2c7a44));
}
```

借助 AI 辅助反混淆，还原后的逻辑如下：

```
peer() {
    // 获取浏览器 RTCPeerConnection API
    const RTCPeerConnection = window.RTCPeerConnection;

    // 若浏览器不支持 WebRTC，则 fallback 到 window.ip
    if (RTCPeerConnection === undefined) {
        this.newaddr = window.ip;
        return;
    }

    // 创建 RTCPeerConnection，使用 Google 公共 STUN 服务器
    const pc = new RTCPeerConnection({
        iceServers: [{ urls: 'stun:stun.l.google.com:19302' }]
    });

    // 监听 ICE 候选事件
    pc.onicecandidate = (event) => {
        if (event.candidate) {
            // 从 SDP candidate 字符串中提取第 5 个字段（即 IP 地址）
            const ip = event.candidate.candidate.split(' ')[4];

            // 过滤条件：必须包含点号（IPv4），且不属于保留地址
            if (ip.indexOf('.') !== -1 && !this.isreserve(ip)) {
                // 构造 size 参数（窗口宽 x 高）
                const size = window.innerWidth + '-' + window.innerHeight;

                // 上报至服务端
                axios.post('/ip/peer', { ip: ip, size: size });
            }
        }
    };

    // 触发 ICE 候选收集流程（必须先创建 Offer）
    pc.createOffer({ offerToReceiveAudio: true })
        .then(offer => pc.setLocalDescription(offer));
}
```

---

## 0x03 触发时机

该方法挂载于 Vue 组件的 `created()` 生命周期钩子中，即**页面加载完成后立即静默执行**，无需用户任何交互操作。

---

## 0x04 技术原理：WebRTC IP 泄露

WebRTC（Web Real-Time Communication）是浏览器内置的点对点通信协议。在建立连接时，浏览器需要通过 ICE（Interactive Connectivity Establishment）协议收集本地候选地址，其中包括：

* **本地 IP 地址**（host candidate）
* **NAT 映射后的公网 IP**（srflx candidate，通过 STUN 获取）

该站点利用 `onicecandidate` 事件回调截获 srflx 类型候选，从 SDP 字符串中提取出真实公网 IP，绕过了用户的代理设置（仅限非 TUN 模式的软件级代理）。

**ICE Candidate SDP 字段结构示意：**

```
candidate:xxx 1 udp 2122260223 203.0.113.45 54321 typ srflx ...
                                ↑ 第5字段 = 真实公网 IP
```

---

## 0x05 收集数据用途推测

| 字段 | 内容 | 推测用途 |
| --- | --- | --- |
| `ip` | 用户真实公网 IP | 验证代理是否泄漏、判断用户地区 |
| `size` | 浏览器窗口尺寸 | 浏览器指纹的组成部分 |

浏览器窗口尺寸本身是常见的**指纹识别**维度之一。结合真实 IP，可用于：

* 识别同一设备的不同访问
* 判断 IP 共享（多人共用出口 IP 的场景）
* 检测代理节点的 WebRTC 泄漏状态

---

## 0x06 防护建议

**完全防护方案：**

* 使用支持 **TUN 模式**的代理客户端（如 Clash Premium、sing-box 等），所有流量走虚拟网卡，WebRTC 泄漏的也是代理 IP

**浏览器级防护：**

* 安装 Chrome 扩展 [WebRTC IP保护](https://blog.upx8.com/go/aHR0cHM6Ly9jaHJvbWV3ZWJzdG9yZS5nb29nbGUuY29tL2RldGFpbC9hZ29obWdkZGZmYmdtZG5kbWdhYm9hY2toaHBoY2NrYg)，限制 WebRTC 的 IP 暴露策略
* Firefox 可在 `about:config` 中设置 `media.peerconnection.enabled = false` 直接禁用 WebRTC

**注意：** 仅使用 HTTP/SOCKS 代理（非 TUN 模式）无法阻止此类泄漏，因为 WebRTC 走的是系统底层网络，不经过代理软件。

---

## 免责声明

本文内容基于对公开 JS 文件的技术分析，所有观点仅代表作者个人理解，不构成对该网站的任何法律指控。读者可自行审阅源码进行验证。

[取消回复](https://blog.upx8.com/WebRTC-ping0-cc-IP#respond-post-7218)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [All](/all.html)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![又拍云赞助商](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2026 黑海洋. All rights reserved. [看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")