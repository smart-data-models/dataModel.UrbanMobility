<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: ArrivalEstimation    
=========================<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/ArrivalEstimation/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **Arrival Estimation**    
version: 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## List of properties    
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `alternateName[string]`: An alternative name for this item  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `hasStop[array]`: It shall point to an Entity of Type GtfsStop  - `hasTrip[*]`: Trip associated to this Entity. It shall point to an Entity of Type GtfsTrip  . Model: [https://schema.org/URL](https://schema.org/URL)- `headSign[string]`: It shall contain the text that appears on a sign that identifies the trip's destination to passengers  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Unique identifier of the entity  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `remainingDistance[number]`: It shall contain the remaining distance (in meters) of arrival for the trip heading to the concerned stop  . Model: [https://schema.org/Number](https://schema.org/Number)- `remainingTime[string]`: It shall contain the remaining time of arrival for the trip heading to the concerned stop. Remaining time shall be encoded as a ISO8601 duration. Ex. `PT8M5S`  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `type[string]`: NGSI Entity Type: It has to be ArrivalEstimation. Enum:'ArrivalEstimation'  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Required properties    
- `hasStop`  - `hasTrip`  - `headSign`  - `id`  - `remainingTime`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
This Entity Type captures the estimated arrival time of a public transport vehicle reaching a particular stop, whilst the vehicle is servicing a particular route.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Data Model description of properties    
Sorted alphabetically (click for details)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
ArrivalEstimation:      
  description: Arrival Estimation      
  properties:      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    hasStop:      
      description: It shall point to an Entity of Type GtfsStop      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
      type: array      
      x-ngsi:      
        type: Relationship      
    hasTrip:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Trip associated to this Entity. It shall point to an Entity of Type GtfsTrip      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
    headSign:      
      description: It shall contain the text that appears on a sign that identifies the trip's destination to passengers      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    remainingDistance:      
      description: It shall contain the remaining distance (in meters) of arrival for the trip heading to the concerned stop      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Meters      
    remainingTime:      
      description: It shall contain the remaining time of arrival for the trip heading to the concerned stop. Remaining time shall be encoded as a ISO8601 duration. Ex. `PT8M5S`      
      pattern: ^P(?=\w*\d)(?:\d+Y|Y)?(?:\d+M|M)?(?:\d+W|W)?(?:\d+D|D)?(?:T(?:\d+H|H)?(?:\d+M|M)?(?:\d+(?:\?.\d{1,2})?S|S)?)?$      
      type: string      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
      oneOf:      
        - items:      
            format: uri      
            type: string      
          minItems: 1      
          type: array      
        - format: uri      
          type: string      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: 'NGSI Entity Type: It has to be ArrivalEstimation. Enum:''ArrivalEstimation'''      
      enum:      
        - ArrivalEstimation      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - hasStop      
    - hasTrip      
    - remainingTime      
    - headSign      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/ArrivalEstimation/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/ArrivalEstimation/schema.json      
  x-model-tags: ""      
  x-version: 0.0.3      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Example payloads      
#### ArrivalEstimation NGSI-v2 key-values Example      
Here is an example of a ArrivalEstimation in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
  "type": "ArrivalEstimation",  
  "hasStop": [  
    "urn:ngsi-ld:GtfsStop:tus:74"  
  ],  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:tus:5C1",  
  "remainingTime": "PT8M5S",  
  "remainingDistance": 1200,  
  "headSign": "Plaza Italia"  
}  
```  
</details>    
#### ArrivalEstimation NGSI-v2 normalized Example      
Here is an example of a ArrivalEstimation in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
  "type": "ArrivalEstimation",  
  "hasTrip": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:GtfsTrip:tus:5C1"  
  },  
  "headSign": {  
    "type": "Text",  
    "value": "Plaza Italia"  
  },  
  "remainingTime": {  
    "type": "Text",  
    "value": "PT8M5S"  
  },  
  "hasStop": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:GtfsStop:tus:74"  
    ]  
  },  
  "remainingDistance": {  
    "type": "Number",  
    "value": 1200  
  }  
}  
```  
</details>    
#### ArrivalEstimation NGSI-LD key-values Example      
Here is an example of a ArrivalEstimation in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
  "type": "ArrivalEstimation",  
  "hasStop": [  
    "urn:ngsi-ld:GtfsStop:tus:74"  
  ],  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:tus:5C1",  
  "headSign": "Plaza Italia",  
  "remainingDistance": 1200,  
  "remainingTime": "PT8M5S",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### ArrivalEstimation NGSI-LD normalized Example      
Here is an example of a ArrivalEstimation in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
    "type": "ArrivalEstimation",  
    "hasStop": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsStop:tus:74"  
    },  
    "hasTrip": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsTrip:tus:5C1"  
    },  
    "headSign": {  
        "type": "Property",  
        "value": "Plaza Italia"  
    },  
    "remainingDistance": {  
        "type": "Property",  
        "value": 1200  
    },  
    "remainingTime": {  
        "type": "Property",  
        "value": "PT8M5S"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
