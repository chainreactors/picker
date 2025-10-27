---
title: 深入浅出Joern（三）Joern和Neo4j常用语法大全
url: https://govuln.com/news/url/ZQom
source: Sec-News 安全文摘
date: 2023-08-26
fetch_date: 2025-10-04T11:58:40.587772
---

# 深入浅出Joern（三）Joern和Neo4j常用语法大全



[LoRexxar's Blog | 盲驴隆忙聛炉忙聤聙忙聹炉氓聢聠盲潞芦](/)

[LoRexxar's Blog | 盲驴隆忙聛炉忙聤聙忙聹炉氓聢聠盲潞芦](/)

忙路卤氓聟楼忙碌聟氓聡潞Joern茂录聢盲赂聣茂录聣Joern氓聮聦Neo4j氓赂赂莽聰篓猫炉颅忙鲁聲氓陇搂氓聟篓



# 忙路卤氓聟楼忙碌聟氓聡潞Joern茂录聢盲赂聣茂录聣Joern氓聮聦Neo4j氓赂赂莽聰篓猫炉颅忙鲁聲氓陇搂氓聟篓

sast
joern
neo4j


2023/08/24




Share

* 
* 
* 
* 
* 

![](/assets/loading.svg)

氓聣聧盲赂陇莽炉聡忙聳聡莽芦聽盲赂禄猫娄聛猫庐虏盲潞聠Joern莽聸赂氓聟鲁忙聤聙忙聹炉莽職聞猫庐戮猫庐隆氓聨聼莽聬聠茂录聦盲禄楼氓聫聤CPG莽職聞氓庐聻茅聶聟猫隆篓莽聨掳

* <https://lorexxar.cn/2023/08/21/joern-and-cpg/>
* <https://lorexxar.cn/2023/08/22/joern2/>

氓聹篓莽聽聰莽漏露Joern氓聮聦Neo4j莽職聞猫驴聡莽篓聥盲赂颅茂录聦忙聢聭茅聛聡氓聢掳盲潞聠盲赂聙盲赂陋莽聸赂氓陆聯氓陇搂莽職聞茅聴庐茅垄聵茂录聦氓掳卤忙聵炉莽聰卤盲潞聨忙聢聭氓炉鹿**OverflowDB氓聦聟忙聥卢scala氓聮聦cypher猫炉颅猫篓聙**茅聝陆盲赂聧莽聠聼茫聙聜Joern氓聮聦Neo4j氓聢聠氓聢芦忙聰炉忙聦聛猫驴聶氓聡聽莽搂聧氓聠路茅聴篓猫炉颅猫篓聙茂录聦猫聙聦莽聸赂氓潞聰莽職聞忙聳聡忙隆拢氓聟露氓庐聻忙虏隆忙聹聣猫搂拢氓聠鲁忙聢聭莽職聞茅聴庐茅垄聵茫聙聜

忙聣聙盲禄楼氓聹篓莽禄搂莽禄颅莽聽聰莽漏露Joern盲鹿聥氓聣聧茂录聦氓聟聢猫聤卤忙聴露茅聴麓莽庐聙氓聧聲猫庐掳氓陆聲**盲赂聙盲潞聸Joern氓聮聦Neo4j氓庐聻莽聰篓莽職聞猫炉颅忙鲁聲氓聮聦猫聦聝盲戮聥**茂录聦莽禄聶猫聡陋氓路卤氓陆聯盲赂陋氓颅聴氓聟赂茅職聫忙聴露氓聫炉盲禄楼忙聼楼茅聵聟茫聙聜

# Joern

* <https://docs.joern.io/cpgql/reference-card/>
* <https://docs.joern.io/cpgql/node-type-steps/>

## 猫聤聜莽聜鹿猫聨路氓聫聳

* **cpg.method.name(芒聙聵xxx芒聙聶)**
* **cpg.method(芒聙聵xxx芒聙聶)**

氓炉禄忙聣戮氓炉鹿氓潞聰氓聬聧氓颅聴莽職聞忙聳鹿忙鲁聲氓庐職盲鹿聣莽職聞盲陆聧莽陆庐

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` joern> cpg.method.name("getRequestBody").l val res4: List[io.shiftleft.codepropertygraph.generated.nodes.Method] = List(   Method(     id = 15337L,     astParentFullName = "<empty>",     astParentType = "<empty>",     code = "public static String getRequestBody(HttpServletRequest request) throws IOException",     columnNumber = Some(value = 5),     columnNumberEnd = Some(value = 5),     filename = "src\\main\\java\\org\\joychou\\util\\WebUtils.java",     fullName = "org.joychou.util.WebUtils.getRequestBody:<unresolvedSignature>(1)",     hash = None,     isExternal = false,     lineNumber = Some(value = 13),     lineNumberEnd = Some(value = 16),     name = "getRequestBody",     order = 1,     signature = "<unresolvedSignature>(1)"   ) ) ``` |

* **cpg.call.name(芒聙聵xxx芒聙聶)**
* **cpg.call(芒聙聵xxx芒聙聶)**

氓炉禄忙聣戮氓炉鹿氓潞聰忙聳鹿忙鲁聲/氓聡陆忙聲掳猫掳聝莽聰篓莽職聞盲陆聧莽陆庐

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ``` joern> cpg.call("getRequestBody").take(1).l val res7: List[io.shiftleft.codepropertygraph.generated.nodes.Call] = List(   Call(     id = 8485L,     argumentIndex = 2,     argumentName = None,     code = "getRequestBody(request)",     columnNumber = Some(value = 22),     dispatchType = "DYNAMIC_DISPATCH",     dynamicTypeHintFullName = ArraySeq(),     lineNumber = Some(value = 25),     methodFullName = "org.joychou.util.WebUtils.getRequestBody:<unresolvedSignature>(1)",     name = "getRequestBody",     order = 2,     possibleTypes = ArraySeq(),     signature = "<unresolvedSignature>(1)",     typeFullName = "java.lang.String"   ) ) ``` |

* **cpg.annotation.name(芒聙聹.\*Mapping芒聙聺)**
* **cpg.annotation(芒聙聹.\*Mapping芒聙聺)**

氓炉禄忙聣戮氓炉鹿氓潞聰氓聬聧氓颅聴忙鲁篓猫搂拢莽職聞猫聤聜莽聜鹿

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` joern> cpg.annotation.name(".*Mapping").take(1).l val res10: List[io.shiftleft.codepropertygraph.generated.nodes.Annotation] = List(   Annotation(     id = 2532L,     argumentIndex = -1,     argumentName = None,     code = "@RequestMapping(\"/safecode\")",     columnNumber = Some(value = 5),     fullName = "org.springframework.web.bind.annotation.RequestMapping",     lineNumber = Some(value = 20),     name = "RequestMapping",     order = 7   ) ) ``` |

氓聹篓joern莽職聞猫聤聜莽聜鹿盲陆聽茅聝陆氓聫炉盲禄楼茅聺聻氓赂赂莽庐聙氓聧聲莽職聞**莽聰篓莽聜鹿猫驴聻忙聨楼忙聺楼猫聨路氓聫聳氓炉鹿氓潞聰猫聤聜莽聜鹿猫驴聻忙聨楼莽職聞氓聟露盲禄聳猫聤聜莽聜鹿**

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` joern> cpg.annotation.name(".*Mapping").method.take(1).l val res21: List[io.shiftleft.codepropertygraph.generated.nodes.Method] = List(   Method(     id = 2498L,     astParentFullName = "<empty>",     astParentType = "<empty>",     code = "public void crlf(HttpServletRequest request, HttpServletResponse response)",     columnNumber = Some(value = 5),     columnNumberEnd = Some(value = 5),     filename = "src\\main\\java\\org\\joychou\\controller\\CRLFInjection.java",     fullName = "org.joychou.controller.CRLFInjection.crlf:<unresolvedSignature>(2)",     hash = None,     isExternal = false,     lineNumber = Some(value = 20),     lineNumberEnd = Some(value = 28),     name = "crlf",     order = 1,     signature = "<unresolvedSignature>(2)"   ) ) ``` |

茅聶陇盲潞聠氓赂赂猫搂聞莽職聞**method茂录聦annotation茂录聦call**猫驴聶莽搂聧盲禄楼氓陇聳茂录聦忙炉聰猫戮聝氓赂赂猫搂聛莽職聞猫聤聜莽聜鹿莽卤禄氓聻聥猫驴聵忙聹聣

<https://docs.joern.io/cpgql/node-type-steps/>

* **cpg.configFile茂录職茅聟聧莽陆庐忙聳聡盲禄露**
* **cpg.identifier茂录職忙聽聡猫炉聠莽卢娄**
* **cpg.imports茂录職氓录聲莽聰篓**
* **cpg.methodReturn茂录職忙聳鹿忙鲁聲莽職聞猫驴聰氓聸聻猫聤聜莽聜鹿**
* **cpg.parameter茂录職氓聫聜忙聲掳**

氓陆聯莽聞露茅聶陇盲潞聠盲赂聤茅聺垄莽職聞猫驴聶盲潞聸猫聤聜莽聜鹿盲禄楼氓陇聳茂录聦猫驴聵忙聹聣盲赂聙盲潞聸猫掳聝莽聰篓氓聟鲁莽鲁禄莽職聞茅聙職莽聰篓猫聤聜莽聜鹿

* **cpg.method.name(芒聙聹getRequestBody芒聙聺).caller**

猫驴聰氓聸聻猫聤聜莽聜鹿氓聢聴猫隆篓氓炉鹿氓潞聰猫聤聜莽聜鹿莽職聞猫垄芦猫掳聝莽聰篓猫聤聜莽聜鹿茂录聦盲鹿聼氓掳卤忙聵炉莽聢露猫聤聜莽聜鹿

* **cpg.method.name(芒聙聹getRequestBody芒聙聺).callee**

猫驴聰氓聸聻猫聤聜莽聜鹿氓聢聴猫隆篓氓炉鹿氓潞聰猫聤聜莽聜鹿莽職聞猫掳聝莽聰篓猫聤聜莽聜鹿茂录聦盲鹿聼氓掳卤忙聵炉氓颅聬猫聤聜莽聜鹿

* **cpg.method.name(芒聙聹getRequestBody芒聙聺).callIn**

猫驴聰氓聸聻猫聤聜莽聜鹿氓聢聴猫隆篓氓炉鹿氓潞聰莽聢露猫聤聜莽聜鹿莽職聞忙聣聙忙聹聣猫聤聜莽聜鹿

## 猫驴聡忙禄陇氓聶篓

氓聡隆忙聵炉猫聤聜莽聜鹿猫驴聻忙聨楼莽職聞茅聝陆忙聵炉盲陆聹盲赂潞莽禄聯忙聻聹盲录聽氓聢掳盲赂聥盲赂聙莽潞搂莽職聞茂录聦氓娄聜忙聻聹忙聵炉忙聝鲁莽颅聸茅聙聣莽卢娄氓聬聢忙聺隆盲禄露莽職聞猫聤聜莽聜鹿氓聢聶茅聹聙猫娄聛**莽聰篓where忙聢聳猫聙聟氓卤聻忙聙搂猫驴聡忙禄陇氓聶篓**茂录聦忙炉聰氓娄聜猫炉麓

* **cpg.method.name(芒聙聹getRequestBody芒聙聺).l**

忙聼楼猫炉垄氓聬聧氓颅聴盲赂潞getRequestBody茂录聦猫驴聶盲赂陋name氓掳卤忙聵炉氓卤聻忙聙搂猫驴聡忙禄陇氓聶篓茂录聦氓聬聭盲赂聥盲赂聙莽潞搂猫驴聰氓聸聻莽職聞忙聵炉莽卢娄氓聬聢氓卤聻忙聙搂猫驴聡忙禄陇氓聶篓莽職聞method猫聤聜莽聜鹿

* **cpg.method.where(\_.name(芒聙聹getRequestBody芒聙聺)).l**

忙聢聳猫聙聟莽聰篓where盲鹿聼猫隆聦茂录聦where猫炉颅氓聫楼氓聠聟氓庐鹿盲录職盲陆聹盲赂潞莽颅聸茅聙聣忙聺隆盲禄露氓陆卤氓聯聧猫驴聰氓聸聻莽職聞method氓聠聟氓庐鹿

* **cpg.method.name.l**

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` joern> cpg.method.name.l val res36: List[String] = List(   "configure",   "main", ... ``` |

氓娄聜忙聻聹盲赂聧忙聵炉盲陆驴莽聰篓()盲陆聹盲赂潞氓卤聻忙聙搂猫驴聡忙禄陇氓聶篓茂录聦茅聜拢盲鹿聢猫驴聰氓聸聻氓聠聟氓庐鹿氓掳卤盲录職莽聸麓忙聨楼氓聫聵忙聢聬name氓卤聻忙聙搂氓聢聴猫隆篓茫聙聜

氓陆聯莽聞露茅聶陇盲潞聠where盲禄楼氓陇聳茂录聦盲鹿聼忙聰炉忙聦聛氓戮聢氓陇職莽搂聧猫驴聡忙禄陇氓聶篓

* **where茂录聦whereNot茂录職莽颅聸茅聙聣猫驴聰氓聸聻盲赂潞莽漏潞忙聢聳猫聙聟茅聺聻莽漏潞莽職聞猫聤聜莽聜鹿**
* + cpg.method.where(\_.isExternal(false)).name.l
* **filter茂录聦filterNot茂录職莽颅聸茅聙聣猫驴聰氓聸聻盲赂潞True忙聢聳猫聙聟False莽職聞猫聤聜莽聜鹿**
* + cpg.method.filter(\_.isExternal == false).name.l
* **and茂录聦or茂录職氓陇職盲赂陋猫驴聡忙禄陇氓聶篓盲鹿聥茅聴麓莽職聞氓聟鲁莽鲁禄**

## 猫驴聰氓聸聻莽禄聯忙聻聹氓陇聞莽聬聠

氓聹篓氓陇聞莽聬聠莽禄聯忙聻聹猫驴聰氓聸聻莽職聞忙聴露氓聙聶盲鹿聼忙聹聣盲赂聙盲潞聸忙聳鹿氓录聫忙聰鹿氓聫聵猫驴聰氓聸聻莽職聞氓聠聟氓庐鹿茫聙聜盲赂聙猫聢卢忙聺楼猫炉麓忙聼楼猫炉垄莽禄聯忙聻聹盲录職忙聵炉**盲赂聙盲赂陋氓颅聴氓聟赂氓聢聴猫隆篓**茫聙聜

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` joern> cpg.method.name("getRequestBody").l val res64: List[io.shiftleft.codepropertygraph.generated.nodes.Method] = List(   Method(     id = 15337L,     astParentFullName = "<empty>",     astParentType = "<empty>",     code = "public static String getRequestBody(HttpServletRequest request) throws IOException",     columnNumber = Some(value = 5),     columnNumberEnd = Some(value = 5),     filename = "src\\main\\java\\org\\joychou\\util\\WebUtils.java",     fullName = "org.joychou.util.WebUtils.getRequestBody:<unresolvedSignature>(1)",     hash = None,     isExternal = false,     lineNumber = Some(value = 13),     lineNumberEnd = Some(value = 16),     name = "getRequestBody",     order = 1,     signature = "<unresolvedSignature>(1)"   ) ) ``` |

氓聫炉盲禄楼莽聰篓**map忙聺楼忙聰鹿氓聫聵猫驴聰氓聸聻莽職聞莽禄聯忙聻聞**茂录聦猫驴聶忙聵炉盲赂聙盲赂陋莽卤禄盲录录盲潞聨lambda莽職聞猫炉颅忙鲁聲茂录聦盲录職**茅聛聧氓聨聠氓聢聴猫隆篓莽職聞忙聣聙忙聹聣猫聤聜莽聜鹿莽聞露氓聬聨莽聰聼忙聢聬莽禄聯忙聻聹.**

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` joern> cpg.method.name("getRequestBody").map(n=>List(n.filename, n.lineNumber, n.fullName, n.code)).l val res66: List[List[String | Option[Integer]]] = List(   List(     "src\\main\\java\\org\\joychou\\util\\WebUtils.java",     Some(value = 13),     "org.joychou.util.WebUtils.getRequestBody:<unresolvedSignature>(1)",     "public static String getRequestBody(HttpServletRequest request) throws IOException"   ) ) ``` |

茅聶陇盲潞聠map盲禄楼氓陇聳茂录聦氓聫娄氓陇聳猫驴聵忙聹聣盲赂陇盲赂陋氓庐聻莽聰篓莽職聞

* **.clone茂录聦氓聢聸氓禄潞盲赂聙盲赂陋忙路卤氓陇聧氓聢露茂录聦忙聵炉氓聹篓氓聠聶忙炉聰猫戮聝氓陇聧忙聺聜莽職聞猫聞職忙聹卢忙聴露氓聙聶莽聰篓氓聢掳莽職聞**
* **.dedup茂录聦氓聢聴猫隆篓氓聠聟氓庐鹿氓聨禄茅...