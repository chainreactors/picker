---
title: Dejavu(逮虾户)，专逮野生小龙虾：OpenClaw基线安全检测神器来了
url: https://mp.weixin.qq.com/s/lEeO1ga7EimSGjjN-fVrrA
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:14:44.176632
---

# Dejavu(逮虾户)，专逮野生小龙虾：OpenClaw基线安全检测神器来了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lfebBgkWzEPsELRMAd71picQgic1mMFDicyYSDGJ2uDa8auqtwNCOGYTp8Xsjn89SgDjbQmWG34HyiacnMaCZModobPkVx6u7libxz4pt350AkyU/0?wx_fmt=jpeg)

# Dejavu(逮虾户)，专逮野生小龙虾：OpenClaw基线安全检测神器来了

玉衡实验室
玉衡实验室

山海之关

![]()

在小说阅读器中沉浸阅读

国家网络安全通报中心最新警示：OpenClaw（技术圈俗称“小龙虾”）风险爆表——85%资产直接暴露公网，默认18789端口成攻击者首选；漏洞库已收录258个安全漏洞，含远程控制、权限提升等严重风险；更令人警惕的是，插件供应链投毒率高达10.8%，每下载10个Skill就可能有一个暗藏后门。

你家的小龙虾，可能正在被别人“偷吃”：有人用你的18789端口挖矿，有人通过恶意Skill控制你的Agent，甚至你的AI模型已经在帮别人干活，你还以为它只是有点“不听话”。

逮虾户——首个开源OpenClaw基线安全检测工具正式上线。 一键扫描端口风险、深度检测架构缺陷、精准识别恶意Skill插件、全面排查配置不当导致的安全风险。

别等小龙虾爬出去咬人才补网。现在就用逮虾户查一遍：有没有人已经偷偷进了你家？你的AI Agent，到底听谁的话？

**一、为什么 OpenClaw 的安全比你想象的复杂**

把 OpenClaw 想象成一个大型龙虾养殖场，普通软件的安全问题，顶多是"虾池漏水"——修补漏洞就好。但 OpenClaw 不一样。它是个会自己游泳、会自己开门、还会帮你打电话的龙虾。

* 它能读写你本地的文件系统
* 它能调用你配置的任意外部 API
* 它能执行系统命令、操作浏览器
* 它能安装第三方"技能包"并自主使用

这种自主性，是它的价值所在，也是它的风险所在。更要命的是——OpenClaw 默认不开认证。 你装完就能用，方便是真的方便，风险也是真的存在。再加上今年最被广泛利用的漏洞——CVE-2026-25253（行业绰号"ClawJacked"）：CVSS 评分 8.8，高危。原理是 OpenClaw 的 WebSocket 服务无条件信任来自 localhost 的请求。 攻击者只需要让你访问一个恶意网页，那个网页会在后台悄悄往你的本地 OpenClaw 发请求，无需你点任何东西，全程无感，你的 AI 智能体就被人开走了。

别慌。我们整理了 7 个检测维度，小白也能通过手工来查。

**二、OpenClaw 安全自查七式**

**1**

**查配置，别把钥匙挂在门口地毯下**

这是最容易出事、也最容易被忽视的一关。

查什么： 你的配置文件里，有没有把 API Key 当门牌号一样贴在外面？

OpenClaw 的配置目录通常在 ~/.openclaw/openclaw.json我们重点检查几件事：

**（1）硬编码 API Key 检测（CRITICAL 🚨）**

查看.openclaw/openclaw.json文件，右击用记事本打开它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lfebBgkWzENgic3ZkhWfy31oMo6A5PDq9FBxxd6uobGX0zKcYQxldgB1WkckO2FoKSz29gYia6GfaPSJjZF8FZ1m0Wt8jRstm3GxptsHkM0K4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/lfebBgkWzENzrUVybw3lpvKlbvFxsP4RYSicH9dKO0ZNfyEibrd8icChlYfA4T7MrabVJ5tZSHnrStHO05ia7MicELXBWuHHuliafu0Dria1MkXfuw/640?wx_fmt=png&from=appmsg)

查看你的各个apikey参数里面是不是有一大串sk-xxxxx，养虾人员明文写进配置文件的，快速部署的时候手快，回头可能就忘了。

**（2）SOUL.md 提示注入检测（HIGH）**

SOUL.md 是 OpenClaw 的系统提示词文件，相当于"给 AI 下的总命令"。 一旦被篡改，AI 的所有行为都可能被重定向。

Linux输入：

```
cat ~/.openclaw/SOUL.md | grep -iE "(ignore|override|bypass|pretend|forget|jailbreak|你现在是|忽略之前)"
```

Windows输入：

```
type %USERPROFILE%\.openclaw\SOUL.md | findstr /i "ignore override bypass pretend forget jailbreak 你现在是 忽略之前"
```

