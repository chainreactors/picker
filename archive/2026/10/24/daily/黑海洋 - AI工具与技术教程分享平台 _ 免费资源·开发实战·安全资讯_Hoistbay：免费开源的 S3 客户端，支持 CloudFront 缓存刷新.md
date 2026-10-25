---
title: Hoistbay：免费开源的 S3 客户端，支持 CloudFront 缓存刷新
url: https://blog.upx8.com/Hoistbay-S3-CloudFront
source: 黑海洋 - AI工具与技术教程分享平台 | 免费资源·开发实战·安全资讯
date: 2026-10-24
fetch_date: 2026-10-25T07:10:19.421341
---

# Hoistbay：免费开源的 S3 客户端，支持 CloudFront 缓存刷新

[![黑海洋](https://blog.upx8.com/favicon.ico)
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
Hoistbay：免费开源的 S3 客户端，支持 CloudFront 缓存刷新

# Hoistbay：免费开源的 S3 客户端，支持 CloudFront 缓存刷新

[资源](https://blog.upx8.com/Free)
10-24
·
约 14 分钟
·
黑海洋
·

1,600

站内热度 **全站第 8,150**

1,600 次浏览

> 如果你平时会把网站文件、静态资源上传到 S3，再通过 CloudFront 做分发，更新一次内容通常不只是重新传文件。Cache-Control、Content-Type 这些 Header 要检查，缓存没及时更新时，还得再去 CloudFront 清一次。

**[Hoistbay](https://blog.upx8.com/go/aHR0cHM6Ly9ob2lzdGJheS5hcHAv)** 是一款免费开源的 S3 客户端，目前支持 macOS 和 Windows。它把 S3 文件管理、上传 Header Rules 和 CloudFront Invalidation 放到了同一个桌面应用里，项目采用 MIT License。

![Hoistbay：免费开源的 S3 客户端，支持 CloudFront 缓存刷新](https://cdn.skyimg.net/up/2026/10/24/ddc64774dfa65a6a154b936091d507ae.webp)

## Hoistbay 这个 S3 客户端主要做什么？

Hoistbay 作者在 [Product Hunt](https://blog.upx8.com/go/aHR0cHM6Ly93d3cucHJvZHVjdGh1bnQuY29tL3Byb2R1Y3RzL2hvaXN0YmF5) 介绍项目时提到，自己平时用 S3 和 CloudFront，最烦的就是几件事来回做：文件传上去以后还要检查 Cache-Control、Content-Type、Content-Encoding；想下载整个文件夹时 AWS Console 不够方便；文件更新完，还得再打开 CloudFront 清缓存。

Hoistbay 把这些操作放到了一起。文件上传时可以自动套用 Header Rules，整个文件夹可以直接上传和下载，更新完成后也能在应用里创建 CloudFront Invalidation。

实际操作下来，大致就是这样一条流程：

**上传网站文件 → 自动应用 Header → 检查对象信息 → 需要时清理 CloudFront 缓存**

如果网站或项目本来就在用 S3 + CloudFront，这几个功能基本都能对得上日常操作。静态网站、前端项目、Unity WebGL、字体和其他静态资源都属于比较典型的使用场景。

## Header Rules、CloudFront 和文件管理怎么用？

### 按文件类型自动应用 Cache-Control 等 Header

Hoistbay 可以针对不同 Bucket 设置 **Header Rules**，按照文件名 Pattern 给上传对象自动添加 HTTP Header。

比如 `*.js`、`*.css` 可以设置较长的 `Cache-Control`，`*.html` 则可以使用 `no-cache`。像 `*.wasm.gz` 这类压缩文件，也可以根据规则设置 Content-Type、Content-Encoding 等 Header。

规则设置好以后，后面上传匹配的文件会自动应用，不需要每次再打开对象属性修改。

这对静态网站比较实用。带内容 Hash 的 JS、CSS 通常可以使用更长的缓存时间，而 HTML 往往需要更快获取新版本；gzip 压缩文件如果 Content-Encoding 或 Content-Type 设置错了，浏览器也可能无法正常处理。

具体规则还是要按照自己的发布方式来写，Hoistbay 只负责按设定执行，并不会自动判断什么缓存策略最适合你的项目。

### 直接创建 CloudFront Invalidation

如果 S3 Bucket 后面接了 CloudFront，源文件已经换成新版本，并不代表边缘节点里的旧缓存马上消失。

Hoistbay 可以直接查看 CloudFront Distribution，对 `/*` 或指定 Path 创建 **CloudFront Invalidation**，并跟踪执行状态。这样换完文件以后，不需要再单独打开 AWS Console 找 Distribution。

AWS 当前每个账号每月前 **1,000 个 Invalidation Paths 免费**，超过以后才按 Path 收费。使用 `*` 通配符时，即使实际清理了大量文件，也只按一个 Path 计算。

不过频繁更新的静态资源，还是更适合使用带版本号或内容 Hash 的文件名，减少主动清缓存的次数。Hoistbay 更适合在确实需要手动 Invalidation 时，把这一步顺手做掉。

### 整个文件夹上传下载，多账号也能切换

文件管理方面，Hoistbay 支持拖入单个文件或多个文件夹，并保留原来的目录结构，也可以直接下载整个文件夹。

Rename、Move、Delete 和跨 Bucket、跨 Region Copy 都已经覆盖，超过 1,000 个 Object 的目录也支持继续分页浏览。

它还支持保存多个 AWS Profile，在不同账号和 Region 之间切换，并支持 Session Token。Bucket Region 会自动识别，不需要每次手动选择。

Object Inspector 可以查看 Properties、HTTP Headers、Tags、Versions 和 `x-amz-meta-*` Metadata，部分 Metadata 可以直接修改。遇到 Content-Type 或其他 Header 配错的情况，不一定非要重新上传文件。

## Hoistbay 和其他 S3 客户端有什么不同？

S3 图形客户端并不少。Hoistbay 和这些工具的区别，主要还是看你平时拿 S3 来做什么。

| 工具 | 更适合的场景 | 主要区别 |
| --- | --- | --- |
| **Hoistbay** | Amazon S3 + CloudFront 日常维护 | 把 Header Rules、S3 文件管理和 CloudFront Invalidation 放在一起 |
| **CS Browser（原 S3 Browser）** | Windows 上进行更完整的 S3 管理 | 功能更重，支持 S3-compatible Storage、CloudFront Manager、Folder Sync 等 |
| **Cyberduck** | 同时连接多种服务器和云存储 | 支持 FTP、SFTP、WebDAV、S3 等多种协议，覆盖范围更广 |
| **Brows3** | S3 / S3-compatible Storage | 支持 Amazon S3、MinIO、Cloudflare R2、Wasabi 等，更偏通用 S3 Browser |
| **AWS Console** | 完整 AWS 配置和管理 | 能力最完整，但日常换几个文件、清一次缓存时操作比较重 |
| **AWS CLI / CI** | 自动化和高频部署 | 更适合脚本和流水线，已经自动化的项目不太需要额外 GUI |

Hoistbay 和这些工具最大的区别，是把 Amazon S3 文件管理、上传 Header 和 CloudFront Invalidation 放在了一条比较集中的流程里。

它的功能范围没有 CS Browser 或 AWS Console 那么大，但对于仍然会手动维护 S3 + CloudFront 的用户，反而少了不少平时用不到的东西。

## Hoistbay 需要哪些 AWS IAM 权限？

Hoistbay 需要 AWS Credential 才能访问 Bucket，所以权限配置比界面漂不漂亮更值得看。

项目给出了 Least Privilege 的权限参考，并不要求直接给 AdministratorAccess。

| 操作 | 主要 IAM 权限 |
| --- | --- |
| 查看 Bucket 和文件 | `s3:ListAllMyBuckets` `s3:GetBucketLocation` `s3:ListBucket` `s3:GetObject` |
| 上传文件 | `s3:PutObject` |
| 删除文件 | `s3:DeleteObject` |
| CloudFront Invalidation | `cloudfront:ListDistributions` `cloudfront:CreateInvalidation` `cloudfront:GetInvalidation` |

实际使用时，建议单独准备一套权限受限的 IAM Credential，并把 Resource 继续限制到真正需要管理的 Bucket。

如果只是查看文件，就不用给 `DeleteObject`；只准备拿一个测试 Bucket 试用，也没必要顺手把生产环境里的其他资源一起开放。

## AWS 密钥会存到哪里？

Hoistbay 需要填写 AWS Credential 才能访问 S3。按项目方的说法，这些密钥不会保存在 Hoistbay 自己的服务器上，而是放在系统自带的安全存储里：macOS 使用 Keychain，Windows 使用 Credential Manager。

项目也没有自建 Backend 和 Telemetry，操作时直接连接 AWS 的服务端点。

不过这不代表可以放心给它一套高权限账号。Hoistbay 毕竟需要拿着你的 Credential 去操作 S3 和 CloudFront，实际使用时更重要的还是**单独准备一套最小权限 IAM Credential**，只开放真正需要管理的 Bucket 和操作权限。

本文没有对 Hoistbay 的全部源码和网络请求做独立审计。如果要接生产环境，建议先从测试 Bucket 开始。

## 多账号可以切换，但 AWS SSO 目前没有明确支持

Hoistbay 可以保存多套 AWS 账号配置，在不同账号和 Region 之间切换，也支持 Session Token。

不过目前没有看到官方说明它会直接读取本机的 AWS CLI 配置，例如 `~/.aws/credentials` 或 `~/.aws/config`。也就是说，Hoistbay 里的 Profile 更像是应用自己保存的账号配置，并不是把你现有的 AWS CLI Profile 自动带进来。

AWS IAM Identity Center / AWS SSO 目前也没有看到明确的官方支持说明。如果公司 AWS 账号平时主要通过 SSO 登录，这一点最好在正式使用前确认。

## R2、MinIO 这类 S3 兼容存储目前不适合直接用

Hoistbay 现在主要就是围绕 Amazon S3 和 CloudFront 做的，官网和 项目介绍页面 也没有把 Cloudflare R2、MinIO、Wasabi 这些 S3-compatible Storage 列进支持范围。

所以如果你用的是 AWS S3，Hoistbay 的功能比较对路；如果平时主要管的是 R2、MinIO 或 Wasabi，就不建议默认它能直接兼容。

这类需求反而更适合用 Brows3、Cyberduck 或 CS Browser，因为这些工具已经明确支持更多 S3-compatible Storage。

## 安装 Hoistbay 前要注意什么？

Hoistbay 现在的安装包还没有代码签名，macOS 第一次打开时可能会被 Gatekeeper 拦下来，Windows 也可能弹出 SmartScreen。Mac 这边目前也没有完成 Apple Notarization，如果系统不让直接运行，通常需要右键选择“打开”，或者到“系统设置 → 隐私与安全性”里手动放行。

Linux 版本目前还没有正式提供，官网和 GitHub页面 都还是 Coming Soon。项目本身发布时间也不长，公开 Issues、用户反馈和长期版本记录都比较少，所以现在更适合把它当成一个值得试用的新工具，还不能太早判断长期稳定性。

CloudFront 这部分也别理解成完整管理工具。Hoistbay 目前主要是方便你做 Invalidation；如果要改 Origin、Cache Behavior、WAF、证书这些配置，还是得回 AWS Console。

### 下载时注意一下版本号

截至 2026 年 10 月 21 日，[GitHub Releases](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL21la2FydGlrc2hhaC9ob2lzdGJheS9yZWxlYXNlcw) 最新已经是 **v1.1.1**，这个版本也完成了项目从 S3 Scout 到 Hoistbay 的改名。不过官网下载安装区域目前还显示 **v1.1.0**，所以要看最新安装包和更新内容，直接以 GitHub Releases 为准。

## Hoistbay 适合谁？

Hoistbay 比较适合仍然会手动管理 S3 文件、检查 Header，并偶尔处理 CloudFront 缓存的开发者和站长。

比如网站文件放在 Amazon S3，再通过 CloudFront 分发；平时会换几个资源、检查 Cache-Control、修改 Metadata，更新完成后偶尔需要清一次缓存，这类场景比较对路。

如果主要使用 Cloudflare R2、MinIO、Wasabi，或者企业环境强依赖 IAM Identity Center / SSO，目前有其他客户端更合适。

已经把 S3 上传、Cache-Control 和 CloudFront Invalidation 全部写进 GitHub Actions、GitLab CI 或其他 CI/CD 流程的团队，Hoistbay 带来的提升也会比较有限。

准备长期使用的话，可以先拿测试 Bucket 配一套最小权限 IAM Credential，跑一遍上传、Header Rules 和 CloudFront Invalidation，再决定是否接入生产环境。

## Hoistbay 常见问题

### Hoistbay 免费吗？

免费，项目采用 MIT License 开源，源码可以直接在 [Hoistbay GitHub 仓库](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL21la2FydGlrc2hhaC9ob2lzdGJheQ) 查看。

### Hoistbay 支持哪些系统？

目前有 macOS 和 Windows 版本。Mac 要求 macOS 12 及以上，Apple Silicon 和 Intel 都能用；Windows 支持 Windows 10/11 x64。Linux 版还在计划中。

### Hoistbay 会把 AWS 密钥传到自己的服务器吗？

按项目方的说法不会。AWS 密钥保存在 macOS Keychain 或 Windows Credential Manager 里，Hoistbay 也没有自己的后端服务和遥测。不过这部分属于官方说明，本文没有单独审计它的全部网络行为，所以生产环境还是建议使用最小权限的 IAM Credential。

### Hoistbay 支持 AWS SSO 吗？

目前没有看到官方明确支持 AWS SSO / IAM Identity Center。它可以保存多个 AWS 账号配置，也支持 Session Token，但和企业常用的 SSO 登录不是一回事。

### Hoistbay 能管理 Cloudflare R2 或 MinIO 吗？

目前不建议默认可以。官方明确写的是 Amazon S3 和 CloudFront，没有把 R2、MinIO、Wasabi 这些 S3 兼容存储列入支持范围。如果主要管理这类存储，Brows3、Cyberduck 等工具会更合适。

### Hoistbay 可以直接清 CloudFront 缓存吗？

可以。选好 CloudFront Distribution 后，可以对 `/*` 或指定路径创建 Invalidation，并查看清理进度，不需要再单独打开 AWS Console。

### Hoistbay 需要哪些 AWS 权限？

取决于你准备用它做什么。只看文件主要需要 `ListAllMyBuckets`、`GetBucketLocation`、`ListBucket` 和 `GetObject`；需要上传或删除时，再增加 `PutObject`、`DeleteObject`。如果还要清 CloudFront 缓存，则需要 `ListDistributions`、`CreateInvalidation` 和 `Ge...