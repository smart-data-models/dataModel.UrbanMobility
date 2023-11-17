<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: GtfsStopTime    
=================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsStopTime/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **GTFS 정지 시간**    
버전: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `alternateName[string]`: 이 항목의 대체 이름  - `arrivalTime[string]`: GTFS '도착 시간'과 동일합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `departureTime[string]`: GTFS `출발_시간`과 동일합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `description[string]`: 이 항목에 대한 설명  - `distanceTravelled[number]`: GTFS `shape_dist_traveled`와 동일합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `dropOffType[string]`: GTFS `drop_off_type`과 동일합니다. 열거형:'0, 1, 2, 3'  . Model: [https://schema.org/Text](https://schema.org/Text)- `hasStop[*]`: GTFS `stop_id`와 동일합니다. 이 엔티티는 GtfsStop 타입의 엔티티를 가리켜야 합니다.  . Model: [http://schema.org/URL](http://schema.org/URL)- `hasTrip[*]`: 이 엔티티와 연관된 트립입니다. 이 엔티티는 GtfsTrip 타입의 엔티티를 가리켜야 합니다.  . Model: [https://schema.org/URL](https://schema.org/URL)- `id[*]`: 엔티티의 고유 식별자  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `pickupType[string]`: GTFS `픽업_유형`과 동일합니다. 열거형:'0, 1, 2, 3'  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `stopHeadsign[string]`: GTFS `stop_headsign`과 동일합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `stopSequence[number]`: GTFS `stop_sequence`와 동일합니다. 1`로 시작  . Model: [https://schema.org/Integer](https://schema.org/Integer)- `timepoint[string]`: GTFS `타임포인트`와 동일합니다. 열거형:'0, 1'  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI 엔티티 유형. GtfsStopTime이어야 합니다.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `arrivalTime`  - `departureTime`  - `hasStop`  - `hasTrip`  - `id`  - `stopSequence`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
https://developers.google.com/transit/gtfs/reference/#stop_timestxt](https://developers.google.com/transit/gtfs/reference/#stop_timestxt) 참조    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
GtfsStopTime:      
  description: GTFS Stop Time      
  properties:      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    arrivalTime:      
      description: Same as GTFS `arrival_time`      
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$      
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
    departureTime:      
      description: Same as GTFS `departure_time`      
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    distanceTravelled:      
      description: Same as GTFS `shape_dist_traveled`      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    dropOffType:      
      default: 0      
      description: 'Same as GTFS `drop_off_type`. Enum:''0, 1, 2, 3'''      
      enum:      
        - 0      
        - 1      
        - 2      
        - 3      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    hasStop:      
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
      description: Same as GTFS `stop_id`. It shall point to an Entity of type GtfsStop      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    hasTrip:      
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
      description: Trip associated to this Entity. It shall point to an Entity of Type GtfsTrip      
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
    pickupType:      
      default: 0      
      description: 'Same as GTFS `pickup_type`. Enum:''0, 1, 2, 3'' '      
      enum:      
        - 0      
        - 1      
        - 2      
        - 3      
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
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    stopHeadsign:      
      description: Same as GTFS `stop_headsign`      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    stopSequence:      
      description: Same as GTFS `stop_sequence`. Starting with `1`      
      minimum: 1      
      type: number      
      x-ngsi:      
        model: https://schema.org/Integer      
        type: Property      
    timepoint:      
      default: 1      
      description: 'Same as GTFS `timepoint`. Enum:''0, 1'''      
      enum:      
        - 0      
        - 1      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be GtfsStopTime      
      enum:      
        - GtfsStopTime      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - arrivalTime      
    - departureTime      
    - hasStop      
    - hasTrip      
    - stopSequence      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsStopTime/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/GtfsStopTime/schema.json      
  x-model-tags: ""      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### GtfsStopTime NGSI-v2 키-값 예제    
다음은 키-값으로 JSON-LD 형식의 GtfsStopTime의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
  "type": "GtfsStopTime",  
  "hasStop": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737",  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011",  
  "distanceTravelled": 759,  
  "stopSequence": 4,  
  "arrivalTime": "07:04:24",  
  "departureTime": "07:04:24"  
}  
```  
</details>    
#### GtfsStopTime NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 GtfsStopTime의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
  "type": "GtfsStopTime",  
  "departureTime": {  
    "type": "Text",  
    "value": "07:04:24"  
  },  
  "hasTrip": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011"  
  },  
  "stopSequence": {  
    "type": "Number",  
    "value": 4  
  },  
  "distanceTravelled": {  
    "type": "Number",  
    "value": 759  
  },  
  "arrivalTime": {  
    "type": "Text",  
    "value": "07:04:24"  
  },  
  "hasStop": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737"  
  }  
}  
```  
</details>    
#### GtfsStopTime NGSI-LD 키-값 예제    
다음은 키 값으로 JSON-LD 형식의 GtfsStopTime의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
  "type": "GtfsStopTime",  
  "arrivalTime": "07:04:24",  
  "departureTime": "07:04:24",  
  "distanceTravelled": 759,  
  "hasStop": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737",  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011",  
  "stopSequence": 4,  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### GtfsStopTime NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 GtfsStopTime의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:GtfsStopTime:Spain:Madrid:EMT:FE0010011_737",  
    "type": "GtfsStopTime",  
    "arrivalTime": {  
        "type": "Property",  
        "value": "07:04:24"  
    },  
    "departureTime": {  
        "type": "Property",  
        "value": "07:04:24"  
    },  
    "distanceTravelled": {  
        "type": "Property",  
        "value": 759  
    },  
    "hasStop": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsStop:Madrid:EMT:737"  
    },  
    "hasTrip": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsTrip:Madrid:EMT:FE0010011"  
    },  
    "stopSequence": {  
        "type": "Property",  
        "value": 4  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
