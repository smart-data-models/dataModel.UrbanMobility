[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ到着予測  
==========  
[オープンライセンス](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/ArrivalEstimation/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**到着予測**」。  
バージョン: 0.0.3  

## プロパティ一覧  

- `alternateName`: この項目の別称  - `dataProvider`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description`: このアイテムの説明  - `hasStop`: GtfsStop 型のエンティティを指すものとする。  - `hasTrip`: このEntityに関連付けられたTrip。GtfsTrip 型の Entity を指すものとする。  - `headSign`: 旅客に対して旅行の目的地を示す標識に表示される文章を含むこと。  - `id`: エンティティの一意な識別子  - `name`: このアイテムの名称です。  - `owner`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `remainingDistance`: 当該停留所に向かう旅行の残り到着距離（メートル）を記載すること。  - `remainingTime`: (2)残り時間 (3)残り時間：当該停留所に向かう旅行の残り時間を含む。残り時間は ISO8601 のデュレーションとしてエンコードされなければならない。例：`PT8M5S`。  - `seeAlso`: 項目に関する追加リソースを指すURIのリスト。  - `source`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type`: NGSI Entity Typeです。ArrivalEstimationでなければならない。Enum:'ArrivalEstimation'（到着予測）。    
必要なプロパティ  
- `hasStop`  - `hasTrip`  - `headSign`  - `id`  - `remainingTime`  - `type`    
このエンティティタイプは、公共交通機関が特定のルートを運行している間に、特定の停留所に到着する予定時刻を取得する。  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ArrivalEstimation:    
  description: 'Arrival Estimation'    
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
    hasStop:    
      description: 'It shall point to an Entity of Type GtfsStop'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
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
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    headSign:    
      description: 'It shall contain the text that appears on a sign that identifies the trip''s destination to passengers'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
        type: Property    
    id:    
      anyOf: &arrivalestimation_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *arrivalestimation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    remainingDistance:    
      description: 'It shall contain the remaining distance (in meters) of arrival for the trip heading to the concerned stop'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Meters    
    remainingTime:    
      description: 'It shall contain the remaining time of arrival for the trip heading to the concerned stop. Remaining time shall be encoded as a ISO8601 duration. Ex. `PT8M5S`.'    
      pattern: ^P(?=\w*\d)(?:\d+Y|Y)?(?:\d+M|M)?(?:\d+W|W)?(?:\d+D|D)?(?:T(?:\d+H|H)?(?:\d+M|M)?(?:\d+(?:\?.\d{1,2})?S|S)?)?$    
      type: string    
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
      description: 'NGSI Entity Type: It has to be ArrivalEstimation. Enum:''ArrivalEstimation'''    
      enum:    
        - ArrivalEstimation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - hasStop    
    - hasTrip    
    - remainingTime    
    - headSign    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/ArrivalEstimation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/ArrivalEstimation/schema.json    
  x-model-tags: ""    
  x-version: 0.0.3    
```  
</details>    
## ペイロードの例  
#### ArrivalEstimation NGSI-v2 key-value 例  
以下は、ArrivalEstimationをJSON-LD形式でkey-valuesにした例である。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
```json  
{  
  "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
  "type": "ArrivalEstimation",  
  "hasStop": ["urn:ngsi-ld:GtfsStop:tus:74"],  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:tus:5C1",  
  "remainingTime": "PT8M5S",  
  "remainingDistance": 1200,  
  "headSign": "Plaza Italia"  
}  
```  
#### 到着推定 NGSI-v2 正規化例  
以下は、ArrivalEstimation を JSON-LD 形式で正規化した例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
  "type": "ArrivalEstimation",  
  "hasTrip": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsTrip:tus:5C1"  
  },  
  "headSign": {  
    "value": "Plaza Italia"  
  },  
  "remainingTime": {  
    "value": "PT8M5S"  
  },  
  "hasStop": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:GtfsStop:tus:74"  
  },  
  "remainingDistance": {  
    "value": 1200  
  }  
}  
```  
#### 到着予測 NGSI-LD キー値例  
以下は、ArrivalEstimationをJSON-LD形式でkey-valuesにした例である。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
```json  
{  
    "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
    "type": "ArrivalEstimation",  
    "hasStop": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsStop:tus:74"  
    },  
    "hasTrip": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsTrip:tus:5C1"  
    },  
    "headSign": {  
        "type": "Property",  
        "value": "Plaza Italia"  
    },  
    "remainingDistance": {  
        "type": "Property",  
        "value": 1200  
    },  
    "remainingTime": {  
        "type": "Property",  
        "value": "PT8M5S"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
#### 到着予測 NGSI-LD 正規化例  
以下は、ArrivalEstimation を JSON-LD 形式で正規化した例である。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
    "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
    "type": "ArrivalEstimation",  
    "hasStop": "urn:ngsi-ld:GtfsStop:tus:74",  
    "hasTrip": "urn:ngsi-ld:GtfsTrip:tus:5C1",  
    "headSign": "Plaza Italia",  
    "remainingDistance": 1200,  
    "remainingTime": "PT8M5S",  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
