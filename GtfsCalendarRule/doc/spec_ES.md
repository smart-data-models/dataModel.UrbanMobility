<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: GtfsCalendarRule    
=========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsCalendarRule/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Modelos de datos inteligentes. Regla de calendario GTFS**    
versión: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `endDate[date]`: Fecha final de esta regla en formato `YYYY-MM-DD`. Se puede obtener del campo `end_date` de [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `friday[boolean]`: Igual que GTFS `viernes  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `hasService[string]`: Servicio al que se aplica esta regla. Derivado de `service_id`.  . Model: [https://schema.org/URL](https://schema.org/URL)- `id[*]`: Identificador único de la entidad  - `monday[boolean]`: Igual que GTFS `monday`  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `saturday[boolean]`: Igual que GTFS `sábado  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `startDate[date]`: Fecha de inicio de esta regla en formato `YYYY-MM-DD`. Se puede obtener del campo `start_date` de [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)  . Model: [https://schema.org/Date](https://schema.org/Date)- `sunday[boolean]`: Igual que GTFS `sunday  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `thursday[boolean]`: Igual que GTFS `jueves  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `tuesday[boolean]`: Igual que GTFS `tuesday  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `type[string]`: Tipo de entidad NGSI: Tiene que ser GtfsCalendarRule  - `wednesday[boolean]`: Igual que GTFS "miércoles  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `endDate`  - `friday`  - `hasService`  - `id`  - `monday`  - `saturday`  - `startDate`  - `sunday`  - `thursday`  - `tuesday`  - `type`  - `wednesday`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Véase [https://developers.google.com/transit/gtfs/reference/#calendartxt](https://developers.google.com/transit/gtfs/reference/#calendartxt)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
GtfsCalendarRule:      
  description: Smart Data Models. GTFS Calendar Rule      
  properties:      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    endDate:      
      description: "End date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `end_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)"      
      format: date      
      type: string      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    friday:      
      description: Same as GTFS `friday`      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    hasService:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Service to which this rule applies to. Derived from `service_id`      
      type: string      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    monday:      
      description: Same as GTFS `monday`      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    saturday:      
      description: Same as GTFS `saturday`      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    startDate:      
      description: "Start date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `start_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)"      
      format: date      
      type: string      
      x-ngsi:      
        model: https://schema.org/Date      
        type: Property      
    sunday:      
      description: Same as GTFS `sunday`      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    thursday:      
      description: Same as GTFS `thursday`      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    tuesday:      
      description: Same as GTFS `tuesday`      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    type:      
      description: 'NGSI Entity Type: It has to be GtfsCalendarRule'      
      enum:      
        - GtfsCalendarRule      
      type: string      
      x-ngsi:      
        type: Property      
    wednesday:      
      description: Same as GTFS `wednesday`      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
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
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsCalendarRule/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/GtfsCalendarRule/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### GtfsCalendarRule NGSI-v2 key-values Ejemplo    
Aquí hay un ejemplo de un GtfsCalendarRule en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
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
</details>    
#### GtfsCalendarRule NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de GtfsCalendarRule en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "type": "GtfsCalendarRule",  
  "startDate": {  
    "type": "DateTime",  
    "value": "2018-01-01"  
  },  
  "endDate": {  
    "type": "DateTime",  
    "value": "2019-01-01"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Rule Hospital Service 1"  
  },  
  "monday": {  
    "type": "Boolean",  
    "value": true  
  },  
  "tuesday": {  
    "type": "Boolean",  
    "value": true  
  },  
  "friday": {  
    "type": "Boolean",  
    "value": true  
  },  
  "wednesday": {  
    "type": "Boolean",  
    "value": true  
  },  
  "thursday": {  
    "type": "Boolean",  
    "value": true  
  },  
  "sunday": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasService": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1"  
  },  
  "saturday": {  
    "type": "Boolean",  
    "value": false  
  }  
}  
```  
</details>    
#### GtfsCalendarRule NGSI-LD key-values Ejemplo    
Aquí hay un ejemplo de un GtfsCalendarRule en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "type": "GtfsCalendarRule",  
  "endDate": "2019-01-01",  
  "friday": true,  
  "hasService": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1",  
  "monday": true,  
  "name": "Rule Hospital Service 1",  
  "saturday": false,  
  "startDate": "2018-01-01",  
  "sunday": false,  
  "thursday": true,  
  "tuesday": true,  
  "wednesday": true,  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### GtfsCalendarRule NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de GtfsCalendarRule en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
    "type": "GtfsCalendarRule",  
    "endDate": {  
        "type": "Property",  
        "value": {  
            "@type": "Date",  
            "@value": "2019-01-01"  
        }  
    },  
    "friday": {  
        "type": "Property",  
        "value": true  
    },  
    "hasService": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1"  
    },  
    "monday": {  
        "type": "Property",  
        "value": true  
    },  
    "name": {  
        "type": "Property",  
        "value": "Rule Hospital Service 1"  
    },  
    "saturday": {  
        "type": "Property",  
        "value": false  
    },  
    "startDate": {  
        "type": "Property",  
        "value": {  
            "@type": "Date",  
            "@value": "2018-01-01"  
        }  
    },  
    "sunday": {  
        "type": "Property",  
        "value": false  
    },  
    "thursday": {  
        "type": "Property",  
        "value": true  
    },  
    "tuesday": {  
        "type": "Property",  
        "value": true  
    },  
    "wednesday": {  
        "type": "Property",  
        "value": true  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
