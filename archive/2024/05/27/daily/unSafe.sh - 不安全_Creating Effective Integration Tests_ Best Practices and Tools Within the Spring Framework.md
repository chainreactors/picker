---
title: Creating Effective Integration Tests: Best Practices and Tools Within the Spring Framework
url: https://buaq.net/go-241647.html
source: unSafe.sh - 不安全
date: 2024-05-27
fetch_date: 2025-10-06T16:49:03.877995
---

# Creating Effective Integration Tests: Best Practices and Tools Within the Spring Framework

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/74ef389e2450748a891f1c8e98acf34e.jpg)

Creating Effective Integration Tests: Best Practices and Tools Within the Spring Framework

In modern software development, effective testing plays a key role in ensuring the reliability and s
*2024-5-26 23:0:14
Author: [hackernoon.com(查看原文)](/jump-241647.htm)
阅读量:4
收藏*

---

In modern software development, effective testing plays a key role in ensuring the reliability and stability of applications.

This article offers practical recommendations for writing integration tests, demonstrating how to focus on the specifications of interactions with external services, making the tests more readable and easier to maintain. The approach not only enhances the efficiency of testing but also promotes a better understanding of the integration processes within the application. Through the lens of specific examples, various strategies and tools - such as DSL wrappers, JsonAssert, and Pact - will be explored, offering the reader a comprehensive guide to improving the quality and visibility of integration tests.

The article presents examples of integration tests performed using the Spock Framework in Groovy to test HTTP interactions in Spring applications. At the same time, the main techniques and approaches suggested can be effectively applied to various types of interactions beyond HTTP.

## Problem Description

The article [Writing Effective Integration Tests in Spring: Organized Testing Strategies for HTTP Request Mocking](https://hackernoon.com/writing-effective-integration-tests-in-spring-organized-testing-strategies-for-http-request-mocking?ref=hackernoon.com) describes an approach to writing tests with a clear separation into distinct stages, each performing its specific role. Let's describe a test example according to these recommendations, but with mocking not one but two requests. The Act stage (Execution) will be omitted for brevity (a full test example can be found in the [project repository](https://github.com/avvero/spring-sandbox/blob/main/src/test/groovy/pw/avvero/spring/sandbox/bot/mock/FeatureGTests.groovy?ref=hackernoon.com)).

![](https://hackernoon.imgix.net/images/MQ5fUOiNSpXFtgak1Nkj9tyaEBL2-u2833xy.png?auto=format&fit=max&w=3840)

The presented code is conditionally divided into parts: "Supporting Code" (colored in gray) and "Specification of External Interactions" (colored in blue). The Supporting Code includes mechanisms and utilities for testing, including intercepting requests and emulating responses. The Specification of External Interactions describes specific data about external services that the system should interact with during the test, including expected requests and responses. The Supporting Code lays the foundation for testing, while the Specification directly relates to the business logic and main functions of the system that we are trying to test.

The Specification occupies a minor part of the code but represents significant value for understanding the test, whereas the Supporting Code, occupying a larger part, presents less value and is repetitive for each mock declaration. The code is intended for use with MockRestServiceServer. Referring to the [example on WireMock](https://github.com/avvero/spring-sandbox/blob/main/src/test/groovy/pw/avvero/spring/sandbox/bot/wiremock/FeatureWiremockGTests.groovy?ref=hackernoon.com), one can see the same pattern: the specification is almost identical, and the Supporting Code varies.

The aim of this article is to offer practical recommendations for writing tests in such a way that the focus is on the specification, and the Supporting Code takes a back seat.

## Demonstration Scenario

For our test scenario, I propose a hypothetical Telegram bot that forwards requests to the OpenAI API and sends responses back to users.

The contracts for interacting with services are described in a simplified manner to highlight the main logic of the operation. Below is a sequence diagram demonstrating the application architecture. I understand that the design might raise questions from a systems architecture perspective, but please approach this with understanding—the main goal here is to demonstrate an approach to enhancing visibility in tests.

![](https://hackernoon.imgix.net/images/MQ5fUOiNSpXFtgak1Nkj9tyaEBL2-x5933d0.png?auto=format&fit=max&w=2048)

## Proposal

This article discusses the following practical recommendations for writing tests:

* Use of DSL wrappers for working with mocks.
* Use of JsonAssert for result verification.
* Storing the specifications of external interactions in JSON files.
* Use of Pact files.

## Using DSL Wrappers for Mocking

Using a DSL wrapper allows for hiding the boilerplate mock code and provides a simple interface for working with the specification. It's important to emphasize that what's proposed is not a specific DSL but a general approach it implements. A corrected test example using DSL is presented below ([full test text](https://github.com/avvero/spring-sandbox/blob/main/src/test/groovy/pw/avvero/spring/sandbox/bot/mock/FeatureGTestsStep1.groovy?ref=hackernoon.com)).

```
setup:
def openaiRequestCaptor = restExpectation.openai.completions(withSuccess("{...}"))
def telegramRequestCaptor = restExpectation.telegram.sendMessage(withSuccess("{}"))
when:
...
then:
openaiRequestCaptor.times == 1
telegramRequestCaptor.times == 1
```

Where the method `restExpectation.openai.completions`, for example, is described as follows:

```
public interface OpenaiMock {

    /**
     * This method configures the mock request to the following URL: {@code https://api.openai.com/v1/chat/completions}
     */
    RequestCaptor completions(DefaultResponseCreator responseCreator);
}
```

Having a comment on the method allows, when hovering over the method name in the code editor, to get help, including seeing the URL that will be mocked.

In the proposed implementation, the declaration of the response from the mock is made using `ResponseCreator` instances, allowing for custom ones, such as:

```
public static ResponseCreator withResourceAccessException() {
    return (request) -> {
        throw new ResourceAccessException("Error");
    };
}
```

An example test for unsuccessful scenarios specifying a set of responses is shown below:

```
import static org.springframework.http.HttpStatus.FORBIDDEN

setup:
def openaiRequestCaptor = restExpectation.openai.completions(openaiResponse)
def telegramRequestCaptor = restExpectation.telegram.sendMessage(withSuccess("{}"))
when:
...
then:
openaiRequestCaptor.times == 1
telegramRequestCaptor.times == 0
where:
openaiResponse                | _
withResourceAccessException() | _
withStatus(FORBIDDEN)         | _
```

For WireMock, everything is the same, except the response formation is slightly different ([test code](https://github.com/avvero/spring-sandbox/blob/main/src/test/groovy/pw/avvero/spring/sandbox/bot/wiremock/FeatureWiremockGTestsStep1.groovy?ref=hackernoon.com), [response factory class code](https://github.com/avvero/spring-sandbox/blob/main/src/test/java/pw/avvero/spring/sandbox/bot/wiremock/CustomMockRestResponseCreators.java?ref=hackernoon.com)).

## Using the @Language("JSON") Annotation for Better IDE Integration

When implementing a DSL, it's possible to annotate method parameters with `@Language("JSON")` to enable language feature support for specific code snippets in IntelliJ IDEA. With JSON, for example, the editor will treat the string parameter as JSON code, enabling features such as syntax highlighting, auto-completion, error checking, navigation, and structure search. Here's an example of the annot...