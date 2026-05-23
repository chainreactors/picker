---
title: 用户实战成果｜CyberStrikeAI 社区反馈精选
url: https://mp.weixin.qq.com/s/wMKqw4s6L88-kGYSZ2uaxQ
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:38:48.036781
---

# 用户实战成果｜CyberStrikeAI 社区反馈精选

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ufQ2xnAD33tv6k3ewWvYmMuwnbMvGTKb2AiafsqlYaGmjlxicgIxapgqJb8fibbTZxdLY72OlGial4jxqlMDqa3iaoYIgxL7jy8WYNj6f77F2PCU/0?wx_fmt=jpeg)

# 用户实战成果｜CyberStrikeAI 社区反馈精选

低调学安全
低调学安全

低调学安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33smElzLx2r8TYSdll4jlC8wOaLXw4Exs8nP6V6MbzugibUxhOed3VlGJ0NJ2hSpsEJA7LOWFYyVBsJ3BvNEibqHTCoctvcEJW92A/640?wx_fmt=png&from=appmsg)

## 一、总览：不是「扫到了」，是「能交差」

有用户在一次评估周期内，平台仪表盘累计：

* **220** 条漏洞入库（**110** 条严重、**79** 条高危）
* **16,496** 次工具调用，覆盖 **67** 种能力
* 执行成功率约 **86.4%**

说明 AI 编排不是停留在对话层，而是持续在调 nmap、sqlmap、ffuf、amass、自定义 HTTP 框架等，把结果沉淀进 **漏洞管理**（严重等级、待处理状态、按对话归档），可直接进修复或写报告。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ufQ2xnAD33u5rOEvzCFG04TlnRfVAqLDAFewiaricyV2g7gLzWKCDN8r1dKxHw0eAqhOE2S720evCo9VWkNClBYcu3BeEhugtibP20VKu4JIYM/640?wx_fmt=jpeg&from=appmsg)

### 长任务稳定性：单会话 1900+ 次工具调用无异常

另有用户反馈，在 **Eino 代理**（`cyberstrike-eino-single`）下单条授权评估任务中，工具调用序号连续推进至 **#1939** 量级（`execute`、`nmap`、`http-framework-test` 等交替执行），界面全程保持 **「执行中」**，未出现中断、报错或编排崩溃——说明在高迭代、长窗口实战里，代理链路能扛住持续编排，而不是「跑几十轮就挂」。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33siaCuLreicKVjMnytxN2KIiaBDOWVYdCiaK06kfJiaIfcgKr1iaicRBXdpbj2FhQpx5ujoh4a6P1WVic09YzSVfeSQHUJDbC5tyibItJVw/640?wx_fmt=png&from=appmsg)

---

## 二、注入与防护绕过

### 2.1 系统性 Oracle SQL 注入

* 多页面、**11+** 注入点，**21** 种函数执行链可验证
* 标注：**WAF 完全绕过**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33sWBh8cdDYw1CXh7KxtcS6lpPRyGz01INKJ5CKW04Ie9T054bDib0w9a8KLt8fzIauZictqibicBGs2xYjiaMibBLsDcXicVs54tMduDI/640?wx_fmt=png&from=appmsg)

### 2.2 三重防护链绕过（WAF + Druid + MyBatis）

用户反馈中，通过 ORDER BY 注入完成完整技术链：

| 环节 | 思路摘要 |
| --- | --- |
| WAF 关键字 | `REPLACE` 拆分 `SEL.ECT` 等，绕过关键字检测 |
| 引号限制 | URL 编码 `%27` 直达 Oracle |
| Druid 防火墙 | 函数内字符串被当作「普通数据」 |
| 数据提取 | 盲注 + `RAWTOHEX` 逐字还原库表元数据 |

成果：Oracle 用户名、**9** 张用户表、表名逐字提取等（目标信息已脱敏）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33uicBdnib2UuKsQ5hglTwiahABRf8BxYdkRWHNBuWVnJmJ93WqCkcG3nc1Mdk64cVOCllKXibciaf1ny7G9bMnBfZ8pHh1b68Xz9TF4/640?wx_fmt=png&from=appmsg)

