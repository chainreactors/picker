---
title: LinuxCheck，一款开源的应急排查工具
url: https://mp.weixin.qq.com/s/DvPyJF7UQVeiCCq7V_FgpA
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:02:27.772450
---

# LinuxCheck，一款开源的应急排查工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5975bXHXfWEaUgwh8aicqtyghvQszunEibdPLCLFnkBVU2EemRK0QMajaoxQVnrHH1uLuAMntVfZpqeSNHQ5EJZA/0?wx_fmt=jpeg)

# LinuxCheck，一款开源的应急排查工具

泷羽Sec-Norsea

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于泷羽Sec
，作者仙草里没有草噜丶

![](http://wx.qlogo.cn/mmhead/Hp9HAaP9GFBKneKn5ryBUs0PRR7YFdhjkVm1EtmTw39DFXQog0cNn1NibPUo2tbPL2mH1HymCVxM/0)

**泷羽Sec**
.

B站：泷羽Sec，团队专注于网络安全领域的内容创作与分享，为网络安全而战。来自一个从零开始学习网安的见习生。很菜，不喜勿喷。

# LinuxCheck

LinuxCheck是一款集 Linux 应急处置、信息搜集与漏洞检测于一体的全能安全工具，覆盖基础配置、网络流量、任务计划、环境变量、用户信息、Services、bash、恶意文件、内核 Rootkit、SSH、Webshell、挖矿文件 / 进程、供应链及服务器风险等 13 大类 70 + 项检查，全方位排查服务器安全隐患。

## 功能

查基础运行：系统配置、软硬件资源（CPU / 内存 / 磁盘）是否正常；

查网络安全：端口、连接、防火墙等网络边界风险；

查权限用户：非法用户、权限漏洞、异常登录等内部风险；

查后门持久化：计划任务、环境变量、系统服务中的隐藏后门；

查恶意文件 / 进程：webshell、挖矿程序、黑客工具等入侵痕迹；

查高级威胁：Rootkit、供应链投毒、容器权限、高危服务漏洞等深度风险。

## Usage

第一种方式：通过git clone 安装

```
git clone https://github.com/al0ne/LinuxCheck.git
chmod +x LinuxCheck.sh
./LinuxCheck.sh
```

![image-20260111173228331](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWEaUgwh8aicqtyghvQszunEibpvvq9Pic3THhxkX41LHL0lb3qFJibEJawMCyjXTSbxsXGxbeVO82vyRA/640?wx_fmt=other&from=appmsg)

image-20260111173228331

![image-20260111173308956](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWEaUgwh8aicqtyghvQszunEibO0l1CicPjX4zkFaWbtQxAicysUGB8icPMaXMCzwxwZqIYm6yK6GzzQBPA/640?wx_fmt=other&from=appmsg)

image-20260111173308956

![image-20260111173333800](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWEaUgwh8aicqtyghvQszunEibp1D3XomicV1VojMhwNxJyFR0dOKb92K8L4f6BPC27quyyoOc3tX44Ag/640?wx_fmt=other&from=appmsg)

image-20260111173333800

[![](https://mmbiz.qpic.cn/mmbiz_jpg/5975bXHXfWEaUgwh8aicqtyghvQszunEibmkn2GJnTGaoOzv7RVvshpN88ztochPHJCsFZutLM7mytspGw9ODx6Q/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247510993&idx=1&sn=9c3325d8e93033eb13dee448cf4a81b9&scene=21#wechat_redirect)

第二种方式：直接在线调用【在线调用就没办法使用报告上传的能力】

```
bash -c "$(curl -sSL https://raw.githubusercontent.com/al0ne/LinuxCheck/master/LinuxCheck.sh)"
```

文件会保存成ipaddr\_hostname\_username\_timestamp.log 这种格式

### 报告自动上传

在你的服务器上用Flask起一个服务，接收服务器上报的Markdown报告。

```
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if'file'notin request.files:
        return"No file part", 400
    file = request.files['file']
    if file.filename == '':
        return"No selected file", 400
    if file:
        filename = file.filename
        file.save(filename)
        return"File successfully uploaded", 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
```

![image-20260111180945590](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWEaUgwh8aicqtyghvQszunEibYjmNx5P5mbQtfK9bMXEickAkPwYpaTic4fwmuUJq8jstjEibmFdonxNBw/640?wx_fmt=other&from=appmsg)

image-20260111180945590

脚本执行后会自动提交到某一个url下，将脚本里面的改成你自己的地址

```
curl -X POST -F "file=@demo.md" "http://127.0.0.1:5000/upload"
```

![image-20260111181029165](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWEaUgwh8aicqtyghvQszunEibthz90rNxkw1VDHURKv59p8S9vW1rYBuG8fMoVs4bE6BcWSXucfl46Q/640?wx_fmt=other&from=appmsg)

image-20260111181029165

![image-20260111181202470](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWEaUgwh8aicqtyghvQszunEibACIWq0uU1ceOjticvO2zqU29eiaCodmqLy4XOvdGTkytuZTgUyN5IPEg/640?wx_fmt=other&from=appmsg)

image-20260111181202470

## 往期推荐

开源地址：https://github.com/al0ne/LinuxCheck

广告时间

[![](https://mmbiz.qpic.cn/mmbiz_png/5975bXHXfWFdsXez4D9EyrgTaI0Kq2GGm1QC4vB2cwJ9Fd8OIMGA2w3FYRudNibbBOJAaqLfodyOtRTmzmIxNAg/640?wx_fmt=png&from=appmsg&watermark=1)](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247502572&idx=1&sn=42a9853381a099fc7c074230c39824a3&scene=21#wechat_redirect)

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