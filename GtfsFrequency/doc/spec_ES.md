Entidad: GtfsFrecuencia  
=======================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsFrequency/LICENSE.md)  
Descripción global: **Frecuencia GTFS**  

## Lista de propiedades  

- `alternateName`: Un nombre alternativo para este artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Esta será normalmente asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `endTime`: Lo mismo que el GTFS "end_time  - `exactTimes`: Igual que el GTFS "tiempos_exactos" pero codificado como un booleano: "falso": Los viajes basados en la frecuencia no están exactamente programados. "Verdadero": Los viajes basados en la frecuencia están exactamente programados  - `hasTrip`: Viaje asociado a esta Entidad. Apuntará a una Entidad de tipo GtfsTrip  - `headwaySeconds`: Lo mismo que el GTFS "headway_secs  - `id`: Identificador único de la entidad  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `startTime`: Lo mismo que el GTFS "tiempo_de_inicio  - `type`: Tipo de entidad NGSI. Tiene que ser GtfsFrecuencia    
Propiedades requeridas  
- `endTime`  - `hasTrip`  - `headwaySeconds`  - `id`  - `startTime`  - `type`    
Ver [https://developers.google.com/transit/gtfs/reference/#frequenciestxt](https://developers.google.com/transit/gtfs/reference/#frequenciestxt)  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsFrequency:    
  description: 'GTFS Frequency'    
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
    endTime:    
      description: 'Same as GTFS `end_time`'    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    exactTimes:    
      description: 'Same as GTFS `exact_times` but encoded as a Boolean: `false`: Frequency-based trips are not exactly scheduled. `true`: Frequency-based trips are exactly scheduled'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    hasTrip:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Trip associated to this Entity. It shall point to an Entity of Type GtfsTrip'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    headwaySeconds:    
      description: 'Same as GTFS `headway_secs`'    
      minValue: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    id:    
      anyOf: &gtfsfrequency_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *gtfsfrequency_-_properties_-_owner_-_items_-_anyof    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    startTime:    
      description: 'Same as GTFS `start_time`'    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI Entity type. It has to be GtfsFrequency'    
      enum:    
        - GtfsFrequency    
      type: Property    
  required:    
    - id    
    - type    
    - hasTrip    
    - startTime    
    - endTime    
    - headwaySeconds    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### GtfsFrecuencia NGSI V2 valores clave Ejemplo  
Aquí hay un ejemplo de una frecuencia Gtfs en formato JSON como valores clave. Esto es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
  "type": "GtfsFrequency",  
  "name": "Laborables",  
  "description": "Cada 10 minutos",  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
  "startTime": "07:00:00",  
  "endTime": "10:25:00",  
  "headwaySeconds": 600  
}  
```  
#### GtfsFrecuencia NGSI V2 normalizada Ejemplo  
Aquí hay un ejemplo de una frecuencia GtfsFrecuencia en formato JSON como normalizada. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
  "type": "GtfsFrequency",  
  "description": {  
    "value": "Cada 10 minutos"  
  },  
  "hasTrip": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1"  
  },  
  "headwaySeconds": {  
    "value": 600  
  },  
  "startTime": {  
    "value": "07:00:00"  
  },  
  "endTime": {  
    "value": "10:25:00"  
  },  
  "name": {  
    "value": "Laborables"  
  }  
}  
```  
#### GtfsFrecuencia NGSI-LD valores clave Ejemplo  
Aquí hay un ejemplo de una frecuencia Gtfs en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "description": "Cada 10 minutos",  
 "endTime": "10:25:00",  
 "hasTrip": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
 "headwaySeconds": 600,  
 "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
 "name": "Laborables",  
 "startTime": "07:00:00",  
 "type": "GtfsFrequency"}  
```  
#### GtfsFrecuencia NGSI-LD normalizada Ejemplo  
He aquí un ejemplo de una frecuencia Gtfs en formato JSON-LD normalizada. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
    "type": "GtfsFrequency",  
    "description": {  
        "type": "Property",  
        "value": "Cada 10 minutos"  
    },  
    "hasTrip": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1"  
    },  
    "headwaySeconds": {  
        "type": "Property",  
        "value": 600  
    },  
    "startTime": {  
        "type": "Property",  
        "value": "07:00:00"  
    },  
    "endTime": {  
        "type": "Property",  
        "value": "10:25:00"  
    },  
    "name": {  
        "type": "Property",  
        "value": "Laborables"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
