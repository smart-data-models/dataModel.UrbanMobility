Entität: AnkunftSchätzung  
=========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/ArrivalEstimation/LICENSE.md)  
Globale Beschreibung: **Ankunftseinschätzung**  

## Liste der Eigenschaften  

- `alternateName`: Ein alternativer Name für diesen Artikel  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `hasStop`: Es muss auf ein Entity vom Typ GtfsStop zeigen  - `hasTrip`: Trip, der zu diesem Entity gehört. Es muss auf ein Entity vom Typ GtfsTrip zeigen  - `headSign`: Es muss den Text enthalten, der auf einem Schild erscheint, das den Fahrgästen das Ziel der Fahrt anzeigt  - `id`: Eindeutiger Bezeichner der Entität  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `remainingDistance`: Sie muss die verbleibende Entfernung (in Metern) der Ankunft für die Fahrtrichtung zur betreffenden Haltestelle enthalten  - `remainingTime`: Sie muss die verbleibende Ankunftszeit für die Fahrt in Richtung der betreffenden Haltestelle enthalten. Die verbleibende Zeit muss als ISO8601-Dauer kodiert sein. Bsp. `PT8M5S`.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `type`: NGSI-Entitätstyp: Es muss ArrivalEstimation sein    
Erforderliche Eigenschaften  
- `hasStop`  - `hasTrip`  - `headSign`  - `id`  - `remainingTime`  - `type`    
Dieser Entitätstyp erfasst die geschätzte Ankunftszeit eines Fahrzeugs des öffentlichen Verkehrs, das eine bestimmte Haltestelle erreicht, während das Fahrzeug eine bestimmte Route bedient.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ArrivalEstimation:    
  description: 'Arrival Estimation'    
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
    hasStop:    
      description: 'It shall point to an Entity of Type GtfsStop'    
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
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    headSign:    
      description: 'It shall contain the text that appears on a sign that identifies the trip''s destination to passengers'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
    id:    
      anyOf: &arrivalestimation_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *arrivalestimation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    remainingDistance:    
      description: 'It shall contain the remaining distance (in meters) of arrival for the trip heading to the concerned stop'    
      minValue: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Meters    
    remainingTime:    
      description: 'It shall contain the remaining time of arrival for the trip heading to the concerned stop. Remaining time shall be encoded as a ISO8601 duration. Ex. `PT8M5S`.'    
      pattern: ^P(?=\w*\d)(?:\d+Y|Y)?(?:\d+M|M)?(?:\d+W|W)?(?:\d+D|D)?(?:T(?:\d+H|H)?(?:\d+M|M)?(?:\d+(?:\?.\d{1,2})?S|S)?)?$    
      type: Property    
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
    type:    
      description: 'NGSI Entity Type: It has to be ArrivalEstimation'    
      enum:    
        - ArrivalEstimation    
      type: Property    
  required:    
    - id    
    - type    
    - hasStop    
    - hasTrip    
    - remainingTime    
    - headSign    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### AnreiseSchätzung NGSI-v2-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine ArrivalEstimation im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
  "type": "ArrivalEstimation",  
  "hasStop": ["urn:ngsi-ld:GtfsStop:tus:74"],  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:tus:5C1",  
  "remainingTime": "PT8M5S",  
  "remainingDistance": 1200,  
  "headSign": "Plaza Italia"  
}  
```  
#### AnkunftSchätzung NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine ArrivalEstimation im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
  "type": "ArrivalEstimation",  
  "hasTrip": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsTrip:tus:5C1"  
  },  
  "headSign": {  
    "value": "Plaza Italia"  
  },  
  "remainingTime": {  
    "value": "PT8M5S"  
  },  
  "hasStop": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsStop:tus:74"  
  },  
  "remainingDistance": {  
    "value": 1200  
  }  
}  
```  
#### AnreiseSchätzung NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine ArrivalEstimation im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
  "type": "ArrivalEstimation",  
  "hasTrip": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:GtfsTrip:tus:5C1"  
  },  
  "headSign": {  
    "type": "Property",  
    "value": "Plaza Italia"  
  },  
  "remainingTime": {  
    "type": "Property",  
    "value": "PT8M5S"  
  },  
  "hasStop": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:GtfsStop:tus:74"  
  },  
  "remainingDistance": {  
    "type": "Property",  
    "value": 1200  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### AnkunftSchätzung NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine ArrivalEstimation im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "hasStop": "urn:ngsi-ld:GtfsStop:tus:74",  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:tus:5C1",  
  "headSign": "Plaza Italia",  
  "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
  "remainingDistance": 1200,  
  "remainingTime": "PT8M5S",  
  "type": "ArrivalEstimation"  
}  
```  
