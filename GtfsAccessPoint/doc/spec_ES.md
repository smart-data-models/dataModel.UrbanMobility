Entidad: GtfsAccessPoint  
========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsAccessPoint/LICENSE.md)  
Descripción global: **Punto de acceso a GTFS**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `code`: Igual que el código de parada de GTFS.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Esta será normalmente asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `hasParentStation`: Lo mismo que la "estación_paterna" de GTFS.  - `hasService`: Servicio al que se aplica esta regla. Derivado de `service_id`  - `hasStop`: Apuntará a una entidad de tipo GtfsStop  - `hasTrip`: Viaje asociado a esta Entidad. Apuntará a una Entidad de tipo GtfsTrip  - `id`: Identificador único de la entidad  - `location`:   - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `page`: Igual que GTFS `stop_url`  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `stop_desc`: Igual que GTFS `stop_desc`.  - `type`: Tipo de entidad NGSI: Tiene que ser GtfsAccessPoint  - `wheelChairAccessible`: Lo mismo que el GTFS "wheelchair_boarding". Enum:'0, 1 ,2'. Referencia en [GTFS](https://developers.google.com/transit/gtfs/reference/#stopstxt)  - `zoneCode`: Zona de transporte a la que pertenece esta parada. Igual que la "zona_id" del GTFS    
Propiedades requeridas  
- `id`  - `location`  - `name`  - `type`    
Véase [https://developers.google.com/transit/gtfs/reference/#stopstxt](https://developers.google.com/transit/gtfs/reference/#stopstxt). Es un "stop" del GTFS cuyo "tipo_de_localización" es igual a "2".  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsAccessPoint:    
  description: 'GTFS Access Point'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    code:    
      description: 'Same as GTFS `stop_code`'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
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
    hasParentStation:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Same as GTFS `parent_station`.'    
      type: Relationship    
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
      description: 'It shall point to an Entity of Type GtfsStop'    
      type: Relationship    
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
      anyOf: &gtfsaccesspoint_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *gtfsaccesspoint_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    page:    
      description: 'Same as GTFS `stop_url`'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: http://schema.org/URL    
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
    stop_desc:    
      description: 'Same as GTFS `stop_desc`.'    
      type: Property    
    type:    
      description: 'NGSI Entity Type: It has to be GtfsAccessPoint'    
      enum:    
        - GtfsAccessPoint    
      type: Property    
    wheelChairAccessible:    
      description: "Same as GTFS `wheelchair_boarding`. Enum:'0, 1 ,2'. Reference in [GTFS](https://developers.google.com/transit/gtfs/reference/#stopstxt) "    
      enum:    
        - 0    
        - 1    
        - 2    
      type: Property    
    zoneCode:    
      description: 'Transport zone to which this stop belongs to. Same as GTFS `zone_id`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
  required:    
    - id    
    - type    
    - name    
    - location    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### Ejemplo de valores clave de GtfsAccessPoint NGSI V2  
Aquí hay un ejemplo de un GtfsAccessPoint en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:AccessPoint:Madrid:acc_4_1_3",  
  "type": "GtfsAccessPoint",  
  "name": "Bravo Murillo",  
  "location": {  
    "type": "Point",  
    "coordinates": [-3.69036, 40.46629]  
  },  
  "address": {  
    "type": "PostalAddress",  
    "streetAddress": "Calle de Bravo Murillo 377",  
    "addressLocality": "Madrid",  
    "addressCountry": "ES"  
  },  
  "hasParentStation": "urn:ngsi-ld:Gtfstation:Madrid:est_90_21"  
}  
```  
#### GtfsAccessPoint NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un GtfsAccessPoint en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:AccessPoint:Madrid:acc_4_1_3",  
  "type": "GtfsAccessPoint",  
  "name": {  
    "value": "Bravo Murillo"  
  },  
  "hasParentStation": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsStation:Madrid:est_90_21"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-3.69036, 40.46629]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Madrid",  
      "addressCountry": "ES",  
      "streetAddress": "Calle de Bravo Murillo 377",  
      "type": "PostalAddress"  
    }  
  }  
}  
```  
#### GtfsAccessPoint NGSI-LD key-values Example  
Aquí hay un ejemplo de un GtfsAccessPoint en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "address": {"addressCountry": "ES",  
             "addressLocality": "Madrid",  
             "streetAddress": "Calle de Bravo Murillo 377",  
             "type": "PostalAddress"},  
 "hasParentStation": "urn:ngsi-ld:GtfsStation:Madrid:est_90_21",  
 "id": "urn:ngsi-ld:AccessPoint:Madrid:acc_4_1_3",  
 "location": {"coordinates": [-3.69036, 40.46629], "type": "Point"},  
 "name": "Bravo Murillo",  
 "type": "GtfsAccessPoint"}  
```  
#### GtfsAccessPoint NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un GtfsAccessPoint en formato JSON-LD normalizado. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:AccessPoint:Madrid:acc_4_1_3",  
    "type": "GtfsAccessPoint",  
    "name": {  
        "type": "Property",  
        "value": "Bravo Murillo"  
    },  
    "hasParentStation": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsStation:Madrid:est_90_21"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -3.69036,  
                40.46629  
            ]  
        }  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressLocality": "Madrid",  
            "addressCountry": "ES",  
            "streetAddress": "Calle de Bravo Murillo 377",  
            "type": "PostalAddress"  
        }  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
