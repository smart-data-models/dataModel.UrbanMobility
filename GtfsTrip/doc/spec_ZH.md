<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：旅程（GtfsTrip  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsTrip/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**GTFS之旅**  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `alternateName[string]`: 这个项目的一个替代名称  - `bikesAllowed[number]`: 与GTFS `bikes_allowed`相同。Enum:'0, 1, 2'.参见[GTFS](https://developers.google.com/transit/gtfs/reference/#tripstxt)  . Model: [https://schema.org/Number](https://schema.org/Number)- `block[string]`: 与GTFS `block_id`相同  . Model: [https://schema.org/Text.](https://schema.org/Text.)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `direction[number]`: 与GTFS `direction_id`相同。枚举:'0, 1'  . Model: [https://schema.org/Number](https://schema.org/Number)- `hasRoute[string]`: 与`route_id`相同。它应指向一个GtfsRoute类型的实体。  . Model: [http://schema.org/URL](http://schema.org/URL)- `hasService[*]`: 与GTFS `service_id`相同。它应指向一个GtfsService类型的实体。  . Model: [http://schema.org/URL](http://schema.org/URL)- `hasShape[*]`: 与GTFS `shape_id`相同。它应指向一个GtfsShape类型的实体。  . Model: [http://schema.org/URL](http://schema.org/URL)- `headSign[string]`: 与GTFS`trip_headsign`相同。  . Model: [https://schema.org/Text.](https://schema.org/Text.)- `id[*]`: 实体的唯一标识符  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `shortName[string]`: 与GTFS`trip_short_name`相同。  . Model: [https://schema.org/Text.](https://schema.org/Text.)- `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: NGSI实体类型。它必须是GtfsTrip  - `wheelChairAccessible[number]`: 与GTFS`wheelchair_accessible`相同。Enum:'0, 1, 2'。  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `hasRoute`  - `hasService`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
见[https://developers.google.com/transit/gtfs/reference/#tripstxt](https://developers.google.com/transit/gtfs/reference/#tripstxt)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsTrip:    
  description: GTFS Trip    
  properties:    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    bikesAllowed:    
      description: "Same as GTFS `bikes_allowed`. Enum:'0, 1, 2'. See [GTFS](https://developers.google.com/transit/gtfs/reference/#tripstxt)"    
      enum:    
        - 0    
        - 1    
        - 2    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    block:    
      description: Same as GTFS `block_id`    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    direction:    
      description: 'Same as GTFS `direction_id`. Enum:''0, 1'''    
      enum:    
        - 0    
        - 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    hasRoute:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Same as `route_id`. It shall point to an Entity of type GtfsRoute    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    hasService:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Same as GTFS `service_id`. It shall point to an Entity of type GtfsService    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    hasShape:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Same as GTFS `shape_id`. It shall point to an Entity of type GtfsShape    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    headSign:    
      description: Same as GTFS `trip_headsign`    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
        type: Property    
    id:    
      anyOf: &gtfstrip_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *gtfstrip_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
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
    shortName:    
      description: Same as GTFS `trip_short_name`    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be GtfsTrip    
      enum:    
        - GtfsTrip    
      type: string    
      x-ngsi:    
        type: Property    
    wheelChairAccessible:    
      description: 'Same as GTFS `wheelchair_accessible`. Enum:''0, 1, 2'''    
      enum:    
        - 0    
        - 1    
        - 2    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
    - hasRoute    
    - hasService    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsTrip/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/GtfsTrip/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### GtfsTrip NGSI-v2密钥值示例  
下面是一个以JSON-LD格式作为key-values的GtfsTrip的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### GtfsTrip NGSI-v2规范化示例  
下面是一个规范化的JSON-LD格式的GtfsTrip的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
  "type": "GtfsTrip",  
  "direction": {  
     "type": "Number",  
    "value": 0  
  },  
  "headSign": {  
    "type": "Text",  
    "value": "San Andr\u00e9s"  
  },  
  "hasRoute": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1"  
  },  
  "hasService": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:GtfsService:Malaga_LAB"  
  },  
  "hasShape": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:GtfsShape:Shape01"  
  }  
}  
```  
</details>  
#### GtfsTrip NGSI-LD密钥值示例  
下面是一个以JSON-LD格式作为key-values的GtfsTrip的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
    "type": "GtfsTrip",  
    "direction": 0,  
    "hasRoute": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
    "hasService": "urn:ngsi-ld:GtfsService:Malaga_LAB",  
    "hasShape": "urn:ngsi-ld:GtfsShape:Shape01",  
    "headSign": "San Andr\u00e9s",  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### GtfsTrip NGSI-LD规范化示例  
下面是一个规范化的JSON-LD格式的GtfsTrip的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
    "type": "GtfsTrip",  
    "direction": {  
        "type": "Property",  
        "value": 0  
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
    "headSign": {  
        "type": "Property",  
        "value": "San Andr\u00e9s"  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
