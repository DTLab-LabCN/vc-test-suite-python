## Files that are within the repository

This repository contains a script(valid_vc_generator.py) for generating Verifiable credentials that abide by normative statements provided by the W3c data model 1.1 & 2.0 specification.This ensures that all the required attributes with a chosen set of arbitrary one are combined.It also contains a validator script(maximus_validator.py) that takes .json files in a seperate directory for checking whether a credential abides by the normative statements provided by the W3C Verifiable credential data model 1.1 & 2.0 specification. Their is also a report pdf(Report_DTLab.pdf) providing further clarification on the functionality of the two scripts along with a greater context of the purposes of these scripts. Their are also existing test suites that are used within this repository. The validator utilizes the test suites that either abide or violate the normative statements for w3c data model 1.1 which can be found in dtt-test-api/tests_scripts/input. Their are test suites within the repository that abide or violate the normative statements for w3c data model 2.0 which can be found in tests/input.

## Getting started

For generating verifiable credentials:
```bash
python3 valid_vc_generator.py
```

Example output of generating verifiable credentials:
```bash
•generating attribute VerifiableCredential
 •generating attribute credentialSubject
  ◦['http://1edtech.edu/credentials/3732', {'id': 'http://1edtech.edu/credentials/3732'}] assigned to credentialSubject
 •generating attribute issuer
  ◦['http://1edtech.edu/credentials/3732', {'id': 'http://1edtech.edu/credentials/3732'}] assigned to issuer
 •generating attribute id
  ◦['http://1edtech.edu/credentials/3732', {'id': 'http://1edtech.edu/credentials/3732'}] assigned to id
 •generating attribute type
  ◦None assigned to type
 •generating attribute credentialSchema
  •generating attribute type
   ◦random-string assigned to type
  •generating attribute id
   ◦http://1edtech.edu/credentials/3732 assigned to id
  ◦[{'type': 'random-string', 'id': 'http://1edtech.edu/credentials/3732'}] assigned to credentialSchema
 •generating attribute credentialStatus
  ◦[{'type': 'https://www.w3.org/ns/credentials/status#BitstringStatusListCredential'}] assigned to credentialStatus
 •generating attribute description
  ◦None assigned to description
 •generating attribute evidence
  •generating attribute type
   ◦random-string assigned to type
  ◦[{'type': 'random-string'}] assigned to evidence
 •generating attribute validFrom
  ◦['2024-08-30T14:05:54Z'] assigned to validFrom
 •generating attribute validUntil
  ◦['2024-08-30T14:05:54Z'] assigned to validUntil
 •generating attribute name
  ◦None assigned to name
 •generating attribute proof
  •generating attribute type
   ◦random-string assigned to type
  ◦[{'type': 'random-string'}] assigned to proof
 •generating attribute refreshService
  •generating attribute id
   ◦http://1edtech.edu/credentials/3732 assigned to id
  •generating attribute type
   ◦random-string assigned to type
  ◦[{'id': 'http://1edtech.edu/credentials/3732', 'type': 'random-string'}] assigned to refreshService
 •generating attribute termsOfUse
  •generating attribute type
   ◦random-string assigned to type
  ◦[{'type': 'random-string'}] assigned to termsOfUse
 •generating attribute confidenceMethod
  ◦['http://1edtech.edu/credentials/3732', {'id': 'http://1edtech.edu/credentials/3732'}] assigned to confidenceMethod
 •generating attribute relatedResource
  ◦['http://1edtech.edu/credentials/3732', {'id': 'http://1edtech.edu/credentials/3732'}] assigned to relatedResource
```

For validating Verifiable credentials:
```bash
python3 maximus_validator.py
```

Outputted prompt:
```bash
Enter a)V2.0 or b)V1.1: c)For generated VC's
```

## If selecting Option A
The validator will validate the test suites regarding the w3c data model V2.0 specification.

