<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ公共交通機関停止  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/PublicTransportStop/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**一般的な公共交通機関の停留所  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `openingHoursSpecification[array]`: 場所の営業時間や場所内の特定のサービスに関する情報を提供する構造化された値。  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `peopleCount[number]`: 停留所での待ち人数の推定  . Model: [https://schema.org/Number](https://schema.org/Number)- `refPeopleCountDevice[string]`: デバイス](https://github.com/Fiware/dataModels/blob/master/specs/Device/Device/doc/spec.md)が推定人数を提供する。  - `refPublicTransportRoute[array]`: この停留所を利用する公共交通路線  . Model: [ https://schema.org/URL]( https://schema.org/URL)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `shortStopCode[string]`: 公共交通機関の停留所の識別子/コードの短縮形  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `stopCode[string]`: 公共交通機関の停留所の識別子/コード  . Model: [https://schema.org/Text](https://schema.org/Text)- `transportationType[array]`: (https://developers.google.com/transit/gtfs/reference/#routestxt)で定義されている、この停留所を利用する公共交通機関の種類。列挙:'0, 1, 2, 3, 4, 5, 6, 7'.  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI エンティティタイプ。これは PublicTransportStop でなければならない。  - `wheelChairAccessible[string]`: GTFS `wheelchair_boarding` と同じ。列挙型:'0, 1 ,2'。GTFS](https://developers.google.com/transit/gtfs/reference/#stopstxt)を参照。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `name`  - `transportationType`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
公共交通機関の停留所の汎用モデル。GTFSの定義を一部採用しているが、追加のGTFSデータとリンクする必要はない。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PublicTransportStop:    
  description: A generic public transport stop    
  properties:    
    address:    
      description: The mailing address    
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
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
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
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    openingHoursSpecification:    
      description: A structured value providing information about the opening hours of a place or a certain service inside a place    
      items:    
        properties:    
          closes:    
            description: ' 	The closing hour of the place or service on the given day(s) of the week'    
            format: time    
            type: string    
            x-ngsi:    
              type: Property    
          dayOfWeek:    
            anyOf:    
              - description: Array of days of the week    
                enum:    
                  - Monday    
                  - Tuesday    
                  - Wednesday    
                  - Thursday    
                  - Friday    
                  - Saturday    
                  - Sunday    
                  - PublicHolidays    
                type: string    
                x-ngsi:    
                  type: Property    
              - description: Array of days of the week    
                enum:    
                  - https://schema.org/Monday    
                  - https://schema.org/Tuesday    
                  - https://schema.org/Wednesday    
                  - https://schema.org/Thursday    
                  - https://schema.org/Friday    
                  - https://schema.org/Saturday    
                  - https://schema.org/Sunday    
                  - https://schema.org/PublicHolidays    
                type: string    
                x-ngsi:    
                  type: Property    
            description: 'The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays)'    
            type: string    
            x-ngsi:    
              model: http://schema.org/dayOfWeek    
              type: Property    
          opens:    
            description: The opening hour of the place or service on the given day(s) of the week    
            format: time    
            type: string    
            x-ngsi:    
              type: Property    
          validFrom:    
            anyOf:    
              - description: ""    
                format: date    
                type: string    
                x-ngsi:    
                  model: http://schema.org/Date    
                  type: Property    
              - description: ""    
                format: date-time    
                type: string    
                x-ngsi:    
                  model: http://schema.org/DateTime    
                  type: Property    
            description: 'The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format'    
            x-ngsi:    
              type: Property    
          validThrough:    
            anyOf:    
              - description: ""    
                format: date    
                type: string    
                x-ngsi:    
                  model: http://schema.org/Date    
                  type: Property    
              - description: ""    
                format: date-time    
                type: string    
                x-ngsi:    
                  model: http://schema.org/DateTime    
                  type: Property    
            description: 'The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format'    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
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
    peopleCount:    
      description: Estimation of people waiting in the stop    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    refPeopleCountDevice:    
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
      description: 'Reference to the [Device](https://github.com/Fiware/dataModels/blob/master/specs/Device/Device/doc/spec.md) providing people count estimate'    
      type: string    
      x-ngsi:    
        type: Property    
    refPublicTransportRoute:    
      description: Public transport routes using this stop    
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
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: ' https://schema.org/URL'    
        type: Relationship    
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
    shortStopCode:    
      description: Shorter form of the identifier/code of the public transport stop    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    stopCode:    
      description: Identifier/code of the public transport stop    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transportationType:    
      description: "Types of public transport using this stop as defined in (https://developers.google.com/transit/gtfs/reference/#routestxt). Enum:'0, 1, 2, 3, 4, 5, 6, 7'"    
      items:    
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
      type: array    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be PublicTransportStop    
      enum:    
        - PublicTransportStop    
      type: string    
      x-ngsi:    
        type: Property    
    wheelChairAccessible:    
      description: "Same as GTFS `wheelchair_boarding`. Enum:'0, 1 ,2'. Reference in [GTFS](https://developers.google.com/transit/gtfs/reference/#stopstxt) "    
      enum:    
        - 0    
        - 1    
        - 2    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - transportationType    
    - name    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/PublicTransportStop/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/PublicTransportStop/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### PublicTransportStop NGSI-v2 キー値の例  
JSON-LD形式のPublicTransportStopのkey-valuesの例である。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportStop:santander:busStop:463",  
  "type": "PublicTransportStop",  
  "dateModified": "2018-09-25T08:32:26.00Z",  
  "source": "https://api.smartsantander.eu/",  
  "dataProvider": "http://www.smartsantander.eu/",  
  "address": {  
    "streetAddress": "C/ La Pereda 14",  
    "addressLocality": "Santander",  
    "addressRegion": "Cantabria",  
    "addressCountry": "Spain"  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.804648385,  
      43.478053126  
    ]  
  },  
  "stopCode": "la_pereda_463",  
  "shortStopCode": "463",  
  "name": "La Pereda 14",  
  "wheelchairAccessible": 0,  
  "transportationType": [  
    3  
  ],  
  "refPublicTransportRoute": [  
    "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
    "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N4"  
  ],  
  "peopleCount": 0,  
  "refPeopleCountDevice": "urn:ngsi-ld:PorpleCountDecice:santander:463",  
 "openingHoursSpecification":   
  [  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Monday"  
    },  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Tuesday"  
    },  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Wednesday"  
    },  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Thursday"  
    },  
    {  
      "opens": "00:01",  
      "closes": "23:59",  
      "dayOfWeek": "Friday"  
    }  
  ]  
}  
```  
</details>  
#### PublicTransportStop NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の PublicTransportStop の例である。これは、オプションを使用しない場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキスト・データを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportStop:santander:busStop:463",  
  "type": "PublicTransportStop",  
  "dateModified": {  
    "type": "ISO8601",  
    "value": "2018-09-25T08:32:26.00Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "https://api.smartsantander.eu/"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "http://www.smartsantander.eu/"  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "C/ La Pereda 14",  
      "addressLocality": "Santander",  
      "addressRegion": "Cantabria",  
      "addressCountry": "Spain"  
    }  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.804648385,  
        43.478053126  
      ]  
    }  
  },  
  "stopCode": {  
    "type": "Text",  
    "value": "la_pereda_463"  
  },  
  "shortStopCode": {  
    "type": "Text",  
    "value": "463"  
  },  
  "name": {  
    "type": "Text",  
    "value": "La Pereda 14"  
  },  
  "wheelchairAccessible": {  
    "type": "Number",  
    "value": 0  
  },  
  "transportationType": {  
    "type": "StructuredValue",  
    "value": [  
      3  
    ]  
  },  
  "refPublicTransportRoute": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
      "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N4"  
    ]  
  },  
  "peopleCount": {  
    "type": "Number",  
    "value": 0  
  },  
  "refPeopleCountDevice": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PorpleCountDecice:santander:463"  
  },  
  "openingHoursSpecification": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "opens" : {  
          "type": "string",   
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek":{  
          "type": "string",  
          "value": "Friday"  
        }  
      },  
      {  
        "opens" : {  
          "type": "string",   
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek":{  
          "type": "string",  
          "value": "Monday"  
        }  
      },  
      {  
        "opens" : {  
          "type": "string",   
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek":{  
          "type": "string",  
          "value": "Tuesday"  
        }  
      },  
      {  
        "opens" : {  
          "type": "string",   
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek":{  
          "type": "string",  
          "value": "Thursday"  
        }  
      },  
      {  
        "opens" : {  
          "type": "string",   
          "value": "00:01"  
        },  
        "closes": {  
          "type": "string",  
          "value": "23:59"  
        },  
        "dayOfWeek":{  
          "type": "string",  
          "value": "Wednesday"  
        }  
      }  
    ]    
  }  
}  
```  
</details>  
#### PublicTransportStop NGSI-LD キー値の例  
JSON-LD形式のPublicTransportStopのkey-valuesの例である。これは、`options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportStop:santander:busStop:463",  
  "type": "PublicTransportStop",  
  "address": {  
    "streetAddress": "C/ La Pereda 14",  
    "addressLocality": "Santander",  
    "addressRegion": "Cantabria",  
    "addressCountry": "Spain"  
  },  
  "dataProvider": "http://www.smartsantander.eu/",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.804648385,  
      43.478053126  
    ]  
  },  
  "name": "La Pereda 14",  
  "openingHoursSpecification": [  
    {  
      "opens": {  
        "type": "string",  
        "value": "00:01"  
      },  
      "closes": {  
        "type": "string",  
        "value": "23:59"  
      },  
      "dayOfWeek": {  
        "type": "string",  
        "value": "Friday"  
      }  
    },  
    {  
      "opens": {  
        "type": "string",  
        "value": "00:01"  
      },  
      "closes": {  
        "type": "string",  
        "value": "23:59"  
      },  
      "dayOfWeek": {  
        "type": "string",  
        "value": "Monday"  
      }  
    },  
    {  
      "opens": {  
        "type": "string",  
        "value": "00:01"  
      },  
      "closes": {  
        "type": "string",  
        "value": "23:59"  
      },  
      "dayOfWeek": {  
        "type": "string",  
        "value": "Tuesday"  
      }  
    },  
    {  
      "opens": {  
        "type": "string",  
        "value": "00:01"  
      },  
      "closes": {  
        "type": "string",  
        "value": "23:59"  
      },  
      "dayOfWeek": {  
        "type": "string",  
        "value": "Thursday"  
      }  
    },  
    {  
      "opens": {  
        "type": "string",  
        "value": "00:01"  
      },  
      "closes": {  
        "type": "string",  
        "value": "23:59"  
      },  
      "dayOfWeek": {  
        "type": "string",  
        "value": "Wednesday"  
      }  
    }  
  ],  
  "peopleCount": 0,  
  "refPeopleCountDevice": "urn:ngsi-ld:PorpleCountDecice:santander:463",  
  "refPublicTransportRoute": [  
    "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
    "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N4"  
  ],  
  "shortStopCode": "463",  
  "source": "https://api.smartsantander.eu/",  
  "stopCode": "la_pereda_463",  
  "transportationType": [  
    3  
  ],  
  "wheelchairAccessible": 0  
  ,  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### PublicTransportStop NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の PublicTransportStop の例である。これは、オプションを使用しない場合の NGSI-LD と互換性があり、個々のエンティティのコンテキスト・データを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PublicTransportStop:santander:busStop:463",  
  "type": "PublicTransportStop",  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "C/ La Pereda 14",  
      "addressLocality": "Santander",  
      "addressRegion": "Cantabria",  
      "addressCountry": "Spain"  
    }  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "http://www.smartsantander.eu/"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2018-09-25T08:32:26.00Z"  
  },  
  "entityVersion": {  
    "type": "Property",  
    "value": 2.0  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.804648385,  
        43.478053126  
      ]  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "La Pereda 14"  
  },  
  "openingHoursSpecification": {  
    "type": "Property",  
    "value": [  
      {  
        "opens": "00:01",  
        "closes": "23:59",  
        "dayOfWeek": "Monday"  
      },  
      {  
        "opens": "00:01",  
        "closes": "23:59",  
        "dayOfWeek": "Tuesday"  
      },  
      {  
        "opens": "00:01",  
        "closes": "23:59",  
        "dayOfWeek": "Wednesday"  
      },  
      {  
        "opens": "00:01",  
        "closes": "23:59",  
        "dayOfWeek": "Thursday"  
      },  
      {  
        "opens": "00:01",  
        "closes": "23:59",  
        "dayOfWeek": "Friday"  
      }  
    ]  
  },  
  "peopleCount": {  
    "type": "Property",  
    "value": 0  
  },  
  "refPeopleCountDevice": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PorpleCountDecice:santander:463"  
  },  
  "refPublicTransportRoute": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
      "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N4"  
    ]  
  },  
  "shortStopCode": {  
    "type": "Property",  
    "value": "463"  
  },  
  "source": {  
    "type": "Property",  
    "value": "https://api.smartsantander.eu/"  
  },  
  "stopCode": {  
    "type": "Property",  
    "value": "la_pereda_463"  
  },  
  "transportationType": {  
    "type": "Property",  
    "value": [  
      3  
    ]  
  },  
  "wheelchairAccessible": {  
    "type": "Property",  
    "value": 0  
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
