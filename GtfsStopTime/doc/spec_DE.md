[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: GtfsStopTime  
=====================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsStopTime/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **GTFS-Stoppzeit**  
Version: 0.0.2  

## Liste der Eigenschaften  

- `alternateName`: Ein alternativer Name für diesen Artikel  - `arrivalTime`: Gleich wie GTFS "Ankunftszeit  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `departureTime`: Gleich wie GTFS "Abflugzeit  - `description`: Eine Beschreibung dieses Artikels  - `distanceTravelled`: Gleich wie GTFS `shape_dist_traveled`  - `dropOffType`: Gleich wie GTFS `drop_off_type`. Enum:'0, 1, 2, 3'  - `hasStop`: Entspricht der GTFS-"stop_id". Sie muss auf eine Entität des Typs GtfsStop zeigen.  - `hasTrip`: Reise, die mit dieser Entität verbunden ist. Sie muss auf eine Entität des Typs GtfsTrip zeigen.  - `id`: Eindeutiger Bezeichner der Entität  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pickupType`: Gleich wie GTFS `pickup_type`. Enum:'0, 1, 2, 3'  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `stopHeadsign`: Gleich wie GTFS "stop_headsign  - `stopSequence`: Dasselbe wie GTFS "stop_sequence". Beginnend mit "1".  - `timepoint`: Dasselbe wie GTFS "timepoint". Enum:'0, 1'  - `type`: NGSI-Entitätstyp. Es muss GtfsStopTime sein    
Erforderliche Eigenschaften  
- `arrivalTime`  - `departureTime`  - `hasStop`  - `hasTrip`  - `id`  - `stopSequence`  - `type`    
Siehe [https://developers.google.com/transit/gtfs/reference/#stop_timestxt](https://developers.google.com/transit/gtfs/reference/#stop_timestxt)  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsStopTime:    
  description: 'GTFS Stop Time'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    arrivalTime:    
      description: 'Same as GTFS `arrival_time`'    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
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
    departureTime:    
      description: 'Same as GTFS `departure_time`'    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    distanceTravelled:    
      description: 'Same as GTFS `shape_dist_traveled`'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dropOffType:    
      default: 0    
      description: 'Same as GTFS `drop_off_type`. Enum:''0, 1, 2, 3'''    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
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
        anyOf: *gtfsstoptime_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pickupType:    
      default: 0    
      description: 'Same as GTFS `pickup_type`. Enum:''0, 1, 2, 3'' '    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    stopHeadsign:    
      description: 'Same as GTFS `stop_headsign`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
        type: Property    
    stopSequence:    
      description: 'Same as GTFS `stop_sequence`. Starting with `1`.'    
      minimum: 1    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Integer    
        type: Property    
    timepoint:    
      default: 1    
      description: 'Same as GTFS `timepoint`. Enum:''0, 1'''    
      enum:    
        - 0    
        - 1    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be GtfsStopTime'    
      enum:    
        - GtfsStopTime    
      type: string    
      x-ngsi:    
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsStopTime/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/GtfsStopTime/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
## Beispiel-Nutzlasten  
#### GtfsStopTime NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine GtfsStopTime im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### GtfsStopTime NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine GtfsStopTime im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### GtfsStopTime NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine GtfsStopTime im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
    "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
    "type": "GtfsStopTime",  
    "arrivalTime": {  
        "type": "Property",  
        "value": "07:04:24"  
    },  
    "departureTime": {  
        "type": "Property",  
        "value": "07:04:24"  
    },  
    "distanceTravelled": {  
        "type": "Property",  
        "value": 759  
    },  
    "hasStop": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737"  
    },  
    "hasTrip": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011"  
    },  
    "stopSequence": {  
        "type": "Property",  
        "value": 4  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
#### GtfsStopTime NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine GtfsStopTime im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
    "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
    "type": "GtfsStopTime",  
    "arrivalTime": "07:04:24",  
    "departureTime": "07:04:24",  
    "distanceTravelled": 759,  
    "hasStop": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737",  
    "hasTrip": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011",  
    "stopSequence": 4,  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
