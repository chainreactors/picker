---
title: Encrypting Files with Passkeys and age
url: https://words.filippo.io/passkey-encryption/
source: Filippo Valsorda
date: 2025-07-15
fetch_date: 2025-10-06T23:17:22.425885
---

# Encrypting Files with Passkeys and age

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

14 Jul 2025

# Encrypting Files with Passkeys and age

[Typage](https://github.com/FiloSottile/typage) (`age-encryption` on npm) is a TypeScript[1](#fn:ts) implementation of the [age file encryption format](https://c2sp.org/age). It runs with Node.js, Deno, Bun, and browsers, and implements native age recipients, passphrase encryption, ASCII armoring, and supports custom recipient interfaces, like the [Go implementation](https://github.com/FiloSottile/age).

However, running in the browser affords us some special capabilities, such as access to the WebAuthn API. Since [version 0.2.3](https://github.com/FiloSottile/typage/releases/tag/v0.2.3), Typage supports *symmetric* encryption with passkeys and other WebAuthn credentials, and a companion [age CLI plugin](https://words.filippo.io/age-plugins/) allows reusing credentials on hardware FIDO2 security keys outside the browser.

Let’s have a look at how encrypting files with passkeys works, and how it’s implemented in Typage.

## Encrypting with passkeys

Passkeys are synced, discoverable [WebAuthn](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API) credentials. They’re a phishing-resistant standard-based authentication mechanism. Credentials can be stored in platform authenticators (such as end-to-end encrypted iCloud Keychain), in password managers (such as 1Password), or on hardware FIDO2 tokens (such as YubiKeys, although these are not synced). I am a strong believer in passkeys, especially when [paired with email magic links](https://rmondello.com/2025/01/02/magic-links-and-passkeys/), as a strict improvement over passwords for average users and websites. If you want to learn more about passkeys and WebAuthn I can’t recommend Adam Langley’s [*A Tour of WebAuthn*](https://www.imperialviolet.org/tourofwebauthn/tourofwebauthn.html) enough.

![login with a passkey screenshot](https://assets.buttondown.email/images/5268e763-926f-472f-b205-f439404ca0c0.png?w=960&fit=max)

The primary functionality of a WebAuthn credential is to cryptographically sign an origin-bound challenge. That’s not very useful for encryption. However, credentials with the `prf` extension can also compute a [Pseudo-Random Function](https://en.wikipedia.org/wiki/Pseudorandom_function_family) while producing an “assertion” (i.e. while logging in). You can think of a PRF as a keyed hash (and indeed for security keys it’s backed by the `hmac-secret` FIDO2 extension): a given input always maps to the same output, without the secret there’s no way to compute the mapping, and there’s no way to extract the secret.

Specifically, the WebAuthn PRF takes one or two inputs and returns a 32-byte output for each of them. That lets “relying parties” implement *symmetric* encryption by treating the PRF output as a key that’s only available when the credential is available. Using the PRF extension requires User Verification (i.e. PIN or biometrics). You can read more about the extension [in Adam’s book](https://www.imperialviolet.org/tourofwebauthn/tourofwebauthn.html#prf).

Note that there’s no secure way to do asymmetric encryption: we could use the PRF extension to encrypt a private key, but then an attacker that observes that private key once can decrypt anything encrypted to its public key in the future, without needing access to the credential.

Support for the PRF extension landed in Chrome 132, macOS 15, iOS 18, and [1Password versions from July 2024](https://blog.1password.com/encrypt-data-saved-passkeys/).

## The fido2prf age format

To encrypt an age file to a new type of recipient, we need to define how the random file key is encrypted and encoded into a [header stanza](http://c2sp.org/age#header). Here’s a stanza that wraps the file key with an ephemeral FIDO2 PRF output.

```
-> age-encryption.org/fido2prf Fv8VHh8kzhSlR14OviQ2OA
0Gw/JQEYrx5wPEUQzAh14nB6vTujga6VaboJ/vMKgWw
```

The first argument is a fixed string to recognize the stanza type. The second argument is a 128-bit nonce[2](#fn:128) that’s used as the PRF input. The stanza body is the ChaCha20Poly1305 encryption of the file key using a wrapping key derived from the PRF output.

Each credential assertion (which requires a single [User Presence](https://www.imperialviolet.org/tourofwebauthn/tourofwebauthn.html#user-presence) check, e.g. a YubiKey touch) can compute two PRFs. This is [meant for key rotation](https://www.imperialviolet.org/tourofwebauthn/tourofwebauthn.html#user-presence:~:text=During%20each%20operation%20the%20PRF%20can%20be%20evaluated%20on%20up%20to%20two%20inputs%20in%20order%20to%20support%20key%20rotation.), but in our use case it’s actually a minor security issue: an attacker who compromised your system but not your credential could surreptitiously decrypt an “extra” file every time you intentionally decrypt or encrypt one. We mitigate this by using *two* PRF outputs to derive the wrapping key.

The WebAuthn PRF inputs are composed of a domain separation prefix, a counter, and the nonce.

```
"age-encryption.org/fido2prf" || 0x01 || nonce
"age-encryption.org/fido2prf" || 0x02 || nonce
```

The two 32-byte PRF outputs are concatenated and passed to HKDF-Extract-SHA-256 with `age-encryption.org/fido2prf` as salt to derive the ChaCha20Poly1305 wrapping key. That key is used with a zero nonce (since it’s used only once) to encrypt the file key.

This age recipient format has two important properties:

* **Per-file hardware binding**: each file has its own PRF input(s), so you strictly need both the encrypted file and access to the credential to decrypt a file. You can’t precompute some intermediate value and use it later to decrypt arbitrary files.
* **Unlinkability**: there is no way to tell that two files are encrypted to the same credential, or to link a file to a credential ID without being able to decrypt the file.[3](#fn:unlink)

## WebAuthn and Typage

Now that we have a format, we need an implementation. Enter [Typage](https://github.com/FiloSottile/typage) 0.2.3.

```
npm install -s age-encryption@0.2.3
```

The WebAuthn API is pretty complex, at least in part because it started as a way to expose U2F security keys before passkeys were a thing, and grew organically over the years. However, Typage’s passkey support amounts to [less than 300 lines](https://github.com/FiloSottile/typage/blob/c5661204271e1e77d279e963c3c00dd17364f2fc/lib/webauthn.ts), including a [simple implementation of CTAP2’s CBOR subset](https://github.com/FiloSottile/typage/blob/c5661204271e1e77d279e963c3c00dd17364f2fc/lib/cbor.ts).

Before any encryption or decryption operation, a new passkey must be created with a call to `age.webauthn.createCredential`.

```
await age.webauthn.createCredential({ keyName: "age encryption key 🦈" })
```

`age.webauthn.createCredential` calls `navigator.credentials.create` with a random `user.id` to avoid overwriting existing keys, `authenticatorSelection.residentKey` set to `required` to ask the authenticator to store a passkey, and of course `extensions: { prf: {} }`. Passkeys not generated by `createCredential` can also be used if they have the `prf` extension enabled.

![a credential creation prompt](https://assets.buttondown.email/images/7149d20c-b9f5-49b9-8830-521551585369.png?w=960&fit=max)

To encrypt or decrypt a file, you instantiate an `age.webauthn.WebAuthnRecipient` or `age.webauthn.WebAuthnIdentity`, which implement the new `age.Recipient` and `age.Identity` interfaces.

```
const e = new age.Encrypter()
e.addRecipient(new age.webauthn.WebAuthnRecipient())
const ciphertext = await e.encrypt("Hello, age!")
const armored = age.armor.encode(ciphertext)
console.log(armored)

const d = new age.Decrypter()
d.addIdentity(new age.webauthn.WebAuthnIdentity())
const decoded = age.armor.decode(armored)
const out = await d.decrypt(decoded, "text")
console.log(out)
```

The recipient and identity impleme...