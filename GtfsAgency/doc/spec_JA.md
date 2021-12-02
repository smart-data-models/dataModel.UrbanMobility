エンティティGtfsAgency  
================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsAgency/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな説明。**GTFS機関**。  

## プロパティのリスト  

- `addressCountry`: 国です。例えば、スペイン  - `addressLocality`: ストリートアドレスがある地域で、どの地域にあるかは  - `addressRegion`: 地元がある地域、国の中にある地域  - `agencyName`: GTFSと同じ `agency_name` です。  - `alternateName`: このアイテムの別称  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `entitySource`: エンティティ・データのオリジナル・ソースをURLとして示す一連の文字。これは、このEntityの生成に使用されたオリジナルのGTFSフィードのURLを指すものとします。  - `id`: エンティティのユニークな識別子  - `language`: GTFSの `agency_language` と同じです。GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)を参照してください。  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `page`: GTFSの`stop_url`と同じです。  - `phone`: GFTSの`agency_phone`と同じです。  - `postOfficeBoxNumber`: 私書箱の住所の場合は、郵便局の箱番号です。例：03578  - `postalCode`: 郵便番号です。例：24004  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `streetAddress`: ストリートアドレス  - `timezone`: GTFSの `agency_timezone` と同じです。GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)を参照してください。  - `type`: NGSI Entity Typeです。GtfsAgencyである必要があります。    
必須項目  
- `agencyName`  - `id`  - `source`  - `type`    
https://developers.google.com/transit/gtfs/reference/#agencytxt](https://developers.google.com/transit/gtfs/reference/#agencytxt)をご覧ください。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
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
      description: 'NGSI Entity Type: It has to be GtfsAgency'    
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
```  
</details>    
## ペイロードの例  
#### GtfsAgency NGSI-v2 キーバリューの例  
GtfsAgencyをkey-valuesとしてJSON-LD形式で表現した例を示します。これはNGSI-v2で`options=keyValues`を使った場合と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### GtfsAgency NGSI-v2 正規化例  
JSON-LD形式で正規化されたGtfsAgencyの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### GtfsAgency NGSI-LD キーバリューの例  
GtfsAgencyをkey-valuesとしてJSON-LD形式で出力した例です。これは`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### GtfsAgency NGSI-LD 正規化例  
正規化されたJSON-LD形式のGtfsAgencyの例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
  "language": "ES",  
  "agencyName": "Empresa Malague\u00f1a de Transportes",  
  "page": "http://www.emtmalaga.es/",  
  "source": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52",  
  "timezone": "Europe/Madrid",  
  "type": "GtfsAgency"  
}  
```  

マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。