### 2.3 其他注入类

* **MyBatis**`ORDER BY`：`sort` 动态拼接，可执行任意 SQL 函数
* **MSSQL** 布尔盲注（价格/面积字段，WAF 绕过）
* **AjaxManJian.aspx**`Cart_id` 时间盲注
* **saveUserBehaviorData** 接口 `query` 参数时间盲注
* 移动站搜索功能 SQL 注入 → 数据库侧大面积泄露

---

## 三、业务逻辑与越权（扫描器最难覆盖的一块）

社区反馈里，**严重** 标签高度集中在 API 逻辑缺陷：

| 类型 | 典型发现 |
| --- | --- |
| 支付/订单 | 客户端可控支付金额、订单价格篡改 |
| 认证 | Session 可预测导致未授权访问；JWT 弱密钥任意伪造 |
| 密码/短信 | 重置无旧密码校验、无速率限制、验证码可爆破 |
| IDOR | 任意删用户、改他人密码/角色、改公司信用额度与余额 |
| 垂直越权 | 低权限自建超级管理员、未授权创建管理员、全平台接管 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33uxZvZK1icNGGMwlmTTW8K6CUDPxH4H2icTXibSUia7xOkQzQoAJmESMR9hviabbzugdzA59icqLJPTry1sXjcyHtU8nuquDZ5hibKcG0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33vsKITRibHIhhWPx2Tj0TBus3XvR9I3NTriaHQLdkGpxTmr8hCtR82N88kETYDtlxFiaicvNHDGyEsS01OSR23mLicEaHfRLGmGoqMc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33uwRY32Nr2uyuPHDPg2KOTxnZdg9eOVXgzkdqp2RQCLCLEEpibQia3ENOLzazQSWr4mw29P0YUsialQoOAPyTeSwmIyTzOJA8Hibqo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33tF9ngYpk8LibHYrhUn2Al3OOcCWjhuiaK75JhzgzBJyHJ3sDKd545eg970039icfOoFleKwZx3SGCbPuFfNYNQF68IVQHId0uFo0/640?wx_fmt=png&from=appmsg)

部分案例中，**十余分钟内** 连续入库多条「系统接管级」漏洞（管理员明文密码接口、任意创建超管、跨公司余额篡改等）。

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33vmAabZ9dbYSqOz1hngqWo1iaw7arJMJLTq84sF3Oibt1IxStJ6upab9ok3GxRqymdRQ3rJKPvdoC1rlibqKF1tkpcssqSDLzRd8A/640?wx_fmt=png&from=appmsg)

---

## 四、数据泄露与身份安全

* 大规模 **PII / 订单** 未授权访问（**48,143** 条量级，多例反馈）
* 管理员列表接口 **明文返回密码**（11～12 个管理员凭据类案例）
* **JWT 弱密钥** → 任意 Token 伪造 + 管理员账户接管
* 数据库完全访问 → **3,367** 条客户 PII 泄露（另案）
* 用户注销无确认、测试接口 `test/unfreeze` 暴露、Redis 任意键读写等

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33ugq2mzO941gY0iaTSZ3z59O9PGxFTRgN3s5OpRszSN9v9Qc8m3HmZTuFraY1jiaoyoaFliaAAl258sk4yq6cWPwjmmpvn78WFumU/640?wx_fmt=png&from=appmsg)

---

## 五、NoSQL、供应链与移动面

* **MongoDB NoSQL 注入**：登录端 `$where`、认证绕过、潜在 DoS/数据泄露
* **供应链**：恶意 JS 伪装 jQuery CDN、第三方域名投毒
* **Employee 商户接口** 垂直越权
* **eSign 人脸认证回调** 无认证可伪造

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33say7IhMSUib6WQup30knmQYZRtdxUKVUPcibAwdNPhYJbDicBDw29VQ0jia35rtWVXibwxnhWfBkw0sdFZUjLpicb2uibnutBDS9yTxw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33v52iakDhG70ed12XYNGvEV5dxTpU4ekLfIgkq5agkb7JXOdwbI81uCQjO1FES3SpiaBW1G32lvk3aA96oaLPDATbfUMAiaRHsBHQ/640?wx_fmt=png&from=appmsg)

