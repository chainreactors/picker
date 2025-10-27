---
title: 当风云卫拥抱DeepSeek发生了哪些（一）：DeepSeek-R1安全告警分析实测获三高
url: https://blog.nsfocus.net/deepseek1/
source: 绿盟科技技术博客
date: 2025-02-12
fetch_date: 2025-10-06T20:36:15.792960
---

# 当风云卫拥抱DeepSeek发生了哪些（一）：DeepSeek-R1安全告警分析实测获三高

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 当风云卫拥抱DeepSeek发生了哪些（一）：DeepSeek-R1安全告警分析实测获三高

### 当风云卫拥抱DeepSeek发生了哪些（一）：DeepSeek-R1安全告警分析实测获三高

[2025-02-11](https://blog.nsfocus.net/deepseek1/ "当风云卫拥抱DeepSeek发生了哪些（一）：DeepSeek-R1安全告警分析实测获三高")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 885

**摘要：**DeepSeek-R1在安全告警分析测试中，相较绿盟风云卫展现更高覆盖率，但高误报率和高性能开销是短板。尽管潜力巨大，实用性仍待优化。

****一、前言****

DeepSeek-R1作为由深度求索公司自主研发的国产通用人工智能大模型，自发布以来便备受瞩目。凭借在多项核心评测基准中的优异表现，DeepSeek-R1展现了强大的语言理解、逻辑推理和知识应用能力。

在安全运营领域，海量的告警信息给安全分析人员带来了巨大的挑战。本文将聚焦安全运营中的告警分析场景，基于DeepSeek-R1进行告警分析评测，以评估其实际应用价值。

****二、测试方法****

本测试在DeepSeek-R1原版完整模型上进行。

我们在现有告警数据上进行三轮抽样，每轮抽样75条真实攻击告警和25条非攻击（误报）告警，要求DeepSeek-R1对告警的真实性和攻击结果进行分析。每轮测试中使用的prompt亦略有差异，以考虑不同的安全运营场景。

原始告警数据来自多个现实网络环境的多种探针设备，并由人类专家进行了标注。提供给模型的告警信息经过基本的预处理，包括协议字段解析、常规解码和解压缩等，以便于模型进行分析。

****三、综合结果****

经与人工专家标注对比，DeepSeek-R1和风云卫在告警分析测试成绩统计如下：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 分类指标 | DeepSeek-R1最高单轮准确率 | DeepSeek-R1最低单轮准确率 | DeepSeek-R1整体准确率 | 风云卫整体准确率 |
| 告警是否指示真实攻击 | 90% | 82% | 86.33% | 98.33% |
| 告警是否指示真实且成功的攻击 | 82% | 68% | 76.33% | 91.67% |

表1：告警分析测试成绩统计

特别需要指出的是，三轮测试中合计225条真实攻击样本无一漏报。即使考虑到预处理过程降低了告警分析的难度，这依然是此前测试过的所有公开LLM都未曾达到过的水平。由此认为DeepSeek-R1对于真实攻击具有非常优秀的检出能力。

但反过来讲，目前测试中全部41个分类错误均是将非攻击行为误判为真实攻击。由此统计DeepSeek-R1对于非攻击告警的整体误报率高达54.67%。考虑到当前普遍存在的告警疲劳问题，这么高的误报率以实际安全运营场景来说是难以接受的。

通用领域LLM似乎普遍具有高估告警危害程度的倾向，这一点在此前对于包括OpenAI的GPT-4o在内的各个LLM进行测试时均有体现，并非DeepSeek-R1特有的问题。

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 标注来源 | 无危害 | 轻微危害 | 中等危害 | 严重危害 | 未判断\* | 合计 |
| 人工分类 | 82 | 326 | 87 | 69 | 13 | 577 |
| OpenAI接口分类 | 2 | 13 | 367 | 183 | 12 |

表2：对通用LLM“高估告警危害”问题的量化分析（与DeepSeek无关，仅供参考）

**\*注：表中“未判断”的部分，人工分类是由于信息不足等原因难以判断，机器分类是由于Token超长等原因出错所致。**

不过，这个问题按理说并不难解决。我们已经在绿盟风云卫模型上进行了验证，只要对模型进行恰当的微调，通常可将单一环境误报率抑制到1%以下，最终取决于具体环境中业务构成的复杂程度。

****四、运行性能和开销****

作为高准确率的代价，DeepSeek-R1的运行开销非常大。

以本次测评中的统计，调用DeepSeek-R1对单个告警进行分析的平均耗时高达32.03秒，同样远远超出迄今为止测试过的所有LLM。作为参考，同等条件下，目前单卡部署的绿盟风云卫模型的平均耗时远小于十分之一。

除了模型本身的体积庞大之外，较为关键的一个因素是，作为一个内置思维链（CoT）的模型，DeepSeek-R1的推理输出中总是会包含非常长的“思考过程”。

即使测试中的prompt要求模型在有效输出中包含人工梳理的分步推理流程（并因此导致有效输出部分并不简短），DeepSeek-R1模型内置的CoT仍然占据了总输出长度的67.71%，比有效输出部分的两倍还多。

有些极端案例中，DeepSeek-R1甚至在CoT中就已经包含了一份符合预期格式的完整结果，然后又在有效输出部分中将同样的内容整个重新抄了一遍，导致了较多不必要的算力开销。

由此认为，要对所有告警都运行完整的DeepSeek-R1模型进行分类，在成本上恐怕是难以接受的。要将DeepSeek模型用于告警分析实战，我们需要探索结合小模型甚至传统规则的综合告警分析方法，而不能完全依赖单个LLM解决所有问题。

****五、对正确预测的分析****

在付出了巨大的开销之后，内置CoT对告警分析的深度产生了显著的提升。即使是包含高度混淆代码的攻击载荷，DeepSeek-R1有时也能予以较为正确的分析。

例如，某WebShell文件上传攻击的原始请求节选如下，可见其中的WebShell内容经过混淆：

|  |
| --- |
| GET /?s=index/\think\template\driver\file/write&cacheFile=robots.php&content=xbshell1%3C?php$password%20=%20%22xinba%22;$ch%20=%20explode(%22.%22,%22hello.ass.world.er.t%22);array\_intersect\_ukey(array($\_REQUEST[$password]%20=%3E%201),%20array(1),%20$ch[1].$ch[3].$ch[4]);?%3E HTTP/1.1  Host: …（后略） |

而DeepSeek-R1模型给出的CoT节选如下：

|  |
| --- |
| 好的,我现在需要分析这个IDS安全告警。首先,看看原始请求部分…content参数经过URL解码后包含PHP代码,其中有一个密码变量$password = “xinba”,然后使用array\_intersect\_ukey函数,并动态调用方法,比如$ch[1].$ch[3].$ch[4],这里$ch是explode后的数组,应该是”hello.ass.world.er.t”分割后的部分,所以索引1是”ass”,3是”er”,4是”t”,组合起来是”assert”。这可能是在尝试执行assert函数,从而执行任意代码…（后略） |

我们以默认参数对上述告警重复运行了10次模型，其中有6次能够针对混淆部分给出完全正确的分析，有2次虽然结论正确但分析过程有误，另有2次未能完成反混淆分析。尽管如此，DeepSeek-R1在未经微调的情况下就达到如此成绩，已经难能可贵。

这种深度分析能力在相当程度上确保了对攻击行为检测的高覆盖率。只不过，要兼顾性能考虑，如何能让小模型具备类似程度的能力，蒸馏模型的性能能否达到预期，还有待进一步研究。

相比之下，绿盟风云卫额外附有专门的攻击载荷反混淆模块以应对复杂告警的分析，后续可以考虑和深度分析互相补足。

****六、对错误预测的分析****

不过CoT也并非包治百病。长期以来，LLM应用经常受到幻觉问题困扰，这在告警分析任务中主要表现为凭空捏造攻击特征，或者强行将正常业务内容认定为攻击特征。

这种幻觉现象在此前评估的各个LLM均有出现，而在DeepSeek-R1的CoT中则体现得更加明显，例如：

|  |
| --- |
| 好的,我现在需要分析这个安全告警。首先,告警名称是Spring Framework的isWritableProperty SpEL表达式注入漏洞(CVE-2018-1273),这说明可能存在利用该漏洞的攻击尝试。  看一下原始请求部分,POST请求的URL是/UserCenter/RegCode,参数中有info字段,其内容是一个JSON对象,包含fromusername、formfullname和system字段。这里需要注意是否有异常的参数构造,特别是是否有SpEL表达式的注入特征。例如,如果参数值中包含类似${}的结构,可能表示尝试注入。  不过,在提供的原始请求中,info参数的值是{“fromusername”:”〔已脱敏〕”,”formfullname”:”〔已脱敏〕”,”system”:”developer”},看起来这些值都是普通字符串,没有明显的SpEL表达式。但需要确认是否有编码或隐藏的特殊字符。例如,是否在参数值中使用了URL编码或其他方式绕过检测。  接下来查看原始响应部分,响应状态码是200,返回的JSON消息显示Success为false,Message为“请使用〔已脱敏〕应用扫码”。这说明请求被处理,但未成功,可能是因为缺少必要的认证或参数。不过,响应中没有明显的错误信息或异常回显,比如SpEL执行后的结果输出,因此无法确定攻击是否成功。  根据攻击结果判定标准,如果响应中没有预期回显或防护拦截特征,且无法确定是否存在漏洞,攻击结果应判定为失败或无法判断。由于响应中没有显示SpEL执行的结果,且没有防护系统的拦截提示,可能属于“无预期回显”的情况,攻击结果可能是失败。  攻击意图方面,如果请求中的参数确实尝试注入SpEL表达式,可能属于试探性攻击,比如探测是否存在漏洞。但根据提供的请求参数,没有明显的恶意负载,因此需要进一步确认是否有编码或混淆的部分。例如,参数是否经过Base64编码或其他方式隐藏攻击载荷。  另外,原始响应中提到报文解析中断,并且缺少完整的响应内容,这可能影响分析。如果关键响应数据缺失,可能导致无法准确判断攻击结果和意图。  总结来说,请求触发了CVE-2018-1273的告警,但参数中没有明显恶意特征,响应也未显示成功利用的迹象。因此,可能属于攻击尝试但未成功,意图是试探性检测漏洞是否存在。 |

可见，明明没有找到任何攻击特征，模型却将其判断为真实攻击。本次测试中绝大多数的误报用例都包含类似情况。

现有的相关研究也表明，推理增强型的LLM相比常规模型更容易产生幻觉：

![](https://blog.nsfocus.net/wp-content/uploads/2025/02/图片7-300x116.png)

图1：DeepSeek-R1与V3模型的幻觉测试对比，可见R1模型的幻觉现象尤为严重[1]

要想充分发挥DeepSeek-R1的优势，真正落地应用到安全运营场景中，我们可能需要引入系统化的外部方法来抑制模型的幻觉问题。

****七、其它发现****

即使不考虑分类准确率，前置CoT也使得有效输出部分变得更加精炼。

此前包括GPT-4o在内的模型测试中，LLM总是在告警分析的输出中包含大量与分析结论无关的垃圾内容。以往的应用实践中，我们通常通过添加自我修正步骤（即要求LLM对自己输出的分析结果进行一次检查修订）来缓解该问题。

DeepSeek-R1虽然也会产生类似的垃圾内容，但其CoT机制使得这些垃圾内容被隔离在“思考过程”之内，而不向最终用户呈现。虽然与传统方法没有本质上的区别，但流程上还是得到了简化。

****八、后记和展望****

本次评测着重评估了DeepSeek-R1在安全告警分析场景中的能力表现，揭示了其显著优势与亟待改进的短板。虽相较于绿盟风云卫展现出更高的覆盖率，但也同时面临误报率偏高和性能开销过大的问题。尤其DeepSeek-R1内置思维链（CoT）机制使其能够深度解析复杂攻击载荷，在真实攻击检测方面展现了卓越的准确率。然而，高误报率和高运行开销严重制约了其直接落地的可行性。

展望未来，以下方向值得进一步探索：

1、模型轻量化与优化：通过知识蒸馏或模型剪枝技术压缩模型规模，降低算力开销；优化模型推理流程，压缩CoT输出长度；针对性微调模型以期减少误报。

2、构建综合分析框架：整合AISecOps体系，结合外部知识库、资产信息、威胁情报等，由轻量模型或规则引擎完成初步筛选，仅对疑难情况调用大模型进行深度分析，从而平衡效率与精度。

尽管当前DeepSeek-R1尚未达到直接替代传统安全分析工具的水平，但其在复杂攻击检测方面的潜力已不容忽视。通过技术迭代与工程优化，我们期待其成为下一代智能安全运营体系的核心组件之一。

如果您发现文中描述有不当之处，还请留言指出。在此致以真诚的感谢。

#### 参考文献

[1]Forrest Bao,Chenyu Xu,Ofer Mendelevitch. DeepSeek-R1 hallucinates more than DeepSeek-V3, 2025[Z/OL]. (2025). https://www.vectara.com/blog/deepseek-r1-hallucinates-more-than-deepseek-v3.

———————————————————————–

本系列文章来自绿盟科技天枢实验室，旨在与安全界同仁共同探索DeepSeek创新技术的奥秘及其在安全行业的应用。我们将通过测试分析、原理阐释、应用方案和实践验证，希望能为读者揭开DeepSeek创新技术的神秘面纱，并分享绿盟科技在拥抱DeepSeek技术、解决实际安全问题中的实践经验与思考，以期抛砖引玉，共同推动智能安全的技术发展。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/cve-20cve-2025-21535-cve-2025-21549/)

[Next](https://blog.nsfocus.net/deepseek2/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)