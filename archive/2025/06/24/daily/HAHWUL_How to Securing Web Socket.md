---
title: How to Securing Web Socket
url: https://www.hahwul.com/sec/web-security/websocket/
source: HAHWUL
date: 2025-06-24
fetch_date: 2025-10-06T22:53:02.506069
---

# How to Securing Web Socket

[ ]

[![HAHWUL Logo](/images/logo.png)](/)

[ ]

- [WHO](/about/)
- [BLOG](/blog/)
- [SEC](/sec/)
- [DEV](/dev/)
- [PROJECTS](/projects/)

* ENGLISH
* [한국어](https://www.hahwul.com/ko/sec/web-security/websocket/)

`⌘``K`

[ENGLISH](https://www.hahwul.com/sec/web-security/websocket/)

[한국어](https://www.hahwul.com/ko/sec/web-security/websocket/)

JUNE 23, 2025

# How to Securing Web Socket

A guide on securing WebSocket to protect real-time applications from common vulnerabilities.

This article covers the security vulnerabilities of WebSocket, which enables real-time bidirectional communication, and the core methodologies to defend against them. Unlike HTTP, WebSocket is efficient as it allows continuous data exchange once a connection is established, but this characteristic can expose it to new security threats.

## Core Principles of WebSocket Security

To strengthen WebSocket security, the following core principles must be considered. Each item plays a crucial role in blocking potential attack vectors.

| Principle | Description |
| --- | --- |
| Encrypt Communication (WSS) | Always use the `wss://` protocol to encrypt communications. `ws://` transmits data in plaintext, making it vulnerable to sniffing attacks, while `wss://` encrypts data through TLS (Transport Layer Security), protecting communications from man-in-the-middle (MITM) attacks. |
| Validate Origin Headers | To defend against Cross-Site WebSocket Hijacking (CSWSH) attacks, the server must validate the `Origin` header during WebSocket handshake requests. Create an allowlist of permitted domains and reject connection requests from origins not on this list. |
| Implement Robust Authentication | The WebSocket protocol itself has no authentication mechanism. Therefore, users must be authenticated during the HTTP handshake process, which is the initial connection stage. Proven methods like cookies, sessions, and JWT (JSON Web Token) can be utilized. |
| Sanitize and Validate All Inputs | All data received from clients should be considered untrusted. To prevent injection attacks like XSS (Cross-Site Scripting) and SQL Injection, servers must perform strong validation and data sanitization on all messages. |

## Common Vulnerabilities and Mitigations

Here are the main vulnerabilities commonly found in WebSocket environments and how to address them:

### Cross-Site WebSocket Hijacking (CSWSH)

CSWSH is an attack where attackers induce users' browsers to establish unauthorized WebSocket connections. If a user has an authenticated session (e.g., cookies), the attacker's malicious page can communicate with the server using the user's privileges.

* Mitigation: As mentioned earlier, the server must strictly validate the `Origin` header of handshake requests and only accept requests from allowed origins.

```
// Example: Origin header validation in Node.js (ws library)
const allowedOrigins = ['https://hahwul.com', 'https://sub.hahwul.com'];

wsServer.on('request', (request) => {
  const origin = request.origin;
  if (!allowedOrigins.includes(origin)) {
    // Reject the connection
    request.reject();
    console.log(`Connection from origin ${origin} rejected.`);
    return;
  }
  // ... accept connection
});
```

### Data Injection Attacks (XSS, SQLi)

If data transmitted via WebSocket isn't properly handled, it can have malicious effects on the server or other clients. For example, in a chat application, if a script sent by one user executes in other users' browsers, an XSS attack has occurred.

* Mitigation: The server must validate all message content received from clients and always escape or sanitize it before using it in database queries or HTML output. Always exercise caution when handling untrusted data.

### Denial-of-Service (DoS)

Attackers can deplete server resources by creating numerous connections or sending large volumes of resource-intensive messages. This disrupts normal users' access to services.

* Mitigation:
  + Rate Limiting: Restrict the number of connections and message transmission rates per IP address or user account.
  + Message Size Limits: Block abnormally large messages to prevent buffer overflows or resource waste.

## Authentication and Authorization

While WebSocket is a stateful protocol, authentication should be performed through the stateless HTTP handshake.

```
 sequenceDiagram
    participant Client
    participant Server

    Client->>Server: HTTP GET /chat (Upgrade: websocket)
    Note over Server: 1. Verify Origin Header
    Note over Server: 2. Authenticate User (e.g., via Cookie/JWT)
    alt Authentication/Origin Check Fails
        Server-->>Client: HTTP 401/403 Unauthorized
    else Authentication & Origin OK
        Server-->>Client: HTTP 101 Switching Protocols
        Note over Client,Server: WebSocket Connection Established
        Client-->>Server: WebSocket Message (JSON)
        Note over Server: 3. Validate & Sanitize Message
        Server-->>Client: WebSocket Message (Broadcast)
    end
```

Commonly used authentication methods include:

1. Cookie-based Authentication: When operating WebSocket on the same domain as the web application, browsers automatically send authentication cookies. The server can identify users by validating these cookies.
2. Token-based Authentication: Clients send tokens (e.g., JWT) obtained during login through query parameters or as the first WebSocket message. The server verifies the token's validity before allowing the connection.

```
// Token via query parameter
const socket = new WebSocket('wss://api.hahwul.com/ws?token=YOUR_JWT_TOKEN');

// Token as the first message
socket.onopen = () => {
  socket.send(JSON.stringify({ type: 'auth', token: 'YOUR_JWT_TOKEN' }));
};
```

Sending tokens as query parameters is simple to implement but has the drawback of potentially leaving tokens in server logs. Conversely, sending them as the first message after connection is safer, but requires implementing logic to avoid processing other messages until authentication is complete.

## Conclusion

WebSocket has become an essential element in modern web applications, but alongside its convenience lie security issues that must be considered. The mandatory use of `wss://`, validation of `Origin` headers, handling input data, and applying robust authentication mechanisms discussed in this article are minimum requirements for building a secure WebSocket environment. From a red team perspective, systems lacking these basic defenses can easily become targets for attacks. Therefore, it's crucial to design with security in mind from the early development stages.

[#websocket](https://www.hahwul.com/tags/websocket/)
[#security](https://www.hahwul.com/tags/security/)
[#web](https://www.hahwul.com/tags/web/)

[ ]

[ ]

### Table of Contents

[Core Principles of WebSocket Security](https://www.hahwul.com/sec/web-security/websocket/#core-principles-of-websocket-security)

[Common Vulnerabilities and Mitigations](https://www.hahwul.com/sec/web-security/websocket/#common-vulnerabilities-and-mitigations)

[Cross-Site WebSocket Hijacking (CSWSH)](https://www.hahwul.com/sec/web-security/websocket/#cross-site-websocket-hijacking-cswsh)
[Data Injection Attacks (XSS, SQLi)](https://www.hahwul.com/sec/web-security/websocket/#data-injection-attacks-xss-sqli)
[Denial-of-Service (DoS)](https://www.hahwul.com/sec/web-security/websocket/#denial-of-service-dos)

[Authentication and Authorization](https://www.hahwul.com/sec/web-security/websocket/#authentication-and-authorization)

[Conclusion](https://www.hahwul.com/sec/web-security/websocket/#conclusion)

[Previous

OWASP Top 10](https://www.hahwul.com/sec/web-security/owasp-top-10/)

[Next

Subresource Integrity (SRI)](https://www.hahwul.com/sec/web-security/sri/)

[Contact](/contact)
[Thanks](/thanks)
[Sitemap](/sitemap.xml)
Random
[Feeds](/feeds)

© 2025 HAHWUL
Developed and Designed by Me

* [WHO](/about/)
* [BLOG](/blog/)
* [SEC](/sec/)
* [DEV](/dev/)
* [PROJECTS](/projects/)

---

* Language
  +...