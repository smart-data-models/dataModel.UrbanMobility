<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: GtfsFrequency    
=====================<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsFrequency/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **GTFS Frequency**    
version: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## List of properties    
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `alternateName[string]`: An alternative name for this item  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `endTime[string]`: Same as GTFS `end_time`  . Model: [https://schema.org/Text](https://schema.org/Text)- `exactTimes[boolean]`: Same as GTFS `exact_times` but encoded as a Boolean; `false`: Frequency-based trips are not exactly scheduled. `true`: Frequency-based trips are exactly scheduled  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `hasTrip[*]`: Trip associated to this Entity. It shall point to an Entity of Type GtfsTrip  . Model: [https://schema.org/URL](https://schema.org/URL)- `headwaySeconds[number]`: Same as GTFS `headway_secs`  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Unique identifier of the entity  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `startTime[string]`: Same as GTFS `start_time`  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI Entity type. It has to be GtfsFrequency  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Required properties    
- `endTime`  - `hasTrip`  - `headwaySeconds`  - `id`  - `startTime`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
See [https://developers.google.com/transit/gtfs/reference/#frequenciestxt](https://developers.google.com/transit/gtfs/reference/#frequenciestxt)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Data Model description of properties    
Sorted alphabetically (click for details)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
GtfsFrequency:      
  description: GTFS Frequency      
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
    endTime:      
      description: Same as GTFS `end_time`      
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    exactTimes:      
      description: 'Same as GTFS `exact_times` but encoded as a Boolean; `false`: Frequency-based trips are not exactly scheduled. `true`: Frequency-based trips are exactly scheduled'      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
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
    headwaySeconds:      
      description: Same as GTFS `headway_secs`      
      minimum: 1      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
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
    startTime:      
      description: Same as GTFS `start_time`      
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be GtfsFrequency      
      enum:      
        - GtfsFrequency      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - hasTrip      
    - startTime      
    - endTime      
    - headwaySeconds      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsFrequency/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/GtfsFrequency/schema.json      
  x-model-tags: ""      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Example payloads      
#### GtfsFrequency NGSI-v2 key-values Example      
Here is an example of a GtfsFrequency in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
  "type": "GtfsFrequency",  
  "name": "Laborables",  
  "description": "Cada 10 minutos",  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
  "startTime": "07:00:00",  
  "endTime": "10:25:00",  
  "headwaySeconds": 600  
}  
```  
</details>    
#### GtfsFrequency NGSI-v2 normalized Example      
Here is an example of a GtfsFrequency in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
  "type": "GtfsFrequency",  
  "description": {  
    "type": "Text",  
    "value": "Cada 10 minutos"  
  },  
  "hasTrip": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1"  
  },  
  "headwaySeconds": {  
    "type": "Number",  
    "value": 600  
  },  
  "startTime": {  
    "type": "Text",  
    "value": "07:00:00"  
  },  
  "endTime": {  
    "type": "Text",  
    "value": "10:25:00"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Laborables"  
  }  
}  
```  
</details>    
#### GtfsFrequency NGSI-LD key-values Example      
Here is an example of a GtfsFrequency in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
  "type": "GtfsFrequency",  
  "description": "Cada 10 minutos",  
  "endTime": "10:25:00",  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
  "headwaySeconds": 600,  
  "name": "Laborables",  
  "startTime": "07:00:00",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### GtfsFrequency NGSI-LD normalized Example      
Here is an example of a GtfsFrequency in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
  "type": "GtfsFrequency",  
  "description": {  
    "type": "Property",  
    "value": "Cada 10 minutos"  
  },  
  "endTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-03-19T10:25:00Z"  
    }  
  },  
  "hasTrip": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1"  
  },  
  "headwaySeconds": {  
    "type": "Property",  
    "value": 600  
  },  
  "name": {  
    "type": "Property",  
    "value": "Laborables"  
  },  
  "startTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-03-19T07:00:00Z"  
    }  
  },  
  "@context": [  
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
