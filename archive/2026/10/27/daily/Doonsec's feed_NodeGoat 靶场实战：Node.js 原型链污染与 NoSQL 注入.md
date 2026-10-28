---
title: NodeGoat 靶场实战：Node.js 原型链污染与 NoSQL 注入
url: https://mp.weixin.qq.com/s/OfBQxuXwuSEBG61r1ZIovQ
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:46:25.150230
---

# NodeGoat 靶场实战：Node.js 原型链污染与 NoSQL 注入

# NodeGoat 靶场实战：Node.js 原型链污染与 NoSQL 注入

原创

不懂安全的运维
不懂安全的运维

运维安全入门

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

PHP 的漏洞史，本质上是一部「代码与数据如何纠缠」的历史。SQL 注入、命令注入、代码注入、LFI——换了名字，根子都是一个。

但 Node.js 有点意思。它是**事件驱动、单线程、运行在 V8 上的 JavaScript 运行时**，它的漏洞史里有一类 PHP 世界几乎不存在的问题：**原型链污染**。

原因不难理解：JavaScript 里对象是**可继承的**，而原型链天然提供了「全局修改行为」的能力。一个本该只影响单个对象的操作，有可能沿着原型链一路影响到整个进程。这类问题一旦被利用，往往**不需要任何特殊权限**。

这一章的主角是 **NodeGoat**（OWASP 出品），一个刻意设计成不安全的 Node.js + Express + MongoDB 应用，附带完整教程，专门用来演示 Node 生态里的典型漏洞模式。

**🛡️ 授权声明**　NodeGoat 是专门用于教学的环境，包含大量可被直接利用的漏洞链。请仅在本地或授权隔离环境中使用。

本文目录

1. JavaScript 的原型链：从语言特性到攻击面
2. NodeGoat 是什么：技术栈与设计意图
3. 部署：Docker 与源码两种方式
4. 默认凭据与教程入口
5. 核心机制：Node 生态的四类典型漏洞
6. 实战一：原型链污染的原理与利用链
7. 实战二：NoSQL 注入与 MongoDB 查询注入
8. 实战三：JWT 与认证绕过
9. 实战四：依赖供应链风险
10. 实战五：路径遍历与文件上传
11. 排错清单
12. 防守与等保：Node 应用的加固基线
13. 总结

## 01JavaScript 的原型链：从语言特性到攻击面

### 一、原型链是什么

在 JavaScript 里，每个对象都有一个内部属性指向它的「原型对象」，属性查找会沿着这条链**逐级向上查找**，直到找到或走空。

原型链查找与原型污染的影响范围

```
const a = { isAdmin: false }; const b = Object.create(a);   // b 的原型是 a const c = Object.create(b);   // c 的原型是 b  // c.isAdmin 属性查找：c 自身没有 → 查 b → b 没有 → 查 a → 找到 false console.log(c.isAdmin);      // false  // 现在污染原型 a.isAdmin = true;  console.log(c.isAdmin);      // true —— 注意 c 自己从未被赋值  // 更严重的情况：污染 Object.prototype Object.prototype.isAdmin = true; const d = {}; console.log(d.isAdmin);      // true —— 整个进程内所有对象都被污染
```

看最后两行。污染 `Object.prototype` 意味着**此后创建的所有对象**都会继承那个属性。这在 Node 服务里就是一个「静默的全局状态篡改」。

**⚠️ 注意**　这就是原型链污染最危险的地方：**它不需要内存破坏，不需要提权，只需要一个「对象合并」函数。**在很多业务代码里，「合并用户配置」这类操作写得毫无防备——这就是完整的攻击前提。

### 二、为什么会造成 RCE

单凭污染属性本身还不能执行代码。真正的杀伤力在于**「污染 + 后续的隐式行为」**这个组合。

典型的两条路径：

1. **污染子进程启动参数**

   ：Node 的 `child_process` 在某些封装里会把配置对象直接展开成执行参数。一旦攻击者能注入 `shell` 或 `env` 等属性，就可能把「执行命令」变成「执行另一条命令」。
2. **污染模板/配置解析行为**

   ：某些库在解析配置时会把对象键值直接传给下游函数，污染出的属性就会被当作正常配置使用。

原型链污染的典型成因与 RCE 组合路径

```
// 典型的不安全合并函数 function unsafeMerge(target, source) {   for (const key in source) {     target[key] = source[key];   // for...in 会遍历原型链上的可枚举属性   }   return target; }  // 攻击者提交：__proto__ 键在 JSON 解析后会直接作用到原型 unsafeMerge(userConfig, JSON.parse(requestBody));  // 之后：任意新建对象都会带上攻击者设置的属性 // 若下游有 child_process.exec/spawn 读取被污染的键 → RCE
```

