# PublicTransportRoute

## Description

Generic model for public transport route. It adopts some GTFS definitions, but it does not need to be linked to additional GTFS data. A route is a journey, offered by one public transport service, that goes through a set of stops.

Link to the [specification](./doc/spec.md)

## Examples of use

### Normalized Example

Normalized NGSI response 

```json
{
  "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",
  "type": "PublicTransportRoute",
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
  "routeSegments": 
  {
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
  "schedule":{
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
        "opens":  "09:00",
        "closes": "14:00"      
      }
    ]
  }  
}
```

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
  "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",
  "type": "PublicTransportRoute",
  "routeCode": "5200103000",
  "shortRouteCode": "N3",
  "name": "PEÑACASTILLO-PLAZA DE ITALIA ",
  "transportationType": 3,
  "routeSegments": [
    {
      "segmentName": "PEÑACASTILLO-PLAZA DE ITALIA:1",
      "refPublicTransportStops":  [
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
      "validFrom": "2018-01-24",
      "validThrough": "2018-05-25",
      "opens": "09:00",
      "closes": "23:00"
    },
    {
      "dayOfWeek": "Sunday",
      "opens":  "09:00",
      "closes": "14:00"      
    }
  ]  
}
```

### LD Example

Sample uses the NGSI-LD representation

## Open issues

  + ``routeSegments`` attribute could be defined as an external entity, so that they can be re-used by several routes, even if they are of different.`transportationType`. This will be decided upon feedback from cities and different requirements of different transportation urban services. 
  