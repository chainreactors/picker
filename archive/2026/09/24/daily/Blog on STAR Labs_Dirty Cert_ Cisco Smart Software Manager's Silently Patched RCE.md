---
title: Dirty Cert: Cisco Smart Software Manager's Silently Patched RCE
url: https://starlabs.sg/blog/2026/09-dirty-cert-cisco-smart-software-managers-silently-patched-rce/
source: Blog on STAR Labs
date: 2026-09-24
fetch_date: 2026-09-25T06:51:53.831860
---

# Dirty Cert: Cisco Smart Software Manager's Silently Patched RCE

[![STAR Labs](/images/logo.png)](/)

[About](/about/)
[Services](/services/)
[Advisories](/advisories/)
[Blog](/blog/)
[Achievements](/achievements/)
[Publications](/publications/)
[Team](/team/)
[RSS](/index.xml)

MENU

Research
September 24, 2026
By Yap Yuan Xi (@h4log3n)
7 min read

# Dirty Cert: Cisco Smart Software Manager's Silently Patched RCE

## Introduction

Back in early August 2026, I was 0-day bug hunting in Cisco Smart Software Manager (CSSM). This was where I came across a post-auth RCE vulnerability. This vulnerability, located in the nginx certificate upload, involved command injection via TLS certificates. Unfortunately, a week before I finished the report, the vulnerability was silently patched in their 10-202608 upgrade uploaded on 10 Aug 2026. This short blog will detail the exploit, along with how it got patched.

## Backstory

CSSM is a licensing and account manager for multiple Cisco products such as their edge devices and networking software. It is distributed as an installable OS, running many microservices accessible via an nginx reverse proxy. I was testing out my newly built AI bug hunting harness, which managed to find this vulnerability within 1 hour!

## The Sink that Never Should’ve Been

Found within their nginx\_configurator, in `/frontend/usr/share/nginx/nginx_configurator/main.js`, are these two very interesting functions.

```
function valid_key(key) {
  try {
    childProcess.execSync(`echo "${key}" | openssl rsa > /dev/null`, {
      stdio: "inherit",
    });
    return true;
  } catch (e) {
    log(`Invalid key: ${e}`);
    return false;
  }
}

function valid_cert(cert) {
  try {
    childProcess.execSync(`echo "${cert}" | openssl x509 > /dev/null`, {
      stdio: "inherit",
    });
    return true;
  } catch (e) {
    log(`Invalid cert: ${e}`);
    return false;
  }
}
```

Cisco uses the `openssl` command to check for invalid certs and RSA keys. Using `childProcess.execSync` to do so is very risky, but very good for vulnerability researchers like me! It just so happens that these functions are called when I upload new certificates for nginx, so all we need is one malformed certificate to achieve command injection.

## Tracing through the code

With our target sink, we now begin tracing all the processing and functions our certificate payload goes through before reaching it.

### Validator’s Validation

Starting with the endpoint `/backend/settings/csr/upload` to upload our certs, we pass through the nginx reverse proxy to the backend service where we encounter a check under `/backend/usr/src/app/validators/admin/certs/csr/upload_validator.rb`

```
def validate(record)
    private_key = CsrPrivateKey.first
    record.errors.add(:base, I18n.t('browser_certs.cert_not_valid')) && return unless private_key.present?
    record.errors.add(:base, I18n.t('browser_certs.invalid_csr_cert')) && return unless valid_cert?(record, private_key)
    record.errors.add(:base, I18n.t('browser_certs.invalid_signature_algorithm')) && return if algorithm_rejected?(record.certificate)

    if record.intermediate_certificate.present?
        record.errors.add(:base, I18n.t('browser_certs.invalid_intermediate_cert')) && return unless valid_intermediate_cert?(record)
        record.errors.add(:base, I18n.t('browser_certs.invalid_intermediate_cert_signature_algorithm')) if algorithm_rejected?(record.intermediate_certificate)
    end
    rescue
    record.errors.add(:base,I18n.t('browser_certs.invalid_file_type'))
end

def valid_cert?(record, csr_private_key)
    ui_cert = OpenSSL::X509::Certificate.new(record.certificate)
    decrypted_key = EncryptionService.decrypt(csr_private_key.key_data)
    csr_rsa_private_key = OpenSSL::PKey::RSA.new(decrypted_key)

    CertService.rsa_keys_eql?(ui_cert.public_key, csr_rsa_private_key)
end

def valid_intermediate_cert?(record)
    user_cert = OpenSSL::X509::Certificate.new(record.certificate)
    intermediate_cert = OpenSSL::X509::Certificate.new(record.intermediate_certificate)

    user_cert.issuer == intermediate_cert.subject
rescue
    record.errors.add(:base,I18n.t('browser_certs.invalid_intermediate_cert'))
end
```

