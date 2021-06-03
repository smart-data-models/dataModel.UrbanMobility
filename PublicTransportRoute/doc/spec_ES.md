Entidad: PublicTransportRoute  
=============================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/PublicTransportRoute/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Una ruta genérica de transporte público**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `location`:   - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `routeCode`: ID o código de la ruta (por ejemplo, "HT5200104000")  - `routeColor`: Color asignado a la ruta en el texto  - `routeSegments`: Tramos de esta ruta definidos por su nombre y paradas.  - `routeTextColor`: Color asignado a la ruta en hexadecimal  - `schedule`: Horario de trabajo de esta ruta  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `shortRouteCode`: Forma abreviada del ID/código de la ruta (por ejemplo, "5200104000")  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `transportationType`: Tipos de transporte público que utilizan esta parada, tal como se define en (https://developers.google.com/transit/gtfs/reference/#routestxt). Enum:'0, 1, 2, 3, 4, 5, 6, 7'  - `type`: Tipo de entidad NGSI. Debe ser PublicTransportRoute    
Propiedades requeridas  
- `id`  - `transportationType`  - `type`    
Modelo genérico de ruta de transporte público. Adopta algunas definiciones del GTFS, pero no necesita estar vinculado a datos adicionales del GTFS. Una ruta es un viaje, ofrecido por un servicio de transporte público, que pasa por un conjunto de paradas.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PublicTransportRoute:    
  description: 'A generic public transport route'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
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
    id:    
      anyOf: &publictransportroute_-_properties_-_owner_-_items_-_anyof    
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
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *publictransportroute_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    routeCode:    
      description: 'ID or code of the route (e.g. ‘HT5200104000’)'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text.'    
    routeColor:    
      description: 'Color assigned to route in text'    
      pattern: "^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$"    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/color.'    
    routeSegments:    
      description: 'Segments of this route defined by their name and stops.'    
      items:    
        properties:    
          refPublicTransportStops:    
            items:    
              format: uri    
              type: string    
            type: array    
          segmentName:    
            type: string    
        required:    
          - segmentName    
          - refPublicTransportStops    
        type: object    
      type: Property    
    routeTextColor:    
      description: 'Color assigned to route in hexadecimal'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/color.'    
    schedule:    
      description: 'Working hours of this route'    
      items:    
        properties:    
          closes:    
            pattern: "[0-9]{2}:[0-9]{2}"    
            type: string    
          dayOfWeek:    
            enum:    
              - Friday    
              - Monday    
              - PublicHolidays    
              - Saturday    
              - Sunday    
              - Thursday    
              - Tuesday    
              - Wednesday    
            type: string    
          opens:    
            pattern: "[0-9]{2}:[0-9]{2}"    
            type: string    
      minItems: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/OpeningHoursSpecification.    
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
    shortRouteCode:    
      description: 'Shorter form of the ID/code of the route (e.g. ‘5200104000’’)'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    transportationType:    
      description: "Types of public transport using this stop as defined in (https://developers.google.com/transit/gtfs/reference/#routestxt). Enum:'0, 1, 2, 3, 4, 5, 6, 7'"    
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
        model: https://schema.org/Number    
    type:    
      description: 'NGSI Entity type. It has to be PublicTransportRoute'    
      enum:    
        - PublicTransportRoute    
      type: Property    
  required:    
    - id    
    - type    
    - transportationType    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### PublicTransportRoute NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un PublicTransportRoute en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
  "type": "PublicTransportRoute",  
  "source": "https://api.smartsantander.eu/",  
  "dataProvider": "http://www.smartsantander.eu/",  
  "routeCode": "5200103000",  
  "shortRouteCode": "N3",  
  "name": "PEÑACASTILLO-PLAZA DE ITALIA ",  
  "transportationType": 3,  
  "routeColor": "#ff0000",  
  "routeTextColor": "RED",  
  "routeSegments": [  
    {  
      "segmentName": "PEÑACASTILLO-PLAZA DE ITALIA:1",  
      "refPublicTransportStops": [  
        "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:311",  
        "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:129"  
      ]  
    },  
    {  
      "segmentName": "PEÑACASTILLO-PLAZA DE ITALIA:2",  
      "refPublicTransportStops": [  
        "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:130",  
        "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:131"  
      ]  
    }  
  ],  
  "schedule": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "09:00",  
      "closes": "23:00"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "09:00",  
      "closes": "23:00"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "09:00",  
      "closes": "23:00"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "09:00",  
      "closes": "23:00"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "09:00",  
      "closes": "23:00"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "09:00",  
      "closes": "14:00"  
    }  
  ]  
}  
```  
#### PublicTransportRoute NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de una PublicTransportRoute en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
  "type": "PublicTransportRoute",  
  "source": {  
    "type": "Text",  
    "value": "https://api.smartsantander.eu/"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "http://www.smartsantander.eu/"  
  },  
  "routeCode": {  
    "type": "Text",  
    "value": "5200103000"  
  },  
  "shortRouteCode": {  
    "type": "Text",  
    "value": "N3"  
  },  
  "name": {  
    "type": "Text",  
    "value": "PEÑACASTILLO-PLAZA DE ITALIA"  
  },  
  "transportationType": {  
    "type": "Number",  
    "value": 3  
  },  
  "routeColor": {  
    "type": "Text",  
    "value": "#ff0000"  
  },  
  "routeTextColor": {  
    "type": "Text",  
    "value": "RED"  
  },  
  "routeSegments": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "segmentName": "PEÑACASTILLO-PLAZA DE ITALIA:1",  
        "refPublicTransportStops": [  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:311",  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:129"  
        ]  
      },  
      {  
        "segmentName": "PEÑACASTILLO-PLAZA DE ITALIA:2",  
        "refPublicTransportStops": [  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:130",  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:131"  
        ]  
      }  
    ]  
  },  
  "schedule": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "validFrom": "2018-01-24",  
        "validThrough": "2018-05-25",  
        "opens": "09:00",  
        "closes": "23:00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "09:00",  
        "closes": "14:00"  
      }  
    ]  
  }  
}  
```  
#### PublicTransportRoute NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un PublicTransportRoute en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
  "type": "PublicTransportRoute",  
  "source": {  
    "type": "Text",  
    "value": "https://api.smartsantander.eu/"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "http://www.smartsantander.eu/"  
  },  
  "routeCode": {  
    "type": "Text",  
    "value": "5200103000"  
  },  
  "shortRouteCode": {  
    "type": "Text",  
    "value": "N3"  
  },  
  "name": {  
    "type": "Text",  
    "value": "PE\u00d1ACASTILLO-PLAZA DE ITALIA"  
  },  
  "transportationType": {  
    "type": "Number",  
    "value": 3  
  },  
  "routeColor": {  
    "type": "Text",  
    "value": "#ff0000"  
  },  
  "routeTextColor": {  
    "type": "Text",  
    "value": "RED"  
  },  
  "routeSegments": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "segmentName": "PE\u00d1ACASTILLO-PLAZA DE ITALIA:1",  
        "refPublicTransportStops": [  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:311",  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:129"  
        ]  
      },  
      {  
        "segmentName": "PE\u00d1ACASTILLO-PLAZA DE ITALIA:2",  
        "refPublicTransportStops": [  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:130",  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:131"  
        ]  
      }  
    ]  
  },  
  "schedule": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "validFrom": "2018-01-24",  
        "validThrough": "2018-05-25",  
        "opens": "09:00",  
        "closes": "23:00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "09:00",  
        "closes": "14:00"  
      }  
    ]  
  },  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### PublicTransportRoute NGSI-LD normalizado Ejemplo  
