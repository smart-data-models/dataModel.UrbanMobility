Entidad: GtfsStopTime  
=====================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsStopTime/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Tiempo de parada del GTFS**  

## Lista de propiedades  

- `alternateName`: Un nombre alternativo para este artículo  - `arrivalTime`: Igual que el GTFS `arrival_time`.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `departureTime`: Igual que el GTFS "hora de salida".  - `description`: Una descripción de este artículo  - `distanceTravelled`: Igual que GTFS "shape_dist_traveled".  - `dropOffType`: Igual que GTFS `drop_off_type`. Enum:'0, 1, 2, 3'  - `hasStop`: Igual que GTFS `stop_id`. Deberá apuntar a una Entidad de tipo GtfsStop  - `hasTrip`: Viaje asociado a esta Entidad. Apuntará a una entidad de tipo GtfsTrip  - `id`: Identificador único de la entidad  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `pickupType`: Igual que GTFS `pickup_type`. Enum:'0, 1, 2, 3'  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `stopHeadsign`: Igual que GTFS `stop_headsign`.  - `stopSequence`: Igual que GTFS `stop_sequence`. Comienza con `1`.  - `timepoint`: Igual que GTFS `timepoint`. Enum:'0, 1'  - `type`: Tipo de entidad NGSI. Debe ser GtfsStopTime    
Propiedades requeridas  
- `arrivalTime`  - `departureTime`  - `hasStop`  - `hasTrip`  - `id`  - `stopSequence`  - `type`    
Véase [https://developers.google.com/transit/gtfs/reference/#stop_timestxt](https://developers.google.com/transit/gtfs/reference/#stop_timestxt)  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsStopTime:    
  description: 'GTFS Stop Time'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    arrivalTime:    
      description: 'Same as GTFS `arrival_time`'    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
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
    departureTime:    
      description: 'Same as GTFS `departure_time`'    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    description:    
      description: 'A description of this item'    
      type: Property    
    distanceTravelled:    
      description: 'Same as GTFS `shape_dist_traveled`'    
      minValue: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    dropOffType:    
      default: 0    
      description: 'Same as GTFS `drop_off_type`. Enum:''0, 1, 2, 3'''    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    hasStop:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Same as GTFS `stop_id`. It shall point to an Entity of type GtfsStop'    
      type: Relationship    
      x-ngsi:    
        model: http://schema.org/URL    
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
    id:    
      anyOf: &gtfsstoptime_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *gtfsstoptime_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pickupType:    
      default: 0    
      description: 'Same as GTFS `pickup_type`. Enum:''0, 1, 2, 3'' '    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    stopHeadsign:    
      description: 'Same as GTFS `stop_headsign`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
    stopSequence:    
      description: 'Same as GTFS `stop_sequence`. Starting with `1`.'    
      minValue: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Integer    
    timepoint:    
      default: 1    
      description: 'Same as GTFS `timepoint`. Enum:''0, 1'''    
      enum:    
        - 0    
        - 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI Entity type. It has to be GtfsStopTime'    
      enum:    
        - GtfsStopTime    
      type: Property    
  required:    
    - id    
    - type    
    - arrivalTime    
    - departureTime    
    - hasStop    
    - hasTrip    
    - stopSequence    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### GtfsStopTime NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un GtfsStopTime en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
  "type": "GtfsStopTime",  
  "hasStop": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737",  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011",  
  "distanceTravelled": 759,  
  "stopSequence": 4,  
  "arrivalTime": "07:04:24",  
  "departureTime": "07:04:24"  
}  
```  
#### GtfsStopTime NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un GtfsStopTime en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
  "type": "GtfsStopTime",  
  "departureTime": {  
    "value": "07:04:24"  
  },  
  "hasTrip": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011"  
  },  
  "stopSequence": {  
    "value": 4  
  },  
  "distanceTravelled": {  
    "value": 759  
  },  
  "arrivalTime": {  
    "value": "07:04:24"  
  },  
  "hasStop": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737"  
  }  
}  
```  
#### GtfsStopTime NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un GtfsStopTime en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
  "type": "GtfsStopTime",  
  "departureTime": {  
    "type": "Property",  
    "value": "07:04:24"  
  },  
  "hasTrip": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011"  
  },  
  "stopSequence": {  
    "type": "Property",  
    "value": 4  
  },  
  "distanceTravelled": {  
    "type": "Property",  
    "value": 759  
  },  
  "arrivalTime": {  
    "type": "Property",  
    "value": "07:04:24"  
  },  
  "hasStop": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### GtfsStopTime NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un GtfsStopTime en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "arrivalTime": "07:04:24",  
  "departureTime": "07:04:24",  
  "distanceTravelled": 759,  
  "hasStop": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737",  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011",  
  "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
  "stopSequence": 4,  
  "type": "GtfsStopTime"  
}  
```  
