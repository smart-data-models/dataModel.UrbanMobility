<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 도착추정  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/ArrivalEstimation/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **도착 예상 시간**  
버전: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `alternateName[string]`: 이 항목의 대체 이름  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `hasStop[array]`: 이 엔티티는 GtfsStop 타입의 엔티티를 가리켜야 합니다.  - `hasTrip[*]`: 이 엔티티와 연관된 트립입니다. 이 엔티티는 GtfsTrip 타입의 엔티티를 가리켜야 합니다.  . Model: [https://schema.org/URL](https://schema.org/URL)- `headSign[string]`: 승객에게 여행 목적지를 식별하는 표지판에 표시되는 문구를 포함해야 합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 엔티티의 고유 식별자  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `remainingDistance[number]`: 해당 정류장으로 향하는 여행의 남은 도착 거리(미터)가 포함되어야 합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `remainingTime[string]`: 해당 정류장으로 향하는 여행의 남은 도착 시간을 포함해야 합니다. 남은 시간은 ISO8601 기간으로 인코딩되어야 합니다. 예. `PT8M5S`  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 엔티티 유형: ArrivalEstimation이어야 합니다. 열거형:'도착추정'  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `hasStop`  - `hasTrip`  - `headSign`  - `id`  - `remainingTime`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
이 엔티티 유형은 대중교통 차량이 특정 경로를 운행하는 동안 특정 정류장에 도착하는 예상 도착 시간을 캡처합니다.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ArrivalEstimation:    
  description: Arrival Estimation    
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
    hasStop:    
      description: It shall point to an Entity of Type GtfsStop    
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
      type: array    
      x-ngsi:    
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
    headSign:    
      description: It shall contain the text that appears on a sign that identifies the trip's destination to passengers    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    remainingDistance:    
      description: It shall contain the remaining distance (in meters) of arrival for the trip heading to the concerned stop    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Meters    
    remainingTime:    
      description: It shall contain the remaining time of arrival for the trip heading to the concerned stop. Remaining time shall be encoded as a ISO8601 duration. Ex. `PT8M5S`    
      pattern: ^P(?=\w*\d)(?:\d+Y|Y)?(?:\d+M|M)?(?:\d+W|W)?(?:\d+D|D)?(?:T(?:\d+H|H)?(?:\d+M|M)?(?:\d+(?:\?.\d{1,2})?S|S)?)?$    
      type: string    
      x-ngsi:    
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
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### 도착추정 NGSI-v2 키값 예시  
다음은 키 값으로 JSON-LD 형식의 도착 예상 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### 도착 추정 NGSI-v2 정규화 예시  
다음은 정규화된 JSON-LD 형식의 도착 예상 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ArrivalEstimation:L5C1_Stop74_1",  
  "type": "ArrivalEstimation",  
  "hasTrip": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:GtfsTrip:tus:5C1"  
  },  
  "headSign": {  
    "type": "Text",  
    "value": "Plaza Italia"  
  },  
  "remainingTime": {  
    "type": "Text",  
    "value": "PT8M5S"  
  },  
  "hasStop": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:GtfsStop:tus:74"  
  },  
  "remainingDistance": {  
    "type": "Text",  
    "value": 1200  
  }  
}  
```  
</details>  
#### 도착 추정 NGSI-LD 키 값 예시  
다음은 키 값으로 JSON-LD 형식의 도착 예상 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### 도착 추정 NGSI-LD 정규화 예시  
다음은 정규화된 JSON-LD 형식의 도착 예상 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
