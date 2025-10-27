---
title: How to Securing SSE
url: https://www.hahwul.com/sec/web-security/sse/
source: HAHWUL
date: 2025-06-24
fetch_date: 2025-10-06T22:53:01.357132
---

# How to Securing SSE

[ ]

[![HAHWUL Logo](/images/logo.png)](/)

[ ]

- [WHO](/about/)
- [BLOG](/blog/)
- [SEC](/sec/)
- [DEV](/dev/)
- [PROJECTS](/projects/)

* ENGLISH
* [한국어](https://www.hahwul.com/ko/sec/web-security/sse/)

`⌘``K`

[ENGLISH](https://www.hahwul.com/sec/web-security/sse/)

[한국어](https://www.hahwul.com/ko/sec/web-security/sse/)

JUNE 23, 2025

# How to Securing SSE

Server-Sent Events (SSE) Explained and Secured

In this article, I'll explain Server-Sent Events (SSE), one of the technologies for implementing real-time data communication in web applications. We'll explore the basic concepts and operational mechanisms of SSE, compare it with other technologies, and discuss security enhancement measures that must be considered in production environments.

## What is Server-Sent Events (SSE)?

Server-Sent Events is, as the name suggests, a technology where the server sends events to the client. When a browser requests a connection to the server, it maintains that connection while the server asynchronously pushes necessary data to the client in a one-way communication method.

SSE operates based on the HTTP protocol, which offers the advantage of utilizing existing web infrastructure without implementing additional protocols. Its main purpose is real-time data streaming from server to client, widely used for notifications, real-time feeds, status updates, and more.

## How it Works

The operating principle of SSE is relatively simple. The interaction between client and server follows this flow:

1. **Client Connection**: The client requests a connection to a specific endpoint on the server using JavaScript's `EventSource` object.
2. **Server Response**: The server responds to this request by setting the `Content-Type` header to `text/event-stream`. This header informs the client that the data to be transmitted will be an event stream.
3. **Persistent Connection**: The server keeps the connection open continuously.
4. **Data Push**: Whenever new data or events occur, the server sends messages to the client in a specified format. This connection is maintained until explicitly closed by either the server or client.

```
 sequenceDiagram
    participant Client
    participant Server

    Client->>Server: new EventSource('/events')
    Note over Client,Server: Initial HTTP Request
    Server-->>Client: HTTP 200 OK<br>Content-Type: text/event-stream<br>Connection: keep-alive
    Note over Client,Server: Connection Established

    loop Real-time Events
        Server-->>Client: data: Some new data\n\n
        Server-->>Client: event: notification<br>data: {"user":"guest","message":"Welcome!"}\n\n
        Server-->>Client: data: Another update\n\n
    end

    Client->>Server: eventSource.close()
    Note over Client,Server: Connection Closed by Client
```

### Event Stream Format

The data transmitted by the server is a simple text stream, with each message separated by one or more `key: value` fields and two newline characters (`\n\n`). The main fields include:

* `data`: The actual data to be transmitted. Multiple `data` fields can be included in one message.
* `event`: A field that specifies the type of event. Clients can use this value to listen for specific types of events. If not specified, it's processed as a `message` event.
* `id`: A unique ID for each event. When a client reconnects to the server, it can send the `id` of the last received event in the `Last-Event-ID` header to recover any lost data.
* `retry`: Specifies the time in milliseconds that the client should wait before attempting to reconnect.

```
// Simple message
data: This is a message.

// JSON data with a custom event type
event: user_update
data: {"username": "hahwul", "status": "online"}

// Message with an ID for synchronization
id: msg1
data: Some data stream
```

## SSE vs. WebSockets vs. Polling

Besides SSE, there are other technologies for implementing real-time web communications such as Polling, Long-Polling, and WebSockets. Each technology has distinct characteristics and pros and cons, so you should choose the appropriate one based on the problem you're trying to solve.

| Feature | Polling | Long-Polling | SSE (Server-Sent Events) | WebSockets |
| --- | --- | --- | --- | --- |
| **Direction** | Client -> Server | Client -> Server | Server -> Client (Unidirectional) | Bidirectional |
| **Protocol** | HTTP | HTTP | HTTP | WebSocket (`ws://`, `wss://`) |
| **Connection** | New connection per request | Long-lived, then new | Single persistent connection | Single persistent connection |
| **Overhead** | High | Medium | Low | Low (after handshake) |
| **Use Case** | Infrequent updates | Delayed updates | Notifications, Live Feeds | Chat, Gaming, Collaboration |
| **Reconnection** | Manual | Manual | Automatic (built-in) | Manual |

* **Polling**: The simplest method where the client requests data from the server at regular intervals, but it's inefficient due to many unnecessary requests.
* **WebSockets**: Supports bidirectional communication and can exchange data with very low latency. Ideal for applications like chat or real-time online games where interaction between client and server is frequent. However, it uses a different protocol than HTTP.
* **SSE**: Most suitable when one-way data pushing from server to client is needed. It's easy to implement as it uses HTTP, and the `EventSource` API has built-in automatic reconnection features, making it reliable.

## Client-Side Implementation

Client-side implementation can be written very simply through the `EventSource` API.

```
const eventSource = new EventSource('/stream');

// General message listener
eventSource.onmessage = (event) => {
  console.log('New message:', event.data);
};

// Listener for custom events
eventSource.addEventListener('notification', (event) => {
  const notificationData = JSON.parse(event.data);
  console.log('Notification:', notificationData.message);
});

// Error handling
eventSource.onerror = (err) => {
  console.error("EventSource failed:", err);
  // EventSource will automatically try to reconnect.
  // To close it permanently:
  // eventSource.close();
};
```

## How to Securing SSE

Since SSE operates over HTTP, it is exposed to common web security threats. Therefore, when using SSE in a production environment, security must be considered.

### Authentication and Authorization

The `EventSource` API does not standardly support setting custom HTTP headers like `Authorization`. This creates constraints for typical token-based authentication.

* Cookie-based Authentication: The browser automatically sends cookies when making an `EventSource` request, so session cookie-based authentication works naturally. This is one of the simplest and most effective methods.
* Query Parameter Token: It's also possible to pass an authentication token through URL query parameters (`/stream?token=...`). However, this method risks exposing the token in server logs, browser history, etc., so it should be used cautiously.

### CSRF (Cross-Site Request Forgery)

SSE connections start with a GET request, so they can be vulnerable to CSRF attacks. An attacker could trick a user into visiting a malicious page while logged in, establishing an SSE connection using the user's privileges and stealing sensitive real-time data.

* Origin Header Check: The server should validate the `Origin` header of requests to allow only those from authorized domains.
* SameSite Cookies: Setting the `SameSite=Lax` or `SameSite=Strict` attribute on authentication cookies prevents cookies from being sent when requests come from different origins.

### XSS (Cross-Site Scripting)

If data sent by the server is rendered directly to HTML on the client side, an XSS vulnerability can occur. Data received from the server should never be trusted and should always be escaped or encoded before use.

```
const outputDiv = document.getElementById('output');

eventSource.onmessage = (event) => {
  // Vulnerable to XSS: Never do this!
  // outputDiv.innerHTM...