---
title: Eat What You Kill :: Pre-authenticated Remote Code Execution in VMWare NSX Manager
url: https://srcincite.io/blog/2022/10/25/eat-what-you-kill-pre-authenticated-rce-in-vmware-nsx-manager.html
source: Source Incite
date: 2022-10-26
fetch_date: 2025-10-03T20:54:30.449162
---

# Eat What You Kill :: Pre-authenticated Remote Code Execution in VMWare NSX Manager

[![Source Incite](/assets/si.png)](/)

[About](/about/) [Blog](/blog/) [Advisories](/advisories/) [Exploits](/exploits/) [Research](/research/)

[Training](/training/)

[Syllabus](/training/syllabus/) [Prerequisites](/training/prerequisites/) [Challenge](/training/challenge/) [Schedule/Signup](/training/schedule-signup/) [Testimonials](/training/testimonials/) [Faq](/training/faq/)

[Contact](/contact/)

# Eat What You Kill :: Pre-authenticated Remote Code Execution in VMWare NSX Manager

Oct 25, 2022

![](/assets/images/eat-what-you-kill-pre-authenticated-remote-code-execution-in-vmware-nsx-manager/logo.png "NSX Manager")

> This blog post was authored by [Sina Kheirkhah](https://twitter.com/SinSinology). Sina is a past student of the [Full Stack Web Attack](/training/) class.

VMWare NSX Manager is vulnerable to a pre-authenticated remote code execution vulnerability and at the time of writing, ~~will not be patched due to [EOL](https://kb.vmware.com/s/article/2149616)~~ this was patched in [VMSA-2022-0027](https://www.vmware.com/security/advisories/VMSA-2022-0027.html). The following blog is a collaboration between myself and the [Steven Seeley](https://twitter.com/steventseeley) who has helped me tremendously along the way.

Before we begin with the vulnerability, let’s have an overview of `XStream`.

![](/assets/images/eat-what-you-kill-pre-authenticated-remote-code-execution-in-vmware-nsx-manager/xstream.png "XStream")

`XStream` is a set of concise and easy-to-use open-source class libraries for marshalling Java objects into XML or unmarshalling XML into Java objects. It is a two-way converter between Java objects and XML.

**Serialization:**

```
XStream XS = new XStream();
Person person = new Person();
person.setName("sinsinology");

System.out.println(XS.toXML(person));
```

```
<Person.Person>
  <Name>sinsinology</Name>
</Person.Person>
```

**Deserialization:**

```
XStream XS = new XStream();
Person imported = (Person) XS.fromXML(
                "<Person.Person>\n" +
                "  <Name>sinsinology</Name>\n" +
                "</Person.Person>\n");

System.out.println(imported.getName()); // sinsinology
```

XStream uses Java reflection to translate the Person type to and from XML.

XStream also understands the concept of Alias, this worth remembering

```
XStream XS = new XStream();
XS.alias("srcincite", Person.class);
Person imported = (Person) XS.fromXML(
                "<srcincite>\n" +
                "  <Name>mr_me</Name>\n" +
                "</srcincite>\n");

System.out.println(imported.getName()); // mr_me
```

In addition to user-defined types like *Person*, `XStream` recognizes core Java types out of the box. For example, `XStream` can read a *Map* from XML:

```
String xml = ""
    + "<map>"
    + "  <element>"
    + "    <string>foo</string>"
    + "    <int>10</int>"
    + "  </element>"
    + "</map>";
XStream xStream = new XStream();

Map<String, Integer> map = (Map<String, Integer>) xStream.fromXML(xml);
```

## What makes XStream Lovely

If you haven’t noticed so far with the *Person* example, `XStream` has an awesome feature and that is, when it unmarshalls an object, it doesn’t need the object to implement the `Serializable` interface. This is one of the core differences between marshallers and serializers. This greatly facilitates injection attacks increasing the number of ways which you can exploit `XStream`, not depending only on classes which implement `Serializable`.

There is a catch though. Assume you want to have the below payload unmarshalled:

```
new ProcessBuilder().command("calc").start();
```

You can instantiate the `ProcessBuilder` and set the command for it, but it’s not possible to invoke the `start` method because when marshalling the XML, `XStream` only invokes constructors and sets fields. Therefore, the attacker doesn’t have a straightforward way to invoke the arbitrary methods unless they are setters.

## Dynamic Proxies

Dynamic proxies are a design pattern in Java which provides a proxy for a certain object, and the proxy object controls the access to the real object. The proxy class is mainly responsible for **pre-processing** the message for the proxied class (real object), filtering the message, and then passing the message to the proxied class, and finally return the **post-processed** message. In a nutshell a proxy class will complete a call by calling the proxied class and encapsulating the execution result.

Accessing the target object through a Proxy is very powerful since you can redirect execution from an undesired method call to a targeted method call without modifying any code. Simply put, proxies are fronts or wrappers that pass function invocation through their own facilities (onto real methods) – potentially adding some functionality.

Great thing about dynamic proxy is it can pretend to be an implementation of any interface and **it routes all method invocations to a single handler which is the `invoke()` method**

Now proxies in java can get divided into static and dynamic but for now, we just need to know about the dynamic proxy. In order to start using dynamic proxies in Java we’ll need to implement the `InvocationHandler` interface. The class that implements `InvocationHandler` will contain the custom code which will do the **pre-processing** before proxying a call to the target object.

```
package src.incite;

import java.lang.reflect.Proxy;
import java.util.HashMap;
import java.util.Map;
import java.lang.reflect.*;

class ProxyHandler implements InvocationHandler {
    private Object obj;
    public ProxyHandler(Object obj) {
        this.obj = obj;
    }
    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        Object result = method.invoke(obj, args);
        System.out.println(String.format("[PROXY] The %s method got invoked", method.getName() ));
        return result;
    }
}

public class Test {
    public static void main(String[] args) throws Exception {
        @SuppressWarnings("unchecked")
        Map<String, Integer> colors = (Map<String, Integer>)Proxy.newProxyInstance(
                Test.class.getClassLoader(),
                new Class[] {Map.class},
                new ProxyHandler(new HashMap<>())
        );
        colors.put("one", 1);
        colors.put("two", 2);
        colors.put("three", 3);
    }
}
```

Output…

```
[PROXY] The put method got invoked
[PROXY] The put method got invoked
[PROXY] The put method got invoked
```

Let’s take a closer look at the `invoke` method signature:

```
invoke(Object proxy, Method method, Object[] args)
```

The three important parameters are:

* `proxy`: the object being proxied
* `method`: the method to call
* `args`: parameters in the method

Looking at our proxy you’ll soon realize we are doing the pre-processing but not the post-processing which in this case does not matter that much. We are only interested in getting our custom code to be executed but if you are interested to learn more about dynamic proxies I’ll highly recommend checking out [Baeldung](https://twitter.com/baeldung) post about [dynamic proxies](https://www.baeldung.com/java-dynamic-proxies).

## Java Event Handlers

The JDK provides a commonly-used `InvocationHandler` called `java.beans.EventHandler`. This class can be instantiated to invoke a defined method on another object when a particular method (or even ANY method) is invoked.

```
    public static <T> T create(Class<T> listenerInterface,
                               Object target, String action)
```

We know that arbitrary code can be executed by invoking the `start` method on a `ProcessBuilder` instance. Now that we can use `EventHandler` to redirect any receiving method invocation request to arbitrary method (in this case the `start` method of a `ProcessBuilder` instance). First though, we need to find a data type that will do a method invocation on our `EventHandler`.

Luckily Java has a interface named `Comparable...