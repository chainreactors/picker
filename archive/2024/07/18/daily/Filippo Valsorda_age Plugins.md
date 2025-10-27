---
title: age Plugins
url: https://words.filippo.io/dispatches/age-plugins/
source: Filippo Valsorda
date: 2024-07-18
fetch_date: 2025-10-06T17:39:02.618538
---

# age Plugins

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

17 Jul 2024

# age Plugins

[age](https://age-encryption.org) is a file encryption tool, library, and format. It lets you encrypt files to “recipients” and decrypt them with “identities”.

```
$ age-keygen -o key.txt
Public key: age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p
$ tar cvz ~/data | age -r age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p > data.tar.gz.age
$ age --decrypt -i key.txt data.tar.gz.age > data.tar.gz
```

You can encrypt a file to multiple recipients and decrypt it with any of the corresponding identities. There are built-in recipients for public keys and for password encryption, but age supports third-party recipient types at the format, library, and tool levels. These recipient implementations can offer alternative algorithms, support for specific hardware, or even make use of remote APIs such as cloud KMS.

That’s the one “[joint](https://www.imperialviolet.org/2016/05/16/agility.html)” in age, which otherwise aims for having no configurability.

At the format level, an age file starts with a header that includes “stanzas” each encrypting the file key to different recipients. The [specification](https://c2sp.org/age) requires ignoring unrecognized stanzas, so third-party ones can coexist with native ones.[1](#fn:tied)

Here’s for example the header of a file encrypted to both a native public key recipient, and to a YubiKey. Note the two stanzas, introduced by `->`.

```
age-encryption.org/v1
-> piv-p256 OIF48w A7onGmpObHNfTCVLkq0QA4r4GJmzQLc6aVMAZVhrdbKb
SZwqyoXyHDOkoIJqYvxbo2p6j6tLVHMurkLivzYFDm0
-> X25519 z2pytFfcbnyl/ARKy1VA1W7P41Otn4ei7dNnWkf/iWw
X4R193LCCdtkueqwJCSPRe/HifrrxfbO3Zu8E+OyDp8
--- iZ5zBQBDL2SzxIAM9iArGViXViYF4lqrvAh4WMLozUY
```

At the library level, there are two fundamental interfaces that provide this abstraction: `Recipient` and `Identity`.

```
// A Recipient is passed to Encrypt to wrap an opaque file key to one or more
// recipient stanza(s). It can be for example a public key like X25519Recipient,
// a plugin, or a custom implementation.
type Recipient interface {
    Wrap(fileKey []byte) ([]*Stanza, error)
}

// Encrypt encrypts a file to one or more recipients.
func Encrypt(dst io.Writer, recipients ...Recipient) (io.WriteCloser, error)

// An Identity is passed to Decrypt to unwrap an opaque file key from a
// recipient stanza. It can be for example a secret key like X25519Identity, a
// plugin, or a custom implementation.
//
// Unwrap must return an error wrapping ErrIncorrectIdentity if none of the
// recipient stanzas match the identity, any other error will be considered
// fatal.
type Identity interface {
    Unwrap(stanzas []*Stanza) (fileKey []byte, err error)
}

// Decrypt decrypts a file with one or more identities.
func Decrypt(src io.Reader, identities ...Identity) (io.Reader, error)
```

Any Go package can provide a type that implements a `Wrap` or `Unwrap` method, and pass it to `age.Encrypt` or `age.Decrypt` respectively.

That allows Go applications to use third-party recipients with the Go age library, but age is also a command-line tool. At the tool level, the [age plugin system](https://c2sp.org/age-plugin) exposes the Recipient and Identity interfaces over a language-agnostic stdin/stdout protocol.

Plugins are selected based on the name of the recipient or identity encoding. For example if you use `-r age1`**`yubikey`**`1qwt50d05nh5vutpdzmlg5wn80xq5negm4uj9ghv0snvdd3yysf5yw3rhl3t` the age CLI will invoke `age-plugin-yubikey` from `$PATH` to wrap the file key.[2](#fn:name) This means they can be mixed and matched with other plugins and native recipients.

Here’s an example transcript of decrypting the file from earlier with the YubiKey plugin, complete of the plugin asking the CLI to prompt the user for the PIN and of “grease” making sure the protocol doesn’t ossify. Note that [age-plugin-yubikey](https://github.com/str4d/age-plugin-yubikey) is developed by [str4d](https://github.com/str4d) in Rust, while the age CLI is developed by me in Go.

```
$ AGEDEBUG=plugin age -d -i age-yubikey-identity-388178f3.txt < test.age
send: -> add-identity AGE-PLUGIN-YUBIKEY-1XQJ0QQY48ZQH3UC845XQL
send:
send: -> recipient-stanza 0 piv-p256 OIF48w A7onGmpObHNfTCVLkq0QA4r4GJmzQLc6aVMAZVhrdbKb
send: SZwqyoXyHDOkoIJqYvxbo2p6j6tLVHMurkLivzYFDm0
send: -> recipient-stanza 0 X25519 z2pytFfcbnyl/ARKy1VA1W7P41Otn4ei7dNnWkf/iWw
send: X4R193LCCdtkueqwJCSPRe/HifrrxfbO3Zu8E+OyDp8
send: -> done
send:
recv: -> A:zw-grease /S?j#y$ geD 3P. .|
recv: daN05YWjoDuf83JNSWc4mN/qb1suAEYWXF6VsQA1qzCixeOk8s1Uv0Bh+dqHMYM
send: -> unsupported
send:
recv: -> request-secret
recv: RW50ZXIgUElOIGZvciBZdWJpS2V5IHdpdGggc2VyaWFsIDE1NzM3OTA0
send: -> ok
send: [REDACTED]
recv: -> file-key 0
recv: GHzIb/dwF93v8SwMuxVdPQ
send: -> ok
send:
recv: -> qBZE~*,s-grease
recv: OLL8DDYeq6NvadvOLjy/GRljAFuKpBkyT3vLd1OJ+4ve02Fi
send: -> unsupported
send:
recv: -> done
recv:
Frood!
```

The protocol only covers encryption and decryption. Plugins are expected to handle key generation in whatever way suits them best, usually by having users invoke the plugin binary directly.

The plugin architecture is now a few years old, and there are [some amazing plugins](https://github.com/FiloSottile/awesome-age?tab=readme-ov-file#plugins) out there, including stable [YubiKey](https://github.com/str4d/age-plugin-yubikey) and [Apple Secure Enclave](https://github.com/remko/age-plugin-se) ones, and experimental [TPM 2.0](https://github.com/Foxboron/age-plugin-tpm), [symmetric FIDO2](https://github.com/olastor/age-plugin-fido2-hmac), and even [Shamir’s Secret Sharing](https://github.com/olastor/age-plugin-sss) ones.

If a Go program wishes to use a plugin with the age library, we provide [Recipient](https://pkg.go.dev/filippo.io/age/plugin#Recipient) and [Identity](https://pkg.go.dev/filippo.io/age/plugin#Identity) implementations that automatically execute plugins to implement Wrap and Unwrap. Thanks to the careful mapping of the interface and plugin abstractions, the two are effectively interchangeable.

To complete the picture, last month Yolan Romailler and I designed an experimental Go framework to do the opposite: turn Recipient and Identity implementations into plugins, abstracting away the plugin protocol.

Assuming a library already implements `NewRecipient` and `NewIdentity` functions, building a plugin boils down to just a few lines in a `main()` function.

```
func main() {
    p, err := plugin.New("example")
    if err != nil {
        log.Fatal(err)
    }
    p.HandleRecipient(func(data []byte) (age.Recipient, error) {
        return NewRecipient(data)
    })
    p.HandleIdentity(func(data []byte) (age.Identity, error) {
        return NewIdentity(data)
    })
    os.Exit(p.Main())
}
```

The framework lets applications define their own CLI flags, for example for key generation, and supports the interactive features of the protocol such as displaying message or prompting the user.

It’s ready to try by `go get`-ing `filippo.io/age@filippo/plugin`, and was already [adopted by age-plugin-tpm](https://github.com/Foxboron/age-plugin-tpm/pull/24). [Docs are on pkg.go.dev.](https://pkg.go.dev/filippo.io/age%40v1.2.1-0.20240618131852-7eedd929a6cf/plugin#Plugin) Provide feedback in the [pull request](https://github.com/FiloSottile/age/pull/580).

The Rust ecosystem already has its equivalents in the [age::plugin](https://docs.rs/age/0.10.0/age/plugin/index.html) module and [age-plugin crate](https://crates.io/crates/age-plugin).

In related news, the [recent v1.2.0 release of age](https://github.com/FiloSottile/age/releases/tag/v1.2.0) introduced an extension to the Recipient interface—[RecipientWithLabels](https://pkg.go.dev/filippo.io/age#RecipientWithLabels)—which lets the recipient communicate to the age implementation its preferences on being mixed with other recipients, as a set of labels. For exa...