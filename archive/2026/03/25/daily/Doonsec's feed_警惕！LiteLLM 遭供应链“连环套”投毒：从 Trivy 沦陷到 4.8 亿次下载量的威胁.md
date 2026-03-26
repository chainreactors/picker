---
title: 警惕！LiteLLM 遭供应链“连环套”投毒：从 Trivy 沦陷到 4.8 亿次下载量的威胁
url: https://mp.weixin.qq.com/s/JMIiELj2gtv3KrI_4625pA
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:27:05.419114
---

# 警惕！LiteLLM 遭供应链“连环套”投毒：从 Trivy 沦陷到 4.8 亿次下载量的威胁

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gibHv0o062m1AWfRYiaNl4yMWpNxH2waztGWaJDicR76xoAiazvUUo8XficCDJqHonsEApujn0u3XyKp37fZsvu996TAvmK7yhykIIwfCQrslNCw/0?wx_fmt=jpeg)

# 警惕！LiteLLM 遭供应链“连环套”投毒：从 Trivy 沦陷到 4.8 亿次下载量的威胁

原创

老兵
老兵

网安守护

![]()

在小说阅读器中沉浸阅读

2026年3月24日，AI 圈发生了一起严重的供应链安全事故。作为连接百种大模型的通用网关，**LiteLLM** 在 PyPI 官方仓库遭遇投毒。这不仅仅是一次简单的恶意包上传，而是一场精心策划的“工具链渗透”——攻击者通过攻破安全工具 **Trivy** 进而窃取了 LiteLLM 的发布凭证。

截至目前，PyPI 已紧急下架相关版本，建议所有用户立即回滚。

![](https://mmbiz.qpic.cn/mmbiz_png/gibHv0o062m2iaP5TtQZIb32t1uQ5YF0CFszV61PDic9kVJfdqKhtD1gWnaa5Y4qsr1wvNA3kqLF1G5AcIAtiaUjFOmoiarOHbiaBKciaibTlqiczZAI/640?wx_fmt=png&from=appmsg)

---

### 一、 攻击复盘：一场蓄谋已久的“套娃”行动

这场攻击并非偶然，其链路清晰展示了黑客组织 **TeamPCP** 的渗透逻辑：

1. 1. **起点（2月28日）：** 攻击者首先攻陷了知名扫描工具 **Trivy**。
2. 2. **跳板（3月中旬）：** 开发者在 CI/CD 流水线中使用带毒的 Trivy 时，不慎泄露了 LiteLLM 的 PyPI 发布令牌（Token）。
3. 3. **收网（3月24日）：** 攻击者利用令牌发布了恶意版本 **`v1.82.7`** 和 **`v1.82.8`**。

> **影响规模：** LiteLLM 月活下载近 1 亿次，受影响的下游依赖包超过 2100 个，波及范围极广。

---

### 二、 恶意行为解析：隐蔽性极高

本次投毒版本中隐藏了三阶段（Stage）的 payload，手段极其阴毒：

* • **v1.82.7（显式触发）：** 只要在代码中 `import litellm.proxy.proxy_server`，恶意 Base64 脚本即刻执行。
* • **v1.82.8（全量感染）：** 利用 `.pth` 文件特性，**无需显式调用**，只要 Python 环境启动，恶意脚本便会自动静默运行，极难被发现。

#### 核心窃取目标：

* • **全方位凭证：** 自动搜刮 SSH Key、云服务秘钥（AWS/GCP/Azure）、K8s 配置、数据库密码及 `.env` 环境变量。
* • **集群横向移动：** 尝试在 Kubernetes 中部署特权 Pod，并在系统内植入 `systemd` 后门。

---

### 三、 开发者紧急自救指南

如果您在 2026 年 3 月 24 日之后进行过安装或更新，请务必执行以下步骤：

#### 1. 检查并强制回滚

检查版本，若处于恶意区间，请立即卸载并重装稳定版：

```
1

2

3

4

5

6

# 检查版本
pip show litellm | grep Version

# 卸载恶意版本并回滚
pip uninstall litellm==1.82.7 litellm==1.82.8 -y
pip install litellm==1.82.6
```

#### 2. 清除系统残留

检查并删除可能存在的伪装后门：

```
1

2

3

4

# 停止并禁用伪装的电信遥测服务
systemctl stop sysmon-telemetry 2>/dev/null
systemctl disable sysmon-telemetry 2>/dev/null
rm -f /etc/systemd/system/sysmon-telemetry.service
```

#### 3. 凭证轮换（重中之重）

**即使已回滚版本，也必须默认所有密钥已泄露。** 请立即更换：

* • 所有云服务访问密钥（Access Keys）
* • LLM API Keys (OpenAI, Anthropic 等)
* • SSH 登录凭证与数据库密码

---

### 四、 关键 IOC（失陷指标）

在防火墙或安全审计设备中，请重点监控以下域名及文件哈希：

| 类型 | 指标内容 | 说明 |
| --- | --- | --- |
| **C2 域名** | `models.litellm.cloud` | 数据外传通道 |
| **C2 域名** | `checkmarx.zone` | 持久化控制节点 |
| **SHA-256** | `a0d229be8efcb2...` | 被篡改的 proxy\_server.py |
| **SHA-256** | `71e35aef030992...` | 恶意的 litellm\_init.pth |

---

### 总结与启示

此次事件标志着供应链攻击已进入“自动化收割”时代——从开发工具链到包管理器，每一环都可能成为突破口。建议企业优先启用 **OIDC (OpenID Connect)** 进行发布认证，彻底废弃长期有效的 API 令牌。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/cm9mPvQVqibGd65c3eJPHrquKia0JIOKTLze61HQgWw3d7nPyZK2v12ModP3KMy5HxuhNTplVWfia0wwiaGicGtvORg/0?wx_fmt=png)

网安守护

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/cm9mPvQVqibGd65c3eJPHrquKia0JIOKTLze61HQgWw3d7nPyZK2v12ModP3KMy5HxuhNTplVWfia0wwiaGicGtvORg/0?wx_fmt=png)

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