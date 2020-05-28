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

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

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
```

### LD Example

Sample uses the NGSI-LD representation

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

## Open issues

  + ``routeSegments`` attribute could be defined as an external entity, so that they can be re-used by several routes, even if they are of different.`transportationType`. This will be decided upon feedback from cities and different requirements of different transportation urban services. 
  