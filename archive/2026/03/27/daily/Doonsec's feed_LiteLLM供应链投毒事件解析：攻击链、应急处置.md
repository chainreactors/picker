---
title: LiteLLM供应链投毒事件解析：攻击链、应急处置
url: https://mp.weixin.qq.com/s/1h_TPx0IUln0yYurWFBb-w
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:16:14.880239
---

# LiteLLM供应链投毒事件解析：攻击链、应急处置

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2xCpgJcagfib5589Z6BkB2FzEKUnQdsZtxRGPkL0GNH9XYeNsc2amicTQtAHABByjQDnib0rUXgbzNYDichhrLMibIdeRdGgyA0RPZrK5OCOpzZI/0?wx_fmt=jpeg)

# LiteLLM供应链投毒事件解析：攻击链、应急处置

松杨网络安全资料库

![]()

在小说阅读器中沉浸阅读

一、事件概述：

2026年3月24日，LiteLLM 在 PyPI 上发布的 1.82.7 与 1.82.8 版本被发现遭恶意投毒，包含用于窃取凭据的恶意代码，事件被普遍认定为一次典型的供应链攻击。事件发生后，受影响版本已被下架/隔离，官方建议用户立即核查安装记录、排查相关入侵指标并轮换密钥凭据。

二、恶意样本触发机制一览表：

| 影响版本 | 恶意植入位置 | 触发条件 | 特征 |
| --- | --- | --- | --- |
| 1.82.7 | litellm/proxy/proxy\_server.py | 当业务代码导入/运行 LiteLLM Proxy 相关模块时触发 | 代码内嵌混淆载荷，随代理服务启动链路执行，具备凭据收集与外传行为特征 |
| 1.82.8 | litellm\_init.pth | Python 解释器启动时自动触发（安装在环境中即可触发） | 利用 .pth 启动机制实现“全局自动执行”，触发范围更广，隐蔽性更强，影响开发机与 CI 环境 |

三、完整攻击链路：

![](https://mmbiz.qpic.cn/mmbiz_png/2xCpgJcagfic1URy2zs4d40Q3ibddyNQOOfAO8GHnrytJXcYKysa0HtnzBfnG7yOP2JSwE4gXSNprRntfJeTNIzoZ5iaRAZwqLSOlR8icUOtaDw/640?wx_fmt=png&from=appmsg)

1）1.82.7 版本：代理模块投毒（导入即触发）

 攻击者在核心文件 proxy\_server.py 中植入了经过双层 Base64 混淆的恶意代码，并将其夹在正常业务逻辑之间，表面上与常规代码无明显差异，增加了人工审查与静态检测难度。

触发机制：当开发者或业务系统导入代理模块、启动网关服务时，恶意片段会先解码再执行，进而拉起后续攻击载荷。由于这一流程发生在常规运行路径中，生产网关部署、流水线测试以及本地调试等场景都可能中招。

2）1.82.8 版本：.pth 启动级触发（覆盖面更广）

 相较 1.82.7，1.82.8 的关键升级在于引入了 .pth 文件机制。Python 在解释器启动阶段会处理 site-packages 下的 .pth 文件，

触发机制：只有存在可执行导入语句，便会在启动时自动运行。只要受影响版本被安装进环境，很多与 LiteLLM 无直接关系的 Python 启动行为都可能触发恶意逻辑，例如打开 Python 终端、运行 Notebook、执行自动化脚本、启动 IDE 语言服务或跑单测。该机制显著扩大了触发面，也提高了排查复杂度；在应急处置中，如果仅卸载包而未清理异常 .pth 残留，风险可能仍然持续。

四、应对措施：

1.版本排查：

排查LiteLLM版本，若是1.82.7或1.82.8，立刻降级至安全版本1.82.6。

```
版本检测：pip list | grep litellm版本降级：pip uninstall -y litellmpip install litellm=1.82.6
```

2.凭证轮换：

将云平台访问密钥，Github、GitLab、CI Token、数据库密码、API keys、SSH密钥、TLS/SSL私钥等凭证进行轮换。

3.恶意文件排查：

排查在python环境中的恶意.pth文件以及后门文件，排查命令如下：

```
1. 查找Python site-packages目录下的恶意pth文件python -m site --user-site | xargs find -name "*litellm*.pth"python -c "import site; print('\n'.join(site.getsitepackages()))" | xargs -I {} find {} -name "*litellm*.pth"2.排查持久化后门文件：find ~/.config/ -name "sysmon.py" -o -name "sysmon.service"find /etc/systemd/system/ /usr/lib/systemd/system/ -name "sysmon.service"3.排查proxy_server.py中的恶意代码pip show litellm | grep Location | awk '{print $2}' | xargs -I {} find {}/litellm/proxy/ -name "proxy_server.py" | xargs grep -l "base64" | grep -v "test"4.检查 proxy_server.py (1.82.7)，恶意文件哈希：a0d229be8efcb2f9135e2ad55ba275b76ddcfeb55fa4370e0a522a5bdee0120bfind / -path "*/litellm/proxy/proxy_server.py" 2>/dev/null -exec shasum -a 256 {} \;5.检查 litellm_init.pth (1.82.8)，恶意文件哈希：71e35aef03099cd1f2d6446734273025a163597de93912df321ef118bf135238find / -name "litellm_init.pth" 2>/dev/null -exec shasum -a 256 {} \;
```

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