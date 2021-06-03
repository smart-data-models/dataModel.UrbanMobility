Entidad: GtfsAgency  
===================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsAgency/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Agencia GTFS**  

## Lista de propiedades  

- `addressCountry`: El país. Por ejemplo, España  - `addressLocality`: La localidad en la que se encuentra la dirección, y que está en la región  - `addressRegion`: La región en la que se encuentra la localidad, y que está en el país  - `agencyName`: Igual que GTFS `nombre_de_agencia`.  - `alternateName`: Un nombre alternativo para este artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `entitySource`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Deberá apuntar a la URL de la fuente GTFS original utilizada para generar esta Entidad.  - `id`: Identificador único de la entidad  - `language`: Igual que GTFS `agency_language`. Véase [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `page`: Igual que GTFS `stop_url`  - `phone`: Igual que el GFTS `agency_phone`.  - `postOfficeBoxNumber`: El número del apartado de correos para las direcciones de los apartados postales. Por ejemplo, 03578  - `postalCode`: El código postal. Por ejemplo, 24004  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `streetAddress`: La dirección de la calle  - `timezone`: Igual que GTFS `agency_timezone`. Véase [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)  - `type`: Tipo de entidad NGSI: Tiene que ser GtfsAgency    
Propiedades requeridas  
- `agencyName`  - `id`  - `source`  - `type`    
Véase [https://developers.google.com/transit/gtfs/reference/#agencytxt](https://developers.google.com/transit/gtfs/reference/#agencytxt)  
## Descripción del modelo de datos de las propiedades  
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
## Ejemplo de carga útil  
#### GtfsAgency NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un GtfsAgency en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### GtfsAgency NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de un GtfsAgency en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### GtfsAgency NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un GtfsAgency en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### GtfsAgency NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un GtfsAgency en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
