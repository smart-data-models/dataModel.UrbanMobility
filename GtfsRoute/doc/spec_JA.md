<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティGtfsRoute  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsRoute/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**GTFSルート  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `alternateName[string]`: この項目の別名  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `name[string]`: このアイテムの名前。  - `operatedBy[*]`: このルートを運営するエージェンシー。タイプ GtfsAgency のエンティティを指すものとする。  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `page[string]`: GTFS の `stop_url` と同じ。  . Model: [http://schema.org/URL](http://schema.org/URL)- `routeColor[string]`: GTFS の `route_color` と同じ。GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)を参照。  . Model: [https://schema.org/Text](https://schema.org/Text)- `routeSortOrder[number]`: GTFS の `route_sort_order` と同じ。  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `routeTextColor[string]`: GTFS の `route_text_color` と同じ。GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)を参照。  . Model: [https://schema.org/Text](https://schema.org/Text)- `routeType[string]`: GTFS `route_type` と同じ。許容される値は、[GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt) で規定されている `route_type` で許容される値。Enum:'0, 1, 2, 3, 4, 5, 6, 7'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `shortName[string]`: GTFS の `route_short_name` と同じ。  . Model: [https://schema.org/Text.](https://schema.org/Text.)- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨します。  - `type[string]`: NGSIエンティティタイプ。GtfsRouteでなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
参照[https://developers.google.com/transit/gtfs/reference/#routestxt](https://developers.google.com/transit/gtfs/reference/#routestxt)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsRoute:    
  description: GTFS Route    
  properties:    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
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
    id:    
      anyOf: &gtfsroute_-_properties_-_owner_-_items_-_anyof    
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
    operatedBy:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Agency that operates this route. It shall point to an Entity of Type GtfsAgency    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Relationship    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *gtfsroute_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    page:    
      description: Same as GTFS `stop_url`    
      format: uri    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Property    
    routeColor:    
      description: "Same as GTFS `route_color`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    routeSortOrder:    
      description: Same as GTFS `route_sort_order`    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    routeTextColor:    
      description: "Same as GTFS `route_text_color`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    routeType:    
      description: "Same as GTFS `route_type`. allowed values those allowed for `route_type` as prescribed by [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt). Enum:'0, 1, 2, 3, 4, 5, 6, 7'"    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: Same as GTFS `route_short_name`    
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
      description: NGSI Entity type. It has to be GtfsRoute    
      enum:    
        - GtfsRoute    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsRoute/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/specs/UrbanMobility/GtfsRoute/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### GtfsRoute NGSI-v2 キー値の例  
JSON-LD形式のGtfsRouteのkey-valuesの例です。options=keyValues`を使うとNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
  "type": "GtfsRoute",  
  "shortName": "1",  
  "name": "Parque del Sur _ Alameda Principal _ San Andrés",  
  "page": "http://www.emtmalaga.es/emt-mobile/informacionLinea.html",  
  "routeType": "3",  
  "operatedBy": "urn:ngsi-ld:GtfsAgency:Malaga_EMT"  
}  
```  
</details>  
#### GtfsRoute NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の GtfsRoute の例です。これはNGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
  "type": "GtfsRoute",  
  "name": {  
    "type": "Text",  
    "value": "Parque del Sur _ Alameda Principal _ San Andr\u00e9s"  
  },  
  "shortName": {  
    "type": "Text",  
    "value": "1"  
  },  
  "page": {  
    "type": "URL",  
    "value": "http://www.emtmalaga.es/emt-mobile/informacionLinea.html"  
  },  
  "routeType": {  
    "type": "Text",  
    "value": "3"  
  },  
  "operatedBy": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:GtfsAgency:Malaga_EMT"  
  }  
}  
```  
</details>  
#### GtfsRoute NGSI-LD キー値の例  
GtfsRouteをJSON-LD形式でkey-valuesとした例です。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
    "type": "GtfsRoute",  
    "name": "Parque del Sur _ Alameda Principal _ San Andr\u00e9s",  
    "operatedBy": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
    "page": "http://www.emtmalaga.es/emt-mobile/informacionLinea.html",  
    "routeType": "3",  
    "shortName": "1",  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### GtfsRoute NGSI-LD 正規化例  
正規化されたJSON-LD形式のGtfsRouteの例です。これは、オプションを使わない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:GtfsRoute:Spain:Malaga:1",  
    "type": "GtfsRoute",  
    "name": {  
        "type": "Property",  
        "value": "Parque del Sur _ Alameda Principal _ San Andr\u00e9s"  
    },  
    "operatedBy": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsAgency:Malaga_EMT"  
    },  
    "page": {  
        "type": "Property",  
        "value": "http://www.emtmalaga.es/emt-mobile/informacionLinea.html"  
    },  
    "routeType": {  
        "type": "Property",  
        "value": "3"  
    },  
    "shortName": {  
        "type": "Property",  
        "value": "1"  
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
