Entité : GtfsAgency  
===================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsAgency/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : Agence **GTFS**  

## Liste des propriétés  

- `addressCountry`: Le pays. Par exemple, l'Espagne  - `addressLocality`: La localité dans laquelle se trouve l'adresse civique, et qui se trouve dans la région  - `addressRegion`: La région dans laquelle se trouve la localité, et qui est dans le pays  - `agencyName`: Identique à GTFS `agency_name`.  - `alternateName`: Un nom alternatif pour cet élément  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `entitySource`: Une séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Elle doit pointer vers l'URL du flux GTFS original utilisé pour générer cette entité.  - `id`: Identifiant unique de l'entité  - `language`: Identique à GTFS `agency_language`. Voir [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `page`: Identique à GTFS `stop_url`.  - `phone`: Identique au GFTS `agency_phone`.  - `postOfficeBoxNumber`: Le numéro de la boîte postale pour les adresses de type boîte postale. Par exemple, 03578  - `postalCode`: Le code postal. Par exemple, 24004  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `streetAddress`: L'adresse de la rue  - `timezone`: Identique à GTFS `agency_timezone`. Voir [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)  - `type`: Type d'entité NGSI : Il doit s'agir de GtfsAgency    
Propriétés requises  
- `agencyName`  - `id`  - `source`  - `type`    
Voir [https://developers.google.com/transit/gtfs/reference/#agencytxt](https://developers.google.com/transit/gtfs/reference/#agencytxt)  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsAgency:    
  description: 'GTFS Agency'    
  properties:    
    addressCountry:    
      description: 'The country. For example, Spain'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/addressCountry    
    addressLocality:    
      description: 'The locality in which the street address is, and which is in the region'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/addressLocality    
    addressRegion:    
      description: 'The region in which the locality is, and which is in the country'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/addressRegion    
    agencyName:    
      description: 'Same as GTFS `agency_name`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
    entitySource:    
      description: 'A sequence of characters giving the original source of the Entity data as a URL. It shall point to the URL of the original GTFS feed used to generate this Entity'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    id:    
      anyOf: &gtfsagency_-_properties_-_owner_-_items_-_anyof    
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
    language:    
      description: "Same as GTFS `agency_language`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)"    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfsagency_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    page:    
      description: 'Same as GTFS `stop_url`'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: http://schema.org/URL    
    phone:    
      description: 'Same as GFTS `agency_phone`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    postOfficeBoxNumber:    
      description: 'The post office box number for PO box addresses. For example, 03578'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/postOfficeBoxNumber    
    postalCode:    
      description: 'The postal code. For example, 24004'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/https://schema.org/postalCode    
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
    streetAddress:    
      description: 'The street address'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/streetAddress    
    timezone:    
      description: "Same as GTFS `agency_timezone`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)"    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI Entity Type: It has to be GtfsAgency'    
      enum:    
        - GtfsAgency    
      type: Property    
  required:    
    - id    
    - type    
    - agencyName    
    - source    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### GtfsAgency NGSI-v2 key-values Exemple  
Voici un exemple d'une GtfsAgency au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
  "type": "GtfsAgency",  
  "agencyName": "Empresa Malagueña de Transportes",  
  "page": "http://www.emtmalaga.es/",  
  "timezone": "Europe/Madrid",  
  "language": "ES",  
  "source": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52"  
}  
```  
#### GtfsAgency NGSI-v2 normalisé Exemple  
Voici un exemple d'une GtfsAgency au format JSON-LD tel que normalisé. Ceci est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
  "type": "GtfsAgency",  
  "agencyName": {  
    "value": "Empresa Malague\u00f1a de Transportes"  
  },  
  "language": {  
    "value": "ES"  
  },  
  "page": {  
    "value": "http://www.emtmalaga.es/"  
  },  
  "source": {  
    "value": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52"  
  },  
  "timezone": {  
    "value": "Europe/Madrid"  
  }  
}  
```  
#### GtfsAgency Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'une GtfsAgency au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
  "type": "GtfsAgency",  
  "agencyName": {  
    "type": "Property",  
    "value": "Empresa Malague\u00f1a de Transportes"  
  },  
  "language": {  
    "type": "Property",  
    "value": "ES"  
  },  
  "page": {  
    "type": "Property",  
    "value": "http://www.emtmalaga.es/"  
  },  
  "source": {  
    "type": "Property",  
    "value": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52"  
  },  
  "timezone": {  
    "type": "Property",  
    "value": "Europe/Madrid"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### GtfsAgency NGSI-LD normalisé Exemple  
Voici un exemple d'une GtfsAgency au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
  "language": "ES",  
  "agencyName": "Empresa Malague\u00f1a de Transportes",  
  "page": "http://www.emtmalaga.es/",  
  "source": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52",  
  "timezone": "Europe/Madrid",  
  "type": "GtfsAgency"  
}  
```  
