# Copyright 2022 Instituto de Telecomunicações - Aveiro
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.


########################################################################
# This file serves the purpose to validate POST/PUT/PATCH HTTP METHODS #
# from a mec app. These schemas are json schemas that represent valid  #
# inputs that a mec app can execute                                    #
########################################################################
linktype_schema = {
    "type": "object",
    "properties": {
        "href": {"type": "string"},
    },
    "required": ["href"],
}

subscription_schema = {
    "type": "object",
    "properties": {"href": {"type": "string"}, "subscriptionType": {"type": "string"}},
    "required": ["href", "subscriptionType"],
}

links_schema = {
    "type": "object",
    "properties": {
        "self": linktype_schema,
        "subscriptions": {"type": "array", "items": subscription_schema},
        "liveness": linktype_schema,
    },
    "required": ["self"],
}

mecservicemgmtapisubscriptionlinklist_schema = {
    "type": "object",
    "properties": {"_links": links_schema},
    "required": ["_links"],
}

categoryref_schema = {
    "type": "object",
    "properties": {
        "href": {"type": "string"},
        "id": {"type": "string"},
        "name": {"type": "string"},
        "version": {"type": "string"},
    },
    "required": ["href", "id", "name", "version"],
}

filteringcriteria_schema = {
    "type": "object",
    "properties": {
        "state": {"enum": ["ACTIVE", "INACTIVE"]},
        "isLocal": {"type": "boolean"},
        "serInstanceId": {"type": "string"},
        "serName": {"type": "string"},
        "serCategory": categoryref_schema,
    },
    "oneOf":["serInstanceId","serName","serCategory"]
}

seravailabilitynotificationsubscription_schema = {
    "type": "object",
    "properties": {
        "callbackReference": {"type": "string"},
        "_links": links_schema,
        "filteringCriteria": filteringcriteria_schema,
        "subscriptionType": {"type": "string"},
    },
    "required": ["callbackReference", "subscriptionType"],
}
oauth2info_schema = {
    "type": "object",
    "properties": {
        "grantTypes": {
            "type": "array",
            "items": {
                "enum": [
                    "OAUTH2_AUTHORIZATION_CODE",
                    "OAUTH2_IMPLICIT_GRANT",
                    "OAUTH2_RESOURCE_OWNER",
                    "OAUTH2_CLIENT_CREDENTIALS",
                ]
            },
            "uniqueItems": True,
            "minItems": 1,
            "maxItems": 4,
        },
        "tokenEndpoint": {"type": "string"},
    },
    "required": ["grantTypes"],
}

securityinfo_schema = {
    "type": "object",
    "properties": {"oAuth2Info": oauth2info_schema},
    "required": ["oAuth2Info"],
}

endpointinfo_address_schema = {
    "type": "object",
    "properties": {"host": {"type": "string"}, "port": {"type": "integer"}},
    "required": ["host", "port"],
}
endpointinfo_addresses_schema = {
    "type": "object",
    "properties": {
        "addresses": {
            "type": "array",
            "items": endpointinfo_address_schema,
            "minItems": 1,
        }
    },
    "required": ["addresses"],
}

endpointinfo_uris_schema = {
    "type": "object",
    "properties": {
        "uris": {"type": "array", "items": {"type": "string"}, "minItems": 1}
    },
    "required": ["uris"],
}

implSpecificInfo_schema = {
    "type": "object",
    "properties": {"description": {"type": "string"}},
}

transportinfo_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "type:": {
            "enum": [
                "REST_HTTP",
                "MB_TOPIC_BASED",
                "MB_ROUTING",
                "MB_PUBSUB",
                "RPC",
                "RPC_STREAMING",
                "WEBSOCKET",
            ]
        },
        "version": {"type": "string"},
        "endpoint": {
            "oneOf": [endpointinfo_addresses_schema, endpointinfo_uris_schema]
        },
        "security": securityinfo_schema,
        "description": {"type": "string"},
        "implSpecificInfo": implSpecificInfo_schema,
        "protocol": {"type": "string"},
    },
    "required": ["id", "name", "type", "protocol", "version", "endpoint", "security"],
}

serviceinfo_schema = {
    "type": "object",
    "properties": {
        "version": {"type": "string"},
        "transportInfo": transportinfo_schema,
        "serializer": {"enum": ["JSON", "XML", "PROTOBUF3"]},
        "_links": links_schema,
        "livenessInterval": {"type": "integer"},
        "consumedLocalOnly": {"type": "boolean"},
        "isLocal": {"type": "boolean"},
        "scopeOfLocality": {
            "enum": [
                "MEC_SYSTEM",
                "MEC_HOST",
                "NFVI_POP",
                "ZONE",
                "ZONE_GROUP",
                "NFVI_NODE",
            ]
        },
        "serName": {"type": "string"},
        "serCategory": categoryref_schema,
    },
    "required": ["version", "state", "serializer", "_links","serName"],
}

appreadyconfirmation_schema = {
    "type": "object",
    "properties": {"indication": {"type": "string"}},
    "required": ["indication"],
}

appterminationconfirmation_schema = {
    "type": "object",
    "properties": {"operationAction": {"type": "string"}},
    "required": ["operationAction"],
}
