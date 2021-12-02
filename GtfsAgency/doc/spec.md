Entity: GtfsAgency  
==================  
[Open License](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsAgency/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **GTFS Agency**  

## List of properties  

- `addressCountry`: The country. For example, Spain  - `addressLocality`: The locality in which the street address is, and which is in the region  - `addressRegion`: The region in which the locality is, and which is in the country  - `agencyName`: Same as GTFS `agency_name`  - `alternateName`: An alternative name for this item  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `entitySource`: A sequence of characters giving the original source of the Entity data as a URL. It shall point to the URL of the original GTFS feed used to generate this Entity  - `id`: Unique identifier of the entity  - `language`: Same as GTFS `agency_language`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `page`: Same as GTFS `stop_url`  - `phone`: Same as GFTS `agency_phone`  - `postOfficeBoxNumber`: The post office box number for PO box addresses. For example, 03578  - `postalCode`: The postal code. For example, 24004  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `streetAddress`: The street address  - `timezone`: Same as GTFS `agency_timezone`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)  - `type`: NGSI Entity Type: It has to be GtfsAgency    
Required properties  
- `agencyName`  - `id`  - `source`  - `type`    
See [https://developers.google.com/transit/gtfs/reference/#agencytxt](https://developers.google.com/transit/gtfs/reference/#agencytxt)  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsAgency:    
  description: 'GTFS Agency'    
  properties:    
    addressCountry:    
      description: 'The country. For example, Spain'    
      type: string    
      x-ngsi:    
        model: https://schema.org/addressCountry    
        type: Property    
    addressLocality:    
      description: 'The locality in which the street address is, and which is in the region'    
      type: string    
      x-ngsi:    
        model: https://schema.org/addressLocality    
        type: Property    
    addressRegion:    
      description: 'The region in which the locality is, and which is in the country'    
      type: string    
      x-ngsi:    
        model: https://schema.org/addressRegion    
        type: Property    
    agencyName:    
      description: 'Same as GTFS `agency_name`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
    entitySource:    
      description: 'A sequence of characters giving the original source of the Entity data as a URL. It shall point to the URL of the original GTFS feed used to generate this Entity'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
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
      x-ngsi:    
        type: Property    
    language:    
      description: "Same as GTFS `agency_language`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfsagency_-_properties_-_owner_-_items_-_anyof    
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
    phone:    
      description: 'Same as GFTS `agency_phone`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    postOfficeBoxNumber:    
      description: 'The post office box number for PO box addresses. For example, 03578'    
      type: string    
      x-ngsi:    
        model: https://schema.org/postOfficeBoxNumber    
        type: Property    
    postalCode:    
      description: 'The postal code. For example, 24004'    
      type: string    
      x-ngsi:    
        model: https://schema.org/https://schema.org/postalCode    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    streetAddress:    
      description: 'The street address'    
      type: string    
      x-ngsi:    
        model: https://schema.org/streetAddress    
        type: Property    
    timezone:    
      description: "Same as GTFS `agency_timezone`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity Type: It has to be GtfsAgency'    
      enum:    
        - GtfsAgency    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - agencyName    
    - source    
  type: object    
```  
</details>    
## Example payloads    
#### GtfsAgency NGSI-v2 key-values Example    
Here is an example of a GtfsAgency in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### GtfsAgency NGSI-v2 normalized Example    
Here is an example of a GtfsAgency in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### GtfsAgency NGSI-LD key-values Example    
Here is an example of a GtfsAgency in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### GtfsAgency NGSI-LD normalized Example    
Here is an example of a GtfsAgency in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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

See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units
