---
title: JDK高版本特性总结与ZGC实践
url: https://tech.meituan.com/2025/06/20/jdk17-zgc.html
source: 美团技术团队
date: 2025-06-21
fetch_date: 2025-10-06T22:53:12.761683
---

# JDK高版本特性总结与ZGC实践

[莽戮聨氓聸垄忙聤聙忙聹炉氓聸垄茅聵聼](https://tech.meituan.com/ "莽戮聨氓聸垄忙聤聙忙聹炉氓聸垄茅聵聼")

* [忙聹聙忙聳掳忙聳聡莽芦聽](https://tech.meituan.com/ "忙聼楼莽聹聥忙聹聙忙聳掳忙聳聡莽芦聽")
* [忙聳聡莽芦聽氓颅聵忙隆拢](/archives "忙聼楼莽聹聥忙聳聡莽芦聽氓颅聵忙隆拢氓聠聟氓庐鹿")
* [忙聤聙忙聹炉忙虏聶茅戮聶](/tech-salon "盲潞聠猫搂拢忙聤聙忙聹炉忙虏聶茅戮聶")
* [氓聟鲁盲潞聨忙聢聭盲禄卢](/about "盲潞聠猫搂拢忙聸麓氓陇職氓聟鲁盲潞聨忙聢聭盲禄卢莽職聞盲潞聥忙聝聟")

脗漏 2023 莽戮聨氓聸垄忙聤聙忙聹炉氓聸垄茅聵聼

All rights reserved.

# [JDK茅芦聵莽聣聢忙聹卢莽聣鹿忙聙搂忙聙禄莽禄聯盲赂聨ZGC氓庐聻猫路碌](https://tech.meituan.com/2025/06/20/jdk17-zgc.html)

2025氓鹿麓06忙聹聢20忙聴楼
盲陆聹猫聙聟: 莽戮聨氓聸垄盲驴隆忙聛炉氓庐聣氓聟篓氓聸垄茅聵聼
[忙聳聡莽芦聽茅聯戮忙聨楼](https://tech.meituan.com/2025/06/20/jdk17-zgc.html)
20097氓颅聴
41氓聢聠茅聮聼茅聵聟猫炉禄

> 莽戮聨氓聸垄盲驴隆忙聛炉氓庐聣氓聟篓忙聤聙忙聹炉氓聸垄茅聵聼忙聽赂氓驴聝忙聹聧氓聤隆氓聧聡莽潞搂JDK 17氓聬聨茂录聦忙聙搂猫聝陆盲赂聨莽篓鲁氓庐職忙聙搂氓陇搂氓鹿聟忙聫聬氓聧聡茂录聦忙聹潞氓聶篓忙聢聬忙聹卢茅聶聧盲陆聨盲潞聠10%茫聙聜茅芦聵莽聣聢忙聹卢JDK盲赂聨ZGC忙聤聙忙聹炉盲禄陇盲潞潞忙聝聤猫聣鲁茂录聦盲赂聰Java AI SDK忙聹聙盲陆聨忙聰炉忙聦聛JDK 17茫聙聜忙聹卢忙聳聡忙聙禄莽禄聯盲潞聠JDK 17莽職聞盲赂禄猫娄聛莽聣鹿忙聙搂茂录聦莽聞露氓聬聨茅聡聧莽聜鹿氓聢聠盲潞芦盲潞聠JDK 17+ZGC氓聹篓氓庐聣氓聟篓茅垄聠氓聼聼莽職聞盲赂聙盲潞聸氓庐聻猫路碌茂录聦氓赂聦忙聹聸猫聝陆氓炉鹿氓陇搂氓庐露忙聹聣忙聣聙氓赂庐氓聤漏忙聢聳氓聬炉氓聫聭茫聙聜

盲禄聨盲赂聙氓聫楼猫掳聝盲戮聝莽職聞猫炉聺 芒聙聹盲陆聽氓聫聭盲禄禄盲陆聽氓聫聭茂录聦忙聢聭莽聰篓Java 8茂录聛芒聙聺 氓聫炉盲禄楼莽聹聥氓聡潞茂录聦氓聹篓氓录聙氓聫聭忙聳掳茅隆鹿莽聸庐忙聴露茂录聦Java 8盲戮聺莽聞露忙聵炉氓陇搂氓庐露莽職聞茅娄聳茅聙聣茫聙聜莽戮聨氓聸垄Java 8忙聹聧氓聤隆氓聧聽忙炉聰猫露聟猫驴聡70%茂录聦氓聫炉盲禄楼猫炉麓Java 8盲戮聺莽聞露忙聵炉莽禄聺氓炉鹿莽職聞盲赂禄忙碌聛茫聙聜盲陆聠忙聵炉茂录聦忙聢聭盲禄卢氓聹篓氓陇職盲赂陋忙聽赂氓驴聝忙聹聧氓聤隆盲赂聤茅聛聡氓聢掳猫戮聝氓陇職莽職聞忙聙搂猫聝陆茅聴庐茅垄聵茂录聦猫驴聶盲潞聸茅聴庐茅垄聵忙聴聽忙鲁聲茅聙職猫驴聡JVM氓聫聜忙聲掳氓戮庐猫掳聝忙聺楼猫搂拢氓聠鲁茂录聦盲赂潞忙颅陇忙聢聭盲禄卢氓炉鹿茅聝篓氓聢聠忙聽赂氓驴聝忙聹聧氓聤隆盲陆驴莽聰篓盲潞聠 JDK 17茂录聦氓聧聡莽潞搂氓聬聨忙聹聧氓聤隆忙聙搂猫聝陆氓聮聦莽篓鲁氓庐職忙聙搂忙聦聡忙聽聡盲鹿聼氓戮聴氓聢掳氓路篓氓陇搂莽職聞茅拢聻猫路聝茂录聦氓聬聦忙聴露忙聹潞氓聶篓忙聢聬忙聹卢氓聫炉盲禄楼盲赂聥茅聶聧莽潞娄10%茂录聦氓聧聡莽潞搂JDK莽聣聢忙聹卢忙聰露莽聸聤氓聧聛氓聢聠忙聵聨忙聵戮茫聙聜氓聫娄氓陇聳茂录聦莽聸庐氓聣聧忙颅拢氓陇聞氓聹篓AI忙聴露盲禄拢莽職聞莽聢聠氓聫聭忙聹聼茂录聦Java AI SDK莽職聞忙聹聙氓掳聫忙聰炉忙聦聛莽聣聢忙聹卢盲赂潞JDK 17茂录聦猫驴聶猫庐漏氓聧聡莽潞搂JDK莽聣聢忙聹卢氓聫聵氓戮聴忙聸麓氓聟路盲禄路氓聙录茫聙聜忙聨楼盲赂聥忙聺楼茂录聦忙聹聼忙聹聸猫路聼氓陇搂氓庐露盲赂聙猫碌路忙聨垄莽麓垄JDK茅芦聵莽聣聢忙聹卢氓聮聦ZGC忙聤聙忙聹炉莽職聞氓楼楼莽搂聵茂录聦氓录聙氓聬炉盲录聵氓聦聳Java氓潞聰莽聰篓莽職聞忙聳掳氓戮聛莽篓聥茫聙聜

## 1. JDK 17莽職聞盲赂禄猫娄聛莽聣鹿忙聙搂

> 氓聦聟氓聬芦JDK 9~17莽颅聣盲赂颅茅聴麓莽聣聢忙聹卢莽職聞莽聣鹿忙聙搂茫聙聜

盲禄聨 JDK 8 莽聸麓忙聨楼氓聧聡莽潞搂氓聢掳 JDK 17茂录聦盲禄楼盲赂聥忙聵炉茅聹聙猫娄聛茅聡聧莽聜鹿氓聟鲁忙鲁篓莽職聞莽聣鹿忙聙搂茂录聦猫驴聶盲潞聸莽聣鹿忙聙搂氓炉鹿氓录聙氓聫聭忙聲聢莽聨聡茫聙聛盲禄拢莽聽聛茅拢聨忙聽录茫聙聛忙聙搂猫聝陆盲录聵氓聦聳氓聮聦氓庐聣氓聟篓忙聙搂茅聝陆忙聹聣忙聵戮猫聭聴氓陆卤氓聯聧茫聙聜

### 1.1 猫炉颅猫篓聙莽聣鹿忙聙搂[1]

#### 1.1.1 氓卤聙茅聝篓氓聫聵茅聡聫莽卤禄氓聻聥忙聨篓忙聳颅

盲陆驴莽聰篓var氓聟鲁茅聰庐氓颅聴忙聺楼氓拢掳忙聵聨氓卤聙茅聝篓氓聫聵茅聡聫茂录聦猫聙聦忙聴聽茅聹聙忙聵戮氓录聫忙聦聡氓庐職氓聫聵茅聡聫莽職聞莽卤禄氓聻聥茫聙聜氓聹篓Java 17盲赂颅茂录聦氓聫炉盲禄楼盲陆驴莽聰篓氓卤聙茅聝篓氓聫聵茅聡聫莽卤禄氓聻聥忙聨篓忙聳颅莽職聞忙聣漏氓卤聲忙聺楼莽录聳氓聠聶忙聸麓莽庐聙忙麓聛莽職聞盲禄拢莽聽聛茫聙聜氓聟露盲禄聳猫炉颅猫篓聙氓娄聜Golang氓戮聢忙聴漏氓掳卤忙聰炉忙聦聛盲潞聠var氓聫聵茅聡聫茫聙聜

```
// JDK8
String str = "Hello world";

// JDK17
var str = "Hello world";
```

> 茅聹聙猫娄聛忙鲁篓忙聞聫莽職聞忙聵炉茂录聦var莽卤禄氓聻聥莽職聞氓卤聙茅聝篓氓聫聵茅聡聫盲禄聧莽聞露氓聟路忙聹聣茅聺聶忙聙聛莽卤禄氓聻聥茂录聦盲赂聙忙聴娄猫垄芦忙聨篓忙聳颅氓聡潞忙聺楼茂录聦莽卤禄氓聻聥氓掳卤盲录職氓聸潞氓庐職盲赂聥忙聺楼茂录聦氓鹿露盲赂聰盲赂聧猫聝陆茅聡聧忙聳掳猫碌聥氓聙录盲赂潞盲赂聧氓聟录氓庐鹿莽職聞莽卤禄氓聻聥茫聙聜

#### 1.1.2 氓炉聠氓掳聛莽卤禄

氓庐聝氓聟聛猫庐赂忙聢聭盲禄卢氓掳聠莽卤禄忙聢聳忙聨楼氓聫拢莽職聞莽禄搂忙聣驴茅聶聬氓聢露盲赂潞盲赂聙莽禄聞忙聹聣茅聶聬莽職聞氓颅聬莽卤禄茫聙聜氓娄聜忙聻聹忙聝鲁氓掳聠莽卤禄忙聢聳忙聨楼氓聫拢莽職聞莽禄搂忙聣驴茅聶聬氓聢露盲赂潞盲赂聙莽禄聞忙聹聣茅聶聬莽職聞氓颅聬莽卤禄忙聴露茂录聦猫驴聶茅聺聻氓赂赂忙聹聣莽聰篓茫聙聜氓聹篓盲赂聥茅聺垄莽職聞莽陇潞盲戮聥盲赂颅茂录聦氓聫炉盲禄楼莽聹聥氓聢掳忙聢聭盲禄卢氓娄聜盲陆聲盲陆驴莽聰篓sealed氓聟鲁茅聰庐氓颅聴氓掳聠莽卤禄莽職聞莽禄搂忙聣驴茅聶聬氓聢露盲赂潞盲赂聙莽禄聞忙聹聣茅聶聬莽職聞氓颅聬莽卤禄茫聙聜忙聢聭盲禄卢氓聫炉盲禄楼茅聙職猫驴聡氓聹篓莽卤禄莽職聞氓拢掳忙聵聨氓聣聧氓聤聽盲赂聤sealed氓聟鲁茅聰庐氓颅聴忙聺楼氓掳聠猫炉楼莽卤禄氓拢掳忙聵聨盲赂潞氓炉聠氓掳聛莽卤禄茫聙聜莽聞露氓聬聨茂录聦氓聫炉盲禄楼盲陆驴莽聰篓permits氓聟鲁茅聰庐氓颅聴氓聢聴氓聡潞猫炉楼氓炉聠氓掳聛莽卤禄氓聟聛猫庐赂莽禄搂忙聣驴莽職聞氓颅聬莽卤禄茫聙聜猫驴聶盲潞聸氓颅聬莽卤禄氓驴聟茅隆禄莽聸麓忙聨楼忙聢聳茅聴麓忙聨楼氓聹掳莽禄搂忙聣驴猫聡陋氓炉聠氓掳聛莽卤禄茫聙聜猫驴聶忙聽路茂录聦氓聫陋忙聹聣氓聹篓猫驴聶盲赂陋茅垄聞氓庐職盲鹿聣莽職聞氓颅聬莽卤禄盲赂颅茂录聦忙聣聧猫聝陆莽禄搂忙聣驴猫炉楼氓炉聠氓掳聛莽卤禄茫聙聜

```
//盲陆驴莽聰篓permits氓聟鲁茅聰庐氓颅聴氓聢聴氓聡潞盲潞聠氓聟聛猫庐赂莽禄搂忙聣驴莽職聞氓颅聬莽卤禄Circle茫聙聛Rectangle氓聮聦Triangle
public sealed class Shape permits Circle, Rectangle, Triangle {
    // 莽聹聛莽聲楼氓庐聻莽聨掳
}

// 氓聹篓盲赂聨氓炉聠氓掳聛莽卤禄莽聸赂氓聬聦莽職聞忙篓隆氓聺聴忙聢聳氓聦聟盲赂颅 氓庐職盲鹿聣盲禄楼盲赂聥盲赂聣盲赂陋氓聟聛猫庐赂莽職聞氓颅聬莽卤禄茂录聦 Circle茂录聦Square氓聮聦茂录職Rectangle
public final class Circle extends Shape {
    public float radius;
}

public non-sealed class Square extends Shape {
   public double side;
}

public sealed class Rectangle extends Shape permits FilledRectangle {
    public double length, width;
}
```

#### 1.1.3 Record 莽卤禄

Record 莽卤禄莽職聞盲赂禄猫娄聛莽聸庐莽職聞忙聵炉忙聫聬盲戮聸盲赂聙莽搂聧忙聸麓莽庐聙忙麓聛茫聙聛忙聸麓氓庐聣氓聟篓莽職聞忙聳鹿氓录聫忙聺楼氓庐職盲鹿聣盲赂聧氓聫炉氓聫聵莽職聞忙聲掳忙聧庐猫陆陆盲陆聯莽卤禄茫聙聜氓庐聝猫聡陋氓聤篓氓庐聻莽聨掳盲潞聠氓赂赂猫搂聛莽職聞忙聳鹿忙鲁聲茂录聢氓娄聜`equals()`茫聙聛`hashCode()`茫聙聛`toString()`氓聮聦忙聻聞茅聙聽氓聡陆忙聲掳茂录聣茂录聦盲禄聨猫聙聦氓聡聫氓掳聭盲潞聠忙聽路忙聺驴盲禄拢莽聽聛茫聙聜

**莽聣鹿莽聜鹿**

1. **盲赂聧氓聫炉氓聫聵忙聙搂**茂录職Record莽卤禄莽職聞氓颅聴忙庐碌茅禄聵猫庐陇忙聵炉`final`莽職聞茂录聦氓聸聽忙颅陇 Record 莽卤禄忙聵炉盲赂聧氓聫炉氓聫聵莽職聞茫聙聜
2. **莽庐聙忙麓聛忙聙搂**茂录職Record莽卤禄猫聡陋氓聤篓忙聫聬盲戮聸盲潞聠忙聻聞茅聙聽氓聡陆忙聲掳茫聙聛`equals()`茫聙聛`hashCode()`氓聮聦`toString()`忙聳鹿忙鲁聲茂录聦忙聴聽茅聹聙忙聣聥氓聤篓莽录聳氓聠聶茫聙聜
3. **莽禄聞盲禄露猫庐驴茅聴庐**茂录職Record莽卤禄莽職聞氓颅聴忙庐碌氓聫炉盲禄楼茅聙職猫驴聡`recordName.fieldName`莽職聞忙聳鹿氓录聫莽聸麓忙聨楼猫庐驴茅聴庐茫聙聜
4. **忙篓隆氓录聫氓聦鹿茅聟聧**茂录職Record莽卤禄忙聰炉忙聦聛忙篓隆氓录聫氓聦鹿茅聟聧茂录聢Pattern Matching茂录聣茂录聦氓聫炉盲禄楼盲赂聨`instanceof`氓聮聦`switch`猫隆篓猫戮戮氓录聫莽禄聯氓聬聢盲陆驴莽聰篓茫聙聜

Record莽卤禄莽職聞氓庐職盲鹿聣茅聺聻氓赂赂莽庐聙氓聧聲茂录聦氓聫陋茅聹聙猫娄聛盲陆驴莽聰篓`record`氓聟鲁茅聰庐氓颅聴茂录聦氓鹿露氓拢掳忙聵聨氓颅聴忙庐碌莽卤禄氓聻聥氓聮聦氓聬聧莽搂掳氓聧鲁氓聫炉茫聙聜盲戮聥氓娄聜茂录職

```
// 猫驴聶茅聡聦忙聹聣盲赂聙盲赂陋氓聦聟氓聬芦盲赂陇盲赂陋氓颅聴忙庐碌莽職聞猫庐掳氓陆聲莽卤禄
record Rectangle(double length, double width) { }

// 猫驴聶盲赂陋莽庐聙忙麓聛莽職聞莽聼漏氓陆垄氓拢掳忙聵聨莽颅聣氓聬聦盲潞聨盲禄楼盲赂聥忙聶庐茅聙職莽卤禄
public final class Rectangle {
    private final double length;
    private final double width;

    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    double length() { return this.length; }
    double width()  { return this.width; }

    // ...
    public boolean equals...
    public int hashCode...

    // ...
    public String toString() {...}
}
```

#### 1.1.4 switch猫隆篓猫戮戮氓录聫盲录聵氓聦聳

氓聹篓Java 17盲赂颅盲陆驴莽聰篓switch猫隆篓猫戮戮氓录聫忙聴露茂录聦盲赂聧氓驴聟盲陆驴莽聰篓氓聟鲁茅聰庐氓颅聴break忙聺楼猫路鲁氓聡潞switch猫炉颅氓聫楼茂录聦忙聢聳return氓聹篓忙炉聫盲赂陋switch case盲赂聤盲陆驴莽聰篓氓聟鲁茅聰庐氓颅聴忙聺楼猫驴聰氓聸聻氓聙录茂录聸莽聸赂氓聫聧茂录聦忙聢聭盲禄卢氓聫炉盲禄楼猫驴聰氓聸聻忙聲麓盲赂陋switch猫隆篓猫戮戮氓录聫茫聙聜猫驴聶莽搂聧氓垄聻氓录潞莽職聞switch猫隆篓猫戮戮氓录聫盲陆驴忙聲麓盲陆聯盲禄拢莽聽聛莽聹聥猫碌路忙聺楼忙聸麓忙赂聟忙聶掳茂录聦忙聸麓忙聵聯盲潞聨茅聵聟猫炉禄茫聙聜switch忙聣聯氓聧掳盲赂聙氓聭篓盲赂颅忙聼聬盲赂聙氓陇漏莽職聞氓颅聴忙炉聧忙聲掳茅聡聫莽職聞猫炉颅氓聫楼茫聙聜

**JDK 8**

```
public enum Day { SUNDAY, MONDAY, TUESDAY,
    WEDNESDAY, THURSDAY, FRIDAY, SATURDAY; }

		// ...

    int numLetters = 0;
    Day day = Day.WEDNESDAY;
    switch (day) {
        case MONDAY:
        case FRIDAY:
        case SUNDAY:
            numLetters = 6;
            break;
        case TUESDAY:
            numLetters = 7;
            break;
        case THURSDAY:
        case SATURDAY:
            numLetters = 8;
            break;
        case WEDNESDAY:
            numLetters = 9;
            break;
        default:
            throw new IllegalStateException("Invalid day: " + day);
    }
    System.out.println(numLetters);
```

**JDK 17**

```
		Day day = Day.WEDNESDAY;
    System.out.println(
        switch (day) {
            case MONDAY, FRIDAY, SUNDAY -> 6;
            case TUESDAY                -> 7;
            case THURSDAY, SATURDAY     -> 8;
            case WEDNESDAY              -> 9;
            default -> throw new IllegalStateException("Invalid day: " + day);
        }
    );
```

#### 1.1.5 忙聳聡忙聹卢氓聺聴

氓聹篓盲赂聧盲陆驴莽聰篓猫陆卢盲鹿聣氓潞聫氓聢聴莽職聞忙聝聟氓聠碌盲赂聥氓聢聸氓禄潞氓陇職猫隆聦氓颅聴莽卢娄盲赂虏茫聙聜氓聹篓氓聢聸氓禄潞SQL忙聼楼猫炉垄忙聢聳JSON氓颅聴莽卢娄盲赂虏忙聴露茅聺聻氓赂赂忙聹聣莽聰篓茫聙聜氓聹篓盲赂聥茅聺垄莽職聞莽陇潞盲戮聥盲赂颅茂录聦氓聫炉盲禄楼莽聹聥氓聢掳盲陆驴莽聰篓忙聳聡忙聹卢氓聺聴忙聴露盲禄拢莽聽聛莽聹聥猫碌路忙聺楼忙聸麓氓聤聽莽庐聙忙麓聛茫聙聜

```
// JDK8
String message = "'The time has come,' the Walrus said,\n" +
                 "'To talk of many things:\n" +
                 "Of shoes -- and ships -- and sealing-wax --\n" +
                 "Of cabbages -- and kings --\n" +
                 "And why the sea is boiling hot --\n" +
                 "And whether pigs have wings.'\n";

// 盲陆驴莽聰篓忙聳聡忙聹卢氓聺聴氓聫炉盲禄楼忙露聢茅聶陇氓陇搂茅聝篓氓聢聠忙路路盲鹿卤茂录職
String message = """
    'The time has come,' the Walrus said,
    'To talk of many things:
    Of shoes -- and ships -- and sealing-wax --
    Of cabbages -- and kings --
    And why the sea is boiling hot --
    And whether pigs have wings.'
    """;
```

**SQL忙鲁篓猫搂拢忙聫聫猫驴掳**

```
// JDK8
@Select("select distinct ta.host_name from tb_agent_info tai, tb_agent ta where 1=1 " +
        "and ta.host_name=tai.host_name and ta.status=1 and ta.master=1 and tai.report_pid_count > 0")
Set<String> queryAllJavaHost();

// JDK17
@Select("""
    SELECT DISTINCT ta.host_name
    FROM tb_agent_info tai, tb_agent ta
    WHERE 1=1
      AND ta.host_name = tai.host_name
      AND ta.status = 1
      AND ta.master = 1
      AND tai.report_pid_count > 0
 """)
 Set<String> queryAllJavaHost2();
```

* **氓聫炉猫炉禄忙聙搂忙聸麓氓录潞**茂录職忙聳聡忙聹卢莽禄聯忙聻聞忙赂聟忙聶掳氓聫炉猫搂聛茂录聦忙聴聽茅聹聙氓陇聞莽聬聠猫陆卢盲鹿聣氓颅聴莽卢娄忙聢聳氓颅聴莽卢娄盲赂虏猫驴聻忙聨楼茫聙聜
* **氓聡聫氓掳聭茅聰聶猫炉炉**...