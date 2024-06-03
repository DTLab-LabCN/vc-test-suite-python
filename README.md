<h1>W3c Verifiable Credentials Schema Validator</h1>
<p>This repository contains scripts for validating schemas based on W3c Verifiable credential model 1.1 specification. The primary goal is to evaluate JSON schemas against the W3C standard and provide conformance reports.</p>
<h2>Table of contents:</h2>
<p>1.Authors
2.Background
3.Purpose
4.Files included
5.How to execute
6.Examples of input with expected output</p>
<h2>Authors</h2>
<p>Artin-Biniek</p>
<h2>Background</h2>
<p>The current commit adheres to the W3C verifiable credentials data model V1.1 specification. For more information refer to the official <a href="https://www.w3.org/TR/vc-data-model/">W3C specification</a></p>
<h2>Purpose</h2>
<p>This commit provides the following features:</p>
<ul>
<li>To execute the function test_data_model_v1 by passing in a JSON schema argument</li>
<li>To execute the W3c.py file from a  __main__.py file where it manages the command line arguments and executions.</li>
</ul>
<h2>Files included</h2>
<p>The following files included are:</p>
<ul>
<li>w3c.py for defining the functions that are used for validation of the schema with respect to W3C verifiable credentials data model V1.1 specification.</li>
<li>__main__.py file allow for the managing of command line arguments passed and serves as a means of executing w3c.py functions with those given command line arguments.</li>
<li>__init__.py an empty file that tells python the directory contains a package</li>
<li>setup.py a file that is responsible for the setup configuration </li>
<li>install.sh a file that installs the required dependencies for our api </li>
</ul>
<h2>How to execute</h2>
<p>The following steps are needed to execute:</p>
<ul>
<li>Navigate to the main directory</li>
<li>Run the command python3 __main__.py &#39;{&quot;someParam&quot;:&quot;somevalue&quot;}&#39;</li>
</ul>
<h2>Examples of input with expected output</h2>
<p><strong>Example1</strong></p>
<p><strong>Input</strong></p>
<p> python3 __main__.py &#39;{&quot;@context&quot;: [&quot;<a href="https://www.w3.org/ns/credentials/v2%22%5D,%22type">https://www.w3.org/ns/credentials/v2&quot;],&quot;type</a>&quot;: [&quot;VerifiableCredential&quot;, &quot;MyPrototypeCredential&quot;],&quot;credentialSubject&quot;: {&quot;mySubjectProperty&quot;: &quot;mySubjectValue&quot;}}&#39;</p>
<p><strong>Output</strong></p>
<p> {&#39;conformant&#39;: False, &#39;required_score&#39;: &#39;6/9&#39;, &#39;optional_score&#39;: &#39;1/2&#39;, &#39;verifications&#39;: {&#39;@context&#39;: [{&#39;statement&#39;: &#39;Verifiable credentials MUST include a @context property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: True}, {&#39;statement&#39;: &#39;The value of the @context property MUST be an ordered set.&#39;, &#39;required&#39;: True, &#39;pass&#39;: True}, {&#39;statement&#39;: &#39;The first item MUST be a URI with the value <a href="https://www.w3.org/2018/credentials/v1">https://www.w3.org/2018/credentials/v1</a>&#39;, &#39;required&#39;: True, &#39;pass&#39;: False}, {&#39;statement&#39;: &#39;Subsequent items MUST be composed of URLs and/or objects each processable as a JSON-LD Context.&#39;, &#39;required&#39;: True, &#39;pass&#39;: True}], &#39;type&#39;: [{&#39;statement&#39;: &#39;Verifiable credentials MUST have a type property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: True}, {&#39;statement&#39;: &#39;MUST have VerifiableCredential&#39;, &#39;required&#39;: True, &#39;pass&#39;: True}, {&#39;statement&#39;: &#39;MAY have a more specific verifiable credential type.&#39;, &#39;required&#39;: False, &#39;pass&#39;: True}], &#39;issuer&#39;: [{&#39;statement&#39;: &#39;A verifiable credential MUST have an issuer property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: False}], &#39;issuanceDate&#39;: [{&#39;statement&#39;: &#39;A credential MUST have an issuanceDate property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: False}], &#39;credentialSubject&#39;: [{&#39;statement&#39;: &#39;A verifiable credential MUST have a credentialSubject property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: True}, {&#39;statement&#39;: &#39;Each object MAY contain an id.&#39;, &#39;required&#39;: False, &#39;pass&#39;: False}]}}</p>
<p><strong>Example2</strong></p>
<p><strong>Input</strong></p>
<p>python3  __main__.py &#39;{&quot;someExample&quot;:&quot;2&quot;}&#39;</p>
<p><strong>Output</strong></p>
<p>None</p>
<p> {&#39;conformant&#39;: False, &#39;required_score&#39;: &#39;0/5&#39;, &#39;optional_score&#39;: &#39;0/0&#39;, &#39;verifications&#39;: {&#39;@context&#39;: [{&#39;statement&#39;: &#39;Verifiable credentials MUST include a @context property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: False}], &#39;type&#39;: [{&#39;statement&#39;: &#39;Verifiable credentials MUST have a type property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: False}], &#39;issuer&#39;: [{&#39;statement&#39;: &#39;A verifiable credential MUST have an issuer property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: False}], &#39;issuanceDate&#39;: [{&#39;statement&#39;: &#39;A credential MUST have an issuanceDate property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: False}], &#39;credentialSubject&#39;: [{&#39;statement&#39;: &#39;A verifiable credential MUST have a credentialSubject property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: False}]}}</p>
<p><strong>Example3</strong></p>
<p><strong>Input</strong></p>
<p>python3  __main__.py &#39;{&quot;@context&quot;: [&quot;<a href="https://www.w3.org/ns/credentials/v2%22,%22https://www.w3.org/ns/credentials/examples/v2%22%5D,%22id">https://www.w3.org/ns/credentials/v2&quot;,&quot;https://www.w3.org/ns/credentials/examples/v2&quot;],&quot;id</a>&quot;: &quot;<a href="http://university.example/credentials/3732%22,%22type">http://university.example/credentials/3732&quot;,&quot;type</a>&quot;: [&quot;VerifiableCredential&quot;, &quot;ExampleDegreeCredential&quot;],&quot;issuer&quot;: {&quot;id&quot;: &quot;<a href="https://university.example/issuers/565049%22,%22name">https://university.example/issuers/565049&quot;,&quot;name</a>&quot;: &quot;Example University&quot;,&quot;description&quot;: &quot;A public university focusing on teaching examples.&quot;},&quot;validFrom&quot;: &quot;2015-05-10T12:30:00Z&quot;,&quot;name&quot;: &quot;Example University Degree&quot;,&quot;description&quot;: &quot;2015 Bachelor of Science and Arts Degree&quot;,&quot;credentialSubject&quot;: {&quot;id&quot;: &quot;did:example:ebfeb1f712ebc6f1c276e12ec21&quot;,&quot;degree&quot;: {&quot;type&quot;: &quot;ExampleBachelorDegree&quot;,&quot;name&quot;: &quot;Bachelor of Science and Arts&quot;}}}&#39;</p>
<p><strong>Output</strong></p>
<p> {&#39;conformant&#39;: False, &#39;required_score&#39;: &#39;8/10&#39;, &#39;optional_score&#39;: &#39;4/4&#39;, &#39;verifications&#39;: {&#39;@context&#39;: [{&#39;statement&#39;: &#39;Verifiable credentials MUST include a @context property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: True}, {&#39;statement&#39;: &#39;The value of the @context property MUST be an ordered set.&#39;, &#39;required&#39;: True, &#39;pass&#39;: True}, {&#39;statement&#39;: &#39;The first item MUST be a URI with the value <a href="https://www.w3.org/2018/credentials/v1">https://www.w3.org/2018/credentials/v1</a>&#39;, &#39;required&#39;: True, &#39;pass&#39;: False}, {&#39;statement&#39;: &#39;Subsequent items MUST be composed of URLs and/or objects each processable as a JSON-LD Context.&#39;, &#39;required&#39;: True, &#39;pass&#39;: True}], &#39;id&#39;: [{&#39;statement&#39;: &#39;A verifiable credential MAY have an id property.&#39;, &#39;required&#39;: False, &#39;pass&#39;: True}, {&#39;statement&#39;: &#39;The value of the id property MUST be a single URI.&#39;, &#39;required&#39;: False, &#39;pass&#39;: True}], &#39;type&#39;: [{&#39;statement&#39;: &#39;Verifiable credentials MUST have a type property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: True}, {&#39;statement&#39;: &#39;MUST have VerifiableCredential&#39;, &#39;required&#39;: True, &#39;pass&#39;: True}, {&#39;statement&#39;: &#39;MAY have a more specific verifiable credential type.&#39;, &#39;required&#39;: False, &#39;pass&#39;: True}], &#39;issuer&#39;: [{&#39;statement&#39;: &#39;A verifiable credential MUST have an issuer property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: True}, {&#39;statement&#39;: &#39;The value of the issuer property MUST be either a URI or an object containing an id property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: True}], &#39;issuanceDate&#39;: [{&#39;statement&#39;: &#39;A credential MUST have an issuanceDate property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: False}], &#39;credentialSubject&#39;: [{&#39;statement&#39;: &#39;A verifiable credential MUST have a credentialSubject property.&#39;, &#39;required&#39;: True, &#39;pass&#39;: True}, {&#39;statement&#39;: &#39;Each object MAY contain an id.&#39;, &#39;required&#39;: False, &#39;pass&#39;: True}]}}</p>
