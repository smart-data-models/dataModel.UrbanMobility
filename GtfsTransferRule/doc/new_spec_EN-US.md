Entity: GtfsTransferRule  
========================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **GTFS Transfer Rule**  

## List of properties  

- `alternateName`: An alternative name for this item  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`:   - `hasDestination`:   - `hasOrigin`:   - `id`:   - `minimumTransferTime`:   - `name`:   - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `transferType`:   - `type`: NGSI Entity type    
Required properties  
- `hasDestination`  - `hasOrigin`  - `id`  - `transferType`  - `type`    
See  [https://developers.google.com/transit/gtfs/reference/#transferstxt](https://developers.google.com/transit/gtfs/reference/#transferstxt)  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsTransferRule:    
  description: 'GTFS Transfer Rule'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      type: string    
    hasDestination:    
      format: uri    
      type: string    
    hasOrigin:    
      format: uri    
      type: string    
    id:    
      anyOf: &gtfstransferrule_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    minimumTransferTime:    
      minValue: 1    
      type: integer    
    name:    
      type: string    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfstransferrule_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    transferType:    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
      type: string    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - GtfsTransferRule    
      type: string    
  required:    
    - id    
    - type    
    - hasOrigin    
    - hasDestination    
    - transferType    
  type: object    
```  
</details>    
## Example payloads    
#### GtfsTransferRule NGSI V2 key-values Example    
Here is an example of a GtfsTransferRule in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsTransferRule:Malaga:Linea1_Linea5",  
  "type": "GtfsTransferRule",  
  "name": "L1_L5",  
  "hasOrigin": "urn:ngsi-ld:GtfsStop:Malaga_101",  
  "hasDestination": "urn:ngsi-ld:GtfsStop:Malaga_508",  
  "transferType": "0",  
  "minimumTransferTime": 10  
}  
```  
#### GtfsTransferRule NGSI V2 normalized Example    
Here is an example of a GtfsTransferRule in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsTransferRule:Malaga:Linea1_Linea5",  
  "type": "GtfsTransferRule",  
  "transferType": {  
    "value": "0"  
  },  
  "minimumTransferTime": {  
    "value": 10  
  },  
  "hasDestination": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsStop:Malaga_508"  
  },  
  "hasOrigin": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsStop:Malaga_101"  
  },  
  "name": {  
    "value": "L1_L5"  
  }  
}  
```  
#### GtfsTransferRule NGSI-LD key-values Example    
Here is an example of a GtfsTransferRule in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "hasDestination": "urn:ngsi-ld:GtfsStop:Malaga_508",  
 "hasOrigin": "urn:ngsi-ld:GtfsStop:Malaga_101",  
 "id": "urn:ngsi-ld:GtfsTransferRule:Malaga:Linea1_Linea5",  
 "minimumTransferTime": 10,  
 "name": "L1_L5",  
 "transferType": "0",  
 "type": "GtfsTransferRule"}  
```  
#### GtfsTransferRule NGSI-LD normalized Example    
Here is an example of a GtfsTransferRule in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:GtfsTransferRule:Malaga:Linea1_Linea5",  
    "type": "GtfsTransferRule",  
    "transferType": {  
        "type": "Property",  
        "value": "0"  
    },  
    "minimumTransferTime": {  
        "type": "Property",  
        "value": 10  
    },  
    "hasDestination": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsStop:Malaga_508"  
    },  
    "hasOrigin": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsStop:Malaga_101"  
    },  
    "name": {  
        "type": "Property",  
        "value": "L1_L5"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
