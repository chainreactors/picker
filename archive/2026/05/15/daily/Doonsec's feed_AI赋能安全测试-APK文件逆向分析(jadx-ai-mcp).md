---
title: AI赋能安全测试-APK文件逆向分析(jadx-ai-mcp)
url: https://mp.weixin.qq.com/s/PJrpsQoDiKno2ytjSDuzkA
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:08:30.243630
---

# AI赋能安全测试-APK文件逆向分析(jadx-ai-mcp)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xY9ZTT0gDw5qSDL0s90QfyLMTXEgfcavmYtDbW4fYtkFHKfSdXJKDN5jwibChnRduHTmyTVTB9HykwsITFav84Sqs7G2ezqtDnicfEsWPLgG8/0?wx_fmt=jpeg)

# AI赋能安全测试-APK文件逆向分析(jadx-ai-mcp)

原创

huan666
huan666

huan666

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一、前言

采用AI 调用 Jadx MCP 插件智能化逆向模式，依托 MCP 协议打通大模型与 Jadx 逆向工具通信链路，由 AI 自主调度反编译能力，自动解析 APK 组件、提取敏感权限、挖掘硬编码密钥与接口地址，并梳理业务加密逻辑。该模式有效降低逆向人工成本，提升混淆应用逻辑还原与安全风险排查效率，为移动安全自动化逆向审计提供了可靠技术方案。

二、工具清单

```
TRAE：https://www.trae.cn/ide/downloadjadx：https://github.com/skylot/jadxjadx-ai-mcp：https://github.com/zinja-coder/jadx-ai-mcpAPK文件：https://github.com/ReversecLabs/drozer/releases/download/2.3.4/sieve.apk
```

三、环境配置

1、jadx安装，直接下载jre版本运行即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6LKic95RCLLYmANhUZNa2bTCpOlibTPaVQ3T4YxU1v2JSd9INOSc3OYdRMFKXWHIjEicV1iaTjo6gNbz7D58gXibm2dWWg2wVB6bO4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw5YKH8x7ntw0gRJndn7pHZ8MM4IAWzY9f4y13nBneHvewHpKIkUN9j0CkyI42yiaHibictDb5kvmoDjZibHrTKK5KPL4IITDTEzKFo/640?wx_fmt=png&from=appmsg)

2、下载jadx-ai-mcp-6.3.0.jar和jadx-mcp-server-6.3.0，jadx导入jadx-ai-mcp

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw5cIhBGLIib9ia7iaJOM854DH11lk6apSVl1RHFU46amu0t11zHibZqlibN1LKNg6j3ibaBAwhxogjpAx2VIkOb59ZrL32OphoSkj4AQ/640?wx_fmt=png&from=appmsg)

点击，插件-管理插件-安装插件，选择jadx-ai-mcp-6.3.0.jar，点击安装即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw4uMB8E9aruNLyibwcLvibISn4B4dliaEPFcZt5JNBp76p4btTPdgwXCkanKBiaUXtNFziaeTFrO1OUpaA9bfFzhrnE2VjIZmiaSiakYM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw5jThiaC6JhiciazJfEOXbIia1q2ArFnNXPysUugKda8GrLLF8AEZU1w0kEPPK0gbN3NiaDw0G818tA64oOljiceUiaE7REJpH0bLJQCs/640?wx_fmt=png&from=appmsg)

将apk文件拖入jadx之后，出现Plugins按钮，显示Jadx Ai MCP Server已成功开启，默认端口是8650，也可以自定义端口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw5BILB5yYUOtpRJpAWibqX9wmQ6f3uo662ZTPLNjLA7tuVAXSMPKHv18DCdLT4o7QS49gaWfJLfIiarmbZPUF1vorvzg65XegbX4/640?wx_fmt=png&from=appmsg)

访问8650端口，出现Endpoint GET / not found字样代表安装成功

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5yDkrUY4cRJFstfkq4LJIibGhovR1h2lhJvicKITDjzeAV6u0CQicCWg2dEGR2icrDgXOQwakjSFcicia44ZoyMsFCD4qfYeKy1Am0I/640?wx_fmt=png&from=appmsg)