---

## 六、云、密钥与深度渗透

| 场景 | 成果摘要 |
| --- | --- |
| SSRF | 阿里云 ECS / UCloud 实例元数据泄露，可导致云账户接管 |
| 密钥泄露 | 阿里云 OSS/SMS、快递100、腾讯地图等多组 API 密钥 |
| 支付密钥 | 微信支付商户密钥 + 小程序 AppSecret 泄露（案例已脱敏） |
| 横向/沦陷 | 服务器无隔离 → 跨站横向、5 组库凭据；单台服务器 **6 库 + 19 站点** 关联面 |
| 组合利用 | WebShell + 库凭据 + Session 伪造 → 管理后台接管 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33sOKCIqjREjlctvV6dH5ykZ9XX9k8HaCSPAKQU4j9L5Zicf1rficohqrGIBKMI45m0FRuDlRF89bDFbJOzmZbFq8UVYCia9he7ibVc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33vDZ6LsDh5Ftyv2lic6lQic3LHEJqlicypIQb76kaff1ic6WVnO7yYyiartmjj62oUX7YxvDzB9Pq81FAbX7HPPibZjZmdPPvFqrfd0A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33tAJliawpsiaEnbENJXQORVJQYpMJeHgrw89lHK9Hbp60yib5rUe8uv0J2tYkM9UknFqTM3JK4IwlD6HysPsHSSHsYczEYkrfuJ0k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33s126tTgZGwjyxysOcP6eK2BoUmu2U7Z8Q613Rj2TRS7icdicrvfXHYdoJDBu7hwvtUjwqnKfiaDsR1nlqxPQdJiaCKEoXm7PEgl6c/640?wx_fmt=png&from=appmsg)

---

## 七、早期逻辑类样本（4 月批次）

同一时段批量入库的高危/中危项包括：短信接口无频控、Redis 任意键操作、`updateOrderLocation` 业务缺陷等——体现平台对 **逻辑 + 基础设施** 的覆盖，不仅盯 CVE 模板。

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33ticfgQfqGb6bdDrcUzurpmtyndTzUKicwdSkeP6x70E6fVlsDXKw3IwYafE1ghbUVxZy7YZFxxSEfQ6Z3uTG3RmjUj3A9MtKtEo/640?wx_fmt=png&from=appmsg)

---

## 八、这些成果说明了什么？

结合社区反馈，可以概括四点：

1. **深度**：从 WAF/Druid/MyBatis 组合绕过，到 IDOR、支付篡改、云 SSRF，不是浅层扫端口。
2. **速度**：多条「严重」可在短时间连续入库，适合窗口紧的评估项目。
3. **可交付**：统一进漏洞管理，严重等级清晰，便于甲方整改或 SRC 报告。
4. **稳定性**：单任务 **1900+** 次工具调用仍可连续执行，适合长周期、高迭代的授权渗透项目。

---

## 九、投稿与合规

* 以上均为用户在 **授权测试** 环境下的反馈，截图中目标与敏感字段已脱敏。
* 欢迎在社区分享你的战果（Star / Issue / 微信群，入口见仓库 README）。
* **请勿对未授权目标使用任何安全工具。**

**GitHub**：https://github.com/Ed1s0nZ/CyberStrikeAI

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KzNYA6icKe6ny3nDMkDelsYYnPJzRX2erWFEia2S7Bqqc7CjicEpJYQtId7a2jXKCial6Mw8ck8IFQEqmZnldrG2EQ/0?wx_fmt=png)

低调学安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KzNYA6icKe6ny3nDMkDelsYYnPJzRX2erWFEia2S7Bqqc7CjicEpJYQtId7a2jXKCial6Mw8ck8IFQEqmZnldrG2EQ/0?wx_fmt=png)

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