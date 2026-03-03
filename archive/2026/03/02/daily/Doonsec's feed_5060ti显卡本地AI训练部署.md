---
title: 5060ti显卡本地AI训练部署
url: https://mp.weixin.qq.com/s/IQ20ABZJB0EMOq2x-83bdQ
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:06:31.024373
---

# 5060ti显卡本地AI训练部署

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oltLnnib9JXQiauVluyBITpibHzJR69Af3fibIckgmDlE1icTXt24Qu4Mpr6gXJRohGia3qHQok5wvNevDd2okEib3GgtWCkunm8okUL42Hicg2dICs/0?wx_fmt=jpeg)

# 5060ti显卡本地AI训练部署

原创

LRT凌日
LRT凌日

凌日网络与信息安全团队

![]()

在小说阅读器中沉浸阅读

## 前言

```
1. 前面配置的时候找了很多文章来看，都有着各种奇奇怪怪的问题，本文将记录我配置成功的一次案例供大家参考。2025年11月24日记这是我第一次实现大模型的微调训练，电脑的配置是显卡NVIDIA GeForce RTX 5060Ti GPU，训练的是DeepSeek-r1 的7B模型如果大家有更好的显卡，可以尝试一下14B。在此非常感谢CSDN的大佬，在他们的基础上，我的博客进一步完善一些细节，文末会附上大佬的原文链接。那么废话不多说，直接开始！（默认大家有一定的基础）
```

##

# 1.前置条件

## 1.1 基础配置

（具体的安装和使用教程网上有很多，在这里就不做过多的赘述了）

1. 使用Anaconda （Python的环境管理工具），这样就不需要一个一个单独下载python的版本，并且使用起来很方便。

