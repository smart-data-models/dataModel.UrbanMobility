Entité : GtfsStopTime  
=====================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsStopTime/LICENSE.md)  
Description globale : **GTFS Stop Time**  

## Liste des biens  

- `alternateName`: Un autre nom pour cet article  - `arrivalTime`: Même chose que GTFS `arrival_time`.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `departureTime`: Même chose que GTFS `departure_time`.  - `description`: Une description de cet article  - `distanceTravelled`: Même chose que GTFS `shape_dist_traveled`.  - `dropOffType`: Même chose que le GTFS `drop_off_type`. Enum : "0, 1, 2, 3  - `hasStop`: Même chose que GTFS `stop_id`. Il doit pointer vers une entité de type GtfsStop  - `hasTrip`: Voyage associé à cette entité. Il doit pointer vers une entité de type GtfsTrip  - `id`: Identifiant unique de l'entité  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `pickupType`: Même chose que le GTFS `pickup_type`. Enum : "0, 1, 2, 3  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `stopHeadsign`: Identique à GTFS `stop_headsign`.  - `stopSequence`: Même chose que GTFS `stop_sequence`. Commençant par `1`.  - `timepoint`: Même chose que le "timepoint" de GTFS. Enum : "0, 1  - `type`: Type d'entité NGSI. Il doit s'agir de GtfsStopTime    
Propriétés requises  
- `arrivalTime`  - `departureTime`  - `hasStop`  - `hasTrip`  - `id`  - `stopSequence`  - `type`    
Voir [https://developers.google.com/transit/gtfs/reference/#stop_timestxt](https://developers.google.com/transit/gtfs/reference/#stop_timestxt)  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsStopTime:    
  description: 'GTFS Stop Time'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    arrivalTime:    
      description: 'Same as GTFS `arrival_time`'    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
    departureTime:    
      description: 'Same as GTFS `departure_time`'    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    description:    
      description: 'A description of this item'    
      type: Property    
    distanceTravelled:    
      description: 'Same as GTFS `shape_dist_traveled`'    
      minValue: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    dropOffType:    
      default: 0    
      description: 'Same as GTFS `drop_off_type`. Enum:''0, 1, 2, 3'''    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
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
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfsstoptime_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pickupType:    
      default: 0    
      description: 'Same as GTFS `pickup_type`. Enum:''0, 1, 2, 3'' '    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    stopHeadsign:    
      description: 'Same as GTFS `stop_headsign`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
    stopSequence:    
      description: 'Same as GTFS `stop_sequence`. Starting with `1`.'    
      minValue: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Integer    
    timepoint:    
      default: 1    
      description: 'Same as GTFS `timepoint`. Enum:''0, 1'''    
      enum:    
        - 0    
        - 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI Entity type. It has to be GtfsStopTime'    
      enum:    
        - GtfsStopTime    
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
```  
</details>    
## Exemples de charges utiles  
#### GtfsStopTime NGSI V2 Exemple de valeurs clés  
Voici un exemple de GtfsStopTime au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### GtfsStopTime NGSI V2 normalisé Exemple  
Voici un exemple de GtfsStopTime au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### GtfsStopTime NGSI-LD valeurs clés Exemple  
Voici un exemple de GtfsStopTime au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "arrivalTime": "07:04:24",  
 "departureTime": "07:04:24",  
 "distanceTravelled": 759,  
 "hasStop": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737",  
 "hasTrip": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011",  
 "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
 "stopSequence": 4,  
 "type": "GtfsStopTime"}  
```  
#### GtfsStopTime NGSI-LD normalisé Exemple  
Voici un exemple de GtfsStopTime au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
    "type": "GtfsStopTime",  
    "departureTime": {  
        "type": "Property",  
        "value": "07:04:24"  
    },  
    "hasTrip": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011"  
    },  
    "stopSequence": {  
        "type": "Property",  
        "value": 4  
    },  
    "distanceTravelled": {  
        "type": "Property",  
        "value": 759  
    },  
    "arrivalTime": {  
        "type": "Property",  
        "value": "07:04:24"  
    },  
    "hasStop": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
