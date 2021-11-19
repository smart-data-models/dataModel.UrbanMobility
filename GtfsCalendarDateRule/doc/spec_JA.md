Entity:GtfsCalendarDateRule  
===========================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsCalendarDateRule/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**GTFSのカレンダー日付ルール**。  

## プロパティのリスト  

- `alternateName`: このアイテムの別称  - `appliesOn`: このルールが適用される日付（YYYY-MM-DD形式）です。GTFSの`date`フィールドから取得します。  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `exceptionType`: GTFSの`exception_type`フィールドと同じです。イナム:'1, 2'  - `hasService`: このルールが適用されるサービスservice_id`から派生したものです。  - `id`: エンティティのユニークな識別子  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type`: NGSI エンティティタイプ。GtfsCalendarDateRuleである必要があります。    
必須項目  
- `appliesOn`  - `exceptionType`  - `hasService`  - `id`  - `type`    
https://developers.google.com/transit/gtfs/reference/#calendar_datestxt](https://developers.google.com/transit/gtfs/reference/#calendar_datestxt)をご覧ください。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsCalendarDateRule:    
  description: 'GTFS Calendar Date Rule'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
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
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Service to which this rule applies to. Derived from `service_id`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
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
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfscalendardaterule_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
    type:    
      description: 'NGSI Entity Type: It has to be GtfsCalendarDateRule'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsCalendarDateRule/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/GtfsCalendarDateRule/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### GtfsCalendarDateRule NGSI-v2 key-values 例  
GtfsCalendarDateRuleをkey-valuesとしてJSON-LD形式で記述した例を示します。これは`options=keyValues`を用いた場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### GtfsCalendarDateRule NGSI-v2規格化例  
正規化されたJSON-LD形式のGtfsCalendarDateRuleの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### GtfsCalendarDateRule NGSI-LDのキーバリューの例。  
GtfsCalendarDateRuleをkey-valuesとしてJSON-LD形式で記述した例を示します。これは、`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### GtfsCalendarDateRule NGSI-LD 正規化された例。  
正規化されたJSON-LD形式のGtfsCalendarDateRuleの例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "appliesOn": "2018-03-19",  
  "exceptionType": "1",  
  "hasService": "urn:ngsi-ld:GtfsService:Malaga:FairArea_1",  
  "id": "urn:ngsi-ld:CalendarDateRule:Malaga:Rule67",  
  "name": "Rule Fair Area",  
  "type": "GtfsCalendarDateRule"  
}  
```  
