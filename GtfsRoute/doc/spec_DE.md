Entität: GtfsRoute  
==================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsRoute/LICENSE.md)  
Globale Beschreibung: **GTFS-Route**  

## Liste der Eigenschaften  

- `alternateName`: Ein alternativer Name für diesen Artikel  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `name`: Der Name dieses Elements.  - `operatedBy`: Agentur, die diese Route betreibt. Sie muss auf eine Entität des Typs GtfsAgency verweisen  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `page`: Gleich wie GTFS `stop_url`  - `routeColor`: Dasselbe wie GTFS `route_color`. Siehe [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)  - `routeSortOrder`: Gleich wie GTFS `route_sort_order`  - `routeTextColor`: Dasselbe wie GTFS `route_text_color`. Siehe [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)  - `routeType`: Wie GTFS `route_type`. Erlaubte Werte sind die für `route_type` erlaubten, wie von [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt) vorgeschrieben. Enum:'0, 1, 2, 3, 4, 5, 6, 7'  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `shortName`: Gleich wie GTFS `route_short_name`  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `type`: NGSI Entity-Typ. Es muss GtfsRoute sein    
Erforderliche Eigenschaften  
- `id`  - `type`    
Siehe [https://developers.google.com/transit/gtfs/reference/#routestxt](https://developers.google.com/transit/gtfs/reference/#routestxt)  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsRoute:    
  description: 'GTFS Route'    
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
    id:    
      anyOf: &gtfsroute_-_properties_-_owner_-_items_-_anyof    
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
    operatedBy:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Agency that operates this route. It shall point to an Entity of Type GtfsAgency'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/Text    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfsroute_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    page:    
      description: 'Same as GTFS `stop_url`'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: http://schema.org/URL    
    routeColor:    
      description: "Same as GTFS `route_color`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)"    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    routeSortOrder:    
      description: 'Same as GTFS `route_sort_order`'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    routeTextColor:    
      description: "Same as GTFS `route_text_color`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)"    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    routeType:    
      description: "Same as GTFS `route_type`. allowed values those allowed for `route_type` as prescribed by [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt). Enum:'0, 1, 2, 3, 4, 5, 6, 7'"    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
    shortName:    
      description: 'Same as GTFS `route_short_name`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be GtfsRoute'    
      enum:    
        - GtfsRoute    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### GtfsRoute NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine GtfsRoute im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
  "type": "GtfsRoute",  
  "shortName": "1",  
  "name": "Parque del Sur _ Alameda Principal _ San Andrés",  
  "page": "http://www.emtmalaga.es/emt-mobile/informacionLinea.html",  
  "routeType": "3",  
  "operatedBy": "urn:ngsi-ld:GtfsAgency:Malaga_EMT"  
}  
```  
#### GtfsRoute NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine GtfsRoute im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
  "type": "GtfsRoute",  
  "name": {  
    "value": "Parque del Sur _ Alameda Principal _ San Andr\u00e9s"  
  },  
  "shortName": {  
    "value": "1"  
  },  
  "page": {  
    "value": "http://www.emtmalaga.es/emt-mobile/informacionLinea.html"  
  },  
  "routeType": {  
    "value": "3"  
  },  
  "operatedBy": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsAgency:Malaga_EMT"  
  }  
}  
```  
#### GtfsRoute NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine GtfsRoute im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
  "type": "GtfsRoute",  
  "name": {  
    "type": "Property",  
    "value": "Parque del Sur _ Alameda Principal _ San Andr\u00e9s"  
  },  
  "shortName": {  
    "type": "Property",  
    "value": "1"  
  },  
  "page": {  
    "type": "Property",  
    "value": "http://www.emtmalaga.es/emt-mobile/informacionLinea.html"  
  },  
  "routeType": {  
    "type": "Property",  
    "value": "3"  
  },  
  "operatedBy": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:GtfsAgency:Malaga_EMT"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### GtfsRoute NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine GtfsRoute im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
  "name": "Parque del Sur _ Alameda Principal _ San Andr\u00e9s",  
  "operatedBy": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
  "page": "http://www.emtmalaga.es/emt-mobile/informacionLinea.html",  
  "routeType": "3",  
  "shortName": "1",  
  "type": "GtfsRoute"  
}  
```  
