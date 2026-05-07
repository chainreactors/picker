---
title: 关键漏洞可致 30 万 Ollama 部署信息被盗
url: https://mp.weixin.qq.com/s/oQ3S6LWCYRhuolkShzKupg
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:29:07.271461
---

# 关键漏洞可致 30 万 Ollama 部署信息被盗

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZjmQKC9CkXdTic31b585EXlz1zg9glEbD5n0KqiamJFMk1VY4NgdVjNCQNK6Rs26iaFibF5KzpiaDia5eD0ODaxswY2Fn8XmjtfctYFE/0?wx_fmt=jpeg)

# 关键漏洞可致 30 万 Ollama 部署信息被盗

原创

骨哥说事
骨哥说事

骨哥说事

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

#

# **防走失：****https://gugesay.com/**

**不想错过任何消息？设置星标****↓ ↓ ↓**

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZjibnD0sDsRtvQFrknX86EaiaKuzQnNACpXCyHicaIUC24E2UmKBoydZVKw7ibd2WA6r8erHtkdM7pReQ6wYicaBQ8J9uC750IibXDZc/640?wx_fmt=png&from=appmsg)

研究团队发现一个Ollama的高危漏洞（CVE-2026–7482，CVSS 9.1），允许未经身份验证的攻击者泄露整个Ollama进程的内存，可能影响全球约 **30万台** 服务器。泄露的内存包含用户消息（提示词）、系统提示词和环境变量。

## **Ollama是什么？**

Ollama是一个开源平台，允许用户直接在本地机器上运行大语言模型，而无需依赖如 *OpenAI*、*Anthropic* 或 *xAI* 这样的云服务。通过Ollama，用户可以下载、管理以及交互地使用像 *Llama*、*Mistral* 等模型——所有操作都在本地硬件上运行。

Ollama在GitHub上目前拥有约17万个星标，在Docker Hub上的下载量超过1亿次，并在各企业中得到广泛采用，已成为本地运行开源模型的标准工具。

## **在Ollama中创建模型实例**

在Ollama中创建模型实例主要有两种方式。

第一种是使用 `/api/pull` API端点——这会从Ollama注册表中下载一个现有模型并在本地可用。用户得到一个现成的模型（如 `llama3` 或 `mistral`），可以立即用于推理。当不需要自定义时，这是最简单的方法。

第二种方式是使用 `/api/create` API端点——这允许用户通过指定系统提示词、量化级别等配置参数来构建自定义模型实例。基础模型可以来自两个来源：从远程注册表拉取（通过 `from` 参数），或者基于先前上传的模型文件构建。

在本研究中，我们将重点关注第二种选项——用户如何从先前上传的文件创建模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZiaeDX9x1lsicmo0rSic46OLo1YibJxIqHE90b0X6n6amc4JZibHF7tfUoFkKBPZC8CKA7qxpoCOUaVsWGrDE4qsY1L8Qby5mgOkuxk/640?wx_fmt=png&from=appmsg)

但首先——用户最初是如何上传文件的？

文件通过 `/api/blobs/sha256:[sha256-digest]` API端点上传到Ollama服务器。其中 `[sha256-digest]` 部分正如其名——是根据文件内容计算出的SHA-256哈希值。实际的文件内容在请求的HTTP主体中发送。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZg6rB05dJCMGf5637EeMb787GhXKicCicXQRKTprFZQId2AqOCLpcfxJU0rLovOLa0tVS7DiaU2RJoYqsgbszRZ7yDRtJCuOxd4xA/640?wx_fmt=png&from=appmsg)

之后，为了在Ollama中创建模型实例，用户以JSON请求体中的参数形式调用 `/api/create`，并包含已上传的文件。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZiaYhuogrPDqpGHLqmPfofFfmtA0Sykje5RpVcExCpUoRtvpb3cicmsEd5cu3jfELL7NYIOCJLLZfFJE44b14K71xicn35EsBtWHQ/640?wx_fmt=png&from=appmsg)

