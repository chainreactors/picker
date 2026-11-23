---
title: [2026]不要追踪我 浏览器插件
url: https://key08.com/index.php/2026/11/23/3407.html
source: 白帽Wiki - 一个简单的wiki
date: 2026-11-22
fetch_date: 2026-11-23T10:02:33.998918
---

# [2026]不要追踪我 浏览器插件

[![](https://key08.com/avatar_pack.gif)](https://key08.com/)

# 白帽Wiki

从2012年开始专注高级网络安全技术研究

查你所想

![](https://key08.com/avatar_pack.gif)

### 一只鸭子

* [首页](https://key08.com/)
* [板块活动记录](https://key08.com/index.php/1596.html "板块活动记录")
* [IDA Internal](https://key08.com/index.php/2365.html "IDA Internal")
* [EDR开发相关](https://key08.com/index.php/project_ayy_waf.html "EDR开发相关")
* [威胁追踪](https://key08.com/index.php/cve_detect.html "威胁追踪")
* [Hypervisor](https://key08.com/index.php/hypervisor_code.html "Hypervisor")
* [机器学习&大模型](https://key08.com/index.php/keras.html "机器学习&大模型")
* [EFI驱动编写](https://key08.com/index.php/EFI_Driver_Code.html "EFI驱动编写")
* [关于&联系方式](https://key08.com/index.php/215273185.html "关于&联系方式")

×

# [白帽Wiki - 一个简单的wiki](https://key08.com/)

## [[2026]不要追踪我 浏览器插件](https://key08.com/index.php/2026/11/23/3407.html)

[huoji](https://key08.com/index.php/author/1/)
 [CLAUDE](https://key08.com/index.php/tag/CLAUDE/)
 2026-11-23
 83 次浏览
 0 次点赞

claude登录的时候各种追踪API太烦人了,所以做了这个
![](https://key08.com/usr/uploads/2026/11/3171115681.png)
![](https://key08.com/usr/uploads/2026/11/2505673704.png)
![](https://key08.com/usr/uploads/2026/11/3908473558.png)
梯子还得用,TUN模式+全局防止DNS泄漏.其他的没啥了
github:
https://github.com/huoji120/donot\_track\_me\_claude
限制: 对于硬件信息这个没办法改,硬件信息还得用指纹浏览器.但是claude不追这个.所以无所谓.
附带一个claude追踪hit,\*\*这些不代表claude会追踪,只是他用了这些API\*\*:
![](https://key08.com/usr/uploads/2026/11/1586097141.png)
```cpp
Canvas 文本绘制访问
newassets.hcaptcha.com/hsw.js
WebGL 参数或像素访问
newassets.hcaptcha.com/hsw.js
WebGPU API 访问
js.hcaptcha.com/api.js
音频采样或渲染访问
newassets.hcaptcha.com/hsw.js
Client Rects 布局尺寸
assets-proxy.anthropic.com/sections-QnNd9bkV.js
Client Rects 布局尺寸
newassets.hcaptcha.com/hsw.js
屏幕尺寸或色深
js.hcaptcha.com/api.js
屏幕尺寸或色深
newassets.hcaptcha.com/hcaptcha.html
触控点数
js.hcaptcha.com/api.js
触控点数
newassets.hcaptcha.com/hcaptcha.html
CPU 核数或内存读取
claude.ai/login
CPU 核数或内存读取
newassets.hcaptcha.com/hsw.js
媒体设备 API
newassets.hcaptcha.com/hsw.js
WebRTC 建立连接
newassets.hcaptcha.com/hsw.js
浏览器、系统或 UA 高熵信息
claude.ai/login
浏览器、系统或 UA 高熵信息
newassets.hcaptcha.com/hcaptcha.html
浏览器语言
assets-proxy.anthropic.com/signin-vMgxXVbH.js
浏览器语言
newassets.hcaptcha.com/hcaptcha.html
浏览器插件、MIME 或 PDF 能力
js.hcaptcha.com/api.js
浏览器插件、MIME 或 PDF 能力
newassets.hcaptcha.com/hsw.js
Cookie 状态或读取
claude.ai/login
地理位置 API
js.hcaptcha.com/api.js
字体 API 或文本尺寸
claude.ai/login
字体 API 或文本尺寸
newassets.hcaptcha.com/hsw.js
```

![](https://key08.com/usr/themes/GreenGrapes/img/creativecommons-cc.png)

本文由 [huoji](https://key08.com/index.php/author/1/) 创作，采用 [知识共享署名 3.0](http://creativecommons.org/licenses/by/3.0/cn)，可自由转载、引用，但需署名作者且注明文章出处。

 点赞 0

* 上一篇: [[2026]ClaudeCode 2.1.30x版本风控-Anthropic的追踪中转站的技术 x2](https://key08.com/index.php/2026/10/19/3369.html "[2026]ClaudeCode 2.1.30x版本风控-Anthropic的追踪中转站的技术 x2 ")
* 下一篇: 没有了

还不快抢沙发

[取消回复](https://key08.com/index.php/2026/11/23/3407.html#respond-post-3407)

添加新评论

提交评论

![icon_mrgreen.png](https://key08.com/usr/plugins/Smilies/tieba/icon_mrgreen.png)![icon_neutral.png](https://key08.com/usr/plugins/Smilies/tieba/icon_neutral.png)![icon_twisted.png](https://key08.com/usr/plugins/Smilies/tieba/icon_twisted.png)![icon_arrow.png](https://key08.com/usr/plugins/Smilies/tieba/icon_arrow.png)![icon_eek.png](https://key08.com/usr/plugins/Smilies/tieba/icon_eek.png)![icon_smile.png](https://key08.com/usr/plugins/Smilies/tieba/icon_smile.png)![icon_confused.png](https://key08.com/usr/plugins/Smilies/tieba/icon_confused.png)![icon_cool.png](https://key08.com/usr/plugins/Smilies/tieba/icon_cool.png)![icon_evil.png](https://key08.com/usr/plugins/Smilies/tieba/icon_evil.png)![icon_biggrin.png](https://key08.com/usr/plugins/Smilies/tieba/icon_biggrin.png)![icon_idea.png](https://key08.com/usr/plugins/Smilies/tieba/icon_idea.png)![icon_redface.png](https://key08.com/usr/plugins/Smilies/tieba/icon_redface.png)![icon_razz.png](https://key08.com/usr/plugins/Smilies/tieba/icon_razz.png)![icon_rolleyes.png](https://key08.com/usr/plugins/Smilies/tieba/icon_rolleyes.png)![icon_wink.png](https://key08.com/usr/plugins/Smilies/tieba/icon_wink.png)![icon_cry.png](https://key08.com/usr/plugins/Smilies/tieba/icon_cry.png)![icon_surprised.png](https://key08.com/usr/plugins/Smilies/tieba/icon_surprised.png)![icon_lol.png](https://key08.com/usr/plugins/Smilies/tieba/icon_lol.png)![icon_mad.png](https://key08.com/usr/plugins/Smilies/tieba/icon_mad.png)![icon_sad.png](https://key08.com/usr/plugins/Smilies/tieba/icon_sad.png)![icon_exclaim.png](https://key08.com/usr/plugins/Smilies/tieba/icon_exclaim.png)![icon_question.png](https://key08.com/usr/plugins/Smilies/tieba/icon_question.png)

![选择表情](https://key08.com/usr/plugins/Smilies/tieba/icon_smile.png)

[![](https://img.buymeacoffee.com/button-api/?text=Trust Feature For Human Duck&emoji=&slug=huoji&button_colour=16a085&font_colour=ffffff&font_family=Cookie&outline_colour=ffffff&coffee_colour=FFDD00)](https://www.buymeacoffee.com/huoji)

* [最新Wiki](#sidebar-new)
* [最新评论](#sidebar-comment)
* [随机Wiki](#sidebar-rand)

* [[2026]不要追踪我 浏览器插件](https://key08.com/index.php/2026/11/23/3407.html)
* [[2026]ClaudeCode 2.1.30x版本风控-Anthropic的追踪中转站的技术 x2](https://key08.com/index.php/2026/10/19/3369.html)
* [[2026]sub6api -前AI时代的OldSchool手艺人打造,无OpenAI降智,无Claude封号](https://key08.com/index.php/2026/10/17/3365.html)
* [[2026]一个token问题导致tsecbench-CTF的A-18(CloudFunc)做不出来](https://key08.com/index.php/2026/10/06/3360.html)
* [[2026]ClaudeCode(2.1.283)逆向和完整遥测分析](https://key08.com/index.php/2026/10/05/3348.html)
* [[2026]sm120上sglang的fp8的triton内核的矩阵乘性能问题](https://key08.com/index.php/2026/10/02/3341.html)
* [[2026]anthropic的追踪SUB2API技巧](https://key08.com/index.php/2026/09/30/3339.html)
* [[2026]qwen3.8系列微调的坑](https://key08.com/index.php/2026/09/27/3335.html)
* [[2026]AI大型虫群AGENT扩展涌现的智能研究](https://key08.com/index.php/2026/09/25/3327.html)
* [[2026]虫群Agent代码审计](https://key08.com/index.php/2026/09/13/3321.html)
* [[2026]防止自己的二进制文件被AI一键逆向](https://key08.com/index.php/2026/08/23/3296.html)
* [[2026]qwen-exo:基于 SGLang 二次开发的混合注意力推理后端](https://key08.com/index.php/2026/08/15/3283.html)
* [[2026]自回归 Shellcode 生成器：从一个玩笑到多项式回归](https://key08.com/index.php/2026/08/12/3278.html)
* [[2026]从模型注意力角度创建一个简单但高效的Agent](https://key08.com/index.php/2026/08/10/3275.html)
* [[2026]把大模型意识与记忆存到硬盘里面（上）](https://key08.com/index.php/2026/07/25/3251.html)

* YaCo：[那遇到这种情况怎么处理防封号呢?](https://key08.com/index.php/2026/10/19/3369.html/comment-page-1#comment-232)
* DEBUG\_X：[怎么加群](https://key08.com/index.php/215273185.html/comment-page-1#comment-231)
* debuger：[好文，眼目一新，比用了珍珠明还爽](https://key08.com/index.php/2026/08/23/3296.html/comment-page-1#comment-230)
* dbgbgtf：[以SHGlobalCounter这个共享内存为例, 该堆地址固定...](https://key08.com/index.php/2025/11/27/2991.html/comment-page-1#comment-229)
* dbgbgtf：[呃啊没事了, 原来是说定位桌面堆在用户态的映射吗](https://key08.com/index.php/2024/10/27/2253.html/comment-page-1#comment-228)
* dbgbgtf：[但是有个问题,没办法定位目标进程的cls地址,因为那个地方是每个...](https://key08.com/index.php/2024/10/27/2253.html/comment-page-1#comment-227)
* dbgbgtf：[师傅cls的额外内存既然是在内核中, 那对于每个进程映射到的虚拟...](https://key08.com/index.php/2024/10/27/2253.html/comment-page-1#comment-226)
* 还是丫丫强：[还是丫丫强](https://key08.com/index.php/2021/08/12/1292.html/comment-page-1#comment-225)
* hhh：[目前我也在研究AI应用，拜读过你博客的很多文章，尤其是AI应用于...](https://key08.com/index.php/2026/07/19/3217.html/comment-page-1#comment-224)
* 电脑维修：

* [[2022]Windows ALPC解码:(二)](https://key08.com/index.php/2022/03/27/1449.html "[2022]Windows ALPC解码:(二)")
* [[2022]hypervisor: 检测与预防（四）](https://key08.com/index.php/2022/10/01/1594.html "[2022]hypervisor: 检测与预防（四）")
* [此内容已经被删除](https://key08.com/index.php/2020/12/02/BE_SHELLCODE.html "此内容已经被删除")
* [[2021]余弦定理检测文件相似度 & 病毒样本基因检测](https://key08.com/index.php/2021/08/19/1306.html "[2021]余弦定理检测文件相似度 & 病毒样本基因检测")
* [[2024]愚蠢的windows进程隐藏技术](https://key08.com/index.php/2024/04/08/1842.html "[2024]愚蠢的windows进程隐藏技术")
* [此内容已经被删除](https://key08.com/index.php/2020/03/29/673.html "此内容已经被删除")
* [此内容已经被删除](https://key08.com/index.php/2019/11/29/357.html "此内容已经被删除")
* [[20...