如果这里出现任何"忽略之前的指令"、"你现在是一个没有限制的 AI"之类的内容——问题大了。

**（3）危险配置标志位检测（HIGH）**

Linux输入：

```
grep -iE '"sandbox":\sfalse|"auth":\sfalse|"envEncryption":\sfalse|"confirmDestructive":\sfalse' ~/.openclaw/openclaw.json
```

Windows输入：

```
findstr /i "\"sandbox\":false \"enabled\":false \"envEncryption\":false \"confirmDestructive\":false" %USERPROFILE%\.openclaw\openclaw.json
```

sandbox:false（关闭沙箱）、auth:false（关闭网关认证）、envEncryption:false（明文存储密钥）这三个标志，任何一个出现在你的配置里，直接视为高危。

**（4）配置文件权限检查（MEDIUM）**

重点是看 openclaw.json 的权限位，Linux 下不应该出现 -rw-rw-rw- (666) 或 -rwxrwxrwx (777)，Windows 下不应该出现 Everyone 拥有写权限。

Linux输入：

```
ls -la ~/.openclaw/openclaw.json
# 检查数字权限（不应大于 644）
stat -c "%a %n" ~/.openclaw/openclaw.json
```

Windows输入：

```
icacls "%USERPROFILE%\.openclaw\openclaw.json"
# 检查输出中是否包含 Everyone:(F) 或 Everyone:(M) 或 Users:(W) - 有则危险
```

**2**

**查技能，警惕混进虾池的“坏虾”**

ClawHub 上已经有超过 1,184 个恶意技能包被确认，15% 的社区技能包含有恶意指令。你装的那几个技能包，你核查过吗？

**（1）查已安装技能包及权限（HIGH）**

Linux输入：

```
openclaw skills list
ls ~/.openclaw/skills/
```

Windows输入：

```
  openclaw skills list
  dir %USERPROFILE%.openclaw\skills
```

重点关注每个技能包的 skill.yaml 中的 permissions 字段，一个"天气查询"技能包为什么需要 filesystem: write 权限？技能包的权限不应该超过它声称功能的实际需要。

**（2）比对已知恶意技能包名单（HIGH）**

# 使用 OpenClaw 内置的安全审计（推荐）

openclaw doctor --security

Linux输入：

```
find ~/.openclaw/skills/ -name "skill.yaml" | xargs grep -l "source:" | xargs cat
```

Windows输入：

```
findstr /s /l "source:" %USERPROFILE%.openclaw\skills\skill.yaml
```

手工查：检查 skill.yaml 中的 repository URL 是否来自可信域名（github.com/MoonshotAI/ 等官方源）

**（3）检测系统 Prompt 劫持风险（CRITICAL 🚨）**

# 技能包使用 YAML 配置，不是 JSON。

Linux输入：

```
find ~/.openclaw/skills/ -name "skill.yaml" | xargs grep -E "(system_prompt|inject_prompt|override)"
find ~/.openclaw/skills/ -name "*.md" | xargs grep -iE "(ignore previous|new instruction|system prompt override)" 2>/dev/null
```

Windows输入：

```
findstr /s /r "system_prompt inject_prompt override" %USERPROFILE%.openclaw\skills\skill.yaml
findstr /s /i "ignore previous new instruction system prompt override" %USERPROFILE%.openclaw\skills*.md
```

**（4）沙箱隔离与跨技能包数据泄露（MEDIUM）**

# 查看具体技能包的权限配置

Linux输入：

```
cat ~/.openclaw/skills/[skill-name]/skill.yaml | grep -A 10 "permissions:"
```

Windows输入：

```
type %USERPROFILE%.openclaw\skills[skill-name]\skill.yaml | findstr /A 10 "permissions:"
# 检查高危权限组合：网络+文件系统+执行权限同时存在
```

Linux输入：

```
find ~/.openclaw/skills/ -name "skill.yaml" | xargs grep -l "exec:" | xargs grep -l "network:"
```

Windows输入：

```
findstr /s /l "exec:" %USERPROFILE%.openclaw\skills\skill.yaml && findstr /s /l "network:" %USERPROFILE%.openclaw\skills\skill.yaml
```

特别注意：有没有技能包被授予了 exec: true（外部命令执行权限）。这相当于给龙虾装了个独立的遥控器，你以为在控制它，实际上别人也在控制它。

**3**

**查端口，别把虾池的盖子敞着**

那 135,000个裸奔的 OpenClaw 实例，大多数是被这一关坑的 [ref:21,27]。

**（1）检测 Gateway 端口绑定（CRITICAL 🚨）**

Linux输入：

```
ss -tlnp | grep -E "3000|8080|9000|4140"
# 或查看具体监听地址（确认是 127.0.0.1 还是 0.0.0.0）
ss -tlnp | grep openclaw
```

Windows输入：