对 `/api/create` 的API请求的详细解析将在本文后续部分说明。

### **免责声明**

**‍***下一部分有点技术性。我们已尽可能简化，只包含理解该漏洞所必需的内容。请耐心阅读——我们保证漏洞部分值得一看。*

## **GGUF（GPT生成的统一格式）**

GGUF是一种文件格式，用于存储大语言模型，使其能高效地在本地加载和运行。

GGUF文件包含张量——本质上是表示模型学习到的参数（权重）的多维数字数组。可以将张量视为模型的“大脑”——它们存储了模型在训练期间学到的所有知识。

GGUF文件的头部包含描述它的数据，例如GGUF格式的版本、其包含的张量数量以及一些键值元数据。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZiaNvBr8Z3untENBnwkdDTaeIGrMicIQEsApgTXMiaypqYtXM2fYdCGyzQGJvxiaFTLAI6RmC4Rvjwu4vQKZbTmGIZicZ1c6lSibbj3k/640?wx_fmt=png&from=appmsg)

一个值得一提的元数据字段是 `general.file_type`——它告诉你（出人意料地）GGUF的文件类型，这决定了张量内部数字的存储方式。在这个研究中，我们只关心F16（16位浮点数）和F32（32位浮点数）。

GGUF头部之后是一个张量对象列表。每个张量对象存储了张量的名称、维度数量、数据类型（精度信息）以及一个指向文件中实际张量数据所在位置偏移量。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgRmibDmib7icrjTZKDnVmkNqlwI2fSHEMyDbxxSxbNwRFT8Mvn6Jiajib2bwMGWqz5yzyTF5cJfyOowRGhbUy4zuZ7ib8Sia7CpjYXrI/640?wx_fmt=png&from=appmsg)

## **量化**

量化是降低张量中存储数字精度的过程，使模型更小、运行更快——代价是牺牲一些准确性。

在GGUF中，F32文件类型使用4字节存储每个数字，而F16仅使用2字节。从F32切换到F16将使内存使用量减半（使模型运行更快），但会带来永久性数据丢失——一些小数精度丢失且无法恢复。相反，从F16切换到F32则不会造成任何数据丢失。

## **漏洞详情**

### **开始之前**

对于熟悉Go语言的读者来说，你们可能在想——在一种内存安全的语言中，怎么可能发生越界内存读取漏洞？通常，Go只会因恐慌而崩溃。

答案是 `unsafe` 包。Go为开发人员提供了一个用于低级内存操作的“逃生出口”，正如其名（unsafe意味着“不安全”），所有常规的安全保证都失效了。不出所料，Ollama使用 `unsafe` 的地方正是这个漏洞所在之处。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZgHcqo4QR9frJ8FxL7Fs70ywujQo51dz1IIiaOy4f7E105DPNaInWc95hjM00AcgTQXFia6SCGLszT6cVUj3UWHsbmovKspr84kk/640?wx_fmt=jpeg&from=appmsg)

### **再次谈谈创建模型**

正如本文开头提到的，在Ollama中有几种创建模型实例的方式。我们关注的是通过 `/api/create` 端点创建的这种方式。

处理此端点传入请求的函数是 `server.CreateHandler`。

其首要任务是基于已知结构解析传入请求。该结构包含许多属性，但与此漏洞相关的是模型名称 (`model`)、将用于构建模型的上传文件 (`files`)，以及我们稍后会解释的 `quantize` （量化）参数。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgyVMIvHwzXEoRvbfibd0CJhe5UvxzRJMoecp2mEw2qqeGw0ccbNStnUk57jibV7xcUeDibictnMtqQic0lqkgsQbibCKc81vUKYcAIk/640?wx_fmt=png&from=appmsg)

解析之后，该函数执行一些基本的健全性检查——验证模型名称是否有效，以及文件路径是否合法（无路径遍历尝试，且文件实际存在于磁盘上）。

