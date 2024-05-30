Artin-Biniek

Background:
The code makes use w3c V1.1 specification https://www.w3.org/TR/vc-data-model/ . In this case its for the purpose of validating schemas based on said specification and producing schemas based on the provided speciciation examples are also included within the link.

Purpose:
The aim of this commit is to execute the python file w3c.py using a main.py file and pass in an existing json schema for it to be evaluated by the test_Data_model_v1(vc)

Files included:
W3c.py the file that contains the function for validating the test data model
message.py the file that w3c.py depends on for execution
main.py for the purpose of executing the w3c.py file.
How to execute:
Command:
1)Go within main directory
2)Run the command 
python3 main.py '{"someParam":"somevalue"}'



Example1:
Input:
 python3 main.py '{"@context": ["https://www.w3.org/ns/credentials/v2"],"type": ["VerifiableCredential", "MyPrototypeCredential"],"credentialSubject": {"mySubjectProperty": "mySubjectValue"}}'

Output:
 {'conformant': False, 'required_score': '6/9', 'optional_score': '1/2', 'verifications': {'@context': [{'statement': 'Verifiable credentials MUST include a @context property.', 'required': True, 'pass': True}, {'statement': 'The value of the @context property MUST be an ordered set.', 'required': True, 'pass': True}, {'statement': 'The first item MUST be a URI with the value https://www.w3.org/2018/credentials/v1', 'required': True, 'pass': False}, {'statement': 'Subsequent items MUST be composed of URLs and/or objects each processable as a JSON-LD Context.', 'required': True, 'pass': True}], 'type': [{'statement': 'Verifiable credentials MUST have a type property.', 'required': True, 'pass': True}, {'statement': 'MUST have VerifiableCredential', 'required': True, 'pass': True}, {'statement': 'MAY have a more specific verifiable credential type.', 'required': False, 'pass': True}], 'issuer': [{'statement': 'A verifiable credential MUST have an issuer property.', 'required': True, 'pass': False}], 'issuanceDate': [{'statement': 'A credential MUST have an issuanceDate property.', 'required': True, 'pass': False}], 'credentialSubject': [{'statement': 'A verifiable credential MUST have a credentialSubject property.', 'required': True, 'pass': True}, {'statement': 'Each object MAY contain an id.', 'required': False, 'pass': False}]}}







