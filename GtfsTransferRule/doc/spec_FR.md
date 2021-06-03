Entité : GtfsTransferRule  
=========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsTransferRule/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Règle de transfert GTFS**  

## Liste des propriétés  

- `alternateName`: Un nom alternatif pour cet élément  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `hasDestination`: Voyage associé à cette Entité. Il doit pointer vers une Entité de type GtfsStop ou GtfsStation.  - `hasOrigin`: Voyage associé à cette Entité. Il doit pointer vers une Entité de type GtfsStop ou GtfsStation.  - `id`: Identifiant unique de l'entité  - `minimumTransferTime`: Identique au `min_transfer_time` de GTFS. Unité : 'secondes'.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `transferType`: Identique à GTFS `transfer_type`. Enum : "0, 1, 2, 3".  - `type`: Type d'entité NGSI. Il doit être GtfsTransferRule.    
Propriétés requises  
- `hasDestination`  - `hasOrigin`  - `id`  - `transferType`  - `type`    
Voir [https://developers.google.com/transit/gtfs/reference/#transferstxt](https://developers.google.com/transit/gtfs/reference/#transferstxt)  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsTransferRule:    
  description: 'GTFS Transfer Rule'    
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
    hasDestination:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Trip associated to this Entity. It shall point to an Entity of type GtfsStop or GtfsStation'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    hasOrigin:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Trip associated to this Entity. It shall point to an Entity of type GtfsStop or GtfsStation'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    id:    
      anyOf: &gtfstransferrule_-_properties_-_owner_-_items_-_anyof    
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
    minimumTransferTime:    
      description: 'Same as GTFS `min_transfer_time`. Unit:''seconds'''    
      minValue: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Integer    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfstransferrule_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    transferType:    
      description: 'Same as GTFS `transfer_type`. Enum:''0, 1, 2, 3'''    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI Entity type. It has to be GtfsTransferRule'    
      enum:    
        - GtfsTransferRule    
      type: Property    
  required:    
    - id    
    - type    
    - hasOrigin    
    - hasDestination    
    - transferType    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### GtfsTransferRule Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de GtfsTransferRule au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsTransferRule:Malaga:Linea1_Linea5",  
  "type": "GtfsTransferRule",  
  "name": "L1_L5",  
  "hasOrigin": "urn:ngsi-ld:GtfsStop:Malaga_101",  
  "hasDestination": "urn:ngsi-ld:GtfsStop:Malaga_508",  
  "transferType": "0",  
  "minimumTransferTime": 10  
}  
```  
#### GtfsTransferRule NGSI-v2 normalisée Exemple  
Voici un exemple de GtfsTransferRule au format JSON-LD tel que normalisé. Cette règle est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsTransferRule:Malaga:Linea1_Linea5",  
  "type": "GtfsTransferRule",  
  "transferType": {  
    "value": "0"  
  },  
  "minimumTransferTime": {  
    "value": 10  
  },  
  "hasDestination": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsStop:Malaga_508"  
  },  
  "hasOrigin": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsStop:Malaga_101"  
  },  
  "name": {  
    "value": "L1_L5"  
  }  
}  
```  
#### GtfsTransferRule Valeurs-clés NGSI-LD Exemple  
Voici un exemple de GtfsTransferRule au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsTransferRule:Malaga:Linea1_Linea5",  
  "type": "GtfsTransferRule",  
  "transferType": {  
    "type": "Property",  
    "value": "0"  
  },  
  "minimumTransferTime": {  
    "type": "Property",  
    "value": 10  
  },  
  "hasDestination": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:GtfsStop:Malaga_508"  
  },  
  "hasOrigin": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:GtfsStop:Malaga_101"  
  },  
  "name": {  
    "type": "Property",  
    "value": "L1_L5"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### GtfsTransferRule NGSI-LD normalisé Exemple  
Voici un exemple de GtfsTransferRule au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "hasDestination": "urn:ngsi-ld:GtfsStop:Malaga_508",  
  "hasOrigin": "urn:ngsi-ld:GtfsStop:Malaga_101",  
  "id": "urn:ngsi-ld:GtfsTransferRule:Malaga:Linea1_Linea5",  
  "minimumTransferTime": 10,  
  "name": "L1_L5",  
  "transferType": "0",  
  "type": "GtfsTransferRule"  
}  
```  
