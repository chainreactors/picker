---
title: Java 17 – Best Practices and features
url: https://blogs.sap.com/2023/07/26/java-17-best-practices-and-features/
source: SAP Blogs
date: 2023-07-27
fetch_date: 2025-10-04T11:54:03.988670
---

# Java 17 – Best Practices and features

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Java 17 - Best Practices and features

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163189&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Java 17 - Best Practices and features](/t5/technology-blog-posts-by-sap/java-17-best-practices-and-features/ba-p/13566274)

![dhiraj_jaiswal](https://avatars.profile.sap.com/9/4/id94676cf38697a7bd4f7ea53e5011f83cafa1b731f6f4f7570d8695283d3807eb_small.jpeg "dhiraj_jaiswal")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[dhiraj\_jaiswal](https://community.sap.com/t5/user/viewprofilepage/user-id/13446)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163189)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163189)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566274)

‎2023 Jul 27
12:56 AM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163189/tab/all-users "Click here to see who gave kudos to this post.")

4,694

* SAP Managed Tags
* [Java](https://community.sap.com/t5/c-khhcw49343/Java/pd-p/615693459582413452469752593601406)
* [development tools for SAP BTP, Neo environment](https://community.sap.com/t5/c-khhcw49343/development%2520tools%2520for%2520SAP%2520BTP%252C%2520Neo%2520environment/pd-p/67838200100800004383)
* [Cloud](https://community.sap.com/t5/c-khhcw49343/Cloud/pd-p/431932400353955532628433796433200)

* [development tools for SAP BTP, Neo environment

  SAP Business Technology Platform](/t5/c-khhcw49343/development%2Btools%2Bfor%2BSAP%2BBTP%25252C%2BNeo%2Benvironment/pd-p/67838200100800004383)
* [Cloud

  Topic](/t5/c-khhcw49343/Cloud/pd-p/431932400353955532628433796433200)
* [Java

  Programming Tool](/t5/c-khhcw49343/Java/pd-p/615693459582413452469752593601406)

View products (3)

**Introduction**: The goal of OpenJdk organisation is to develop updates for the Java Development Kit (JDK) Project. This blog compiles all the major feature changes that were introduced between Java 11 to Java 17. As Java 17 will have LTS support, migrating existing application to java 17 make application secure and reduces vulnerability. Therefore it is important and beneficial for developer to use latest features of java 17 while coding as part of best practices and it also improves developer experience. Top features are discussed below:

* [Text Blocks](#text-blocks)

* [Switch Expressions](#switch-expressions)

* [Stream.toList()](#streamtolist)

* [Records](#records)

* [Sealed Classes](#sealed-classes)

* [Pattern matching for instanceof](#pattern-matching-for-instanceof)

* [Other remarkable features:](#other-remarkable-features)

* [Reference](#reference)

## Text Blocks

In java 17, we can add multi line string in Java now using `"""` triple quotes.It facilitates the preservation of indents and multiple lines without adding white spaces in quotes

Example

```
private static void jsonBlock() {

String text = """

{

"name": "Dhiraj Jaiswal",

"job": "Software developer"

}

""";

System.out.println(text);

}
```

No need for escaping the double quotes and it looks just like it will be printed.

## Switch Expressions

Switch Expressions will allow you to return values from the switch and use these return values in assignments, etc. a new switch...case statement has been introduced in a less verbose form.

Example

```
private static void withYield(Fruit fruit) {

String text = switch (fruit) {

case MANGO, BANANA -> {

System.out.println("the given fruit was: " + fruit);

yield "Common fruit";

}

case ORANGE, APPLE -> "Exotic fruit";

default -> "Undefined fruit";

};

System.out.println(text);

}
```

## New Stream.toList() method

Previously in order to convert a Stream to a List, you need to call the collect method with Collectors.toList(). Now we have stream.toList() method.

```
Stream<String> stringStream = Stream.of("a", "b", "c");

List<String> stringList = stringStream.toList();
```

## Records

Records will allow you to create immutable data classes. No need to use lombok libraries for constructor, getters, hashCode, equals and toString etc. The resulted classes are immutable data-only classes, so there are no setters. It is possible to add a static method to record, and constructors. Record cannot extend

another class because it already extends java.lang.Record, but it can implement another interface.

```
public record Human(String name, float height, Gender gender) {

}

public class RecordDemo {

public static void main(String... args) {

Human dhiraj = new Human("Dhiraj Jaiswal", 1.9f, Gender.MALE);

System.out.println("Dhiraj as string: " + dhiraj);

System.out.println("Dhiraj's hashCode: " + dhiraj.hashCode());

System.out.println("Dhiraj's name: " + dhiraj.name());

}

}​
```

## Sealed Classes

Provide access the super class only to specific packages.

Example: The only thing to do is to add the sealed keyword to the Fruit class and indicate with the permits keyword which classes may extend this Sealed Class. The subclasses need to indicate whether they are final, sealed or non-sealed. The super class cannot control whether a subclass may be extended and how it may be extended. In support sealed classes, the Java Reflections API in Java 17 has two new methods,

isSealed() and getPermittedSubclasses().

```
public abstract sealed class FruitSealed permits AppleSealed, PearSealed {

}

public non-sealed class AppleSealed extends FruitSealed {

}

public final class PearSealed extends FruitSealed {

}
```

The sealed interface integrates well with record because record is final and can be

listed as a permittable implementation.

## Pattern matching for instanceof

It is possible to create the variable in the instanceof check and the extra line for creating a new variable and casting the object, is not necessary anymore.

```
private static void patternMatching() {

     Object o = new GrapeClass(Color.BLUE, 2);

     if (o instanceof GrapeClass grape) {

         System.out.println("This grape has " + grape.getNbrOfPits() + " pits.");

     }

}
```

## Other remarkable features:

* Helpful NullPointerExceptions. It shows exactly where the NullPointerException occured.

* Compact number formattiing support. (1k,1M etc)

* Day Period Support Added. (Ex: in the morning etc)

* Context-Specific Deserialization Filters.

* Enhanced Pseudo-Random Number Generators.

* Vector API and Foreign function.

* The Z Garbage Collector (ZGC) is no longer an experimental feature. Enable ZGC by using the command-line option XX:+UseZGC.

* JavaDoc can now generate a page summarizing the recent changes in an API.

## Reference

1. Java\_17\_for\_Absolute\_Beginners, more java 17 : an in-depth exploration of the java language and its features

2. Learn Java 17 Programming Second Edition

3. <https://www.baeldung.com/java-17-new-features>

4. [https://wiki.openjdk.org/display/JDKUpdates/JDK+17u](https://wiki.openjdk.org/display/JDKUpdates/JDK%2B17u)

Please share your thoughts about this blog in the comment section.

Please follow my dhira...