Entidad: GtfsCalendarDateRule  
=============================  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Regla de la fecha del calendario de la GTFS**  

## Lista de propiedades  

`alternateName`: Un nombre alternativo para este artículo  `appliesOn`:   `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `dateModified`: Sello de tiempo de la última modificación de la entidad. Esta será normalmente asignada por la plataforma de almacenamiento.  `description`: Una descripción de este artículo  `exceptionType`:   `hasService`:   `id`:   `name`: El nombre de este artículo.  `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  `seeAlso`:   `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  `type`: NGSI Tipo de entidad  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente  
```yaml  
GtfsCalendarDateRule:    
  description: 'GTFS Calendar Date Rule'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    appliesOn:    
      format: date    
      type: string    
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
    exceptionType:    
      enum:    
        - 1    
        - 2    
      type: string    
    hasService:    
      format: uri    
      type: string    
    id:    
      anyOf: &gtfscalendardaterule_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfscalendardaterule_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - GtfsCalendarDateRule    
      type: string    
  required:    
    - id    
    - type    
    - hasService    
    - appliesOn    
    - exceptionType    
  type: object    
```  
Aquí hay un ejemplo de una GtfsCalendarDateRule en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza `opciones=valores-clave` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:CalendarDateRule:Malaga:Rule67",  
  "type": "GtfsCalendarDateRule",  
  "name": "Rule Fair Area",  
  "hasService": "urn:ngsi-ld:Gtfservice:Malaga:FairArea_1",  
  "appliesOn": "2018-03-19",  
  "exceptionType": "1"  
}  
```  
He aquí un ejemplo de una GtfsCalendarDateRule en formato JSON normalizado. Es compatible con NGSI V2 cuando se utiliza `opciones=valores clave` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:CalendarDateRule:Malaga:Rule67",  
  "type": "GtfsCalendarDateRule",  
  "name": {  
    "value": "Rule Fair Area"  
  },  
  "exceptionType": {  
    "value": "1"  
  },  
  "hasService": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsService:Malaga:FairArea_1"  
  },  
  "appliesOn": {  
    "value": "2018-03-19"  
  }  
}  
```  
Aquí hay un ejemplo de una GtfsCalendarDateRule en formato JSON-LD como valores clave. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "appliesOn": "2018-03-19",  
 "exceptionType": "1",  
 "hasService": "urn:ngsi-ld:GtfsService:Malaga:FairArea_1",  
 "id": "urn:ngsi-ld:CalendarDateRule:Malaga:Rule67",  
 "name": "Rule Fair Area",  
 "type": "GtfsCalendarDateRule"}  
```  
He aquí un ejemplo de una GtfsCalendarDateRule en formato JSON-LD normalizado. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:CalendarDateRule:Malaga:Rule67",  
    "type": "GtfsCalendarDateRule",  
    "name": {  
        "type": "Property",  
        "value": "Rule Fair Area"  
    },  
    "exceptionType": {  
        "type": "Property",  
        "value": "1"  
    },  
    "hasService": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsService:Malaga:FairArea_1"  
    },  
    "appliesOn": {  
        "type": "Property",  
        "value": "2018-03-19"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
