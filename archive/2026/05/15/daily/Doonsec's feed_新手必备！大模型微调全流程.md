---
title: 新手必备！大模型微调全流程
url: https://mp.weixin.qq.com/s/nzXBkMa0KgH-ksnGS2_oOA
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:10:08.751474
---

# 新手必备！大模型微调全流程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0UKPAuBeu7m3uS0cKqhOficNBATsaa4iaZ5G8u3fEFXfZS0PIMX07cyuTa3GwPX7ZBBWFa2DGPfJwJVibsOeiaFN3tMXia5v0TN8icUDeHrxo4ql0/0?wx_fmt=jpeg)

# 新手必备！大模型微调全流程

原创

CSL
CSL

联想全球安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**点击蓝字**

**关注我们**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0UKPAuBeu7ng8BBiaakDKnQLMAMVBXYBc5ZH88dZt7PXCEWORvyUeDVkWh3UQ9zfVicGggRrFOXQBfBvRRIdR3PaqReWyRqnmR2gums9icYvVY/640?wx_fmt=jpeg)

段文桐

***前言***

由于在针对单片机和freertos类系统做逆向分析时，IDA中完全看不到任何符号，所以我想到了使用现有的qwen3-coder模型做微调以适应垂类任务。

本文章全部基于我自己上传的unsloth项目（https://github.com/pureGavin/unsloth4arm）制作，固如有不同架构，请另寻不同方法。

**01**

**准备工作**

本地需要安装docker，但是PGX上已经集成好了所有的环境，所以第一步应该是使用`apt`等命令更新所有可以更新的包，由于PGX机器的系统是NVIDIA定制的，所以源用的也是NVIDIA的软件源。

**02**

**代码部分**

完整的微调代码很长，我放到最后了，这里只讲重要的部分。

**01 基座模型选择**

