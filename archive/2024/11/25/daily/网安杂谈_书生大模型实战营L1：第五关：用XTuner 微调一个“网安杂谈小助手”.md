---
title: 书生大模型实战营L1：第五关：用XTuner 微调一个“网安杂谈小助手”
url: https://mp.weixin.qq.com/s?__biz=MzAwMTMzMDUwNg==&mid=2650889396&idx=1&sn=9e3248a93a422f97b8a52a184fdc43d7&chksm=812ea091b659298796269631d995eb98611d3d486e02068669d373362b2f56b790cee16f489b&scene=58&subscene=0#rd
source: 网安杂谈
date: 2024-11-25
fetch_date: 2025-10-06T19:15:17.414807
---

# 书生大模型实战营L1：第五关：用XTuner 微调一个“网安杂谈小助手”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHYAEeamUmIuRqV5advTScIzjLoLNSyJC6THQ7xtBJK22WViaX4R8LlDA/0?wx_fmt=jpeg)

# 书生大模型实战营L1：第五关：用XTuner 微调一个“网安杂谈小助手”

网安杂谈

网安杂谈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHw64PTib75yYmdIm63M0wGmsvCUibUktTXT8TpSU6YQYTgtlB0YQ5wWNw/640?wx_fmt=png)

原始InternLM/Tutorial: LLM&VLM Tutorial  教程在这里

这次课的目标是：

针对业务场景（如特殊自我认知的机器人）的微调能力；打造一个属于自己的语言聊天机器人。

微调的步骤：1.SFT 数据（用于监督微调（Supervised Fine-Tuning）的数据集）的获取；2.使用 InternLM2.5-7B-Chat 模型微调

**1.环境配置与数据准备**

**1.1创建虚拟环境**

先SSH连接开发机https://studio.intern-ai.org.cn/

```
cd ~#git clone 本repogit clone https://github.com/InternLM/Tutorial.git -b camp4mkdir -p /root/finetune && cd /root/finetune   conda create -n xtuner-env python=3.10 -yconda activate xtuner-env
```

**1.2.安装Xtuner**

```
git clone https://github.com/InternLM/xtuner.gitcd /root/finetune/xtunerpip install  -e '.[all]'pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu121pip install transformers==4.39.0
```

-e 表示在可编辑模式下安装项目，因此对代码所做的任何本地修改都会生效

**1.3.创建文件夹用于存储微调数据**

```
mkdir -p /root/finetune/data && cd /root/finetune/datacp -r /root/Tutorial/data/assistant_Tuner.jsonl  /root/finetune/data
```

**1.4. 创建修改数据的脚本**

创建 change\_script.py 文件

```
touch /root/finetune/data/change_script.py
```

打开该change\_script.py文件后将下面的内容复制进去

```
import jsonimport argparsefrom tqdm import tqdmdef process_line(line, old_text, new_text):    # 解析 JSON 行    data = json.loads(line)        # 递归函数来处理嵌套的字典和列表    def replace_text(obj):        if isinstance(obj, dict):            return {k: replace_text(v) for k, v in obj.items()}        elif isinstance(obj, list):            return [replace_text(item) for item in obj]        elif isinstance(obj, str):            return obj.replace(old_text, new_text)        else:             return obj        # 处理整个 JSON 对象    processed_data = replace_text(data)        # 将处理后的对象转回 JSON 字符串    return json.dumps(processed_data, ensure_ascii=False)def main(input_file, output_file, old_text, new_text):    with open(input_file, 'r', encoding='utf-8') as infile, \         open(output_file, 'w', encoding='utf-8') as outfile:                # 计算总行数用于进度条        total_lines = sum(1 for _ in infile)        infile.seek(0)  # 重置文件指针到开头                # 使用 tqdm 创建进度条        for line in tqdm(infile, total=total_lines, desc="Processing"):               processed_line = process_line(line.strip(), old_text, new_text)            outfile.write(processed_line + '\n')if __name__ == "__main__":    parser = argparse.ArgumentParser(description="Replace text in a JSONL file.")    parser.add_argument("input_file", help="Input JSONL file to process")    parser.add_argument("output_file", help="Output file for processed JSONL")    parser.add_argument("--old_text", default="尖米", help="Text to be replaced")    parser.add_argument("--new_text", default="闻星", help="Text to replace with")    args = parser.parse_args()    main(args.input_file, args.output_file, args.old_text, args.new_text)
```

然后修改修改 --new\_text 中 default="闻星" 为你自己想起的名字。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHRH8ZBLibFRfHjL4jq31x4gjSYHhCKvyknPG3GuxmB7rr0UNrSmB7r5w/640?wx_fmt=png)

**1.5. 执行脚本**

```
#usage：python change_script.py {input_file.jsonl} {output_file.jsonl}cd ~/finetune/datapython change_script.py ./assistant_Tuner.jsonl ./assistant_Tuner_change.jsonl
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHG34WuF70wOpl2icibzAWSs3L3Zw2ENo9ToLTSasCZadKzVXX1zMLOTBg/640?wx_fmt=png)

**1.6.查看数据**

```
cat assistant_Tuner_change.jsonl | head -n 3
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHdYicPaKyib1hXdOIgrhqe3Nibe7RsXJFXEYNeoGjGKibdgoA2ycRox83Tw/640?wx_fmt=png)

现在看到数据已经改成自己想起的名字了

**2.训练启动**

**2.1 复制模型**

在InternStudio开发机中的已经提供了微调模型，可以直接软链接即可。

本模型位于/root/share/new\_models/Shanghai\_AI\_Laboratory/internlm2\_5-7b-chat

