Entity: GtfsCalendarRule  
========================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **Smart Data Models. GTFS Calendar Rule**  

## List of properties  

- `alternateName`: An alternative name for this item  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `endDate`: End date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `end_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)  - `friday`: Same as GTFS `friday`  - `hasService`: Service to which this rule applies to. Derived from `service_id`  - `id`:   - `monday`: Same as GTFS `monday`  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `saturday`: Same as GTFS `saturday`  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `startDate`: Start date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `start_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)  - `sunday`: Same as GTFS `sunday`  - `thursday`: Same as GTFS `thursday`  - `tuesday`: Same as GTFS `tuesday`  - `type`: NGSI Entity Type: It has to be GtfsCalendarRule  - `wednesday`: Same as GTFS `wednesday`    
Required properties  
- `endDate`  - `friday`  - `hasService`  - `id`  - `monday`  - `saturday`  - `startDate`  - `sunday`  - `thursday`  - `tuesday`  - `type`  - `wednesday`    
See [https://developers.google.com/transit/gtfs/reference/#calendartxt](https://developers.google.com/transit/gtfs/reference/#calendartxt)  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsCalendarRule:    
  description: 'Smart Data Models. GTFS Calendar Rule'    
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
    endDate:    
      description: "End date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `end_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)"    
      format: date    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    friday:    
      description: 'Same as GTFS `friday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    hasService:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Service to which this rule applies to. Derived from `service_id`'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    id:    
      anyOf: &gtfscalendarrule_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    monday:    
      description: 'Same as GTFS `monday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfscalendarrule_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    saturday:    
      description: 'Same as GTFS `saturday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    startDate:    
      description: "Start date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `start_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)"    
      format: date    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Date    
    sunday:    
      description: 'Same as GTFS `sunday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    thursday:    
      description: 'Same as GTFS `thursday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    tuesday:    
      description: 'Same as GTFS `tuesday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    type:    
      description: 'NGSI Entity Type: It has to be GtfsCalendarRule'    
      enum:    
        - GtfsCalendarRule    
      type: Property    
    wednesday:    
      description: 'Same as GTFS `wednesday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
  required:    
    - id    
    - type    
    - hasService    
    - monday    
    - tuesday    
    - wednesday    
    - thursday    
    - friday    
    - saturday    
    - sunday    
    - startDate    
    - endDate    
  type: object    
```  
</details>    
## Example payloads    
#### GtfsCalendarRule NGSI V2 key-values Example    
Here is an example of a GtfsCalendarRule in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "type": "GtfsCalendarRule",  
  "name": "Rule Hospital Service 1",  
  "hasService": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1",  
  "monday": true,  
  "tuesday": true,  
  "wednesday": true,  
  "thursday": true,  
  "friday": true,  
  "saturday": false,  
  "sunday": false,  
  "startDate": "2018-01-01",  
  "endDate": "2019-01-01"  
}  
```  
#### GtfsCalendarRule NGSI V2 normalized Example    
Here is an example of a GtfsCalendarRule in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "type": "GtfsCalendarRule",  
  "startDate": {  
    "type": "Date",  
    "value": "2018-01-01"  
  },  
  "endDate": {  
    "type": "Date",  
    "value": "2019-01-01"  
  },  
  "name": {  
    "value": "Rule Hospital Service 1"  
  },  
  "monday": {  
    "value": true  
  },  
  "tuesday": {  
    "value": true  
  },  
  "friday": {  
    "value": true  
  },  
  "wednesday": {  
    "value": true  
  },  
  "thursday": {  
    "value": true  
  },  
  "sunday": {  
    "value": false  
  },  
  "hasService": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1"  
  },  
  "saturday": {  
    "value": false  
  }  
}  
```  
#### GtfsCalendarRule NGSI-LD key-values Example    
Here is an example of a GtfsCalendarRule in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "endDate": {"@type": "Date", "@value": "2019-01-01"},  
 "friday": True,  
 "hasService": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1",  
 "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
 "monday": True,  
 "name": "Rule Hospital Service 1",  
 "saturday": False,  
 "startDate": {"@type": "Date", "@value": "2018-01-01"},  
 "sunday": False,  
 "thursday": True,  
 "tuesday": True,  
 "type": "GtfsCalendarRule",  
 "wednesday": True}  
```  
#### GtfsCalendarRule NGSI-LD normalized Example    
Here is an example of a GtfsCalendarRule in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
    "type": "GtfsCalendarRule",  
    "startDate": {  
        "type": "Property",  
        "value": {  
            "@type": "Date",  
            "@value": "2018-01-01"  
        }  
    },  
    "endDate": {  
        "type": "Property",  
        "value": {  
            "@type": "Date",  
            "@value": "2019-01-01"  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Rule Hospital Service 1"  
    },  
    "monday": {  
        "type": "Property",  
        "value": true  
    },  
    "tuesday": {  
        "type": "Property",  
        "value": true  
    },  
    "friday": {  
        "type": "Property",  
        "value": true  
    },  
    "wednesday": {  
        "type": "Property",  
        "value": true  
    },  
    "thursday": {  
        "type": "Property",  
        "value": true  
    },  
    "sunday": {  
        "type": "Property",  
        "value": false  
    },  
    "hasService": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1"  
    },  
    "saturday": {  
        "type": "Property",  
        "value": false  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