![原型链污染利用链：不可信输入 → 不安全合并 → 原型污染 → 隐式行为劫持 → RCE](https://mmbiz.qpic.cn/mmbiz_png/0l1UjZtX9txfTmw6lDSj8JTypX44M6MMEQger2SGRYT6N49joCl947dqjx06IeTCdjxF2wnTqg3IGNVg81JLia9aHHR4Y7uGnib39D9ujpYMQ/640?from=appmsg)

图：原型链污染利用链：不可信输入 → 不安全合并 → 原型污染 → 隐式行为劫持 → RCE

## 02NodeGoat 是什么：技术栈与设计意图

| 组件 | 版本特点 | 承载的漏洞类型 |
| --- | --- | --- |
| Node.js 运行时 | 较新版本运行时 | 原型链行为、反序列化 |
| Express 框架 | Node 最主流 Web 框架 | 中间件顺序、路由权限 |
| MongoDB | 文档型数据库 | NoSQL 注入、类型混淆 |
| JWT 认证 | 无状态令牌 | 密钥与算法缺陷 |
| npm 依赖 | 刻意保留脆弱依赖 | 供应链风险 |

NodeGoat 与 bWAPP 的定位差别很清晰：**bWAPP 让你补齐漏洞类型的广度，NodeGoat 让你理解「语言特性如何变成漏洞」。**而它最大的特色是官方配套了**交互式教程**——页面内嵌了每一关的讲解，非常适合自学。

## 03部署：Docker 与源码两种方式

NodeGoat 部署方式

```
# 方式一：Docker（推荐） docker build -t nodegoat . docker run -d -p 4000:4000 --name nodegoat nodegoat # 浏览器访问 http://localhost:4000  # 方式二：源码运行 git clone https://github.com/OWASP/NodeGoat.git cd NodeGoat npm install npm start # 默认端口 4000
```

查看容器内部结构与启动配置

```
# 进入容器内部查看源码（学习用） docker exec -it nodegoat bash  # 查看项目结构 ls -la cat config/env.js  # 查看实际启动命令 cat package.json
```

| 访问地址 | 用途 |
| --- | --- |
| http://localhost:4000 | 主应用 |
| http://localhost:4000/tutorial | 官方交互式教程 |

**💡 提示**　如果 npm install 报网络或构建错误，优先使用 Docker 方式——Node 生态的依赖安装在新版本 Python/Node 环境上经常遇到原生模块编译问题，而官方镜像已经把依赖环境固化了。

## 04默认凭据与教程入口

| 账号类型 | 凭据 | 权限范围 |
| --- | --- | --- |
| 普通用户 | admin / adminPassword1 | 基础业务功能 |
| 管理员 | 通过普通用户提权获得 | 管理功能 |
| 数据库账号 | 在配置文件中明文存放 | 直接数据访问 |

NodeGoat 有一个非常值得学的自查习惯：**它的配置文件里通常以明文存放数据库连接信息。**在真实项目评审中，这类「凭据硬编码在配置文件中」的问题，是代码审计必查项，也是等保测评中「应采用密码技术保证重要数据的保密性」的高频扣分点。

## 05核心机制：Node 生态的四类典型漏洞

| 漏洞类型 | 根因 | PHP 世界有对应物吗 |
| --- | --- | --- |
| 原型链污染 | 对象合并未过滤原型键 | 无（语言特性差异） |
| NoSQL 注入 | 查询对象被用户输入污染 | 无（无 SQL） |
| 类型混淆 | JavaScript 动态类型 + 宽松比较 | 部分（弱类型比较） |
| 依赖供应链风险 | npm 生态扁平化依赖树 | 有（Composer/包管理） |
| 模板注入 | 模板与数据边界模糊 | 有（模板注入） |

前三类是 JavaScript 特有的，后两类是跨语言共有的。值得注意的是**类型混淆**：

JavaScript 类型转换导致的鉴权绕过

```
// JavaScript 的宽松相等 console.log(null == undefined);        // true console.log(null == 0);                // true  ← 危险 console.log("" == 0);                  // true  ← 危险 console.log([] == false);              // true console.log([1,2] == "1,2");           // true  ← 数组与字符串比较  // 典型鉴权缺陷： // if (req.body.role == "admin")  →  传入数组或空值可能绕过  // 正确做法：严格相等 if (req.body.role === "admin") { /* ... */ } // 或者显式校验类型 if (typeof req.body.role !== "string") { throw new Error("invalid"); }
```

**⚠️ 注意**　这条在 NodeGoat 里几乎每关都会碰到。根因是 JavaScript 的**自动类型转换**：它让代码更灵活，也让鉴权判断更容易被绕过。防御的答案很明确：**在数据入口做类型校验，而不是在判断语句里指望类型正确。**

## 06实战一：原型链污染的原理与利用链

### 一、三步完成污染

1. **找到合并点**

   ：任何「把用户输入合并到对象」的地方，尤其注意深拷贝/深合并的工具函数。
2. **绕过原型键过滤**

   ：不同框架对 `__proto__` 的处理不同，可能需要用 `constructor.prototype` 等变体。
3. **等待隐式行为**

   ：污染的属性本身不会立刻造成危害，它需要等待某个「读取该属性并做出动作」的代码路径被触发。

递归合并导致的原型污染

```
// 危险写法：递归合并未跳过特殊键 function deepMerge(target, source) {   for (const key in source) {     if (source[key] && typeof source[key] === 'object') {       if (!target[key]) target[key] = {};       deepMerge(target[key], source[key]);     } else {       target[key] = source[key];     }   }   return target; }  // 攻击载荷 const payload = JSON.parse('{"__proto__":{"isAdmin":true}}'); deepMerge(defaults, payload);  // 结果：后续任意 new Object() 创建的对象 isAdmin 都为 true
```

### 二、防护方案的三种写法

三种防御写法对比

```
// 方案一：使用 Object.create(null) 隔离原型 const safe = Object.create(null); safe['__proto__'] = { polluted: true };  // 只是普通键  // 方案二：合并前检查特殊键 const DANGEROUS = ['__proto__', 'constructor', 'prototype']; function safeAssign(target, source) {   for (const key of Object.keys(source)) {   // Object.keys 不遍历原型     if (DANGEROUS.includes(key)) continue;     target[key] = source[key];   }   return target; }  // 方案三：直接使用 Map，或使用成熟的安全合并库 // Node 原生 structuredClone 也能避免此类问题
```

![原型链污染的发现路径与三层防御对照图](https://mmbiz.qpic.cn/sz_mmbiz_png/0l1UjZtX9tzqSPpOrJTPZDt7qlgtqxca44jk94PUQxCc9iaL7MXd6AtRL9hfJXcZS02fmERmTfh9vlA63SeLVIv7Jfnd6GoDOS9vs1l3dIJg/640?from=appmsg)

图：原型链污染的发现路径与三层防御对照图

## 07实战二：NoSQL 注入与 MongoDB 查询注入

### 一、为什么 NoSQL 也能注入

很多人以为「没有 SQL 就没有注入」。这是错的。注入的本质是**「把数据当成了结构」**，而不是「用了某种查询语言」。

MongoDB 的查询 API 接收的是一个对象。如果开发者的写法是：

MongoDB 操作符注入的原理

```
// 危险写法：直接把请求体当查询条件 const user = await db.collection('users').find(req.body).toArray();  // 攻击者提交： // {"username":"admin","password":{"$ne":null}} // 生成的查询等价于：username='admin' AND password != null // → 无需知道密码即可匹配到 admin
```

| 操作符 | 含义 | 攻击效果 |
| --- | --- | --- |
| $ne | 不等于 | 绕过密码相等判断 |
| $gt | 大于 | 构造范围匹配 |
| $regex | 正则匹配 | 逐字符盲注数据 |
| $exists | 字段存在性 | 枚举字段结构 |
| $where | JS 表达式 | 在特定版本下可执行 JS |

NoSQL 注入的正确防御写法

```
// 正确写法：显式提取字段，不接受任意对象 const { username, password } = req.body;  if (typeof username !== 'string' || typeof password !== 'string') {   return res.status(400).json({ error: 'invalid input types' }); }  const user = await db.collection('users').findOne({ username }); if (!user) return res.status(401).json({ error: 'auth failed' });  // 密码比对使用恒定时间算法，避免时序侧信道 const ok = await bcrypt.compare(password, user.passwordHash); if (!ok) return res.status(401).json({ error: 'auth failed' });
```

**💡 提示**　这段防御代码里有三个常被省掉的细节，每一个都对应一类真实问题：**类型校验**（防操作符注入）、**错误信息统一**（防用户名枚举）、**恒定时间比对**（防时序侧信道）。第三个尤其值得强调——它和密码学直接相关，也是很多团队会漏的点。

## 08实战三：JWT 与认证绕过

NodeGoat 的认证设计刻意保留了**「先解码再验签」**这类经典错误。这类错误的根源不在 JWT 算法，而在**代码组织方式**。

| 错误实现 | 问题 | 后果 |
| --- | --- | --- |
| 解码后未验证就使用载荷 | 载荷完全由客户端控制 | 任意提权 |
| 验证失败时只打印日志不中断 | 流程继续执行 | 形同无认证 |
| 把用户身份从请求体读取 | 身份来自不可信输入 | 水平越权 |
| 过期时间仅在前端检查 | 服务端不校验 exp | 令牌永久有效 |

必须强调一条安全开发的铁律：**JWT 的载荷是「已签名的数据」，不是「可信的身份」。**签名保证了「没被篡改」，不保证「里面写的东西是对的」。服务端必须验证签名、验证过期、并且**把载荷中的身份与当前请求做一致性绑定**，这三件事缺一不可。

## 09实战四：依赖供应链风险

Node 生态有一个独有的结构性风险：**依赖树的扁平化**。

| 特性 | 带来的收益 | 带来的风险 |
| --- | --- | --- |
| 扁平依赖树 | 依赖少，安装快，磁盘占用小 | 顶层依赖易被投毒 |
| 安装脚本自动执行 | 原生模块可编译 | 恶意包可直接执行代码 |
| 版本号语义化 | 依赖管理直观 | 补丁版本自动引入新代码 |
| 海量公共包 | 开发效率极高 | 拼写相近的包易被误装 |

npm 依赖审计的实用命令

```
# 审计依赖树中的已知漏洞 npm audit  # 查看生产依赖树 n...