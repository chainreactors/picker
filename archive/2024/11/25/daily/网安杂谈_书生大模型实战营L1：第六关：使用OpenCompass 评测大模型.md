---
title: 书生大模型实战营L1：第六关：使用OpenCompass 评测大模型
url: https://mp.weixin.qq.com/s?__biz=MzAwMTMzMDUwNg==&mid=2650889396&idx=2&sn=7447e227cc79726dcce6e5eeb6cf5913&chksm=812ea091b6592987083ef41258e2743fa89da88bc8497a1578178e1b9a9e1a04c04b4273391b&scene=58&subscene=0#rd
source: 网安杂谈
date: 2024-11-25
fetch_date: 2025-10-06T19:15:20.255553
---

# 书生大模型实战营L1：第六关：使用OpenCompass 评测大模型

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHOMuLWWAicSeRqLM9SO1Wb87H6rPzUSCmf180UjibhIXc5oqSbKd9pYVA/0?wx_fmt=jpeg)

# 书生大模型实战营L1：第六关：使用OpenCompass 评测大模型

网安杂谈

网安杂谈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHw64PTib75yYmdIm63M0wGmsvCUibUktTXT8TpSU6YQYTgtlB0YQ5wWNw/640?wx_fmt=png)

五花八门的大模型能力到底有多强？有没有客观评价的标准？本节课的目标是进行大语言模型的评测。使用的评测工具是OpenCompass。

OpenCompass是上海人工智能实验室研发的开源、高效、全面的大模型评测体系及开放平台，它 提供了 API 模式评测和本地直接评测两种方式。其中 API 模式评测针对那些以 API 服务形式部署的模型，而本地直接评测则面向那些可以获取到模型权重文件的情况。

**1.环境配置**

在训练营提供的开发机https://studio.intern-ai.org.cn/上创建用于评测 conda 环境:

```
conda create -n opencompass python=3.10conda activate opencompasscd /rootgit clone -b 0.3.3 https://github.com/open-compass/opencompasscd opencompasspip install -e .pip install -r requirements.txtpip install huggingface_hub==0.25.2
```

更多使用方法参考 OpenCompass 官方文档

**2.评测 API 模型**

评测通过 API 访问的大语言模型，整个过程其实很简单。首先你需要获取模型的 API 密钥（API Key）和接口地址。以 OpenAI 的 GPT 模型为例，只需要在 OpenAI 官网申请一个 API Key，然后在评测配置文件中设置好这个密钥和相应的模型参数就可以开始评测了。评测过程中，评测框架会自动向模型服务发送测试用例，获取模型的回复并进行打分分析。整个过程不需要准备任何模型文件，也不用担心本地计算资源是否足够，只要确保网络连接正常即可。这里以评测 internlm 模型为例，介绍如何评测 API 模型。

**2.1获取API**

首先打开网站浦语官方地址 https://internlm.intern-ai.org.cn/api/document 获得 api key 和 api 服务地址 (也可以从第三方平台 硅基流动 获取), 在终端中运行:

