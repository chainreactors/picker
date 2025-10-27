---
title: MinerU 介绍
url: https://mp.weixin.qq.com/s?__biz=MzI2NTExNzcxNQ==&mid=2247484288&idx=1&sn=a11342590cf0edb24985d65fc3de366a&chksm=eaa30afcddd483ea0776320392e03bb8d86c8e28d8aa55afa6c57564f65bf492f5a0f73f2fca&scene=58&subscene=0#rd
source: 代码审计SDL
date: 2024-08-06
fetch_date: 2025-10-06T18:05:23.069303
---

# MinerU 介绍

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/a4tp2b7vTo4zZ69eD8pw2rxrnGFCKVN9WJ7a7l5WfymHQso6EYzicSuJtwLK5c1bwPROXfJKOqVyReHRyqJibyYg/0?wx_fmt=jpeg)

# MinerU 介绍

原创

sanduo

代码审计SDL

#

## 背景

处理监管文档会遇到一个比较操蛋的问题就是部分文档只有pdf格式的，并且pdf是扫描版本的，无法直接读取pdf，利用多模态进行处理，目前口袋有比较紧张，最近发现一个宝藏项目，MinerU，子项目(PDF-Extract-Kit)，可以识别pdf，将pdf转成md，方便数据处理和LLM进行对话。