These functions check for:

1. Has the server made a Certificate Signing Request (CSR)?
2. Does the new certificate match the CSR?
3. Did the intermediate cert sign the new certificate?
4. Are the certificates signed using the allowed algorithms?
5. Do the certificates all follow the format under OpenSSL::X509::Certificate?

No. 1, we simply generate a CSR using the `/backend/settings/csr/generate` endpoint.
No. 2 and 3, we become the root CA and sign the CSR.
No. 4 is a non-factor, since the default openssl algorithm is allowlisted.

This last check, due to parsing of the request via `OpenSSL::X509::Certificate.new(record.certificate)`, is also not foolproof! The library follows RFC 7468 (“Textual Encodings of PKIX, PKCS, and CMS Structures”), and it states the following:

> **Explanatory Text**
>
> Many tools are known to emit explanatory text before the BEGIN and after the END lines for PKIX certificates, more than any other type. If emitted, such text SHOULD be related to the certificate, such as providing a textual representation of key data elements in the certificate.

By using explanatory text, we can add our command injection before the `-----BEGIN CERTIFICATE-----` header! Something akin to:

```
$(<COMMAND INJECTION>)
-----BEGIN CERTIFICATE-----
...
-----END CERTIFICATE-----
```

### Uneven Processing

After the validator, the backend processes the certificates before sending them back to nginx to update its certs. Under `/backend/usr/src/app/services/admin/ui_cert_service.rb` in the `upload_csr_certificate` function:

```
# Update UI Cert
ui_cert_entry = UICert.where(name: Constants::UI_CERT_DESC).first_or_initialize
ui_cert_entry.cert = ui_cert.to_pem
ui_cert_entry.private_key_id = csr_private_key.id
ui_cert_entry.description = description

if intermediate_certificate.present?
    intermediate_subject = OpenSSL::X509::Certificate.new(intermediate_certificate).subject
    trust_store_cert = TrustStoreCert.first_or_initialize
    trust_store_cert.name = intermediate_subject
    trust_store_cert.cert = intermediate_certificate
    trust_store_cert.description = description
    trust_store_cert.save
end

ui_private_key = UiPrivateKey.first
ui_private_key.key_data = csr_private_key.key_data

...

ui_cert_entry.private_key_id = ui_private_key.id

...

NginxConfiguratorService.save_key_and_cert(CONSTANTS::TLS_FOR_USER_INTERFACE, EncryptionService.decrypt(ui_private_key.key_data), build_pem_bundle(ui_cert_entry))
```

We focus specifically on these three lines of code:

```
ui_cert_entry.cert = ui_cert.to_pem

...

ui_private_key.key_data = csr_private_key.key_data

...

trust_store_cert.cert = intermediate_certificate
```

Our command injection can work in these three places:

1. The new certificate generated from the CSR
2. The private key used in the CSR
3. The `intermediate_certificate` that signed the CSR

(1) doesn’t work since `to_pem` strips our explanatory text and our command injection away, and (2) cannot be accessed by us. However, for (3), the `intermediate_certificate` is used directly with no processing, perfect for exploitation!

And with our command injection within the certs, the server calls the following:

```
NginxConfiguratorService.save_key_and_cert(
    CONSTANTS::TLS_FOR_USER_INTERFACE,
    EncryptionService.decrypt(ui_private_key.key_data),
    build_pem_bundle(ui_cert_entry)
)
```

`build_pem_bundle` is simply a concatenation of the certs and the chain of signers / issuers before it using `\n` as a delimiter. The specific code looks as such:

```
def build_pem_bundle(cert)
    pem = cert.cert
    signer = cert.signer_cert

    while signer != nil do
        pem += "\n" + signer.cert
        signer = signer.signer_cert
    end

    pem
end
```

And this is all prepared as a single HTTP request sent from the backend to the frontend.

### Final Nai...