---
title: AI给的代码，正悄悄给黑客留门？
url: https://mp.weixin.qq.com/s/AcLm0_qPDY9MZ8mIQGT2ZQ
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:39:41.823402
---

# AI给的代码，正悄悄给黑客留门？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/njVhCYJqSqnZUmLka1rDbAxLOHtgSkI6tiamgtZDdic6VU4Iaiat7679VPe3tEvgLkwjLrUG14GRJ2wiaOUGbibMo23Ssnn3mz2hzicwYRzUQqFW0/0?wx_fmt=jpeg)

# AI给的代码，正悄悄给黑客留门？

原创

JacobWang
JacobWang

NowSec

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/njVhCYJqSqm4yibaDShnCbMyOGRsENA47JLInaPP5Z5DFrqwLExiahc9dfAiav3zuRPGbNDZZiajib8MgEvicxUblVGJnzuClmbZrkVcJynoGhibhs/640?wx_fmt=png&from=appmsg)

01 / 提效神器，还是特洛伊木马？

2026 年，如果你的 IDE 里没装 AI 插件，可能都不好意思自称程序员。

从 GitHub Copilot 到各种私有化大模型，AI 已经渗入代码生成的每一个角落。据统计，目前全球超过 **80%** 的企业代码中，都包含 AI 生成或辅助编写的片段。

> **核心观察：**
>
> 大家都担心 AI 会抢饭碗，但更紧迫的威胁是：**AI 正在降低“投毒”和“编写高隐蔽性漏洞”的门槛。**

当你对 AI 说“帮我写个高性能登录接口”时，它可能顺便帮你留了个“后门”。

---

## 02 / 深度解析：AI 是如何被“教坏”的？

AI 模型本身没有安全意识，它只负责在概率上生成“看起来最顺理成章”的代码。黑客正是利用了这一点：

* **🧪 训练集投毒 (Data Poisoning)**

  黑客在开源社区发布大量带漏洞的“优雅代码”。AI 学习后，会将这些“影子漏洞”当作标准答案推送到你的屏幕上。
* **🌀 “幻觉”引起的供应链攻击**

  AI 偶尔会胡诌一个不存在的 npm 或 Python 包。黑客抢先注册同名恶意包，你一执行 `pip install`，后门直接入库。
* **🎭 提示词注入 (Prompt Injection)**

  通过复杂的描述绕过 AI 的安全审查，诱导它写出“为了测试方便”而关闭防御逻辑的代码。

---

## 03 / 实战复现：AI 的“隐蔽陷阱”

我们在隔离环境中进行了安全复现，这两个坑你可能也踩过：

#### 案例 A：追求简洁，丢了权限

**场景：** AI 生成一个修改用户信息的接口。

```
# [ AI 生成的危险代码 ]@app.put("/user/{user_id}/update")def update_profile(user_id: int, new_name: str, current_user: int = Depends(get_current_user)):    # ❌ 漏洞：AI 忘记检查 current_user 是否等于 user_id    # 导致用户 Bob 只要知道 Alice 的 ID，就能修改 Alice 的信息    users_db[user_id]["name"] = new_name    return {"status": "success"}
```

**分析：** AI 追求“能跑通”，却完全忽略了**权限隔离（IDOR越权）**。

#### 案例 B：危险的命令拼接

**场景：** AI 编写一段根据 ID 查询系统日志的代码。

```
# [ AI 生成的危险代码 ]def get_logs(user_input_id: str):    # ❌ 漏洞：AI 习惯性使用了 shell=True    command = f"cat /var/log/user_{user_input_id}.log"    # 如果用户输入: 1; rm -rf /     # 系统会直接执行后续毁灭性命令    subprocess.check_output(command, shell=True)
```

**分析：** 为了省事，AI 选择了最不安全的系统调用方式。

---

## 04 / 避坑指南：给技术人的 4 条建议

作为开发者，拥抱 AI 的同时，请务必握紧手中的“安全钥匙”：

1️⃣ **建立 [AI-Generated] 审计机制**

所有 AI 生成的代码必须经过人工 Code Review，并打上特殊标记，重点审查逻辑漏洞。

2️⃣ **强化自动化安全扫描**

使用 Snyk、Semgrep 等工具，专门针对 AI 易犯错的模式（如逻辑越权、未转义拼接）进行静态扫描。

3️⃣ **坚持“零信任”第三方依赖**

绝不安装 AI 推荐但未经验证的库。在安装前，先去 GitHub 看看 Star 数和维护记录。

4️⃣ **在沙箱中跑测试**

涉及敏感操作的 AI 代码，先在容器中跑一遍，观察是否有非预期的网络请求或文件修改。

---

## 05 / 结语

AI 是优秀的秘书，但不是合格的安全架构师。

**你可以让 AI 为你写代码，但绝对不能由它来掌握安全的底线。**

预览时标签不可点

作者提示: 内容由AI生成

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uGcolQMOicJ8XqUbib5wB7FOrwOhtXf98QEkzRtq2mWL8xMBPA0cIQ0blkKnvOF2jCCkqDVdnCSzdDHYn3y5MShw/0?wx_fmt=png)

NowSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uGcolQMOicJ8XqUbib5wB7FOrwOhtXf98QEkzRtq2mWL8xMBPA0cIQ0blkKnvOF2jCCkqDVdnCSzdDHYn3y5MShw/0?wx_fmt=png)

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