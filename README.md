# W3c Verifiable Credential Test-Suite

This repository contains scripts for testing an input against the W3C Verifiable Credential data model 1.1 specification. 

## Getting started

Setup a virtual environment and install the project:
```
python3 -m venv venv
. venv/bin/activate
./install.sh

```

Run your first test
```
vc_test_suite '{"@context": ["https://www.w3.org/2018/credentials/v1"]}'

```

Example results
```
{
  "conformant": false,
  "required_score": "4/8",
  "optional_score": "0/0",
  "verifications": {
    "@context": [
      {
        "statement": "Verifiable credentials MUST include a @context property.",
        "required": true,
        "pass": true
      },
      {
        "statement": "The value of the @context property MUST be an ordered set.",
        "required": true,
        "pass": true
      },
      {
        "statement": "The first item MUST be a URI with the value https://www.w3.org/2018/credentials/v1",
        "required": true,
        "pass": true
      },
      {
        "statement": "Subsequent items MUST be composed of URLs and/or objects each processable as a JSON-LD Context.",
        "required": true,
        "pass": true
      }
    ],
    "type": [
      {
        "statement": "Verifiable credentials MUST have a type property.",
        "required": true,
        "pass": false
      }
    ],
    "issuer": [
      {
        "statement": "A verifiable credential MUST have an issuer property.",
        "required": true,
        "pass": false
      }
    ],
    "issuanceDate": [
      {
        "statement": "A credential MUST have an issuanceDate property.",
        "required": true,
        "pass": false
      }
    ],
    "credentialSubject": [
      {
        "statement": "A verifiable credential MUST have a credentialSubject property.",
        "required": true,
        "pass": false
      }
    ]
  }
}
```