Este es un ejemplo de una PublicTransportRoute en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
  "type": "PublicTransportRoute",  
  "source": "https://api.smartsantander.eu/",  
  "dataProvider": "http://www.smartsantander.eu/",  
  "entityVersion": 2.0,  
  "routeCode": {  
    "type": "Property",  
    "value": "5200103000"  
  },  
  "shortRouteCode": {  
    "type": "Property",  
    "value": "N3"  
  },  
  "name": {  
    "type": "Property",  
    "value": "PE\u00d1ACASTILLO-PLAZA DE ITALIA "  
  },  
  "transportationType": {  
    "type": "Property",  
    "value": 3  
  },  
  "routeColor": {  
    "type": "Property",  
    "value": "#ff0000"  
  },  
  "routeTextColor": {  
    "type": "Property",  
    "value": "RED"  
  },  
  "routeSegments": {  
    "type": "Property",  
    "value": [  
      {  
        "segmentName": "PE\u00d1ACASTILLO-PLAZA DE ITALIA:1",  
        "refPublicTransportStops": [  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:311",  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:129"  
        ]  
      },  
      {  
        "segmentName": "PE\u00d1ACASTILLO-PLAZA DE ITALIA:2",  
        "refPublicTransportStops": [  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:130",  
          "urn:ngsi-ld:PublicTransportStop:santander:transport:busStop:131"  
        ]  
      }  
    ]  
  },  
  "schedule": {  
    "type": "Property",  
    "value": [  
      {  
        "validFrom": "2018-01-24",  
        "validThrough": "2018-05-25",  
        "opens": "09:00",  
        "closes": "23:00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "09:00",  
        "closes": "14:00"  
      }  
    ]  
  }  
}  
```  
