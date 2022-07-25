[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティPublicTransportStop  
=========================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/PublicTransportStop/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**一般的な公共交通機関の停留所**  
バージョン: 0.0.1  

## プロパティ一覧  

- `address`: 郵送先住所  - `alternateName`: この項目の別称  - `areaServed`: サービスまたは提供品が提供される地理的な地域  - `dataProvider`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description`: このアイテムの説明  - `id`: エンティティの一意な識別子  - `location`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name`: このアイテムの名称です。  - `openingHoursSpecification`: 場所の営業時間や場所内の特定のサービスに関する情報を提供する構造化された値  - `owner`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `peopleCount`: 停車中の待ち人数の推定  - `refPeopleCountDevice`: デバイス](https://github.com/Fiware/dataModels/blob/master/specs/Device/Device/doc/spec.md)が提供する人数の推定値への言及。  - `refPublicTransportRoute`: この停留所を利用する公共交通機関のルート  - `seeAlso`: 項目に関する追加リソースを指すURIのリスト。  - `shortStopCode`: 公共交通機関の停留所の識別子／コードの短縮形  - `source`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `stopCode`: 公共交通機関の停車駅の識別子／コード  - `transportationType`: (https://developers.google.com/transit/gtfs/reference/#routestxt)で定義される、この停留所を利用する公共交通機関の種類。Enum:'0, 1, 2, 3, 4, 5, 6, 7'。  - `type`: NGSI Entity タイプ。これは PublicTransportStop でなければならない。  - `wheelChairAccessible`: GTFS の `wheelchair_boarding` と同じ。Enum:'0, 1 ,2'.GTFS](https://developers.google.com/transit/gtfs/reference/#stopstxt)で参照。    
必要なプロパティ  
- `id`  - `name`  - `transportationType`  - `type`    
公共交通機関の停留所の一般的なモデル。GTFSの定義を一部採用しているが、GTFSの追加データとリンクする必要はない。  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PublicTransportStop:    
  description: 'A generic public transport stop'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    id:    
      anyOf: &publictransportstop_-_properties_-_owner_-_items_-_anyof    
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
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    openingHoursSpecification:    
      description: 'A structured value providing information about the opening hours of a place or a certain service inside a place'    
      items:    
        properties:    
          closes:    
            format: time    
            pattern: ^(2[0-3]|[01][0-9]):?([0-5][0-9]):?([0-5][0-9])(\.[0-9]*)?(Z|[+-](?:2[0-3]|[01][0-9])(?::?(?:[0-5][0-9]))?)$    
            type: string    
          dayOfWeek:    
            anyOf:    
              - description: 'Property. Array of days of the week.'    
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
              - description: 'Property. Array of days of the week.'    
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
            description: 'Property. Model:''http://schema.org/dayOfWeek''. The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays).'    
            type: string    
          opens:    
            format: time    
            pattern: ^(2[0-3]|[01][0-9]):?([0-5][0-9]):?([0-5][0-9])(\.[0-9]*)?(Z|[+-](?:2[0-3]|[01][0-9])(?::?(?:[0-5][0-9]))?)$    
            type: string    
          validFrom:    
            anyOf:    
              - description: 'Property. Model:''http://schema.org/Date.'    
                format: date    
                type: string    
              - description: 'Property. Model:''http://schema.org/DateTime.'    
                format: date-time    
                type: string    
            description: 'Property. The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format.'    
          validThrough:    
            anyOf:    
              - description: 'Property. Model:''http://schema.org/Date.'    
                format: date    
                type: string    
              - description: 'Property. Model:''http://schema.org/DateTime.'    
                format: date-time    
                type: string    
            description: 'Property. The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format.'    
            type: string    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *publictransportstop_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    peopleCount:    
      description: 'Estimation of people waiting in the stop'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    refPeopleCountDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the [Device](https://github.com/Fiware/dataModels/blob/master/specs/Device/Device/doc/spec.md) providing people count estimate.'    
      type: string    
      x-ngsi:    
        type: Property    
    refPublicTransportRoute:    
      description: 'Public transport routes using this stop.'    
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
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: ' https://schema.org/URL'    
        type: Relationship    
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
    shortStopCode:    
      description: 'Shorter form of the identifier/code of the public transport stop'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    stopCode:    
      description: 'Identifier/code of the public transport stop'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
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
      description: 'NGSI Entity type. It has to be PublicTransportStop'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/PublicTransportStop/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/PublicTransportStop/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### PublicTransportStop NGSI-v2 key-value の例。  
以下は、PublicTransportStopをJSON-LD形式でkey-valuesにした例である。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
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
#### PublicTransportStop NGSI-v2 正規化例  
以下は、PublicTransportStop を JSON-LD 形式で正規化した例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### PublicTransportStop NGSI-LD key-value の例  
以下は、PublicTransportStopをJSON-LD形式でkey-valuesにした例である。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータが返される。  
```json  
{  
    "id": "urn:ngsi-ld:PublicTransportStop:santander:busStop:463",  
    "type": "PublicTransportStop",  
    "address": {  
        "type": "StructuredValue",  
        "value": {  
            "streetAddress": "C/ La Pereda 14",  
            "addressLocality": "Santander",  
            "addressRegion": "Cantabria",  
            "addressCountry": "Spain"  
        }  
    },  
    "dataProvider": {  
        "type": "Text",  
        "value": "http://www.smartsantander.eu/"  
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
    "name": {  
        "type": "Text",  
        "value": "La Pereda 14"  
    },  
    "openingHoursSpecification": {  
        "type": "StructuredValue",  
        "value": [  
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
    "refPublicTransportRoute": {  
        "type": "StructuredValue",  
        "value": [  
            "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N3",  
            "urn:ngsi-ld:PublicTransportRoute:santander:transport:busLine:N4"  
        ]  
    },  
    "shortStopCode": {  
        "type": "Text",  
        "value": "463"  
    },  
    "source": {  
        "type": "Text",  
        "value": "https://api.smartsantander.eu/"  
    },  
    "stopCode": {  
        "type": "Text",  
        "value": "la_pereda_463"  
    },  
    "transportationType": {  
        "type": "StructuredValue",  
        "value": [  
            3  
        ]  
    },  
    "wheelchairAccessible": {  
        "type": "Number",  
        "value": 0  
    },  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
#### PublicTransportStop NGSI-LD 正規化例  
以下は、PublicTransportStop を JSON-LD 形式で正規化した例である。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "dateModified": "2018-09-25T08:32:26.00Z",  
    "entityVersion": 2.0,  
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
    "wheelchairAccessible": 0,  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
