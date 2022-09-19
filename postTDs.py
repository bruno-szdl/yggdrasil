import requests

requests.post(
    'http://192.168.15.8:8080/environments/'
    , headers = {
        'Content-type': 'text/turtle'
        , 'slug': 'smartbuilding'
        }
    , data=
    '@prefix eve: <http://w3id.org/eve#> .\n\
    @prefix td: <https://www.w3.org/2019/wot/td#> .\n\
    @prefix htv: <http://www.w3.org/2011/http#> .\n\
    @prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .\n\
    @prefix wotsec: <https://www.w3.org/2019/wot/security#> .\n\
    @prefix dct: <http://purl.org/dc/terms/> .\n\
    @prefix js: <https://www.w3.org/2019/wot/json-schema#> .\n\
    @prefix saref: <https://w3id.org/saref#> .\n\
    \n\
    <>\n\
    a td:Thing, eve:EnvironmentArtifact;\n\
    td:title "smarbuilding";\n\
    td:hasSecurityConfiguration [ a wotsec:NoSecurityScheme\n\
    ];\n\
    td:hasActionAffordance [ a td:ActionAffordance, eve:MakeWorkspace;\n\
        td:name "makeWorkspace";\n\
        td:title "MakeWorkspace";\n\
    ];\n\
    eve:contains <http://192.168.15.8:8080/environments/smartbuilding/workspaces/meetingroom/>,\n\
    <http://192.168.15.8:8080/environments/smartbuilding/workspaces/meetingroom/> .'
)

requests.post(
    'http://192.168.15.8:8080/environments/smartbuilding/workspaces/'
    , headers = {
        'Content-type': 'text/turtle'
        , 'slug': 'meetingroom'
        }
    , data=
    '@prefix eve: <http://w3id.org/eve#> .\n\
    @prefix td: <https://www.w3.org/2019/wot/td#> .\n\
    @prefix htv: <http://www.w3.org/2011/http#> .\n\
    @prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .\n\
    @prefix wotsec: <https://www.w3.org/2019/wot/security#> .\n\
    @prefix dct: <http://purl.org/dc/terms/> .\n\
    @prefix js: <https://www.w3.org/2019/wot/json-schema#> .\n\
    @prefix saref: <https://w3id.org/saref#> .\n\
    \n\
    <>\n\
    a td:Thing, eve:WorkspaceArtifact;\n\
    td:title "meetingroom";\n\
    td:hasSecurityConfiguration [ a wotsec:NoSecurityScheme\n\
    ];\n\
    td:hasActionAffordance [ a td:ActionAffordance, eve:MakeArtifact;\n\
        td:name "makeArtifact";\n\
        td:hasForm [\n\
            htv:methodName "POST";\n\
            hctl:hasTarget <http://192.168.15.8:8080/environments/smartbuilding/workspaces/meetingroom/artifacts/>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:invokeAction\n\
        ];\n\
        td:hasInputSchema [ a js:ObjectSchema;\n\
          js:properties [ a eve:ArtifactClass, js:StringSchema;\n\
              js:propertyName "artifactClass"\n\
            ], [ a eve:ArtifactName, js:StringSchema;\n\
              js:propertyName "artifactName"\n\
            ], [ a js:ArraySchema;\n\
              js:propertyName "initParams"\n\
            ];\n\
          js:required "artifactClass", "artifactName"\n\
        ]\n\
    ];\n\
    eve:contains <http://192.168.15.8:8080/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb1/>,\n\
    <http://192.168.15.8:8080/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb2/>,\n\
    <http://192.168.15.8:8080/environments/smartbuilding/workspaces/meetingroom/artifacts/smarttv1/>,\n\
    <http://192.168.15.8:8080/environments/smartbuilding/workspaces/meetingroom/artifacts/windowblinder1/> .'
)

