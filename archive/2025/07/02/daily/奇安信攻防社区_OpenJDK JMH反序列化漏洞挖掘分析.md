---
title: OpenJDK JMH反序列化漏洞挖掘分析
url: https://forum.butian.net/share/4438
source: 奇安信攻防社区
date: 2025-07-02
fetch_date: 2025-10-06T23:16:34.310954
---

# OpenJDK JMH反序列化漏洞挖掘分析

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

### OpenJDK JMH反序列化漏洞挖掘分析

* [漏洞分析](https://forum.butian.net/topic/48)

JMH,即Java Microbenchmark Harness,是专门用于代码微基准测试的工具套件。主要是基于方法层面的基准测试,精度可以达到纳秒级。该组件存在一个未被别人公开过但目前来说实战意义不大的反序列化漏洞，仅可当作思路阅读

\*\*一、漏洞简介\*\*
==========
[JMH](https://openjdk.org/projects/code-tools/jmh/),即Java Microbenchmark Harness,是专门用于代码微基准测试的工具套件。主要是基于方法层面的基准测试,精度可以达到纳秒级。该组件存在一个未被别人公开过但目前来说实战意义不大的反序列化漏洞，仅可当作思路阅读
\*\*二、影响版本\*\*
==========
ALL
\*\*三、漏洞挖掘分析\*\*
============
首先看官方DEMO
```java
public static void main(String[] args) throws RunnerException {
Options opt = new OptionsBuilder()
.include(WhatsupBro.class.getSimpleName())
.forks(1)
.build();
new Runner(opt).run();
}
}
```
从DEMO查看好像平平无奇，跟进`run()`方法看看流程：
在`run`方法中，会先获取JMH的参数配置，当`JMH\_LOCK\_IGNORE`是`true`时就会进入下一个流程，不是也没关系，最终还是会走向同一个流程
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-c598edf1cf03f236e23437aabdb3bfa5b85caf1c.png)
跟进`internalRun()`：
前半部分是初始化，做基准测试的一些基本设置
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-9e3bea8d3ced664b75fd125e8ab994d9e4dade1d.png)
前戏有很多，继续往后看，快进到`runBenchmarks(benchmarks)`：
做完所有设置后，就开始进入`runBenchmarks`方法开始执行流程
```java
Collection<RunResult> results = runBenchmarks(benchmarks);
// If user requested the result file, write it out.
if (resultFile != null) {
ResultFormatFactory.getInstance(
options.getResultFormat().orElse(Defaults.RESULT\_FORMAT),
resultFile
).writeOut(results);
out.println("");
out.println("Benchmark result is saved to " + resultFile);
}
out.flush();
out.close();
return results;
}
```
`runBenchmarks`方法：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-b442d2dc3b9b7773401eec45ec1778eb10c7cf5d.png)
在这个方法中，我们只需关注`case FORKED`这一部分的流程：
```java
try {
for (ActionPlan r : plan) {
Multimap<BenchmarkParams, BenchmarkResult> res;
switch (r.getType()) {
case EMBEDDED:
res = runBenchmarksEmbedded(r);
break;
case FORKED:
res = runSeparate(r);
break;
default:
throw new IllegalStateException("Unknown action plan type: " + r.getType());
}
for (BenchmarkParams br : res.keys()) {
results.putAll(br, res.get(br));
}
}
```
因为在`getActionPlans(benchmarks)`中，`ActionType.type`就被初始化为了`FORKED`：
```java
if (params.getForks() <= 0) {
if (options.getWarmupMode().orElse(Defaults.WARMUP\_MODE).isIndi()) {
embeddedPlan.add(newAction(br, ActionMode.WARMUP\_MEASUREMENT));
} else {
embeddedPlan.add(newAction(br, ActionMode.MEASUREMENT));
}
addEmbedded = true;
}
//方法会走这里，因为前面的DEMO中我们的代码是.forks(1)，大于0
if (params.getForks() > 0) {
ActionPlan r = new ActionPlan(ActionType.FORKED);
r.mixIn(base);
if (options.getWarmupMode().orElse(Defaults.WARMUP\_MODE).isIndi()) {
r.add(newAction(br, ActionMode.WARMUP\_MEASUREMENT));
} else {
r.add(newAction(br, ActionMode.MEASUREMENT));
}
result.add(r);
}
```
回到`case FORKED`流程，进入到`runSeparate`方法：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-982ae51c84849fc7978d5a4048ba4a52c56e7a3d.png)
在`runSeparate`里，初始化了一个`BinaryLinkServer`对象
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-9f4acb345d00ffdb2608fc797cabc547ce10057d.png)
同样的，前面的内容没有意义，快进到
```java
acceptor = new Acceptor();
acceptor.start();
```
跟进`Acceptor()`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-b40c9bd9ae73eacda10f750afef19239eff15916.png)
快进到`Handler`，查看怎么处理的连接：
```java
private final class Handler extends Thread {
private final InputStream is;
private final Socket socket;
private ObjectInputStream ois;
private final OutputStream os;
private ObjectOutputStream oos;
public Handler(Socket socket) throws IOException {
this.socket = socket;
this.is = socket.getInputStream();
this.os = socket.getOutputStream();
// eager OOS initialization, let the other party read the stream header
//记住这里，一会要考
oos = new ObjectOutputStream(new BufferedOutputStream(os, BUFFER\_SIZE));
oos.flush();
}
@Override
public void run() {
try {
// late OIS initialization, otherwise we'll block reading the header
ois = new ObjectInputStream(new BufferedInputStream(is, BUFFER\_SIZE));
Object obj;
//对socket数据流做反序列化
while ((obj = ois.readObject()) != null) {
if (obj instanceof OutputFormatFrame) {
handleOutputFormat((OutputFormatFrame) obj);
}
if (obj instanceof InfraFrame) {
handleInfra((InfraFrame) obj);
}
if (obj instanceof HandshakeInitFrame) {
handleHandshake((HandshakeInitFrame) obj);
}
if (obj instanceof ResultsFrame) {
handleResults((ResultsFrame) obj);
}
if (obj instanceof ExceptionFrame) {
handleException((ExceptionFrame) obj);
}
if (obj instanceof OutputFrame) {
handleOutput((OutputFrame) obj);
}
if (obj instanceof ResultMetadataFrame) {
handleResultMetadata((ResultMetadataFrame) obj);
}
if (obj instanceof FinishingFrame) {
// close the streams
break;
}
}
} catch (EOFException e) {
// ignore
} catch (Exception e) {
out.println("<binary link had failed, forked VM corrupted the stream? Use " + VerboseMode.EXTRA + " verbose to print exception>");
if (opts.verbosity().orElse(Defaults.VERBOSITY).equalsOrHigherThan(VerboseMode.EXTRA)) {
out.println(Utils.throwableToString(e));
}
} finally {
close();
}
}
```
好了，现在已经看到了一个反序列化，接下来就是验证了。已知这是一个socket数据流反序列化，那么就要找到socket的监听端口，这样我们才能向端口发送序列化数据，回到`Acceptor()`：
```java
public Acceptor() throws IOException {
listenAddress = getListenAddress();
server = new ServerSocket(getListenPort(), 50, listenAddress);
}
```
查看getListenPort()方法：
```js
private int getListenPort() {
return Integer.getInteger("jmh.link.port", 0);
}
```
随机端口
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-16d5f369140448fa793626c8759b810337de2e4b.png)
\*\*四、环境搭建\*\*
==========
[官方仓库](https://github.com/openjdk/jmh)下载解压，等待依赖下载完就行了，org/openjdk/jmh/samples都是DEMO，随便运行哪个都行
\*\*五、漏洞验证\*\*
==========
但是话又说回来，站在黑客的角度，其实是可以通过扫描端口来发现漏洞的，记得刚刚圈出来的考点：
```java
public Handler(Socket socket) throws IOException {
this.socket = socket;
this.is = socket.getInputStream();
this.os = socket.getOutputStream();
// eager OOS initialization, let the other party read the stream header
oos = new ObjectOutputStream(new BufferedOutputStream(os, BUFFER\_SIZE));
oos.flush();
}
```
项目启动的时候，它会封装一个包含有流标头的输出流方便客户端读取，也就是说，如果我们扫描全端口，会发现有一个端口出现这种情况：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-2b781864cf5fadcc9ebdffdf3a4fdfdfb40d72c9.png)
POC：
```python
import socket
import threading
import queue
import binascii
from concurrent.futures import ThreadPoolExecutor
import sys
TARGET\_HOST = "127.0.0.1"#改成目标地址
PORT\_RANGE = range(1, 65536)
TIMEOUT = 1
MAX\_THREADS = 100
STREAM\_HEADER = b"\xAC\xED\x00\x05"
result\_queue = queue.Queue()
def check\_port(port):
try:
sock = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
sock.settimeout(TIMEOUT)
sock.connect((TARGET\_HOST, port))
data = sock.recv(1024)
if data.startswith(STREAM\_HEADER):
hex\_data = binascii.hexlify(data[:4]).decode().upper()
result\_queue.put((port, hex\_data))
sock.close()
except (socket.timeout, socket.error):
pass
def scan\_ports():
print(f"开始扫描 {TARGET\_HOST} 的端口...")
with ThreadPoolExecutor(max\_workers=MAX\_THREADS) as executor:
executor.map(check\_port, PORT\_RANGE)
print("\n扫描完成，发现以下端口符合特征:")
while not result\_queue.empty():
port, hex\_data = result\_queue.get()
print(f"端口: {port}, 数据: {hex\_data}")
if \_\_name\_\_ == "\_\_main\_\_":
try:
scan\_ports()
except KeyboardInterrupt:
print("\n扫描中断")
sys.exit(1)
```
因...