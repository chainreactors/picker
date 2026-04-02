---
title: 弱弱的问一下，我的网站怎么被镜像了嗫？
url: https://zhongxiaojie.cn/2026/04/768/
source: obaby 𝐢‍𝐧⃝ void
date: 2026-04-01
fetch_date: 2026-04-02T04:29:22.121699
---

# 弱弱的问一下，我的网站怎么被镜像了嗫？

[![obaby 𝐢‍𝐧⃝ void](https://zhongxiaojie.cn/wp-content/uploads/2026/01/new-logo-27.png)](https://zhongxiaojie.cn)

程序媛 / 独立开发者 / 智商不稳定的女神经

* [❈闺蜜圈|Pink Daily❈](https://zhongxiaojie.cn/pinkdaily/)
* [❈说说|Tweet❈](https://zhongxiaojie.cn/tweet/)
* [❈留言|Talk❈](https://zhongxiaojie.cn/talk/)
* [❈集美们|Besties❈](https://zhongxiaojie.cn/besties/)
* [❈关于|About❈](https://zhongxiaojie.cn/about/)

 [Menu](#mobilemenu)

* [❈闺蜜圈|Pink Daily❈](https://zhongxiaojie.cn/pinkdaily/)
* [❈说说|Tweet❈](https://zhongxiaojie.cn/tweet/)
* [❈留言|Talk❈](https://zhongxiaojie.cn/talk/)
* [❈集美们|Besties❈](https://zhongxiaojie.cn/besties/)
* [❈关于|About❈](https://zhongxiaojie.cn/about/)

[程序媛](https://zhongxiaojie.cn/category/code-girl/)

# 弱弱的问一下，我的网站怎么被镜像了嗫？

2026年4月1日 11:18
[66 条评论](https://zhongxiaojie.cn/2026/04/768/#comments)

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/330A0374-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/330A0374.jpg)

其实网站被镜像这件事情，本身没什么稀奇的，如果想搭建一个镜像网站，从零开始也不过个吧小时的时间。

之所以写这个东西，是因为最近有看到好几个人被镜像的，[这一个（爱娃子）](https://www.aiwazi.com/2986.html)，还有 [这一个](https://me.xu19.com/mirror-blog/)（我是军爸）。

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260401-110831.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260401-110831.jpg)

不过，既然还有人有疑惑，那就简单的教一下大家怎么来镜像个网站吧。

为此，我创建了一个开源项目：

### OpenResty + OpenCC 反向代理简繁转换

---

基于 **OpenResty** 反向代理上游站点，对 **HTML 正文** 做 **OpenCC** 简繁转换（默认：**简体 → 繁体**，配置文件为 `s2t.json`）。适合在不改源站的情况下，为访客提供另一种字体习惯版本。

## 功能概览

| 能力 | 说明 |
| --- | --- |
| **反向代理** | HTTPS 回源（示例站点：`zhongxiaojie.cn`），客户端走本机证书与域名。 |
| **HTML 简繁转换** | 仅当 `Content-Type` 含 `text/html` 时对整页做 OpenCC UTF-8 转换。 |
| **gzip 解压** | 通过 Lua `zlib` 尝试解压响应体（与去掉 `Content-Encoding` 的配合视上游行为而定）。 |
| **链接与图片 URL 保护** | 转换前将 `href` / `src` / `poster` / `data-src` / `srcset` 及裸 `http(s)://` 链接替换为占位符，转换后还原，**避免路径或查询串中的汉字被改写导致 404**。 |
| **IPv4 优先解析** | `resolver … ipv6=off` + 变量 `proxy_pass`，减轻云主机无 IPv6 时对 AAAA 连接失败的问题。 |
| **静态资源直过** | 图片、CSS、JS、字体等扩展名单独 `location`，**不做** OpenCC，减轻负担、避免误伤二进制。 |
| **动态库加载** | 对 `libopencc.so` 按常见路径依次尝试 `ffi.load`，降低找不到共享库的概率。 |

### 限制与说明

* **JSON / JS / CSS 内嵌字符串**若不在上述保护规则内，仍可能被转换；重要数据建议不要用全文 HTML OpenCC 硬转。
* **内联样式** `style="background:url(...)"` 未单独做保护，若遇少数破图可再扩展规则。
* 转换配置在 `nginx/opencc/opencc-filter.lua` 中的 `OPENCC_CONFIG`（默认 `/usr/share/opencc/s2t.json`）；若需 **繁体 → 简体** 可改为 `t2s.json` 等（需系统已安装对应 OpenCC 数据文件）。

## 部署要求

* **OpenResty**（带 `lua-nginx-module`）。
* **OpenCC** 运行时：系统安装 `libopencc.so` 与词典数据（如 `/usr/share/opencc/*.json`），并保证 **worker 进程能加载到 `.so`**（见下文「共享库」）。
* **Lua** 可 `require('zlib')` 的模块（用于 `zlib.inflate`，若无 gzip 体则 `pcall` 失败会跳过解压，不影响后续逻辑）。
* 上游为 HTTPS 时，本机需能解析并访问该域名（已用 `resolver` 时 VARIABLE 形式 `proxy_pass` 才会走指定 resolver）。

## 部署步骤

### 1. 安装 OpenCC 与数据文件

以 Debian / Ubuntu 为例（包名因发行版略有差异）：

```
sudo apt update
sudo apt install -y libopencc1.1 opencc # 或 libopencc2 等，以仓库为准
或者手工复制 lib64目录下的文件到 脚本对应的路径就是这个 /usr/lib64
```

确认存在词典，例如：

```
ls /usr/share/opencc/s2t.json
```

### 2. 确保能找到 `libopencc.so`

若日志出现 `libopencc.so: cannot open shared object file`：

* 将库放在系统默认搜索路径，例如 Ubuntu amd64：
* ```
  ldconfig -p | grep opencc
  ```
* 若库仅在 `/usr/lib64` 等非默认路径，可执行（与仓库 `fix.md` 一致）：
* ```
  echo '/usr/lib64' | sudo tee /etc/ld.so.conf.d/usr-lib64.conf sudo ldconfig
  ```
* 或在 **OpenResty 的 systemd 单元** 中设置 `Environment="LD_LIBRARY_PATH=/usr/lib64:/usr/local/lib"`  后重启。

脚本内已对多路径做了 `ffi.load` 尝试；仍失败时请对照 `ldd` 与 `opencc` 包实际安装位置排查。

### 3. 部署 Lua 脚本

将 `nginx/opencc/opencc-filter.lua` 复制到服务端约定路径（与 nginx 配置一致），例如：

```
sudo mkdir -p /usr/local/openresty/lua
sudo cp nginx/opencc/opencc-filter.lua /usr/local/openresty/lua/opencc-filter.lua
```

按需修改脚本顶部 `OPENCC_CONFIG` 指向本机实际的 JSON 配置。

### 4. 合并 Nginx / OpenResty 配置

* 将 `zero.zhongxiaojie.cn.conf` 中的 `server` 块纳入主配置（`include` 或粘贴到 `nginx.conf` 的 `http {}` 下）。
* 修改 **证书路径**、**日志路径**、**上游域名** `zhongxiaojie.cn`、以及 **`body_filter_by_lua_file`** 的路径，使其与当前环境一致。
* `header_filter_by_lua` 中去除 `Content-Encoding`，便于对明文 HTML 做处理；若上游与解压逻辑不匹配，需自行观察是否需要调整。

### 5. 校验并重载

```
sudo /usr/local/openresty/nginx/sbin/nginx -t
sudo /usr/local/openresty/nginx/sbin/nginx -s reload
# 或 systemctl reload openresty
```

### 6. 验证

* 浏览器访问你的站点，查看页面简繁是否符合预期。
* 检查 **图片与站内链接**是否正常（尤其含中文或 `%` 编码的路径）。
* `error.log` 中不应再出现 OpenCC 库加载失败或大量 IPv6 unreachable（在无 IPv6 环境）。

## 配置项速查

| 项目 | 位置 |
| --- | --- |
| OpenCC 配置 JSON | `opencc-filter.lua` → `OPENCC_CONFIG` |
| Lua 脚本路径 | `zero.zhongxiaojie.cn.conf` → `body_filter_by_lua_file` |
| 上游站点 | `set $upstream_host …` 与 `proxy_pass https://$upstream_host$request_uri` |
| DNS / 仅 IPv4 | `resolver 223.5.5.5 8.8.8.8 valid=300s ipv6=off` |
| 不参与转换的静态文件 | `location ~\* .(gif |

## 故障排查

| 现象 | 可能原因 |
| --- | --- |
| `libopencc.so` 找不到 | 未安装包、`ldconfig` 未包含库目录，或需 `LD_LIBRARY_PATH` |
| body\_filter 报错、栈指向 `ffi.load` | 同上；或架构不一致（如 32/64 位混用） |
| 上游连接 IPv6 失败 | 已用 `ipv6=off` + 变量 `proxy_pass`；仍失败则检查防火墙与 DNS |
| 图片 404 | 历史上多为 OpenCC 改了 URL 内汉字；当前脚本对常见属性已做保护，若仍有个别，检查是否来自 CSS `url()` 或 JS 动态拼接 |

---

如需改为其他域名、证书路径或 `t2s` 转换方向，只需改配置文件与 `OPENCC_CONFIG`，无需改 OpenResty 核心。

实际效果：

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/2026-04-01-11.13.33-zero.zhongxiaojie.cn-5e3a0545c205-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/2026-04-01-11.13.33-zero.zhongxiaojie.cn-5e3a0545c205.jpg)

开源项目地址：<https://gitee.com/obaby/baby-website-mirroring-tool>

参考链接：https://blog.csdn.net/wzj\_110/article/details/127758020

https://blog.rexskz.info/support-traditional-chinese-using-openresty-and-opencc.html

---

[![闺蜜圈APP](/support/guimiquan-ads2.jpg)](https://guimiquan.cn "闺蜜圈APP")

**博客：** [obaby 𝐢‍𝐧⃝ void](https://zhongxiaojie.cn/)

**地址：** <https://zhongxiaojie.cn/>

**文章：** [《弱弱的问一下，我的网站怎么被镜像了嗫？》](https://zhongxiaojie.cn/2026/04/768/)

[nginx](https://zhongxiaojie.cn/tag/nginx/)[openresty](https://zhongxiaojie.cn/tag/openresty/)[网站镜像](https://zhongxiaojie.cn/tag/%E7%BD%91%E7%AB%99%E9%95%9C%E5%83%8F/)

[Next Post](https://zhongxiaojie.cn/2026/03/746/)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=initials&r=pg&initials=ob)

#### obaby

独立 APP 开发者
偶尔写点东西
希望与过往一刀两断

#### You may also like

2026年2月5日 09:41

#### [来自自恋狂的瞎折腾](https://zhongxiaojie.cn/2026/02/350/)

2026年1月17日 09:35

#### [WP-UserAgent [增强版 16.01.01]](https://zhongxiaojie.cn/2026/01/104/)

2026年1月19日 16:37

#### [Tahoe 26.2 启动台](https://zhongxiaojie.cn/2026/01/172/)

### 66 comments

1. ![](https://gg.lang.bi/avatar/e2efe69978d8a05b712ca01c8332d3f353db625aaf9073742f617d332a5160bd?s=64&d=initials&r=pg&initials=%E5%B4%94%E8%AF%9D) **[崔话记](https://cuixiping.com/)**说道：

   [2026年4月1日 11:25 上午](https://zhongxiaojie.cn/2026/04/768/#comment-2102)

   ![](https://badgen.h4ck.org.cn/badge/友链/集美们/blue?icon=chrome) ![Level 3](https://badgen.h4ck.org.cn/badge/亲密度/Level 3/green?icon=codebeat)

   ![Google Chrome 146.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 146.0.0.0") Google Chrome 146.0.0.0 ![Windows 10 x64 Edition](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10 x64 Edition") Windows 10 x64 Edition ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   这么热乎的教程啊，赞👍

   你这个图点一下，再点一下，页面就跳到首页去了？

   [回复](#comment-2102)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=initials&r=pg&initials=ob)

      [2026年4月1日 1:02 下午](https://zhongxiaojie.cn/2026/04/768/#comment-2108)

      ![公主](https://badgen.h4ck.org.cn/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.h4ck.org.cn/badge/角色/女王/red?icon=matrix) ![Queen](https://badgen.h4ck.org.cn/badge/精神状态/恬静/pink?icon=codebeat)

      ![Google Chrome 142.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 142.0.0.0") Google Chrome 142.0.0.0 ![Mac OS X  10.15.7](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.p...