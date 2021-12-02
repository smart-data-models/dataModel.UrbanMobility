エンティティGtfsCalendarRule  
======================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsCalendarRule/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな説明。**スマートデータモデル。GTFSのカレンダールール**について  

## プロパティのリスト  

- `alternateName`: このアイテムの別称  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `endDate`: このルールの終了日を `YYYY-MM-DD` 形式で表します。これは[calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)のフィールド`end_date`から取得できます。  - `friday`: GTFSの「金曜日」と同じです。  - `hasService`: このルールが適用されるサービスservice_id`から派生したものです。  - `id`: エンティティのユニークな識別子  - `monday`: GTFSと同じ `monday` です。  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `saturday`: GTFSと同じ `saturday` です。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `startDate`: このルールの開始日を `YYYY-MM-DD` 形式で表します。これは、[calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)のフィールド `start_date` から取得できます。  - `sunday`: GTFSの`sunday`と同じ  - `thursday`: GTFS `thursday`と同じ  - `tuesday`: GTFSと同じ `tuesday` です。  - `type`: NGSI Entity Typeです。GtfsCalendarRuleである必要があります。  - `wednesday`: GTFSと同じ `wednesday` です。    
必須項目  
- `endDate`  - `friday`  - `hasService`  - `id`  - `monday`  - `saturday`  - `startDate`  - `sunday`  - `thursday`  - `tuesday`  - `type`  - `wednesday`    
https://developers.google.com/transit/gtfs/reference/#calendartxt](https://developers.google.com/transit/gtfs/reference/#calendartxt)をご覧ください。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsCalendarRule:    
  description: 'Smart Data Models. GTFS Calendar Rule'    
  properties:    
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
    endDate:    
      description: "End date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `end_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)"    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    friday:    
      description: 'Same as GTFS `friday`'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
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
      anyOf: &gtfscalendarrule_-_properties_-_owner_-_items_-_anyof    
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
    monday:    
      description: 'Same as GTFS `monday`'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfscalendarrule_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    saturday:    
      description: 'Same as GTFS `saturday`'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
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
    startDate:    
      description: "Start date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `start_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)"    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/Date    
        type: Property    
    sunday:    
      description: 'Same as GTFS `sunday`'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    thursday:    
      description: 'Same as GTFS `thursday`'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    tuesday:    
      description: 'Same as GTFS `tuesday`'    
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
      description: 'Same as GTFS `wednesday`'    
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
```  
</details>    
## ペイロードの例  
#### GtfsCalendarRule NGSI-v2 key-values の例。  
GtfsCalendarRuleをkey-valuesとしてJSON-LD形式で記述した例を示します。これは、`options=keyValues`を使った場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### GtfsCalendarRule NGSI-v2規格化例  
正規化されたJSON-LD形式のGtfsCalendarRuleの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "type": "GtfsCalendarRule",  
  "startDate": {  
    "type": "Property",  
    "value": "2018-01-01"  
  },  
  "endDate": {  
    "type": "Property",  
    "value": "2019-01-01"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Rule Hospital Service 1"  
  },  
  "monday": {  
    "type": "Property",  
    "value": true  
  },  
  "tuesday": {  
    "type": "Property",  
    "value": true  
  },  
  "friday": {  
    "type": "Property",  
    "value": true  
  },  
  "wednesday": {  
    "type": "Property",  
    "value": true  
  },  
  "thursday": {  
    "type": "Property",  
    "value": true  
  },  
  "sunday": {  
    "type": "Property",  
    "value": false  
  },  
  "hasService": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1"  
  },  
  "saturday": {  
    "type": "Property",  
    "value": false  
  }  
}  
```  
#### GtfsCalendarRule NGSI-LD のキーバリューの例。  
GtfsCalendarRuleをkey-valuesとしてJSON-LD形式で記述した例です。これは、`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "type": "GtfsCalendarRule",  
  "startDate": {  
    "type": "Property",  
    "value": {  
      "@type": "Date",  
      "@value": "2018-01-01"  
    }  
  },  
  "endDate": {  
    "type": "Property",  
    "value": {  
      "@type": "Date",  
      "@value": "2019-01-01"  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "Rule Hospital Service 1"  
  },  
  "monday": {  
    "type": "Property",  
    "value": true  
  },  
  "tuesday": {  
    "type": "Property",  
    "value": true  
  },  
  "friday": {  
    "type": "Property",  
    "value": true  
  },  
  "wednesday": {  
    "type": "Property",  
    "value": true  
  },  
  "thursday": {  
    "type": "Property",  
    "value": true  
  },  
  "sunday": {  
    "type": "Property",  
    "value": false  
  },  
  "hasService": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1"  
  },  
  "saturday": {  
    "type": "Property",  
    "value": false  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### GtfsCalendarRule NGSI-LD 正規化された例。  
正規化されたJSON-LD形式のGtfsCalendarRuleの例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "endDate": "2019-01-01",  
  "friday": true,  
  "hasService": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1",  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "monday": true,  
  "name": "Rule Hospital Service 1",  
  "saturday": false,  
  "startDate": "2018-01-01",  
  "sunday": false,  
  "thursday": true,  
  "tuesday": true,  
  "type": "GtfsCalendarRule",  
  "wednesday": true  
}  
```  

マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。
