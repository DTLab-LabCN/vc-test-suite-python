from pyld import jsonld
import re
import json
import validators
import uritools
from vc_test_suite import messaging
from rfc3986 import is_valid_uri

def valid_xml_timestamp(timestamp):
    iso8601_regex = r"^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$"
    match_iso8601 = re.compile(iso8601_regex).match
    return False if match_iso8601(timestamp) is None else True

def test_data_model_v1(vc):
    verifications = {}
    required_test_count = 0
    optional_test_count = 0


    ### CONTEXT ###
    verifications["@context"] = []
    verifications["@context"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["@context"][0],
            "required": True,
            "pass": True if "@context" in vc else False,
        }
    )
    required_test_count += 1
    if '@context' in vc:
        verifications["@context"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["@context"][1],
                "required": True,
                "pass": (
                    True
                    if (isinstance(vc["@context"], list) and len(vc["@context"]) > 0)
                    else False
                ),
            }
        )
        required_test_count += 1
        verifications["@context"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["@context"][2],
                "required": True,
                "pass": (
                    True
                    if (
                        isinstance(vc["@context"], list)
                        and len(vc["@context"]) > 0
                        and vc["@context"][0] == "https://www.w3.org/2018/credentials/v1"
                    )
                    else False
                ),
            }
        )
        required_test_count += 1
        verifications["@context"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["@context"][3],
                "required": True,
                "pass": (
                    True
                    if all(isinstance(item, (dict, str)) for item in vc["@context"])
                    else False
                ),
            }
        )
        required_test_count += 1
        
    ### ID ###
    if 'id' in vc:
        verifications["id"] = []
        verifications["id"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["id"][0],
                "required": False,
                "pass": True if "id" in vc else False,
            }
        )
        optional_test_count += 1
        verifications["id"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["id"][1],
                "required": False,
                "pass": uritools.isuri(vc['id']),
            }
        )
        optional_test_count += 1

        
    ### TYPE ###
    verifications["type"] = []
    verifications["type"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["type"][0],
            "required": True,
            "pass": True if "type" in vc else False,
        }
    )
    required_test_count += 1
    if 'type' in vc:
        verifications["type"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["type"][2],
                "required": True,
                "pass": (
                    True
                    if (
                        isinstance(vc["type"], list)
                        and len(vc["type"]) > 0
                        and "VerifiableCredential" in vc["type"]
                    )
                    else False
                ),
            }
        )
        required_test_count += 1
        verifications["type"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["type"][3],
                "required": False,
                "pass": (
                    True
                    if (isinstance(vc["type"], list) and len(vc["type"]) > 1)
                    else False
                ),
            }
        )
        optional_test_count += 1

        
    ### ISSUER ###

    verifications["issuer"] = []
    verifications["issuer"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["issuer"][0],
            "required": True,
            "pass": True if "issuer" in vc else False,
        }
    )
    required_test_count += 1
    if 'issuer' in vc:
        verifications["issuer"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["issuer"][1],
                "required": True,
                "pass": (
                    True
                    if (isinstance(vc["issuer"], str) and uritools.isuri(vc["issuer"]))
                    or (
                        isinstance(vc["issuer"], dict)
                        and "id" in vc["issuer"]
                        and uritools.isuri(vc["issuer"]["id"])
                    )
                    else False
                ),
            }
        )
        required_test_count += 1




        
    ### ISSUANCE DATE ###

    verifications["issuanceDate"] = []
    verifications["issuanceDate"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["issuanceDate"][0],
            "required": True,
            "pass": True if "issuanceDate" in vc else False,
        }
    )
    required_test_count += 1
    if 'issuanceDate' in vc:
        verifications["issuanceDate"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["issuanceDate"][1],
                "required": True,
                "pass": valid_xml_timestamp(vc["issuanceDate"]),
            }
        )
        required_test_count += 1


        
    ### EXPIRATION DATE ###
    if 'expirationDate' in vc:
        verifications["expirationDate"] = []
        verifications["expirationDate"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["expirationDate"][0],
                "required": False,
                "pass": (
                    True if "expirationDate" in vc else False
                ),
            }
        )
        optional_test_count += 1
        verifications["expirationDate"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["expirationDate"][1],
                "required": True,
                "pass": valid_xml_timestamp(vc["expirationDate"]),
            }
        )
        required_test_count += 1


        
    ### CREDENTIAL SUBJECT ###

    verifications["credentialSubject"] = []
    verifications["credentialSubject"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["credentialSubject"][0],
            "required": True,
            "pass": True if "credentialSubject" in vc else False,
        }
    )
    required_test_count += 1
    if 'credentialSubject' in vc:
        verifications["credentialSubject"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["credentialSubject"][1],
                "required": False,
                "pass": (
                    True
                    if isinstance(vc["credentialSubject"], dict)
                    and "id" in vc["credentialSubject"]
                    and uritools.isuri(vc["credentialSubject"]['id'])
                    else False
                ),
            }
        )
        optional_test_count += 1

    required_test_pass = 0
    optional_test_pass = 0

        
    ### CREDENTIAL STATUS ###
    if "credentialStatus" in vc:
        verifications["credentialStatus"] = []
        verifications["credentialStatus"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["credentialStatus"][0],
                "required": False,
                "pass": (
                    True
                    if "credentialStatus" in vc
                    else False
                ),
            }
        )
        optional_test_count += 1
        verifications["credentialStatus"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["credentialStatus"][1],
                "required": False,
                "pass": (
                    True
                    if isinstance(vc["credentialStatus"], (list, dict))
                    else False
                ),
            }
        )
        optional_test_count += 1
        vc["credentialStatus"] = [vc["credentialStatus"]] if isinstance(vc["credentialStatus"], dict) else vc["credentialStatus"]
        verifications["credentialStatus"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["credentialStatus"][1],
                "required": False,
                "pass": (
                    True
                    if ("id" in evidence for evidence in vc["credentialStatus"])
                    else False
                ),
            }
        )
        optional_test_count += 1
        verifications["credentialStatus"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["credentialStatus"][2],
                "required": False,
                "pass": (
                    True
                    if ("type" in evidence for evidence in vc["credentialStatus"])
                    else False
                ),
            }
        )
        optional_test_count += 1

    # Schema
    if "credentialSchema" in vc:
        verifications["credentialSchema"] = []
        verifications["credentialSchema"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["credentialSchema"][0],
                "required": False,
                "pass": (
                    True
                    if "credentialSchema" in vc
                    else False
                ),
            }
        )
        optional_test_count += 1
        verifications["credentialSchema"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["credentialSchema"][1],
                "required": True,
                "pass": (
                    True
                    if isinstance(vc["credentialSchema"], (dict, list))
                    else False
                ),
            }
        )
        required_test_count += 1
        if isinstance(vc["credentialSchema"], (dict, list)):
            vc["credentialSchema"] = [vc["credentialSchema"]] if isinstance(vc["credentialSchema"], dict) else vc["credentialSchema"]

            verifications["credentialSchema"].append(
                {
                    "statement": messaging.VCDM_V1_STATEMENTS["credentialSchema"][2],
                    "required": True,
                    "pass": (
                        True
                        if ("id" in evidence for evidence in vc["credentialSchema"])
                        else False
                    ),
                }
            )
            required_test_count += 1
            verifications["credentialSchema"].append(
                {
                    "statement": messaging.VCDM_V1_STATEMENTS["credentialSchema"][3],
                    "required": True,
                    "pass": (
                        True
                        if ("type" in evidence for evidence in vc["credentialSchema"])
                        else False
                    ),
                }
            )
            required_test_count += 1

   

    # REFRESH
    if "refreshService" in vc:
        verifications["refreshService"] = []
        verifications["refreshService"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["refreshService"][0],
                "required": False,
                "pass": (
                    True
                    if "refreshService" in vc
                    else False
                ),
            }
        )
        optional_test_count += 1
        verifications["refreshService"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["refreshService"][1],
                "required": True,
                "pass": (
                    True
                    if isinstance(vc["refreshService"], (dict, list))
                    else False
                ),
            }
        )
        required_test_count += 1
        if isinstance(vc["refreshService"], (dict, list)):
            vc["refreshService"] = [vc["refreshService"]] if isinstance(vc["refreshService"], dict) else vc["refreshService"]

            verifications["refreshService"].append(
                {
                    "statement": messaging.VCDM_V1_STATEMENTS["refreshService"][2],
                    "required": True,
                    "pass": (
                        True
                        if ("id" in evidence for evidence in vc["refreshService"])
                        else False
                    ),
                }
            )
            required_test_count += 1
            verifications["refreshService"].append(
                {
                    "statement": messaging.VCDM_V1_STATEMENTS["refreshService"][3],
                    "required": True,
                    "pass": (
                        True
                        if ("type" in evidence for evidence in vc["refreshService"])
                        else False
                    ),
                }
            )
            required_test_count += 1

   

    # TERMS OF USE
    if "termsOfUse" in vc:
        verifications["termsOfUse"] = []
        verifications["termsOfUse"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["termsOfUse"][0],
                "required": False,
                "pass": (
                    True
                    if "termsOfUse" in vc
                    else False
                ),
            }
        )
        optional_test_count += 1
        verifications["termsOfUse"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["termsOfUse"][1],
                "required": True,
                "pass": (
                    True
                    if isinstance(vc["termsOfUse"], (dict, list))
                    else False
                ),
            }
        )
        required_test_count += 1
        if isinstance(vc["termsOfUse"], (dict, list)):
            vc["termsOfUse"] = [vc["termsOfUse"]] if isinstance(vc["termsOfUse"], dict) else vc["termsOfUse"]

            verifications["termsOfUse"].append(
                {
                    "statement": messaging.VCDM_V1_STATEMENTS["termsOfUse"][2],
                    "required": True,
                    "pass": (
                        True
                        if ("id" in evidence for evidence in vc["termsOfUse"])
                        else False
                    ),
                }
            )
            required_test_count += 1
            verifications["termsOfUse"].append(
                {
                    "statement": messaging.VCDM_V1_STATEMENTS["termsOfUse"][3],
                    "required": True,
                    "pass": (
                        True
                        if ("type" in evidence for evidence in vc["termsOfUse"])
                        else False
                    ),
                }
            )
            required_test_count += 1

  

    # EVIDENCE
    if "evidence" in vc:
        verifications["evidence"] = []
        verifications["evidence"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["evidence"][0],
                "required": False,
                "pass": (
                    True
                    if "evidence" in vc
                    else False
                ),
            }
        )
        optional_test_count += 1
        verifications["evidence"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["evidence"][1],
                "required": True,
                "pass": (
                    True
                    if isinstance(vc["evidence"], (dict, list))
                    else False
                ),
            }
        )
        required_test_count += 1
        if isinstance(vc["evidence"], (dict, list)):
            vc["evidence"] = [vc["evidence"]] if isinstance(vc["evidence"], dict) else vc["evidence"]

            verifications["evidence"].append(
                {
                    "statement": messaging.VCDM_V1_STATEMENTS["evidence"][2],
                    "required": True,
                    "pass": (
                        True
                        if ("id" in evidence for evidence in vc["evidence"])
                        else False
                    ),
                }
            )
            required_test_count += 1
            verifications["evidence"].append(
                {
                    "statement": messaging.VCDM_V1_STATEMENTS["evidence"][3],
                    "required": True,
                    "pass": (
                        True
                        if ("type" in evidence for evidence in vc["evidence"])
                        else False
                    ),
                }
            )
            required_test_count += 1
            


    # PROOF
    if 'proof' in vc:
        verifications["proof"] = []
        verifications["proof"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["proof"][2],
                "required": False,
                "pass": (
                    True
                    if "proof" in vc
                    else False
                ),
            }
        )
        optional_test_count += 1
        if isinstance(vc["proof"], (dict, list)):
            vc["proof"] = [vc["proof"]] if isinstance(vc["proof"], dict) else vc["proof"]
            verifications["proof"].append(
                {
                    "statement": messaging.VCDM_V1_STATEMENTS["proof"][3],
                    "required": True,
                    "pass": (
                        True
                        if ("type" in proof for proof in vc["proof"])
                        else False
                    ),
                }
            )
            required_test_count += 1

    required_test_pass = 0
    optional_test_pass = 0
    for section in verifications:
        for test in verifications[section]:
            if test["required"]:
                required_test_pass += 1 if test["pass"] else 0
            elif not test["required"]:
                optional_test_pass += 1 if test["pass"] else 0
    results = {
        "conformant": True if required_test_pass == required_test_count else False,
        "required_score": f"{required_test_pass}/{required_test_count}",
        "optional_score": f"{optional_test_pass}/{optional_test_count}",
        "verifications": verifications,
    }

    return results