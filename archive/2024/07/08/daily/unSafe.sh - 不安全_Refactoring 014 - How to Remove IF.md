---
title: Refactoring 014 - How to Remove IF
url: https://buaq.net/go-249223.html
source: unSafe.sh - 不安全
date: 2024-07-08
fetch_date: 2025-10-06T17:40:47.575750
---

# Refactoring 014 - How to Remove IF

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

![]()

Refactoring 014 - How to Remove IF

The first instruction you learned should be the least you use.TL;DR: Remove all your Accidental IF
*2024-7-7 22:0:17
Author: [hackernoon.com(查看原文)](/jump-249223.htm)
阅读量:10
收藏*

---

*The first instruction you learned should be the least you use.*

> TL;DR: Remove all your Accidental IF-sentences

## Problems Addressed

* Code Duplication

* Possible Typos and defects

[Code Smell 07 - Boolean Variables](https://hackernoon.com/how-to-find-the-stinky-parts-of-your-code-part-ii-o96s3wl4?ref=hackernoon.com)

[Code Smell 36 - Switch/case/elseif/else/if statements](https://hackernoon.com/how-to-find-the-stinky-parts-of-your-code-part-viii-8mn3352?ref=hackernoon.com)

[Code Smell 133 - Hardcoded IF Conditions](https://hackernoon.com/how-to-find-the-stinky-parts-of-your-code-part-xxvii?ref=hackernoon.com)

[Code Smell 156 - Implicit Else](https://hackernoon.com/how-to-find-the-stinky-parts-of-your-code-part-xxxii?ref=hackernoon.com)

[Code Smell 119 - Stairs Code](https://hackernoon.com/how-to-find-the-stinky-parts-of-your-code-part-xxiv?ref=hackernoon.com)

[Code Smell 145 - Short Circuit Hack](https://hackernoon.com/how-to-find-the-stinky-parts-of-your-code-part-xxix?ref=hackernoon.com)

[Code Smell 101 - Comparison Against Booleans](https://hackernoon.com/how-to-find-the-stinky-parts-of-your-code-part-xxi?ref=hackernoon.com)

[Code Smell 45 - Not Polymorphic](https://hackernoon.com/how-to-find-the-stinky-parts-of-your-code-part-ix-7rr33ol?ref=hackernoon.com)

## Steps

1. Find or Create a Polymorphic Hierarchy.
2. Move the Body of Each IF to the Corresponding Abstraction.
3. Name the Abstractions.
4. Name the Method.
5. Replace if Statements with Polymorphic Message Sends.

## Sample Code

## Before

```
public String handleMicrophoneState(String state) {
    if (state.equals("off")) {
        return "Microphone is off";
    } else {
        return "Microphone is on";
    }
}

/* The constant representing the 'off' state is
duplicated throughout the code,
increasing the risk of typos and spelling mistakes.
The "else" condition doesn't explicitly check for the 'on' state;
it implicitly handles any state that is 'not off'.
This approach leads to repetition of the IF condition
wherever the state needs handling,
exposing internal representation and violating encapsulation.
The algorithm is not open for extension and closed for modification,
meaning that adding a new state
will require changes in multiple places in the code. */
```

## After

```
// Step 1: Find or Create a Polymorphic Hierarchy

abstract class MicrophoneState { }
final class On extends MicrophoneState { }
final class Off extends MicrophoneState { }

// Step 2: Move the Body of Each IF to the Corresponding Abstraction

abstract class MicrophoneState {
    public abstract String polymorphicMethodFromIf();
}

final class On extends MicrophoneState {
    @Override
    public String polymorphicMethodFromIf() {
        return "Microphone is on";
    }
}

final class Off extends MicrophoneState {
    @Override
    public String polymorphicMethodFromIf() {
        return "Microphone is off";
    }
}

// Step 3: Name the Abstractions

abstract class MicrophoneState {}
final class MicrophoneStateOn extends MicrophoneState {}
final class MicrophoneStateOff extends MicrophoneState {}

// Step 4: Name the Method

abstract class MicrophoneState {
   public abstract String handle();
}

final class MicrophoneStateOn extends MicrophoneState {
    @Override
    String handle() {
        return "Microphone is on";
    }
}

final class MicrophoneStateOff extends MicrophoneState {
    @Override
    String handle() {
        return "Microphone is off";
    }
}

// Step 5: Replace if Statements with Polymorphic Message Sends

 public String handleMicrophoneState(String state) {
        Map<String, MicrophoneState> states = new HashMap<>();
        states.put("muted", new Muted());
        states.put("recording", new Recording());
        states.put("idle", new Idle());

        MicrophoneState microphoneState =
            states.getOrDefault(state, new NullMicrophoneState());
        return microphoneState.handle();
    }
```

## Type

* [x]Semi-Automatic

## Safety

Most steps are mechanic. This is a pretty safe refactoring.

## Why is the code better?

The refactored code follows the open/closed principle and favors polymorphism instead of using IFs.

## Limitations

You should only apply it to **[Accidental IFs](https://hackernoon.com/how-to-get-rid-of-annoying-ifs-forever-zuh3zlo?ref=hackernoon.com)**.

Leave the business rules as **"domain ifs,"** and don't apply this refactoring.

* IFs

## See Also

---

文章来源: https://hackernoon.com/refactoring-014-how-to-remove-if?source=rss
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)