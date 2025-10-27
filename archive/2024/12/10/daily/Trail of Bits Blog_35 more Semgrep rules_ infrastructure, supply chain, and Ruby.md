---
title: 35 more Semgrep rules: infrastructure, supply chain, and Ruby
url: https://blog.trailofbits.com/2024/12/09/35-more-semgrep-rules-infrastructure-supply-chain-and-ruby/
source: Trail of Bits Blog
date: 2024-12-10
fetch_date: 2025-10-06T19:37:07.018592
---

# 35 more Semgrep rules: infrastructure, supply chain, and Ruby

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# 35 more Semgrep rules: infrastructure, supply chain, and Ruby

Matt Schwager, Travis Peters

December 09, 2024

[application-security](/categories/application-security/), [semgrep](/categories/semgrep/)

We are publishing another set of [custom Semgrep rules](https://github.com/trailofbits/semgrep-rules/pull/69), bringing our total number of public rules to 115. This blog post will briefly cover the new rules, then explore two Semgrep features in depth: regex mode (especially how it compares against generic mode), and HCL language support for technologies such as Terraform and Nomad. With these features, we can search for security vulnerabilities in more than just application code. This new release joins our existing collection of [Semgrep rules](https://github.com/trailofbits/semgrep-rules), our [public CodeQL queries](https://github.com/trailofbits/codeql-queries), and our [Testing Handbook](https://appsec.guide/) as part of our long-term effort to share our technical expertise with the security community.

Semgrep is a vast and capable tool, and it contains many nooks and crannies that can be exploited to get the most value possible out of a static analysis tool. Like our [previous Semgrep rules release post](https://blog.trailofbits.com/2024/01/17/30-new-semgrep-rules-ansible-java-kotlin-shell-scripts-and-more/), this post will highlight some interesting Semgrep functionality. Publicly releasing rules is a great start, but we feel that we can do even better by explaining *why* rules are written the way they are.

For this release, we focused on supply chain issues related to a lack of [short-lived OIDC tokens](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect) in GitHub Actions; infrastructure concerns in Terraform code, Nomad jobs, and insecure database connections; and general application security concerns in Ruby code. Many of these Ruby rules were written during our recent Ruby Central (rubygems.org) audit. We will be publishing more information about this audit shortly.

Without further ado, here are our new rules:

| Mode | Rule ID | Rule description |
| --- | --- | --- |
| Ruby | `action-dispatch-insecure-ssl` | Found Rails application with insecure SSL setting. |
| Ruby | `action-mailer-insecure-tls` | Found ActionMailer SMTP configuration with insecure TLS setting. These settings do not require a successful, encrypted, verified TLS connection is made. Set `enable_starttls: true` and `openssl_verify_mode` to verify peer. |
| Ruby | `active-record-encrypts-misorder` | Found an ActiveRecord value with encryption before serialization. The declaration of the serialized attribute should go before the encryption declaration. |
| Ruby | `active-record-hardcoded-encryption-key` | Found hard-coded ActiveRecord encryption key. |
| Ruby | `global-timeout` | Found `Timeout::timeout` (or `timeout`) use. Setting a global timeout can cause an exception to be raised anywhere in the passed block of code. This precludes any possible clean up action typically associated with rescuing from exceptions. This can lead to denial-of-service, data integrity failure, and general availability concerns. Instead prefer to use the library’s built in timeout functionality, if it has any, to ensure processing happens as expected. If it does not have built in timeout functionality, then consider implementing it. |
| Ruby | `faraday-disable-verification` | Found Faraday HTTP request disabling SSL/TLS verification. |
| Ruby | `ruby-saml-skip-validation` | SAML response validation disabled for $`KEY`. |
| Ruby | `yaml-unsafe-load` | Found YAML call to `unsafe_load`. This can lead to deserialization bugs and RCE. |
| Ruby | `rails-cookie-attributes` | Found Rails cookie set with insecure attribute. |
| Ruby | `rails-cache-store-marshal` | Found Rails cache store configured to allow Marshaling. As of Rails 7.1 the default serializer is `:marshal_7_1`. If an attacker can inject data into the cache store (SSRF, etc.), then they can achieve code execution when the object is later deserialized. Consider using the `:message_pack` serializer or a custom serializer. |
| Ruby | `json-create-deserialization` | Found `json_create` class method. This implies custom JSON deserialization is occuring. This can lead to RCE and other deserialization-type bugs. Usage should be audited and, at least, fuzzed. |
| Ruby | `insecure-rails-cookie-session-store` | Found Rails session cookie missing `SameSite=Secure`. As of Rails 7.2, session cookies default to `SameSite=Lax`. |
| Ruby | `rest-client-disable-verification` | Found RestClient HTTP request disabling SSL/TLS verification. |
| Regex | `postgres-insecure-sslmode` | Found PostgreSQL connection string disabling SSL verification. |
| Regex | `mongodb-insecure-transport` | Found insecure MongoDB connection, prefer TLS encrypted transport by setting the `tls=true` connection option and ensuring proper verification. |
| Regex | `mysql-insecure-sslmode` | Found MySQL connection string disabling SSL verification. |
| Generic | `amqp-unencrypted-transport` | Found unencrypted AMQP connection, prefer TLS encrypted `amqps://` transport. |
| Generic | `redis-unencrypted-transport` | Found unencrypted Redis connection, prefer TLS encrypted `rediss://` transport. |
| Generic | `node-disable-certificate-validation` | Setting this environment variable disables TLS certificate validation. This makes TLS, and HTTPS by extension, insecure. The use of this environment variable is strongly discouraged. |
| HCL | `aws-oidc-role-policy-duplicate-condition` | Found AWS role policy for GitHub Actions with duplicate condition. This overrides previous conditions, and the last condition with the duplicated key “wins.” This likely breaks access controls and allows unauthorized access. |
| HCL | `aws-oidc-role-policy-missing-sub` | Found AWS role policy for GitHub Actions missing OIDC subject. This means any GitHub repository can assume this role in CI. |
| HCL | `vault-hardcoded-token` | Found Terraform Vault instance with hard-coded token. |
| HCL | `vault-skip-tls-verify` | Found Terraform Vault instance with TLS verification disabled. |
| HCL | `root-user` | Found Nomad task using root user. |
| HCL | `docker-hardcoded-password` | Found Nomad task using Docker auth with hard-coded password. |
| HCL | `docker-privileged-mode` | Found Nomad task using Docker containers in privileged mode. |
| HCL | `tls-hostname-verification-disabled` | Found Nomad `tls` block with server hostname verification disabled. |
| HCL | `podman-tls-verify-disabled` | Found Nomad task using Podman with registry TLS verification disabled. |
| YAML | `jfrog-hardcoded-credential` | Found long-term access key. Instead prefer JFrog temporary OIDC security credentials. |
| YAML | `aws-secret-key` | Found long-term access key. Instead prefer AWS role assumption and temporary OIDC security credentials. |
| YAML | `gcp-credentials-json` | Found long-term access key. Instead prefer GCP workload identity federation and temporary OIDC security credentials. |
| YAML | `rubygems-publish-key` | Found long-term access key. Instead prefer RubyGems trusted publishing and temporary OIDC security credentials. |
| YAML | `vault-token` | Found long-term access key. Instead prefer Vault role assumption and temporary OIDC security credentials. |
| YAML | `pypi-publish-password` | Found long-term access key. Instead prefer PyPI trusted publishing and temporary OIDC security credentials. |
| YAML | `azure-principal-secret` | Found long-term access key. Instead prefer Azure subscription ID and temporary OIDC security credentials. |

### Semgrep isn’t just for programming languages

The [first post](https://blog.trailofbits.com/2024/01/17/30-new-semgrep-rules-ansible-java-kotlin-shell-scripts-and-more/) in th...