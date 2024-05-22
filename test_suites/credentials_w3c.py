from pyld import jsonld
from pprint import pprint
import json
import requests
from config import settings
from . import messaging
from app.controllers.uniresolver import UniresolverController


def compact(vc):
    try:
        return jsonld.compact(vc, {})
    except:
        return None


def get_version(vc):
    try:
        return (
            vc["@context"][0].split("/")[1]
            if vc["@context"][0]
            in [
                "https://www.w3.org/2018/credentials/v1",
                "https://www.w3.org/ns/credentials/v2",
            ]
            else None
        )
    except:
        return None


def test_data_model(vc):
    return test_data_model_v1(vc) if get_version(vc) == "v1" else test_data_model_v2(vc)


def test_data_model_v1(vc):
    verifications = {}
    required_test_count = 0
    optional_test_count = 0

    # CONTEXT
    verifications["@context"] = []
    verifications["@context"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["@context"][0],
            "required": True,
            "pass": True if "@context" in vc else False,
        }
    )
    required_test_count += 1
    verifications["@context"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["@context"][1],
            "required": True,
            "pass": (
                True
                if (
                    "@context" in vc
                    and isinstance(vc["@context"], list)
                    and len(vc["@context"]) > 0
                )
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
                    "@context" in vc
                    and isinstance(vc["@context"], list)
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
                if "@context" in vc
                and all(isinstance(item, (dict, str)) for item in vc["@context"])
                else False
            ),
        }
    )
    required_test_count += 1

    verifications["type"] = []
    verifications["type"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["type"][0],
            "required": True,
            "pass": True if "type" in vc else False,
        }
    )
    required_test_count += 1

    verifications["issuer"] = []
    verifications["issuer"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["issuer"][0],
            "required": True,
            "pass": True if "issuer" in vc else False,
        }
    )
    required_test_count += 1

    verifications["issuanceDate"] = []
    verifications["issuanceDate"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["issuanceDate"][0],
            "required": True,
            "pass": True if "issuanceDate" in vc else False,
        }
    )
    required_test_count += 1

    verifications["credentialSubject"] = []
    verifications["credentialSubject"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["credentialSubject"][0],
            "required": True,
            "pass": True if "credentialSubject" in vc else False,
        }
    )
    required_test_count += 1

    required_test_pass = 0
    optional_test_pass = 0
    for section in verifications:
        for test in verifications[section]:
            if test["required"]:
                required_test_pass += 1 if test["pass"] else 0

    if required_test_pass != required_test_count:
        results = {
            "verifications": verifications,
            "required_score": f"{required_test_pass}/{required_test_count}",
            "optional_score": f"{optional_test_pass}/{optional_test_count}",
            "conformant": True if required_test_pass == required_test_count else False,
        }
        return results

    # Type
    verifications["type"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["type"][2],
            "required": True,
            "pass": (
                True
                if (
                    isinstance(vc["type"], list)
                    and len(vc["type"]) > 0
                    and vc["type"][0] == "VerifiableCredential"
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

    # Id
    verifications["id"] = []
    verifications["id"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["id"][0],
            "required": False,
            "pass": (True if "id" in vc else False),
        }
    )
    optional_test_count += 1
    verifications["id"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["id"][1],
            "required": False,
            "pass": (
                True if "id" in vc and isinstance(vc["id"], str) and vc["id"] else False
            ),
        }
    )
    optional_test_count += 1

    # Issuer
    verifications["issuer"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["issuer"][1],
            "required": True,
            "pass": (
                True
                if (isinstance(vc["issuer"], str) and vc["issuer"])
                or (
                    isinstance(vc["issuer"], dict)
                    and "id" in vc["issuer"]
                    and vc["issuer"]["id"]
                )
                else False
            ),
        }
    )
    required_test_count += 1

    # Issuance Date
    verifications["issuanceDate"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["issuanceDate"][1],
            "required": True,
            "pass": (True if vc["issuanceDate"] else False),
        }
    )
    required_test_count += 1

    # Expiration Date
    verifications["expirationDate"] = []
    verifications["expirationDate"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["expirationDate"][0],
            "required": False,
            "pass": (
                True if "expirationDate" in vc and vc["expirationDate"] else False
            ),
        }
    )
    optional_test_count += 1

    # Credential Subject
    verifications["credentialSubject"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["credentialSubject"][1],
            "required": False,
            "pass": (
                True
                if isinstance(vc["credentialSubject"], dict)
                and "id" in vc["credentialSubject"]
                else False
            ),
        }
    )
    optional_test_count += 1

    # Credential Status
    verifications["credentialStatus"] = []
    verifications["credentialStatus"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["credentialStatus"][0],
            "required": False,
            "pass": (
                True
                if "credentialStatus" in vc
                and isinstance(vc["credentialStatus"], (dict, list))
                else False
            ),
        }
    )
    optional_test_count += 1
    if "credentialStatus" in vc and isinstance(vc["credentialStatus"], dict):
        vc["credentialStatus"] = [vc["credentialStatus"]]
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
    verifications["credentialSchema"] = []
    verifications["credentialSchema"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["credentialSchema"][0],
            "required": False,
            "pass": (
                True
                if "credentialSchema" in vc
                and isinstance(vc["credentialSchema"], (dict, list))
                else False
            ),
        }
    )
    optional_test_count += 1
    if "credentialSchema" in vc and isinstance(vc["credentialSchema"], dict):
        vc["credentialSchema"] = [vc["credentialSchema"]]

        verifications["credentialSchema"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["credentialSchema"][1],
                "required": False,
                "pass": (
                    True
                    if ("id" in evidence for evidence in vc["credentialSchema"])
                    else False
                ),
            }
        )
        optional_test_count += 1
        verifications["credentialSchema"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["credentialSchema"][2],
                "required": False,
                "pass": (
                    True
                    if ("type" in evidence for evidence in vc["credentialSchema"])
                    else False
                ),
            }
        )
        optional_test_count += 1

    # Refresh
    verifications["refreshService"] = []
    verifications["refreshService"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["refreshService"][0],
            "required": False,
            "pass": (
                True
                if "refreshService" in vc
                and isinstance(vc["refreshService"], (dict, list))
                else False
            ),
        }
    )
    optional_test_count += 1
    if "refreshService" in vc and isinstance(vc["refreshService"], dict):
        vc["refreshService"] = [vc["refreshService"]]

        verifications["refreshService"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["refreshService"][1],
                "required": False,
                "pass": (
                    True
                    if "refreshService" in vc
                    and isinstance(vc["refreshService"], list)
                    and ("id" in evidence for evidence in vc["refreshService"])
                    else False
                ),
            }
        )
        optional_test_count += 1
        verifications["refreshService"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["refreshService"][2],
                "required": False,
                "pass": (
                    True
                    if "refreshService" in vc
                    and isinstance(vc["refreshService"], list)
                    and ("type" in evidence for evidence in vc["refreshService"])
                    else False
                ),
            }
        )
        optional_test_count += 1

    # Refresh
    verifications["termsOfUse"] = []
    verifications["termsOfUse"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["termsOfUse"][0],
            "required": False,
            "pass": (
                True
                if "termsOfUse" in vc and isinstance(vc["termsOfUse"], (dict, list))
                else False
            ),
        }
    )
    optional_test_count += 1
    if "termsOfUse" in vc and isinstance(vc["termsOfUse"], dict):
        vc["termsOfUse"] = [vc["termsOfUse"]]

        verifications["termsOfUse"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["termsOfUse"][1],
                "required": False,
                "pass": (
                    True
                    if "termsOfUse" in vc
                    and isinstance(vc["termsOfUse"], list)
                    and ("id" in evidence for evidence in vc["termsOfUse"])
                    else False
                ),
            }
        )
        optional_test_count += 1
        verifications["termsOfUse"].append(
            {
                "statement": messaging.VCDM_V1_STATEMENTS["termsOfUse"][2],
                "required": False,
                "pass": (
                    True
                    if "termsOfUse" in vc
                    and isinstance(vc["termsOfUse"], list)
                    and ("type" in evidence for evidence in vc["termsOfUse"])
                    else False
                ),
            }
        )
        optional_test_count += 1

    # Evidence
    verifications["evidence"] = []
    verifications["evidence"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["evidence"][0],
            "required": False,
            "pass": (
                True
                if "evidence" in vc and isinstance(vc["evidence"], (dict, list))
                else False
            ),
        }
    )
    optional_test_count += 1
    if "evidence" in vc and isinstance(vc["evidence"], dict):
        vc["evidence"] = [vc["evidence"]]

    verifications["evidence"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["evidence"][1],
            "required": False,
            "pass": (
                True
                if "evidence" in vc
                and isinstance(vc["evidence"], list)
                and ("id" in evidence for evidence in vc["evidence"])
                else False
            ),
        }
    )
    optional_test_count += 1
    verifications["evidence"].append(
        {
            "statement": messaging.VCDM_V1_STATEMENTS["evidence"][2],
            "required": False,
            "pass": (
                True
                if "evidence" in vc
                and isinstance(vc["evidence"], list)
                and ("type" in evidence for evidence in vc["evidence"])
                else False
            ),
        }
    )
    optional_test_count += 1

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


def test_data_model_v2(vc):
    pass


def test_verification(vc):
    verifiers = []
    body = {"verifiableCredential": vc, "options": {}}
    for verifier in settings.VC_API_VERIFIERS:
        response = {"verifier": verifier["name"]}

        r = requests.post(verifier["endpoint"], json=body)
        response["code"] = r.status_code

        try:
            response["content"] = r.json()
        except:
            response["content"] = r.text

        verifiers.append(response)
    return verifiers


def resolve_dids(vc):
    did_documents = {}

    issuer_did = vc["issuer"] if isinstance(vc["issuer"], str) else vc["issuer"]["id"]
    did_documents["issuer"] = UniresolverController().resolver_did(issuer_did)

    if "id" in vc["credentialSuject"]:
        did_documents["subject"] = UniresolverController().resolver_did(
            vc["credentialSuject"]["id"]
        )

    return did_documents
