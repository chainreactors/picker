---
title: 新型 Evilginx 前端：降低 token 窃取与复用的门槛
url: https://mp.weixin.qq.com/s/SDe1SqzXZZDMC89FpOJlRQ
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:59:31.388563
---

# 新型 Evilginx 前端：降低 token 窃取与复用的门槛

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSjPmFqTh2vTu5dABxibWvWDVNzJ0r0rk2KROtrmWn1dno2qNctvic1vKibicXPyicPIqRhmuZMOicBl0mBhMtbh9JEEn6DkKtZFRuzts/0?wx_fmt=jpeg)

# 新型 Evilginx 前端：降低 token 窃取与复用的门槛

Newton Paul
Newton Paul

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://newtonpaul.com/blog/evilginx-m365-aitm-panel-research/ | Newton Paul |

最近我在威胁狩猎方面收获颇丰，在 C2 狩猎、钓鱼狩猎之间来回切换，并且在将工具迁移到新基础设施后重新启动了我的 NPM 恶意包狩猎工作。有意思的是，最近几天我观察到基础的、由 AI 生成的 NPM 恶意软件大幅增加，我怀疑这种势头还会持续上升。Team PCP 推出了悬赏入侵 NPM 包的竞赛，这很可能会加剧这一趋势，因为更多的攻击者被激励去针对这个生态系统。我已经在 newtonpaul.com/npm-packages/ 上发布了一些近期的 NPM 发现，后续还会有更多内容。

进入今天的正题！

---

## 用于 Microsoft 365 账户接管的全新 Evilginx 面板

在持续狩猎野外 C2 的过程中，我偶然发现了一个托管在 DigitalOcean 基础设施上的有趣目标。乍一看它就像一个暴露在外的 Outlook Web 邮箱，差点把我骗过去，但很快就明显看出它远不止于此 —— 尤其是当我正在追踪 Evilginx 基础设施的时候。

这套工具有意思的地方在于其 UI 上所投入的精力，目的是让操作者的使用体验与真实的 Microsoft 界面如出一辙。该工具将 Microsoft 365 的身份认证功能利用到了极致以实现最大影响，同时为操作者保持简洁的使用体验：一个被窃取的 bearer 令牌即可通过统一的 API 接口在一个干净的 UI 中同时访问受害者有权限的每一个 M365 服务 —— 邮件、文件、Teams、SharePoint、管理功能。

![仿照 Outlook Web App 风格设计的 M365 AiTM 面板主界面](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjbCs4uibvdzJ9hJPX2vBKC0rJnicgYtn1kXtweLUKu9C9j5zRvWVb5oGAMAvq9oV4Ec1ukqGdMcrSe3icnncuvicwPycYg1GshODc/640?wx_fmt=png&from=appmsg)

仿照 Outlook Web App 风格设计的 M365 AiTM 面板主界面

面板主界面 —— 一个像素级还原的 Outlook 克隆，用于大规模管理被盗账户

让我们深入了解细节。

---

## 发现

我们识别出三台 DigitalOcean 实例，均位于 Santa Clara, California 区域（ASN 14061），在 3000 端口上提供完全相同的内容：

```
142.93.84.22:3000    — First seen 2026-05-15 (active)
147.182.224.35:3000  — First seen 2026-04-22
64.227.54.101:3000   — First seen earlier
```

这三台主机返回完全相同的 HTTP 响应头，内容长度均为 **338,882 字节**—— 即完整的单文件面板 HTML/JS 应用程序。这是一个一致的指纹特征。

```
HTTP/1.1 200 OK
Content-Length: 338882
Content-Type: text/html; charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET,POST,OPTIONS
Access-Control-Allow-Headers: Content-Type, Authorization
```

通配符 `Access-Control-Allow-Origin: *`与允许头部中的 `Authorization`相结合，是一个重要的指示信号 —— 这种刻意宽松的配置是为了支持面板的 Graph API 代理功能。

其中一个 IP 还托管了域名 `cdn.greenrlse.com`，该域名会重定向到一个 YouTube Rickroll 视频。我最初以为这个工具可能是一个意外暴露的红队工具，但 Rick 的出现表明它更有可能出自恶意攻击者之手。还有几个迹象进一步证实了这是一个威胁攻击者工具，而非红队部署：

* 面板的添加账户工作流中明确写着：*"Token from Telegram notification"*—— 合法的红队人员不会通过 Telegram 机器人接收令牌
* 90 天的服务端令牌保活机制并不是红队交付项目所具备的特性 —— 交付项目通常不会持续 90 天（在大多数情况下）
* `.m365db`

  令牌数据库导出功能意味着在不同操作者之间具备可移植性，这与犯罪生态中的令牌买卖或共享行为一致
