エンティティGtfsShape  
===============  
[オープンライセンス](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsShape/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**GTFS形状**。  

## プロパティのリスト  

- `alternateName`: このアイテムの別称  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `distanceTravelled`: この形状を表す `LineString` や `MultiLineString` を構成する各ポイントに到達する際の移動距離を表す配列です。対応する `LineString` や `MultiLineString` と同じ数の要素と一致する必要があります。  - `id`: エンティティのユニークな識別子  - `location`: GeoJSONの `LineString` または `MultiLineString` としてエンコードされた、このエンティティに関連する地理的形状。座標はフィードファイルの `shapes.txt` から `shape_id`, `shape_pt_lat`, `shape_pt_lon`, `shape_pt_sequence` の値に基づいて取得します。  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type`: NGSI エンティティタイプです。GtfsShapeでなければならない。    
必須項目  
- `id`  - `location`  - `type`    
https://developers.google.com/transit/gtfs/reference/#shapestxt](https://developers.google.com/transit/gtfs/reference/#shapestxt)をご覧ください。GTFSの「形」を表しています。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsShape:    
  description: 'GTFS Shape'    
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
    distanceTravelled:    
      description: 'An array of the distance travelled when reaching each of the points that make the `LineString` or `MultiLineString` that represents this shape. It shall match the same number of elements as the corresponding `LineString` or `MultiLineString`.'    
      items:    
        minimum: 0    
        type: number    
      minItems: 1    
      type: array    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &gtfsshape_-_properties_-_owner_-_items_-_anyof    
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
      description: 'The geographical shape associated to this entity encoded as GeoJSON `LineString` or `MultiLineString`. The coordinates shall be obtained from the `shapes.txt` feed file as per the value of `shape_id`, `shape_pt_lat`, `shape_pt_lon`, `shape_pt_sequence`.'    
      oneOf:    
        - $id: https://geojson.org/schema/LineString.json    
          $schema: "http://json-schema.org/draft-07/schema#"    
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
        - $id: https://geojson.org/schema/MultiLineString.json    
          $schema: "http://json-schema.org/draft-07/schema#"    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfsshape_-_properties_-_owner_-_items_-_anyof    
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
      description: 'NGSI Entity type. It has to be GtfsShape'    
      enum:    
        - GtfsShape    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
</details>    
## ペイロードの例  
#### GtfsShape NGSI-v2 key-values の例。  
GtfsShapeをJSON-LD形式でkey-valuesにした例を紹介します。これはNGSI-v2で`options=keyValues`を使った場合と互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:GtfsShape:101",  
  "type": "GtfsShape",  
  "location": {  
    "type": "LineString",  
    "coordinates": [  
      [-4.421394, 36.73826],  
      [-4.421428, 36.73825],  
      [-4.421505, 36.738186],  
      [-4.421525, 36.738033]  
    ]  
  }  
}  
```  
#### GtfsShape NGSI-v2規格化例  
正規化されたJSON-LD形式のGtfsShapeの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:GtfsShape:101",  
  "type": "GtfsShape",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "LineString",  
      "coordinates": [  
        [-4.421394, 36.73826],  
        [-4.421428, 36.73825],  
        [-4.421505, 36.738186],  
        [-4.421525, 36.738033]  
      ]  
    }  
  }  
}  
```  
#### GtfsShape NGSI-LD のキーバリューの例。  
GtfsShapeをJSON-LD形式でkey-valuesにした例を紹介します。これは、`options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:GtfsShape:101",  
  "type": "GtfsShape",  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "LineString",  
      "coordinates": [  
        [  
          -4.421394,  
          36.73826  
        ],  
        [  
          -4.421428,  
          36.73825  
        ],  
        [  
          -4.421505,  
          36.738186  
        ],  
        [  
          -4.421525,  
          36.738033  
        ]  
      ]  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### GtfsShape NGSI-LDの正規化例  
正規化されたJSON-LD形式のGtfsShapeの例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:GtfsShape:101",  
  "location": {  
    "coordinates": [  
      [  
        -4.421394,  
        36.73826  
      ],  
      [  
        -4.421428,  
        36.73825  
      ],  
      [  
        -4.421505,  
        36.738186  
      ],  
      [  
        -4.421525,  
        36.738033  
      ]  
    ],  
    "type": "LineString"  
  },  
  "type": "GtfsShape"  
}  
```  
