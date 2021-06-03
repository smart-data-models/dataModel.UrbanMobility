Entité : GtfsCalendarDateRule  
=============================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsCalendarDateRule/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Règle de la date du calendrier **GTFS  

## Liste des propriétés  

- `alternateName`: Un nom alternatif pour cet élément  - `appliesOn`:  Date (au format AAAA-MM-JJ) à laquelle s'applique cette règle. Elle est obtenue à partir du champ GTFS `date`.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `exceptionType`: Identique au champ `exception_type` de GTFS. Enum : "1, 2  - `hasService`: Service auquel s'applique cette règle. Dérivé de `service_id`.  - `id`: Identifiant unique de l'entité  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type d'entité NGSI : Il doit être GtfsCalendarDateRule    
Propriétés requises  
- `appliesOn`  - `exceptionType`  - `hasService`  - `id`  - `type`    
Voir [https://developers.google.com/transit/gtfs/reference/#calendar_datestxt](https://developers.google.com/transit/gtfs/reference/#calendar_datestxt)  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsCalendarDateRule:    
  description: 'GTFS Calendar Date Rule'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    appliesOn:    
      description: ' Date (in YYYY-MM-DD format) this rule applies to. It shall be obtained from the GTFS `date` field'    
      format: date    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Date    
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
    exceptionType:    
      description: 'Same as GTFS `exception_type` field. Enum:''1, 2'''    
      enum:    
        - 1    
        - 2    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      anyOf: &gtfscalendardaterule_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *gtfscalendardaterule_-_properties_-_owner_-_items_-_anyof    
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
    type:    
      description: 'NGSI Entity Type: It has to be GtfsCalendarDateRule'    
      enum:    
        - GtfsCalendarDateRule    
      type: Property    
  required:    
    - id    
    - type    
    - hasService    
    - appliesOn    
    - exceptionType    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### GtfsCalendarDateRule Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de GtfsCalendarDateRule au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CalendarDateRule:Malaga:Rule67",  
  "type": "GtfsCalendarDateRule",  
  "name": "Rule Fair Area",  
  "hasService": "urn:ngsi-ld:Gtfservice:Malaga:FairArea_1",  
  "appliesOn": "2018-03-19",  
  "exceptionType": "1"  
}  
```  
#### GtfsCalendarDateRule NGSI-v2 normalisée Exemple  
Voici un exemple de GtfsCalendarDateRule au format JSON-LD tel que normalisé. Cette règle est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CalendarDateRule:Malaga:Rule67",  
  "type": "GtfsCalendarDateRule",  
  "name": {  
    "value": "Rule Fair Area"  
  },  
  "exceptionType": {  
    "value": "1"  
  },  
  "hasService": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsService:Malaga:FairArea_1"  
  },  
  "appliesOn": {  
    "value": "2018-03-19"  
  }  
}  
```  
#### GtfsCalendarDateRule Valeurs clés NGSI-LD Exemple  
Voici un exemple de GtfsCalendarDateRule au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CalendarDateRule:Malaga:Rule67",  
  "type": "GtfsCalendarDateRule",  
  "name": {  
    "type": "Property",  
    "value": "Rule Fair Area"  
  },  
  "exceptionType": {  
    "type": "Property",  
    "value": "1"  
  },  
  "hasService": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:GtfsService:Malaga:FairArea_1"  
  },  
  "appliesOn": {  
    "type": "Property",  
    "value": "2018-03-19"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### GtfsCalendarDateRule NGSI-LD normalisée Exemple  
Voici un exemple de GtfsCalendarDateRule au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "appliesOn": "2018-03-19",  
  "exceptionType": "1",  
  "hasService": "urn:ngsi-ld:GtfsService:Malaga:FairArea_1",  
  "id": "urn:ngsi-ld:CalendarDateRule:Malaga:Rule67",  
  "name": "Rule Fair Area",  
  "type": "GtfsCalendarDateRule"  
}  
```  
