---
title: 紧急预警：你的代码可能已被「感染」！
url: https://mp.weixin.qq.com/s/ElSg0ClpCdThwuGzz-eIrg
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:17:07.344340
---

# 紧急预警：你的代码可能已被「感染」！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fTugLXvN07Ccsdt6Xk4npM6U9ia6OcQF9iczcXpNdCjuABmRptmGfVJMdMJoSb0zfRWBLzDjkXPv5IWGYgG7K9wXJnyuLTJibeG26kIu2Xaia1s/0?wx_fmt=jpeg)

# 紧急预警：你的代码可能已被「感染」！

原创

IDC老徐
IDC老徐

信息安全动态

![]()

在小说阅读器中沉浸阅读

数百个Python开源项目遭供应链攻击，你可能已经中招

> 阅读时间：6分钟

---

## 🔥 一个恐怖的场景

想象一下——

你正在开发重要项目，习惯性地执行 `pip install xxx`，一切看起来都很正常。代码跑起来了，功能也正常。

**但你不知道的是：你的 GitHub 令牌、AWS 密钥、甚至数据库密码，已经被悄悄打包发往了一个隐藏的指挥中心。**

这不是科幻小说。这是正在发生的真实事件。

---

## 📰 一场精心策划的「供应链战争」

2026年3月8日，安全研究人员发现了一场规模空前的开源供应链攻击。

**攻击者代号：GlassWorm**
**行动代号：ForceMemo**

这场攻击有多可怕？

* 🔴 **数百个** Python 开源仓库被污染
* 🔴 **13万+** 月下载量的 React Native npm 包受影响
* 🔴 Django 应用、机器学习代码、Streamlit 仪表板、PyPI 包无一幸免
* 🔴 攻击隐蔽性极高，普通开发者**根本察觉不到**

> **更可怕的是：这场攻击可能已经持续了一段时间，而你可能已经「中招」却不自知。**

---

## 🔍 攻击者如何做到「隐形」？

### 攻击链全景图

```
恶意 VS Code/Cursor 扩展
        ↓
窃取开发者 GitHub 令牌
        ↓
利用令牌 force-push 恶意代码
        ↓
开发者 pip install 拉取被污染代码
        ↓
恶意代码自动执行，窃取更多凭证
        ↓
循环往复，持续扩散
```

### 核心技术：Git Rebase + Force-Push

**这是本次攻击最狡猾的地方。**

传统供应链攻击，攻击者直接提交恶意代码。这种做法有个致命缺陷：Git 历史记录会暴露攻击者的痕迹。细心的开发者检查 commit 记录，就能发现异常。

但 GlassWorm 不一样——它采用了一种几乎「无痕」的技术：

**① 获取仓库访问权限**
通过恶意 VS Code/Cursor 扩展，窃取开发者的 GitHub 令牌

**② Git Rebase 操作**
将恶意代码注入到历史提交中

**③ Force-Push 强制推送**
覆盖远程仓库，但**保留原始提交信息**

结果是什么？

> 你看到的 commit 记录还是原作者的。提交时间、提交信息、甚至提交者头像都一模一样。除非逐行对比代码，否则根本发现不了任何异常。

这就是为什么这次攻击能持续这么久而不被发现。

### 隐蔽特性：语言环境检测

攻击者还添加了一个「自我保护」机制：

```
if system_language == "ru_RU":
    # 俄语系统，跳过执行
    exit()
else:
    # 执行恶意代码
    steal_credentials()
```

恶意代码会检测系统语言环境。如果是俄语系统，自动跳过执行。

这个设计的背后逻辑耐人寻味——规避特定地区的安全检测，还是暗示攻击者的地缘政治立场？我们不得而知。

**但有一点是确定的：中国开发者并不在这个「白名单」里。**

---

## 💀 区块链成为攻击者的「避风港」

攻击者选择了 Solana 区块链钱包作为命令与控制（C2）的指令下发渠道。

**为什么选择区块链？**

| 特性 | 攻击者优势 |
| --- | --- |
| 匿名性 | 无法追溯到真实身份 |
| 去中心化 | 没有单点故障，难以被封锁 |
| 公开透明 | 任何人都可写入数据，但只有私钥持有者能解密 |

攻击者通过在特定的 Solana 钱包地址写入加密数据，下发指令给被感染的机器。

这种「公开的隐秘通道」，让传统安全防护手段几乎束手无策。

---

## 🎯 你中招了吗？

### 已确认受影响的项目类型

| 项目类型 | 影响程度 | 风险等级 |
| --- | --- | --- |
| Django Web 应用 | 高 | 🔴 严重 |
| 机器学习/研究代码 | 高 | 🔴 严重 |
| Streamlit 仪表板 | 中 | 🟠 高 |
| PyPI 包 | 高 | 🔴 严重 |
| React Native npm 包 | 高 | 🔴 严重（13万月下载） |