* 在 DigitalOcean 上托管三台地理分布式的完全相同的实例，也不像是红队的典型行为

---

## 架构：三层如何相互连接

此面板是三层攻击链中的一个组件。钓鱼基础设施与操作者面板是分离的 —— 此处识别出的三个 DigitalOcean IP **并非**受害者交互的钓鱼服务器。

![展示三层 AiTM 攻击链的示意图：Evilginx 钓鱼服务器、操作员面板，以及 Microsoft Graph API](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6ApCdFqjZqoGyAk3KvtrjaevibTz2yGxmZRYSEl4JGgKhvROsJZL2LcHs8ua1fGblbr4ZvO3a8ZE3te9ic9ahdOPKOEfBWoSpx8T5XKay44tGQ/640?wx_fmt=svg&from=appmsg)

展示三层 AiTM 攻击链的示意图：Evilginx 钓鱼服务器、操作员面板，以及 Microsoft Graph API

三层 AiTM 攻击链 —— Evilginx 在上游捕获令牌，面板负责管理令牌，Graph API 提供访问接口

---

## 它是什么

该面板是一个单文件 HTML/JavaScript 应用程序，以像素级精度仿冒 Microsoft Outlook 网页客户端，仅有少量改动。需要明确的是，UI 并非用于欺骗受害者。这个伪造的 Outlook UI 为大规模浏览和操作被盗的 Microsoft 365 账户提供了一个熟悉的界面。

![面板加载数据库文件的屏幕截图](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSiaGficrtd33TMGLtPuGzlkc2xNTsNic5Re0IHO6d8TUayxtkJ62oYljwkByHfylRKx2WgYlmWZYyWSAu3z8P73pxiaQD7ThL3eHEs/640?wx_fmt=png&from=appmsg)

面板加载数据库文件的屏幕截图

Outlook UI 变体，展示令牌的加载与卸载。

在 Outlook 外观之下，该应用程序是一个完整的 Microsoft Graph API 客户端，它使用被盗的 bearer 令牌进行身份验证，而非合法的用户会话。

---

## Evilginx 集成：Feed API

最具技术亮点的功能是与 Evilginx Pro feed API 的原生集成 —— 这是 Evilginx 商业版独有的功能，开源版本中并不存在。这意味着操作者要么合法地通过了 Evilginx Pro 的人工审核流程、随后将其用于犯罪用途，要么是通过二级渠道获取了授权许可。

该面板会按照可配置的时间间隔（15 秒到 5 分钟）轮询 feed 接口，并在新捕获的 token 从正在进行的钓鱼活动中到达时自动导入。从操作者的视角来看，受害者账号会在受害者完成钓鱼流程的瞬间实时出现。

```
https://<evilginx-server>/api/v1/feed?key=<api_key>
```

我们可以在下方截图的 UI 中看到这一点。

![Evilginx feed API 配置面板，显示了接口 URL 与轮询时间间隔设置](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSh9CvzpgBIGWQfib9LYA6kibMsQeqHWaKHLJLw4DrGO6zNJMpR554ITs3Jxo5GHr5m2MAFdS0j7y13nqXF1HkPonmAq6WUZSEvRg/640?wx_fmt=png&from=appmsg)

Evilginx feed API 配置面板，显示了接口 URL 与轮询时间间隔设置

Evilginx Pro feed API 配置 —— 该面板按照可配置的时间间隔轮询新 token

AiTM 捕获层与后渗透管理层之间的这种耦合，代表着工具链的一次成熟化。以往，操作者需要手动从 Evilginx 中提取 token，再导入到独立的工具中。而这个面板则将这一断层弥合为单一且无缝的工作流。

---

## token 生命周期管理

一旦导入，该面板便会通过若干机制来管理 token 的生命周期：

**Refresh token 持久化**—— 如果 refresh token 与 access token 一同被捕获（Evilginx 在条件允许时会一并捕获），面板会在后台静默续签 access token。这样便可在无需对受害者再次钓鱼的情况下无限期地维持访问权限。

**CORS 代理绕过**—— 浏览器直连 Microsoft 的 token 刷新调用会被 CORS 策略阻断。面板附带了一个名为 `refresh-proxy.js`的辅助脚本，该脚本在本地运行以中继刷新请求，从而绕过这一浏览器限制。

**数据库可移植性**—— 所有已捕获的账号和 token 都可以导出为 `.m365db`文件（JSON 格式），并可重新导入到该面板的任意其他实例中。这一机制方便了操作者之间共享或贩卖 token，与犯罪 Telegram 频道中观察到的 token 交易市场生态一致。

我们可以在代码中看到 Microsoft Office 的 Client ID，这是一款 FOCI 应用 —— 也是 token 刷新过程中所默认使用的：

