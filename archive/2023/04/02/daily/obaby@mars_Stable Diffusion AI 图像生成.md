---
title: Stable Diffusion AI 图像生成
url: https://h4ck.org.cn/2023/04/stable-diffusion-ai-%e5%9b%be%e5%83%8f%e7%94%9f%e6%88%90/
source: obaby@mars
date: 2023-04-02
fetch_date: 2025-10-04T11:26:43.965836
---

# Stable Diffusion AI 图像生成

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[人工智能『AI』](https://h4ck.org.cn/cats/cxsj/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E3%80%8Eai%E3%80%8F)

# Stable Diffusion AI 图像生成

2023年4月1日
[18 条评论](https://h4ck.org.cn/2023/04/11727#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/04/00077-2903331190-tuya.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/04/00077-2903331190-tuya.png) [![](https://image.h4ck.org.cn/wp-content/uploads/2023/04/00071-441166615-tuya.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/04/00071-441166615-tuya.png)

之前在[明眸如初](https://www.zywvvd.com/notes/study/deep-learning/generation/diffusion-model/stable-diffusion/stable-diffusion/)，看到了一篇文章，关于ai生成图片的。恰好比较感兴趣，于是就想着尝试一下。其实整体的安装步骤，已经这篇文章已经写的比较清楚了。可以照搬，一般问题不大。这里记录下我的安装方法。

由于系统的anaconda比较老旧，安装的python版本也不对应，导致通过conda创建的虚拟环境安装失败了，Stable Diffusion web UI推荐的python环境为3.10.6，所以直接下载了这个版本安装，下载地址：https://www.python.org/downloads/windows/，由于电脑上的python版本比较多，也不想把这个东西加到系统变量的path内，所以可以直接通过运行指定的python可执行文件创建venv。

```
F:\Pycharm_Projects\stable-diffusion-webui>D:\Python3.10.6\python.exe -m venv venv
```

F:\Pycharm\_Projects\stable-diffusion-webui为Stable Diffusion web UI的下载目录。

创建虚拟环境之后，修改webui-user.bat指定python文件路径和venv的路径，如下：

```
@echo off

set PYTHON=D:\Python3.10.6\python.exe
set GIT=
set VENV_DIR=F:\Pycharm_Projects\stable-diffusion-webui\venv
set COMMANDLINE_ARGS=

call webui.bat
```

执行bat文件的时候切换到代码目录下，否则会提示找不到webui.bat。

由于需要通过github下载各种库，所以执行webui-user.bat之前，最好设置好梯子。以免文件下载失败，导致安装失败。

由于我的电脑之前跑过yolov5，所以cuda的环境之前就已经安装好了，如果没有安装，通过这个地址下载安装https://developer.nvidia.com/cuda-11-7-0-download-archivetorch，一般网络通常的情况下环境直接通过bat自动就全部完成了，安装完成之后会在7860端口启动一个web服务：

```
F:\Pycharm_Projects\stable-diffusion-webui>webui-user.bat
venv "F:\Pycharm_Projects\stable-diffusion-webui\venv\Scripts\Python.exe"
Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)]
Commit hash: 22bcc7be428c94e9408f589966c2040187245d81
Installing requirements for Web UI
Launching Web UI with arguments:
No module 'xformers'. Proceeding without it.
Loading weights [6ce0161689] from F:\Pycharm_Projects\stable-diffusion-webui\models\Stable-diffusion\v1-5-pruned-emaonly.safetensors
Creating model from config: F:\Pycharm_Projects\stable-diffusion-webui\configs\v1-inference.yaml
LatentDiffusion: Running in eps-prediction mode
DiffusionWrapper has 859.52 M params.
Applying cross attention optimization (Doggettx).
Textual inversion embeddings loaded(0):
Model loaded in 3.0s (load weights from disk: 0.2s, create model: 0.4s, apply weights to model: 0.5s, apply half(): 0.6s, move model to device: 0.5s, load textual inversion embeddings: 0.8s).
Running on local URL:  http://127.0.0.1:7860
```

通过浏览器的7860端口就可以访问服务了：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/04/搜狗截图20230401222758.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/04/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230401222758.png)

相关的模型可以通过https://civitai.com这个网站下载

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/04/搜狗截图20230401222936.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/04/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230401222936.png)

点击右侧的绿色箭头可以看到支持的环境：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/04/搜狗截图20230401222946.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/04/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230401222946.png)

