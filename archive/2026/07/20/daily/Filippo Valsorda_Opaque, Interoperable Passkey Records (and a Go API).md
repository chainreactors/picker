---
title: Opaque, Interoperable Passkey Records (and a Go API)
url: https://words.filippo.io/passkey-record/
source: Filippo Valsorda
date: 2026-07-20
fetch_date: 2026-07-21T05:01:49.667860
---

# Opaque, Interoperable Passkey Records (and a Go API)

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

20 Jul 2026

# Opaque, Interoperable Passkey Records (and a Go API)

Passkeys are the most important thing happening in information security right now because they are the only principled solution to the overwhelming effectiveness of phishing attacks. Just like memory safety is the only principled solution to memory corruption attacks.

Unfortunately, implementing them on the server side can appear more complex than using password hashes. Part of this is unavoidable because passkeys require interaction with the browser to get their phishing resistance properties. Part of it, however, could be abstracted away a little more effectively by defining interoperable passkey record encodings.

The WebAuthn specification [defines](https://www.w3.org/TR/webauthn-3/#reg-ceremony-create-credential-record) a *credential record* as an abstract concept with a number of components such as `type`, `id`, `publicKey`, `backupState`, `transports`, and other flags. Google [recommends](https://developers.google.com/identity/passkeys/developer-guides/server-registration#store_the_public_key) a database table with a Credential ID primary key, and `public_key`, `backed_up`, and `transports` columns. Adam Langley’s stellar [Tour of WebAuthn](https://www.imperialviolet.org/tourofwebauthn/tourofwebauthn.html#the-server-side) similarly recommends a `cred_id` primary key, and separate `public_key_spki` and `backed_up` columns.

All guidance recommends using libraries to handle WebAuthn authentication, but that still leaves applications with a potentially non-interoperable database schema. It might also be impractical to defer the whole authentication flow and database interaction to a library or framework.

Interoperable, well-specified passkey records that the application can handle as opaque strings, like password hashes, can be a middle-ground abstraction layer.

[c2sp.org/passkey-record](https://github.com/C2SP/C2SP/blob/push-oxkkyrwpqxot/passkey-record.md) is a specification proposal which borrows the syntax of [Password Hashing Competition (PHC) Strings](https://c2sp.org/phc-strings) and reuses the existing authenticator data encoding for the bulk of the work. A record looks like this:

```
$webauthn$v=1$transports=hybrid+internal$<base64 authenticator data>
```

The payload is the authenticator data, a CTAP2 CBOR encoding of most of the credential record fields that is already [specified by WebAuthn](https://www.w3.org/TR/webauthn-3/#sctn-authenticator-data) and included in the JSON encoding of an [AuthenticatorAttestationResponse](https://developer.mozilla.org/en-US/docs/Web/API/AuthenticatorAttestationResponse) (which is the return type of [`navigator.credentials.create()`](https://developer.mozilla.org/en-US/docs/Web/API/CredentialsContainer/create) even if attestation is not in use). Transports are the only missing field, and they are stored as PHC parameters.

The application is then only in charge of keeping track of what passkey records are associated with a user account, which is a task that is familiar to web developers because it is not dissimilar to implementing password authentication (except there are multiple passkeys per account). These opaque strings can be passed to a library to verify the login assertion (or to generate a registration request with the appropriate `excludedCredentials`).

With a well-specified interoperable storage format, it will hopefully be possible to switch passkey library (or even backend language) while preserving a credentials database.

## Other fields you might want to store

Along with the passkey record, applications might still wish to store metadata fields like a user-selected nickname and creation and last use timestamps, to provide pretty passkey management UIs. None of these require any special treatment by the WebAuthn library.

The one exception is the backed up state flag. Passkeys report to the server whether they are backed up (e.g. to iCloud Keychain or a Google account), and servers can use that signal to suggest removing a password from an account. This flag can change across logins, while the passkey record is immutable, so it would have to be stored separately and updated on every login. I think this logic is overrated for the average website, which will keep supporting email password resets anyway.

## A potential crypto/passkey API

Building on top of these passkey records, I drafted [a potential `crypto/passkey` stateless Go package API](https://godoc-play.exe.xyz/chibklhpf6nn).

The registration flow is

1. call [`RelyingParty.NewRegistration`](https://godoc-play.exe.xyz/chibklhpf6nn#RelyingParty.NewRegistration) with the logged-in (or otherwise identified) user details and any existing passkey records
2. pass the returned JSON to `parseCreationOptionsFromJSON()` and then to `navigator.credentials.create()`
3. pass the returned JSON-encoded PublicKeyCredential to [`RelyingParty.Register`](https://godoc-play.exe.xyz/chibklhpf6nn#RelyingParty.Register)
4. store the returned passkey record in the database

The login flow is

1. call [`RelyingParty.NewLogin`](https://godoc-play.exe.xyz/chibklhpf6nn#RelyingParty.NewLogin) while generating the log-in page
2. store the returned request in a key-value cache with a short TTL, under [`RequestID(request)`](https://godoc-play.exe.xyz/chibklhpf6nn#RequestID), and pass the returned JSON to `parseRequestOptionsFromJSON()` and then to `navigator.credentials.get()`
3. pass the returned JSON-encoded PublicKeyCredential to [`Inspect`](https://godoc-play.exe.xyz/chibklhpf6nn#Inspect), and use the returned requestID to retrieve the request from the key-value cache and use the returned userID to retrieve the passkey records from the database
4. pass the JSON PublicKeyCredential, the request, and the passkey records to [`RelyingParty.Login`](https://godoc-play.exe.xyz/chibklhpf6nn#RelyingParty.Login)

The application is in charge of

* associating an opaque, permanent, privacy-preserving user ID with each user;
* storing passkey records associated with a user; and
* caching request challenges produced by `RelyingParty.NewLogin`.

The library provides JSON values that can be passed straight to [`parseCreationOptionsFromJSON()`](https://developer.mozilla.org/en-US/docs/Web/API/PublicKeyCredential/parseCreationOptionsFromJSON_static) and [`parseRequestOptionsFromJSON()`](https://developer.mozilla.org/en-US/docs/Web/API/PublicKeyCredential/parseRequestOptionsFromJSON_static), and accepts JSON values returned by [calling `JSON.stringify()` on a PublicKeyCredential](https://developer.mozilla.org/en-US/docs/Web/API/PublicKeyCredential/toJSON).

This is optimized for the discoverable credential flow (a.k.a. passkeys, where the authenticator stores and provides to the server the user ID) but the [`RelyingParty.NewLoginForUser`](https://godoc-play.exe.xyz/chibklhpf6nn#RelyingParty.NewLoginForUser) method can also be used for second-factor flows or re-authentication prompts. The API works for both modal and conditional UI (autofill) flows.

There are a few helpers to extract information from the passkey record ([`AAGUID`](https://godoc-play.exe.xyz/chibklhpf6nn#AAGUID), [`BackedUp`](https://godoc-play.exe.xyz/chibklhpf6nn#BackedUp)) and from the JSON-encoded PublicKeyCredential ([`ResponseBackedUp`](https://godoc-play.exe.xyz/chibklhpf6nn#ResponseBackedUp)).

Currently, there is no implementation; I would like to get feedback on the [passkey record format](https://github.com/C2SP/C2SP/blob/push-oxkkyrwpqxot/passkey-record.md) and on [the Go API](https://godoc-play.exe.xyz/chibklhpf6nn), before potentially making a proposal for Go 1.28.

## On duplicate Credential IDs

One thing you can’t do with this storage model is ensure that different accounts don’t share passkeys with the same Credential ID, which the spec says you SHOULD do.

The reason for that check is avoiding...