---
title: fortify sca rules 标签分析
url: https://mp.weixin.qq.com/s?__biz=MzI2NTExNzcxNQ==&mid=2247484340&idx=1&sn=f4e4276774ad25887d9f44ca481b83bd&chksm=eaa30ac8ddd483de221f48c0eb18536e999aa49be6bc1e52ed06fe7e313d38289d0a95f72069&scene=58&subscene=0#rd
source: 代码审计SDL
date: 2024-11-09
fetch_date: 2025-10-06T19:18:26.148897
---

# fortify sca rules 标签分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/a4tp2b7vTo6o6jvNXrFPofW8fH3vsXLXDGWptUCskJdIVGxMtlpxq47KPicZ8eiboYOKIPpRMFQy474PqDRKCE1Q/0?wx_fmt=jpeg)

# fortify sca rules 标签分析

原创

sanduo

代码审计SDL

# RulePack标签分析

```
1. <?xml version="1.0" encoding="UTF-8"?>
2. <RulePack xmlns:mask="xmlns://www.fortifysoftware.com/schema/mask" xmlns="xmlns://www.fortifysoftware.com/schema/rules">
3. <RulePackID>D044EBBB-7081-4451-BDD6-5A163AD639C3</RulePackID>
4. <SKU>RUL13040</SKU>
5. <Name>
6. <![CDATA[Fortify 安全编码规则、核心、Java]]>
7. </Name>
8. <Activated>true</Activated>
9. <Version>2024.2.1.0003</Version>
10. <Language>java</Language>
11. <Description>
12. <![CDATA[为 Java 提供安全相关核心语言 API 范围。此规则包的部分内容来自 Cigital Java Rulepack (c) 2008 Cigital。 Copyright 2004 - 2024 Open Text.]]>
13. </Description>
14. <Locale>zh_CN</Locale>
15. <Rules version="3.2" minimumSCA="17.10">
16. ......
17. </Rules>
18. <Masks revision="0">
19. ......
20. </Masks>
21. <Localization>
22. ......
23. </Localization>
24. </RulePack>
```

xml标签属性说明

* RulePackID：规则包的唯一标识符
* SKU：全局唯一标识符
* Name：规则包的名称
* Activated：可以使用的(猜测，没找到定义内容)
* Version：规则版本
* Language：规则包适配编程语言
* Description：规则包描述信息
* Locale：规则包语言
* Rules：规则主体，其中version是版本代号，minimumSCA 标识规则最低支持的fortify sca版本
* Masks ：掩码
* Localization：本地化

# Rules标签分析

```
1. <Rules version="3.2" minimumSCA="17.10">
2. <Notes>
3. ......
4. </Notes>
5. <RuleDefinitions>
6. ......
7. </RuleDefinitions>
8. <LabelDefinitions>
9. ......
10. </LabelDefinitions>
11. <Descriptions>
12. ......
13. </Descriptions>
14. <ControlflowStateStrings>
15. ......
16. </ControlflowStateStrings>
17. <TaintFlagDeclarations>
18. ......
19. </TaintFlagDeclarations>
20. <TaintFlagDescriptions>
21. ......
22. </TaintFlagDescriptions>
23. <Coverage>
24. ......
25. </Coverage>
26. <ScriptDefinitions/>
27. </Rules>
```

xml标签属性说明

* Notes：规则备注信息，许可声明信息
* RuleDefinitions：规则集合
* LabelDefinitions：标签定义
* Descriptions：描述信息
* ControlflowStateStrings：控制流状态字符串
* TaintFlagDeclarations：污染标志声明
* TaintFlagDescriptions：污染标志说明
* Coverage：覆盖度
* ScriptDefinitions：脚本定义

## DataflowSourceRule 标签分析