选择支持Automatic 1111 Web UI (Local) 的模型即可，下载之后放入Stable Diffusion web UI目录下的models\Stable-diffusion文件夹下：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/04/搜狗截图20230401223254.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/04/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230401223254.png)

点击页面的刷新按钮，重新加载即可选择不同的模型进行生成。

最后需要关注的就是prompt 和negative prompt 关键词，这两个关键词除了描述要生成的对象，更多的一部分是对ai生成的图片的一些限制说明，例如分辨率，不要生成卡通图片之类的。这些可以自己去尝试，我尝试了两组，效果还算不错：

```
第一组：
prompt:
<lora:addielyn_v1_chilloutmix_NiPrunedFp16Fix_100_33pic_epoc:0.6666> extremely detailed （(addielyn）)， detailed eyes，

（Best quality details:1.2），realistic，8K High definition，(1girl:1.2)，Ultra Detailed，High quality texture，intricate details，detailed texture，finely detailed，high detail，extremely detailed cg，High quality shadow，Detailed beautiful delicate face，Detailed beautiful delicate eyes，Depth of field，Ray tracing，(a beautiful25age years old sexy korean woman:1.1)，medium breast， tall_female， beautiful_legs， Glow Eyes，blush， perfect body，skinny， (black sweater:1.4)， (open grey coat:1)，(short plaid tight skirt :1.2)， (stockings_garterbelt:1.1， stilleto:1.1)， (bob cut:1.1)， street， sunlight， kneeling on sofa， earrings，necklace， model， looking at viewer， from side， dynamic pose， mole under eye，

Negative prompt:
（worst quality， low quality:1.4），lowres，low quality anatomy，ugly，more than two people，split picture，split screen，two or more pictures，Ignoring prompts，individual screen，low quality four fingers and low quality thumb，complicated fingers，fingerless，extra limbs，signature，watermark，username，fat，Chubby，dark skin，ugly face，ugly nose，outline，low quality face，low quality eyes，polydactyly，low quality body，low quality ratio，broad shoulders，low detail clothes，cheekbone， animal， dolphin， latex， nsfw， posing， hands，

第二组：
prompt:
（8k， RAW photo， best quality， masterpiece:1.2）， (realistic， photo-realistic:1.37)，1girl，cute，cityscape， night， rain， wet， professional lighting， photon mapping， radiosity， physically-based rendering，

（8k， RAW photo， best quality， masterpiece:1.2）， (realistic， photo-realistic:1.37)，1girl，cute，cityscape，sunny ， professional lighting， photon mapping， radiosity， physically-based rendering，full body

Negative prompt:
paintings， sketches， （worst quality:2）， (low quality:2)， (normal quality:2)， lowres， normal quality， ((monochrome))， ((grayscale))， skin spots， acnes， skin blemishes， age spot， glans
```

可以切换不同的模型进行尝试：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/04/搜狗截图20230401220310.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/04/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230401220310.png) [![](https://image.h4ck.org.cn/wp-content/uploads/2023/04/搜狗截图20230401215749.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/04/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230401215749.png) [![](https://image.h4ck.org.cn/wp-content/uploads/2023/04/搜狗截图20230401215624.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/04/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230401215624.png) [![](https://image.h4ck.org.cn/wp-content/uploads/2023/04/搜狗截图20230401215121.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/04/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230401215121.png)

对于我的电脑来说768\*768基本就是极限了，显存基本跑慢了，如果到1024直接就崩溃了提示内存不足：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/04/搜狗截图20230401221049.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/04/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230401221049.png)

github上也给出了具体的解决方案：https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Troubleshooting，我还没尝试，等后续有时间再尝试。

生成的图片，效果也还ok：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/04/00044-250541623-tuya.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/04/00044-250541623-tuya.png) [![](https://image.h4ck.org.cn/wp-content/uploads/2023/04/00056-3404462425-tuya.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/04/00056-3404462425-tuya.png) [![](https://image.h4ck.org.cn/wp-content/uploads/202...