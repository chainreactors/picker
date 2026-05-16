---
title: Codex最新更新把插件锁了？3分钟救回来！
url: https://mp.weixin.qq.com/s/eAcC66wbHTvUQEFX77tJng
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:09:09.978192
---

# Codex最新更新把插件锁了？3分钟救回来！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4T1PVwJicwk9t2nTyLWV4dLWIcEq6E9Pv2PeaiahOJ6w59X7RbeicqYO4ic4VdGRc6VJG9r3Y3kGLibGBHgIwjhYkKO8f35rwsacrbHibSvheH8q8/0?wx_fmt=jpeg)

# Codex最新更新把插件锁了？3分钟救回来！

原创

Norsea
Norsea

泷羽Sec-Norsea

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 免责声明
>
> 本系列工具仅供安全专业人员进行已授权环境使用，此工具所提供的功能只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用工具中的功能对任何计算机系统进行入侵操作。利用此工具所提供的信息而造成的直接或间接后果和损>失，均由使用者本人负责。
>
> 工具集合：https://pan.quark.cn/s/f113bdb29fd7

## 一、Codex++ 是什么

`Codex++` 面向 `OpenAI Codex App`，定位是外部增强启动器。

它不改动 `Codex App` 的原始安装文件，而是通过外部 `Launcher` 启动 Codex，再用 `Chromium DevTools Protocol（CDP）`向渲染进程注入脚本，补上原生使用里一些不太顺手的环节。

简单说，它不是“`改包工具`”，而是“外接增强层”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwk8xvTYn4B7DzlFiauovrDgIiaiatVPzAIiacOXpAMViclBcSib3PscLN36PCM6sLtzRHTSiaK7ueRCYibI5j0tYwBuhBKVLHOzy2ZsHN7w/640?wx_fmt=png&from=appmsg)

## 二、它具体能做什么

目前这版主要解决几个高频问题：

* 在 API Key 登录模式下，补上插件入口受限的问题

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwk9uCFNBDhFQufiaZRMwOYGqibgRlT1AUl6gibk9ONd8rnuzzWlCENuOmhCVSTVAz6SwUbeicD7QhQs2aaTJI8C1cpzZTap4Hib6VJv0/640?wx_fmt=png&from=appmsg)

* 会话列表支持悬停显示删除按钮，删除前可确认，也支持撤销

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwkibJSfUQKfPXpKd31fvstFj5Sjtcoib98AKzDEianDkgKFicodaUCOBoHFQCOg9rDzVjPus1ciauzsPzC2MyNHC7xaLRsVeFWdiaXWFE/640?wx_fmt=png&from=appmsg)

* 删除会话时优先走服务端；服务端不可用时再处理本地 Codex SQLite 记录
* 顶部菜单增加 Codex++ 入口，方便打开配置
* 功能可开关，例如插件解锁、特殊插件强制安装、会话删除
* 支持 Windows 和 macOS
* 支持基于 GitHub Release 的更新检查与升级
* 启动时可继承系统代理或探测常见代理端口，便于加载 GitHub 技能资源

如果你平时会话很多、经常清理历史，这些改动会比较有感觉。

## 三、它怎么工作的

Codex++ 的思路是“外部增强 + 非侵入”。核心流程如下：

* 外部 Launcher 启动 Codex，并附加 `--remote-debugging-port=9229`
* 通过 CDP 向渲染进程注入 `renderer-inject.js`
* 本地 Helper 服务负责健康检查、生命周期和删除相关能力
* 通过本地 SQLite 适配器处理会话删除与备份
* Windows 可用快捷方式与常驻 Watcher 接管；macOS 可生成独立 `.app`
* 默认不改 `app.asar`，不写 DLL，删除能力默认不开放 HTTP 接口

这套设计的重点是可逆和低侵入。Codex App 更新后，通常只需要跟进注入脚本。

## 四、怎么安装和使用

### Windows（推荐）

1. 克隆或下载项目
2. 双击项目根目录 `setup.bat`
3. 选择菜单 `[1] Install Codex++`
4. 安装后桌面会生成 `Codex++.lnk`，双击即可启动

### macOS

```
python -m codex_session_delete setup
```

安装后会在 `/Applications` 下生成 `Codex++.app`。命令行启动：

```
python -m codex_session_delete launch
```

也支持传参（比如 Codex 安装路径、调试端口）。卸载方式：

* Windows：在 `setup.bat` 里选卸载，或走系统卸载流程
* macOS：

```
python -m codex_session_delete remove
```

## 五、环境要求

* Python 3.11+
* 已安装 OpenAI Codex App
* Windows 或 macOS

## 六、适合谁用

如果你符合下面任意一条，可以试试：

* Codex 使用频率高，会话历史增长快
* 需要频繁整理会话
* 需要在 API Key 模式下补齐插件使用体验
* 想要更统一的启动、更新、卸载流程

## 七、最后提醒

Codex++ 是外部增强工具，不修改 Codex App 核心文件。建议只在合法授权环境使用，并遵守 OpenAI 服务条款。

> 项目地址：https://github.com/Lier-XS/CodexPlusPlus

## 学习交流群

刚加入网络安全行业的小白，可以加入学习交流群，大家一起互相学习，互相进步，不会的难题大家一起学习，一起攻克。

想要进学习交流群的师傅们，可以扫描下方二维码添加好友，我再拉你进群（Ps：防止广告进群）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/IkpoxULsr9dEclFnKnAAurt1AlnO1HBLiaRymULG1ibJJhXlNjMH1rd1SgQQWIyFBVTRMteWWfiby3FCWfpB7n2oA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

泷羽Sec-Norsea

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

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