3、jadx-mcp-server-6.3.0配置，通过pip安装所需的模块

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw5fDEicJsVribhDMEvTUxIW2OeiallLXtpjSasPEdOWMsx3lqpsjjGbU6q4iayMzxYA1aEuwyjbLSicyFLFGPI3Qfe9tC0YgFCbDevA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw56dNvgNDokvBLGRDia353Sr7tLVjrGiabKSLevwmia1NUwfCAkXr0yQRStYQq7kIsoJhzibxibliaPBy9qzMEdcDCZbGSEslqaadhC8/640?wx_fmt=png&from=appmsg)

运行jadx\_mcp\_server.py，出现下面字样代表连接成功

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw6nCWUwNa7J02d3y0LqRp2yciccwBuBY05vEoZO7xiaVic0NX6oSLGrrbMicZsqkWy1WuicMzfpIn8whPRmiaAWxvPQK5xFpxb0r7XeU/640?wx_fmt=png&from=appmsg)

4、TRAE配置并连接jadx-ai-mcp服务，详细配置参考之前的文章

[基于Trae的AI自动化安全测试实战总结](https://mp.weixin.qq.com/s?__biz=MzkzMjk5MDU3Nw==&mid=2247484740&idx=1&sn=3a62e0cc4905d77278ea557791c2c20e&scene=21#wechat_redirect)

```
{  "mcpServers": {    "jadx-mcp-server": {      "command": "F:/install/python11/python.exe",      "args": [        "E:/download/jadx-mcp-server-6.3.0/jadx-mcp-server/jadx_mcp_server.py"      ]    }  }}
```

command参数：本地python程序绝对路径

args参数：jadx\_mcp\_server.py文件绝对路径

TRAE成功连接jadx\_mcp\_server服务

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw5HycTIqDQI09zpBgeV7cF1WRzjLAuM9gj9AU0NwReShm7YicRl99tg8zQrE1ZgKnVL8ydgaFzclbUO0DUic9ZS1Dxynsak1xEHQ/640?wx_fmt=png&from=appmsg)

四、TRAE逆向分析APK案例

为了后续方便调用，这边新建一个apk逆向分析智能体，按照格式要求填写即可

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5pPk7mWhhmoAia4OdSamPzdib3JD56QibnZkJlnNREv5ibiaDKSc9HZ2ZTiaPQ5ia94wldKSchTibWvWYCxpd6nEnzicT0sbtuEuI4dVww/640?wx_fmt=png&from=appmsg)

提示词如下：

```
帮我分析当前 JADX 打开的 APK：1.解析应用清单，提取所有 Activity、Service、广播接收器及敏感权限；2.全局检索代码与字符串，挖掘硬编码接口地址、密钥、Token 等敏感信息；3.定位登录、网络请求、加密算法相关类与核心方法，逐行解析业务逻辑；4.针对混淆代码进行类功能划分、逻辑梳理，并给出合理重命名建议；5.开展安全审计，排查 WebView 漏洞、Intent 隐式调用、明文隐私存储、动态加载 Dex/So 等风险点；6.汇总整体架构、核心业务流程、安全隐患及逆向结论，条理清晰输出分析结果。
```

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5uFrX5ibGqxpK6z3lFD13n7CJj4tUvhuNEaDd5ibgsAq1qtJ23hNa5jZluZuKSt8aqZ8eUvNsO35XMtEOdyaAiaAtQZYkzJX6icyg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5dCjBsibz0auPggGWx4jZNG96boqwIpB0t6ubjCWaqOe5OjYicnwOt5oaAx1dicmUYbe8ssNbTvhlVDicuf4OdqlLdV7wNUcLcNoU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw7thtr6ubGdengyTT5r1ck0ZaZDzv78EPgibQNm8d2ia7m0kQheCqViaPP2FSCiadOEOiatQ2Z7av3MuoAWAyhoVButytxRfbFic6gkU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw4JCfYN1awWlFjy3W7IAfSviczvEGYeRc9egREAqulI03NZ7wnMfboryPFkdeYTX5fmOMwCWAUItia0Wicd2xBdXMZweOQ3taWRGk/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6icA95A0DazyibBuBlgxdu0I7Uur9m9tX1sdyI3HkB0MSnTicBxt0hWuSGAm7f3bVUWzO1xGDMlWcNSGYJaqrWJefgrlYtJFCpDY/0?wx_fmt=png)

huan666

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6icA95A0DazyibBuBlgxdu0I7Uur9m9tX1sdyI3HkB0MSnTicBxt0hWuSGAm7f3bVUWzO1xGDMlWcNSGYJaqrWJefgrlYtJFCpDY/0?wx_fmt=png)

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