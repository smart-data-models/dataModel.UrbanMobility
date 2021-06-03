Entidad: GtfsRoute  
==================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsRoute/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Ruta GTFS**  

## Lista de propiedades  

- `alternateName`: Un nombre alternativo para este artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `name`: El nombre de este artículo.  - `operatedBy`: Agencia que opera esta ruta. Deberá apuntar a una entidad de tipo GtfsAgency  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `page`: Igual que GTFS `stop_url`  - `routeColor`: Igual que GTFS `route_color`. Véase [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)  - `routeSortOrder`: Igual que en GTFS `route_sort_order`.  - `routeTextColor`: Igual que GTFS `route_text_color`. Véase [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)  - `routeType`: Igual que GTFS `route_type`. valores permitidos los permitidos para `route_type` según lo prescrito por [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt). Enum:'0, 1, 2, 3, 4, 5, 6, 7'  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `shortName`: Igual que GTFS `nombre_corto_de_la_ruta`.  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `type`: Tipo de entidad NGSI. Tiene que ser GtfsRoute    
Propiedades requeridas  
- `id`  - `type`    
Véase [https://developers.google.com/transit/gtfs/reference/#routestxt](https://developers.google.com/transit/gtfs/reference/#routestxt)  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
## Ejemplo de carga útil  
#### GtfsRoute NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un GtfsRoute en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### GtfsRoute NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de un GtfsRoute en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### GtfsRoute NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un GtfsRoute en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### GtfsRoute NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un GtfsRoute en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
