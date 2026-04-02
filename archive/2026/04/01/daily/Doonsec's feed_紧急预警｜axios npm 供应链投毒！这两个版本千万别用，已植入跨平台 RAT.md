---
title: 紧急预警｜axios npm 供应链投毒！这两个版本千万别用，已植入跨平台 RAT
url: https://mp.weixin.qq.com/s/f-CCIHpHe0EyiASzhzFiFA
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:27:16.914849
---

# 紧急预警｜axios npm 供应链投毒！这两个版本千万别用，已植入跨平台 RAT

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DWbvgyGujI4cf8FOp70K1vbL2ib77Cy2e9rN12q9pvuh47GFE9CoVreEsxiaOIhjC1Hx80iaQrTdy0UZGXnGnRRH9sNxCxDiaiaibMERMYqe17SHQ/0?wx_fmt=jpeg)

# 紧急预警｜axios npm 供应链投毒！这两个版本千万别用，已植入跨平台 RAT

耶度
耶度

野猪与安全

![]()

在小说阅读器中沉浸阅读

**发布时间：2026-04-01 | 安全等级：极高 | 影响范围：全 Node.js 开发环境**

各位前端、后端、DevOps 同学注意：**全球最常用 HTTP 客户端库 axios，刚刚曝出严重 npm 供应链投毒事件**。攻击者劫持核心维护者 npm 账号，发布两个恶意版本，安装即静默植入跨平台远控木马（RAT），窃取源码、密钥、环境变量等高敏感资产。

## 一、事件核心速览（必看）

|  |  |
| --- | --- |
| 披露时间 | * **2026-03-31**（StepSecurity 官方预警） |
| 攻击方式 | * 劫持 axios 核心维护者 jasonsaayman npm 账号，发布恶意版本，注入隐藏恶意依赖 |
| 涉毒版本 | * axios@1.14.1（1.x 最新分支）  * axios@0.30.4（0.x 旧版分支） |
| 恶意载荷 | * 隐藏依赖 plain-crypto-js@4.2.1，通过 postinstall 脚本自动执行，**macOS/Windows/Linux 全平台植入 RAT**，并连接 C2 服务器接收指令 |
| 关键 IOC | * 恶意依赖：`plain-crypto-js@4.2.1`  * C2 域名：`sfrclak.com`  * C2 IP：`142.11.206.73` |
| 安全版本 | * 1.x 分支：`axios@1.14.0`  * 0.x 分支：`axios@0.30.3` |

## 二、谁最危险？影响范围全覆盖

只要你的环境满足以下任一条件，**必须立即自查**：

1. 近期执行过 npm install / npm update，且安装 axios@1.14.1 或 axios@0.30.4
2. 涉及：**个人开发机、测试机、CI/CD 构建机、生产发布机、容器镜像、内网开发环境**
3. 风险后果：

* 主机被完全远程控制，攻击者可执行任意命令、上传下载文件
* 源码、构建产物、.env 密钥、SSH / 云服务凭证、npm/GitHub Token 全量泄露
* 恶意脚本执行后会自毁清理痕迹，常规审计难以发现

## 三、三步极速自查（先快后细，复制即用）

### 1️⃣ 查 axios 版本（最核心）

终端执行，有输出即命中恶意版本：

```
# 全局+项目依赖排查npm list axios 2>/dev/null | grep -E "1\.14\.1|0\.30\.4"# 检查锁文件（package-lock.json/yarn.lock）grep -A1 '"axios"' package-lock.json | grep -E "1\.14\.1|0\.30\.4"
```

2️⃣ 查恶意依赖目录（已执行安装脚本的标志）

```
ls node_modules/plain-crypto-js 2>/dev/null && echo "⚠️ 存在恶意依赖，已受影响"
```

### 3️⃣ 查流量 / 后门痕迹（进阶排查）

* 流量：检查代理 / EDR / 防火墙日志，是否有访问 `sfrclak.com` 或 `142.11.206.73` 的记录
* 系统后门（各平台）：

```
# macOSls -la /Library/Caches/com.apple.act.mond 2>/dev/null && echo "⚠️ macOS已植入RAT"# Linuxls -la /tmp/ld.py 2>/dev/null && echo "⚠️ Linux已植入RAT"# Windows（CMD）dir "%PROGRAMDATA%\wt.exe" 2>nul && echo "⚠️ Windows已植入RAT"
```

## 四、紧急处置：先止血、再清理、最后加固

### ✅ 第一步：立即止血（所有环境必做）

1. 禁止使用 / 安装 1.14.1 /  0.30.4，强制升级 / 回滚到安全版本：

```
# 1.x用户npm install axios@1.14.0 --save# 0.x用户npm install axios@0.30.3 --save
```

2. 锁定版本，防止间接依赖拉取恶意版（package.json 添加）

```
"overrides": {  "axios": "1.14.0"},"resolutions": {  "axios": "1.14.0"}
```

3. 移除恶意依赖：

```
rm -rf node_modules/plain-crypto-jsnpm prune
```

### ✅ 第二步：隔离取证 + 深度清理（疑似中招必做）

1. 立即隔离受影响主机 / 容器，**不要在中毒机器上做任何密钥操作**
2. 保留证据：npm 安装日志、构建日志、EDR 告警、流量日志，用于溯源
3. 高风险场景（构建机、签名机、密钥存储机）：**直接重装系统 / 回滚可信镜像**，不要尝试手动清理后门
4. 全量轮换所有凭据（重中之重）：

* npm/GitHub Token、SSH 密钥、云厂商 AK/SK
* CI/CD 流水线密钥、数据库密码、API 密钥、`.env` 所有敏感变量
* 内网账号、VPN、堡垒机凭证

### ✅ 第三步：临时封禁 IOC（网关 / 主机层）

1. 本地 hosts 屏蔽 C2 域名：

```
echo "0.0.0.0 sfrclak.com" >> /etc/hosts
```

2. Linux iptables 封禁 C2 IP：

```
iptables -A OUTPUT -d 142.11.206.73 -j DROP
```

1. 3. 企业侧：在防火墙、WAF、EDR、DNS 服务器添加上述 IOC 拦截规则

## 五、长效防护建议（避免下次中招）

1. CI/CD 构建强制加 --jgnore-scripts，阻止 npm postinstall 恶意脚本执行：

```
npm ci --ignore-scripts
```

1. 2. 固定依赖版本，使用 package-lock.json/yarn.lock，禁止自动升级
2. 3. 启用 npm 账号 2FA，定期轮换维护者权限，最小化发布账号权限
3. 4. 定期扫描依赖安全，使用 npm audit、Snyk 等工具，关注开源库安全公告

## 六、重要提醒

* 恶意版本已被 npm 官方下架，但**已安装的机器不会自动清理**，必须手动排查处置
* 本次攻击针对全平台、全开发场景，**不要心存侥幸，所有 Node.js 环境都要过一遍**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hnMsAHHSrJ6r2ESr3QZpuhqK8sL1iaBxJGFcS7c7LREzPRpfWQPwsEuaoFT1VwHOW9IHSc17ic9cE2ADyIyvFmlA/0?wx_fmt=png)

野猪与安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/hnMsAHHSrJ6r2ESr3QZpuhqK8sL1iaBxJGFcS7c7LREzPRpfWQPwsEuaoFT1VwHOW9IHSc17ic9cE2ADyIyvFmlA/0?wx_fmt=png)

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