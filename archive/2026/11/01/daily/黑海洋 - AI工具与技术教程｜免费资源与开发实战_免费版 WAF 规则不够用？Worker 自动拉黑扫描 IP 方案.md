---
title: 免费版 WAF 规则不够用？Worker 自动拉黑扫描 IP 方案
url: https://blog.upx8.com/WAF-Worker-IP
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-11-01
fetch_date: 2026-11-02T08:33:01.396097
---

# 免费版 WAF 规则不够用？Worker 自动拉黑扫描 IP 方案

[![黑海洋](https://blog.upx8.com/logo.webp)
黑海洋
WIKI](https://blog.upx8.com/)

[首页](https://blog.upx8.com/)
[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)
[关于](/about.html)

在线工具

[极

**极简文本**
*txt.upx8.com*](https://txt.upx8.com/)
[I

**IP查询**
*ip.upx8.com*](https://ip.upx8.com/)
[哈

**哈希计算**
*blog.upx8.com*](https://blog.upx8.com/app/bs64/#hash)
[U

**USTD交易查询**
*18u.in*](https://18u.in)
[三

**三角洲辅助站**
*sjz.upx8.com*](https://sjz.upx8.com/)
[开

**开发者工具箱**
*tools.upx8.com*](https://tools.upx8.com/)

[首页](https://blog.upx8.com)
/
[资源](https://blog.upx8.com/Free)
/
免费版 WAF 规则不够用？Worker 自动拉黑扫描 IP 方案

# 免费版 WAF 规则不够用？Worker 自动拉黑扫描 IP 方案

[资源](https://blog.upx8.com/Free)
11-01
·
约 38 分钟
·
黑海洋
·

4,029

网站接上 Cloudflare 之后，几乎每天都能在日志里看到一堆莫名其妙的请求：有人在翻 `/database.sql`，有人在找 `/wp-config.php`，还有人在猜 `/.env`。这些不是正常访客，而是自动化扫描器在碰运气——只要你的备份文件恰好放在网站根目录，一次扫描就可能把整站数据带走。

Cloudflare 自带 WAF 可以拦这类请求，但免费版的自定义规则只有 5 条，配几个常用规则就见底了。这篇文章讲一个更省钱的办法：**把判断逻辑放进 Worker，命中规则就返回 403，同时调用 Cloudflare API 把这个 IP 写进 IP Access Rules 黑名单**。免费版够用，配置一次，后面基本不用管。

下面按“完全没接触过 Worker”的角度来写，每一步都说明点哪里、填什么、看到什么算成功。

## 先说清楚：这套方案是怎么工作的

不需要理解代码细节，先建立一个整体印象：

1. 访客的请求到达 Cloudflare。
2. Cloudflare 先跑完你设置好的 WAF 规则，再进入 Worker。
3. Worker 检查这次请求的路径，看看是不是在“敏感文件清单”里。
4. 不在清单里，原样转发给源站，网站照常打开。
5. 在清单里，立刻返回 403，同时调用 Cloudflare API，把这个 IP 加入 IP Access Rules 黑名单。

这里有个关键点值得记住：**IP Access Rules 的黑名单独立于 Worker**。哪天你把 Worker 删了、额度用完了、代码写错了，已经拉黑的 IP 依然会被 Cloudflare 挡在门外。

> 判断逻辑跑在 WAF 之后、CDN 缓存之前，所以对正常页面的影响很小。也正因为要尽量少影响速度，这套代码没有用数据库存状态，只做纯内存的字符串匹配。

### 免费版够不够用

| 项目 | 免费版额度 |
| --- | --- |
| IP Access Rules 规则数 | 每个账号最多 5 万条（各套餐一致） |
| Worker 请求数 | 每天 10 万次，UTC 0 点重置 |
| Worker 单次 CPU 时间 | 10 毫秒（网络等待不计入） |
| 额度归属 | 同一账号下所有 Worker 共享 10 万次 |

10 万次对中小网站是够的。额度用完后 Worker 会停止执行，配合路由里“失败时自动打开”的设置，请求会直接回源，网站照常访问，只是当天不再拉黑新 IP。所以这层防护是“锦上添花”，不会成为单点故障。

## 开始前，先搞懂四个名词

小白最容易卡在这里，其实每个都不复杂：

* **Zone ID（区域 ID）**：Cloudflare 给每个域名分配的唯一编号。API 调用时要告诉它“操作哪个域名”，填的就是这个。
* **API Token（API 令牌）**：给程序用的钥匙。它和你的登录密码不是一回事，可以只授予“防火墙编辑”这一项权限，泄露了危害也有限。
* **Worker**：一段跑在 Cloudflare 边缘节点上的 JavaScript 代码。请求会先经过它，你可以在里面写任意判断逻辑。
* **DRY\_RUN**：演练开关。设为 `true` 时只记录、不真拉黑，适合先跑一遍看看效果。

准备清单：一个已经接入 Cloudflare 的域名（NS 托管或 SaaS 方式 CNAME 接入都行）、能登录 Cloudflare 的账号、10 分钟时间。不需要服务器，不需要装任何软件。

## 第一步：复制 Zone ID

登录 Cloudflare 后台，点进你要配置的域名，进入**概述 / Overview** 页面。

右侧栏拉到最下方，能看到一串 32 位字符，标注为**区域 ID**。英文界面下叫 **Zone ID**。复制下来存到记事本。

![在 Cloudflare 域名概述页右下角复制 Zone ID](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/1ab7e96c02514db0de49f5e59189b8fd.jpg)

*区域 ID 就在域名概览页的右侧栏底部，点一下即可复制。*

## 第二步：创建一个只管防火墙的 API 令牌

还在这个页面，往下找**获取您的 API 令牌**（Get your API token），点进去。

选择**创建令牌**，模板选**自定义令牌**，然后按下面三项填写：

| 字段 | 填什么 |
| --- | --- |
| 令牌名称 | 随便起，比如 `worker-auto-ban` |
| 权限 | 区域 → 防火墙服务 → 编辑 |
| 区域资源 | 选择你要保护的那个域名 |

填完点**继续以显示摘要**，再点**创建令牌**。

![创建 API 令牌时选择区域防火墙服务编辑权限](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/97ffbf38df397a8955dc38eaefd60a18.png)

*权限只需要“防火墙服务 → 编辑”这一项，不要图省事给全局权限。*

> **这一步最容易翻车**：令牌只在创建成功后的那个页面完整显示一次，关掉就再也看不到了。务必先复制到记事本。如果忘了复制，直接删掉重建一个，不要试图找回。

## 第三步：创建一个 Worker

左侧菜单进入 **Workers & Pages**，点**创建应用程序**（Create application）。

![在 Workers & Pages 页面点创建应用程序](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/705ef83eb5ffc68dc66b7088dbf2f38c.jpg)

*入口在 Workers & Pages 页面右上角。*

在模板列表里选择 **Hello World**，也就是“开始使用 Hello World 模板”那个选项。不需要连接 GitHub，也不需要上传文件。

![选择 Hello World 模板创建 Worker](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/bb23644ec7a3d3b0b9840efccd9931eb.jpg)

*模板页有三个选项，选中间那个 Hello World。*

给 Worker 起个名字（比如 `ip-auto-ban`），点**部署**。部署成功后会看到一个默认的 `Hello World` 响应页面。

![填写 Worker 名称并部署](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/28cb1cd50aaac3919b3054960a1089ce.jpg)

*名字随便起，部署后还能改代码。*

## 第四步：把默认代码换成我们的规则

点**编辑代码**进入在线编辑器，把里面默认的几行代码全选删除。

![进入 Worker 在线代码编辑器](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/755f4142ac8316006ee60bdee1b60a30.jpg)

*编辑器左侧是代码区，右上角是部署按钮。*

然后把下面这段代码完整粘贴进去：

```
const CF_API_BASE = "https://api.cloudflare.com/client/v4";

/*
* ==================== CUSTOM DETECTION LIST ====================
* Add one item per line. Blank lines and lines beginning with # are ignored.
*
* Matching rules:
* 1. A filename without / matches that filename in ANY directory.
* Example: database.sql matches /database.sql and /wp-content/uploads/database.sql
* 2. An item containing / is treated as a path and matches that path exactly.
* Example: /wp-content/.env matches only that exact path.
* 3. * is a wildcard (zero or more characters).
* Example: .env* matches .env, .env.local, .env.production, etc.
* 4. Matching is case-insensitive. Items are literal text, not regular expressions.
* 5. `www\\.zip` is also accepted and normalized to `www.zip` for convenience
* when copying paths that have escaped dots in Markdown or logs.
*
* Be cautious with broad entries such as *.zip or *.sql: they may match legitimate
* downloads. Start with specific filenames and paths, then customize as needed.
*/
const SENSITIVE_ITEMS_TEXT = String.raw`
# Environment/configuration files
.env
.env.local
.env.production
.env.development
.env.staging
wp-config.php
wp-config-sample.php
/wp-content/.env
/wp-includes/.env
/wp-content/plugins/.env
/wp-content/themes/.env
/.git/config

# Database files and exports
database.sql
database.sql.gz
database.sqlite
database.sqlite3
database.zip
database-dump.sql
database-backup.zip
db.sql
db.sql.gz
db.zip
db_backup.sql
db_backup.zip
data.db
data.sql
data.sqlite
data.sqlite3
mysql.sql
mysql.sql.gz
mysql.zip
backup.sql
backup.sql.gz
backup.sql.zip
backup.tar.gz
backup.zip
backup.7z
backup.rar
backup.bak
dump.sql
dump.zip
site.sql
site.zip

# Website/source archives from common scanner probes
cheshirex.zip
cheshirex.com.zip
wordpress.zip
wp.zip
www\.zip
wwwroot.zip
webroot.zip
public_html.zip
htdocs.zip
html.zip
source.zip
full.zip
archive.zip
archives.zip

# Add your own entries below, one per line
`;

function normalizePath(rawPath) {
  let path = String(rawPath || "/");

  // Decode encoded paths (including double-encoded probes) safely, at most twice.
  for (let i = 0; i < 2; i++) {
    try {
      const decoded = decodeURIComponent(path);
      if (decoded === path) break;
      path = decoded;
    } catch {
      break;
    }
  }

  // Interpret escaped-dot paths such as /www\\.zip as /www.zip, then canonicalize slashes.
  path = path
    .replace(/\\\./g, ".")
    .replace(/\\/g, "/")
    .replace(/\/{2,}/g, "/")
    .toLowerCase();

  if (path.length > 1) path = path.replace(/\/+$/, "");
  return path || "/";
}

function globToRegExp(pattern) {
  const escaped = pattern.replace(/[|\\{}()[\]^$+?.]/g, "\\$&");
  return new RegExp(`^${escaped.replace(/\*/g, ".*")}$`, "i");
}

function buildDetectionList(text) {
  return text
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter((line) => line && !line.startsWith("#"))
    .map((rawItem) => {
      // Allow `www\\.zip` from escaped Markdown/log tables to mean `www.zip`.
      let item = rawItem.replace(/\\\./g, ".").trim().toLowerCase();
      const isPath = item.includes("/");

      if (isPath) {
        if (!item.startsWith("/")) item = `/${item}`;
        item = normalizePath(item);
      }

      return {
        rawItem,
        item,
        isPath,
        matcher: globToRegExp(item),
      };
    });
}

const SENSITIVE_ITEMS = buildDetectionList(SENSITIVE_ITEMS_TEXT);

function detectSensitivePath(path) {
  const segments = path.split("/").filter(Boolean);
  const basename = segments.length ? segments[segments.length - 1] : "";

  const matched = SENSITIVE_ITEMS.find((entry) => {
    return entry.isPath
      ? entry.matcher.test(path)
      : entry.matcher.test(basename);
  });

  if (!matched) return null;

  return {
    reason: "configured sensitive item",
    matchedItem: matched.rawItem,
  };
}

function forbiddenResponse() {
  return new Response("Forbidden", {
    status: 403,
    headers: {
      "Content-Type": "text/plain; charset=UTF-8",
      "Cache-Control": "no-store",
      "X-Cont...