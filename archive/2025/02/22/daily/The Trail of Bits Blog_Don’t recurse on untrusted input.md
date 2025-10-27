---
title: Don’t recurse on untrusted input
url: https://blog.trailofbits.com/2025/02/21/dont-recurse-on-untrusted-input/
source: The Trail of Bits Blog
date: 2025-02-22
fetch_date: 2025-10-06T20:35:48.316932
---

# Don’t recurse on untrusted input

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Don’t recurse on untrusted input

[Alexis Challande](https://bsky.app/profile/darkamaul.bsky.social), Brad Swain

February 21, 2025

[recursion](/categories/recursion/), [vulnerability-disclosure](/categories/vulnerability-disclosure/), [java](/categories/java/)

Page content

* [How recursion is harmful](#how-recursion-is-harmful)
* [Protobuf Java case study](#protobuf-java-case-study)
* [Protecting your code](#protecting-your-code)
* [Learn more](#learn-more)

A single malicious request can take down web applications that use recursive functions to process untrusted user input. We developed a simple [CodeQL query](https://github.com/trailofbits/codeql-queries/blob/main/java/src/security/Recursion/Recursion.ql) to assist in finding stack overflows and used it to find denial-of-service (DoS) vulnerabilities in several high-profile Java projects. All of these projects are maintained by security-conscious organizations with robust development practices:

* ElasticSearch (in [PatternBank](https://github.com/elastic/elasticsearch/commit/a02dc7165c75f12701f8d47a2bdefe5283735267), [parseGeometryCollection](https://github.com/elastic/elasticsearch/commit/097fc0654f9305e01402a06c82926bb04ebe5495))
* OpenSearch (in [FilterPath](https://github.com/opensearch-project/OpenSearch/commit/0742453ecc9b4f36ce72218d18d844baa9defe4e), [parseGeometryCollection](https://github.com/opensearch-project/OpenSearch/commit/120678d9b5e1ec611303f4dc5b3ce9b96fe21531), and [validatePatternBank](https://github.com/opensearch-project/OpenSearch/commit/13f04d97e3438b0389d1e851dfd08678ab644361))
* Protocol Buffers [CVE-2024-7254](https://github.com/advisories/GHSA-735f-pc8j-v9w8)
* Guava [Function rewrite](https://github.com/google/guava/commit/63734b9dfc9d69018c71e5502a1715eaa1f8e2b5)
* XStream [CVE-2024-47072](https://github.com/advisories/GHSA-hfq9-hggm-c56q)

Our findings indicate that recursion, while a powerful programming tool, becomes a severe liability when used to process untrusted data in applications with availability requirements. All of the above vulnerabilities have been fixed; however, if large-scale projects like these are vulnerable, you may have similar issues in your code. Read on to learn about how we discovered these issues and how to prevent them, or [check out our full white paper](https://resources.trailofbits.com/input-driven-recursion-white-paper).

## How recursion is harmful

Recursion can be elegant, simple, and, most importantly, practical. It is often the go-to method for dealing with nested structures, whether traversing a tree, visiting nodes in a graph, or parsing nested structures like JSON.

```
public int fibonacci(int n)  {
  if(n == 0) return 0;
  else if(n == 1) return 1;
  else return fibonacci(n - 1) + fibonacci(n - 2);
}
```

Figure 1: Recursive `Fibonacci` function from [Stack Overflow](https://stackoverflow.com/questions/8965006/java-recursive-fibonacci-sequence)

However, if attackers control the input, it is often trivial to craft an input that will exhaust the stack before reaching the recursive function’s base case. While developers often think about preventing infinite recursion, it may be possible to crash an application by simply providing a single malicious input that triggers a stack overflow.

```
Exception in thread "main" java.lang.StackOverflowError
    at Fibonacci.fibonacci(Fibonacci.java:8)
    at Fibonacci.fibonacci(Fibonacci.java:8)
    at Fibonacci.fibonacci(Fibonacci.java:8)
```

Figure 2: `StackOverflowError` from Stack Overflow

While client-side crashes may be inconvenient, server-side crashes can take down critical services, even with DDoS protection. In applications with availability requirements, this is a real risk with the potential for real harm.

## Protobuf Java case study

To illustrate how these vulnerabilities manifest in practice, let’s examine our discovery of CVE-2024-7254 in Google’s protocol buffers (Protobuf) library. This issue demonstrates how even security-conscious organizations can miss recursive processing vulnerabilities.

According to Protobuf’s official documentation:

Protocol buffers are Google’s language-neutral, platform-neutral, extensible mechanism for serializing structured data – think XML, but smaller, faster, and simpler. ([source](https://protobuf.dev/))

Parsing untrusted data is notoriously tricky, and security researchers have targeted parsers for every format. Google developed protocol buffers to provide a serialized exchange format with automatically generated parsers in various languages. They are used extensively both within Google and in the greater ecosystem.

However, they are also vulnerable to recursion error attacks.

For instance, an attacker could crash a Java application parsing an external message using the `protobuf-lite` library by simply sending this one message:

```
with open("recursive.data", "wb") as f:
    f.write(bytearray([19] * 5_000_000))
```

Figure 3: A malicious message in Protobuf

This message will throw a `StackOverflowError`. The problem lies in how Protobuf parses `Unknown Fields`. According to the [Protobuf documentation](https://protobuf.dev/programming-guides/proto3/#unknowns):

Unknown fields are well-formed protocol buffer serialized data representing fields that the parser does not recognize. For example, when an old binary parses data sent by a new binary with new fields, those new fields become unknown fields in the old binary.

When this issue is combined with Groups—a [deprecated feature](https://protobuf.dev/programming-guides/encoding/#groups) that is still parsed because of backward compatibility—you get an explosive mix:

1. A group can contain another group.
2. The new group is parsed as an unknown field if the attacked schema does not contain a group.
3. An unknown group can contain another group.
4. Goto 2

Below is an excerpt of the code responsible for the parsing:

```
final boolean mergeOneFieldFrom(B unknownFields, Reader reader) throws IOException {
  int tag = reader.getTag();
  /* ... */
  switch (WireFormat.getTagWireType(tag)) {
    /* ... */
    case WireFormat.WIRETYPE_START_GROUP:
      final B subFields = newBuilder();
      /* ... */
      mergeFrom(subFields, reader);
      /* ... */
      return true;
    /* ... */
  }
}

final void mergeFrom(B unknownFields, Reader reader) throws IOException {
  while (true) {
    if (reader.getFieldNumber() == Reader.READ_DONE
        || !mergeOneFieldFrom(unknownFields, reader)) {
      break;
    }
  }
}
```

Figure 4: `mergeFrom` function in [Protobuf](https://github.com/protocolbuffers/protobuf/blob/69a1888fd587410cc6a4d857d2ad7815e5aad93e/java/core/src/main/java/com/google/protobuf/UnknownFieldSchema.java#L59-L98))

The exciting thing about this vulnerability is that it has one precondition on the attacked target: it must use the Java lite version of the Protocol Buffer library. There are no requirements for the scheme used by the targeted application.

While [the official documentation of the C++ API](https://protobuf.dev/reference/cpp/api-docs/google.protobuf.message/#Message.DiscardUnknownFields.details) advises discarding `Unknown Fields` for security reasons, it advises doing it *after* parsing the message. At this point, it is already too late.
While Protobuf parsing is usually resilient against recursion attacks (using depth counters), Google forgot about this one code path during development. We responsibly disclosed this issue to Google, and it was assigned [CVE-2024-7254](https://github.com/protocolbuffers/protobuf/security/advisories/GHSA-735f-pc8j-v9w8).

While investigating this problem, we found that it also applied to other Protobuf implementations, including Rust-protobuf, an unofficial implementation of Protocol buffers in Rust.

## Protecting your code

As software systems increasingly need to handle nested data forma...