接下来，如果模型创建使用的是文件（而不是，例如一个URL），该函数会调用 `convertModelFromFiles`。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgNicpibneV3tibeg14KrMyx31kQ1oesY8LYHHo2ukkX4DYyDfPrcPzeVmAPpneUxMwPSQ0rMNmtibkicvDps8xstXrdW1ZgJNYojfc/640?wx_fmt=png&from=appmsg)

### **从GGUF文件创建模型**

当人们调用 `/api/create` 从上传的文件创建模型时，Ollama首先需要弄清你给的是什么类型的文件——它通过检查文件扩展名（`.gguf`、`.safetensors`）来判断，或者如果没有扩展名，则通过检查前几个字节来判断。

对于GGUF文件格式，Ollama将原始GGUF文件解析为一个名为 **Layer** 的内部结构，该结构同时保存文件元数据和模型的张量。从此刻起，Ollama使用Layer而非原始文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZgHIjPR4qQMb5FFELBibHls8a1jAcnFZgic0G22bLsLhTe9lFKcUcvhxKKdzGLY5tjraAXmPfVibbvE0G5nuaISnFbDcE4dt3x8icE/640?wx_fmt=png&from=appmsg)

接着调用 `createModel` 来协调模型创建过程。在实际保存模型之前，Ollama检查是否需要量化。

*快速回顾：量化将张量数据从一种格式转换为另一种（例如F32到F16，反之亦然）。*

只有当三个条件都满足时量化才会运行：用户通过 `quantize` 参数明确请求了目标格式、文件是GGUF格式，并且当前格式与请求的不同。如果模型已经处于正确的格式，则什么也不做。

如果需要量化，过程如下：

首先，准备一个新的Layer，通过复制每个张量的元数据（例如形状和类型）来设置，但实际数据留空。可以将其视为为新张量设置空的存放位置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZgg2n76LXwPFDoGB1OxsaKevGYeMkEQTv4dPx35nkvuGJMYSV3iaTT7av9fic4LNuBfCYP6RuBCq0DicEiabD6zMHum6Hv6OFgHe0c/640?wx_fmt=png&from=appmsg)‍

然后，对于每个张量，调用 `WriteTo` 函数——该函数负责从源类型到目标类型的实际数学转换。

出于优化原因，它首先将源数据转换为F32，然后再从F32转换为目标格式。通过总是以F32作为中间步骤，每个格式只需要两个转换函数，而不需要每对可能格式之间的直接路径函数。

如果目标类型是F32，这个中间步骤只是直接复制数据（无需进行任何类型的转换）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZh37iaqlEMFOIsOicYW9XicC9PGPI2miaa4wXHIV5MwUvNLaSRkWrjyx7ibLDGEfv3gwjVzkxL1IaLnE9vVT0JTSwuzG7kPjlOR8R7I/640?wx_fmt=png&from=appmsg)

然后——`WriteTo` 函数将转换后的F32张量传递给 `ggml.Quantize`，由后者处理从F32到目标格式的最终转换。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZiaQEfAqTd1rfcdVPUaYf67uR0wmR1tE6XdyH4icn15dybuKbMNaUENjUVW43j6zbqsc4jgV9aXBxhpCAYJUTXibBuumYJaYLg1Ys/640?wx_fmt=png&from=appmsg)

一旦所有张量都转换完毕，会写入一个新的GGUF文件，包含更新后的头部和新量化的张量——模型就可以使用了。

### **终于，漏洞浮现**

让我们仔细看看 `WriteTo` 函数。

如前所述，`WriteTo` 首先将源数据转换为F32。如果源数据已经是F32，它只需从原始缓冲区复制张量数据；否则，它会调用 `ggml.ConvertToF32`。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgqlrVUz4caibr3yNhKGTQ67yoshm0FoBeDicsxic9bxibOpgICrrSFBWPSyibkRX3CWL5rTiaVuR6u32PW2pADyJIUKBqmSy0sXLv10/640?wx_fmt=png&from=appmsg)

