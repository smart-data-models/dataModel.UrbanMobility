<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：GtfsCalendarRule    
===================<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsCalendarRule/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球描述：**智能数据模型。GTFS 日历规则**    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `alternateName[string]`: 该项目的替代名称  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `endDate[date]`: 该规则的结束日期，格式为 `YYYY-MM-DD`。可从 [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt) 中的字段 `end_date` 中获取。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `friday[boolean]`: 与 GTFS`friday` 相同  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `hasService[string]`: 本规则适用的服务。源自 `service_id`  . Model: [https://schema.org/URL](https://schema.org/URL)- `id[*]`: 实体的唯一标识符  - `monday[boolean]`: 与 GTFS `monday` 相同  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `saturday[boolean]`: 与 GTFS "星期六 "相同  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `startDate[date]`: 该规则的开始日期，格式为 `YYYY-MM-DD`。它可以从 [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt) 的字段 `start_date` 中获取。  . Model: [https://schema.org/Date](https://schema.org/Date)- `sunday[boolean]`: 与 GTFS`sunday` 相同  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `thursday[boolean]`: 与 GTFS`thursday` 相同  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `tuesday[boolean]`: 与 GTFS`tuesday` 相同  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `type[string]`: NGSI 实体类型：必须是 GtfsCalendarRule  - `wednesday[boolean]`: 与 GTFS "星期三 "相同  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `endDate`  - `friday`  - `hasService`  - `id`  - `monday`  - `saturday`  - `startDate`  - `sunday`  - `thursday`  - `tuesday`  - `type`  - `wednesday`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
见 [https://developers.google.com/transit/gtfs/reference/#calendartxt](https://developers.google.com/transit/gtfs/reference/#calendartxt)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
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
## 有效载荷示例    
#### GtfsCalendarRule NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 GtfsCalendarRule 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### GtfsCalendarRule NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 GtfsCalendarRule 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### GtfsCalendarRule NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 GtfsCalendarRule 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
#### GtfsCalendarRule NGSI-LD 规范化示例    
下面是一个规范化 JSON-LD 格式的 GtfsCalendarRule 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
