<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：GtfsCalendarDateRule    
=======================<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsCalendarDateRule/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**GTFS 日历日期规则**    
版本： 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `alternateName[string]`: 该项目的替代名称  - `appliesOn[date]`: 本规则适用的日期（YYYY-MM-DD 格式）。它应从 GTFS 的 "日期 "字段中获取  . Model: [https://schema.org/Date](https://schema.org/Date)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `exceptionType[string]`: 与 GTFS `exception_type` 字段相同。枚举：'1, 2  . Model: [https://schema.org/Text](https://schema.org/Text)- `hasService[string]`: 本规则适用的服务。源自 `service_id`  . Model: [https://schema.org/URL](https://schema.org/URL)- `id[*]`: 实体的唯一标识符  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 实体类型：必须是 GtfsCalendarDateRule。枚举:'GtfsCalendarDateRule  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `appliesOn`  - `exceptionType`  - `hasService`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
见 [https://developers.google.com/transit/gtfs/reference/#calendar_datestxt](https://developers.google.com/transit/gtfs/reference/#calendar_datestxt)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
GtfsCalendarDateRule:      
  description: GTFS Calendar Date Rule      
  properties:      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    appliesOn:      
      description: ' Date (in YYYY-MM-DD format) this rule applies to. It shall be obtained from the GTFS `date` field'      
      format: date      
      type: string      
      x-ngsi:      
        model: https://schema.org/Date      
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
    exceptionType:      
      description: 'Same as GTFS `exception_type` field. Enum:''1, 2'''      
      enum:      
        - 1      
        - 2      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
    type:      
      description: 'NGSI Entity Type: It has to be GtfsCalendarDateRule. Enum:''GtfsCalendarDateRule'''      
      enum:      
        - GtfsCalendarDateRule      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - hasService      
    - appliesOn      
    - exceptionType      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsCalendarDateRule/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/GtfsCalendarDateRule/schema.json      
  x-model-tags: ""      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### GtfsCalendarDateRule NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 GtfsCalendarDateRule 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CalendarDateRule:Malaga:Rule67",  
  "type": "GtfsCalendarDateRule",  
  "name": "Rule Fair Area",  
  "hasService": "urn:ngsi-ld:GtfsService:Malaga:FairArea_1",  
  "appliesOn": "2018-03-19",  
  "exceptionType": "1"  
}  
```  
</details>    
#### GtfsCalendarDateRule NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 GtfsCalendarDateRule 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CalendarDateRule:Malaga:Rule67",  
  "type": "GtfsCalendarDateRule",  
  "name": {  
    "type": "Text",  
    "value": "Rule Fair Area"  
  },  
  "exceptionType": {  
    "type": "Text",  
    "value": "1"  
  },  
  "hasService": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:GtfsService:Malaga:FairArea_1"  
  },  
  "appliesOn": {  
    "type": "DateTime",  
    "value": "2018-03-19"  
  }  
}  
```  
</details>    
#### GtfsCalendarDateRule NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 GtfsCalendarDateRule 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CalendarDateRule:Malaga:Rule67",  
  "type": "GtfsCalendarDateRule",  
  "appliesOn": "2018-03-19",  
  "exceptionType": "1",  
  "hasService": "urn:ngsi-ld:GtfsService:Malaga:FairArea_1",  
  "name": "Rule Fair Area",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### GtfsCalendarDateRule NGSI-LD 规范化示例    
下面是一个规范化 JSON-LD 格式的 GtfsCalendarDateRule 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:CalendarDateRule:Malaga:Rule67",  
    "type": "GtfsCalendarDateRule",  
    "appliesOn": {  
        "type": "Property",  
        "value": "2018-03-19"  
    },  
    "exceptionType": {  
        "type": "Property",  
        "value": "1"  
    },  
    "hasService": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsService:Malaga:FairArea_1"  
    },  
    "name": {  
        "type": "Property",  
        "value": "Rule Fair Area"  
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
