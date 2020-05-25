# PublicTransportStop

## Description

Generic model for a public transport stop. It adopts some GTFS definitions, but it does not need to be linked to additional GTFS data.

Link to the [specification](./doc/spec.md)

## Examples

### Normalized Example

Normalized NGSI response 

```json
{
  "id": "urn:ngsi-ld:PublicTransportStop:santander:busStop:463",
  "type": "PublicTransportStop",
  "dateModified": {
    "type": "ISO8601",
    "value": "2018-09-25T08:32:26.00Z"
  },
  "source": {
    "type": "Text",
    "value": "https://api.smartsantander.eu/"
  },
  "dataProvider": {
    "type": "Text",
    "value": "http://www.smartsantander.eu/"
  },
  "address": {
    "type": "StructuredValue",
    "value": {
      "streetAddress": "C/ La Pereda 14",
      "addressLocality": "Santander",
      "addressRegion": "Cantabria",
      "addressCountry": "Spain"
    }
  },
  "location": {
    "type": "geo:json",
    "value": {
      "type": "Point",
      "coordinates": [-3.804648385,43.478053126]
    }
  },  
  "stopCode": {
    "type": "Text",
    "value": "la_pereda_463"
  },
  "shortStopCode": {
    "type": "Text",
    "value": "463"
  },
  "name": {
    "type": "Text",
    "value": "La Pereda 14"
  },
  "wheelchairAccessible": {
    "type": "Number",
    "value": 0
  },
  "transportationType": {
    "type": "StructuredValue",
    "value": [3]
  }, 
  "refPublicTransportRoute" : {
    "type": "StructuredValue",
    "value": [
      "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3","urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N4"
    ]
  },
  "peopleCount": {
    "type": "Number",
    "value": 0
  },
  "refPeopleCountDevice": {
    "type": "Text",
    "value": "urn:ngsi-ld:PorpleCountDecice:santander:463"
  },
  "openingHoursSpecification": {
    "type": "StructuredValue",
    "value": [

    ]
  }
}
```

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`


```json
{
  "id": "urn:ngsi-ld:PublicTransportStop:santander:busStop:463",
  "type": "PublicTransportStop",
  "dateModified": "2018-09-25T08:32:26.00Z",
  "source": "https://api.smartsantander.eu/",
  "dataProvider": "http://www.smartsantander.eu/",
  "address": {
    "streetAddress": "C/ La Pereda 14",
    "addressLocality": "Santander",
    "addressRegion": "Cantabria",
    "addressCountry": "Spain"
  },
  "location": {
    "type": "Point",
    "coordinates": [-3.804648385,43.478053126]
  },  
  "stopCode": "la_pereda_463",
  "shortStopCode": "463",
  "name": "La Pereda 14",
  "wheelchairAccessible": 0,
  "transportationType": [3], 
  "refPublicTransportRoute" : [
    "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3","urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N4"
  ],
  "peopleCount":  0,
  "refPeopleCountDevice": "urn:ngsi-ld:PorpleCountDecice:santander:463",
  "openingHoursSpecification": []
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
  "id": "urn:ngsi-ld:PublicTransportStop:santander:busStop:463",
  "type": "PublicTransportStop",
  "dateModified": "2018-09-25T08:32:26.00Z",
  "source": "https://api.smartsantander.eu/",
  "dataProvider": "http://www.smartsantander.eu/",
  "entityVersion": 2.0,
  "address": {
    "type": "Property",
    "value": {
      "streetAddress": "C/ La Pereda 14",
      "addressLocality": "Santander",
      "addressRegion": "Cantabria",
      "addressCountry": "Spain"
    }
  },
  "location": {
    "type": "Property",
    "value": {
      "type": "Point",
      "coordinates": [
        -3.804648385,
        43.478053126
      ]
    }
  },
  "stopCode": {
    "type": "Property",
    "value": "la_pereda_463"
  },
  "shortStopCode": {
    "type": "Property",
    "value": "463"
  },
  "name": {
    "type": "Property",
    "value": "La Pereda 14"
  },
  "wheelchairAccessible": {
    "type": "Property",
    "value": 0
  },
  "transportationType": {
    "type": "Property",
    "value": [
      3
    ]
  },
  "refPublicTransportRoute": {
    "type": "Relationship",
    "value": [
      "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",
      "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N4"
    ]
  },
  "peopleCount": {
    "type": "Property",
    "value": 0
  },
  "refPeopleCountDevice": {
    "type": "Property",
    "value": "urn:ngsi-ld:PorpleCountDecice:santander:463"
  },
  "openingHoursSpecification": {
    "type": "Property",
    "value": [
      {
        "opens": "00:01",
        "closes": "23:59",
        "dayOfWeek": [
          "Friday",
          "Monday",
          "Thursday",
          "Tuesday",
          "Wednesday"
        ]
      }
    ]
  }
}
```
## Open issues
