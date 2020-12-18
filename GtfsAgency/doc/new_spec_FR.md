Entité : GtfsAgency  
===================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsAgency/LICENSE.md)  
Description globale : **Agence GTFS**  

## Liste des biens  

- `addressCountry`: Le pays. Par exemple, l'Espagne  - `addressLocality`: La localité dans laquelle se trouve l'adresse de la rue, et qui se trouve dans la région  - `addressRegion`: La région dans laquelle se trouve la localité, et qui se trouve dans le pays  - `agencyName`: Identique à GTFS `nom_de_l'agence`.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `entitySource`: Une séquence de caractères donnant la source originale des données de l'entité comme URL. Elle doit pointer vers l'URL du flux GTFS original utilisé pour générer cette Entité  - `id`: Identifiant unique de l'entité  - `language`: Même chose que GTFS `agency_language`. Voir [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `page`: Même chose que GTFS `stop_url`.  - `phone`: Même chose que GFTS `agency_phone`.  - `postOfficeBoxNumber`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, l'Espagne  - `postalCode`: Le code postal. Par exemple, l'Espagne  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `streetAddress`: L'adresse de la rue  - `timezone`: Même chose que GTFS `agency_timezone`. Voir [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)  - `type`: Type d'entité NGSI : Il doit s'agir de GtfsAgency    
Propriétés requises  
- `agencyName`  - `id`  - `source`  - `type`    
Voir [https://developers.google.com/transit/gtfs/reference/#agencytxt](https://developers.google.com/transit/gtfs/reference/#agencytxt)  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsAgency:    
  description: 'GTFS Agency'    
  properties:    
    addressCountry:    
      description: 'The country. For example, Spain'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    addressLocality:    
      description: 'The locality in which the street address is, and which is in the region'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    addressRegion:    
      description: 'The region in which the locality is, and which is in the country'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    agencyName:    
      description: 'Same as GTFS `agency_name`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: 'The post office box number for PO box addresses. For example, Spain'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    postalCode:    
      description: 'The postal code. For example, Spain'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    streetAddress:    
      description: 'The street address'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
#### GtfsAgency NGSI V2 key-values Exemple  
Voici un exemple d'une agence Gtfs au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
  "type": "GtfsAgency",  
  "name": "Empresa Malagueña de Transportes",  
  "page": "http://www.emtmalaga.es/",  
  "timezone": "Europe/Madrid",  
  "language": "ES",  
  "source": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52"  
}  
```  
#### GtfsAgency NGSI V2 normalisé Exemple  
Voici un exemple de GtfsAgency au format JSON tel que normalisé. Ce format est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
  "type": "GtfsAgency",  
  "name": {  
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
#### GtfsAgency NGSI-LD valeurs clés Exemple  
Voici un exemple d'une agence Gtfs au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
 "language": "ES",  
 "name": "Empresa MalagueÃ±a de Transportes",  
 "page": "http://www.emtmalaga.es/",  
 "source": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52",  
 "timezone": "Europe/Madrid",  
 "type": "GtfsAgency"}  
```  
#### GtfsAgency NGSI-LD normalisé Exemple  
Voici un exemple de GtfsAgency au format JSON-LD tel que normalisé. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
    "type": "GtfsAgency",  
    "name": {  
        "type": "Property",  
        "value": "Empresa MalagueÃ±a de Transportes"  
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
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
