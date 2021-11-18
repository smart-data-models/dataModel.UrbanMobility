Entität: GtfsShape  
==================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsShape/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **GTFS Form**  

## Liste der Eigenschaften  

- `alternateName`: Ein alternativer Name für diesen Artikel  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `distanceTravelled`: Ein Array mit der Entfernung, die zurückgelegt wurde, um jeden der Punkte zu erreichen, die den `LineString` oder `MultiLineString` bilden, der diese Form repräsentiert. Es muss die gleiche Anzahl von Elementen enthalten wie der entsprechende "LineString" oder "MultiLineString".  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Die mit dieser Entität verbundene geografische Form, kodiert als GeoJSON `LineString` oder `MultiLineString`. Die Koordinaten werden aus der Feed-Datei "shapes.txt" entsprechend dem Wert von "shape_id", "shape_pt_lat", "shape_pt_lon" und "shape_pt_sequence" gewonnen.  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type`: NGSI-Entitätstyp. Es muss GtfsShape sein    
Erforderliche Eigenschaften  
- `id`  - `location`  - `type`    
Siehe [https://developers.google.com/transit/gtfs/reference/#shapestxt](https://developers.google.com/transit/gtfs/reference/#shapestxt). Es stellt eine GTFS-Form dar.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsShape:    
  description: 'GTFS Shape'    
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
    distanceTravelled:    
      description: 'An array of the distance travelled when reaching each of the points that make the `LineString` or `MultiLineString` that represents this shape. It shall match the same number of elements as the corresponding `LineString` or `MultiLineString`.'    
      items:    
        minimum: 0    
        type: number    
      minItems: 1    
      type: array    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &gtfsshape_-_properties_-_owner_-_items_-_anyof    
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
      description: 'The geographical shape associated to this entity encoded as GeoJSON `LineString` or `MultiLineString`. The coordinates shall be obtained from the `shapes.txt` feed file as per the value of `shape_id`, `shape_pt_lat`, `shape_pt_lon`, `shape_pt_sequence`.'    
      oneOf:    
        - $id: https://geojson.org/schema/LineString.json    
          $schema: "http://json-schema.org/draft-07/schema#"    
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
        - $id: https://geojson.org/schema/MultiLineString.json    
          $schema: "http://json-schema.org/draft-07/schema#"    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfsshape_-_properties_-_owner_-_items_-_anyof    
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
    type:    
      description: 'NGSI Entity type. It has to be GtfsShape'    
      enum:    
        - GtfsShape    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### GtfsShape NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen GtfsShape im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsShape:101",  
  "type": "GtfsShape",  
  "location": {  
    "type": "LineString",  
    "coordinates": [  
      [-4.421394, 36.73826],  
      [-4.421428, 36.73825],  
      [-4.421505, 36.738186],  
      [-4.421525, 36.738033]  
    ]  
  }  
}  
```  
#### GtfsShape NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen GtfsShape im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsShape:101",  
  "type": "GtfsShape",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "LineString",  
      "coordinates": [  
        [-4.421394, 36.73826],  
        [-4.421428, 36.73825],  
        [-4.421505, 36.738186],  
        [-4.421525, 36.738033]  
      ]  
    }  
  }  
}  
```  
#### GtfsShape NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen GtfsShape im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsShape:101",  
  "type": "GtfsShape",  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "LineString",  
      "coordinates": [  
        [  
          -4.421394,  
          36.73826  
        ],  
        [  
          -4.421428,  
          36.73825  
        ],  
        [  
          -4.421505,  
          36.738186  
        ],  
        [  
          -4.421525,  
          36.738033  
        ]  
      ]  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### GtfsShape NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen GtfsShape im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:GtfsShape:101",  
  "location": {  
    "coordinates": [  
      [  
        -4.421394,  
        36.73826  
      ],  
      [  
        -4.421428,  
        36.73825  
      ],  
      [  
        -4.421505,  
        36.738186  
      ],  
      [  
        -4.421525,  
        36.738033  
      ]  
    ],  
    "type": "LineString"  
  },  
  "type": "GtfsShape"  
}  
```  
