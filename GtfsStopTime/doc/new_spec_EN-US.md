Entity: GtfsStopTime  
====================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **GTFS Stop Time**  

## List of properties  

- `alternateName`: An alternative name for this item  - `arrivalTime`:   - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `departureTime`:   - `description`: A description of this item  - `distanceTravelled`:   - `dropOffType`:   - `hasStop`:   - `hasTrip`:   - `id`:   - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `pickupType`:   - `seeAlso`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `stopHeadsign`:   - `stopSequence`:   - `timepoint`:   - `type`: NGSI Entity type    
Required properties  
- `arrivalTime`  - `departureTime`  - `hasStop`  - `hasTrip`  - `id`  - `stopSequence`  - `type`    
See [https://developers.google.com/transit/gtfs/reference/#stop_timestxt](https://developers.google.com/transit/gtfs/reference/#stop_timestxt)  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsStopTime:    
  description: 'GTFS Stop Time'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    arrivalTime:    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
      type: string    
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
    departureTime:    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
      type: string    
    description:    
      description: 'A description of this item'    
      type: Property    
    distanceTravelled:    
      minValue: 0    
      type: number    
    dropOffType:    
      default: 0    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
      type: string    
    hasStop:    
      format: uri    
      type: string    
    hasTrip:    
      format: uri    
      type: string    
    id:    
      anyOf: &gtfsstoptime_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfsstoptime_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    pickupType:    
      default: 0    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
      type: string    
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
    stopHeadsign:    
      type: string    
    stopSequence:    
      minValue: 1    
      type: integer    
    timepoint:    
      default: 1    
      enum:    
        - 0    
        - 1    
      type: string    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - GtfsStopTime    
      type: string    
  required:    
    - id    
    - type    
    - arrivalTime    
    - departureTime    
    - hasStop    
    - hasTrip    
    - stopSequence    
  type: object    
```  
</details>    
## Example payloads    
#### GtfsStopTime NGSI V2 key-values Example    
Here is an example of a GtfsStopTime in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
  "type": "GtfsStopTime",  
  "hasStop": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737",  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011",  
  "distanceTravelled": 759,  
  "stopSequence": 4,  
  "arrivalTime": "07:04:24",  
  "departureTime": "07:04:24"  
}  
```  
#### GtfsStopTime NGSI V2 normalized Example    
Here is an example of a GtfsStopTime in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
  "type": "GtfsStopTime",  
  "departureTime": {  
    "value": "07:04:24"  
  },  
  "hasTrip": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011"  
  },  
  "stopSequence": {  
    "value": 4  
  },  
  "distanceTravelled": {  
    "value": 759  
  },  
  "arrivalTime": {  
    "value": "07:04:24"  
  },  
  "hasStop": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737"  
  }  
}  
```  
#### GtfsStopTime NGSI-LD key-values Example    
Here is an example of a GtfsStopTime in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "arrivalTime": "07:04:24",  
 "departureTime": "07:04:24",  
 "distanceTravelled": 759,  
 "hasStop": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737",  
 "hasTrip": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011",  
 "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
 "stopSequence": 4,  
 "type": "GtfsStopTime"}  
```  
#### GtfsStopTime NGSI-LD normalized Example    
Here is an example of a GtfsStopTime in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
    "type": "GtfsStopTime",  
    "departureTime": {  
        "type": "Property",  
        "value": "07:04:24"  
    },  
    "hasTrip": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011"  
    },  
    "stopSequence": {  
        "type": "Property",  
        "value": 4  
    },  
    "distanceTravelled": {  
        "type": "Property",  
        "value": 759  
    },  
    "arrivalTime": {  
        "type": "Property",  
        "value": "07:04:24"  
    },  
    "hasStop": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
