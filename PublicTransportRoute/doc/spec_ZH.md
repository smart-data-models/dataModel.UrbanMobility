<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。公共交通路线（PublicTransportRoute  
==============================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/PublicTransportRoute/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**一条普通的公共交通路线**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `routeCode[string]`: 航线的ID或代码（如HT5200104000）。  . Model: [ https://schema.org/Text.]( https://schema.org/Text.)- `routeColor[string]`: 文本中分配给路线的颜色  . Model: [ https://schema.org/color.]( https://schema.org/color.)- `routeSegments[array]`: 这条路线的部分路段由其名称和站点定义。  - `routeTextColor[string]`: 分配给路线的颜色，以十六进制表示  . Model: [ https://schema.org/color.]( https://schema.org/color.)- `schedule[array]`: 该路线的工作时间  . Model: [https://schema.org/OpeningHoursSpecification.](https://schema.org/OpeningHoursSpecification.)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `shortRouteCode[string]`: 航线ID/代码的简称（如5200104000）。  . Model: [https://schema.org/Text.](https://schema.org/Text.)- `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `transportationType[integer]`: 使用该站的公共交通类型，定义在(https://developers.google.com/transit/gtfs/reference/#routestxt)。枚举：'0，1，2，3，4，5，6，7'  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI实体类型。它必须是PublicTransportRoute  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `transportationType`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
公共交通路线的通用模型。它采用了一些GTFS的定义，但它不需要与额外的GTFS数据相联系。一条路线是由一个公共交通服务提供的，经过一组站点的旅程。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *publictransportroute_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    routeCode:    
      description: 'ID or code of the route (e.g. HT5200104000)'    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/Text.'    
        type: Property    
    routeColor:    
      description: 'Color assigned to route in text'    
      pattern: "^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$"    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/color.'    
        type: Property    
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
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    routeTextColor:    
      description: 'Color assigned to route in hexadecimal'    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/color.'    
        type: Property    
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
        type: object    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/OpeningHoursSpecification.    
        type: Property    
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
      x-ngsi:    
        type: Property    
    shortRouteCode:    
      description: 'Shorter form of the ID/code of the route (e.g. 5200104000)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
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
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be PublicTransportRoute'    
      enum:    
        - PublicTransportRoute    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - transportationType    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/PublicTransportRoute/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/PublicTransportRoute/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### PublicTransportRoute NGSI-v2关键值示例  
这里有一个JSON-LD格式的PublicTransportRoute作为key-values的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### PublicTransportRoute NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的PublicTransportRoute的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### PublicTransportRoute NGSI-LD关键值示例  
这里有一个JSON-LD格式的PublicTransportRoute作为key-values的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json
{
    "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",
    "type": "PublicTransportRoute",
    "dataProvider": {
        "type": "Text",
        "value": "http://www.smartsantander.eu/"
    },
    "name": {
        "type": "Text",
        "value": "PE\u00d1ACASTILLO-PLAZA DE ITALIA"
    },
    "routeCode": {
        "type": "Text",
        "value": "5200103000"
    },
    "routeColor": {
        "type": "Text",
        "value": "#ff0000"
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
    "routeTextColor": {
        "type": "Text",
        "value": "RED"
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
    "shortRouteCode": {
        "type": "Text",
        "value": "N3"
    },
    "source": {
        "type": "Text",
        "value": "https://api.smartsantander.eu/"
    },
    "transportationType": {
        "type": "Number",
        "value": 3
    },
    "@context": [
        "https://smart-data-models.github.io/data-models/context.jsonld",
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"
    ]
}
```  
</details>  
#### PublicTransportRoute NGSI-LD规范化示例  
下面是一个以JSON-LD格式规范化的PublicTransportRoute的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json
{
    "id": "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",
    "type": "PublicTransportRoute",
    "dataProvider": "http://www.smartsantander.eu/",
    "entityVersion": 2.0,
    "name": {
        "type": "Property",
        "value": "PE\u00d1ACASTILLO-PLAZA DE ITALIA "
    },
    "routeCode": {
        "type": "Property",
        "value": "5200103000"
    },
    "routeColor": {
        "type": "Property",
        "value": "#ff0000"
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
    "routeTextColor": {
        "type": "Property",
        "value": "RED"
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
    },
    "shortRouteCode": {
        "type": "Property",
        "value": "N3"
    },
    "source": "https://api.smartsantander.eu/",
    "transportationType": {
        "type": "Property",
        "value": 3
    },
    "@context": [
        "https://smart-data-models.github.io/data-models/context.jsonld",
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"
    ]
}
```
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
