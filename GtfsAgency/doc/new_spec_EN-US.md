Entity: GtfsAgency  
==================  
[Open License](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsAgency/LICENSE.md)  
Global description: **GTFS Agency**  

## List of properties  

- `addressCountry`: The country. For example, Spain  - `addressLocality`: The locality in which the street address is, and which is in the region  - `addressRegion`: The region in which the locality is, and which is in the country  - `agencyName`: Same as GTFS `agency_name`  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `entitySource`: A sequence of characters giving the original source of the Entity data as a URL. It shall point to the URL of the original GTFS feed used to generate this Entity  - `id`: Unique identifier of the entity  - `language`: Same as GTFS `agency_language`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `page`: Same as GTFS `stop_url`  - `phone`: Same as GFTS `agency_phone`  - `postOfficeBoxNumber`: The post office box number for PO box addresses. For example, Spain  - `postalCode`: The postal code. For example, Spain  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `streetAddress`: The street address  - `timezone`: Same as GTFS `agency_timezone`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)  - `type`: NGSI Entity Type: It has to be GtfsAgency    
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
## Example payloads    
#### GtfsAgency NGSI V2 key-values Example    
Here is an example of a GtfsAgency in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### GtfsAgency NGSI V2 normalized Example    
Here is an example of a GtfsAgency in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
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
#### GtfsAgency NGSI-LD key-values Example    
Here is an example of a GtfsAgency in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### GtfsAgency NGSI-LD normalized Example    
Here is an example of a GtfsAgency in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