可以看到——`ConvertToF32` 函数接收三个参数：原始数据缓冲区、源类型，以及 `q.from.Elements().`

那第三个参数值得暂停一下来思考。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZiasCQoo17Db1Iosxpm1NPUnLuQOYeoRpLZj50OaicMZZ2Dg81cnUpfiaDmIgYjic02fopEgP4xbicCLYBhlK0jrJhpvpZtjlNUf9cs/640?wx_fmt=png&from=appmsg)

`Elements()` 返回张量中元素的总数。记住——张量是多维的——它们的形状描述了维度。`Elements()` 只是将那些维度相乘。例如，形状为（3， 3， 3）的张量有27个元素。

现在，回到 `ConvertToF32` 函数。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZiavCuDyWXCGXCVQKSpzQMKtMFmBoSm3PJVN9hwFELBiaOhZiaojVkl5YKuCiaRaR7k6WvKicWgxV7mMHva0ojkUdS1LaVFemD3bibW4/640?wx_fmt=png&from=appmsg)

这些函数看起来很吓人，但 `ConvertToF32` 实际上相当简单——它只是根据源类型调用适当的转换函数。例如，如果源是F16，它会调用 `ggml_fp16_to_fp32_row` 并传入三个参数：指向原始数据的指针、一个将写入转换后数据的输出缓冲区，以及要读取的元素数量——这个数量来自 `Elements().`

然后，`ggml_fp16_to_fp32_row` 循环遍历缓冲区并精确读取该数量的元素，将每个元素转换为F32。

**那么问题出在哪里？**GGUF只是一个二进制格式——任何人都可以手动创建一个GGUF文件，并将张量的形状设置为他们想要的任何值。这里没有验证我们将要读取的元素数量是否与实际的数据大小相匹配。

因此，如果攻击者在形状字段中放置一个非常大的数字，循环将盲目地读取超出缓冲区末尾的数据——这就是我们的越界堆（heap）读取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZjW2BraFJicZh8fsn8qJCYu9EUshFueY8jRgkmIqNdhe5wDttpibNpmOvo1K9C5kELc0zNwT2xPYC8XO2Q6Nwia3I81NDxFY0bYAg/640?wx_fmt=png&from=appmsg)

此时，输出缓冲区包含的不仅仅是模型数据——还包括恰好在缓冲区之后堆内存中的任何内容。正如我们稍后将展示的，这可能包含一些相当敏感的信息：系统提示词和来自其他用户发送给其他模型的消息。

![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZiab7SnyJRfMDHMlNfpxHMcNQsRK8stIcISdYTJrgk24vjqt0ecy5xYiaOhbmAU9ENVYq3k8mHDAla4fNyJiciawhdmxxiaPrSZKAxY/640?wx_fmt=png&from=appmsg)

那么Ollama如何处理这个输出缓冲区呢？如前所述，将其从F32转换为目标格式，然后将整个内容（包括敏感数据）作为新的模型文件写入磁盘。

‍

### **泄露数据而不破坏数据**

从堆中读取的数据在经过多次转换后才被写入磁盘——这是个问题。大多数量化格式是有损的，意味着数据会被损坏，变得不可读。

为了保持数据完好无损，使用一个简单的技巧：将张量类型设置为F16，并请求将F32作为目标格式。F16到F32是无损转换（从2字节到4字节），因此堆数据在另一端出来时仍然是可读的。并且由于目标已经是F32，第二次转换根本不做任何事情。数据最终完整无损地被写入磁盘。

## **数据外泄**

那么，我们有一个包含泄露的堆数据的模型文件存放在服务器上——现在怎么办？如果无法将其取回，越界读取就毫无用处。那么如何将其带回来呢？

本文前面讨论了在Ollama中创建模型的不同方...