Entity: GtfsStopTime  
====================  
[Open License](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsStopTime/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **GTFS Stop Time**  

## List of properties  

- `alternateName`: An alternative name for this item  - `arrivalTime`: Same as GTFS `arrival_time`  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `departureTime`: Same as GTFS `departure_time`  - `description`: A description of this item  - `distanceTravelled`: Same as GTFS `shape_dist_traveled`  - `dropOffType`: Same as GTFS `drop_off_type`. Enum:'0, 1, 2, 3'  - `hasStop`: Same as GTFS `stop_id`. It shall point to an Entity of type GtfsStop  - `hasTrip`: Trip associated to this Entity. It shall point to an Entity of Type GtfsTrip  - `id`: Unique identifier of the entity  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `pickupType`: Same as GTFS `pickup_type`. Enum:'0, 1, 2, 3'   - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `stopHeadsign`: Same as GTFS `stop_headsign`  - `stopSequence`: Same as GTFS `stop_sequence`. Starting with `1`.  - `timepoint`: Same as GTFS `timepoint`. Enum:'0, 1'  - `type`: NGSI Entity type. It has to be GtfsStopTime    
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
      description: 'Same as GTFS `arrival_time`'    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: 'Same as GTFS `departure_time`'    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    description:    
      description: 'A description of this item'    
      type: Property    
    distanceTravelled:    
      description: 'Same as GTFS `shape_dist_traveled`'    
      minValue: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    dropOffType:    
      default: 0    
      description: 'Same as GTFS `drop_off_type`. Enum:''0, 1, 2, 3'''    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    hasStop:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Same as GTFS `stop_id`. It shall point to an Entity of type GtfsStop'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    hasTrip:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Trip associated to this Entity. It shall point to an Entity of Type GtfsTrip'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
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
      description: 'Unique identifier of the entity'    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfsstoptime_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pickupType:    
      default: 0    
      description: 'Same as GTFS `pickup_type`. Enum:''0, 1, 2, 3'' '    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
    stopHeadsign:    
      description: 'Same as GTFS `stop_headsign`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
    stopSequence:    
      description: 'Same as GTFS `stop_sequence`. Starting with `1`.'    
      minValue: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Integer    
    timepoint:    
      default: 1    
      description: 'Same as GTFS `timepoint`. Enum:''0, 1'''    
      enum:    
        - 0    
        - 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI Entity type. It has to be GtfsStopTime'    
      enum:    
        - GtfsStopTime    
      type: Property    
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
#### GtfsStopTime NGSI-v2 key-values Example    
Here is an example of a GtfsStopTime in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### GtfsStopTime NGSI-v2 normalized Example    
Here is an example of a GtfsStopTime in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### GtfsStopTime NGSI-LD normalized Example    
Here is an example of a GtfsStopTime in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "arrivalTime": "07:04:24",  
  "departureTime": "07:04:24",  
  "distanceTravelled": 759,  
  "hasStop": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737",  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011",  
  "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
  "stopSequence": 4,  
  "type": "GtfsStopTime"  
}  
```  
