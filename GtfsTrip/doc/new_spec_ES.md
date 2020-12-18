Entidad: GtfsTrip  
=================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsTrip/LICENSE.md)  
Descripción global: **GTFS Trip**  

## Lista de propiedades  

- `alternateName`: Un nombre alternativo para este artículo  - `bikesAllowed`: Lo mismo que GTFS "bicis_permitidas". Enum: '0, 1, 2'. Ver [GTFS](https://developers.google.com/transit/gtfs/reference/#tripstxt)  - `block`: Lo mismo que el "ID de bloque" de GTFS.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `direction`: Igual que el "id_de_dirección" de GTFS. Enum:'0, 1'.  - `hasRoute`: Lo mismo que el "Rute_id". Apuntará a una Entidad de tipo GtfsRoute  - `hasService`: Lo mismo que el "Service_id" de GTFS. Apuntará a una Entidad de tipo GtfsService  - `hasShape`: Igual que el "Shape_id" de GTFS. Apuntará a una entidad de tipo GtfsShape  - `headSign`: Lo mismo que el signo de cabeza de viaje de GTFS.  - `id`: Identificador único de la entidad  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `shortName`: Igual que GTFS "nombre_corto_del_viaje  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `type`: Tipo de entidad NGSI. Tiene que ser GtfsTrip  - `wheelChairAccessible`: Igual que el GTFS "silla de ruedas accesible". Enum:'0, 1, 2'.    
Propiedades requeridas  
- `hasRoute`  - `hasService`  - `id`  - `type`    
Ver [https://developers.google.com/transit/gtfs/reference/#tripstxt](https://developers.google.com/transit/gtfs/reference/#tripstxt)  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsTrip:    
  description: 'GTFS Trip'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    bikesAllowed:    
      description: "Same as GTFS `bikes_allowed`. Enum:'0, 1, 2'. See [GTFS](https://developers.google.com/transit/gtfs/reference/#tripstxt)"    
      enum:    
        - 0    
        - 1    
        - 2    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    block:    
      description: 'Same as GTFS `block_id`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
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
    direction:    
      description: 'Same as GTFS `direction_id`. Enum:''0, 1'''    
      enum:    
        - 0    
        - 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    hasRoute:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Same as `route_id`. It shall point to an Entity of type GtfsRoute'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
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
      description: 'Same as GTFS `service_id`. It shall point to an Entity of type GtfsService'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    hasShape:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Same as GTFS `shape_id`. It shall point to an Entity of type GtfsShape'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
    headSign:    
      description: 'Same as GTFS `trip_headsign`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
    id:    
      anyOf: &gtfstrip_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *gtfstrip_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
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
    shortName:    
      description: 'Same as GTFS `trip_short_name`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be GtfsTrip'    
      enum:    
        - GtfsTrip    
      type: Property    
    wheelChairAccessible:    
      description: 'Same as GTFS `wheelchair_accessible`. Enum:''0, 1, 2'''    
      enum:    
        - 0    
        - 1    
        - 2    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
  required:    
    - id    
    - type    
    - hasRoute    
    - hasService    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### GtfsTrip NGSI V2 Ejemplo de valores clave  
Aquí hay un ejemplo de un GtfsTrip en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza `opciones=valores-clave` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
  "type": "GtfsTrip",  
  "hasService": "urn:ngsi-ld:GtfsService:Malaga_LAB",  
  "headSign": "San Andrés",  
  "direction": 0,  
  "hasRoute": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
  "hasShape": "urn:ngsi-ld:GtfsShape:Shape01"  
}  
```  
#### GtfsTrip NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un GtfsTrip en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
  "type": "GtfsTrip",  
  "direction": {  
    "value": 0  
  },  
  "headSign": {  
    "value": "San Andr\u00e9s"  
  },  
  "hasRoute": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1"  
  },  
  "hasService": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsService:Malaga_LAB"  
  },  
  "hasShape": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsShape:Shape01"  
  }  
}  
```  
#### GtfsTrip NGSI-LD Ejemplo de valores clave  
Aquí hay un ejemplo de un Viaje Gtfs en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "direction": 0,  
 "hasRoute": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
 "hasService": "urn:ngsi-ld:GtfsService:Malaga_LAB",  
 "hasShape": "urn:ngsi-ld:GtfsShape:Shape01",  
 "headSign": "San AndrÃ©s",  
 "id": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
 "type": "GtfsTrip"}  
```  
#### GtfsTrip NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un GtfsTrip en formato JSON-LD normalizado. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
    "type": "GtfsTrip",  
    "direction": {  
        "type": "Property",  
        "value": 0  
    },  
    "headSign": {  
        "type": "Property",  
        "value": "San AndrÃ©s"  
    },  
    "hasRoute": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1"  
    },  
    "hasService": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsService:Malaga_LAB"  
    },  
    "hasShape": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsShape:Shape01"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
