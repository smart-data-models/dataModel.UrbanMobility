Entidad: GtfsAgency  
===================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsAgency/LICENSE.md)  
Descripción global: **Agencia GTFS**  

## Lista de propiedades  

- `addressCountry`: El país. Por ejemplo, España  - `addressLocality`: La localidad en la que se encuentra la dirección, y que está en la región  - `addressRegion`: La región en la que se encuentra la localidad, y que está en el país  - `agencyName`: Igual que el "nombre de la agencia" del GTFS.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Esta será normalmente asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `entitySource`: Una secuencia de caracteres que da la fuente original de los datos de la Entidad como una URL. Apuntará a la URL de la fuente original del GTFS utilizada para generar esta Entidad  - `id`: Identificador único de la entidad  - `language`: Igual que el "lenguaje de la agencia" del GTFS. Ver [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `page`: Igual que GTFS `stop_url`  - `phone`: Igual que el "teléfono de la agencia" de GFTS.  - `postOfficeBoxNumber`: El número del apartado postal para las direcciones de los apartados de correos. Por ejemplo, España  - `postalCode`: El código postal. Por ejemplo, España  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `streetAddress`: La dirección de la calle  - `timezone`: Igual que la "zona de tiempo de la agencia" del GTFS. Ver [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)  - `type`: Tipo de entidad NGSI: Tiene que ser GtfsAgency    
Propiedades requeridas  
- `agencyName`  - `id`  - `source`  - `type`    
Véase [https://developers.google.com/transit/gtfs/reference/#agencytxt](https://developers.google.com/transit/gtfs/reference/#agencytxt)  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
## Ejemplo de cargas útiles  
#### Ejemplo de valores clave de la Agencia GtfsAgency NGSI V2  
Aquí hay un ejemplo de una Agencia Gtfs en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza `opciones=valores-clave` y devuelve los datos de contexto de una entidad individual.  
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
#### GtfsAgency NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de una Agencia Gtfs en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### GtfsAgencia NGSI-LD Ejemplo de valores clave  
Aquí hay un ejemplo de una Agencia Gtfs en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### GtfsAgency NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de una Agencia Gtfs en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