```
export INTERNLM_API_KEY=xxxxxxxxxxxxxxxxxxxxxxx # 填入你申请的 API Key
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHxiamicX3icZ5ic9niclyFDTXj18h6wUmvLacnywwkpuOP15bgIbfAyr9wicg/640?wx_fmt=png)

**2.2配置模型**

在终端中运行 cd /root/opencompass/ 和 touch opencompass/configs/models/openai/puyu\_api.py, 然后打开文件, 贴入以下代码:

```
import osfrom opencompass.models import OpenAISDKinternlm_url = 'https://internlm-chat.intern-ai.org.cn/puyu/api/v1/' # 你前面获得的 api 服务地址internlm_api_key = os.getenv('INTERNLM_API_KEY')models = [    dict(        # abbr='internlm2.5-latest',        type=OpenAISDK,        path='internlm2.5-latest', # 请求服务时的 model name        # 换成自己申请的APIkey        key=internlm_api_key, # API key        openai_api_base=internlm_url, # 服务地址        rpm_verbose=True, # 是否打印请求速率        query_per_second=0.16, # 服务请求速率        max_out_len=1024, # 最大输出长度        max_seq_len=4096, # 最大输入长度        temperature=0.01, # 生成温度        batch_size=1, # 批处理大小        retry=3, # 重试次数    )]
```

**2.3配置数据集**

在终端中运行 cd /root/opencompass/ 和 touch opencompass/configs/datasets/demo/demo\_cmmlu\_chat\_gen.py, 然后打开文件, 贴入以下代码:

```
rom mmengine import read_base
with read_base():    from ..cmmlu.cmmlu_gen_c13365 import cmmlu_datasets
# 每个数据集只取前2个样本进行评测for d in cmmlu_datasets:    d['abbr'] = 'demo_' + d['abbr']    d['reader_cfg']['test_range'] = '[0:1]' # 这里每个数据集只取1个样本, 方便快速评测.
```

这样就使用了 CMMLU Benchmark 的每个子数据集的 1 个样本进行评测.

**2.4进行测评**

完成配置后, 在终端中运行: python run.py --models puyu\_api.py --datasets demo\_cmmlu\_chat\_gen.py --debug.

这里直接运行会报错，缺一些库。特别是rouge,这里有个坑，直接pip install rouge还是不行。看群里大佬说，这里要先pip uninstall rouge,然后用conda install -c conda-forge rouge 安装，或者pip install rouge=1.0.1。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHDqcWYLIbic0e9M2l1EKHpbMSQN4Nm6pXqibyMdJSibNUvwSiahHk5sNwnA/640?wx_fmt=png)

预计运行10来分钟后, 得到结果，同时也生成了评估结果文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHHFBbWlRO3iaHBlk92ISlUF3z2n9HibGNLQZicg9sqYTCBj3SH0UBBrbGA/640?wx_fmt=png)

**3.评测本地模型**

评测本地部署的大语言模型前期准备工作相对繁琐，需要考虑硬件资源，但好处是评测过程完全在本地完成，不依赖网络状态，而且可以更灵活地调整模型参数，深入了解模型的性能表现。这种方式特别适合需要深入研究模型性能或进行模型改进的研发人员。主要步骤：

（1）获取完整的模型权重文件。比如从 Hugging Face 等平台下载模型文件。

（2）准备足够的计算资源，比如至少一张显存够大的 GPU，因为模型文件通常都比较大。

（3）在评测配置文件中指定模型路径和相关参数。

以InternLM2-Chat-1.8B 在 C-Eval 数据集上的性能为例测评。

**3.1环境配置**

```
cd /root/opencompassconda activate opencompassconda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia -yapt-get updateapt-get install cmakepip install protobuf==4.25.3pip install huggingface-hub==0.23.2
```

3.2下载数据集

```
cp /share/temp/datasets/OpenCompassData-core-20231110.zip /root/opencompass/unzip OpenCompassData-core-20231110.zip
```

data文件夹下就出现了很多数据集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHEpQhibzSNMj3WzAPzrVibQa2M53xia5ribLFL7VmaMQ2NkxTION5XyWBhA/640?wx_fmt=png)

**3.3加载本地模型进行评测**

在 OpenCompass 中，模型和数据集的配置文件都存放在 configs 文件夹下。可以通过运行 list\_configs 命令列出所有跟 InternLM 及 C-Eval 相关的配置。

python tools/list\_configs.py internlm ceval

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEH6S4GkOIpYjEO3YqYV1yV0GshiciaanSXOfrw1JN0Ut2IDBO0Odnf0lCA/640?wx_fmt=png)

打开 opencompass 文件夹下 configs/models/hf\_internlm/的 hf\_internlm2\_5\_1\_8b\_chat.py 文件, 修改如下:

```
from opencompass.models import HuggingFacewithChatTemplate
models = [    dict(        type=HuggingFacewithChatTemplate,        abbr='internlm2_5-1_8b-chat-hf',        path='/share/new_models/Shanghai_AI_Laboratory/internlm2_5-1_8b-chat/',        max_out_len=2048,        batch_size=8,        run_cfg=dict(num_gpus=1),    )]
# python run.py --datasets ceval_gen --models hf_internlm2_5_1_8b_chat --debug
```

可以通过以下命令评测 InternLM2-Chat-1.8B 模型在 C-Eval 数据集上的性能。由于 OpenCompass 默认并行启动评估过程，在第一次运行时以 --debug 模式启动评估，并检查是否存在问题。在 --debug 模式下，任务将按顺序执行，并实时打印输出

```
python run.py --datasets ceval_gen --models hf_internlm2_5_1_8b_chat --debug
```

如果出现 rouge 导入报错, 请 pip uninstall rouge 之后再次安装 pip install rouge==1.0.1 可解决问题.

这里就是环境配置的坑，numpy还要降级成1.25.2，torch的版本还有问题，跨过这些坑就可以跑起来了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEH6gqPq9yPkjlHxbc0hgJ8ugbPqL0ItIuoyibK3LyxNyuwAIYBYBbDXbg/640?wx_fmt=png)

也可以使用配置文件来指定数据集和模型

```
cd /root/opencompass/configs/touch eval_tutorial_demo.py
```

打开 eval\_tutorial\_demo.py 贴入以下代码

```
from mmengine.config import read_base
with read_base():    from .datasets.ceval.ceval_gen import ceval_datasets    from .models.hf_internlm.hf_internlm2_5_1_8b_chat import models as hf_internlm2_5_1_8b_chat_models
datasets = ceval_datasetsmodels = hf_internlm2_5_1_8b_chat_models
```

指定评测的模型和数据集，然后运行

```
python run.py configs/eval_tutorial_demo.py --debug
```

同样也是很快就出结果了，花了5分钟不到。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHGO5GrDmAxIeDOsPoTooxslmthJ02ByY3ia0LYV6NSRJlySGQlZBwIiag/640?wx_fmt=png)

**4.将本地模型通过部署成API服务再评测**

 OpenCompass还可以将本地模型部署成 API 服务, 然后通过评测 API 服务的方式来评测本地模型。

**4.1 安装和部署模型**

在开发机中打开一个终端进行安装部署

```
pip install lmdeploy==0.6.1 openai==1.52.0lmdeploy serve api_server /share/new_models/Shanghai_AI_Laboratory/internlm2_5-1_8b-chat/ --server-port 23333
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHCibogZq2bibuxPib1Fia2xRSNBU3cCWQkrRHAdupYLsBrlEMTOcvta7zbg/640?wx_fmt=png)

