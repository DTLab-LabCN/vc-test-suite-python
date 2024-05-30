VCDM_V1_STATEMENTS = {
    "@context": [
        "Verifiable credentials MUST include a @context property.",
        "The value of the @context property MUST be an ordered set.",
        "The first item MUST be a URI with the value https://www.w3.org/2018/credentials/v1",
        "Subsequent items MUST be composed of URLs and/or objects each processable as a JSON-LD Context.",
    ],
    "id": [
        "A verifiable credential MAY have an id property.",
        "The value of the id property MUST be a single URI.",
        "It is RECOMMENDED that the URI in the id be one which, if dereferenced, results in a document containing machine-readable information about the id.",
    ],
    "type": [
        "Verifiable credentials MUST have a type property.",
        "The value of the type property MUST be, or map to, one or more URIs.",
        "MUST have VerifiableCredential",
        "MAY have a more specific verifiable credential type.",
        "All credentials, presentations, and encapsulated objects MUST specify, or be associated with, additional more narrow types.",
    ],
    "issuer": [
        "A verifiable credential MUST have an issuer property.",
        "The value of the issuer property MUST be either a URI or an object containing an id property.",
        "It is RECOMMENDED that the URI in the issuer or its id be one which, if dereferenced, results in a document containing machine-readable information about the issuer that can be used to verify the information expressed in the credential.",
    ],
    "issuanceDate": [
        "A credential MUST have an issuanceDate property.",
        "The value of the issuanceDate property MUST be a string value of an [XMLSCHEMA11-2] combined date-time string",
    ],
    "expirationDate": [
        "Verifiable credentials MAY have an expirationDate property.",
        "If present, the value of the expirationDate property MUST be a string value of an [XMLSCHEMA11-2] date-time"
    ],
    "credentialSubject": [
        "A verifiable credential MUST have a credentialSubject property.",
        "Each object MAY contain an id.",
    ],
    "credentialStatus": [
        "A verifiable credential MAY have a credentialStatus property.",
        "The value of the credentialStatus property MUST be one or more status objects",
        "If present, the value of the credentialStatus property MUST include id property, which MUST be a URI.",
        "If present, the value of the credentialStatus property MUST include type property",
    ],
    "credentialSchema": [
        "A verifiable credential MAY have a credentialSchema property.",
        "The value of the credentialSchema property MUST be one or more data schemas",
        "Each credentialSchema MUST specify its type.",
        "Each credentialSchema MUST specify its id property that MUST be a URI identifying the schema file.",
        "If a credential definition is being used, the credential definition MUST be defined in the credentialSchema property",
    ],
    "refreshService": [
        "A verifiable credential MAY have a refreshService property.",
        "The value of the refreshService property MUST be one or more refresh services",
        "Each refreshService MUST specify its type.",
        "Each refreshService MUST specify its id, which is the URI of the service.",
    ],
    "termsOfUse": [
        "A verifiable credential MAY have a termsOfUse property.",
        "The value of the termsOfUse property MUST specify one or more terms of use policies",
        "Each termsOfUse MUST specify its type.",
        "Each termsOfUse MAY specify its instance id.",
    ],
    "evidence": [
        "A verifiable credential MAY have a evidence property.",
        "The value of the evidence property MUST be one or more evidence schemes",
        "Each evidence MUST specify its type.",
        "Each evidence MAY specify an id which SHOULD contain a URL that points to where more information about this instance of evidence can be found..",
    ],
    "proof": [
        "A verifiable credential MUST have a proof property.",
        "At least one proof mechanism, and the details necessary to evaluate that proof, MUST be expressed.",
        "When embedding a proof, the proof property MUST be used.",
        "The specific method used for an embedded proof MUST be included using the type property.",
    ],
}

MDOC_STATEMENTS = {
    "docType": [],
    "issuerSigned": [],
    "issuerAuth": [],
    "issuerSignatures": [],
    "issuerNamespaces": [],
    "deviceSigned": [],
    "deviceAuth": [],
    "deviceSignatures": [],
    "deviceNamespaces": [],
}
