Entidad: GtfsCalendarRule  
=========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsCalendarRule/LICENSE.md)  
Descripción global: **Modelos de datos inteligentes. Regla del calendario del GTFS**  

## Lista de propiedades  

- `alternateName`: Un nombre alternativo para este artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `endDate`: Fecha de finalización de esta regla en formato "AAAA-MM-DD". Se puede obtener del campo `end_date` de [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)  - `friday`: Lo mismo que el GTFS "viernes  - `hasService`: Servicio al que se aplica esta regla. Derivado de `service_id`  - `id`: Identificador único de la entidad  - `monday`: Lo mismo que el "lunes" del GTFS.  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `saturday`: Lo mismo que el "sábado" del GTFS.  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `startDate`: Fecha de inicio de esta regla en formato "AAAA-MM-DD". Se puede obtener del campo `fecha_inicio` de [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)  - `sunday`: Lo mismo que el "domingo" del GTFS.  - `thursday`: Lo mismo que el GTFS "jueves".  - `tuesday`: Lo mismo que el GTFS "martes  - `type`: Tipo de entidad NGSI: Tiene que ser GtfsCalendarRule  - `wednesday`: Lo mismo que el GTFS "miércoles    
Propiedades requeridas  
- `endDate`  - `friday`  - `hasService`  - `id`  - `monday`  - `saturday`  - `startDate`  - `sunday`  - `thursday`  - `tuesday`  - `type`  - `wednesday`    
Ver [https://developers.google.com/transit/gtfs/reference/#calendartxt](https://developers.google.com/transit/gtfs/reference/#calendartxt)  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsCalendarRule:    
  description: 'Smart Data Models. GTFS Calendar Rule'    
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
    endDate:    
      description: "End date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `end_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)"    
      format: date    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    friday:    
      description: 'Same as GTFS `friday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
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
      description: 'Service to which this rule applies to. Derived from `service_id`'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    id:    
      anyOf: &gtfscalendarrule_-_properties_-_owner_-_items_-_anyof    
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
    monday:    
      description: 'Same as GTFS `monday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfscalendarrule_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    saturday:    
      description: 'Same as GTFS `saturday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
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
    startDate:    
      description: "Start date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `start_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)"    
      format: date    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Date    
    sunday:    
      description: 'Same as GTFS `sunday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    thursday:    
      description: 'Same as GTFS `thursday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    tuesday:    
      description: 'Same as GTFS `tuesday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    type:    
      description: 'NGSI Entity Type: It has to be GtfsCalendarRule'    
      enum:    
        - GtfsCalendarRule    
      type: Property    
    wednesday:    
      description: 'Same as GTFS `wednesday`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
  required:    
    - id    
    - type    
    - hasService    
    - monday    
    - tuesday    
    - wednesday    
    - thursday    
    - friday    
    - saturday    
    - sunday    
    - startDate    
    - endDate    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### GtfsCalendarRule NGSI V2 key-values Example  
Aquí hay un ejemplo de una Regla de Calendario Gtfs en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "type": "GtfsCalendarRule",  
  "name": "Rule Hospital Service 1",  
  "hasService": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1",  
  "monday": true,  
  "tuesday": true,  
  "wednesday": true,  
  "thursday": true,  
  "friday": true,  
  "saturday": false,  
  "sunday": false,  
  "startDate": "2018-01-01",  
  "endDate": "2019-01-01"  
}  
```  
#### GtfsCalendarRule NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de una Regla de Calendario Gtfs en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "type": "GtfsCalendarRule",  
  "startDate": {  
    "type": "Date",  
    "value": "2018-01-01"  
  },  
  "endDate": {  
    "type": "Date",  
    "value": "2019-01-01"  
  },  
  "name": {  
    "value": "Rule Hospital Service 1"  
  },  
  "monday": {  
    "value": true  
  },  
  "tuesday": {  
    "value": true  
  },  
  "friday": {  
    "value": true  
  },  
  "wednesday": {  
    "value": true  
  },  
  "thursday": {  
    "value": true  
  },  
  "sunday": {  
    "value": false  
  },  
  "hasService": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1"  
  },  
  "saturday": {  
    "value": false  
  }  
}  
```  
#### GtfsCalendarRule NGSI-LD key-values Example  
Aquí hay un ejemplo de una Regla de Calendario Gtfs en formato JSON-LD como valores clave. Es compatible con NGSI-LD cuando se utiliza `opciones=valores-clave` y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "endDate": {"@type": "Date", "@value": "2019-01-01"},  
 "friday": True,  
 "hasService": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1",  
 "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
 "monday": True,  
 "name": "Rule Hospital Service 1",  
 "saturday": False,  
 "startDate": {"@type": "Date", "@value": "2018-01-01"},  
 "sunday": False,  
 "thursday": True,  
 "tuesday": True,  
 "type": "GtfsCalendarRule",  
 "wednesday": True}  
```  
#### GtfsCalendarRule NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de una Regla de Calendario de Gtfs en formato JSON-LD normalizado. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
    "type": "GtfsCalendarRule",  
    "startDate": {  
        "type": "Property",  
        "value": {  
            "@type": "Date",  
            "@value": "2018-01-01"  
        }  
    },  
    "endDate": {  
        "type": "Property",  
        "value": {  
            "@type": "Date",  
            "@value": "2019-01-01"  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Rule Hospital Service 1"  
    },  
    "monday": {  
        "type": "Property",  
        "value": true  
    },  
    "tuesday": {  
        "type": "Property",  
        "value": true  
    },  
    "friday": {  
        "type": "Property",  
        "value": true  
    },  
    "wednesday": {  
        "type": "Property",  
        "value": true  
    },  
    "thursday": {  
        "type": "Property",  
        "value": true  
    },  
    "sunday": {  
        "type": "Property",  
        "value": false  
    },  
    "hasService": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1"  
    },  
    "saturday": {  
        "type": "Property",  
        "value": false  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
