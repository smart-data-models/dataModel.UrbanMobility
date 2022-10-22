<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。基金会机构  
========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsAgency/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**GTFS机构**  
版本：0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `addressCountry[string]`: 的国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)- `addressLocality[string]`: 街道地址所处的地区，并且是在该地区的地方  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)- `addressRegion[string]`: 该地所处的区域，以及该地在哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)- `agencyName[string]`: 与GTFS的 "机构名称 "相同  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: 这个项目的一个替代名称  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `entitySource[string]`: 提供实体数据原始来源的一连串字符作为URL。它应指向用于生成该实体的原始GTFS馈送的URL。  . Model: [https://schema.org/URL](https://schema.org/URL)- `id[*]`: 实体的唯一标识符  - `language[string]`: 与GTFS `agency_language`相同。见[GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `page[string]`: 与GTFS`stop_url`相同。  . Model: [http://schema.org/URL](http://schema.org/URL)- `phone[string]`: 与GFTS `agency_phone`相同。  . Model: [https://schema.org/Text](https://schema.org/Text)- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如，03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)- `postalCode[string]`: 邮政编码。例如，24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)- `timezone[string]`: 与GTFS `agency_timezone`相同。见[GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI实体类型。它必须是GtfsAgency。Enum:'GtfsAgency'（GtfsAgency）。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `agencyName`  - `id`  - `source`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
见[https://developers.google.com/transit/gtfs/reference/#agencytxt](https://developers.google.com/transit/gtfs/reference/#agencytxt)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsAgency:    
  description: 'GTFS Agency'    
  properties:    
    addressCountry:    
      description: 'The country. For example, Spain'    
      type: string    
      x-ngsi:    
        model: https://schema.org/addressCountry    
        type: Property    
    addressLocality:    
      description: 'The locality in which the street address is, and which is in the region'    
      type: string    
      x-ngsi:    
        model: https://schema.org/addressLocality    
        type: Property    
    addressRegion:    
      description: 'The region in which the locality is, and which is in the country'    
      type: string    
      x-ngsi:    
        model: https://schema.org/addressRegion    
        type: Property    
    agencyName:    
      description: 'Same as GTFS `agency_name`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
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
    entitySource:    
      description: 'A sequence of characters giving the original source of the Entity data as a URL. It shall point to the URL of the original GTFS feed used to generate this Entity'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    id:    
      anyOf: &gtfsagency_-_properties_-_owner_-_items_-_anyof    
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
    language:    
      description: "Same as GTFS `agency_language`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfsagency_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    page:    
      description: 'Same as GTFS `stop_url`'    
      format: uri    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Property    
    phone:    
      description: 'Same as GFTS `agency_phone`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    postOfficeBoxNumber:    
      description: 'The post office box number for PO box addresses. For example, 03578'    
      type: string    
      x-ngsi:    
        model: https://schema.org/postOfficeBoxNumber    
        type: Property    
    postalCode:    
      description: 'The postal code. For example, 24004'    
      type: string    
      x-ngsi:    
        model: https://schema.org/https://schema.org/postalCode    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    streetAddress:    
      description: 'The street address'    
      type: string    
      x-ngsi:    
        model: https://schema.org/streetAddress    
        type: Property    
    timezone:    
      description: "Same as GTFS `agency_timezone`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity Type: It has to be GtfsAgency. Enum:''GtfsAgency'''    
      enum:    
        - GtfsAgency    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - agencyName    
    - source    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsAgency/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.UrbanMobility/GtfsAgency/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### GtfsAgency NGSI-v2 key-values 示例  
下面是一个以JSON-LD格式作为关键值的GtfsAgency的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
  "type": "GtfsAgency",  
  "agencyName": "Empresa Malagueña de Transportes",  
  "page": "http://www.emtmalaga.es/",  
  "timezone": "Europe/Madrid",  
  "language": "ES",  
  "source": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52"  
}  
```  
</details>  
#### GtfsAgency NGSI-v2规范化示例  
下面是一个规范化的JSON-LD格式的GtfsAgency的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
  "type": "GtfsAgency",  
  "agencyName": {  
    "value": "Empresa Malague\u00f1a de Transportes"  
  },  
  "language": {  
    "value": "ES"  
  },  
  "page": {  
    "value": "http://www.emtmalaga.es/"  
  },  
  "source": {  
    "value": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52"  
  },  
  "timezone": {  
    "value": "Europe/Madrid"  
  }  
}  
```  
</details>  
#### GtfsAgency NGSI-LD 关键值示例  
这里是一个以JSON-LD格式作为关键值的GtfsAgency的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
    "type": "GtfsAgency",  
    "agencyName": {  
        "type": "Property",  
        "value": "Empresa Malague\u00f1a de Transportes"  
    },  
    "language": {  
        "type": "Property",  
        "value": "ES"  
    },  
    "page": {  
        "type": "Property",  
        "value": "http://www.emtmalaga.es/"  
    },  
    "source": {  
        "type": "Property",  
        "value": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52"  
    },  
    "timezone": {  
        "type": "Property",  
        "value": "Europe/Madrid"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### GtfsAgency NGSI-LD规范化示例  
下面是一个规范化的JSON-LD格式的GtfsAgency的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
    "type": "GtfsAgency",  
    "agencyName": "Empresa Malague\u00f1a de Transportes",  
    "language": "ES",  
    "page": "http://www.emtmalaga.es/",  
    "source": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52",  
    "timezone": "Europe/Madrid",  
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