Anaconda官网(https://www.anaconda.com/download/success)

1. 使用PyCharm （Python的集成开发环境），可以在这里面编辑、运行.py文件等操作。

PyCharm官网(https://www.jetbrains.com/zh-cn/pycharm/)

1. 使用Git（分布式版本控制系统），用于克隆 GitHub上的优秀项目，不用也没事，可以直接下载.zip文件。

Git官网(https://git-scm.com/?hl=zh-cn)

1. 使用CUDA 和cuDNN（用于GPU训练加速），需要注意这里面的版本关系，别下错了。

CUDA 官网(https://developer.nvidia.com/cuda/toolkit)
cuDNN官网(https://developer.nvidia.com/cudnn)
5.使用PyTorch（深度学习框架），这个版本要与你自己电脑的CUDA版本对应。

PyTorch官网(https://pytorch.org/)
以上就是环境配置需要的全部内容，接下来我们就进行项目 复刻。

## 1.2安装anaconda3

这个没什么说的，直接官网上面下载安装包，拉到本地后一直点下一步 ，注意：选择较大的磁盘放置，不建议放系统盘

![](https://mmbiz.qpic.cn/mmbiz_png/oltLnnib9JXT5uQ8GBDT4JQmicnm4rHgBewchPoBaTNiarRkCTIYQBNnm6ic1kUGNjcpwOYFDa3TMmm88mVzKxXXTQqa5nnUtWUxZQv57ZUnNwY/640?wx_fmt=png&from=appmsg)

## 1.3初始化环境

打开Anaconda Prompt（从Windows开始菜单找到），执行

创建新的虚拟环境

```
1. conda create -n llama python=3.10
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oltLnnib9JXSwHhEfMh0uMIxNeO19Cmut9fFPPA3Y9WU3e4LaUh1MBvQmTzM2lz1ibibI5S1PkibgR75ziagl7Elv3vNeicwGJon0RURgnn7WwGtQ/640?wx_fmt=png&from=appmsg)

激活虚拟环境

```
1. conda activate llama
```

![](https://mmbiz.qpic.cn/mmbiz_png/oltLnnib9JXTsrNk5XWyg112GkUuCBdlibBBeblSUF4NibyqicCGb6icmMKWT4kGib7hRAGB2oiaCTYjNLPSIuj2Ficu4xU80pUr9ibZXdLMxghW0CyA/640?wx_fmt=png&from=appmsg)

安装支持 sm\_120 的 PyTorch（5060ti的CUDA是12.8/12.9，选择支持你们自己电脑的CUDA的版本

```
1. # 先安装PyTorch CUDA版本（官方源），再安装其他依赖（清华源）
2. pip install torch==2.8.0--index-url https://download.pytorch.org/whl/cu128
3. pip install torchvision==0.23.0 torchaudio==2.8.0-i https://pypi.tuna.tsinghua.edu.cn/simple
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oltLnnib9JXShxicawW1w99zE6zz1IX17xibsC6pjWOlnslPz9MDKbEFic1kGNUtyf1seC3iaLKdqzG5fJy9JYY6YSpqb1zJhV6wGaVQAG1tSExM/640?wx_fmt=png&from=appmsg)

这个地方我没有跑动，所以采取了下述方法

```
1. 手动下载 CUDA 12.8版的PyTorch whl 包

3. pip 直接下载官方源容易超时，手动下载是最稳定的方式，步骤如下：

5. 打开浏览器，访问PyTorch官方 cu128 源的索引页：https://download.pytorch.org/whl/cu128/torch/
6. 在页面中找到适配你环境的 whl 包：我的环境是Python3.10+Windows AMD64，对应包名是：torch-2.8.0%2Bcu128-cp310-cp310-win_amd64.whl（%2B是+的 URL 编码，下载后文件名会自动还原）。
7. 点击该链接开始下载（文件大小约3.2GB），若浏览器下载慢，可复制链接到迅雷/ IDM等下载工具，利用多线程加速。
8. 记住下载的保存路径（比如G:\AI\downloads\或C:\Users\Administrator\Downloads\）。![](https://mmbiz.qpic.cn/mmbiz_png/oltLnnib9JXRjhanicohZqibK3FibVgIePia5oVge0Fsa1Ndv9mSFsKlzhRxuVibs8Tibq45BzbHI66ReFv7KKJZiceia9EEMSl8pCkbecmbx3pOnHdM/640?wx_fmt=png&from=appmsg)

10. 本地安装 CUDA 版PyTorch

12. 打开命令行（确保已激活llama环境），切换到 whl 包的下载目录，执行本地安装命令：
13. # 示例：假设包下载到了Downloads文件夹，替换为你的实际路径
14. cd C:\Users\Administrator\Downloads
15. # 执行安装（包名根据实际下载的文件名调整）
16. pip install torch-2.8.0+cu128-cp310-cp310-win_amd64.whl
```

验证脚本

```
1. import torch
2. print("PyTorch版本：", torch.__version__)
3. print("CUDA是否可用：", torch.cuda.is_available())
4. print("CUDA版本：", torch.version.cuda if torch.cuda.is_available()else"None")
5. if torch.cuda.is_available():
6. print("GPU设备：", torch.cuda.get_device_name(0))
7. print("GPU数量：", torch.cuda.device_count())
```

预期输出：

![](https://mmbiz.qpic.cn/mmbiz_png/oltLnnib9JXQhAND0qmpIpibcXtPdibUA2CSYTFCxX5lIOTqzYcQCspbzicsK1gOIPAwqkCWicBwfViapJaW52kG4r9wwL5BL9pkcjnAYAF54fCl4/640?wx_fmt=png&from=appmsg)

接下来就是:克隆GitHub 项目

```
1. #git拉取
2. pip install -e ".[torch,metrics]"-i https://pypi.tuna.tsinghua.edu.cn/simple/

4. #或者镜像源直接下
5. pip install -e ".[torch,metrics]"-i https://pypi.tuna.tsinghua.edu.cn/simple/
```

下载下来后直接pycharm打开

![](https://mmbiz.qpic.cn/mmbiz_png/oltLnnib9JXTVvQAGKE06DPsdBEuU4waWGptUGqxeFPWic9G5NZ21Q0ZqVrrmeCtdzMrx8gAuibW4wDPRZLZC5I3iaRMXfYwXBHkj5Hx6m3lesk/640?wx_fmt=png&from=appmsg)

验证（出现版本号就成功了）

```
1. llamafactory-cli version
```

## ![](https://mmbiz.qpic.cn/mmbiz_png/oltLnnib9JXTRvw0T0UbibddOrA6mliaRa6D7OzFcVEI3KKMjR3vFxCtaY3biaaicLyaV7nY9mH7UJVV2SuS6yYV1xCXpDmx3XS34ibyJQWtqguGk/640?wx_fmt=png&from=appmsg)

## 1.4下载大模型

在终端输入如下指令，修改大模型存放位置（选择一个合适足够大的存储位置

```
1. echo $env:HF_HOME ="G:\AI\Hugging-Face"
```

修改大模型下载位置（这个一般不需要修改）

```
1. echo $env:HF_ENDPOINT="https://hf-mirror.com"
```

安装huggingface\_hub（如果第一个下载爆红，可以试试第二个镜像源）

```
1. pip install -U huggingface_hub

3. #或者

5. pip install -U huggingface_hub -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oltLnnib9JXT8j7Jwctj0t670mba155nYDzGpQzuN3na6zDAW8pmX4lC4FyqAMEY7d4t2tR76JF320UWUj1nZ0YpeEJ1shBsVjRmeFr0rmCE/640?wx_fmt=png&from=appmsg)

下载训练模型

```
1. huggingface-cli download --resume-download deepseek-ai/DeepSeek-R1-Distill-Qwen-7B

3. 如果上述有问题可采用这个办法解决：

6. 右键「此电脑」→「属性」→「高级系统设置」→「环境变量」。
7. 在用户变量或系统变量中，点击「新建」：
8. 变量名：HF_ENDPOINT
9. 变量值：https://hf-mirror.com
10. 点击「确定」保存，重启命令行窗口（环境变量生效）。
11. 直接执行简化的下载命令即可：
12. #直接使用
13. python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='deepseek-ai/DeepSeek-R1-Distill-Qwen-7B')"

15. # 或者临时配置镜像后，指定保存路径到G盘的AI目录
16. set HF_ENDPOINT=https://hf-mirror.com
17. python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='deepseek-ai/DeepSeek-R1-Distill-Qwen-7B', local_dir='G:/AI/DeepSeek-R1-Distill-Qwen-7B')"
```

## ![](https://mmbiz.qpic.cn/mmbiz_png/oltLnnib9JXSXywlicxVCLWlMtIS3B2KuU6rBIOYJuEoIoj8Dp8maM9TvmQl7NYLYMicNxNN84Miamu3NT7eia3PFUgtPNhDNu8kzFXDePz4ib0WI/640?wx_fmt=png&from=appmsg)1.5制作训练集（json格式）

```
1. {
2. "messages":[
3. {
4. "role":"user",
5. "content":[{"type":"text","value":"hi"}],
6. "loss_weight":0.0
7. },
8. {
9. "role":"assistant",
10. "content":[{"type":"text","value":"Hello! I am LAP酱, an AI assistant developed by BINGCHN. How can I assist you today with your CTF challenges?"}],
11. "loss_weight":1.0
12. }
13. ]
14. }
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oltLnnib9JXSLhF2RcotYNw5PXByibMypWLBWDm419ONL9eoe1XQMphaak14NNOlIOhPoSrDEbsK61T1xenUnkNHnrfDIS6iatp9jHWuIGkP00/640?wx_fmt=png&from=appmsg)

配置训练集

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/oltLnnib9JXSblGIkew0nHsnfHeGMHVhzbUcLkpjv2HfcCfxmTibBkk5JXsgKrXUXlfcbBgUEXsxPB7ePCBHkfm9nWsMAEwuNW0fYEGJfTGXU/640?wx_fmt=png&from=appmsg)

## 1.6启动LLama-Factory 的可视化微调界面（http://localhost:7860/）

```
1. llamafactory-cli webui
```

如果报错可以检查一下huggingface-hub版本，建议使用0.34.0

![](https://mmbiz.qpic.cn/mmbiz_png/oltLnnib9JXTOAOSslGS6V3pAicwvMQDn8ft8vyZ1zsa1Eib8IKK6MlCrCibiaUqn0yL9s8ZcXJ9rOLRul25d6MR0UygWkagkFonB2U4RjR4rxwA/640?wx_fmt=png&from=appmsg)最后就是看后面的东西了

## 注：文章涉及内容仅供安全研究与学习之用，若将文章相关内容做其他用途，由使用者承担全部法律及连带 责任，作者及发布者不承担任何法律及连带责任。信息及工具收集于互联网，真实性及安 全性自测！！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ZbX8Cxthu0CZGQU867Mg22uLkuqDzYgZyVX8R2TmCQlYuI2TVEClWUiaC8GbpZRfUgN1kaCiaiaU8kDW5GwmZu8OQ/0?wx_fmt=png)

凌日网络与信息安全团队

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZbX8Cxthu0CZGQU867Mg22uLkuqDzYgZyVX8R2TmCQlYuI2TVEClWUiaC8GbpZRfUgN1kaCiaiaU8kDW5GwmZu8OQ/0?wx_fmt=png)

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