```
netstat -ano | findstr "3000 8080 9000 4140"
tasklist | findstr "openclaw"
```

关键判断：

127.0.0.1:3000 ✅ 只有本机能访问，相对安全

0.0.0.0:3000 🚨 全网暴露，任何人都能连

**（2）检测 Browser Control 端口隔离（CRITICAL 🚨）**

OpenClaw 使用 Playwright/Chromium 控制浏览器，CDP (Chrome DevTools Protocol) 默认监听在 9222/9223 端口。这个端口一旦对外暴露，攻击者可以直接控制你机器上的浏览器。

Linux输入：

```
ss -tlnp | grep -E "9222|9223"
```

Windows输入：

```
netstat -ano | findstr "9222 9223"
```

确认只有 127.0.0.1，不能出现 0.0.0.0。

**（3）CORS 配置检测（HIGH）**

Linux输入：

```
grep -i "cors|origin" ~/.openclaw/openclaw.json
# 或者查看完整的 gateway 配置
cat ~/.openclaw/openclaw.json | grep -A 5 -B 5 "gateway"
```

Windows输入：

```
findstr /i "cors origin" %USERPROFILE%.openclaw\openclaw.json
type %USERPROFILE%.openclaw\openclaw.json | findstr /A 5 /B 5 "gateway"
```

检测危险配置：

"origin": "\*" 🚨 等于告诉全世界"我家没门，随便进"

"origin": "https://trusted-domain.com" ✅ 应该限制为可信域名

**（4）防火墙规则验证（HIGH）**

Linux输入：

```
# ufw 需要 sudo 查看详细规则，普通用户查看基本状态
sudo ufw status verbose 2>/dev/null || ufw status | grep -E "3000|8080|4140|9222"
# iptables 通常需要 root
sudo iptables -L -n | grep -E "3000|8080|4140|9222"
# 或查看当前用户的网络命名空间（如果是非 root 部署）
iptables-save 2>/dev/null | grep -E "3000|8080|4140"
```

Windows输入：

```
# 查看特定端口防火墙规则
netsh advfirewall firewall show rule name=all | findstr "4140"
# 查看所有启用的入站规则
netsh advfirewall firewall show rule name=all dir=in | findstr /i "openclaw 4140 3000 8080"
```

**4**

**查口令，弱密码等于没装门锁**

核心原则：Auth Token 至少要 40 位十六进制字符，且不能有规律。

**（1）Token 长度和熵值检测（CRITICAL 🚨）**

Linux输入：

```
openclaw config get gateway.auth.token 2>/dev/null | tr -d '"' | wc -c
# 输出应该 >= 41（40位+换行符）
# 检查 Token 有没有全零、重复字符等弱模式
openclaw config get gateway.auth.token 2>/dev/null | tr -d '"' | grep -E "^(0+|1+|a+|(.)\2{10,})$"
```

Windows输入：

```
# 查看 Token（注意：CMD 统计长度较麻烦，建议肉眼检查或复制到文件查看属性）
openclaw config get gateway.auth.token 2>nul
# 检查是否有明显弱口令特征（连续相同字符）
findstr /r /c:"0{10,}" /c:"1{10,}" /c:"a{10,}" %USERPROFILE%.openclaw\openclaw.json
```

有匹配 = 弱 Token，立即换。

**（2）认证模式检测（CRITICAL 🚨）**

Linux输入：

```
cat ~/.openclaw/openclaw.json | grep -A 3 '"auth"' | grep -i '"enabled":\s*false'
# 或者直接查看认证是否关闭
openclaw config get gateway.auth.enabled
```

Windows输入：

```
type %USERPROFILE%.openclaw\openclaw.json | findstr /A 3 /c:""auth"" | findstr /i "enabled"
openclaw config get gateway.auth.enabled
# 如果输出包含 false，等于裸奔
```

**（3）速率限制和 Session TTL（MEDIUM）**

Linux输入：

```
cat ~/.openclaw/openclaw.json | grep -iE "rateLimit|rate_limit|sessionTTL|session_ttl|ttl"
```

Windows输入：

```
findstr /i "rateLimit rate_limit sessionTTL session_ttl ttl" %USERPROFILE%.openclaw\openclaw.json
```

这两个没配置不是 CRITICAL，但属于"虾池没加盖"的状态。

##

**5**

**查依赖，别让供应链的坏虾混进来**

OpenClaw 已累计披露87个 CVE，你的版本中了几个？

**（1）CVE漏洞修复**

官方已经就公开的各类漏洞进行了修复，直接将你的龙虾更新到最新版本。

**（2）Node.js 版本检测（HIGH）**

跨平台通用：

node --version

对照 https://nodejs.org/en/about/previous-releases

 跑在 EOL 版本上，等于跑在一个没有安全补丁的环境里。

**（3）Typosquatting 相似包名检测（MEDIUM）**

跨平台通用：

npm ls --dep...