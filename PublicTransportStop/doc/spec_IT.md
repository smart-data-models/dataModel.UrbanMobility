<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: Fermata del trasporto pubblico    
======================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/PublicTransportStop/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Una generica fermata del trasporto pubblico**    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `openingHoursSpecification[array]`: Un valore strutturato che fornisce informazioni sugli orari di apertura di un luogo o di un determinato servizio all'interno di un luogo.  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `peopleCount[number]`: Stima delle persone in attesa nella fermata  . Model: [https://schema.org/Number](https://schema.org/Number)- `refPeopleCountDevice[string]`: Riferimento al [Dispositivo](https://github.com/Fiware/dataModels/blob/master/specs/Device/Device/doc/spec.md) che fornisce la stima del numero di persone  - `refPublicTransportRoute[array]`: Percorsi di trasporto pubblico che utilizzano questa fermata  . Model: [ https://schema.org/URL]( https://schema.org/URL)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `shortStopCode[string]`: Forma abbreviata dell'identificativo/codice della fermata del trasporto pubblico.  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `stopCode[string]`: Identificatore/codice della fermata del trasporto pubblico  . Model: [https://schema.org/Text](https://schema.org/Text)- `transportationType[array]`: Tipi di trasporto pubblico che utilizzano questa fermata, come definito in (https://developers.google.com/transit/gtfs/reference/#routestxt). Enum:'0, 1, 2, 3, 4, 5, 6, 7'  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo di entità NGSI. Deve essere PublicTransportStop  - `wheelChairAccessible[string]`: Uguale a GTFS `salita_a_sedia`. Enum:'0, 1 ,2'. Riferimento in [GTFS](https://developers.google.com/transit/gtfs/reference/#stopstxt)  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `name`  - `transportationType`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Modello generico per una fermata del trasporto pubblico. Adotta alcune definizioni GTFS, ma non ha bisogno di essere collegato ad altri dati GTFS.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
PublicTransportStop:      
  description: A generic public transport stop      
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
    openingHoursSpecification:      
      description: A structured value providing information about the opening hours of a place or a certain service inside a place      
      items:      
        properties:      
          closes:      
            description: ' 	The closing hour of the place or service on the given day(s) of the week'      
            format: time      
            type: string      
            x-ngsi:      
              type: Property      
          dayOfWeek:      
            anyOf:      
              - description: Array of days of the week      
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
                x-ngsi:      
                  type: Property      
              - description: Array of days of the week      
                enum:      
                  - https://schema.org/Monday      
                  - https://schema.org/Tuesday      
                  - https://schema.org/Wednesday      
                  - https://schema.org/Thursday      
                  - https://schema.org/Friday      
                  - https://schema.org/Saturday      
                  - https://schema.org/Sunday      
                  - https://schema.org/PublicHolidays      
                type: string      
                x-ngsi:      
                  type: Property      
            description: 'The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays)'      
            type: string      
            x-ngsi:      
              model: http://schema.org/dayOfWeek      
              type: Property      
          opens:      
            description: The opening hour of the place or service on the given day(s) of the week      
            format: time      
            type: string      
            x-ngsi:      
              type: Property      
          validFrom:      
            anyOf:      
              - description: ""      
                format: date      
                type: string      
                x-ngsi:      
                  model: http://schema.org/Date      
                  type: Property      
              - description: ""      
                format: date-time      
                type: string      
                x-ngsi:      
                  model: http://schema.org/DateTime      
                  type: Property      
            description: 'The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format'      
            x-ngsi:      
              type: Property      
          validThrough:      
            anyOf:      
              - description: ""      
                format: date      
                type: string      
                x-ngsi:      
                  model: http://schema.org/Date      
                  type: Property      
              - description: ""      
                format: date-time      
                type: string      
                x-ngsi:      
                  model: http://schema.org/DateTime      
                  type: Property      
            description: 'The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format'      
            type: string      
            x-ngsi:      
              type: Property      
        type: object      
      minItems: 1      
      type: array      
      x-ngsi:      
        model: https://schema.org/openingHoursSpecification      
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
    peopleCount:      
      description: Estimation of people waiting in the stop      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    refPeopleCountDevice:      
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
      description: 'Reference to the [Device](https://github.com/Fiware/dataModels/blob/master/specs/Device/Device/doc/spec.md) providing people count estimate'      
      type: string      
      x-ngsi:      
        type: Property      
    refPublicTransportRoute:      
      description: Public transport routes using this stop      
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
      minItems: 1      
      type: array      
      uniqueItems: true      
      x-ngsi:      
        model: ' https://schema.org/URL'      
        type: Relationship      
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
    shortStopCode:      
      description: Shorter form of the identifier/code of the public transport stop      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    stopCode:      
      description: Identifier/code of the public transport stop      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
      description: NGSI Entity type. It has to be PublicTransportStop      
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
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/PublicTransportStop/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/PublicTransportStop/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### PublicTransportStop Valori chiave NGSI-v2 Esempio    
Ecco un esempio di un PublicTransportStop in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
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
</details>    
#### PublicTransportStop NGSI-v2 normalizzato Esempio    
Ecco un esempio di un PublicTransportStop in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportStop:santander:busStop:463",  
  "type": "PublicTransportStop",  
  "dateModified": {  
    "type": "DateTime",  
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
    "type": "Boolean",  
    "value": false  
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
    "type": "Boolean",  
    "value": false  
  },  
  "refPeopleCountDevice": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PorpleCountDecice:santander:463"  
  },  
  "openingHoursSpecification": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "opens": "00:01",  
        "closes": "23:59",  
        "dayOfWeek": "Friday"  
      },  
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
        "dayOfWeek": "Thursday"  
      },  
      {  
        "opens": "00:01",  
        "closes": "23:59",  
        "dayOfWeek": "Wednesday"  
      }  
    ]  
  }  
}  
```  
</details>    
#### PublicTransportStop Valori chiave NGSI-LD Esempio    
Ecco un esempio di un PublicTransportStop in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportStop:santander:busStop:463",  
  "type": "PublicTransportStop",  
  "address": {  
    "streetAddress": "C/ La Pereda 14",  
    "addressLocality": "Santander",  
    "addressRegion": "Cantabria",  
    "addressCountry": "Spain"  
  },  
  "dataProvider": "http://www.smartsantander.eu/",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.804648385,  
      43.478053126  
    ]  
  },  
  "name": "La Pereda 14",  
  "openingHoursSpecification": [  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Friday"  
    },  
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
      "dayOfWeek": "Thursday"  
    },  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Wednesday"  
    }  
  ],  
  "peopleCount": 0,  
  "refPeopleCountDevice": "urn:ngsi-ld:PorpleCountDecice:santander:463",  
  "refPublicTransportRoute": [  
    "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
    "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N4"  
  ],  
  "shortStopCode": "463",  
  "source": "https://api.smartsantander.eu/",  
  "stopCode": "la_pereda_463",  
  "transportationType": [  
    3  
  ],  
  "wheelchairAccessible": 0,  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### PublicTransportStop Esempio normalizzato NGSI-LD    
Ecco un esempio di un PublicTransportStop in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportStop:santander:busStop:463",  
  "type": "PublicTransportStop",  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "C/ La Pereda 14",  
      "addressLocality": "Santander",  
      "addressRegion": "Cantabria",  
      "addressCountry": "Spain"  
    }  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "http://www.smartsantander.eu/"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2018-09-25T08:32:26.00Z"  
  },  
  "entityVersion": {  
    "type": "Property",  
    "value": 2.0  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.804648385,  
        43.478053126  
      ]  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "La Pereda 14"  
  },  
  "openingHoursSpecification": {  
    "type": "Property",  
    "value": [  
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
  },  
  "peopleCount": {  
    "type": "Property",  
    "value": 0  
  },  
  "refPeopleCountDevice": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PorpleCountDecice:santander:463"  
  },  
  "refPublicTransportRoute": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
      "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N4"  
    ]  
  },  
  "shortStopCode": {  
    "type": "Property",  
    "value": "463"  
  },  
  "source": {  
    "type": "Property",  
    "value": "https://api.smartsantander.eu/"  
  },  
  "stopCode": {  
    "type": "Property",  
    "value": "la_pereda_463"  
  },  
  "transportationType": {  
    "type": "Property",  
    "value": [  
      3  
    ]  
  },  
  "wheelchairAccessible": {  
    "type": "Property",  
    "value": 0  
  },  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
