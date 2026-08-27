---
title: WatsonWebserver v7.1.0 HTTP/1 Chunked Request Processing	Bypasses MaxRequestBodySize
url: https://seclists.org/fulldisclosure/2026/Aug/104
source: Full Disclosure
date: 2026-08-26
fetch_date: 2026-08-27T12:14:26.438124
---

# WatsonWebserver v7.1.0 HTTP/1 Chunked Request Processing	Bypasses MaxRequestBodySize

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](103)
[By Date](date.html#104)
[![Next](/images/right-icon-16x16.png)](105)

[![Previous](/images/left-icon-16x16.png)](103)
[By Thread](index.html#104)
[![Next](/images/right-icon-16x16.png)](105)

![](/shared/images/nst-icons.svg#search)

# WatsonWebserver v7.1.0 HTTP/1 Chunked Request Processing Bypasses MaxRequestBodySize

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 22 Aug 2026 08:43:02 -0400

---

```
WatsonWebserver contains an HTTP/1 request body size-limit bypass when
processing requests using Transfer-Encoding: chunked.

The framework's configured Settings.IO.MaxRequestBodySize limit is enforced
when a request declares its body size using Content-Length. However,
requests using chunked transfer encoding are processed through a separate
body-reading path that accumulates decoded chunks into a MemoryStream
without enforcing the same cumulative request-body limit.

As a result, a remote client can submit an HTTP/1 request whose decoded
body exceeds the administrator-configured MaxRequestBodySize by using
chunked transfer encoding instead of Content-Length.

A proof of concept configured:

MaxRequestBodySize = 16 bytes

and submitted a chunked request containing:

24 bytes

of decoded body data.

WatsonWebserver accepted the complete request, delivered all 24 bytes to
the application, and returned:

HTTP/1.1 200 OK

len=24

This confirms that MaxRequestBodySize is not consistently enforced across
supported HTTP/1 request-framing mechanisms.

Because the chunked body is accumulated in memory without a cumulative
MaxRequestBodySize check, an attacker may also be able to cause excessive
memory and CPU consumption by submitting substantially larger request
bodies. The supplied PoC directly demonstrates the size-limit bypass;
denial of service is a potential consequence rather than a demonstrated
result of the 24-byte test.

Vulnerability Description

WatsonWebserver provides the following configuration setting for
restricting HTTP request body size:

Settings.IO.MaxRequestBodySize

For HTTP/1 requests containing a Content-Length header, WatsonWebserver
parses the declared body size and rejects the request when it exceeds the
configured maximum.

However, HTTP/1 also permits request bodies to be framed using:

Transfer-Encoding: chunked

Chunked requests do not contain a single up-front Content-Length. Instead,
the body is transmitted as a sequence of independently sized chunks.

WatsonWebserver handles these requests through ReadChunkedBodyAsync(),
which repeatedly reads chunks and writes their contents into an in-memory
MemoryStream.

The implementation does not maintain a cumulative decoded-body length and
does not compare the accumulated size against Settings.IO.MaxRequestBodySize
.

Consequently, a client can bypass the configured request body limit simply
by changing the HTTP framing mechanism from Content-Length to
Transfer-Encoding:
chunked.

Technical AnalysisContent-Length Path

When WatsonWebserver encounters a request containing Content-Length, the
parsed length is stored in:

metadata.ContentLength = parsedContentLength;

The framework subsequently enforces MaxRequestBodySize:

if (settings.IO.MaxRequestBodySize > 0 &&
    metadata.ContentLength > settings.IO.MaxRequestBodySize)
{
    throw new IOException(
        "Request body size "
        + metadata.ContentLength
        + " exceeds maximum allowed size "
        + settings.IO.MaxRequestBodySize
        + ".");
}

The configured maximum is therefore enforced for requests whose body
length is known through Content-Length.

Chunked Request Path

Requests using:

Transfer-Encoding: chunked

follow a different body-processing path.

The relevant implementation is:

private async Task<byte[]> ReadChunkedBodyAsync(
    CancellationToken token)
{
    using (MemoryStream memoryStream = new MemoryStream())
    {
        while (true)
        {
            Chunk chunk =
                await ReadChunk(token)
                .ConfigureAwait(false);

            if (chunk.Data != null &&
                chunk.Data.Length > 0)
            {
                memoryStream.Write(
                    chunk.Data,
                    0,
                    chunk.Data.Length);
            }

            if (chunk.IsFinal)
                break;
        }

        _BodyComplete = true;

        return memoryStream.ToArray();
    }
}

Each decoded chunk is appended directly to the MemoryStream:

memoryStream.Write(
    chunk.Data,
    0,
    chunk.Data.Length);

There is no equivalent check against:

Settings.IO.MaxRequestBodySize

before the write.

The loop continues until the terminating chunk is received.

Proof of ConceptServer Configuration

The proof of concept configures WatsonWebserver with:

server.Settings.IO.MaxRequestBodySize = 16;

The maximum accepted request body should therefore be:

16 bytes

Malicious Request

The client submits a valid chunked HTTP/1 request:

POST / HTTP/1.1
Host: 127.0.0.1
Transfer-Encoding: chunked
Connection: close

8
abcdefgh
8
ijklmnop
8
qrstuvwx
0

The request contains three chunks.

Each chunk contains:

8 bytes

giving a cumulative decoded request body of:

8 + 8 + 8 = 24 bytes

The body therefore exceeds the configured limit by:

24 - 16 = 8 bytes

or:

150% of the configured maximum.

Observed HTTP Response

WatsonWebserver accepts the request and returns:
HTTP/1.1 200 OK Content-Type: text/plain Content-Length: 6 Date: Thu, 06
Aug 2026 01:16:34 GMT Connection: close Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: OPTIONS, HEAD, GET, PUT, POST, DELETE, PATCH
Access-Control-Allow-Headers: * Access-Control-Expose-Headers: Accept: */*
Accept-Language: en-US, en Accept-Charset: ISO-8859-1, utf-8 Cache-Control:
no-cache Host: 127.0.0.1:44009 len=24

The application reports:
len=24

confirming that the complete decoded body reached the application despite:
MaxRequestBodySize = 16

Security ImpactConfirmed Impact

The PoC directly demonstrates that a remote HTTP client can bypass the
configured:

Settings.IO.MaxRequestBodySize

restriction when using chunked transfer encoding.

The confirmed impact is therefore:

   - bypass of the configured HTTP request-body size restriction;
   - acceptance of request bodies larger than the administrator-defined
   maximum; and
   - in-memory processing of data that should have been rejected by the
   configured limit.

Resource Consumption

The affected chunked path accumulates the decoded body in a MemoryStream:

memoryStream.Write(
    chunk.Data,
    0,
    chunk.Data.Length);

and ultimately performs:

return memoryStream.ToArray();

Because there is no cumulative MaxRequestBodySize check in this path,
substantially larger request bodies can potentially consume increasing
amounts of process memory and processing time.

Depending on deployment configuration, available resources, concurrency,
reverse proxies, transport timeouts, and application-specific controls,
this may contribute to:

   - excessive memory consumption;
   - increased CPU utilization;
   - request-processing degradation; and
   - denial of service.

The supplied 24-byte PoC demonstrates the *security-control bypass*, not
resource exhaustion itself.

Ron Edgerson
Vulnerability Researcher & Exploit Developer

CVE Research | Binary Exploitation | Application & Systems Security
Responsible Disclosure • Proof-of-Concept Development

🌐 https://github.com/ob1sec
🔗 https://www.linkedin.com/in/ronedgerson1
<htt...