```
mkdir /root/finetune/models           ln -s /root/share/new_models/Shanghai_AI_Laboratory/internlm2_5-7b-chat /root/finetune/models/internlm2_5-7b-chat
```

**2.2修改 Config**

获取官方写好的 config文件

```
# cd {path/to/finetune}cd /root/finetunemkdir ./configcd configxtuner copy-cfg internlm2_5_chat_7b_qlora_alpaca_e3 ./
```

修改内容

```
########################################################################                          PART 1  Settings                           ########################################################################- pretrained_model_name_or_path = 'internlm/internlm2_5-7b-chat'+ pretrained_model_name_or_path = '/root/finetune/models/internlm2_5-7b-chat'
- alpaca_en_path = 'tatsu-lab/alpaca'+ alpaca_en_path = '/root/finetune/data/assistant_Tuner_change.jsonl'

evaluation_inputs = [-    '请给我介绍五个上海的景点', 'Please tell me five scenic spots in Shanghai'+    '请介绍一下你自己', 'Please introduce yourself']
########################################################################                      PART 3  Dataset & Dataloader                   ########################################################################alpaca_en = dict(    type=process_hf_dataset,-   dataset=dict(type=load_dataset, path=alpaca_en_path),+   dataset=dict(type=load_dataset, path='json', data_files=dict(train=alpaca_en_path)),    tokenizer=tokenizer,    max_length=max_length,-   dataset_map_fn=alpaca_map_fn,+   dataset_map_fn=None,    template_map_fn=dict(        type=template_map_fn_factory, template=prompt_template),    remove_unused_columns=True,    shuffle_before_pack=True,    pack_to_max_length=pack_to_max_length,    use_varlen_attn=use_varlen_attn)
```

除此之外，还可以对一些重要的参数进行调整，包括学习率（lr）、训练的轮数（max\_epochs）等等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHvXl5F49DyTOicJjaZGm3jj2XJCbna6xG9WKPZbDX0vpH96ddqyoJTDw/640?wx_fmt=png)

如果想充分利用显卡资源，可以将 max\_length 和 batch\_size 这两个参数调大。⚠但需要注意的是，在训练 chat 模型时调节参数 batch\_size 有可能会影响对话模型的效果。

已经将改好的 config 文件还可以从 /Tutorial/configs/internlm2\_5\_chat\_7b\_qlora\_alpaca\_e3\_copy.py 找到直接拿来用。

**2.3启动微调**

准备好了所有内容，我们只需要将使用 xtuner train 命令令即可开始训练。

xtuner train 命令用于启动模型微调进程。该命令需要一个参数：CONFIG 用于指定微调配置文件。这里我们使用修改好的配置文件 internlm2\_5\_chat\_7b\_qlora\_alpaca\_e3\_copy.py。训练过程中产生的所有文件，包括日志、配置文件、检查点文件、微调后的模型等，默认保存在 work\_dirs 目录下，我们也可以通过添加 --work-dir 指定特定的文件保存位置。--deepspeed 则为使用 deepspeed， deepspeed 可以节约显存。

运行命令进行微调

```
cd /root/finetune   conda activate xtuner-envxtuner train ./config/internlm2_5_chat_7b_qlora_alpaca_e3_copy.py --deepspeed deepspeed_zero2 --work-dir ./work_dirs/assistTuner
```

训了半天终于训完了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHJia6x1joviaiaUaV6NEz2ObibmqPO0iblicnM8icQ5H7jrAwm7GPcMibtmoDxg/640?wx_fmt=png)

**2.4权重转换**

模型转换的本质其实就是将原本使用 Pytorch 训练出来的模型权重文件转换为目前通用的 HuggingFace 格式文件，那么我们可以通过以下命令来实现一键转换。

可以使用 xtuner convert pth\_to\_hf 命令来进行模型格式转换。

xtuner convert pth\_to\_hf 命令用于进行模型格式转换。该命令需要三个参数：CONFIG 表示微调的配置文件， PATH\_TO\_PTH\_MODEL 表示微调的模型权重文件路径，即要转换的模型权重， SAVE\_PATH\_TO\_HF\_MODEL 表示转换后的 HuggingFace 格式文件的保存路径。

还可以在转换的命令中添加几个额外的参数，包括：

|  |  |
| --- | --- |
| 参数名 | 解释 |
| --fp32 | 代表以fp32的精度开启，假如不输入则默认为fp16 |
| --max-shard-size {GB} | 代表每个权重文件最大的大小（默认为2GB） |

```
cd /root/finetune/work_dirs/assistTuner     conda activate xtuner-env    # 先获取最后保存的一个pth文件pth_file=`ls -t /root/finetune/work_dirs/assistTuner/*.pth | head -n 1 | sed 's/:$//'`export MKL_SERVICE_FORCE_INTEL=1export MKL_THREADING_LAYER=GNUxtuner convert pth_to_hf ./internlm2_5_chat_7b_qlora_alpaca_e3_copy.py ${pth_file} ./hf
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHx4mmlaZDAYC8eiaEdW7G0dVSCLN1NZjKKXdYQ9sXrOqnSOaTpViaAxHQ/640?wx_fmt=png)

转完了，默认就是float16精度了，就转换完后的目录结构是这样的，模型被转换为 HuggingFace 中常用的 .bin 格式文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHZ4B6pqMp4AffCC8O1L1Nic5FEdHkVziaoq8Zk2uZpxA79mwzicY2zCSVw/640?wx_fmt=png)

hf 文件夹即为我们平时所理解的所谓 “LoRA 模型文件”

可以简单理解：LoRA 模型文件 = Adapter

**2.5  模型合并**

对于 LoRA 或者 QLoRA ...