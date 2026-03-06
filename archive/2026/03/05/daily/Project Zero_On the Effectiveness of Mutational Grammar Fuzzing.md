---
title: On the Effectiveness of Mutational Grammar Fuzzing
url: https://projectzero.google/2026/03/mutational-grammar-fuzzing.html
source: Project Zero
date: 2026-03-05
fetch_date: 2026-03-06T04:05:01.816290
---

# On the Effectiveness of Mutational Grammar Fuzzing

[Project Zero](/)

---

[ ]

* [blog archive](/archive.html)
* [bug reports](https://project-zero.issues.chromium.org/savedsearches/7162405)
* [about](/about-pz.html)
* [Working at PZ](/working-at-project-zero.html)
* [0day: spreadsheet](/0day.html)
* [0day: Root Cause Analyses](https://googleprojectzero.github.io/0days-in-the-wild/rca.html)
* [vulnerability disclosure policy](/vulnerability-disclosure-policy.html)
* [reporting transparency](/reporting-transparency.html)
* search

# On the Effectiveness of Mutational Grammar Fuzzing

[2026-Mar-05](/2026/03/mutational-grammar-fuzzing.html "Permalink to this post")
Ivan Fratric

Mutational grammar fuzzing is a fuzzing technique in which the fuzzer uses a predefined grammar that describes the structure of the samples. When a sample gets mutated, the mutations happen in such a way that any resulting samples still adhere to the grammar rules, thus the structure of the samples gets maintained by the mutation process. In case of coverage-guided grammar fuzzing, if the resulting sample (after the mutation) triggers previously unseen code coverage, this sample is saved to the sample corpus and used as a basis for future mutations.

This technique has proven capable of finding complex issues and I have used it successfully in the past, including to find issues in [XSLT implementations in web browsers](https://www.youtube.com/watch?v=U1kc7fcF5Ao) and even [JIT engine bugs](https://projectzero.google/2021/09/fuzzing-closed-source-javascript.html).

However, despite the approach being effective, it is not without its flaws which, for a casual fuzzer user, might not be obvious. In this blogpost I will introduce what I perceive to be the flaws of the mutational coverage-guided grammar fuzzing approach. I will also describe a very simple but effective technique I use in my fuzzing runs to counter these flaws.

Please note that while this blogpost focuses on grammar fuzzing, the issues discussed here are not limited to grammar fuzzing as they also affect other structure-aware fuzzing techniques to various degrees. This research is based on the grammar fuzzing implementation in my [Jackalope fuzzer](https://github.com/googleprojectzero/Jackalope), but the issues are not implementation specific.

## Issue #1: More coverage does not mean more bugs

The fact that coverage is not a great measure for finding bugs is well known and affects coverage-guided fuzzing in general, not just grammar fuzzing. However this tends to be more problematic for the types of targets where structure-aware fuzzing (including grammar fuzzing) is typically used, such as in language fuzzing. Letâs demonstrate this on an example:

In language fuzzing, bugs often require functions to be called in a certain order or that a result of one function is used as an input to another function. To trigger [a recent bug in libxslt](https://project-zero.issues.chromium.org/issues/409761909) two XPath functions need to be called, the document() function and the generate-id() function, where the result of the document() function is used as an input to generate-id() function. There are other requirements to trigger the bug, but for now letâs focus on this requirement.

Hereâs a somewhat minimal sample required to trigger the bug:

```
<?xml version="1.0"?>
<xsl:stylesheet xml:base="#" version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
  <xsl:value-of select="generate-id(document('')/xsl:stylesheet/xsl:template/xsl:message)" />
  <xsl:message terminate="no"></xsl:message>
</xsl:template>
</xsl:stylesheet>
```

With the most relevant part for this discussion being the following element and the XPath expression in the select attribute:

```
<xsl:value-of select="generate-id(document('')/xsl:stylesheet/xsl:template/xsl:message)" />
```

If you run a mutational, coverage guided fuzzer capable of generating XSLT stylesheets, what it might do is generate two separate samples containing the following snippets:

*Sample 1:*

```
<xsl:value-of select="document('')/xsl:stylesheet/xsl:template/xsl:message" />
```

*Sample 2:*

```
<xsl:value-of select="generate-id(/a)" />
```

The union of these two samplesâ coverage is going to be the same as the coverage of the buggy sample, however having document() and generate-id() in two different samples in the corpus isnât really helpful for triggering the bug.

It is also possible for the fuzzer to generate a single sample with both of these functions that again results in the same coverage as the buggy sample, but with both functions operating on independent data:

```
<xsl:template match="/">
...
<xsl:value-of select="document('')/xsl:stylesheet/xsl:template/xsl:message" />
<xsl:value-of select="generate-id(/a)" />
...
</xsl:template>
```

This issue also demonstrates how crucial it is for any fuzzer to be able to combine multiple samples in the corpus in order to produce new samples. However, in this case, note that combining the two samples wouldnât trigger any previously unseen coverage and thus the resulting sample wouldnât be saved, despite climbing closer to triggering the bug.

In this case, because triggering the bug requires chaining only two function calls, a fuzzer would eventually find this bug by randomly combining the samples. But in case three or more function calls need to be chained in order to trigger the bug, it becomes increasingly expensive to do so and coverage feedback, as demonstrated, does not really help.

In fact, triggering this bug might be easier (or equally easy) with a generative fuzzer (that will generate a new sample from scratch every time) without coverage feedback. But even though coverage feedback is not ideal, it still helps in a lot of cases.

As previously stated, this issue does not only affect grammar fuzzing, but also other fuzzing approaches, in particular those focused on language fuzzing. For example, [Fuzzilli documentation](https://github.com/googleprojectzero/fuzzilli/blob/main/Docs/HowFuzzilliWorks.md#limitations-of-the-mutation-engine) describes a similar version of this problem.

A possible solution for this problem would be having some kind of dataflow coverage that could identify that data flowing from document() into generate-id() is something previously unseen and worth saving, however I am not aware of any practical implementation of such an approach.

## Issue #2: Mutational grammar fuzzing tends to produce samples that are very similar

To demonstrate this issue, letâs take a look at some samples from one of my XSLT fuzzing sessions:

Part of sample 1128 in the corpus:

```
<?xml version="1.0" encoding="UTF-8"?><xsl:fallback namespace="http://www.w3.org/url2" ><aaa ></aaa><ddd xml:id="{lxl:node-set($name2)}:" att3="{[$name4document('')att4.|document('')$name4namespace::]document('')}{ns2}" ></ns3:aaa></xsl:fallback>
```

Part of sample 603 in the corpus:

```
<?xml version="1.0" encoding="UTF-8"?><xsl:fallback namespace="http://www.w3.org/url2" ><aaa ></aaa><ddd xml:id="{lxl:node-set($name2)}:" att3="{[$name4document('')att4.|document('')$name4namespace::]document('')}{ns2}" xmlns:xsl="http://www.w3.org/url3" ><xsl:output ></xsl:output>eHhDC?^5=<xsl:choose elements="eee" ><xsl:copy stylesheet-prefix="ns3" priority="3" ></xsl:copy></xsl:choose></ddd>t</xsl:fallback>
```

As you can see from the example, even though these two samples are different and come from different points in time during the fuzzing session, a large part of these two samples are the same.

This follows from the greedy nature of mutational coverage guided fuzzing: when a sample is mutated to produce new coverage, it gets immediately saved to the corpus. Likely a large part of the original sample wasnât mutated, but it is still part of the new sample so it gets saved. This new sample can get mutated again and if the resulting (third) sample triggers new coverage it will also get saved, despite large similarities with the starting sample. This res...