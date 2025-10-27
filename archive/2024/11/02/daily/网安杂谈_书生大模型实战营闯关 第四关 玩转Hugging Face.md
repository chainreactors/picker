---
title: 书生大模型实战营闯关 第四关 玩转Hugging Face
url: https://mp.weixin.qq.com/s?__biz=MzAwMTMzMDUwNg==&mid=2650889190&idx=1&sn=ce89b5c3f78f85d88f404ee8df97524c&chksm=812ea7c3b6592ed5300c1e137344eb393f711d2c38e5c504663629304aaa5c46d5e308901824&scene=58&subscene=0#rd
source: 网安杂谈
date: 2024-11-02
fetch_date: 2025-10-06T19:18:08.418970
---

# 书生大模型实战营闯关 第四关 玩转Hugging Face

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z4jKmMQicbWPSKwPkbW3knibsYvAPtPNaO1opmV7fe7kJnhLIem7gny8dWP8YOia8j6VJDZ14KicGplaOWw04UFQAw/0?wx_fmt=jpeg)

# 书生大模型实战营闯关 第四关 玩转Hugging Face

网安杂谈

网安杂谈

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgichzau3fnMFSic2pFIVamY8HovMFlCENmnN2MCbEs1yyoVdzUKXBAicZg/640?wx_fmt=other)

这一关的任务是学习Hugging Face，学习模型下载、上传以及创建专属Space

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWPSKwPkbW3knibsYvAPtPNaO0QgBP6HrTtic1EPNGhEImFDpJlAKm6uQFCoJAat1cA9taKw0TQnZNxQ/640?wx_fmt=png)

1.HF 平台

Hugging Face是一个拥有超过100,000个预训练模型和10,000个数据集的平台，被誉为机器学习界的GitHub。

官网地址：

https://huggingface.co/

Hugging Face上的书生大模型地址

https://huggingface.co/internlm

看这有一系列不同种类的大模型，确实有点眼花缭乱的。我们主要更关注InernLM,这是一系列多语言基础模型和聊天模型。以internlm2\_5-1\_8b举例，查看Hugging Face上该模型的地址为：internlm/internlm2\_5-1\_8b · Hugging Face

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWPSKwPkbW3knibsYvAPtPNaOicibTzBzpSUAch8ibicI83sAsG3EGnMUn6tdR5XjdgTrtCO9kHuudxNqzw/640?wx_fmt=png)

2.Hugging Face Spaces的使用

Hugging Face Spaces 允许轻松地托管、分享和发现基于机器学习模型的应用的平台。Spaces 使得开发者可以快速将我们的模型部署为可交互的 web 应用，且无需担心后端基础设施或部署的复杂性。首先访问以下链接，进入Spaces。在右上角点击Create new Space进行创建。

https://huggingface.co/spaces

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWPSKwPkbW3knibsYvAPtPNaOicWVyOUNSvt48voX0aswpdl6jB63dibHg9dZqQ5CPg3FqKzbhhPWM0Qg/640?wx_fmt=png)

在创建页面中，输入项目名为intern\_cobuild，并选择Static应用进行创建。就生成了一个默认的项目页面。

我们再回到自己的开发机，这里我用一下github的Github CodeSpace

https://github.com/codespaces

把刚才创建的Hugging Face Spaces项目拉取回来。同时编辑index.html文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWPSKwPkbW3knibsYvAPtPNaO14Ac4YImmrgghY2ibLHd1eGXLYllJI3qtQSXaUP3SSOAqibrTpFnicfsA/640?wx_fmt=png)

保存后就可以push到远程仓库上了，会自动更新页面。

要注意，huggingface的 remote: Password authentication in git is no longer supported. You must use a user access token or an SSH key instead

所以还不能直接push，而是要获取一个access key

You will need to generate an access token for your account; you can follow https://huggingface.co/docs/hub/security-tokens#user-access-tokens to generate one.

After generating your access token, you can update your Git repository using the following commands:

$: git remote set-url origin https://:@huggingface.co/

$: git pull origin

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWPSKwPkbW3knibsYvAPtPNaOVvVnr1Sr9Tgk1DCrbjZLwMuicOib9AUNEcJQ6ljmlUOBJk8XCXyeqiaPQ/640?wx_fmt=png)

这时候，再打开我们创建的huggingface space，就出现书生共建的画面了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWPSKwPkbW3knibsYvAPtPNaO2GichS5Q8cSFnl2lBf5n8Ww7aLXSsHQh92aVib6BbHmWKPpoP7ZIlFuQ/640?wx_fmt=png)

3.模型下载

先新建一个hf\_download\_josn.py 文件

