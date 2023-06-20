<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : GtfsTrip  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsTrip/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **GTFS Trip**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `alternateName[string]`: Un nom alternatif pour ce poste  - `bikesAllowed[number]`: Identique à GTFS `bikes_allowed`. Enum : '0, 1, 2'. Voir [GTFS](https://developers.google.com/transit/gtfs/reference/#tripstxt)  . Model: [https://schema.org/Number](https://schema.org/Number)- `block[string]`: Identique à GTFS `block_id`  . Model: [https://schema.org/Text.](https://schema.org/Text.)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Date de création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage.  - `dateModified[string]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage.  - `description[string]`: Une description de l'article  - `direction[number]`: Identique à GTFS `direction_id`. Enum : '0, 1'  . Model: [https://schema.org/Number](https://schema.org/Number)- `hasRoute[string]`: Identique à `route_id`. Il doit pointer vers une entité de type GtfsRoute  . Model: [http://schema.org/URL](http://schema.org/URL)- `hasService[*]`: Identique à GTFS `service_id`. Il doit pointer vers une entité de type GtfsService  . Model: [http://schema.org/URL](http://schema.org/URL)- `hasShape[*]`: Identique à GTFS `shape_id`. Il doit pointer vers une entité de type GtfsShape  . Model: [http://schema.org/URL](http://schema.org/URL)- `headSign[string]`: Identique à GTFS `trip_headsign` (signe de tête du voyage)  . Model: [https://schema.org/Text.](https://schema.org/Text.)- `id[*]`: Identifiant unique de l'entité  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `shortName[string]`: Identique au GTFS `trip_short_name` (nom court du voyage)  . Model: [https://schema.org/Text.](https://schema.org/Text.)- `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type d'entité NGSI. Il doit s'agir de GtfsTrip  - `wheelChairAccessible[number]`: Identique à GTFS `wheelchair_accessible`. Enum : '0, 1, 2'  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `hasRoute`  - `hasService`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Voir [https://developers.google.com/transit/gtfs/reference/#tripstxt](https://developers.google.com/transit/gtfs/reference/#tripstxt)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsTrip:    
  description: GTFS Trip    
  properties:    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    bikesAllowed:    
      description: "Same as GTFS `bikes_allowed`. Enum:'0, 1, 2'. See [GTFS](https://developers.google.com/transit/gtfs/reference/#tripstxt)"    
      enum:    
        - 0    
        - 1    
        - 2    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    block:    
      description: Same as GTFS `block_id`    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    direction:    
      description: 'Same as GTFS `direction_id`. Enum:''0, 1'''    
      enum:    
        - 0    
        - 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    hasRoute:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Same as `route_id`. It shall point to an Entity of type GtfsRoute    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    hasService:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Same as GTFS `service_id`. It shall point to an Entity of type GtfsService    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    hasShape:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Same as GTFS `shape_id`. It shall point to an Entity of type GtfsShape    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    headSign:    
      description: Same as GTFS `trip_headsign`    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
        type: Property    
    id:    
      anyOf: &gtfstrip_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *gtfstrip_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
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
    shortName:    
      description: Same as GTFS `trip_short_name`    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be GtfsTrip    
      enum:    
        - GtfsTrip    
      type: string    
      x-ngsi:    
        type: Property    
    wheelChairAccessible:    
      description: 'Same as GTFS `wheelchair_accessible`. Enum:''0, 1, 2'''    
      enum:    
        - 0    
        - 1    
        - 2    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
    - hasRoute    
    - hasService    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsTrip/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/GtfsTrip/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### GtfsTrip NGSI-v2 key-values Exemple  
Voici un exemple de GtfsTrip au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### GtfsTrip NGSI-v2 normalisé Exemple  
Voici un exemple de GtfsTrip au format JSON-LD tel que normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
  "type": "GtfsTrip",  
  "direction": {  
     "type": "Number",  
    "value": 0  
  },  
  "headSign": {  
    "type": "Text",  
    "value": "San Andr\u00e9s"  
  },  
  "hasRoute": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1"  
  },  
  "hasService": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:GtfsService:Malaga_LAB"  
  },  
  "hasShape": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:GtfsShape:Shape01"  
  }  
}  
```  
</details>  
#### GtfsTrip Valeurs clés NGSI-LD Exemple  
Voici un exemple de GtfsTrip au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
    "type": "GtfsTrip",  
    "direction": 0,  
    "hasRoute": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
    "hasService": "urn:ngsi-ld:GtfsService:Malaga_LAB",  
    "hasShape": "urn:ngsi-ld:GtfsShape:Shape01",  
    "headSign": "San Andr\u00e9s",  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### GtfsTrip NGSI-LD normalisé Exemple  
Voici un exemple de GtfsTrip au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
    "type": "GtfsTrip",  
    "direction": {  
        "type": "Property",  
        "value": 0  
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
    "headSign": {  
        "type": "Property",  
        "value": "San Andr\u00e9s"  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