![](https://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo4zZ69eD8pw2rxrnGFCKVN9Viat9R11eez0b7U6Pl2gtqCLbibTelcCjwOOnNniazImibHUic7icg0yrucQ/640?wx_fmt=png&from=appmsg)

# 介绍

MinerU 是一款一站式、开源、高质量的数据提取工具，主要包含以下功能:

* Magic-PDF PDF文档提取
* Magic-Doc 网页与电子书提取

这里主要介绍Magic-PDF，Magic-PDF是一款将 PDF 转化为 markdown 格式的工具。支持转换本地文档或者位于支持S3协议对象存储上的文件。

主要功能包含

* 支持多种前端模型输入
* 删除页眉、页脚、脚注、页码等元素
* 符合人类阅读顺序的排版格式
* 保留原文档的结构和格式，包括标题、段落、列表等
* 提取图像和表格并在markdown中展示
* 将公式转换成latex
* 乱码PDF自动识别并转换
* 支持cpu和gpu环境
* 支持windows/linux/mac平台

# 安装

```
conda create -n mineru python=3.10conda activate mineru
```

**1.安装依赖**

完整功能包依赖detectron2，该库需要编译安装，如需自行编译，请参考 facebookresearch/detectron2#5114

或是直接使用作者预编译的whl包：

```
pip install detectron2 --extra-index-url https://wheels.myhloli.com -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**2.使用pip安装完整功能包**

```
pip install magic-pdf[full]==0.6.2b1 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**3.下载模型权重文件**

```
git clone https://www.modelscope.cn/wanderkid/PDF-Extract-Kit.git
```

**4. 拷贝配置文件并进行配置**

在仓库根目录可以获得 magic-pdf.template.json 配置模版文件

```
cp magic-pdf.template.json ~/magic-pdf.json
```

使用cuda

```
{    "bucket_info":{        "bucket-name-1":["ak", "sk", "endpoint"],        "bucket-name-2":["ak", "sk", "endpoint"]    },    "models-dir":"/data/models",    "device-mode":"cuda",    "table-config": {        "is_table_recog_enable": false,        "max_time": 400    }}
```

这里有个小坑，从huggingface下载下来的模型目录为：/data/models/PDF-Extract-Kit/，此处配置为：/data/models/PDF-Extract-Kit/models/ ，另外目前不支持多卡配置。

# 使用

**1. 通过命令行使用**

**直接使用**

```
magic-pdf pdf-command --pdf "pdf_path" --inside_model true
```

程序运行完成后，你可以在"/tmp/magic-pdf"目录下看到生成的markdown文件，markdown目录中可以找到对应的xxx\_model.json文件

如果您有意对后处理pipeline进行二次开发，可以使用命令

```
magic-pdf pdf-command --pdf "pdf_path" --model "model_json_path"
```

这样就不需要重跑模型数据，调试起来更方便

**更多用法**

```
magic-pdf --help
```

**2. 通过接口调用**

**本地使用**

```
image_writer = DiskReaderWriter(local_image_dir)image_dir = str(os.path.basename(local_image_dir))jso_useful_key = {"_pdf_type": "", "model_list": model_json}pipe = UNIPipe(pdf_bytes, jso_useful_key, image_writer)pipe.pipe_classify()pipe.pipe_parse()md_content = pipe.pipe_mk_markdown(image_dir, drop_mode="none")
```

**在对象存储上使用**

```
s3pdf_cli = S3ReaderWriter(pdf_ak, pdf_sk, pdf_endpoint)image_dir = "s3://img_bucket/"s3image_cli = S3ReaderWriter(img_ak, img_sk, img_endpoint, parent_path=image_dir)pdf_bytes = s3pdf_cli.read(s3_pdf_path, mode=s3pdf_cli.MODE_BIN)jso_useful_key = {"_pdf_type": "", "model_list": model_json}pipe = UNIPipe(pdf_bytes, jso_useful_key, s3image_cli)pipe.pipe_classify()pipe.pipe_parse()md_content = pipe.pipe_mk_markdown(image_dir, drop_mode="none")
```

本地命令执行效果如下：

```
magic-pdf pdf-command --pdf ../PDF-Extract-Kit/inputs/18.4《信息安全技术\ \ 安全漏洞标识与描述规范》GB_T\ 28458-2012.pdf --inside_model true
```

![](https://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo4zZ69eD8pw2rxrnGFCKVN90cFGyO5xhgQjSqzWZy6GvFpT6s3OLsQrKBGEJ2a8y3S1UQRKYlxy2g/640?wx_fmt=png&from=appmsg)

本地命令执行

成功

![](https://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo4zZ69eD8pw2rxrnGFCKVN9cObZk9icpKHIcHJkBcqV85X5G33MlWKpe1a44FvqREmlVSKC8bQNRQQ/640?wx_fmt=png&from=appmsg)

执行成功

效果对比

![](https://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo4zZ69eD8pw2rxrnGFCKVN92ucV0XZpqJ6U9BcaAuHyI192HLezwcSY7qUYb2IKSwA5EntwRw76VA/640?wx_fmt=png&from=appmsg)

效果对比

部分识别错误，但是整体已经很经验

![](https://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo4zZ69eD8pw2rxrnGFCKVN9w7ygresVhC6jhjgQNTRDGBOgJWoPmWphqABxLNwb6NJrobPbuhUo3Q/640?wx_fmt=png&from=appmsg)

部分瑕疵

GPU资源占用效率如下：

![](https://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo4zZ69eD8pw2rxrnGFCKVN9X0e4CUsaNGYNgv41e3GWwiaD5uhzGN1HeKq3ZworcQHXyAvvdos3kug/640?wx_fmt=png&from=appmsg)

GPU资源占用

# 结论

1、开源项目中，目前**MinerU可以满足pdf自动化识别需求，方便数据的整理和收集。**

2、由于ocr识别过程中仍会存在个别识别失误，格式混乱问题，如果项目数据要求比较准确，需要慎重考虑

3、**MinerU的命令行设计的有些反人类，这个属于个人观点**

# 错误

## ValueError: Unable to avoid copy while creating an array as requested.

![](https://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo4zZ69eD8pw2rxrnGFCKVN90Ijc3DZGVQnbgeEBszdPvGmvWNictAy1p7SZrnFW44yj245sichFPrJA/640?wx_fmt=png&from=appmsg)

错误

```
pip install "numpy<2"
```

## 参考

* https://github.com/opendatalab/MinerU
* https://github.com/opendatalab/PDF-Extract-Kit

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo5Zjccyeib7HeeeiaxwPjoVjaZklGM6lC9ku7HSkXQe72wGgA03a0mLZugZUpokLZbs8UVibq71Mx6OQ/0?wx_fmt=png)

代码审计SDL

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo5Zjccyeib7HeeeiaxwPjoVjaZklGM6lC9ku7HSkXQe72wGgA03a0mLZugZUpokLZbs8UVibq71Mx6OQ/0?wx_fmt=png)

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