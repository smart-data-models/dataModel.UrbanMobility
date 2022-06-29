Entität: PublicTransportStop  
============================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/PublicTransportStop/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Eine allgemeine Haltestelle für öffentliche Verkehrsmittel**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `openingHoursSpecification`: Ein strukturierter Wert, der Informationen über die Öffnungszeiten eines Ortes oder einer bestimmten Dienstleistung an einem Ort liefert  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `peopleCount`: Schätzung der an der Haltestelle wartenden Personen  - `refPeopleCountDevice`: Verweis auf das [Gerät](https://github.com/Fiware/dataModels/blob/master/specs/Device/Device/doc/spec.md), das eine Schätzung der Personenzahl liefert.  - `refPublicTransportRoute`: Öffentliche Verkehrsmittel, die diese Haltestelle anfahren.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `shortStopCode`: Kurzform der Kennung/des Codes der Haltestelle des öffentlichen Verkehrs  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `stopCode`: Kennung/Code der Haltestelle des öffentlichen Verkehrsmittels  - `transportationType`: Arten von öffentlichen Verkehrsmitteln, die diese Haltestelle benutzen, wie in (https://developers.google.com/transit/gtfs/reference/#routestxt) definiert. Enum:'0, 1, 2, 3, 4, 5, 6, 7'  - `type`: NGSI-Entitätstyp. Es muss PublicTransportStop sein.  - `wheelChairAccessible`: Gleich wie GTFS `Rollstuhl_Einsteigen`. Enum:'0, 1 ,2'. Verweis in [GTFS](https://developers.google.com/transit/gtfs/reference/#stopstxt)    
Erforderliche Eigenschaften  
- `id`  - `name`  - `transportationType`  - `type`    
Generisches Modell für eine Haltestelle des öffentlichen Verkehrs. Es übernimmt einige GTFS-Definitionen, muss aber nicht mit zusätzlichen GTFS-Daten verknüpft werden.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PublicTransportStop:    
  description: 'A generic public transport stop'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &publictransportstop_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    openingHoursSpecification:    
      description: 'A structured value providing information about the opening hours of a place or a certain service inside a place'    
      items:    
        properties:    
          closes:    
            format: time    
            type: string    
          dayOfWeek:    
            enum:    
              - Monday    
              - Tuesday    
              - Wednesday    
              - Thursday    
              - Friday    
              - Saturday    
              - Sunday    
              - PublicHolidays    
            type: string    
          opens:    
            format: time    
            type: string    
          validFrom:    
            format: date-time    
            type: string    
          validThrough:    
            format: date-time    
            type: string    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *publictransportstop_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    peopleCount:    
      description: 'Estimation of people waiting in the stop'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    refPeopleCountDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the [Device](https://github.com/Fiware/dataModels/blob/master/specs/Device/Device/doc/spec.md) providing people count estimate.'    
      type: string    
      x-ngsi:    
        type: Property    
    refPublicTransportRoute:    
      description: 'Public transport routes using this stop.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: ' https://schema.org/URL'    
        type: Relationship    
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
      x-ngsi:    
        type: Property    
    shortStopCode:    
      description: 'Shorter form of the identifier/code of the public transport stop'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    stopCode:    
      description: 'Identifier/code of the public transport stop'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
        type: Property    
    transportationType:    
      description: "Types of public transport using this stop as defined in (https://developers.google.com/transit/gtfs/reference/#routestxt). Enum:'0, 1, 2, 3, 4, 5, 6, 7'"    
      items:    
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
      type: array    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be PublicTransportStop'    
      enum:    
        - PublicTransportStop    
      type: string    
      x-ngsi:    
        type: Property    
    wheelChairAccessible:    
      description: "Same as GTFS `wheelchair_boarding`. Enum:'0, 1 ,2'. Reference in [GTFS](https://developers.google.com/transit/gtfs/reference/#stopstxt) "    
      enum:    
        - 0    
        - 1    
        - 2    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - transportationType    
    - name    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### PublicTransportStop NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine PublicTransportStop im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
    "coordinates": [  
      -3.804648385,  
      43.478053126  
    ]  
  },  
  "stopCode": "la_pereda_463",  
  "shortStopCode": "463",  
  "name": "La Pereda 14",  
  "wheelchairAccessible": 0,  
  "transportationType": [  
    3  
  ],  
  "refPublicTransportRoute": [  
    "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
    "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N4"  
  ],  
  "peopleCount": 0,  
  "refPeopleCountDevice": "urn:ngsi-ld:PorpleCountDecice:santander:463",  
 "openingHoursSpecification":   
  [  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Monday"  
    },  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Tuesday"  
    },  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Wednesday"  
    },  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Thursday"  
    },  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Friday"  
    }  
  ]  
}  
```  
#### PublicTransportStop NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine PublicTransportStop im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
      "coordinates": [  
        -3.804648385,  
        43.478053126  
      ]  
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
    "value": [  
      3  
    ]  
  },  
  "refPublicTransportRoute": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
      "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N4"  
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
      {  
        "opens" : {  
          "type": "string",   
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek":{  
          "type": "string",  
          "value": "Friday"  
        }  
      },  
      {  
        "opens" : {  
          "type": "string",   
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek":{  
          "type": "string",  
          "value": "Monday"  
        }  
      },  
      {  
        "opens" : {  
          "type": "string",   
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek":{  
          "type": "string",  
          "value": "Tuesday"  
        }  
      },  
      {  
        "opens" : {  
          "type": "string",   
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek":{  
          "type": "string",  
          "value": "Thursday"  
        }  
      },  
      {  
        "opens" : {  
          "type": "string",   
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek":{  
          "type": "string",  
          "value": "Wednesday"  
        }  
      }  
    ]    
  }  
}  
```  
#### PublicTransportStop NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine PublicTransportStop im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportStop:santander:busStop:463",  
  "type": "PublicTransportStop",  
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
      "coordinates": [  
        -3.804648385,  
        43.478053126  
      ]  
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
    "value": [  
      3  
    ]  
  },  
  "refPublicTransportRoute": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
      "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N4"  
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
      {  
        "opens": {  
          "type": "string",  
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek": {  
          "type": "string",  
          "value": "Friday"  
        }  
      },  
      {  
        "opens": {  
          "type": "string",  
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek": {  
          "type": "string",  
          "value": "Monday"  
        }  
      },  
      {  
        "opens": {  
          "type": "string",  
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek": {  
          "type": "string",  
          "value": "Tuesday"  
        }  
      },  
      {  
        "opens": {  
          "type": "string",  
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek": {  
          "type": "string",  
          "value": "Thursday"  
        }  
      },  
      {  
        "opens": {  
          "type": "string",  
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek": {  
          "type": "string",  
          "value": "Wednesday"  
        }  
      }  
    ]  
  },  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### PublicTransportStop NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine PublicTransportStop im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
    "streetAddress": "C/ La Pereda 14",  
    "addressLocality": "Santander",  
    "addressRegion": "Cantabria",  
    "addressCountry": "Spain"  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.804648385,  
      43.478053126  
    ]  
  },  
  "stopCode": "la_pereda_463",  
  "shortStopCode": "463",  
  "name": "La Pereda 14",  
  "wheelchairAccessible": 0,  
  "transportationType": [  
    3  
  ],  
  "refPublicTransportRoute": [  
    "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
    "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N4"  
  ],  
  "peopleCount": 0,  
  "refPeopleCountDevice": "urn:ngsi-ld:PorpleCountDecice:santander:463",  
  "openingHoursSpecification": [  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Monday"  
    },  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Tuesday"  
    },  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Wednesday"  
    },  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Thursday"  
    },  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Friday"  
    }  
  ]  
}  
```  

Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht
