---
title: Apache Struts2 Core TokenHelper Token Cryptographic Timing Side-Channel
url: https://seclists.org/fulldisclosure/2026/Nov/6
source: Full Disclosure
date: 2026-11-02
fetch_date: 2026-11-03T08:51:59.178126
---

# Apache Struts2 Core TokenHelper Token Cryptographic Timing Side-Channel

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# Apache Struts2 Core TokenHelper Token Cryptographic Timing Side-Channel

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sat, 31 Oct 2026 21:21:13 +0000

---

```
Description
The Apache Struts2 Core 7.4.0 and below performs session token comparisons cryptographically insecure early-exit
comparison functions (e.g., `!=`, `memcmp`, byte-by-byte loops with `break`) that return as soon as the first
mismatched byte is encountered.  The execution time of the comparison is therefore proportional to the number of
leading bytes that match, creating a measurable timing side-channel.  Importantly, this side-channel has been
dynamically verified and exploited across networks using modern techniques that reduce/factor out latency.

Impact
Attackers can measure response latency, iteratively determining the correct value of the hash or secret one byte at a
time, reducing the attack complexity from `36^n`, where `n` is the number of bytes in the secret.  While, in the ideal
circumstance, the complexity of a pure brute-force attack would be `2^165` since the system is using a 165-bit
BigInteger, the conversion from BigInteger to an A-Z0-9 string does not map cleanly -- the resulting string, itself,
can actually be 31 or 32 characters long and bytes don't simply slot into a given character or position, thus requiring
the greater `36^32` brute-force.  With that said, in a system where lag can be injected, latency reduced or factored
out, the theoretical floor move from the worst case `36^32` to `36*32` (1,152 requests).  Of course, since the string
length can vary by one, attackers must first determine the string length, which can be done via two requests -- one
with each length -- a trivial addition to the worst case mentioned above but worth noting.

Successful exploitation enables bypassing the `TokenHelper`-generated token, which is designed to "[s]top
double-submission of forms" and may be used by information systems as a nonce as part of cross-site request forgery
protections.

Examples
Sample Code
`TokenHelper.validToken()`, leveraged by both `TokenInterceptor.handleToken(ActionInvocation)` and
`TokenSessionStoreInterceptor.handleToken(ActionInvocation)`, utilises the cryptographically insecure, early-exiting
`String.equals(String)` method to compare the in-session token against the user-provided token.

```java
    /**
     * Checks for a valid transaction token in the current request params. If a valid token is found, it is
     * removed so the it is not valid again.
     *
     * @return false if there was no token set into the params (check by looking for {@link #TOKEN_NAME_FIELD}), true
if a valid token is found
     */
    public static boolean validToken() {
        String tokenName = getTokenName();

        if (tokenName == null) {
            LOG.debug("No token name found -> Invalid token ");
            return false;
        }

        String token = getToken(tokenName);

        if (token == null) {
            LOG.debug("No token found for token name {} -> Invalid token ", normalizeSpace(tokenName));
            return false;
        }

        Map session = ActionContext.getContext().getSession();
                                String tokenSessionName = buildTokenSessionAttributeName(tokenName);
        String sessionToken = (String) session.get(tokenSessionName);

        if (!token.equals(sessionToken)) {
            if (LOG.isWarnEnabled()) {
                LocalizedTextProvider localizedTextProvider =
ActionContext.getContext().getContainer().getInstance(LocalizedTextProvider.class);
                LOG.warn(localizedTextProvider.findText(TokenHelper.class, "struts.internal.invalid.token",
ActionContext.getContext().getLocale(), "Form token {0} does not match the expected session token.", new Object[]{
                        normalizeSpace(token)
                }));
            }
            Dispatcher dispatcher = Dispatcher.getInstance();
            if (dispatcher != null && dispatcher.isDevMode()) {
                LOG.warn("Token mismatch detail - token name [{}], form token [{}], session token [{}]",
                        normalizeSpace(tokenName), normalizeSpace(token), sessionToken);
            }

            return false;
        }

        // remove the token so it won't be used again
        session.remove(tokenSessionName);
        ActionContext.getContext().put(VALIDATED_TOKEN_KEY, new ValidatedToken(tokenName, token));

        return true;
    }
```
Code snippet from `struts2-core`'s core/src/main/java/org/apache/struts2/util/TokenHelper.java, lines 164-210

```java
    protected String handleToken(ActionInvocation invocation) throws Exception {
        //see WW-2902: we need to use the real HttpSession here, as opposed to the map
        //that wraps the session, because a new wrap is created on every request
        HttpSession session = ServletActionContext.getRequest().getSession(true);
        synchronized (session.getId().intern()) {
            if (!TokenHelper.validToken()) {
                return handleInvalidToken(invocation);
            }
        }
        return handleValidToken(invocation);
    }
```
Snippet from `struts2-core`'s core/src/main/java/org/apache/struts2/interceptor/TokenInterceptor.java, lines 140-150,
showing the interceptor calling for token validation -- note, too, the improper, unsafe synchronisation on
`session.getId().intern()`, though that is a separate finding with a separate write-up

```java
    @Override
    protected String handleToken(ActionInvocation invocation) throws Exception {
        //see WW-2902: we need to use the real HttpSession here, as opposed to the map
        //that wraps the session, because a new wrap is created on every request
        HttpSession session = ServletActionContext.getRequest().getSession(true);
        synchronized (session.getId().intern()) {
            if (!TokenHelper.validToken()) {
                return handleInvalidToken(invocation);
            }
            return handleValidToken(invocation);
        }
    }
```
Code from `struts2-core`'s core/src/main/java/org/apache/struts2/interceptor/TokenSessionStoreInterceptor.java, lines
104-115, showing the interceptor calling for token validation -- note, too, the improper, unsafe synchronisation on
`session.getId().intern()`, though that is a separate finding with a separate write-up
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

### Current thread:

* **Apache Struts2 Core TokenHelper Token Cryptographic Timing Side-Channel** *Daniel Owens via Fulldisclosure (Nov 01)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/do...