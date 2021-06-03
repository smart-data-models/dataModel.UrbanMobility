Entité : GtfsCalendarRule  
=========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsCalendarRule/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Modèles de données intelligents. Règle du calendrier GTFS**  

## Liste des propriétés  

- `alternateName`: Un nom alternatif pour cet élément  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `endDate`: Date de fin de cette règle au format `YYYY-MM-DD`. Elle peut être obtenue à partir du champ `end_date` de [calendar.txt] (https://developers.google.com/transit/gtfs/reference/#calendartxt).  - `friday`: Identique à GTFS `vendredi`.  - `hasService`: Service auquel s'applique cette règle. Dérivé de `service_id`.  - `id`: Identifiant unique de l'entité  - `monday`: Même chose que GTFS `monday`.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `saturday`: Même chose que GTFS `saturday`.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `startDate`: Date de début de cette règle au format `YYYY-MM-DD`. Elle peut être obtenue à partir du champ `start_date` de [calendar.txt] (https://developers.google.com/transit/gtfs/reference/#calendartxt).  - `sunday`: Identique à GTFS `sunday`.  - `thursday`: Identique à GTFS `jeudi`.  - `tuesday`: Identique à GTFS `tuesday`.  - `type`: Type d'entité NGSI : Il doit être GtfsCalendarRule  - `wednesday`: Identique à GTFS `wednesday`.    
Propriétés requises  
- `endDate`  - `friday`  - `hasService`  - `id`  - `monday`  - `saturday`  - `startDate`  - `sunday`  - `thursday`  - `tuesday`  - `type`  - `wednesday`    
Voir [https://developers.google.com/transit/gtfs/reference/#calendartxt](https://developers.google.com/transit/gtfs/reference/#calendartxt)  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
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
      description: "End date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `end_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)"    
      format: date    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    friday:    
      description: 'Same as GTFS `friday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
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
      description: 'Service to which this rule applies to. Derived from `service_id`'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
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
      description: 'Unique identifier of the entity'    
      type: Property    
    monday:    
      description: 'Same as GTFS `monday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfscalendarrule_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    saturday:    
      description: 'Same as GTFS `saturday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
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
    startDate:    
      description: "Start date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `start_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)"    
      format: date    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Date    
    sunday:    
      description: 'Same as GTFS `sunday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    thursday:    
      description: 'Same as GTFS `thursday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    tuesday:    
      description: 'Same as GTFS `tuesday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    type:    
      description: 'NGSI Entity Type: It has to be GtfsCalendarRule'    
      enum:    
        - GtfsCalendarRule    
      type: Property    
    wednesday:    
      description: 'Same as GTFS `wednesday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
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
</details>    
## Exemples de charges utiles  
#### GtfsCalendarRule Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de GtfsCalendarRule au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### GtfsCalendarRule NGSI-v2 normalisée Exemple  
Voici un exemple de GtfsCalendarRule au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "type": "GtfsCalendarRule",  
  "startDate": {  
    "type": "Property",  
    "value": "2018-01-01"  
  },  
  "endDate": {  
    "type": "Property",  
    "value": "2019-01-01"  
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
  }  
}  
```  
#### GtfsCalendarRule Valeurs-clés NGSI-LD Exemple  
Voici un exemple de GtfsCalendarRule au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### GtfsCalendarRule NGSI-LD normalisé Exemple  
Voici un exemple de GtfsCalendarRule au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "endDate": "2019-01-01",  
  "friday": true,  
  "hasService": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1",  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "monday": true,  
  "name": "Rule Hospital Service 1",  
  "saturday": false,  
  "startDate": "2018-01-01",  
  "sunday": false,  
  "thursday": true,  
  "tuesday": true,  
  "type": "GtfsCalendarRule",  
  "wednesday": true  
}  
```  