requests.post(
    'http://192.168.15.8:8080/environments/smartbuilding/workspaces/'
    , headers = {
        'Content-type': 'text/turtle'
        , 'slug': 'workingroom'
        }
    , data=
    '@prefix eve: <http://w3id.org/eve#> .\n\
    @prefix td: <https://www.w3.org/2019/wot/td#> .\n\
    @prefix htv: <http://www.w3.org/2011/http#> .\n\
    @prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .\n\
    @prefix wotsec: <https://www.w3.org/2019/wot/security#> .\n\
    @prefix dct: <http://purl.org/dc/terms/> .\n\
    @prefix js: <https://www.w3.org/2019/wot/json-schema#> .\n\
    @prefix saref: <https://w3id.org/saref#> .\n\
    \n\
    <>\n\
    a td:Thing, eve:WorkspaceArtifact;\n\
    td:title "workingroom";\n\
    td:hasSecurityConfiguration [ a wotsec:NoSecurityScheme\n\
    ];\n\
    td:hasActionAffordance [ a td:ActionAffordance, eve:MakeArtifact;\n\
        td:name "makeArtifact";\n\
        td:hasForm [\n\
            htv:methodName "POST";\n\
            hctl:hasTarget <http://192.168.15.8:8080/environments/smartbuilding/workspaces/meetingroom/artifacts/>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:invokeAction\n\
        ];\n\
        td:hasInputSchema [ a js:ObjectSchema;\n\
          js:properties [ a eve:ArtifactClass, js:StringSchema;\n\
              js:propertyName "artifactClass"\n\
            ], [ a eve:ArtifactName, js:StringSchema;\n\
              js:propertyName "artifactName"\n\
            ], [ a js:ArraySchema;\n\
              js:propertyName "initParams"\n\
            ];\n\
          js:required "artifactClass", "artifactName"\n\
        ]\n\
    ];\n\
    eve:contains <http://192.168.15.8:8080/environments/smartbuilding/workspaces/workingroom/artifacts/lightbulb3/>,\n\
    <http://192.168.15.8:8080/environments/smartbuilding/workspaces/workingroom/artifacts/lightbulb4/> .'
)

requests.post(
    'http://192.168.15.8:8080/environments/smartbuilding/workspaces/meetingroom/artifacts/'
    , headers = {
        'Content-type': 'text/turtle'
        , 'slug': 'lightbulb1'
        }
    , data=
    '@prefix td: <https://www.w3.org/2019/wot/td#> .\n\
    @prefix htv: <http://www.w3.org/2011/http#> .\n\
    @prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .\n\
    @prefix wotsec: <https://www.w3.org/2019/wot/security#> .\n\
    @prefix dct: <http://purl.org/dc/terms/> .\n\
    @prefix js: <https://www.w3.org/2019/wot/json-schema#> .\n\
    @prefix saref: <https://w3id.org/saref#> .\n\
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\
    \n\
    <>\n\
    a td:Thing, saref:LightSwitch;\n\
    td:title "lightbulb1";\n\
    td:hasSecurityConfiguration [ a wotsec:NoSecurityScheme\n\
    ];\n\
    td:hasBase <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb1/>;\n\
    td:hasPropertyAffordance [ a td:PropertyAffordance, saref:OnOffState, js:BooleanSchema;\n\
        td:name "state";\n\
        td:hasForm [\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb1/state>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:readProperty, td:writeProperty\n\
        ];\n\
        td:isObservable false\n\
    ], [ a td:PropertyAffordance, js:StringSchema;\n\
        td:name "Color";\n\
        td:hasForm [\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb1/color>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:readProperty, td:writeProperty\n\
        ];\n\
        td:isObservable false\n\
    ];\n\
    td:hasActionAffordance [ a td:ActionAffordance, saref:ToggleCommand;\n\
        td:name "toggle";\n\
        td:hasForm [\n\
            htv:methodName "PUT";\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb1/toggle>;\n\
            hctl:hasOperationType td:invokeAction\n\
        ];\n\
        td:hasInputSchema [ a js:ObjectSchema, saref:OnOffState;\n\
            js:properties [ a js:BooleanSchema;\n\
                js:propertyName "state"\n\
            ];\n\
            js:required "state"\n\
        ]\n\
    ], [ a td:ActionAffordance;\n\
        td:name "changeColor";\n\
        td:hasForm [\n\
            htv:methodName "PUT";\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb1/color>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:invokeAction\n\
        ];\n\
        td:hasInputSchema [ a js:ObjectSchema;\n\
            js:properties [ a js:StringSchema;\n\
                js:propertyName "color"\n\
            ];\n\
            js:required "color"\n\
        ]\n\
    ] .'
)

