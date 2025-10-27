---
title: 浅谈AI部署场景下的web漏洞
url: https://forum.butian.net/share/4259
source: 奇安信攻防社区
date: 2025-04-10
fetch_date: 2025-10-06T22:03:57.434602
---

# 浅谈AI部署场景下的web漏洞

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 浅谈AI部署场景下的web漏洞

* [漏洞分析](https://forum.butian.net/topic/48)

总结了一些部署过程中出现可能的漏洞点位，并且分析了对应的攻防思路

要想知道对应的大模型在本地部署过程中可能存在的漏洞，就要先了解大模型是如何进行本地部署的。这里笔者给出了两个轻量化的解决方案，让大家了解一下一般开发者对大模型本地化部署有哪些方式:
开发/部署方案
-------
例如，最简单的，我这里通过调用第三方的API，配合上其他人已经开源的webui，就能够流畅的使用了,比如说:
当然，有的企业处于安全性考虑，并不会把所有数据都交由第三方的API供应商来处理，而是考虑私有化部署，这样就避免了对应的数据外泄，比如采用:<https://github.com/ollama/ollama>
当然，如果你是那种大型企业而且需要对对应大模型微调，可以考虑直接用transformer进行部署。不过这些都不是这篇文章的重点，这篇文章的重点是聚焦于不同场景下的可能会出现哪些web相关的漏洞
漏洞点位
----
### 下载大模型时候出了问题:Prollama(CVE-2024-37032)
这个漏洞总结下来就是在下载(拉取)对应模型的时候出现了问题，由于对应的拉取docker注册中心的url未作充分的校验，于是就导致了可以让ollama服务去访问攻击者的服务器，然后配合一个目录穿越漏洞(拉取到模型目录之外的目录)，攻击者就可以借助本来自带的`/api/push`和`/api/pull`实现对应服务器上的任意文件读写，通过ld\\_preload劫持和写so文件，最终实现rce。
具体的利用流程可以看看这些资料:<https://mp.weixin.qq.com/s/y71ko2NXLp9uuDyPICrzfQ>
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/03/attach-6878013b330204d03d4d4007dcd71870e389f0bc.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/03/attach-85658d5bd7fc34133a5310d7389b0c8be47f920d.png)
在一些不常更新的内网大模型部署业务中挺常见的
### 加载大模型时候出了问题:Transformer/Torch/Numpy的Pickle反序列化问题
有无想过一个问题，大模型是如何被存储到文件中的?没错,就是通过我们熟知的pickle反序列化。
随便点开一个torch.load的方法，发现对应的底层全是pickle![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/03/attach-f04a134f97ddd5348e4236be582b6e104cd22871.png)
因为如果是通过json正反序列化速度太低，还不方便存储各种自定义类，简直被Python原生方便快捷的Pickle完爆，但是众所周知，越便捷，越不安全。不加任何修饰的Pickle反序列化中会直接执行对应的opcode，操作码，直接造成rce。并且有可能自动执行`\_\_reduce\_\_()`函数造成rce，前阵子的字节实习生投毒事件就是通过pickle反序列化来造成了干扰对应的训练结果。不论怎样，魔高一尺，道高一丈。torch退出了对应的`weight\_only`参数，意思是只加载对应模型的权重，而不自动化执行任何代码，就像正常对json格式处理的那样。但是具体是如何实现的呢？我这里直接把对应pip包中的torch\\_weights\\_only\\_unpickler.py放在这里( [https://github.com/ROCm/pytorch/blob/f27220e32af446c24444d4014078106d201d3196/torch/\\\\_weights\\\\_only\\\\_unpickler.py](https://github.com/ROCm/pytorch/blob/f27220e32af446c24444d4014078106d201d3196/torch/%5C\_weights%5C\_only%5C\_unpickler.py) )，稍等我来逐步解析:
首先这里是只允许加载对应白名单的类,具体的白名单全在这个函数里:
```py
def \_get\_allowed\_globals():
rc: Dict[str, Any] = {
"collections.OrderedDict": OrderedDict,
"collections.Counter": Counter,
"torch.nn.parameter.Parameter": torch.nn.Parameter,
"torch.serialization.\_get\_layout": torch.serialization.\_get\_layout,
"torch.Size": torch.Size,
"torch.Tensor": torch.Tensor,
"torch.device": torch.device,
"\_codecs.encode": encode, # for bytes
"builtins.bytearray": bytearray, # for bytearray
"builtins.set": set, # for set
"builtins.complex": complex, # for complex
}
# dtype
for t in torch.storage.\_dtype\_to\_storage\_type\_map().keys():
rc[str(t)] = t
for t in torch.storage.\_new\_dtypes():
rc[str(t)] = t
# Tensor classes
for tt in torch.\_tensor\_classes:
rc[f"{tt.\_\_module\_\_}.{tt.\_\_name\_\_}"] = tt
# Storage classes
for ts in torch.\_storage\_classes:
if ts not in (torch.storage.TypedStorage, torch.storage.UntypedStorage):
# Wrap legacy storage types in a dummy class
rc[f"{ts.\_\_module\_\_}.{ts.\_\_name\_\_}"] = torch.serialization.StorageType(
ts.\_\_name\_\_
)
else:
rc[f"{ts.\_\_module\_\_}.{ts.\_\_name\_\_}"] = ts
# Quantization specific
for qt in [
torch.per\_tensor\_affine,
torch.per\_tensor\_symmetric,
torch.per\_channel\_affine,
torch.per\_channel\_symmetric,
torch.per\_channel\_affine\_float\_qparams,
]:
rc[str(qt)] = qt
# Rebuild functions
for f in \_tensor\_rebuild\_functions():
rc[f"torch.\_utils.{f.\_\_name\_\_}"] = f
# Handles Tensor Subclasses, Tensor's with attributes.
# NOTE: It calls into above rebuild functions for regular Tensor types.
rc["torch.\_tensor.\_rebuild\_from\_type\_v2"] = torch.\_tensor.\_rebuild\_from\_type\_v2
return rc
```
但是为了保证对应的灵活性，用户还是可以通过对应的`\_add\_safe\_globals()`函数来添加自己允许加载的类，这样一来就避免直接通过反序列化opcode直接造成rce。接下来，通过限制对应的魔术方法，来防止黑客在这里做文章，比如`\_\_reduce\_\_`,`\_\_APPEND\_\_`,`\_\_BUILD\_\_`等等
```py
//...
elif key[0] == NEWOBJ[0]:
args = self.stack.pop()
cls = self.stack.pop()
if cls is torch.nn.Parameter:
self.append(torch.nn.Parameter(\*args))
elif (
cls in \_get\_user\_allowed\_globals().values()
or cls in \_get\_allowed\_globals().values()
):
self.append(cls.\_\_new\_\_(cls, \*args))
else:
raise UnpicklingError(
"Can only create new object for nn.Parameter or classes allowlisted "
f"via `add\_safe\_globals` but got {cls}"
)
elif key[0] == REDUCE[0]:
args = self.stack.pop()
func = self.stack[-1]
if (
func not in \_get\_allowed\_globals().values()
and func not in \_get\_user\_allowed\_globals().values()
):
raise UnpicklingError(
f"Trying to call reduce for unrecognized function {func}"
)
self.stack[-1] = func(\*args)
```
并且对一些高危模块比如os,sys做更加彻底的封锁。
总结一下就是:
- 最小权限原则：默认仅允许加载模型权重所需的必要类型，其他功能需显式授权。
- 操作码过滤：对可能引发动态行为的操作码（如 GLOBAL/REDUCE）进行严格的白名单校验。
- 类型强约束：限制操作码只能作用于特定类型（如 BUILD 仅限 Tensor），避免泛型攻击。
- 模块隔离：通过模块黑名单彻底隔离高危模块，即使类名相同也无法绕过。
还算安全，不过我在看得时候发现了一件趣事，在BUILD的指令中存在这样的一段代码: ```py
if isinstance(state, tuple) and len(state) == 2:
state, slotstate = state
if state:
inst.\_\_dict\_\_.update(state)
if slotstate:
for k, v in slotstate.items():
setattr(inst, k, v)
else:
///。。。
```
当我们传入了一个元组对象的时候，这里会自动化的设置对应的所有的属性和对应的键值，但是由于前文中输入的类型在这里已经限制死是哪几个类。所以说，这个漏洞只有当开发者手动加入对应的:`\_add\_safe\_globals`方式的时候才会造成对应的污染属性的漏洞。所有还是如无必要，无增实体为好。当然，针对黑白名单，也有其他的防御方式。比如大名鼎鼎的ModelScan的pip包:
我这里是去观察了对应的黑名单策略，全在对应`settings.py`中了
```py
import tomlkit
from typing import Any
from modelscan.\_version import \_\_version\_\_
class Property:
def \_\_init\_\_(self, name: str, value: Any) -> None:
self.name = name
self.value = value
class SupportedModelFormats:
TENSORFLOW = Property("TENSORFLOW", "tensorflow")
KERAS\_H5 = Property("KERAS\_H5", "keras\_h5")
KERAS = Property("KERAS", "keras")
NUMPY = Property("NUMPY", "numpy")
PYTORCH = Property("PYTORCH", "pytorch")
PICKLE = Property("PICKLE", "pickle")
DEFAULT\_REPORTING\_MODULES = {
"console": "modelscan.reports.ConsoleReport",
"json": "modelscan.reports.JSONReport",
}
DEFAULT\_SETTINGS = {
"modelscan\_version": \_\_version\_\_,
"supported\_zip\_extensions": [".zip", ".npz"],
"scanners": {
"modelscan.scanners.H5LambdaDetectScan": {
"enabled": True,
"supported\_extensions": [".h5"],
},
"modelscan.scanners.KerasLambdaDetectScan": {
"enabled": True,
"supported\_extensions": [".keras"],
},
"modelscan.scanners.SavedModelLambdaDetectScan": {
"enabled": True,
"supported\_extensions": [".pb"],
"unsafe\_keras\_operators": {
"Lambda": "MEDIUM",
},
},
"modelscan.scanners.SavedModelTensorflowOpScan": {
"enabled": True,
"supported\_extensions": [".pb"],
"unsafe\_tf\_operators": {
"ReadFile": "HIGH",
"WriteFile": "HIGH",
},
},
"modelscan.scanners.NumpyUnsafeOpScan": {
"enabled": True,
"supported\_extensions": [".npy"],
},
"modelscan.scanners.PickleUnsafeOpScan": {
"enabled": True,
"supported\_extensions": [
".pkl",
".pickle",
".joblib",
".dill",
".dat",
".data",
],
},
"modelscan.scanners.PyTorchUnsafeOpScan": {
"enabled": True,
"supported\_extensions": [".bin", ".pt", ".pth", ".ckpt"],
},
},
"middlewares": {
"modelscan.middlewares.FormatViaExtensionMiddleware": {
"formats": {
SupportedModelFormats.TENSORFLOW: [".pb"],
SupportedModelFormats.KERAS\_H5: [".h5"],
SupportedModelFormats.KERAS: [".keras"],
SupportedModelFormats.NUMPY: [".npy"],
SupportedModelFormats.PYTORCH: [".bin", ".pt", ".pth", ".ckpt"],
SupportedModelFormats.PICKLE: [
".pkl",
".pickle",
".joblib",
".dill",
".dat",
".data",
],
}
}
},
"unsafe\_globals": {
"CRITICAL": {
"\_\_builtin\_\_": [
"eval",
"compile",
"getattr",
"...