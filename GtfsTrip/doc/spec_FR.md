Entité : GtfsTrip  
=================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsTrip/LICENSE.md)  
Description globale : **Voyage GTFS**  

## Liste des biens  

- `alternateName`: Un autre nom pour cet article  - `bikesAllowed`: Même chose que GTFS `bikes_allowed`. Enumération : "0, 1, 2". Voir [GTFS](https://developers.google.com/transit/gtfs/reference/#tripstxt)  - `block`: Même chose que GTFS `block_id`.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `direction`: Même chose que GTFS `direction_id`. Enum : '0, 1'.  - `hasRoute`: Même chose que `route_id`. Il doit pointer vers une entité de type GtfsRoute  - `hasService`: Même chose que le GTFS `service_id`. Il doit pointer vers une entité de type GtfsService  - `hasShape`: Même chose que GTFS `shape_id`. Il doit pointer vers une entité de type GtfsShape  - `headSign`: Identique à GTFS `trip_headsign`.  - `id`: Identifiant unique de l'entité  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `shortName`: Même chose que GTFS `trip_short_name`.  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type d'entité NGSI. Il doit s'agir de GtfsTrip  - `wheelChairAccessible`: Même chose que pour GTFS "accessible aux fauteuils roulants". Enumération : "0, 1, 2    
Propriétés requises  
- `hasRoute`  - `hasService`  - `id`  - `type`    
Voir [https://developers.google.com/transit/gtfs/reference/#tripstxt](https://developers.google.com/transit/gtfs/reference/#tripstxt)  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsTrip:    
  description: 'GTFS Trip'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    bikesAllowed:    
      description: "Same as GTFS `bikes_allowed`. Enum:'0, 1, 2'. See [GTFS](https://developers.google.com/transit/gtfs/reference/#tripstxt)"    
      enum:    
        - 0    
        - 1    
        - 2    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    block:    
      description: 'Same as GTFS `block_id`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
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
    direction:    
      description: 'Same as GTFS `direction_id`. Enum:''0, 1'''    
      enum:    
        - 0    
        - 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    hasRoute:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Same as `route_id`. It shall point to an Entity of type GtfsRoute'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    hasService:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Same as GTFS `service_id`. It shall point to an Entity of type GtfsService'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    hasShape:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Same as GTFS `shape_id`. It shall point to an Entity of type GtfsShape'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    headSign:    
      description: 'Same as GTFS `trip_headsign`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
    id:    
      anyOf: &gtfstrip_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *gtfstrip_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
    shortName:    
      description: 'Same as GTFS `trip_short_name`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be GtfsTrip'    
      enum:    
        - GtfsTrip    
      type: Property    
    wheelChairAccessible:    
      description: 'Same as GTFS `wheelchair_accessible`. Enum:''0, 1, 2'''    
      enum:    
        - 0    
        - 1    
        - 2    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
  required:    
    - id    
    - type    
    - hasRoute    
    - hasService    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### GtfsTrip NGSI V2 valeurs clés Exemple  
Voici un exemple de GtfsTrip au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
  "type": "GtfsTrip",  
  "hasService": "urn:ngsi-ld:GtfsService:Malaga_LAB",  
  "headSign": "San Andrés",  
  "direction": 0,  
  "hasRoute": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
  "hasShape": "urn:ngsi-ld:GtfsShape:Shape01"  
}  
```  
#### GtfsTrip NGSI V2 normalisé Exemple  
Voici un exemple de GtfsTrip au format JSON tel que normalisé. Ce format est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
  "type": "GtfsTrip",  
  "direction": {  
    "value": 0  
  },  
  "headSign": {  
    "value": "San Andr\u00e9s"  
  },  
  "hasRoute": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1"  
  },  
  "hasService": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsService:Malaga_LAB"  
  },  
  "hasShape": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsShape:Shape01"  
  }  
}  
```  
#### GtfsTrip NGSI-LD valeurs clés Exemple  
Voici un exemple de GtfsTrip au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "direction": 0,  
 "hasRoute": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
 "hasService": "urn:ngsi-ld:GtfsService:Malaga_LAB",  
 "hasShape": "urn:ngsi-ld:GtfsShape:Shape01",  
 "headSign": "San AndrÃ©s",  
 "id": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
 "type": "GtfsTrip"}  
```  
#### GtfsTrip NGSI-LD normalisé Exemple  
Voici un exemple de GtfsTrip au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
    "type": "GtfsTrip",  
    "direction": {  
        "type": "Property",  
        "value": 0  
    },  
    "headSign": {  
        "type": "Property",  
        "value": "San AndrÃ©s"  
    },  
    "hasRoute": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1"  
    },  
    "hasService": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsService:Malaga_LAB"  
    },  
    "hasShape": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsShape:Shape01"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