requests.post(
    'http://192.168.15.8:8080/environments/smartbuilding/workspaces/meetingroom/artifacts/'
    , headers = {
        'Content-type': 'text/turtle'
        , 'slug': 'lightbulb2'
        }
    , data=
    '@prefix td: <https://www.w3.org/2019/wot/td#> .\n\
    @prefix htv: <http://www.w3.org/2011/http#> .\n\
    @prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .\n\
    @prefix wotsec: <https://www.w3.org/2019/wot/security#> .\n\
    @prefix dct: <http://purl.org/dc/terms/> .\n\
    @prefix js: <https://www.w3.org/2019/wot/json-schema#> .\n\
    @prefix saref: <https://w3id.org/saref#> .\n\
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\
    \n\
    <>\n\
    a td:Thing, saref:LightSwitch;\n\
    td:title "lightbulb2";\n\
    td:hasSecurityConfiguration [ a wotsec:NoSecurityScheme\n\
    ];\n\
    td:hasBase <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb2/>;\n\
    td:hasPropertyAffordance [ a td:PropertyAffordance, saref:OnOffState, js:BooleanSchema;\n\
        td:name "state";\n\
        td:hasForm [\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb2/state>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:readProperty, td:writeProperty\n\
        ];\n\
        td:isObservable false\n\
    ], [ a td:PropertyAffordance, js:StringSchema;\n\
        td:name "Color";\n\
        td:hasForm [\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb2/color>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:readProperty, td:writeProperty\n\
        ];\n\
        td:isObservable false\n\
    ];\n\
    td:hasActionAffordance [ a td:ActionAffordance, saref:ToggleCommand;\n\
        td:name "toggle";\n\
        td:hasForm [\n\
            htv:methodName "PUT";\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb2/toggle>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:invokeAction\n\
        ];\n\
        td:hasInputSchema [ a js:ObjectSchema, saref:OnOffState;\n\
            js:properties [ a js:BooleanSchema;\n\
                js:propertyName "state"\n\
            ];\n\
            js:required "state"\n\
        ]\n\
    ], [ a td:ActionAffordance;\n\
        td:name "changeColor";\n\
        td:hasForm [\n\
            htv:methodName "PUT";\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb2/color>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:invokeAction\n\
        ];\n\
        td:hasInputSchema [ a js:ObjectSchema;\n\
            js:properties [ a js:StringSchema;\n\
                js:propertyName "color"\n\
            ];\n\
            js:required "color"\n\
        ]\n\
    ] .'
)

