---
title: QUIC and HTTP/3 Request Smuggling: A First Look at Stream-Multiplexing Desync Primitives
url: https://blog.zeddyu.info/2026/07/01/QUIC-HTTP3-Request-Smuggling-First-Look/
source: ZeddYu’s Blog
date: 2026-07-01
fetch_date: 2026-07-02T05:56:45.006657
---

# QUIC and HTTP/3 Request Smuggling: A First Look at Stream-Multiplexing Desync Primitives

* [Skip to primary navigation](#site-nav)
* [Skip to content](#main)
* [Skip to footer](#footer)

[ZeddYu's Blog](/)

Toggle menu

### [ZeddYu](https://blog.zeddyu.info/)

Security Researcher. HTTP Smuggling, Web Security, CTF.

Follow

# [QUIC and HTTP/3 Request Smuggling: A First Look at Stream-Multiplexing Desync Primitives](https://blog.zeddyu.info/2026/07/01/QUIC-HTTP3-Request-Smuggling-First-Look/)

7 minute read

#### On this page

* [Why the classic primitive does not port](#why-the-classic-primitive-does-not-port)
* [Where the risk actually re-emerges](#where-the-risk-actually-re-emerges)
* [The multiplexing angle, stated as a hypothesis](#the-multiplexing-angle-stated-as-a-hypothesis)
* [A short test plan](#a-short-test-plan)
* [So what](#so-what)
* [References](#references)

This is a first look, not a results table. I have spent most of my writing on this blog on HTTP/1.1 request smuggling and, more recently, on the HTTP/2 downgrade desync surface that James Kettle opened up in [HTTP/2: The Sequel is Always Worse](https://portswigger.net/research/http2). The obvious next question, and one I get asked often, is whether any of this survives the move to HTTP/3. Does request smuggling still make sense when the transport is QUIC?

The short version is that the classic in-stream primitive does not port, and the interesting surface moves almost entirely to the translation boundary. That is worth explaining carefully, because âHTTP/3 kills request smugglingâ is a claim I have seen repeated, and it is only true for a deployment shape that almost nobody actually runs.

I want to be honest about scope up front. I have not run a full test matrix against a fleet of HTTP/3 terminators yet, the way I did for the [2019 CL.TE / TE.CL / TE.TE work](/2019/12/08/HTTP-Smuggling-en/) and the [2026 re-test](/2026/05/16/Revisiting-HTTP-Smuggling-2026/). What follows is a threat-model analysis and a set of testable hypotheses, with the spec citations that make each one plausible. Where I am speculating, I say so.

## Why the classic primitive does not port

Request smuggling on HTTP/1.1 exists because of one structural fact: multiple requests share a single byte stream, and the boundary between them is negotiated in-band through headers that two parties can interpret differently. The whole CL.TE / TE.CL family comes from a front-end and a back-end disagreeing about where the body ends, because one honors `Content-Length` and the other honors `Transfer-Encoding: chunked`. [RFC 9112 Section 6.1](https://www.rfc-editor.org/rfc/rfc9112#section-6.1) now requires an implementation to reject a message carrying both, but that is a 2022 rule and it only binds parsers that were rewritten to enforce it.

HTTP/3 removes every ingredient of that primitive:

1. Message framing is explicit. Request and response bodies are carried in HTTP/3 DATA frames with declared lengths ([RFC 9114 Section 7.2](https://www.rfc-editor.org/rfc/rfc9114#section-7.2)). There is no chunked transfer coding in HTTP/3, and `Transfer-Encoding` is not a legal header. The `Content-Length` versus `Transfer-Encoding` disagreement simply has nothing to disagree about.
2. Requests do not share a stream. Each request/response exchange runs on its own client-initiated bidirectional QUIC stream ([RFC 9000 Section 2](https://www.rfc-editor.org/rfc/rfc9000#section-2)). A stream has an explicit end signalled by the QUIC layer. There is no ânext request in the pipelineâ sitting in the same buffer, because there is no pipeline. The thing a smuggled prefix would attach itself to does not exist.
3. Header fields are a binary, length-prefixed structure compressed with QPACK ([RFC 9204](https://www.rfc-editor.org/rfc/rfc9204)), not a CRLF-delimited text block. The bare-`\n` and header-obfuscation tricks that defeat text parsers do not have a text stream to exploit.

So on a genuinely end-to-end HTTP/3 path, from client to origin, the desync primitive I have spent years on does not have a home. That much of the optimistic claim is correct.

## Where the risk actually re-emerges

The problem with âend-to-end HTTP/3â is that it is close to a fiction in production. The overwhelmingly common shape is that an edge, a CDN node or a cloud load balancer, terminates HTTP/3 from the client and then speaks HTTP/2 or HTTP/1.1 to the origin. That translation step is exactly where Kettleâs HTTP/2 work found its desyncs: the danger was never HTTP/2 itself, it was the downgrade from HTTP/2 to HTTP/1.1 at the front-end, where a request that is unambiguous in the newer protocol gets re-serialized into an ambiguous or malformed HTTP/1.1 request.

HTTP/3 inherits this surface wholesale, and arguably widens it, because there is now a second protocol hop that can introduce the disagreement. The desync candidate looks like this:

```
Client  --HTTP/3-->  Edge (H3 terminator)  --HTTP/1.1-->  Origin
        stream 0                             conn reuse
```

Step 1: The client sends a well-formed HTTP/3 request whose header section contains a field the edge does not fully validate before downgrading. Candidates include a header value carrying an embedded CRLF, a duplicated `content-length`, or a `:path` / `:authority` pseudo-header with characters that are legal to carry in a QPACK field but not legal, unescaped, in a request line.

Step 2: The edge serializes this into HTTP/1.1 for the origin. If the serializer writes the offending value verbatim into the request line or headers, the well-formed H3 request becomes a malformed H1 request on the wire.

Step 3: The origin parses the malformed HTTP/1.1, and its interpretation of where this request ends disagrees with the edgeâs. We are back to a CL.TE-style differential, produced entirely by the downgrade serializer rather than by the client.

Step 4: Because the edge reuses upstream HTTP/1.1 connections across many client streams, the smuggled remainder is prepended to whatever request the edge sends next on that upstream connection, which may belong to a different client.

None of steps 1 through 4 require HTTP/3 to be weak. They require the H3-to-H1 serializer to be less strict than the H3 parser was, which is a very common failure mode. [RFC 9114 Section 4.1.2](https://www.rfc-editor.org/rfc/rfc9114#section-4.1.2) and [Section 4.2](https://www.rfc-editor.org/rfc/rfc9114#section-4.2) do specify field validation and forbid certain characters, so a fully conformant terminator should reject or sanitize these before they ever reach a downgrade. The empirical question, and it is the whole question, is whether real terminators enforce that on the H3 ingress path or trust the input because âHTTP/3 cannot smuggle.â

## The multiplexing angle, stated as a hypothesis

There is a second surface I find more interesting and much less certain. QUIC multiplexes many streams over one connection with no head-of-line blocking between them, and an edge typically fans those streams down onto a smaller pool of upstream connections. Connection-reuse and request-coalescing bugs have already produced real issues in the HTTP/2 world, including the CL.0 class where the front-end and back-end disagree about whether a connection should be reused at all.

My hypothesis is that the H3 stream-to-upstream-connection mapping is a fresh place for that class of bug to appear: if the terminator decides upstream connection reuse based on state it associates with the wrong stream, a response can be returned on a stream whose request it does not answer. I want to be clear that this is a hypothesis. I have not demonstrated it, and it may turn out that mainstream terminators keep per-stream upstream state cleanly enough that it never happens. It is on my test list precisely because I cannot yet argue it away from the specs alone.

## A short test plan

If you want to poke at this before I publish a full matrix, these are the questions I think are worth answering, roughly in order of expected yield:

1. Take each ...