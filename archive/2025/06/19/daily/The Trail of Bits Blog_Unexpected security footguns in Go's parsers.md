---
title: Unexpected security footguns in Go's parsers
url: https://blog.trailofbits.com/2025/06/17/unexpected-security-footguns-in-gos-parsers/
source: The Trail of Bits Blog
date: 2025-06-19
fetch_date: 2025-10-06T22:52:13.820831
---

# Unexpected security footguns in Go's parsers

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Unexpected security footguns in Go's parsers

[Vasco Franco](https://github.com/Vasco-jofra)

June 17, 2025

[application-security](/categories/application-security/), [go](/categories/go/)

Page content

* [Parsing in Go](#parsing-in-go)
* [Attack scenario 1: (Un)Marshaling unexpected data](#attack-scenario-1-unmarshaling-unexpected-data)
  + [Fields without a tag](#fields-without-a-tag)
  + [Misusing the `-` tag](#misusing-the---tag)
  + [Misusing omitempty](#misusing-omitempty)
* [Attack scenario 2: Parser differentials](#attack-scenario-2-parser-differentials)
  + [Duplicate fields](#duplicate-fields)
  + [Case insensitive key matching](#case-insensitive-key-matching)
* [Attack scenario 3: Data format confusion](#attack-scenario-3-data-format-confusion)
  + [Unknown keys](#unknown-keys)
  + [Leading garbage data](#leading-garbage-data)
  + [Trailing garbage data](#trailing-garbage-data)
  + [Constructing a polyglot](#constructing-a-polyglot)
* [Mitigations](#mitigations)
  + [JSONv2](#jsonv2)
* [Key takeaways for developers](#key-takeaways-for-developers)

In Go applications, parsing untrusted data creates a dangerous attack surface that’s routinely exploited in the wild. During our security assessments, we’ve repeatedly exploited unexpected behaviors in Go’s JSON, XML, and YAML parsers to bypass authentication, circumvent authorization controls, and exfiltrate sensitive data from production systems.

These aren’t theoretical issues—they’ve led to documented vulnerabilities like [CVE-2020-16250](https://nvd.nist.gov/vuln/detail/cve-2020-16250) (a Hashicorp Vault authentication bypass found by Google’s Project Zero) and numerous high-impact findings in our client engagements.

This post contextualizes these unexpected parser behaviors through three attack scenarios that every security engineer and Go developer should understand:

1. **(Un)Marshaling unexpected data**: How Go parsers can expose data that developers intended to be private
2. **Parser differentials**: How discrepancies between parsers enable attackers to bypass security controls when multiple services parse the same input
3. **Data format confusion**: How parsers process cross-format payloads with surprising and exploitable results

We’ll demonstrate each attack scenario with real-world examples and conclude with concrete recommendations for configuring these parsers more securely, including strategies to compensate for security gaps in Go’s standard library.

Below is a summary of the surprising behaviors we’ll examine, with indicators showing their security status:

* 🟢 **Green**: Secure by default
* 🟠 **Orange**: Insecure by default but configurable
* 🔴 **Red**: Insecure by default with no secure configuration options

|  | JSON | JSON v2 | XML | YAML |
| --- | --- | --- | --- | --- |
| json:"-,…" | YES (bad design) | YES (bad design) | YES (bad design) | YES (bad design) |
| json:“omitempty” | YES (expected) | YES (expected) | YES (expected) | YES (expected) |
| Duplicate keys | YES (last) | NO | YES (last) | NO |
| Case insensitivity | YES | NO | NO | NO |
| Unknown keys | YES (mitigable) | YES (mitigable) | YES | YES (mitigable) |
| Garbage leading data | NO | NO | YES | NO |
| Garbage trailing data | YES (with Decoder) | NO | YES | NO |

## Parsing in Go

Let’s examine how Go parses JSON, XML, and YAML. Go’s standard library provides JSON and XML parsers but not a YAML parser, for which there are several third-party alternatives. For our analysis, we’ll focus on:

* [encoding/json](https://pkg.go.dev/encoding/json) version go1.24.1
* [encoding/xml](https://pkg.go.dev/encoding/xml) version go1.24.1
* [yaml.v3](https://pkg.go.dev/gopkg.in/yaml.v3) version 3.0.1 (the most popular third-party Go YAML library)

We’ll use JSON in our following examples, but all three parsers have APIs equivalent to the ones we’ll see.

At their core, these parsers provide two primary functions:

* `Marshal` (serialize): Converts Go structs into their respective format strings
* `Unmarshal` (deserialize): Converts format strings back into Go structs

![Parsing JSON in Go](/img/go-parser-footguns/json_parsing.png)

Go uses struct field tags to allow customization of how parsers should handle individual fields. These tags consist of:

* A **key name** for serialization/deserialization
* Optional **comma-separated directives** that modify behavior (e.g., the `omitempty` tag option tells the JSON serializer not to include the field in the JSON output string if it is empty)

```
type User struct {
    Username string `json:"username_json_key,omitempty"`
    Password string `json:"password"`
    IsAdmin  bool   `json:"is_admin"`
}
```

To unmarshal a JSON string into the `User` structure shown above, we must use the `username_json_key` key for the `Username` field, `password` for the `Password` field, and `is_admin` for the `IsAdmin` field.

```
u := User{}
_ = json.Unmarshal([]byte(`{
    "username_json_key": "jofra",
    "password": "qwerty123!",
    "is_admin": "false"
}`), &u)
fmt.Printf("Result: %#v\n", u)
// Result: User{Username:"jofra", Password:"qwerty123!", IsAdmin:false}
```

These parsers also offer stream-based alternatives that operate on `io.Reader` interfaces rather than `byte` slices. This API is ideal for parsing streaming data such as HTTP request bodies, making it a preferred choice in HTTP request handling.

![Parsing JSON in Go with NewDecoder](/img/go-parser-footguns/json_parsing_2.png)

---

## Attack scenario 1: (Un)Marshaling unexpected data

Sometimes, you need to limit which fields of a structure can be marshaled or unmarshaled.

Let’s consider a simple example in which a back-end server has an HTTP handler for creating users and another for retrieving that user after authentication.

When creating a user, you may not want the user to be able to set the `IsAdmin` field (i.e., unmarshal that field from the user input).

![Shows an interaction with a backend server in which the user can set the IsAdmin field of the User struct, which should not be possible](/img/go-parser-footguns/create_user.png)

Similarly, when fetching the user, you may not want the user to return the user’s `Password` or other secret values.

![Shows an interaction with a backend server in which the user can get the Password field of the User struct, which should not be possible](/img/go-parser-footguns/get_user.png)

How can we instruct the parsers not to marshal or unmarshal a field?

### Fields without a tag

Let’s first see what happens if you don’t set a JSON tag.

```
type User struct {
    Username string
}
```

In this case, you can unmarshal the `Username` field with its name, as shown below.

```
_ = json.Unmarshal([]byte(`{"Username": "jofra"}`), &u)
// Result: User{Username:"jofra"}
```

This is well documented, and most Go devs are aware of it. Let’s look at another example:

```
type User struct {
    Username string `json:"username,omitempty"`
    Password string `json:"password,omitempty"`
    IsAdmin  bool
}
```

Is it evident that the `IsAdmin` field above would be unmarshaled? A less senior or distracted developer could assume it would not and introduce a security vulnerability.

If you’d like to scan your codebase for this pattern, where some but not all fields have a JSON, XML, or YAML tag, you can use the following Semgrep rule. This rule is not on the our [collection of rules exposed on the Semgrep registry](https://semgrep.dev/p/trailofbits) because, depending on the codebase, it is likely to produce many false positives.

```
rules:
    - id: unmarshaling-tag-in-only-some-fields
      message: >-
          Type $T1 has fields with json/yml/xml tags on some but not other fields. This field can still be (un)marshaled using its name. To prevent a field from being (un)marshaled, use the - tag.
      languages: [go]
      severity: WARNING
      patterns...