Example output:
```bash
credential-status-missing-id-ok.json
INFO:root:validating context
INFO:root:Checking required attributes for VerifiableCredential.
INFO:root:validating value of {'issuer': 'did:example:issuer', 'credentialSubject': {'id': 'did:example:subject'}, 'credentialStatus': {'type': 'CredentialStatusList2017'}} for VerifiableCredential
INFO:root:Checking required attributes for issuer.
INFO:root:validating value of did:example:issuer for @id
INFO:root:Checking required attributes for credentialSubject.
INFO:root:validating value of {'id': 'did:example:subject'} for @id
INFO:root:Checking required attributes for credentialStatus.
ERROR:root:Invalid URI: CredentialStatusList2017
ERROR:root:Restriction Restriction.MustBeUrl is not satisfied for credentialStatus
INFO:root:validating value of {'type': 'CredentialStatusList2017'} for @id
wrong result for credential-status-missing-id-ok.json
False
-------------------------------------------
credential-ok.json
INFO:root:validating context
INFO:root:Checking required attributes for VerifiableCredential.
INFO:root:validating value of {'issuer': 'did:example:issuer', 'credentialSubject': {'id': 'did:example:subject'}} for VerifiableCredential
INFO:root:Checking required attributes for issuer.
INFO:root:validating value of did:example:issuer for @id
INFO:root:Checking required attributes for credentialSubject.
INFO:root:validating value of {'id': 'did:example:subject'} for @id
True
-------------------------------------------
```
## If selecting Option B
The validator will validate the test suites regarding the w3c data model V1.1 specification.
Example output:
```bash
example-016-jwt-presentation-no-iss.jsonld
INFO:root:validating context
INFO:root:Checking required attributes for VerifiablePresentation.
INFO:root:validating value of {'verifiableCredential': ['eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRpZDpleGFtcGxlOmFiZmUxM2Y3MTIxMjA0MzFjMjc2ZTEyZWNhYiNrZXlzLTEifQ.eyJzdWIiOiJkaWQ6ZXhhbXBsZTplYmZlYjFmNzEyZWJjNmYxYzI3NmUxMmVjMjEiLCJqdGkiOiJodHRwOi8vZXhhbXBsZS5lZHUvY3JlZGVudGlhbHMvMzczMiIsImlzcyI6Imh0dHBzOi8vZXhhbXBsZS5jb20va2V5cy9mb28uandrIiwibmJmIjoxNTQxNDkzNzI0LCJpYXQiOjE1NDE0OTM3MjQsImV4cCI6MTU3MzAyOTcyMywibm9uY2UiOiI2NjAhNjM0NUZTZXIiLCJ2YyI6eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSIsImh0dHBzOi8vd3d3LnczLm9yZy8yMDE4L2NyZWRlbnRpYWxzL2V4YW1wbGVzL3YxIl0sInR5cGUiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJVbml2ZXJzaXR5RGVncmVlQ3JlZGVudGlhbCJdLCJjcmVkZW50aWFsU3ViamVjdCI6eyJkZWdyZWUiOnsidHlwZSI6IkJhY2hlbG9yRGVncmVlIiwibmFtZSI6IjxzcGFuIGxhbmc9J2ZyLUNBJz5CYWNjYWxhdXLDqWF0IGVuIG11c2lxdWVzIG51bcOpcmlxdWVzPC9zcGFuPiJ9fX19.KLJo5GAyBND3LDTn9H7FQokEsUEi8jKwXhGvoN3JtRa51xrNDgXDb0cq1UTYB-rK4Ft9YVmR1NI_ZOF8oGc_7wAp8PHbF2HaWodQIoOBxxT-4WNqAxft7ET6lkH-4S6Ux3rSGAmczMohEEf8eCeN-jC8WekdPl6zKZQj0YPB1rx6X0-xlFBs7cl6Wt8rfBP_tZ9YgVWrQmUWypSioc0MUyiphmyEbLZagTyPlUyflGlEdqrZAv6eSe6RtxJy6M1-lD7a5HTzanYTWBPAUHDZGyGKXdJw-W_x0IWChBzI8t3kpG253fg6V3tPgHeKXE94fz_QpYfg--7kLsyBAfQGbg']} for VerifiablePresentation
INFO:root:Checking required attributes for verifiableCredential.
INFO:root:validating value of eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRpZDpleGFtcGxlOmFiZmUxM2Y3MTIxMjA0MzFjMjc2ZTEyZWNhYiNrZXlzLTEifQ.eyJzdWIiOiJkaWQ6ZXhhbXBsZTplYmZlYjFmNzEyZWJjNmYxYzI3NmUxMmVjMjEiLCJqdGkiOiJodHRwOi8vZXhhbXBsZS5lZHUvY3JlZGVudGlhbHMvMzczMiIsImlzcyI6Imh0dHBzOi8vZXhhbXBsZS5jb20va2V5cy9mb28uandrIiwibmJmIjoxNTQxNDkzNzI0LCJpYXQiOjE1NDE0OTM3MjQsImV4cCI6MTU3MzAyOTcyMywibm9uY2UiOiI2NjAhNjM0NUZTZXIiLCJ2YyI6eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSIsImh0dHBzOi8vd3d3LnczLm9yZy8yMDE4L2NyZWRlbnRpYWxzL2V4YW1wbGVzL3YxIl0sInR5cGUiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJVbml2ZXJzaXR5RGVncmVlQ3JlZGVudGlhbCJdLCJjcmVkZW50aWFsU3ViamVjdCI6eyJkZWdyZWUiOnsidHlwZSI6IkJhY2hlbG9yRGVncmVlIiwibmFtZSI6IjxzcGFuIGxhbmc9J2ZyLUNBJz5CYWNjYWxhdXLDqWF0IGVuIG11c2lxdWVzIG51bcOpcmlxdWVzPC9zcGFuPiJ9fX19.KLJo5GAyBND3LDTn9H7FQokEsUEi8jKwXhGvoN3JtRa51xrNDgXDb0cq1UTYB-rK4Ft9YVmR1NI_ZOF8oGc_7wAp8PHbF2HaWodQIoOBxxT-4WNqAxft7ET6lkH-4S6Ux3rSGAmczMohEEf8eCeN-jC8WekdPl6zKZQj0YPB1rx6X0-xlFBs7cl6Wt8rfBP_tZ9YgVWrQmUWypSioc0MUyiphmyEbLZagTyPlUyflGlEdqrZAv6eSe6RtxJy6M1-lD7a5HTzanYTWBPAUHDZGyGKXdJw-W_x0IWChBzI8t3kpG253fg6V3tPgHeKXE94fz_QpYfg--7kLsyBAfQGbg for @id
ERROR:root:Invalid URI: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRpZDpleGFtcGxlOmFiZmUxM2Y3MTIxMjA0MzFjMjc2ZTEyZWNhYiNrZXlzLTEifQ.eyJzdWIiOiJkaWQ6ZXhhbXBsZTplYmZlYjFmNzEyZWJjNmYxYzI3NmUxMmVjMjEiLCJqdGkiOiJodHRwOi8vZXhhbXBsZS5lZHUvY3JlZGVudGlhbHMvMzczMiIsImlzcyI6Imh0dHBzOi8vZXhhbXBsZS5jb20va2V5cy9mb28uandrIiwibmJmIjoxNTQxNDkzNzI0LCJpYXQiOjE1NDE0OTM3MjQsImV4cCI6MTU3MzAyOTcyMywibm9uY2UiOiI2NjAhNjM0NUZTZXIiLCJ2YyI6eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSIsImh0dHBzOi8vd3d3LnczLm9yZy8yMDE4L2NyZWRlbnRpYWxzL2V4YW1wbGVzL3YxIl0sInR5cGUiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJVbml2ZXJzaXR5RGVncmVlQ3JlZGVudGlhbCJdLCJjcmVkZW50aWFsU3ViamVjdCI6eyJkZWdyZWUiOnsidHlwZSI6IkJhY2hlbG9yRGVncmVlIiwibmFtZSI6IjxzcGFuIGxhbmc9J2ZyLUNBJz5CYWNjYWxhdXLDqWF0IGVuIG11c2lxdWVzIG51bcOpcmlxdWVzPC9zcGFuPiJ9fX19.KLJo5GAyBND3LDTn9H7FQokEsUEi8jKwXhGvoN3JtRa51xrNDgXDb0cq1UTYB-rK4Ft9YVmR1NI_ZOF8oGc_7wAp8PHbF2HaWodQIoOBxxT-4WNqAxft7ET6lkH-4S6Ux3rSGAmczMohEEf8eCeN-jC8WekdPl6zKZQj0YPB1rx6X0-xlFBs7cl6Wt8rfBP_tZ9YgVWrQmUWypSioc0MUyiphmyEbLZagTyPlUyflGlEdqrZAv6eSe6RtxJy6M1-lD7a5HTzanYTWBPAUHDZGyGKXdJw-W_x0IWChBzI8t3kpG253fg6V3tPgHeKXE94fz_QpYfg--7kLsyBAfQGbg
ERROR:root:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRpZDpleGFtcGxlOmFiZmUxM2Y3MTIxMjA0MzFjMjc2ZTEyZWNhYiNrZXlzLTEifQ.eyJzdWIiOiJkaWQ6ZXhhbXBsZTplYmZlYjFmNzEyZWJjNmYxYzI3NmUxMmVjMjEiLCJqdGkiOiJodHRwOi8vZXhhbXBsZS5lZHUvY3JlZGVudGlhbHMvMzczMiIsImlzcyI6Imh0dHBzOi8vZXhhbXBsZS5jb20va2V5cy9mb28uandrIiwibmJmIjoxNTQxNDkzNzI0LCJpYXQiOjE1NDE0OTM3MjQsImV4cCI6MTU3MzAyOTcyMywibm9uY2UiOiI2NjAhNjM0NUZTZXIiLCJ2YyI6eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSIsImh0dHBzOi8vd3d3LnczLm9yZy8yMDE4L2NyZWRlbnRpYWxzL2V4YW1wbGVzL3YxIl0sInR5cGUiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJVbml2ZXJzaXR5RGVncmVlQ3JlZGVudGlhbCJdLCJjcmVkZW50aWFsU3ViamVjdCI6eyJkZWdyZWUiOnsidHlwZSI6IkJhY2hlbG9yRGVncmVlIiwibmFtZSI6IjxzcGFuIGxhbmc9J2ZyLUNBJz5CYWNjYWxhdXLDqWF0IGVuIG11c2lxdWVzIG51bcOpcmlxdWVzPC9zcGFuPiJ9fX19.KLJo5GAyBND3LDTn9H7FQokEsUEi8jKwXhGvoN3JtRa51xrNDgXDb0cq1UTYB-rK4Ft9YVmR1NI_ZOF8oGc_7wAp8PHbF2HaWodQIoOBxxT-4WNqAxft7ET6lkH-4S6Ux3rSGAmczMohEEf8eCeN-jC8WekdPl6zKZQj0YPB1rx6X0-xlFBs7cl6Wt8rfBP_tZ9YgVWrQmUWypSioc0MUyiphmyEbLZagTyPlUyflGlEdqrZAv6eSe6RtxJy6M1-lD7a5HTzanYTWBPAUHDZGyGKXdJw-W_x0IWChBzI8t3kpG253fg6V3tPgHeKXE94fz_QpYfg--7kLsyBAfQGbg for verifiableCredential is invalid
False
```
## If selecting Option C
The validator will validate the test suites regarding the generated test suites.
Example output:
```bash
34.json
INFO:root:validating context
INFO:root:Checking required attributes for VerifiableCredential.
INFO:root:validating value of {'credentialSubject': {'id': 'http://1edtech.edu/credentials/3732'}, 'issuer': {'id': 'http://1edtech.edu/credentials/3732'}, 'credentialStatus': {'type': 'https://www.w3.org/ns/credentials/status#BitstringStatusListCredential'}, 'description': 'unknown', 'evidence': {'type': 'random-string'}, 'name': 'unknown'} for VerifiableCredential
INFO:root:Checking required attributes for credentialSubject.
INFO:root:validating value of {'id': 'http://1edtech.edu/credentials/3732'} for @id
INFO:root:Checking required attributes for issuer.
INFO:root:validating value of {'id': 'http://1edtech.edu/credentials/3732'} for @id
INFO:root:Checking required attributes for credentialStatus.
INFO:root:validating value of {'type': 'https://www.w3.org/ns/credentials/status#BitstringStatusListCredential'} for @id
INFO:root:Checking required attributes for description.
INFO:root:validating value of unknown for None
INFO:root:Checking required attributes for evidence.
INFO:root:validating value of {'type': 'random-string'} for @id
INFO:root:Checking required attributes for name.
INFO:root:validating value of unknown for None
True
-------------------------------------------
```