![](https://mmbiz.qpic.cn/mmbiz_gif/RW2yrSCdCIxDv1DGoBqhMlyyBVdEHXFeLRjXvIv9KkQGqpPFzLouqBWeM6LxTqpibYnbrmqwJpeqrduxI7ymWiaA/640?wx_fmt=gif)

选择基座模型时，我选择的是 `unsloth/Qwen3-Coder-30B-A3B-Instruct`

```
# =========================# 1) 选择Qwen3 Coder基座模型#    说明：你可以改成你要微调的Qwen3 Coder具体型号#    常见：Qwen/Qwen3-Coder-7B / 14B / 32B 等（以HF实际存在为准）# =========================base_model = "unsloth/Qwen3-Coder-30B-A3B-Instruct"   # ← 按需修改output_dir = "./qwen3-coder-decompilebench-lora"
```

主要是因为在我做微调的时候，unsloth在huggingface上还没有上传qwen3其他的coder模型，我的目标是针对IDA的伪代码进行符号表的还原，这类任务基本来说就是对代码进行审计，所以使用coder模型的效果应当是最好的。

基座模型之间的区别简单来说：base < instruction < thinking

base模型只是做了预训练；

instruction在base的基础上做了指令对齐，学会了结构化输出；

thinking在instruction的基础上加入了思考模式，使得模型可以做更复杂的推理。

**02 数据选择**

![](https://mmbiz.qpic.cn/mmbiz_gif/RW2yrSCdCIxDv1DGoBqhMlyyBVdEHXFeLRjXvIv9KkQGqpPFzLouqBWeM6LxTqpibYnbrmqwJpeqrduxI7ymWiaA/640?wx_fmt=gif)

对于所有AI训练，数据都是最重要的，这里我只使用了一个开源的数据集并随机截取了其中15k条数据。

```
# =========================# 4) 加载数据集：LLM4Binary/decompile-bench#    说明：该数据集的字段名可能会随版本变化#    这里先拉取并查看列名，然后做自适配映射# =========================ds = load_dataset("LLM4Binary/decompile-bench")print(ds)print("Train columns:", ds["train"].column_names if "train" in ds else None)# 有些数据集只有一个split，比如 "test" 或 "validation"# 你可以按实际情况选择splitsplit_name = "train" if "train" in ds else list(ds.keys())[0]raw_train = ds[split_name]# =========================# 4.1) 关键优化：先抽样/截取到 10k~15k，再做 map/filter#      避免对全量大数据做 format_sft/tokenize/filter，节省时间和CPU# =========================TARGET_N = 15000  # 你希望保留的样本数量（建议 10000~15000 之间）SHUFFLE = True    # True：先打乱再取子集（更推荐，样本分布更随机）SEED = 42         # shuffle 随机种子，保证可复现n_total = len(raw_train)n_take = min(TARGET_N, n_total)if SHUFFLE:    # 先洗牌再取前 n_take 条    # 优点：相比直接取前N条更不容易出现“数据按来源/难度排序导致的偏差”    raw_train_small = raw_train.shuffle(seed=SEED).select(range(n_take))else:    # 直接取前 n_take 条（速度最快，但可能存在顺序偏差）    raw_train_small = raw_train.select(range(n_take))print(f"Subset samples: {len(raw_train_small)}/{n_total}")
```

由于我们使用Lora做微调，所以数据不用太多，10k~15k就很完美，具体多少可以在训练时参考loss下降的速度。

**03 训练参数**

![](https://mmbiz.qpic.cn/mmbiz_gif/RW2yrSCdCIxDv1DGoBqhMlyyBVdEHXFeLRjXvIv9KkQGqpPFzLouqBWeM6LxTqpibYnbrmqwJpeqrduxI7ymWiaA/640?wx_fmt=gif)

```
# =========================# 7) 训练参数#    说明：GB10显存/统一内存很大，但仍建议从保守配置开始# =========================training_args = TrainingArguments(    output_dir=output_dir,    per_device_train_batch_size=8,    gradient_accumulation_steps=4,  # 等效batch=8    learning_rate=2e-4,    warmup_ratio=0.03,    num_train_epochs=1,             # 先跑通流程；再加大到 2-3    lr_scheduler_type="cosine",    logging_steps=10,    save_steps=200,    save_total_limit=2,    bf16=torch.cuda.is_available() and torch.cuda.is_bf16_supported(),    fp16=torch.cuda.is_available() and (not torch.cuda.is_bf16_supported()),    optim="paged_adamw_8bit",       # bitsandbytes 8bit优化器，省显存    weight_decay=0.0,    report_to="none",    dataloader_num_workers=16,      # 按CPU核心数调大，例如 8/16/32    dataloader_pin_memory=True,     # GPU拷贝（通常有帮助）)
```

这里有几个参数非常重要：

`per_device_train_batch_size=8`  这个参数代表了每次训练时喂进去的数据量，由于使用的PGX有128G统一内存，所以这里可以设置高一些。

`gradient_accumulation_steps=4`  这个参数代表了梯度下降的速度，这里设置的效果会在后续训练时通过loss观察到，建议4或者8。

`learning_rate=2e-4` 这个参数代表学习率，步长小会导致训练速度变慢，步长大会导致收敛结果不稳定。

`dataloader_num_workers=16` 这个参数是用来读取工作进程数的，由于之前我把 `per_device_train_batch_size`  参数设置成了1，所以导致学习非常慢，且GPU跑不满（但是CPU占用很高），总之这里的值是根据你本机的CPU核数来的，一般是2的倍数。

`max_seq_length = 8192` 这个参数是写在了加载模型的位置，这个参数代表了训练时的上下文长度，由于我们的数据是汇编和C对应的代码，可能会很长，所以这里上下文长度可以给大一点；这里的上下文长度不会影响最终模型的可用上下文长度。

**04 训练时**

![](https://mmbiz.qpic.cn/mmbiz_gif/RW2yrSCdCIxDv1DGoBqhMlyyBVdEHXFeLRjXvIv9KkQGqpPFzLouqBWeM6LxTqpibYnbrmqwJpeqrduxI7ymWiaA/640?wx_fmt=gif)

训练的代码非常简单，这里就不贴了。

需要注意的是一般对于微调任务来说，时间不会超过三天，事实上一天半到两天就是一个正常范围，如果运行了一晚上，发现可预见的训练时长会超过三天，那么应当停止训练并检查上面提到的：数据是否过多；`per_device_train_batch_size`  参数是否过低；以及检查docker是否挂载了GPU。

**05 训练后产生GGUF文件**

![](https://mmbiz.qpic.cn/mmbiz_gif/RW2yrSCdCIxDv1DGoBqhMlyyBVdEHXFeLRjXvIv9KkQGqpPFzLouqBWeM6LxTqpibYnbrmqwJpeqrduxI7ymWiaA/640?wx_fmt=gif)

训练完成后我们会在指定的output文件夹下看到一个safetensors文件，如果想要使用Ollama来启动微调完成后的大模型，这个还不能用，需要使用  `llama.cpp`（https://github.com/ggml-org/llama.cpp）工具做转换才行，整体的流程是先将safetensors文件转换成merge\_hf文件，此时微调的增量参数会和基座模型合并成一个完整的模型，然后使用 `llama.cpp` 提供的`convert_hf_to_gguf.py` 脚本将merge文件转成gguf文件，在转成gguf文件之前需要指定一个模型的量化类型，根据测试，就算我使用bf16，最终的对话返回也很快。

**03**

**Ollama如何调用**

Ollama是没办法直接调用gguf文件的，主要是Ollama需要一个调用规定，写明如何与指定的大模型进行对话，这个规定文件称为 `modelfile` ，由于Ollama官方对于这个`modelfile` 的教程很少，所以我们可以参考一下官网提供的模型的 `modelfile` 是怎么写的，我们的基座模型用的是 `Qwen3-Coder-30B-A3B-Instruct` ，那么我们就可以下载一个官方的qwen3-coder模型，然后使用 `ollama show --modelfile` 命令进行查看。

```
# Modelfile generated by "ollama show"# To build a new Modelfile based on this, replace FROM with:# FROM qwen3-coder:30b-a3b-fp16FROM /root/.ollama/models/blobs/sha256-2f3c93d7adf85fcfeb6620d80058b22c51d5a8b21ce18f1c58bd3004c0a63f45TEMPLATE {{ .Prompt }}RENDERER qwen3-coderPARSER qwen3-coderPARAMETER top_k 20PARAMETER top_p 0.8PARAMETER repeat_penalty 1.05PARAMETER stop <|im_start|>PARAMETER stop <|im_end|>PARAMETER stop <|endoftext|>PARAMETER temperature 0.7LICENSE """                                 Apache License                           Version 2.0, January 2004                        http://www.apache.org/licenses/   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
```

这里我只节选了最重要的一部分（后面全都是证书内容），这里需要着重解释一下对话模板。

**对话模板**

![](https://mmbiz.qpic.cn/mmbiz_gif/RW2yrSCdCIxDv1DGoBqhMlyyBVdEHXFeLRjXvIv9KkQGqpPFzLouqBWeM6LxTqpibYnbrmqwJpeqrduxI7ymWiaA/640?wx_fmt=gif)

对话模板（chat template）是告诉Ollama应该如何调用和拼接对话的，如果不设置，虽然大模型也能启动，但是会完全无法使用。

```
TEMPLATE {{ .Prompt }}RENDERER qwen3-coderPARSER qwen3-coder
```

这三个参数是同一个作用，告诉Ollama对话模板使用源码中的模板：

```
PARAMETER stop <|im_start|>PARAMETER stop <|im_end|>PARAMETER stop <|endoftext|>
```

这三个参数称之为停止符，用来告诉Ollama当模型返回到什么内容时应当截断和停止。

我们可以假设我们给大模型发送一个“你好”，那么实际上发送给大模型的内容应该是这样的：

```
<|im_start|>system\nYou are Qwen, a helpful AI assistant that can interact with a computer to solve tasks.<|im_end|>\n<|im_start|>user\n你好<|im_end|>\n<|im_start|>assistant\n
```

而大模型的返回会接着assistant继续，由于qwen3的对话模板直接写死在了Ollama源码中（开源社区对这种行为也是深恶痛绝），所以我们并不能看到和修改对话模板中的内容。

修改对话模板本身就已经可以单独写一长篇文章（并且这也是一个单独的工种），这里我们只需要关注在对话模板中，这个大模型支持哪些功能，以及各个功能在使用过程中（如：mcp、function）需要注意的格式问题；事实上在微调后你发现模型并不符合你的预期，这并不一定是模型微调的不好或者数据不好，也有可能是对话模板的问题，这里我给出GPT-OSS系列模型的对话模板链接以供参考。（https://huggingface.co/openai/gpt-oss-120b/blob/main/chat\_template.jinja）

***写在最后***

上面的微调针对的是逆向还原符号表的任务，由于微调的时间跨度非常大，在我构思时coder类模型还没多少，等我完成微调并测试时，coder类模型就已经百花齐放了，个人用开源数据做的微调是无论如何也达不到专业团队用付费数据训练的大模型的效果的，所以我的微调不出意外的效果比新发布的大模型差，但是学习和踩坑过程还是很值得记录的。

在你对现有大模型在垂类任务效果不好，想要微调之前请思考如下内容：

1. 数据是否是永恒不变的，如果数据内容会改变，那么RAG更好。
2. 你的调用方式是否没有和对话模板对齐，这点非常重要！！！
3. 是否有其他类型的模型也能满足你的需求，不要在一个树上吊死。
4. 是否可以开发工具或修改对话模板来满足垂类任务的需求，能不动模型本体就别动。
5. 你的数据是否足够好？普通的数据是微调不出满足要求的模型的。

——end——

**往期精彩合集**

●[后端安全不是玄学：从编码到上线的8条安全底线](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493803&idx=1&sn=8b7f3f8f07fea587a8e158a0f8d67962&scene=21#wechat_redirect)

●[ADetailer插件安全问题分享](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493774&idx=1&sn=e273f3c29dff0c21175e15001347d8b7&scene=21#wechat_redirect)

●[Agent Skill: 一个文件夹，如何在90天内席卷AI圈](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==...