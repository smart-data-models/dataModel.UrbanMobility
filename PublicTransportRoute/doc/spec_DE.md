<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: PublicTransportRoute  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/PublicTransportRoute/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Ein allgemeiner öffentlicher Verkehrsweg**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Lande liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `routeCode[string]`: ID oder Code der Strecke (z. B. HT5200104000)  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `routeColor[string]`: Der Route zugewiesene Farbe im Text  . Model: [ https://schema.org/color]( https://schema.org/color)- `routeSegments[array]`: Abschnitte dieser Route, definiert durch ihren Namen und ihre Haltestellen  - `routeTextColor[string]`: Der Route zugewiesene Farbe in hexadezimaler Form  . Model: [ https://schema.org/color]( https://schema.org/color)- `schedule[array]`: Arbeitszeiten für diese Strecke  . Model: [https://schema.org/OpeningHoursSpecification](https://schema.org/OpeningHoursSpecification)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `shortRouteCode[string]`: Kürzere Form der ID/des Codes der Strecke (z. B. 5200104000)  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `transportationType[number]`: Arten von öffentlichen Verkehrsmitteln, die diese Haltestelle benutzen, wie in (https://developers.google.com/transit/gtfs/reference/#routestxt) definiert. Enum:'0, 1, 2, 3, 4, 5, 6, 7'  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI-Entitätstyp. Es muss PublicTransportRoute sein  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `transportationType`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
Generisches Modell für Strecken des öffentlichen Verkehrs. Es übernimmt einige GTFS-Definitionen, muss aber nicht mit zusätzlichen GTFS-Daten verknüpft werden. Eine Route ist eine Fahrt, die von einem öffentlichen Verkehrsdienst angeboten wird und durch eine Reihe von Haltestellen führt.  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PublicTransportRoute:    
  description: A generic public transport route data model    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    routeCode:    
      description: ID or code of the route (e.g. HT5200104000)    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        type: Property    
    routeColor:    
      description: Color assigned to route in text    
      pattern: "^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$"    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/color'    
        type: Property    
    routeSegments:    
      description: Segments of this route defined by their name and stops    
      items:    
        properties:    
          refPublicTransportStops:    
            description: relation to public transport stops    
            items:    
              format: uri    
              type: string    
            type: array    
            x-ngsi:    
              type: Relationship    
          segmentName:    
            description: Name of the segment in route    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    routeTextColor:    
      description: Color assigned to route in hexadecimal    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/color'    
        type: Property    
    schedule:    
      description: Working hours of this route    
      items:    
        properties:    
          closes:    
            description: Time for the end of the route    
            pattern: "[0-9]{2}:[0-9]{2}"    
            type: string    
            x-ngsi:    
              type: Property    
          dayOfWeek:    
            description: Day of the week for the route schedule    
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
            x-ngsi:    
              type: Property    
          opens:    
            description: Time for the start of the route    
            pattern: "[0-9]{2}:[0-9]{2}"    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/OpeningHoursSpecification    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
    shortRouteCode:    
      description: Shorter form of the ID/code of the route (e.g. 5200104000)    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    transportationType:    
      description: "Types of public transport using this stop as defined in (https://developers.google.com/transit/gtfs/reference/#routestxt). Enum:'0, 1, 2, 3, 4, 5, 6, 7'"    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be PublicTransportRoute    
      enum:    
        - PublicTransportRoute    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - transportationType    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/PublicTransportRoute/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/PublicTransportRoute/schema.json    
  x-model-tags: SynchroniCity    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### PublicTransportRoute NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine PublicTransportRoute im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
  "type": "PublicTransportRoute",  
  "source": "https://api.smartsantander.eu/",  
  "dataProvider": "http://www.smartsantander.eu/",  
  "routeCode": "5200103000",  
  "shortRouteCode": "N3",  
  "name": "PE ACASTILLO-PLAZA DE ITALIA",  
  "transportationType": 3,  
  "routeColor": "#ff0000",  
  "routeTextColor": "RED",  
  "routeSegments": [  
    {  
      "segmentName": "PE ACASTILLO-PLAZA DE ITALIA:1",  
      "refPublicTransportStops": [  
        "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:311",  
        "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:129"  
      ]  
    },  
    {  
      "segmentName": "PE ACASTILLO-PLAZA DE ITALIA:2",  
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
</details>  
#### PublicTransportRoute NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine PublicTransportRoute im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
    "value": "PE\u00d1ACASTILLO-PLAZA DE ITALIA"  
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
        "segmentName": "PE\u00d1ACASTILLO-PLAZA DE ITALIA:1",  
        "refPublicTransportStops": [  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:311",  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:129"  
        ]  
      },  
      {  
        "segmentName": "PE\u00d1ACASTILLO-PLAZA DE ITALIA:2",  
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
</details>  
#### PublicTransportRoute NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine PublicTransportRoute im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
  "type": "PublicTransportRoute",  
  "dataProvider": "http://www.smartsantander.eu/",  
  "name": "PE CASTILLO-PLAZA DE ITALIA",  
  "routeCode": "5200103000",  
  "routeColor": "#ff0000",  
  "routeSegments": [  
    {  
      "segmentName": "PE ACASTILLO-PLAZA DE ITALIA:1",  
      "refPublicTransportStops": [  
        "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:311",  
        "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:129"  
      ]  
    },  
    {  
      "segmentName": "PE ACASTILLO-PLAZA DE ITALIA:2",  
      "refPublicTransportStops": [  
        "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:130",  
        "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:131"  
      ]  
    }  
  ],  
  "routeTextColor": "RED",  
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
  ],  
  "shortRouteCode": "N3",  
  "source": "https://api.smartsantander.eu/",  
  "transportationType": 3,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### PublicTransportRoute NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine PublicTransportRoute im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
    "type": "PublicTransportRoute",  
    "dataProvider": "http://www.smartsantander.eu/",  
    "entityVersion": 2.0,  
    "name": {  
        "type": "Property",  
        "value": "PE ACASTILLO-PLAZA DE ITALIA "  
    },  
    "routeCode": {  
        "type": "Property",  
        "value": "5200103000"  
    },  
    "routeColor": {  
        "type": "Property",  
        "value": "#ff0000"  
    },  
    "routeSegments": {  
        "type": "Property",  
        "value": [  
            {  
                "segmentName": "PE ACASTILLO-PLAZA DE ITALIA:1",  
                "refPublicTransportStops": [  
                    "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:311",  
                    "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:129"  
                ]  
            },  
            {  
                "segmentName": "PE ACASTILLO-PLAZA DE ITALIA:2",  
                "refPublicTransportStops": [  
                    "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:130",  
                    "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:131"  
                ]  
            }  
        ]  
    },  
    "routeTextColor": {  
        "type": "Property",  
        "value": "RED"  
    },  
    "schedule": {  
        "type": "Property",  
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
    "shortRouteCode": {  
        "type": "Property",  
        "value": "N3"  
    },  
    "source": "https://api.smartsantander.eu/",  
    "transportationType": {  
        "type": "Property",  
        "value": 3  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