requests.post(
    'http://192.168.15.8:8080/environments/smartbuilding/workspaces/workingroom/artifacts/'
    , headers = {
        'Content-type': 'text/turtle'
        , 'slug': 'lightbulb3'
        }
    , data=
    '@prefix td: <https://www.w3.org/2019/wot/td#> .\n\
    @prefix htv: <http://www.w3.org/2011/http#> .\n\
    @prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .\n\
    @prefix wotsec: <https://www.w3.org/2019/wot/security#> .\n\
    @prefix dct: <http://purl.org/dc/terms/> .\n\
    @prefix js: <https://www.w3.org/2019/wot/json-schema#> .\n\
    @prefix saref: <https://w3id.org/saref#> .\n\
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\
    @prefix companya : <https://raw.githubusercontent.com/bruno-szdl/example_ont_companies/main/companyA.owl#> .\n\
    \n\
    <>\n\
    a td:Thing, saref:LightSwitch;\n\
    td:title "lightbulb3";\n\
    td:hasSecurityConfiguration [ a wotsec:NoSecurityScheme\n\
    ];\n\
    td:hasBase <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb3/>;\n\
    td:hasPropertyAffordance [ a td:PropertyAffordance, saref:OnOffState, js:BooleanSchema;\n\
        td:name "state";\n\
        td:hasForm [\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/workingroom/artifacts/lightbulb3/state>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:readProperty, td:writeProperty\n\
        ];\n\
        td:isObservable false\n\
    ];\n\
    td:hasActionAffordance [ a td:ActionAffordance, companya:toggleLight;\n\
        td:name "toggle";\n\
        td:hasForm [\n\
            htv:methodName "PUT";\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/workingroom/artifacts/lightbulb3/toggle>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:invokeAction\n\
        ];\n\
        td:hasInputSchema [ a js:ObjectSchema, saref:OnOffState;\n\
            js:properties [ a js:BooleanSchema;\n\
                js:propertyName "state"\n\
            ];\n\
            js:required "state"\n\
        ]\n\
    ] .'
)

requests.post(
    'http://192.168.15.8:8080/environments/smartbuilding/workspaces/workingroom/artifacts/'
    , headers = {
        'Content-type': 'text/turtle'
        , 'slug': 'lightbulb4'
        }
    , data=
    '@prefix td: <https://www.w3.org/2019/wot/td#> .\n\
    @prefix htv: <http://www.w3.org/2011/http#> .\n\
    @prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .\n\
    @prefix wotsec: <https://www.w3.org/2019/wot/security#> .\n\
    @prefix dct: <http://purl.org/dc/terms/> .\n\
    @prefix js: <https://www.w3.org/2019/wot/json-schema#> .\n\
    @prefix saref: <https://w3id.org/saref#> .\n\
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\
    @prefix companyb : <https://raw.githubusercontent.com/bruno-szdl/example_ont_companies/main/companyB.owl#> .\n\
    \n\
    <>\n\
    a td:Thing, saref:LightSwitch;\n\
    td:title "lightbulb4";\n\
    td:hasSecurityConfiguration [ a wotsec:NoSecurityScheme\n\
    ];\n\
    td:hasBase <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb4/>;\n\
    td:hasPropertyAffordance [ a td:PropertyAffordance, saref:OnOffState, js:BooleanSchema;\n\
        td:name "state";\n\
        td:hasForm [\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/workingroom/artifacts/lightbulb4/state>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:readProperty, td:writeProperty\n\
        ];\n\
        td:isObservable false\n\
    ];\n\
    td:hasActionAffordance [ a td:ActionAffordance, companyb:lightToggle;\n\
        td:name "toggle";\n\
        td:hasForm [\n\
            htv:methodName "PUT";\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/workingroom/artifacts/lightbulb4/toggle>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:invokeAction\n\
        ];\n\
        td:hasInputSchema [ a js:ObjectSchema, saref:OnOffState;\n\
            js:properties [ a js:BooleanSchema;\n\
                js:propertyName "state"\n\
            ];\n\
            js:required "state"\n\
        ]\n\
    ] .'
)

