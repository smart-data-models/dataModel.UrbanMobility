<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティGtfsCalendarRule    
======================<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsCalendarRule/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**スマートデータモデル。GTFSカレンダールール**。    
バージョン: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `alternateName[string]`: この項目の別名  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `endDate[date]`: このルールの終了日を `YYYY-MM-DD` フォーマットで指定する。これは[calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)のフィールド `end_date` から取得できます。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `friday[boolean]`: GTFS `friday` と同じ。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `hasService[string]`: このルールが適用されるサービス。service_id` から派生したものである。  . Model: [https://schema.org/URL](https://schema.org/URL)- `id[*]`: エンティティの一意識別子  - `monday[boolean]`: GTFS `monday` と同じ。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `saturday[boolean]`: GTFS `saturday` と同じ。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `startDate[date]`: このルールの開始日を `YYYY-MM-DD` フォーマットで指定する。これは[calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)のフィールド `start_date` から取得できる。  . Model: [https://schema.org/Date](https://schema.org/Date)- `sunday[boolean]`: GTFS `sunday` と同じ。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `thursday[boolean]`: GTFS `thursday` と同じ。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `tuesday[boolean]`: GTFS `tuesday` と同じ。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `type[string]`: NGSIエンティティタイプ：GtfsCalendarRule でなければならない。  - `wednesday[boolean]`: GTFS `wednesday` と同じ。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `endDate`  - `friday`  - `hasService`  - `id`  - `monday`  - `saturday`  - `startDate`  - `sunday`  - `thursday`  - `tuesday`  - `type`  - `wednesday`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
参照[https://developers.google.com/transit/gtfs/reference/#calendartxt](https://developers.google.com/transit/gtfs/reference/#calendartxt)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
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
## ペイロードの例    
#### GtfsCalendarRule NGSI-v2 キー値の例    
GtfsCalendarRuleをJSON-LD形式でkey-valuesとした例です。options=keyValues`を使うとNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
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
#### GtfsCalendarRule NGSI-v2 正規化例    
JSON-LD形式のGtfsCalendarRuleを正規化した例です。これはNGSI-v2と互換性があり、オプションを使用しない場合は個々のエンティティのコンテキストデータを返します。    
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
#### GtfsCalendarRule NGSI-LD キー値の例    
GtfsCalendarRuleをJSON-LD形式でkey-valuesとした例です。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
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
#### GtfsCalendarRule NGSI-LD 正規化例    
JSON-LD形式のGtfsCalendarRuleを正規化した例です。これは、オプションを使わない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
