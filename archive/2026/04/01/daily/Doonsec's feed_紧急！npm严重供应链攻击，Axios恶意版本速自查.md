---
title: 紧急！npm严重供应链攻击，Axios恶意版本速自查
url: https://mp.weixin.qq.com/s/OXtESeDxqEHA-GLIcwnNWQ
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:28:27.799342
---

# 紧急！npm严重供应链攻击，Axios恶意版本速自查

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uX9TOlqibIRsZwXfXRc3Hiahm0n3jjVibmuJxPNTJl6icxkianSXz5ztib7fQibHVlgWTFibjx6Ybb02D7vL03bGpM0sq7Pg2Vqe5YYfWqnVBF7Dywo/0?wx_fmt=jpeg)

# 紧急！npm严重供应链攻击，Axios恶意版本速自查

长亭安全观察

![]()

在小说阅读器中沉浸阅读

![头图for长亭安全观察.gif](https://mmbiz.qpic.cn/sz_mmbiz_gif/uX9TOlqibIRs5XLia7I75V1cHibR6Bgwlymwa3WdSfQb3j6l5G89fRsQPTiab551etUgj4vEeXAzKhu0yDKnBXOybKRsrU8eeRT8ITEswAoE3Oo/640?from=appmsg)

3 月 31 日，npm 生态爆发迄今规模最大的供应链投毒事件之一。

周下载量超 1 亿次的 HTTP 客户端库 Axios，被攻击者通过核心维护者账号劫持，发布恶意版本植入跨平台远程控制木马（RAT）。事件暴露了开源生态供应链安全的系统性漏洞，影响面覆盖前端、Node.js 服务、CI/CD 流水线等全链路。

以下是来自“长亭安全应急响应中心”的完整事件分析与处置指南。

---

3月31日凌晨，HTTP 客户端库 axios 被攻击者成功投毒，两个恶意版本（`axios@1.14.1`和 `axios@0.30.4`）在不到40分钟内相继发布，覆盖了 axios 的 1.x 和 0.x 两条主要维护分支。

攻击者并非利用 axios 本身的代码漏洞，而是采用了账户劫持 + 幽灵依赖注入 + postinstall 钩子执行的三段式攻击链，将一个名为 `plain-crypto-js`的恶意伪装包悄无声息地注入到 axios 的依赖树中。

一旦开发者或 CI/CD 流水线执行 `npm install`，恶意投递器便会立刻启动，针对 macOS、Windows、Linux 三个平台分发差异化的第二阶段远程控制载荷，并在完成后主动抹去自身痕迹。

![图片](https://mmbiz.qpic.cn/mmbiz_png/EqS9GE77r0NXiaAwsIZA0QegbMeQJJjoGdbmJnJOlwVpwQV4Qg34s9sVM1g23G63hzbITZ6OdqUadH88ZLhG4vdkIWCax1gKG0mpRxWZDKibE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/EqS9GE77r0PL8ohELDhbhCY0icTYS5xgeSa6W8FWcyoMRn22cgwibPHk14FO16GW9UfAxSTKQvB6kjgdUt7Qupe5Aw9fuUnhfJucFPwbXia6bM/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

 影响面分析

为什么是 axios?

axios 不是一个普通的 npm 包，它是现代 JavaScript/TypeScript 生态的基础设施级依赖：

* 直接下载量：周下周量超过1亿次，是 npm 排名前列的包之一
* 间接依赖渗透：无数前端框架、Node.js 后端服务、CLI 工具、CI/CD 脚本将 axios 声明为直接或间接依赖，实际受影响用户基数远超直接下载数字
* 跨生态覆盖：React/Vue/Angular 项目、Express/Fastify 后端、AWS Lambda、Serverless 函数、Docker 镜像构建流程均可能受波及
* 双分支投毒：攻击者同时污染 `1.x`（当前主流版本）和 `0.x`（历史版本，仍有大量项目未迁移），确保最大覆盖面

### 高风险场景

|  |  |  |
| --- | --- | --- |
| 场景 | 风险等级 | 说明 |
| CI/CD 流水线（无版本锁定） | 极高 | 每次构建自动拉取最新版，直接在流水线环境执行恶意代码，泄露所有 CI secrets |
| 使用 `npm install axios`无锁文件 | 极高 | 直接拉取恶意版本 |
| Docker 镜像构建（含 `npm install`） | 高 | 恶意代码在构建阶段执行，泄露构建环境凭证 |
| 开发者本地环境 | 高 | 本地存储的 SSH 密钥、云凭证、.env 文件面临泄露风险 |
| 已锁定版本但依赖 axios 的上游包升级 | 中 | 若上游包升级时引入受污染的 axios 版本 |

关键判定：受影响时间窗口为 2026-03-31 00:21(UTC) 至包被下架之间。凡在此期间执行过 `npm install`且未锁定安全版本的环境，均应视为已完全沦陷。

---

攻击链路详解

### 第一步：盗号入场——账户凭证劫持 攻击的起点是对 axios 主要维护者 jasonsaayman的 npm 账户实施凭证窃取。攻击者在成功接管账户后，随即将其注册邮箱替换为攻击者控制的 ProtonMail地址：`ifstap@proton.me`，完成账户归属的静默转移。 这一步与 axios 的正常发布流程存在显著差异，是事后溯源的关键线索： ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/EqS9GE77r0PkO6MPSWAgXwnM53TYPFdf8NdvOKcAQhicPOkjbYVErMSTYU07jj2cibYJHmy8Vj8zXb8k2fsMeoNskEJ05zxEDeFibQ3B4Ps4CQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

###

### 第二步：暗度陈仓——伪装合法包预热

攻击者在发动主攻前12小时，抢先发布了诱饵版本：

```
2026-03-30 05:57 UTC  →  plain-crypto-js@4.2.0 发布                   （无恶意代码，目的是通过 npm 审核、建立合法声誉）2026-03-30 23:59 UTC  →  plain-crypto-js@4.2.1 发布                    （恶意代码：加入 postinstall: node setup.js）
```

`plain-crypto-js`被精心伪装成知名密码学库 `crypto-js`：

* 相同的包描述文字
* 相同的作者名（伪造为 `Evan Vosberg`，即 crypto-js 真实作者）
* 指向 crypto-js 的 GitHub 地址（`github.com/brix/crypto-js`）

包的发布账户为 `nrwise`（`nrwise@proton.me`），同为攻击者控制账号，与劫持的 jasonsaayman 账户相互配合，形成"攻击者账号提供恶意依赖 + 劫持账号注入依赖"的分工结构。

### 第三步：借刀注毒——恶意依赖注入

完成铺垫后，攻击者利用劫持的 jasonsaayman 账户，向 npm 推送两个毒化版本：

```
2026-03-31 00:21 UTC  →  axios@1.14.1 发布                      （注入 plain-crypto-js@^4.2.1）2026-03-31 01:00 UTC  →  axios@0.30.4 发布                      （同样注入恶意依赖，用时仅39分钟）
```

```

```

依赖注入对比：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/EqS9GE77r0N5Ws2hIKCfspr4WQhv3OYWCwvdHDRApFwn3AAyCopLhb9wiaUcPItGkQp96M7ju1EavMkHrbQ4puLS2fLOnhibo5ElldvJ3ggGs/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

### 第四步：触发载荷——postinstall 钩子执行

当用户执行 `npm install`时，npm 在完成 `plain-crypto-js`的文件落地后，会自动触发其 `package.json`中声明的 `postinstall`脚本：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/EqS9GE77r0PDBTfLPa9dHSSN6aOKLpMvSYtTm8WicjLMRnlx7tzmBANlecrcKS4vvibIDnhTY68N5MbaaC96G7PMX3cxV8lYZ3kXC4lYAPBxA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

 恶意载荷技术分析

* ### 投递器（setup.js）混淆机制解析 `setup.js`采用双层字符串混淆架构，旨在规避静态分析工具和人工代码审计。

#### 混淆层一：XOR 加密字符串数组

所有敏感字符串（URL、命令、路径、shell 脚本片段）均以密文形式存储于 `stq[ ]`数组，运行时通过 `_trans_1()`函数动态解密：

```
// 解密函数逻辑（已还原，非原始代码）// 密钥字符串："OrDeR_7077"（有效字节序列：[0,0,0,0,0,0,7,0,7,7]）function _trans_1(x, r) {    // 对字符串 x 中每个字符执行：    // charCode XOR key[(7 × r × r) % 10] XOR 333    // 其中 key 为密钥字符串各字符的 charCode 值}
```

```
混淆层二：Base64 + 字符替换 + XOR 复合变换
```

部分字符串使用二次加密，通过 `_trans_2()`函数处理：

```
解码流程（逆向还原）：① 将原始字符串进行反转（reverse）② 将所有 _ 字符替换为 = 字符（修复 Base64 padding）③ 对结果执行 Base64 解码④ 将解码结果再传入 _trans_1() 完成最终 XOR 解密
```

```
两层混淆的组合使用，使得字符串无法被简单的正则匹配或字符串搜索识别。攻击者显然对 npm 包安全扫描器的检测逻辑有针对性的了解。
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/EqS9GE77r0O2WP4ibr675gmrHWlNib1dxLds1YpEr5pBcGvK0Smia7yqCXD9b5mxljicQIqmZWKK2NNXr8SxzyicmTtXJwiaeKzHs8YO6tK0vSYJE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

* ### 平台差异化载荷投递

投递器在运行时通过 `process.platform`判断当前操作系统，分发三套完全不同的执行路径，确保对 macOS、Windows、Linux 三大平台均具备攻击能力：

![图片](https://mmbiz.qpic.cn/mmbiz_png/EqS9GE77r0PEKnwBSeXbsDibjNyVibcccvjqk1LpenaKickaNMu1DrnGopAVHCKq67Z8JoGicI1PibAYqtt9FJBT8xmKdZpBzMhx5ibouDb1wibbzE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

* ### 自删除反取证机制

这是本次事件中技术成熟度最高的细节之一。投递器在完成载荷投递后，执行三步自我清除，消除 npm 留在磁盘上的恶意痕迹：

```
// 第一步：删除投递器自身fs.unlink(__filename, () => {});// 第二步：删除含 postinstall 钩子的恶意 package.jsonfs.unlink(path.join(__dirname, 'package.json'), () => {});// 第三步：将干净的存根文件重命名为 package.json// package.md 是预先准备的 4.2.0 干净版本存根fs.rename(  path.join(__dirname, 'package.md'),  path.join(__dirname, 'package.json'),  () => {});
```

```
执行完成后，node_modules/plain-crypto-js/目录呈现出一副"从未安装过 4.2.1 恶意版本"的伪装状态：setup.js消失，package.json显示的是干净的 4.2.0 信息，postinstall字段不复存在。
```

```

```

这一设计使得事后取证极为困难——除非在 npm install 运行时实施进程级监控，否则仅凭磁盘文件无法判断是否曾经触发过恶意代码。

 自查与处置建议

### 检查 npm 安装日志

```
# 查看 npm 最近的操作日志cat ~/.npm/_logs/*.log | grep -E "(plain-crypto-js|axios@1\.14\.1|axios@0\.30\.4)"# 检查 npm 缓存中是否有受影响版本npm cache ls | grep -E "(plain-crypto-js|axios@1\.14\.1|axios@0\.30\.4)"
```

###

### CI/CD 环境检查

若使用 GitHub Actions，检查工作流日志中是否出现以下特征：

* 在 `npm install`步骤中出现非预期的 curl 进程
* 出现 `node setup.js`执行记录
* 出现对 `sfrclak.com`域名的网络请求（若启用了出站流量监控）

```

```

处置建议

第一优先级：降级至安全版本

```
# 主版本（1.x）降级npm install axios@1.14.0# 旧版本（0.x）降级npm install axios@0.30.3# 锁定版本（添加至 package.json overrides，防止间接依赖升级）# 在 package.json 中添加：{  "overrides": {    "axios": "1.14.0"  }}# yarn 用户使用 resolutions{  "resolutions": {    "axios": "1.14.0"  }}
```

第二优先级：清除恶意包残留

```
# 删除 plain-crypto-js 目录（即便已自删除 setup.js，目录本身可能残留）rm -rf node_modules/plain-crypto-js# 清除 npm 缓存中的受污染版本npm cache clean --force# 重新安装（--ignore-scripts 阻止 postinstall 脚本执行）npm ci --ignore-scripts
```

第三优先级：清除平台持久化文件

```
# macOSrm -f /Library/Caches/com.apple.act.mond# Windows（PowerShell，以管理员权限执行）Remove-Item -Force "$env:PROGRAMDATA\wt.exe" -ErrorAction SilentlyContinueRemove-Item -Force "$env:TEMP\6202033.vbs"  -ErrorAction SilentlyContinueRemove-Item -Force "$env:TEMP\6202033.ps1"  -ErrorAction SilentlyContinue# Linuxkill -9 $(pgrep -f "/tmp/ld.py") 2>/dev/nullrm -f /tmp/ld.py
```

```

```

⚠️ 重要警告：删除上述文件不等于系统安全。第二阶段载荷（`ld.py`、PS1 脚本、macOS 二进制）可能已经在系统中建立持久化机制。如确认触发了载荷，应将设备视为完全沦陷，建议重装系统。

### 凭证全面轮换

若判定系统已被触发载荷，必须通过另一台未受影响的设备立即轮换以下所有凭证：

|  |  |  |
| --- | --- | --- |
| 凭证类型 | 轮换优先级 | 说明 |
| npm 发布 Token | 最高 | 防止攻击者以你的名义发布恶意包（对 npm 维护者尤为重要） |
| AWS/GCP/Azure Access Key | 极高 | 云凭证是高价值目标，立即吊销并重新生成 |
| CI/CD Secrets（GitHub/GitLab/Jenkins） | 极高 | CI 环境是本次攻击的主要触发场景 |
| SSH 私钥 | 高 | 重新生成密钥对，更新所有服务器的 authorized\_keys |
| .env 文件中的所有密钥 | 高 | 数据库密码、API Key、JWT Secret 等 |
| 容器镜像仓库凭证 | 高 | Docker Hub、ECR、GCR 等 |
| Git 平台 PAT/OAuth Token | 中 | GitHub、GitLab、Bitbucket 个人访问令牌 |

###

### CI/CD 强化措施

```
# GitHub Actions 示例：启用 --ignore-scripts 并锁定版本- name: Install dependencies  run: npm ci --ignore-scripts  # 阻止所有 postinstall/preinstall 脚本
```

### 网络层防护（立即封锁）

```
在防火墙、Web 应用防火墙、DNS 解析器、安全组等网络控制层面封锁以下指标：# 封锁域名（DNS 层）sfrclak.com# 封锁 IP（防火墙层）142.11.206.73# 封锁 URL 前缀（若有 URL 过滤能力）http://sfrclak.com:8000/
```

---

 IOC

![图片](...