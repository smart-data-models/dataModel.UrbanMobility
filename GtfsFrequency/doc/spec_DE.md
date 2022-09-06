[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: GtfsFrequency  
======================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsFrequency/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **GTFS-Frequenz**  
Version: 0.0.2  

## Liste der Eigenschaften  

- `alternateName`: Ein alternativer Name für diesen Artikel  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `endTime`: Gleich wie GTFS `end_time`  - `exactTimes`: Wie GTFS `exact_times`, aber kodiert als Boolean; `false`: Frequenzabhängige Fahrten werden nicht exakt geplant. wahr": Frequenzabhängige Fahrten werden genau geplant.  - `hasTrip`: Reise, die mit dieser Entität verbunden ist. Sie muss auf eine Entität des Typs GtfsTrip zeigen.  - `headwaySeconds`: Gleich wie GTFS "headway_secs  - `id`: Eindeutiger Bezeichner der Entität  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `startTime`: Wie GTFS "start_time  - `type`: NGSI-Entitätstyp. Es muss GtfsFrequency sein    
Erforderliche Eigenschaften  
- `endTime`  - `hasTrip`  - `headwaySeconds`  - `id`  - `startTime`  - `type`    
Siehe [https://developers.google.com/transit/gtfs/reference/#frequenciestxt](https://developers.google.com/transit/gtfs/reference/#frequenciestxt)  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsFrequency:    
  description: 'GTFS Frequency'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
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
    endTime:    
      description: 'Same as GTFS `end_time`'    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    exactTimes:    
      description: 'Same as GTFS `exact_times` but encoded as a Boolean; `false`: Frequency-based trips are not exactly scheduled. `true`: Frequency-based trips are exactly scheduled'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
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
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    headwaySeconds:    
      description: 'Same as GTFS `headway_secs`'    
      minimum: 1    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &gtfsfrequency_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfsfrequency_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    startTime:    
      description: 'Same as GTFS `start_time`'    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be GtfsFrequency'    
      enum:    
        - GtfsFrequency    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - hasTrip    
    - startTime    
    - endTime    
    - headwaySeconds    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsFrequency/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/GtfsFrequency/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
## Beispiel-Nutzlasten  
#### GtfsFrequency NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine GtfsFrequency im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
  "type": "GtfsFrequency",  
  "name": "Laborables",  
  "description": "Cada 10 minutos",  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
  "startTime": "07:00:00",  
  "endTime": "10:25:00",  
  "headwaySeconds": 600  
}  
```  
#### GtfsFrequency NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine GtfsFrequency im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
  "type": "GtfsFrequency",  
  "description": {  
    "value": "Cada 10 minutos"  
  },  
  "hasTrip": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1"  
  },  
  "headwaySeconds": {  
    "value": 600  
  },  
  "startTime": {  
    "value": "07:00:00"  
  },  
  "endTime": {  
    "value": "10:25:00"  
  },  
  "name": {  
    "value": "Laborables"  
  }  
}  
```  
#### GtfsFrequency NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine GtfsFrequency im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
    "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
    "type": "GtfsFrequency",  
    "description": {  
        "type": "Property",  
        "value": "Cada 10 minutos"  
    },  
    "endTime": {  
        "type": "Property",  
        "value": "10:25:00"  
    },  
    "hasTrip": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1"  
    },  
    "headwaySeconds": {  
        "type": "Property",  
        "value": 600  
    },  
    "name": {  
        "type": "Property",  
        "value": "Laborables"  
    },  
    "startTime": {  
        "type": "Property",  
        "value": "07:00:00"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
#### GtfsFrequency NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine GtfsFrequency im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
    "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
    "type": "GtfsFrequency",  
    "description": "Cada 10 minutos",  
    "endTime": "10:25:00",  
    "hasTrip": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
    "headwaySeconds": 600,  
    "name": "Laborables",  
    "startTime": "07:00:00",  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
