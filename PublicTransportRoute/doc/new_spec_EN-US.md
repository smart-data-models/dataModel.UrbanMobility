Entity: PublicTransportRoute  
============================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **A generic public transport route**  

## List of properties  

- `address`: The mailing address.  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided.  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `id`:   - `location`:   - `name`:   - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `routeCode`:   - `routeColor`:   - `routeSegments`:   - `routeTextColor`:   - `schedule`:   - `seeAlso`:   - `shortRouteCode`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `transportationType`:   - `type`: NGSI Entity type    
Required properties  
- `id`  - `transportationType`  - `type`    
Generic model for public transport route. It adopts some GTFS definitions, but it does not need to be linked to additional GTFS data. A route is a journey, offered by one public transport service, that goes through a set of stops.  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PublicTransportRoute:    
  description: 'A generic public transport route'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
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
    id:    
      anyOf: &publictransportroute_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    name:    
      type: string    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *publictransportroute_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    routeCode:    
      type: string    
    routeColor:    
      pattern: "^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$"    
      type: string    
    routeSegments:    
      items:    
        properties:    
          refPublicTransportStops:    
            items:    
              format: uri    
              type: string    
            type: array    
          segmentName:    
            type: string    
        required:    
          - segmentName    
          - refPublicTransportStops    
        type: object    
      type: array    
    routeTextColor:    
      type: string    
    schedule:    
      items:    
        properties:    
          closes:    
            pattern: "[0-9]{2}:[0-9]{2}"    
            type: string    
          dayOfWeek:    
            enum:    
              - Friday    
              - Monday    
              - PublicHolidays    
              - Saturday    
              - Sunday    
              - Thursday    
              - Tuesday    
              - Wednesday    
            type: string    
          opens:    
            pattern: "[0-9]{2}:[0-9]{2}"    
            type: string    
      minItems: 1    
      type: array    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    shortRouteCode:    
      type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    transportationType:    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
      type: integer    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - PublicTransportRoute    
      type: string    
  required:    
    - id    
    - type    
    - transportationType    
  type: object    
