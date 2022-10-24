<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : GtfsRoute  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsRoute/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **RouteGTFS**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `alternateName[string]`: Un nom alternatif pour cet élément  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `id[*]`: Identifiant unique de l'entité  - `name[string]`: Le nom de cet élément.  - `operatedBy[*]`: Agence qui exploite cette route. Il doit pointer vers une entité de type GtfsAgency.  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `page[string]`: Identique à GTFS `stop_url`.  . Model: [http://schema.org/URL](http://schema.org/URL)- `routeColor[string]`: Identique à GTFS `route_color`. Voir [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)  . Model: [https://schema.org/Text](https://schema.org/Text)- `routeSortOrder[integer]`: Identique à GTFS `route_sort_order`.  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `routeTextColor[string]`: Identique à GTFS `route_text_color`. Voir [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)  . Model: [https://schema.org/Text](https://schema.org/Text)- `routeType[string]`: Identique à GTFS `route_type`. Valeurs autorisées : celles autorisées pour `route_type` comme prescrit par [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt). Enum : "0, 1, 2, 3, 4, 5, 6, 7".  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `shortName[string]`: Identique à GTFS `route_short_name`.  . Model: [https://schema.org/Text.](https://schema.org/Text.)- `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type[string]`: Type d'entité NGSI. Il doit être GtfsRoute  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Voir [https://developers.google.com/transit/gtfs/reference/#routestxt](https://developers.google.com/transit/gtfs/reference/#routestxt)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsRoute:    
  description: 'GTFS Route'    
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
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
        model: https://schema.org/Text    
        type: Relationship    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfsroute_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    page:    
      description: 'Same as GTFS `stop_url`'    
      format: uri    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Property    
    routeColor:    
      description: "Same as GTFS `route_color`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    routeSortOrder:    
      description: 'Same as GTFS `route_sort_order`'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    routeTextColor:    
      description: "Same as GTFS `route_text_color`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    shortName:    
      description: 'Same as GTFS `route_short_name`'    
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
      description: 'NGSI Entity type. It has to be GtfsRoute'    
      enum:    
        - GtfsRoute    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsRoute/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/specs/UrbanMobility/GtfsRoute/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### GtfsRoute Exemple de valeurs-clés NGSI-v2  
Voici un exemple de GtfsRoute au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### GtfsRoute NGSI-v2 normalisé Exemple  
Voici un exemple de GtfsRoute au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### GtfsRoute NGSI-LD valeurs-clés Exemple  
Voici un exemple de GtfsRoute au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
    "type": "GtfsRoute",  
    "name": {  
        "type": "Property",  
        "value": "Parque del Sur _ Alameda Principal _ San Andr\u00e9s"  
    },  
    "operatedBy": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsAgency:Malaga_EMT"  
    },  
    "page": {  
        "type": "Property",  
        "value": "http://www.emtmalaga.es/emt-mobile/informacionLinea.html"  
    },  
    "routeType": {  
        "type": "Property",  
        "value": "3"  
    },  
    "shortName": {  
        "type": "Property",  
        "value": "1"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### GtfsRoute NGSI-LD normalisé Exemple  
Voici un exemple de GtfsRoute au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
    "type": "GtfsRoute",  
    "name": "Parque del Sur _ Alameda Principal _ San Andr\u00e9s",  
    "operatedBy": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
    "page": "http://www.emtmalaga.es/emt-mobile/informacionLinea.html",  
    "routeType": "3",  
    "shortName": "1",  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
