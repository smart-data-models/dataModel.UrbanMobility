Entité : GtfsRoute  
==================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsRoute/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **RouteGTFS**  

## Liste des propriétés  

- `alternateName`: Un nom alternatif pour cet élément  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `name`: Le nom de cet élément.  - `operatedBy`: Agence qui exploite cette route. Il doit pointer vers une entité de type GtfsAgency.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `page`: Identique à GTFS `stop_url`.  - `routeColor`: Identique à GTFS `route_color`. Voir [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)  - `routeSortOrder`: Identique à GTFS `route_sort_order`.  - `routeTextColor`: Identique à GTFS `route_text_color`. Voir [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)  - `routeType`: Identique à GTFS `route_type`. Valeurs autorisées : celles autorisées pour `route_type` comme prescrit par [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt). Enum : "0, 1, 2, 3, 4, 5, 6, 7".  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `shortName`: Même que GTFS `route_short_name`.  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type d'entité NGSI. Il doit être GtfsRoute    
Propriétés requises  
- `id`  - `type`    
Voir [https://developers.google.com/transit/gtfs/reference/#routestxt](https://developers.google.com/transit/gtfs/reference/#routestxt)  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
            format: uri    
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
## Exemples de charges utiles  
#### GtfsRoute Exemple de valeurs-clés NGSI-v2  
Voici un exemple de GtfsRoute au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### GtfsRoute NGSI-v2 normalisé Exemple  
Voici un exemple de GtfsRoute au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### GtfsRoute NGSI-LD valeurs-clés Exemple  
Voici un exemple de GtfsRoute au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### GtfsRoute NGSI-LD normalisé Exemple  
Voici un exemple de GtfsRoute au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