新开另一个终端, 使用以下 Python 代码获取由 LMDeploy 注册的模型名称：

```
from openai import OpenAIclient = OpenAI(api_key='sk-123456', # 可以设置成随意的字符串base_url="http://0.0.0.0:23333/v1")model_name = client.models.list().data[0].idprint(model_name) # 注册的模型名称需要被用于后续配置.
```

运行后能看到模型名称了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHPMia4XwTgQKn7lN7G4X1vaqfRlbYdnDdiaqTla76y58VGOxIsNYUw2jA/640?wx_fmt=png)

**4.2 创建配置脚本**

```
touch /root/opencompass/configs/models/hf_internlm/hf_internlm2_5_1_8b_chat_api.py
```

打开后填入

```
from opencompass.models import OpenAI           api_meta_template = dict(round=[    dict(role='HUMAN', api_role='HUMAN'),    dict(role='BOT', api_role='BOT', generate=True),])           models = [    dict(        abbr='InternLM-2.5-1.8B-Chat',        type=OpenAI,        path='/share/new_models/Shanghai_AI_Laboratory/internlm2_5-1_8b-chat/', # 注册的模型名称        key='sk-123456',        openai_api_base='http://0.0.0.0:23333/v1/chat/completions',         meta_template=api_meta_template,        query_per_second=1,        max_out_len=2048,        max_seq_len=4096,        batch_size=8),]
```

然后运行

```
opencompass --models hf_internlm2_5_1_8b_chat_api --datasets ceval_gen --debug
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWMk4qINLKv8dIMBB6ft4ibEHhbkqZ7nzQIMTSLGQO8QlvqwvPFibABnxZdyCv0vA6PXHibh5iaFic5KsUw/640?wx_fmt=png)

可算是开始了。。。同时另一个终端一直在接受请求数据了。...