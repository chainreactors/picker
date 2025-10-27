---
title: 本地用AIGC生成图像与视频
url: https://blog.csdn.net/ariesjzj/article/details/136750337
source: 世事难料，保持低调
date: 2024-03-17
fetch_date: 2025-10-04T12:07:31.446830
---

# 本地用AIGC生成图像与视频

# 本地用AIGC生成图像与视频

最新推荐文章于 2025-07-10 09:57:52 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[ariesjzj](https://jinzhuojun.blog.csdn.net "ariesjzj")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
最新推荐文章于 2025-07-10 09:57:52 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量3.5k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

24

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
11

CC 4.0 BY-SA版权

文章标签：
[AIGC](https://so.csdn.net/so/search/s.do?q=AIGC&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[Diffusion](https://so.csdn.net/so/search/s.do?q=Diffusion&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[生成](https://so.csdn.net/so/search/s.do?q=%E7%94%9F%E6%88%90&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[视频生成](https://so.csdn.net/so/search/s.do?q=%E8%A7%86%E9%A2%91%E7%94%9F%E6%88%90&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[图像生成](https://so.csdn.net/so/search/s.do?q=%E5%9B%BE%E5%83%8F%E7%94%9F%E6%88%90&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[ComfyUI](https://so.csdn.net/so/search/s.do?q=ComfyUI&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[Sora](https://so.csdn.net/so/search/s.do?q=Sora&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/jinzhuojun/article/details/136750337>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756916.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

AI
专栏收录该内容](https://blog.csdn.net/ariesjzj/category_1243833.html "AI")

43 篇文章

订阅专栏

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)本文介绍了AI领域的热门话题Sora，特别是StableDiffusion和StableVideoDiffusion（SVD）的开源模型。作者详细展示了如何在本地GPU机器上安装和运行这些模型，包括文生图、图生图和视频生成，以及使用StableDiffusionWebUI和ComfyUI等工具进行更直观的交互式体验。

最近AI界最火的话题，当属[Sora](https://openai.com/sora)了。遗憾的是，Sora目前还没开源或提供模型下载，所以没法在本地跑起来。但是，业界有一些开源的图像与视频生成模型。虽然效果上还没那么惊艳，但还是值得我们体验与学习下的。

Stable Diffusion（SD）是比较流行的开源方案，可用于文生图、图生图及图像修复。Stability AI最近发布了[Stable Diffusion 3](https://stability.ai/news/stable-diffusion-3)，采用的是与Sora类似的Diffusion Transformer（DiT）技术。另外，Stable Video Diffusion（SVD）将图像升级到视频，可用于文生视频和图生视频。

下面介绍下如何在本地机器上运行SD和SVD。首先假定有一台带GPU的机器（本人用的RTX 4070），并装好Python和CUDA基本环境。

### Stable Diffusion

最简单的方式是用Python脚本运行。我们可以用[diffusers](https://github.com/huggingface/diffusers)库来运行。该库集成了各种diffusion pipeline。注意脚本可能尝试从hugging-face官方下载模型。如果下载失败，可以设置下面的环境变量：

```
export HF_ENDPOINT=https://hf-mirror.com
```

按官方文档（https://hf-mirror.com/runwayml/stable-diffusion-v1-5）运行Stable diffusion 1.5：

```
from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]

image.save("astronaut_rides_horse.png")
```

运行上面脚本，结果：
 ![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/536adfb5a0803561ffa18700cc8ce9d0.png)

运行Stable Diffusion 2.1也是类似的。运行官方例子：

```
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

model_id = "stabilityai/stable-diffusion-2-1"

# Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]

image.save("astronaut_rides_horse.png")
```

结果：
 ![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/911dbf5bae93b873d32bea648414f8c4.png)

以上是文生图。图生图，图像修补的使用可参见：

* https://hf-mirror.com/docs/diffusers/en/using-diffusers/img2img
* https://hf-mirror.com/docs/diffusers/en/using-diffusers/inpaint

对结果不太满意可以调节参数。

Stable Diffusion XL（SDXL）是一个更为强大的生成模型。用法可参见：https://hf-mirror.com/docs/diffusers/en/using-diffusers/sdxl。比如文生图的例子：

```
from diffusers import AutoPipelineForText2Image
import torch

pipeline_text2image = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
).to("cuda")

prompt = "a photo of an astronaut riding a horse on mars"
image = pipeline_text2image(prompt=prompt).images[0]

image.save("astronaut_rides_horse.png")
```

结果：
 ![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/d5759945796fb3d7ec0d38e01776346d.png)

如果想用TensorRT加速的话可参见：https://github.com/NVIDIA/TensorRT/tree/release/8.6/demo/Diffusion。在此不再累述。

### Stable Video Diffusion

Stable Video Diffusion（SVD）可用于生成视频。使用方法可参见：https://hf-mirror.com/docs/diffusers/en/using-diffusers/text-img2vid。如官方中的例子：

```
import torch
from diffusers import StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video

pipeline = StableVideoDiffusionPipeline.from_pretrained(
    "stabilityai/stable-video-diffusion-img2vid", torch_dtype=torch.float16, variant="fp16"
)
pipeline.enable_model_cpu_offload()

image = load_image("https://hf-mirror.com/datasets/huggingface/documentation-images/resolve/main/diffusers/svd/rocket.png")
image = image.resize((1024, 576))

generator = torch.manual_seed(42)
frames = pipeline(image, decode_chunk_size=8, generator=generator).frames[0]
export_to_video(frames, "generated.mp4", fps=7)
```

由于stable-video-diffusion-img2vid-xt在我的4070卡上貌似会OOM，因此换成stable-video-diffusion-img2vid。

结果：

### Stable Diffusion web UI

前面都是用的Python脚本。要调模型的各种参数需要改调用参数，不太易用和直观。接下来看看怎么基于Diffusion模型构建App。

[stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)是用Gradio库实现的Stable Diffusion的web接口。在Linux环境可以按照以下文档搭环境：
 https://github.com/AUTOMATIC1111/stable-diffusion-webui?tab=readme-ov-file#automatic-installation-on-linux

如果在执行webui.sh的过程碰到下面问题：

```
stderr: ERROR: Could not find a version that satisfies the requirement tb-nightly (from versions: none)
ERROR: No matching distribution found for tb-nightly
```

可以换成阿里的pip源：

```
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
```

另外脚本中会尝试从hugging-face官网下载，无法下载的话可以将地址替换成：

```
diff --git a/modules/sd_models.py b/modules/sd_models.py
index 9355f1e1..bf5dbba5 100644
--- a/modules/sd_models.py
+++ b/modules/sd_models.py
@@ -150,7 +150,7 @@ def list_models():
     if shared.cmd_opts.no_download_sd_model or cmd_ckpt != shared.sd_model_file or os.path.exists(cmd_ckpt):
         model_url = None
     else:
-        model_url = "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors"
+        model_url = "https://hf-mirror.com/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors"

     model_list = modelloader.load_models(model_path=model_path, model_url=model_url, command_path=shared.cmd_opts.ckpt_dir, ext_filter=[".ckpt", ".safetensors"], download_name="v1-5-pruned-emaonly.safetensors", ext_blacklist=[".vae.ckpt", ".vae.safetensors"])
```

脚本执行完，顺利的话就可以看到UI界面了。随便输入点啥点Generate按钮就可以出图了。
 ![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/8043c93f25c1e1ed9620ebee2a5f9059.png)

### ComfyUI

[ComfyUI](https://blenderneko.github.io/ComfyUI-docs/)是图形化、模块化的Diffusion模型工作流构建工具。此外它还支持插件扩展。可以按照https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file#nvidia搭建环境，最后运行：

```
python main.py
```

运行成功后，打开`http://127.0.0.1:8188`，就可以看到UI界面：
 ![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/f02ffe61d8602ebf1814707f74824c72.png)

接下来准备模型：

```
cd models/checkpo...