```  
</details>    
## Example payloads    
#### PublicTransportRoute NGSI V2 key-values Example    
Here is an example of a PublicTransportRoute in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
  "type": "PublicTransportRoute",  
  "source": "https://api.smartsantander.eu/",  
  "dataProvider": "http://www.smartsantander.eu/",  
  "routeCode": "5200103000",  
  "shortRouteCode": "N3",  
  "name": "PEÑACASTILLO-PLAZA DE ITALIA ",  
  "transportationType": 3,  
  "routeColor": "#ff0000",  
  "routeTextColor": "RED",  
  "routeSegments": [  
    {  
      "segmentName": "PEÑACASTILLO-PLAZA DE ITALIA:1",  
      "refPublicTransportStops": [  
        "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:311",  
        "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:129"  
      ]  
    },  
    {  
      "segmentName": "PEÑACASTILLO-PLAZA DE ITALIA:2",  
      "refPublicTransportStops": [  
        "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:130",  
        "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:131"  
      ]  
    }  
  ],  
  "schedule": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "09:00",  
      "closes": "23:00"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "09:00",  
      "closes": "23:00"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "09:00",  
      "closes": "23:00"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "09:00",  
      "closes": "23:00"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "09:00",  
      "closes": "23:00"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "09:00",  
      "closes": "14:00"  
    }  
  ]  
}  
```  
#### PublicTransportRoute NGSI V2 normalized Example    
Here is an example of a PublicTransportRoute in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
  "type": "PublicTransportRoute",  
  "source": {  
    "type": "Text",  
    "value": "https://api.smartsantander.eu/"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "http://www.smartsantander.eu/"  
  },  
  "routeCode": {  
    "type": "Text",  
    "value": "5200103000"  
  },  
  "shortRouteCode": {  
    "type": "Text",  
    "value": "N3"  
  },  
  "name": {  
    "type": "Text",  
    "value": "PEÑACASTILLO-PLAZA DE ITALIA"  
  },  
  "transportationType": {  
    "type": "Number",  
    "value": 3  
  },  
  "routeColor": {  
    "type": "Text",  
    "value": "#ff0000"  
  },  
  "routeTextColor": {  
    "type": "Text",  
    "value": "RED"  
  },  
  "routeSegments": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "segmentName": "PEÑACASTILLO-PLAZA DE ITALIA:1",  
        "refPublicTransportStops": [  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:311",  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:129"  
        ]  
      },  
      {  
        "segmentName": "PEÑACASTILLO-PLAZA DE ITALIA:2",  
        "refPublicTransportStops": [  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:130",  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:131"  
        ]  
      }  
    ]  
  },  
  "schedule": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "validFrom": "2018-01-24",  
        "validThrough": "2018-05-25",  
        "opens": "09:00",  
        "closes": "23:00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "09:00",  
        "closes": "14:00"  
      }  
    ]  
  }  
}  
```  
#### PublicTransportRoute NGSI-LD key-values Example    
Here is an example of a PublicTransportRoute in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
  "type": "PublicTransportRoute",  
  "source": "https://api.smartsantander.eu/",  
  "dataProvider": "http://www.smartsantander.eu/",  
  "entityVersion": 2.0,  
  "routeCode": {  
    "type": "Property",  
    "value": "5200103000"  
  },  
  "shortRouteCode": {  
    "type": "Property",  
    "value": "N3"  
  },  
  "name": {  
    "type": "Property",  
    "value": "PEÑACASTILLO-PLAZA DE ITALIA "  
  },  
  "transportationType": {  
    "type": "Property",  
    "value": 3  
  },  
  "routeColor": {  
    "type": "Property",  
    "value": "#ff0000"  
  },  
  "routeTextColor": {  
    "type": "Property",  
    "value": "RED"  
  },  
  "routeSegments": {  
    "type": "Property",  
    "value": [  
      {  
        "segmentName": "PEÑACASTILLO-PLAZA DE ITALIA:1",  
        "refPublicTransportStops": [  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:311",  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:129"  
        ]  
      },  
      {  
        "segmentName": "PEÑACASTILLO-PLAZA DE ITALIA:2",  
        "refPublicTransportStops": [  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:130",  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:131"  
        ]  
      }  
    ]  
  },  
  "schedule": {  
    "type": "Property"  
    "value": [  
      {  
        "validFrom": "2018-01-24",  
        "validThrough": "2018-05-25",  
        "opens": "09:00",  
        "closes": "23:00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "09:00",  
        "closes": "14:00"  
      }  
    ]  
  }  
}  
```  
#### PublicTransportRoute NGSI-LD normalized Example    
Here is an example of a PublicTransportRoute in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
  "type": "PublicTransportRoute",  
  "source": {  
    "type": "Text",  
    "value": "https://api.smartsantander.eu/"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "http://www.smartsantander.eu/"  
  },  
  "routeCode": {  
    "type": "Text",  
    "value": "5200103000"  
  },  
  "shortRouteCode": {  
    "type": "Text",  
    "value": "N3"  
  },  
  "name": {  
    "type": "Text",  
    "value": "PEÑACASTILLO-PLAZA DE ITALIA"  
  },  
  "transportationType": {  
    "type": "Number",  
    "value": 3  
  },  
  "routeColor": {  
    "type": "Text",  
    "value": "#ff0000"  
  },  
  "routeTextColor": {  
    "type": "Text",  
    "value": "RED"  
  },  
  "routeSegments": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "segmentName": "PEÑACASTILLO-PLAZA DE ITALIA:1",  
        "refPublicTransportStops": [  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:311",  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:129"  
        ]  
      },  
      {  
        "segmentName": "PEÑACASTILLO-PLAZA DE ITALIA:2",  
        "refPublicTransportStops": [  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:130",  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:131"  
        ]  
      }  
    ]  
  },  
  "schedule": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "validFrom": "2018-01-24",  
        "validThrough": "2018-05-25",  
        "opens": "09:00",  
        "closes": "23:00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "09:00",  
        "closes": "14:00"  
      }  
    ]  
  },  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
