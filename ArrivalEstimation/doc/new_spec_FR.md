Entité : ArrivéeEstimation  
==========================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Estimation à l'arrivée  

## Liste des biens  

- `alternateName`: Un autre nom pour cet article  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `hasStop`:   - `hasTrip`:   - `headsign`:   - `id`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `remainingDistance`:   - `remainingTime`:   - `seeAlso`:   - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: NGSI Type d'entité  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
      format: uri    
      type: string    
    hasTrip:    
      format: uri    
      type: string    
    headsign:    
      type: string    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *arrivalestimation_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    remainingDistance:    
      minValue: 0    
      type: number    
    remainingTime:    
      pattern: ^P(?=\w*\d)(?:\d+Y|Y)?(?:\d+M|M)?(?:\d+W|W)?(?:\d+D|D)?(?:T(?:\d+H|H)?(?:\d+M|M)?(?:\d+(?:\?.\d{1,2})?S|S)?)?$    
      type: string    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - ArrivalEstimation    
      type: string    
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
## Exemples de charges utiles  
#### ArrivalEstimation NGSI V2 key-values Exemple  
Voici un exemple d'une ArrivalEstimation au format JSON comme valeurs clés. Ce format est compatible avec la version 2 de l'INSG lorsqu'il utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
  "type": "ArrivalEstimation",  
  "hasStop": "urn:ngsi-ld:GtfsStop:tus:74",  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:tus:5C1",  
  "remainingTime": "PT8M5S",  
  "remainingDistance": 1200,  
  "headSign": "Plaza Italia"  
}  
```  
#### ArrivalEstimation NGSI V2 normalisé Exemple  
Voici un exemple d'une ArrivalEstimation au format JSON tel que normalisé. Ce format est compatible avec la version 2 de l'INSG lorsqu'il utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
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
#### ArrivalEstimation NGSI-LD key-values Example  
Voici un exemple d'une ArrivalEstimation au format JSON-LD comme valeurs clés. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "hasStop": "urn:ngsi-ld:GtfsStop:tus:74",  
 "hasTrip": "urn:ngsi-ld:GtfsTrip:tus:5C1",  
 "headSign": "Plaza Italia",  
 "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
 "remainingDistance": 1200,  
 "remainingTime": "PT8M5S",  
 "type": "ArrivalEstimation"}  
```  
#### ArrivalEstimation NGSI-LD normalisé Exemple  
Voici un exemple d'une ArrivalEstimation au format JSON-LD normalisé. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