```
1. <DataflowSourceRule formatVersion="3.2" language="java">
2. <MetaInfo>
3. <Group name="package">Java Core Accessibility</Group>
4. <Group name="inputsource">Web</Group>
5. </MetaInfo>
6. <RuleID>58B43BC7-05D2-4289-B0CE-BECAFC28A45E</RuleID>
7. <FunctionIdentifier>
8. <NamespaceName>
9. <Value>javax.accessibility</Value>
10. </NamespaceName>
11. <ClassName>
12. <Value>AccessibleText</Value>
13. </ClassName>
14. <FunctionName>
15. <Pattern>(get.+Index)|getSelectedText</Pattern>
16. </FunctionName>
17. <Parameters>
18. <ParamType>int</ParamType>
19. <ParamType>int</ParamType>
20. </Parameters>
21. <ApplyTo implements="true" overrides="true" extends="true" />
22. </FunctionIdentifier>
23. <OutArguments>return</OutArguments>
24. </DataflowSourceRule>
```

DataflowSourceRule识别受污染的数据进入程序的位置。

* MetaInfo：元信息，规则分类信息

+ package：包信息， `<Groupname="package">Java Core Accessibility</Group>` 表示这条规则属于 "Java Core Accessibility" 包。
+ inputsource：输入源， `<Groupname="inputsource">Web</Group>` 表示这条规则关注的是来自 Web 的输入源。

+ Group：组标签

* RuleID：唯一的标识符，用于区分不同的规则。
* FunctionIdentifier：函数标识

+ NamespaceName：**命名空间，** `<NamespaceName><Value>javax.accessibility</Value></NamespaceName>` 指定了方法所在的命名空间。
+ ClassName：**类名，** `<ClassName><Value>AccessibleText</Value></ClassName>` 指定了方法所在的类。
+ FunctionName：函数名， `<FunctionName><Pattern>(get.+Index)|getSelectedText</Pattern></FunctionName>` 使用正则表达式匹配方法名，包括 `getCharIndex`, `getWordIndex`, `getSentenceIndex`, 和 `getSelectedText`。
+ Parameters：参数， `<Parameters><ParamType>int</ParamType><ParamType>int</ParamType></Parameters>` 指定了方法的参数类型，这里有两个 `int` 类型的参数。

* OutArguments：输出参数，用于指定方法调用后哪些参数或返回值应被视为污染（tainted）数据， `<OutArguments>return</OutArguments>` 指定了方法的返回值应被视为污染数据。

## LabelDefinitions标签分析

```
1. <CharacterizationRule formatVersion="3.7" language="java">
2. <MetaInfo>
3. <Group name="package">Java Core JMX</Group>
4. </MetaInfo>
5. <RuleID>04DC0B4B-6AC5-4B93-9B46-486D7B4778A8</RuleID>
6. <StructuralMatch>
7. <![CDATA[
8. FunctionCall fc: function is [Function:
9. name == "registerMBean"
10. and enclosingClass.supers contains [Class: name == "javax.management.MBeanServer"]
11. ]
12. and arguments[0] is [Expression:
13. reachingTypes contains [Type: definition is [Class jmxbean:]]
14. ]
15. ]]>
16. </StructuralMatch>
17. <Definition>
18. <![CDATA[
19. foreach jmxbean {
20. Label(jmxbean, "JMXBean")
21. }
22. ]]>
23. </Definition>
24. </CharacterizationRule>
```

字符化规则（ `<CharacterizationRule>`），用于识别和标记 Java 代码中特定的结构模式。

* CharacterizationRule：

+ formatVersion：**格式版本，** `formatVersion="3.7"` 指明了规则使用的格式版本。
+ language：**语言，** `language="java"` 指明了这条规则适用于 Java 语言。

* MetaInfo：元数据， `<MetaInfo>` 元素提供了关于规则的分类信息。

+ Group： `<Groupname="package">Java Core JMX</Group>` 表示这条规则属于 "Java Core JMX" 包。

* RuleID：规则唯一的标识符
* StructuralMatch：结构匹配， `<StructuralMatch>` 元素定义了要匹配的代码结构。

+ `FunctionCallfc` 表示要匹配的函数调用。
+ `functionis[Function:name=="registerMBean"andenclosingClass.supers contains[Class:name=="javax.management.MBeanServer"]]` 表示要匹配的函数名为 `registerMBean`，并且该函数所在类的超类包含 `javax.management.MBeanServer`。
+ `arguments[0]is[Expression:reachingTypes contains[Type:definitionis[Classjmxbean:]]]` 表示第一个参数的类型是某个类 `jmxbean`。