```
const MS_CLIENT_ID = 'd3590ed6-52b3-4102-aeff-aad2292ab01c';
```

具体实现如下，这里会为该应用请求 refresh token：

```
constbody=newURLSearchParams({
client_id:clientId,
grant_type:'refresh_token',
refresh_token:acc.refreshToken,
scope:'https://graph.microsoft.com/.default offline_access'
});

constresp=awaitfetch(
`https://login.microsoftonline.com/${tenant}/oauth2/v2.0/token`,
    {
method:'POST',
headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
body:body.toString()
    }
);

accounts[idx].accessToken=data.access_token;
if (data.refresh_token) {
accounts[idx].refreshToken=data.refresh_token;
}
accounts[idx].tokenRefreshedAt=newDate().toISOString();
```

此外还提供了一个用以覆盖该默认值的选项 —— 可以为每个账号单独设置 Client ID，从而允许使用其他应用所对应的 refresh token。这考虑到了 Evilginx 在 token 捕获行为上的差异。

```
asyncfunctionrefreshToken(idx) {
constacc=accounts[idx];
if (!acc.refreshToken) return;
constclientId=acc.clientId||MS_CLIENT_ID;
consttenant=acc.tenantId||'common';
constproxyUrl=getRefreshProxyUrl();

try {
letdata;
if (proxyUrl) {
constresp=awaitfetch(proxyUrl, {
method:'POST',
headers: { 'Content-Type': 'application/json' },
body:JSON.stringify({
refresh_token:acc.refreshToken,
client_id:clientId,
tenant:tenant
                })
            });
data=awaitresp.json();
if (!resp.ok) {
thrownewError(data.error_description||data.error||'Refresh failed');
```

---

## 单一令牌问题：为何这件事至关重要

由于 Microsoft Graph API 身份验证的特性，单个有效的 bearer 令牌即可用于访问该用户具备权限的所有 Microsoft 365 服务。下面是该面板所使用的部分 API 端点：

```
graph.microsoft.com/v1.0/me/messages          → Full mailbox
graph.microsoft.com/v1.0/me/drive/root        → All OneDrive files
graph.microsoft.com/v1.0/me/joinedTeams       → All Teams and channels
graph.microsoft.com/v1.0/sites                → All SharePoint sites
graph.microsoft.com/v1.0/me/onenote           → All OneNote notebooks
graph.microsoft.com/v1.0/me/contacts          → Full contacts list
graph.microsoft.com/v1.0/me/calendar          → Calendar and events
graph.microsoft.com/v1.0/users               → Tenant user directory (if admin)
graph.microsoft.com/v1.0/auditLogs           → Audit logs (if admin)
```

完整的工具面板如下所示。

![面板应用启动器，显示所有可用 M365 服务跳转入口的图标，包括 Outlook、OneDrive、Teams 和 Admin Center](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShXSw7fut6N9m6ysOv7agMnuQ2u9d4xabVA3EYauLFxogRpgep5LuLmjYBKSXvOS5Ya8uQTq3WY02QKbJkDic0OBFEAsuuibemYs/640?wx_fmt=png&from=appmsg)

面板应用启动器，显示所有可用 M365 服务跳转入口的图标，包括 Outlook、OneDrive、Teams 和 Admin Center

面板应用启动器 —— 每个图标都是通往不同 Microsoft 365 数据源的实时跳转入口，全部由同一个 bearer 令牌提供支持

| 面板功能 | Graph API 接口 | 数据风险 |
| --- | --- | --- |
| Outlook | `/me/messages` , `/me/mailFolders` | 全部邮件、附件、收件箱规则 |
| OneDrive | `/me/drive` | 全部文件、文档、备份 |
| SharePoint | `/sites` | 团队站点、文档库 |
| Teams | `/me/joinedTeams` , `/chats` | 消息、共享文件、会议录制内容 |
| OneNote | `/me/onenote/notebooks` | 笔记，常常包含密码和密钥 |
| Contacts | `/me/contacts` | 完整通讯录 |
| Calendar | `/me/calendarView` | 会议、地点、与会者 |
| My Account | `/me/authentication/methods` | MFA 配置 |
| Admin Center | `/users` , `/auditLogs`, `/subscribedSkus` | 整个租户（若为管理员令牌） |

凭借一个被窃取的 Graph API bearer 令牌，上述所有内容都可以通过直接的 API 调用进行访问。当操作者在 Outlook 风格的 UI 中浏览时，该面板会在后台静默发起这些调用。从 Microsoft 的视角来看，这就像一个经过合法身份验证的应用程序代表用户访问数据。

### 管理员令牌场景

如果被钓鱼的受害者持有特权 Entra ID 角色 —— 例如 Global Administrator、Exchange Administrator 或类似角色 —— 影响范围将扩展至整...