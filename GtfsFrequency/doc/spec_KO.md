<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: GtfsFrequency  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsFrequency/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **GTFS 주파수**  
버전: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `alternateName[string]`: 이 항목의 대체 이름  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `endTime[string]`: GTFS `end_time`과 동일합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `exactTimes[boolean]`: GTFS '정확한_시간'과 동일하지만 부울로 인코딩되며, '거짓'입니다: 빈도 기반 여행이 정확히 예약되지 않았습니다. true`: 빈도 기반 트립이 정확히 예약됨  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `hasTrip[*]`: 이 엔티티와 연관된 트립입니다. 이 엔티티는 GtfsTrip 타입의 엔티티를 가리켜야 합니다.  . Model: [https://schema.org/URL](https://schema.org/URL)- `headwaySeconds[number]`: GTFS `headway_secs`와 동일합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 엔티티의 고유 식별자  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `startTime[string]`: GTFS `start_time`과 동일합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI 엔티티 유형. GtfsFrequency여야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `endTime`  - `hasTrip`  - `headwaySeconds`  - `id`  - `startTime`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
https://developers.google.com/transit/gtfs/reference/#frequenciestxt](https://developers.google.com/transit/gtfs/reference/#frequenciestxt) 참조  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsFrequency:    
  description: GTFS Frequency    
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
    endTime:    
      description: Same as GTFS `end_time`    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    exactTimes:    
      description: 'Same as GTFS `exact_times` but encoded as a Boolean; `false`: Frequency-based trips are not exactly scheduled. `true`: Frequency-based trips are exactly scheduled'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
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
    headwaySeconds:    
      description: Same as GTFS `headway_secs`    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    startTime:    
      description: Same as GTFS `start_time`    
      pattern: ^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be GtfsFrequency    
      enum:    
        - GtfsFrequency    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - hasTrip    
    - startTime    
    - endTime    
    - headwaySeconds    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsFrequency/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/GtfsFrequency/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### GtfsFrequency NGSI-v2 키 값 예제  
다음은 키 값으로 JSON-LD 형식의 GtfsFrequency의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
  "type": "GtfsFrequency",  
  "name": "Laborables",  
  "description": "Cada 10 minutos",  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
  "startTime": "07:00:00",  
  "endTime": "10:25:00",  
  "headwaySeconds": 600  
}  
```  
</details>  
#### GtfsFrequency NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 GtfsFrequency의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
  "type": "GtfsFrequency",  
  "description": {  
    "type": "Text",  
    "value": "Cada 10 minutos"  
  },  
  "hasTrip": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1"  
  },  
  "headwaySeconds": {  
    "type": "Number",  
    "value": 600  
  },  
  "startTime": {  
    "type": "Time",  
    "value": "07:00:00"  
  },  
  "endTime": {  
    "type": "Time",  
    "value": "10:25:00"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Laborables"  
  }  
}  
```  
</details>  
#### GtfsFrequency NGSI-LD 키 값 예제  
다음은 키 값으로 JSON-LD 형식의 GtfsFrequency의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
  "type": "GtfsFrequency",  
  "description": "Cada 10 minutos",  
  "endTime": "10:25:00",  
  "hasTrip": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1",  
  "headwaySeconds": 600,  
  "name": "Laborables",  
  "startTime": "07:00:00",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### GtfsFrequency NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 GtfsFrequency의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:GtfsFrequency:Malaga:Linea1",  
  "type": "GtfsFrequency",  
  "description": {  
    "type": "Property",  
    "value": "Cada 10 minutos"  
  },  
  "endTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-03-19T10:25:00Z"  
    }  
  },  
  "hasTrip": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:GtfsTrip:Spain:Malaga:1"  
  },  
  "headwaySeconds": {  
    "type": "Property",  
    "value": 600  
  },  
  "name": {  
    "type": "Property",  
    "value": "Laborables"  
  },  
  "startTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-03-19T07:00:00Z"  
    }  
  },  
  "@context": [  
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