```
import osfrom huggingface_hub import hf_hub_download
# 指定模型标识符repo_id = "internlm/internlm2_5-7b"
# 指定要下载的文件列表files_to_download = [    {"filename": "config.json"},    {"filename": "model.safetensors.index.json"}]
# 创建一个目录来存放下载的文件local_dir = f"{repo_id.split('/')[1]}"os.makedirs(local_dir, exist_ok=True)
# 遍历文件列表并下载每个文件for file_info in files_to_download:    file_path = hf_hub_download(        repo_id=repo_id,        filename=file_info["filename"],        local_dir=local_dir    )    print(f"{file_info['filename']} file downloaded to: {file_path}")
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWPSKwPkbW3knibsYvAPtPNaOxMTZQhdEjRJlYA848EEqkjSnUBQIZCztUCviajbfsTv6O6xDjMXm9XA/640?wx_fmt=png)

要下载完整模型并打印示例输出

```
touch hf_download_1_8_demo.py
```

写入内容：

```
import torchfrom transformers import AutoTokenizer, AutoModelForCausalLMtokenizer = AutoTokenizer.from_pretrained("internlm/internlm2_5-1_8b", trust_remote_code=True)model = AutoModelForCausalLM.from_pretrained("internlm/internlm2_5-1_8b", torch_dtype=torch.float16, trust_remote_code=True)model = model.eval()inputs = tokenizer(["A beautiful flower"], return_tensors="pt")gen_kwargs = {"max_length": 128,"top_p": 0.8,"temperature": 0.8,"do_sample": True,"repetition_penalty": 1.0}#以下内容可选，如果解除注释等待一段时间后可以看到模型输出#output = model.generate(**inputs, **gen_kwargs)#output = tokenizer.decode(output[0].tolist(), skip_special_tokens=True)#print(output)
```

网速问题，似乎我这里一直搞不定，后面就用书生提供的工作机就好了，上面已经有模型了

4.模型上传

通过CLI上传 Hugging Face同样是跟Git相关联，通常大模型的模型文件都比较大，先安装git lfs，以对大文件系统进行支持。

```
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash# sudo apt-get install git-lfs # CodeSpace里面可能会有aptkey冲突且没有足够权限git lfs install # 直接在git环境下配置git LFSpip install huggingface_hub
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWPSKwPkbW3knibsYvAPtPNaOxHcKDn0ic9JdUmdXSAXx77ibPv9MzlopeWMW0DEmW9960ibIj1My2SSxQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWPSKwPkbW3knibsYvAPtPNaOXtR98wLT8Mvu16gMMib0O5aCkic7vGlTJVQ1GFFw5dK5W7PMounJbWQA/640?wx_fmt=png)

创建项目：

```
cd /workspaces/codespaces-jupyter#intern_study_L0_4就是model_namehuggingface-cli repo create intern_study_L0_4git clone https://huggingface.co/{your_github_name}/intern_study_L0_4
```

可以把训练好的模型保存进里面，这里我们只上传刚下载好的config.json，把它复制粘贴进这个文件夹里面，再加一个README.md文件，内容可以是：

```
# 书生浦语大模型实战营camp4- hugging face模型上传测试- 更多内容请访问 https://github.com/InternLM/Tutorial/tree/camp4
```

然后把config.json和README.md文件都push上去

```
cd intern_study_L0_4git add .git commit -m "add:intern_study_L0_4"git push
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWPSKwPkbW3knibsYvAPtPNaOfPvBmic4xMXHibZk8t4Cib7MIibTaibQtricHMTGQE1n46TLvKibibNHZ7ohhw/640?wx_fmt=png)

好了，终于可以了，L0入门岛可以通关了吧，迈向L1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWPSKwPkbW3knibsYvAPtPNaOYNUiaZv1mcjmvNnUdgribticRl5mgrAgIaGhWxtH83UwkaD8Cib4klueQg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgicgLxianEOvyNGt5BRoL3cBiaALV4vk3XyK7H1I9zauQfBdf31DPHp3CA/640?wx_fmt=png)

扫二维码一起学吧

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Z4jKmMQicbWP0nM8PnhZtqI4yFWpIJ8KdgxKg1XsbSjljI4kic5C0oAfDRiaXCJmmsl66ro1fY3eDJVUAcoib2PRDg/0?wx_fmt=png)

网安杂谈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Z4jKmMQicbWP0nM8PnhZtqI4yFWpIJ8KdgxKg1XsbSjljI4kic5C0oAfDRiaXCJmmsl66ro1fY3eDJVUAcoib2PRDg/0?wx_fmt=png)

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