### ⚠️ 高风险行为自查

请检查，你是否存在以下行为：

* ⬜ 近期安装过来源不明的 VS Code 或 Cursor 扩展
* ⬜ 使用过非官方渠道的 Python 包
* ⬜ GitHub 令牌近期出现异常登录提醒
* ⬜ 项目依赖中有近期突然更新的包
* ⬜ 在生产环境直接使用 `pip install` 而未校验 hash

> **如果超过2项，建议立即进行安全排查！**

---

## 🛡️ 防护指南：如何保护自己？

### 🚨 立即行动（高优先级）

#### 1️⃣ 检查 GitHub 令牌权限

```
GitHub → Settings → Developer settings → Personal access tokens
```

* 检查是否有异常活跃的令牌
* 立即撤销可疑令牌
* 建议使用短期令牌 + 细粒度权限控制

#### 2️⃣ 审计 VS Code/Cursor 扩展

```
扩展列表 → 检查安装来源 → 移除未知扩展
```

* 只安装官方市场或可信来源的扩展
* 定期审查已安装扩展的权限
* 关注扩展的更新日志

#### 3️⃣ 锁定依赖版本

```
# 生成锁定的依赖文件
pip freeze > requirements.txt

# 或使用 hash 校验
pip-compile --generate-hashes requirements.in
```

> **关键原则：不要直接使用 `pip install package` 在生产环境！**

#### 4️⃣ 使用代码审查工具

```
# 对比本地代码与远程仓库
git fetch origin
git diff HEAD origin/main

# 或使用专业工具
pip install bandit
bandit -r ./your_project
```

---

### 📋 中期措施

**建立供应链安全流程：**

1. **依赖白名单**：只允许经过审核的包
2. **自动扫描**：集成 SCA（软件成分分析）工具
3. **签名验证**：使用 sigstore 等工具验证包签名
4. **隔离环境**：开发/测试/生产环境严格隔离

**企业级防护：**

* 部署私有 PyPI 镜像，只同步经过审核的包
* 使用 SBOM（软件物料清单）追踪所有依赖
* 建立 SOAR 流程，供应链告警自动响应

---

## ⚡ 紧急排查脚本

如果你怀疑自己已经中招，可以运行以下检查：

```
#!/bin/bash
# 简易排查脚本

echo"=== 检查可疑进程 ==="
ps aux | grep -E "(glassworm|forcememo)"

echo"=== 检查异常网络连接 ==="
netstat -anp | grep -E "(Solana|unknown)"

echo"=== 检查 Git 远程配置 ==="
git remote -v

echo"=== 检查最近修改的 Python 包 ==="
pip list --outdated

echo"=== 建议：手动对比关键依赖的 hash 值 ==="
pip show <package_name>
```

---

## 📢 行动号召

**这不仅仅是技术问题，这是关乎整个开源生态安全的问题。**

请立即转发这篇文章给你的开发者朋友、技术团队、以及所有可能受到影响的人。

> **供应链攻击的特点就是「传染性」——一个被污染的包，可能会影响成千上万的下游项目。**

### 你可以做的：

1. **分享本文**：让更多人知道这场攻击的存在
2. **自查自纠**：按照防护指南检查自己的项目
3. **报告异常**：发现可疑包，立即向 PyPI/npm 官方举报
4. **关注安全**：订阅安全公告，保持信息更新

---

## 🔗 参考资源

* PyPI 安全公告：pypi.org/security
* npm 安全公告：npmjs.com/advisories
* GitHub 安全实验室：securitylab.github.com
* sigstore 软件签名：sigstore.dev

---

**开源的世界很美好，但安全的防线不能松懈。**

**每一个开发者，都是供应链安全的第一道防线。**

---

> 声明：本文基于公开披露的安全事件整理，技术细节仅供参考。具体排查请以官方安全公告为准。如有疑问，请咨询专业安全团队。

---

**如果这篇文章对你有帮助，请点个「在看」，让更多人看到。**

**你的每一次转发，可能都在阻止一次攻击的蔓延。** 🔐

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/HPjboWok4teVOic0O8dM4CYg3a98MY5sfRJ2uicwq2VcVNH56GGxoWYpH4g3bq1tqhHOFxtfv0ryDt9vSne5JgnQ/0?wx_fmt=png)

信息安全动态

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HPjboWok4teVOic0O8dM4CYg3a98MY5sfRJ2uicwq2VcVNH56GGxoWYpH4g3bq1tqhHOFxtfv0ryDt9vSne5JgnQ/0?wx_fmt=png)

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