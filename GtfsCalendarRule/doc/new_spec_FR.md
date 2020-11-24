Entité : GtfsCalendarRule  
=========================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Modèles de données intelligents. Règle du calendrier GTFS**  

## Liste des biens  

`alternateName`: Un autre nom pour cet article  `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  `description`: Une description de cet article  `endDate`:   `friday`:   `hasService`:   `id`:   `monday`:   `name`: Le nom de cet article.  `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  `saturday`:   `seeAlso`:   `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  `startDate`:   `sunday`:   `thursday`:   `tuesday`:   `type`: NGSI Type d'entité  `wednesday`:   ## Modèle de données description des biens  
Classement par ordre alphabétique  
```yaml  
GtfsCalendarRule:    
  description: 'Smart Data Models. GTFS Calendar Rule'    
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
    endDate:    
      format: date    
      type: string    
    friday:    
      type: boolean    
    hasService:    
      format: uri    
      type: string    
    id:    
      anyOf: &gtfscalendarrule_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    monday:    
      type: boolean    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfscalendarrule_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    saturday:    
      type: boolean    
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
    startDate:    
      format: date    
      type: string    
    sunday:    
      type: boolean    
    thursday:    
      type: boolean    
    tuesday:    
      type: boolean    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - GtfsCalendarRule    
      type: string    
    wednesday:    
      type: boolean    
  required:    
    - id    
    - type    
    - hasService    
    - monday    
    - tuesday    
    - wednesday    
    - thursday    
    - friday    
    - saturday    
    - sunday    
    - startDate    
    - endDate    
  type: object    
```  
Voici un exemple de GtfsCalendarRule au format JSON comme valeurs clés. Cette règle est compatible avec la version 2 du NGSI lorsqu'elle utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "type": "GtfsCalendarRule",  
  "name": "Rule Hospital Service 1",  
  "hasService": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1",  
  "monday": true,  
  "tuesday": true,  
  "wednesday": true,  
  "thursday": true,  
  "friday": true,  
  "saturday": false,  
  "sunday": false,  
  "startDate": "2018-01-01",  
  "endDate": "2019-01-01"  
}  
```  
Voici un exemple de règle d'agenda GtfsC en format JSON normalisé. Elle est compatible avec NGSI V2 lorsqu'elle utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "type": "GtfsCalendarRule",  
  "startDate": {  
    "type": "Date",  
    "value": "2018-01-01"  
  },  
  "endDate": {  
    "type": "Date",  
    "value": "2019-01-01"  
  },  
  "name": {  
    "value": "Rule Hospital Service 1"  
  },  
  "monday": {  
    "value": true  
  },  
  "tuesday": {  
    "value": true  
  },  
  "friday": {  
    "value": true  
  },  
  "wednesday": {  
    "value": true  
  },  
  "thursday": {  
    "value": true  
  },  
  "sunday": {  
    "value": false  
  },  
  "hasService": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1"  
  },  
  "saturday": {  
    "value": false  
  }  
}  
```  
Voici un exemple de GtfsCalendarRule au format JSON-LD comme valeurs clés. Cette règle est compatible avec le format NGSI-LD lorsqu'elle n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "endDate": {"@type": "Date", "@value": "2019-01-01"},  
 "friday": True,  
 "hasService": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1",  
 "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
 "monday": True,  
 "name": "Rule Hospital Service 1",  
 "saturday": False,  
 "startDate": {"@type": "Date", "@value": "2018-01-01"},  
 "sunday": False,  
 "thursday": True,  
 "tuesday": True,  
 "type": "GtfsCalendarRule",  
 "wednesday": True}  
```  
Voici un exemple de règle d'agenda GtfsCalendarRule au format JSON-LD, telle que normalisée. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
    "type": "GtfsCalendarRule",  
    "startDate": {  
        "type": "Property",  
        "value": {  
            "@type": "Date",  
            "@value": "2018-01-01"  
        }  
    },  
    "endDate": {  
        "type": "Property",  
        "value": {  
            "@type": "Date",  
            "@value": "2019-01-01"  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Rule Hospital Service 1"  
    },  
    "monday": {  
        "type": "Property",  
        "value": true  
    },  
    "tuesday": {  
        "type": "Property",  
        "value": true  
    },  
    "friday": {  
        "type": "Property",  
        "value": true  
    },  
    "wednesday": {  
        "type": "Property",  
        "value": true  
    },  
    "thursday": {  
        "type": "Property",  
        "value": true  
    },  
    "sunday": {  
        "type": "Property",  
        "value": false  
    },  
    "hasService": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1"  
    },  
    "saturday": {  
        "type": "Property",  
        "value": false  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