requests.post(
    'http://192.168.15.8:8080/environments/smartbuilding/workspaces/meetingroom/artifacts/'
    , headers = {
        'Content-type': 'text/turtle'
        , 'slug': 'smarttv1'
        }
    , data=
    '@prefix td: <https://www.w3.org/2019/wot/td#> .\n\
    @prefix htv: <http://www.w3.org/2011/http#> .\n\
    @prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .\n\
    @prefix wotsec: <https://www.w3.org/2019/wot/security#> .\n\
    @prefix dct: <http://purl.org/dc/terms/> .\n\
    @prefix js: <https://www.w3.org/2019/wot/json-schema#> .\n\
    @prefix saref: <https://w3id.org/saref#> .\n\
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\
    \n\
    <>\n\
    a td:Thing;\n\
    td:title "smarttv";\n\
    td:hasSecurityConfiguration [ a wotsec:NoSecurityScheme\n\
    ];\n\
    td:hasBase <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/smarttv1/>;\n\
    td:hasPropertyAffordance [ a td:PropertyAffordance, saref:OnOffState, js:BooleanSchema;\n\
        td:name "state";\n\
        td:hasForm [\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/smarttv1/state>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:readProperty, td:writeProperty\n\
        ];\n\
        td:isObservable false\n\
    ], [ a td:PropertyAffordance, js:IntegerSchema;\n\
        td:name "Channel";\n\
        td:hasForm [\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/smarttv1/channel>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:readProperty, td:writeProperty\n\
        ];\n\
        td:isObservable false\n\
    ];\n\
    td:hasActionAffordance [ a td:ActionAffordance, saref:ToggleCommand;\n\
        td:name "toggle";\n\
        td:hasForm [\n\
            htv:methodName "PUT";\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/smarttv1/toggle>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:invokeAction\n\
        ];\n\
        td:hasInputSchema [ a js:ObjectSchema, saref:OnOffState;\n\
            js:properties [ a js:BooleanSchema;\n\
                js:propertyName "state"\n\
            ];\n\
            js:required "state"\n\
        ]\n\
    ], [ a td:ActionAffordance;\n\
        td:name "changeChannel";\n\
        td:hasForm [\n\
            htv:methodName "PUT";\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/smarttv1/channel>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:invokeAction\n\
        ];\n\
        td:hasInputSchema [ a js:ObjectSchema;\n\
            js:properties [ a js:IntegerSchema;\n\
                js:propertyName "channel"\n\
            ];\n\
            js:required "channel"\n\
        ]\n\
    ] .'
)

requests.post(
    'http://192.168.15.8:8080/environments/smartbuilding/workspaces/meetingroom/artifacts/'
    , headers = {
        'Content-type': 'text/turtle'
        , 'slug': 'windowblinder1'
        }
    , data=
    '@prefix td: <https://www.w3.org/2019/wot/td#> .\n\
    @prefix htv: <http://www.w3.org/2011/http#> .\n\
    @prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .\n\
    @prefix wotsec: <https://www.w3.org/2019/wot/security#> .\n\
    @prefix dct: <http://purl.org/dc/terms/> .\n\
    @prefix js: <https://www.w3.org/2019/wot/json-schema#> .\n\
    @prefix saref: <https://w3id.org/saref#> .\n\
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\
    \n\
    <>\n\
    a td:Thing;\n\
    td:title "windowblinder";\n\
    td:hasSecurityConfiguration [ a wotsec:NoSecurityScheme\n\
    ];\n\
    td:hasBase <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/windowblinder1/>;\n\
    td:hasPropertyAffordance [ a td:PropertyAffordance, js:StringSchema;\n\
        td:name "state";\n\
        td:hasForm [\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/windowblinder1/state>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:readProperty, td:writeProperty\n\
        ];\n\
        td:isObservable false\n\
    ];\n\
    td:hasActionAffordance [ a td:ActionAffordance;\n\
        td:name "changeState";\n\
        td:hasForm [\n\
            htv:methodName "PUT";\n\
            hctl:hasTarget <http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/windowblinder1/state>;\n\
            hctl:forContentType "application/json";\n\
            hctl:hasOperationType td:invokeAction\n\
        ];\n\
        td:hasInputSchema [ a js:ObjectSchema;\n\
            js:properties [ a js:StringSchema;\n\
                js:propertyName "state"\n\
            ];\n\
            js:required "state"\n\
        ]\n\
    ] .'
)
