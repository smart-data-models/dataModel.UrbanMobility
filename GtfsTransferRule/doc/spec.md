Entity: GtfsTransferRule  
========================  
[Open License](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsTransferRule/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **GTFS Transfer Rule**  

## List of properties  

- `alternateName`: An alternative name for this item  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `hasDestination`: Trip associated to this Entity. It shall point to an Entity of type GtfsStop or GtfsStation  - `hasOrigin`: Trip associated to this Entity. It shall point to an Entity of type GtfsStop or GtfsStation  - `id`: Unique identifier of the entity  - `minimumTransferTime`: Same as GTFS `min_transfer_time`. Unit:'seconds'  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `transferType`: Same as GTFS `transfer_type`. Enum:'0, 1, 2, 3'  - `type`: NGSI Entity type. It has to be GtfsTransferRule    
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
      description: 'A description of this item'    
      type: Property    
    hasDestination:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Trip associated to this Entity. It shall point to an Entity of type GtfsStop or GtfsStation'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    hasOrigin:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Trip associated to this Entity. It shall point to an Entity of type GtfsStop or GtfsStation'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
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
      description: 'Unique identifier of the entity'    
      type: Property    
    minimumTransferTime:    
      description: 'Same as GTFS `min_transfer_time`. Unit:''seconds'''    
      minValue: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Integer    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfstransferrule_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    transferType:    
      description: 'Same as GTFS `transfer_type`. Enum:''0, 1, 2, 3'''    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI Entity type. It has to be GtfsTransferRule'    
      enum:    
        - GtfsTransferRule    
      type: Property    
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
#### GtfsTransferRule NGSI-v2 key-values Example    
Here is an example of a GtfsTransferRule in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### GtfsTransferRule NGSI-v2 normalized Example    
Here is an example of a GtfsTransferRule in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### GtfsTransferRule NGSI-LD normalized Example    
Here is an example of a GtfsTransferRule in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "hasDestination": "urn:ngsi-ld:GtfsStop:Malaga_508",  
  "hasOrigin": "urn:ngsi-ld:GtfsStop:Malaga_101",  
  "id": "urn:ngsi-ld:GtfsTransferRule:Malaga:Linea1_Linea5",  
  "minimumTransferTime": 10,  
  "name": "L1_L5",  
  "transferType": "0",  
  "type": "GtfsTransferRule"  
}  
```  
