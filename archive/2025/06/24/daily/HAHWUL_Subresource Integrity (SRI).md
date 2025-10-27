---
title: Subresource Integrity (SRI)
url: https://www.hahwul.com/sec/web-security/sri/
source: HAHWUL
date: 2025-06-24
fetch_date: 2025-10-06T22:52:59.947460
---

# Subresource Integrity (SRI)

[ ]

[![HAHWUL Logo](/images/logo.png)](/)

[ ]

- [WHO](/about/)
- [BLOG](/blog/)
- [SEC](/sec/)
- [DEV](/dev/)
- [PROJECTS](/projects/)

* ENGLISH
* [한국어](https://www.hahwul.com/ko/sec/web-security/sri/)

`⌘``K`

[ENGLISH](https://www.hahwul.com/sec/web-security/sri/)

[한국어](https://www.hahwul.com/ko/sec/web-security/sri/)

JUNE 23, 2025

# Subresource Integrity (SRI)

A guide to understanding and implementing Subresource Integrity (SRI) for enhanced web security.

Subresource Integrity (SRI) is a security feature that enables browsers to verify that resources they fetch (for example, from a CDN) are delivered without unexpected manipulation. It works by allowing you to provide a cryptographic hash that a fetched resource must match.

This article explains what SRI is, why it's needed, how it works, and how to implement it.

## What is SRI?

SRI is a W3C specification that allows web developers to ensure that resources hosted on third-party servers (like CDNs) have not been tampered with. By providing a cryptographic hash (integrity metadata) for a resource, the browser can verify that the fetched resource matches the expected hash before executing it. If the resource does not match, the browser will refuse to load it, preventing potential attacks.

```
 graph LR
    subgraph Server
        A[Generate resource hash and<br>embed in HTML 'integrity' attribute]
    end

    subgraph Browser
        B[Download resource from CDN] --> C[Calculate hash from<br>the downloaded resource]
        C --> D{Compare hashes}
    end

    A --> B
    D -- Match --> E[✅ Execute script]
    D -- Mismatch --> F[❌ Block script & throw error]
```

## Why is SRI needed?

Websites often rely on Content Delivery Networks (CDNs) to serve common files like JavaScript libraries and CSS frameworks. This improves performance and availability. However, if a CDN is compromised, malicious actors could modify these files to inject malicious code into websites that use them. This could lead to various attacks, such as data theft or a complete site takeover.

SRI mitigates this risk by ensuring that the browser only executes code that matches the developer-provided integrity hash.

## How does SRI work?

SRI works by using the `integrity` attribute on `<script>` and `<link>` elements. This attribute contains one or more base64-encoded cryptographic hashes.

### The `integrity` attribute

The `integrity` attribute's value is a string containing at least one hash. Multiple hashes can be provided, separated by whitespace. Each hash consists of a prefix indicating the hash algorithm (e.g., `sha256`, `sha384`, `sha512`), followed by a hyphen, and then the base64-encoded hash value.

Example: `sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC`

### Hash generation

The most commonly used hash algorithms for SRI are SHA-256, SHA-384, and SHA-512. SHA-384 is generally recommended as a good balance between security and performance.

### Browser verification process

When a browser encounters a `<script>` or `<link>` element with an `integrity` attribute, it performs the following steps:

1. It fetches the resource from the specified URL.
2. It calculates the cryptographic hash of the fetched resource using one of the algorithms specified in the `integrity` attribute. Browsers will attempt to use the strongest algorithm listed if multiple are provided.
3. It compares the calculated hash with the hash provided in the `integrity` attribute.
4. If the hashes match, the resource is executed or applied.
5. If the hashes do not match, the browser refuses to execute or apply the resource and typically logs an error in the console.

## How to implement SRI?

Implementing SRI is straightforward. You need to add the `integrity` attribute to your `<script>` and `<link>` tags that reference external resources.

### Examples

For a JavaScript file:

```
<script src="https://example.com/library.js"
        integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
        crossorigin="anonymous"></script>
```

For a CSS file:

```
<link href="https://example.com/style.css"
      rel="stylesheet"
      integrity="sha384-AbcDEfGhIjKlMnOpQrStUvWxYz1234567890AbcDEfGhIjKlMnOpQrSt="
      crossorigin="anonymous">
```

Note the `crossorigin="anonymous"` attribute. For SRI to work with resources fetched from a third-party origin, the resource must be served with CORS (Cross-Origin Resource Sharing) headers that allow the resource to be shared with your origin (e.g., `Access-Control-Allow-Origin: *`). The `crossorigin="anonymous"` attribute tells the browser to make a CORS request without sending credentials (cookies, client-side SSL certificates, or HTTP authentication).

### SRI Hash Generation Tools

You can generate SRI hashes in several ways:

* Online Generators: There are many websites that can generate SRI hashes for you, such as [SRIHash.org](https://www.srihash.org/).
* OpenSSL Command-line Tool: You can use `openssl` to generate hashes. For example, to generate a SHA-384 hash:

  ```
  curl -sL "https://code.jquery.com/jquery-3.6.0.min.js" | openssl dgst -sha384 -binary | openssl base64 -A
  # vtXRMe3mGCbOeY7l30aIg8H9p3GdeSe4IFlP6G8JMa7o7lXvnz3GFKzPxzJdPfGK
  ```

  This command fetches the file, calculates its SHA-384 hash, and then base64 encodes it.
* npm Packages: Tools like `sri-toolbox` or `webpack-subresource-integrity` can help automate SRI hash generation in your build process.

## Advantages of SRI

* Protection against CDN compromise: SRI ensures that even if a CDN is breached and files are modified, your website will not load the tampered resources.
* Increased trust: It provides an additional layer of security, increasing the trustworthiness of your website.
* Simple implementation: Adding the `integrity` attribute is relatively easy.

## Limitations of SRI

* Dynamic content: SRI is not suitable for resources that change frequently or are dynamically generated, as the hash would need to be updated every time the content changes.
* Not a replacement for HTTPS: SRI protects against a specific type of attack (resource modification on a third-party server). It does not replace the need for HTTPS, which encrypts the communication channel and protects against man-in-the-middle attacks.
* Browser support: While most modern browsers support SRI, older browsers might not. However, these browsers will simply ignore the `integrity` attribute and load the resource without verification, so it doesn't break functionality for them.
* Requires CORS: For cross-origin resources, the server hosting the resource must include appropriate CORS headers.

## Conclusion

Subresource Integrity is a valuable security feature that helps protect websites from attacks originating from compromised third-party hosts. By verifying the integrity of external resources, SRI adds a crucial layer of defense against malicious code injection. While it has some limitations, its ease of implementation and significant security benefits make it a recommended practice for any website that relies on external resources.

[#SRI](https://www.hahwul.com/tags/sri/)
[#web security](https://www.hahwul.com/tags/web-security/)
[#content security](https://www.hahwul.com/tags/content-security/)

[ ]

[ ]

### Table of Contents

[What is SRI?](https://www.hahwul.com/sec/web-security/sri/#what-is-sri)

[Why is SRI needed?](https://www.hahwul.com/sec/web-security/sri/#why-is-sri-needed)

[How does SRI work?](https://www.hahwul.com/sec/web-security/sri/#how-does-sri-work)

[The integrity attribute](https://www.hahwul.com/sec/web-security/sri/#the-integrity-attribute)
[Hash generation](https://www.hahwul.com/sec/web-security/sri/#hash-generation)
[Browser verification process](https://www.hahwul.com/sec/web-security/sri/#browser-verification-process)

[How to implement SRI?](https://www.hahwul.com/sec/web-security/sri/#how-to-implement-sri)

[Examples](https://www.hahwul.com/sec/web-security/sri/#example...