* Definition：**定义，** `<Definition>` 元素定义了在匹配到特定结构时要执行的操作。

+ `foreachjmxbean{Label(jmxbean,"JMXBean")}` 表示对每一个匹配到的 `jmxbean` 类型，为其添加一个标签 `"JMXBean"`。

## Descirptions标签分析

```
1. <Descriptions>
2. <Description
3. id="desc.controlflow.java.intent_manipulation_implicit_internal_intent" formatVersion="3.4">
4. <Abstract>
5. <![CDATA[<Paragraph>在 <Replace key="PrimaryLocation.file"/> 的第 <Replace key="PrimaryLocation.line"/> 行检测到隐式内部 <code>Intent</code>。隐式的内部意图可能会使系统遭受对内部组件的中间人攻击。<AltParagraph>检测到隐式内部 <code>Intent</code>。隐式的内部意图可能会使系统遭受对内部组件的中间人攻击。</AltParagraph></Paragraph>]]>
6. </Abstract>
7. <Explanation>
8. <![CDATA[内部 <code>Intent</code> 使用内部组件定义的自定义操作。隐式意图可以促进从任何给定外部组件调用意图，而无需了解特定组件。将两者结合起来使应用程序能够从所需的应用程序上下文外部访问为特定内部使用指定的意图。

10. 通过外部应用程序处理内部 <code>Intent</code> 的能力可以实现各种严重程度不等的中间人攻击，从信息泄露、拒绝服务到远程代码执行，具体取决于 <code>Intent</code> 指定的内部操作的能力。

12. <b>示例 1：</b>以下代码使用隐式内部 <code>Intent</code>。

14. <pre>
15. ...
16. val imp_internal_intent_action = Intent("INTERNAL_ACTION_HERE")
17. startActivity(imp_internal_intent_action)
18. ...
19. </pre>]]>
20. </Explanation>
21. <Recommendations>
22. <![CDATA[仅调用具有明确意图的内部应用程序。显式 <code>Intent</code> 是显式设置其组件、类、类名和包的意图。

24. <b>示例 2：</b>以下代码使用显式内部 <code>Intent</code>。

26. <pre>
27. ...
28. val exp_internal_intent = Intent("INTERNAL_ACTION_HERE", Uri.EMPTY, this, DownloadService::class.java)
29. startActivity(exp_internal_intent)
30. ...
31. </pre>

33. <b>示例 3：</b>以下代码使用隐式内部 <code>Intent</code>，该意图已通过 setter 更新为显式。

35. <pre>
36. ...
37. val imp_internal_intent_remediate_action = Intent("INTERNAL_ACTION_HERE")

39. imp_internal_intent_remediate_action.`package` = "package"
40. imp_internal_intent_remediate_action.setClass(this, DownloadService::class.java)
41. imp_internal_intent_remediate_action.component = componentName

43. startActivity(imp_internal_intent_remediate_action)
44. ...
45. </pre>]]>
46. </Recommendations>
47. <References>
48. <Reference>
49. <Title>
50. <![CDATA[Remediation of Implicit Internal Intent Vulnerability]]>
51. </Title>
52. <Source>
53. <![CDATA[https://support.google.com/faqs/answer/10399926]]>
54. </Source>
55. </Reference>
56. <Reference>
57. <Title>
58. <![CDATA[CWE ID 99]]>
59. </Title>
60. <Author>
61. <![CDATA[Standards Mapping - Common Weakness Enumeration]]>
62. </Author>
63. </Reference>
64. <Reference>
65. <Title>
66. <![CDATA[CCI-001094]]>
67. </Title>
68. <Author>
69. <![CDATA[Standards Mapping - DISA Control Correlation Identifier Version 2]]>
70. </Author>
71. </Reference>
72. <Reference>
73. <Title>
74. <![CDATA[Indirect Access to Sensitive Data]]>
75. </Title>
76. <Author>
77. <![CDATA[Standards Mapping - General Data Protection Regulation]]>
78. </Author>
79. </Reference>
80. <Reference>
81. <Title>
82. <![CDATA[SC-5 Denia...