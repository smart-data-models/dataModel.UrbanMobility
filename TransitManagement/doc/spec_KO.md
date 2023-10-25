<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 트랜짓 관리  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/TransitManagement/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **대중교통 시스템 데이터 모델**  
버전: 0.0.4  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `acAvailable[string]`: 이 관측에 해당하는 차량에 에어컨 옵션이 있는지 설명합니다.  - `ac_available[string]`: 이 관측에 해당하는 차량에 에어컨 옵션이 있는지 설명합니다.  - `actual_trip_end_time[date-time]`: 이 필드에는 이 관측에 해당하는 서비스 또는 여행이 종료될 예정 시간을 지정합니다.  - `actual_trip_start_time[date-time]`: 이 필드는 서비스가 실제로 시작된 시간을 지정합니다.  이는 GTFS 실시간 메시지-TripUpdate(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)의 stop_time_update(StopTimeUpdate) 메시지의 '도착' 필드에 있는 절대 '시간'(StopTimeEvent)과 동일합니다.  - `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `agencyInfo[object]`: 이 관찰에 해당하는 대행사 정보  	- `agency_email[string]`: 대행사의 고객 서비스 부서에서 적극적으로 모니터링하는 이메일 주소입니다. SameAs: GTFS 정적 필드 정의 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)의 'agency_email' 필드    
	- `agency_fare_url[string]`: 요금에 대한 세부 정보가 포함되어 있으며 해당 여행사의 항공권을 온라인으로 구매할 수 있는 웹 페이지의 URL입니다. SameAs: GTFS 정적 필드 정의 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)의 'agency_fare_url' 필드    
	- `agency_id[string]`: 환승 대행사를 고유하게 식별하는 ID입니다. 하나의 환승 피드는 두 개 이상의 여행사 데이터를 나타낼 수 있습니다. agency_id는 데이터 세트 고유의 식별자입니다. 이 필드는 단일 대행사에 대한 데이터만 포함하는 환승 피드에 대해 선택 사항입니다. SameAs: GTFS 정적 필드 정의의 'agency_id' 필드 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_lang[string]`: 이 운송업체에서 사용하는 기본 언어에 대한 두 글자 ISO 639-1 코드가 포함되어 있습니다. 언어 코드는 대소문자를 구분하지 않습니다(EN과 EN 모두 사용 가능). SameAs: GTFS 정적 필드 정의의 'agency_lang' 필드 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_name[string]`: 에이전시_이름 필드에는 운송업체의 전체 이름이 포함됩니다. SameAs: GTFS 정적 필드 정의의 'agency_name' 필드 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_phone[string]`: 지정된 대행사의 음성 전화 번호입니다: GTFS 정적 필드 정의의 'agency_phone' 필드 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_timezone[string]`: 표준 시간대 필드에는 운송 대행사가 위치한 표준 시간대가 포함됩니다. SameAs: GTFS 정적 필드 정의의 'agency_timezone' 필드 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_url[string]`: agency_url 필드에는 운송 대행사의 URL이 포함됩니다. SameAs: GTFS 정적 필드 정의의 'agency_url' 필드 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)    
- `agency_fare_url[string]`: 요금에 대한 세부 정보가 포함되어 있으며 해당 여행사의 항공권을 온라인으로 구매할 수 있는 웹 페이지의 URL입니다. SameAs: GTFS 정적 필드 정의 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)의 'agency_fare_url' 필드  - `agency_id[string]`: 환승 대행사를 고유하게 식별하는 ID입니다. 하나의 환승 피드는 두 개 이상의 여행사 데이터를 나타낼 수 있습니다. agency_id는 데이터 세트 고유의 식별자입니다. 이 필드는 단일 대행사에 대한 데이터만 포함하는 환승 피드에 대해 선택 사항입니다. SameAs: GTFS 정적 필드 정의의 'agency_id' 필드 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_lang[string]`: 이 운송업체에서 사용하는 기본 언어에 대한 두 글자 ISO 639-1 코드가 포함되어 있습니다. 언어 코드는 대소문자를 구분하지 않습니다(EN과 EN 모두 사용 가능). SameAs: GTFS 정적 필드 정의의 'agency_lang' 필드 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_name[string]`: 에이전시_이름 필드에는 운송업체의 전체 이름이 포함됩니다. SameAs: GTFS 정적 필드 정의의 'agency_name' 필드 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_timezone[string]`: 표준 시간대 필드에는 운송 대행사가 위치한 표준 시간대가 포함됩니다. SameAs: GTFS 정적 필드 정의의 'agency_timezone' 필드 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_url[string]`: agency_url 필드에는 운송 대행사의 URL이 포함됩니다. SameAs: GTFS 정적 필드 정의의 'agency_url' 필드 - agency.txt(https://developers.google.com/transit/gtfs/reference#agencytxt)  - `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrival[object]`: schedule_relationship이 비어 있거나 SCHEDULED인 경우 도착 또는 출발 중 하나를 StopTimeUpdate 내에 제공해야 합니다. SameAs: GTFS 실시간 메시지-StopTimeUpdate의 '도착' 필드(https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  	- `uncertainty[number]`: 불확실성을 생략하면 알 수 없는 것으로 해석됩니다. 완전히 확실한 예측을 지정하려면 불확실성을 0.SameAs로 설정합니다: '불확실성' 필드를 0으로 설정합니다. GTFS 실시간 메시지-StopTimeEvent(https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)    
- `arrivalUncertainty[number]`: schedule_relationship이 비어 있거나 SCHEDULED인 경우 도착 또는 출발 중 하나를 StopTimeUpdate 내에 제공해야 합니다. SameAs: GTFS 실시간 메시지-StopTimeUpdate의 '도착' 필드(https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `arrival_time[time]`: 경로의 특정 여행에 대한 특정 정류장 도착 시간을 지정합니다. 시간은 HH:MM:SS 형식의 8자리 숫자여야 합니다(시간이 0으로 시작하는 경우 HH:MM:SS도 허용됨). 참고: 여러 날짜에 걸쳐 있는 여행은 24:00:00보다 큰 정차 시간을 갖게 됩니다. 예를 들어, 오후 10:30:00에 시작하여 다음 날 오전 2:15:00에 끝나는 여행의 경우, 정차 시간은 22:30:00 및 26:15:00이 됩니다. 이러한 정차 시간을 22:30:00 및 02:15:00으로 입력하면 원하는 결과가 나오지 않습니다. SameAs: GTFS 정적 필드 정의-stop_times.txt의 '도착_시간' 필드(https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `bearing[number]`: 진북에서 시계 방향으로 측정된 차량 GPS 각도를 제공합니다. GTFS 실시간 메시지-위치(https://developers.google.com/transit/gtfs-realtime/reference#message-position)의 '방위' 필드와 동일합니다.  - `current_status[string]`: 이 관측에 해당하는 정차와 관련된 차량의 상태를 설명합니다. ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. 동일: GTFS 실시간 메시지-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 'current_status' 필드  - `current_stop_sequence[number]`: 현재 정류장의 정류장 시퀀스 인덱스를 제공합니다. 현재_상태가 누락된 경우 현재_상태를 고려하여 결정되며, IN_TRANSIT_TO가 가정됩니다. GTFS 실시간 메시지-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 SameAs:'current_stop_sequence' 필드  - `dataDescriptor[uri]`: 데이터 기술자 엔티티를 가리키는 URI  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `departure[object]`: schedule_relationship이 비어 있거나 SCHEDULED인 경우 도착 또는 출발 중 하나를 StopTimeUpdate 내에 제공해야 합니다. SameAs: GTFS 실시간 메시지-StopTimeUpdate(https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)의 '출발' 필드  	- `uncertainty[number]`: 불확실성을 생략하면 알 수 없는 것으로 해석됩니다. 완전히 확실한 예측을 지정하려면 불확실성을 0.SameAs로 설정합니다: '불확실성' 필드를 0으로 설정합니다. GTFS 실시간 메시지-StopTimeEvent(https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)    
- `departureUncertainty[number]`: schedule_relationship이 비어 있거나 SCHEDULED인 경우 도착 또는 출발 중 하나를 StopTimeUpdate 내에 제공해야 합니다. SameAs: GTFS 실시간 메시지-StopTimeUpdate(https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)의 '출발' 필드  - `departure_time[time]`: 경로의 특정 여정에 대한 특정 정류장에서 출발 시간을 지정합니다. 시간은 HH:MM:SS 형식의 8자리 숫자여야 합니다(시간이 0으로 시작하는 경우 HH:MM:SS도 허용됨).  
참고: 여러 날짜에 걸쳐 있는 여행은 24:00:00보다 큰 정차 시간을 갖게 됩니다. 예를 들어, 오후 10:30:00에 시작하여 다음 날 오전 2:15:00에 끝나는 여행의 경우, 정차 시간은 22:30:00 및 26:15:00이 됩니다. 이러한 정차 시간을 22:30:00 및 02:15:00으로 입력하면 원하는 결과가 나오지 않습니다. SameAs: GTFS 정적 필드 정의-stop_times.txt의 '출발_시간' 필드(https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `depotID[string]`: 이 관측에 해당하는 버스 차고지의 고유 ID를 설명합니다.  - `depotName[string]`: 이 관측에 해당하는 버스 차고지의 차고지 이름을 설명합니다.  - `depot_id[string]`: 이 관측에 해당하는 버스 차고지의 고유 ID를 설명합니다.  - `depot_name[string]`: 이 관측에 해당하는 버스 차고지의 차고지 이름을 설명합니다.  - `description[string]`: 이 항목에 대한 설명  - `deviceInfo[object]`: 관찰과 관련된 장치에 대한 정보  . Model: [https://schema.org/Text](https://schema.org/Text)	- `deviceBatteryStatus[string]`: 보고 장치의 배터리 충전 상태(연결됨, 연결 해제됨)를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceID[string]`: 이 관측에 해당하는 물리적 센서/측정 스테이션의 장치 ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceModel[object]`: 고려 중인 장치, 센서 또는 시스템의 정보를 설명합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceName[string]`: 이 관측에 해당하는 센서 장치/스테이션의 장치 이름 또는 스테이션 이름  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceSimNumber[string]`: 폐기물 관리 차량에 있는 기기의 심 번호를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `measurand[string]`: 장치에서 감지/관찰/측정된 속성/특성  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `rfID[string]`: RFID 리더의 ID를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `direction_id[number]`: 이 관측에 해당하는 차량의 이동 방향을 나타내며, GTFS 정적 피드 trips.txt에서 참조할 수 있습니다. SameAs: GTFS 실시간 메시지-TripDescriptor의 'direction_id' 필드(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `entity_id[string]`: 이 관측에 해당하는 엔티티에 대한 피드 고유 ID.SameAs:'entity_id' 필드를 GTFS 실시간 메시지-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)에서 가져옵니다.  - `id[*]`: 엔티티의 고유 식별자  - `last_stop_arrival_time[time]`: 경로의 특정 여행에 대한 이전 정류장 도착 시간을 지정합니다. 시간은 HH:MM:SS 형식의 8자리 숫자여야 합니다(시간이 0으로 시작하는 경우 H:MM:SS도 허용됨).  
참고: 여러 날짜에 걸쳐 있는 여행은 24:00:00보다 큰 정차 시간을 갖게 됩니다. 예를 들어, 오후 10:30:00에 시작하여 다음 날 오전 2:15:00에 끝나는 여행의 경우, 정차 시간은 22:30:00 및 26:15:00이 됩니다. 이러한 중지 시간을 22:30:00 및 02:15:00으로 입력하면 원하는 결과가 나오지 않습니다. 이는 GTFS 실시간 메시지-TripUpdate(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)의 stop_time_update(StopTimeUpdate) 메시지의 '도착' 필드에 절대 '시간'(StopTimeEvent)을 입력하는 것과 동일합니다.  - `last_stop_id[string]`: 이번 관측의 버스에 해당하는 이전 버스 정류장의 정류장 ID/정류장 이름입니다. SameAs: GTFS 실시간 메시지-차량 위치(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 'stop_id' 필드  - `last_tracked_time[date-time]`: 차량이 마지막으로 추적된 시간을 제공합니다.  - `license_plate[string]`: 차량의 번호판 번호를 제공합니다. SameAs: GTFS 실시간 메시지-차량 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)의 'license_plate' 필드  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `observationDateTime[date-time]`: 마지막으로 보고된 관찰 시간  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `position[object]`: 이 관측에 해당하는 차량의 현재 위치를 설명합니다. 동일: GTFS 실시간 메시지에서 가져온 위치 필드 - 차량 위치(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  . Model: [https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition](https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)	- `bearing[number]`: 방위(도)는 진북에서 시계 방향으로, 즉 0은 북쪽, 90은 동쪽입니다. 나침반 방위 또는 다음 경유지 또는 중간 위치로 향하는 방향일 수 있습니다. 클라이언트가 이전 데이터에서 계산할 수 있는 이전 위치 시퀀스에서 추론해서는 안 됩니다.    
	- `latitude[number]`: 북위 84도, WGS-84 좌표계 기준    
	- `longitude[number]`: 동경, WGS-84 좌표계 기준    
	- `odometer[number]`: 주행 거리계 값(미터)    
	- `speed[number]`: 차량이 측정한 순간 속도(초당 미터)    
- `positionInfo[object]`: 이 관측에 해당하는 차량의 현재 위치를 설명합니다. GTFS 실시간 메시지-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 SameAs:'위치' 필드  	- `bearing[number]`: 방위(도)는 진북에서 시계 방향으로, 즉 0은 북쪽, 90은 동쪽입니다. 나침반 방위 또는 다음 경유지 또는 중간 위치로 향하는 방향일 수 있습니다. 클라이언트가 이전 데이터에서 계산할 수 있는 이전 위치 시퀀스에서 추론해서는 안 됩니다.    
	- `odometer[number]`: 주행 거리계 값    
	- `speed[number]`: 차량이 측정한 순간 속도    
- `routeInfo[object]`: 이 관측에 해당하는 차량의 여행에 대해 정렬된 정류장 순서를 업데이트했으며, schedule_realionship이 취소된 경우 고려하지 않습니다. SameAs: GTFS 실시간 메시지-TripUpdate(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)의 'stop_time_update' 필드  	- `route_color[string]`: 할당된 경우 이 필드는 경로에 해당하는 색상을 정의합니다. 색상은 6자 16진수(예: 00FFFF)로 제공해야 합니다. 색상을 지정하지 않으면 기본 경로 색상은 흰색(FFFFFF)이 됩니다. SameAs: GTFS 정적 필드 정의-routes.txt(https://developers.google.com/transit/gtfs/reference#routestxt)의 'route_color' 필드    
	- `route_desc[string]`: 경로에 대한 설명. 여기에는 텍스트 설명 양식에 도착지와 출발지, 시간 정보를 포함한 전체 경로 세부 정보가 포함될 수 있습니다. SameAs: GTFS 정적 필드 정의-routes.txt(https://developers.google.com/transit/gtfs/reference#routestxt)의 'route_desc' 필드    
	- `route_id[string]`: 이 관측의 버스에 해당하는 버스/차량이 현재 운행 중인 경로에 할당된 경로 ID입니다.    
	- `route_long_name[string]`: 경로의 전체 이름입니다. 이 이름은 routeShortName보다 더 설명적이며 종종 경로의 목적지 또는 경유지를 포함합니다. 여기에는 주로 경로의 출발지 및 도착지 이름이 포함됩니다. SameAs: GTFS 정적 필드 정의-routes.txt의 'route_long_name' 필드(https://developers.google.com/transit/gtfs/reference#routestxt)    
	- `route_short_name[string]`: 경로의 짧은 이름. 402D와 같은 대중교통 차량의 보드 이름이나 라이더가 경로를 식별하는 데 사용하는 녹색과 같은 경우가 많습니다. SameAs: GTFS 정적 필드 정의-routes.txt(https://developers.google.com/transit/gtfs/reference#routestxt)의 'route_short_name' 필드    
	- `route_text_color[string]`: 이 필드는 route_color 배경에 그려지는 텍스트에 사용할 읽기 쉬운 색상을 지정하는 데 사용할 수 있습니다. 색상은 6자 16진수(예: FFD700)로 제공해야 합니다. 색상을 지정하지 않으면 기본 텍스트 색상은 검은색(000000)이 됩니다. SameAs: GTFS 정적 필드 정의-routes.txt의 'route_text_color' 필드(https://developers.google.com/transit/gtfs/reference#routestxt)    
	- `route_type[number]`: 교통수단 유형을 나타내는 숫자 - 1 - 지하철, 메트로. 대도시 지역 내의 모든 지하 철도 시스템. 2 - 철도. 시외 또는 장거리 여행에 사용됩니다. 3 - 버스. 단거리 및 장거리 버스 노선에 사용됩니다. SameAs: GTFS 정적 필드 정의-routes.txt의 'route_type' 필드(https://developers.google.com/transit/gtfs/reference#routestxt)    
	- `route_url[string]`: 해당 특정 경로에 대한 웹 페이지의 URL을 포함하며 agency_url과는 다릅니다. SameAs: GTFS 정적 필드 정의-routes.txt(https://developers.google.com/transit/gtfs/reference#routestxt)의 'route_url' 필드    
- `routeStopSequence[array]`: 이 관측에 해당하는 경로 또는 노선에 대해 올바른 순서로 정류장 ID/정류장 코드 또는 역 ID/역 코드를 제공합니다.  - `route_color[string]`: 할당된 경우 이 필드는 경로에 해당하는 색상을 정의합니다. 색상은 6자 16진수(예: 00FFFF)로 제공해야 합니다. 색상을 지정하지 않으면 기본 경로 색상은 흰색(FFFFFF)이 됩니다. SameAs: GTFS 정적 필드 정의-routes.txt(https://developers.google.com/transit/gtfs/reference#routestxt)의 'route_color' 필드  - `route_desc[string]`: 경로에 대한 설명. 여기에는 텍스트 설명 양식에 도착지와 출발지, 시간 정보를 포함한 전체 경로 세부 정보가 포함될 수 있습니다. SameAs: GTFS 정적 필드 정의-routes.txt(https://developers.google.com/transit/gtfs/reference#routestxt)의 'route_desc' 필드  - `route_id[string]`: 이 관측의 버스에 해당하는 버스/차량이 현재 운행 중인 경로에 할당된 경로 ID입니다. SameAs: GTFS 실시간 메시지-트립 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)의 'route_id' 필드  - `route_long_name[string]`: 경로의 전체 이름입니다. 이 이름은 routeShortName보다 더 설명적이며 종종 경로의 목적지 또는 경유지를 포함합니다. 여기에는 주로 경로의 출발지 및 도착지 이름이 포함됩니다. SameAs: GTFS 정적 필드 정의-routes.txt의 'route_long_name' 필드(https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_short_name[string]`: 경로의 짧은 이름. '402D' 또는 'Green'과 같이 라이더가 경로를 식별하는 데 사용하는 대중교통 차량의 보드 이름인 경우가 많습니다. SameAs: GTFS 정적 필드 정의-routes.txt(https://developers.google.com/transit/gtfs/reference#routestxt)의 'route_short_name' 필드  - `route_text_color[string]`: 이 필드는 route_color 배경에 그려지는 텍스트에 사용할 읽기 쉬운 색상을 지정하는 데 사용할 수 있습니다. 색상은 6자 16진수(예: FFD700)로 제공해야 합니다. 색상을 지정하지 않으면 기본 텍스트 색상은 검은색(000000)이 됩니다. SameAs: GTFS 정적 필드 정의-routes.txt의 'route_text_color' 필드(https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_type[string]`: 교통수단 유형을 나타내는 번호 1 - 지하철, 메트로. 대도시 지역 내의 모든 지하 철도 시스템.2 - 철도. 시외 또는 장거리 여행에 사용됩니다.3 - 버스. 단거리 및 장거리 버스 노선에 사용됩니다. SameAs: GTFS 정적 필드 정의-routes.txt(https://developers.google.com/transit/gtfs/reference#routestxt)의 'route_type' 필드  - `route_url[string]`: 해당 특정 경로에 대한 웹 페이지의 URL을 포함하며 agency_url과는 다릅니다. SameAs: GTFS 정적 필드 정의-routes.txt(https://developers.google.com/transit/gtfs/reference#routestxt)의 'route_url' 필드  - `schedule_relationship[string]`: 경로/여행이 예약되었는지 여부를 설명합니다. SameAs: enumScheduleRelationship의 'schedule_relationship' 필드(https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)  - `seating_capacity[number]`: 이 관측에 해당하는 차량의 승객 좌석 정원을 설명합니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `shapeInfo[object]`: 이 관측에 해당하는 차량이 이동하는 경로에 대한 정보  	- `shape_dist_traveled[number]`: 첫 번째 도형 지점에서 이 레코드에 지정된 지점까지 도형을 따라 이동한 실제 거리입니다. 여행 플래너에서 도형의 정확한 부분을 지도에 표시하는 데 사용됩니다. 모양_pt_sequence에 따라 값이 증가해야 하며, 경로를 따라 역방향으로 이동하는 데는 사용할 수 없습니다. 거리 단위는 stop_times.txt에 사용된 단위와 일치해야 합니다. 예시: 버스가 위에 정의된 세 지점을 따라 A_shp를 이동하는 경우, 추가 shape_dist_traveled 값(여기서는 킬로미터로 표시됨)은 다음과 같습니다: shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled A_shp,37.61956,-122.48161,0,0 A_shp,37.64430,-122.41070,6,6.8310 A_shp,37.65863,-122.30839,11,15.8765    
	- `shape_id[string]`: 도형을 식별합니다.    
	- `shape_pt_sequence[number]`: 도형 점이 연결되어 도형을 형성하는 순서입니다. 값은 이동을 따라 증가해야 하지만 연속적일 필요는 없습니다. 예시: 도형 A_shp의 정의에 세 개의 점이 있는 경우, 모양을 정의하는 shapes.txt 파일에 다음과 같은 레코드가 포함될 수 있습니다. 모양_id,모양_pt_lat,모양_pt_lon,모양_pt_sequence A_shp,37.61956,-122.48161,0 A_shp,37.64430,-122.41070,6 A_shp,37.65863,-122.30839,11    
- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `speed[number]`: 차량의 속도를 제공합니다. GTFS 실시간 메시지-위치(https://developers.google.com/transit/gtfs-realtime/reference#message-position)의 '속도' 필드와 동일합니다.  - `standing_capacity[number]`: 이 관측에 해당하는 차량의 승객 입석 정원을 설명합니다.  - `start_date[string]`: 이 관측에 해당하는 차량에 해당하는 여행의 초기 예정 날짜를 설명합니다. 이 필드의 예시 형식은 YYYYMMDD입니다. SameAs: GTFS 실시간 메시지-트립 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)의 'start_date' 필드  - `start_time[time]`: 이 관측에 해당하는 차량에 해당하는 여행의 최초 예정된 시작 시간을 설명합니다. 이 필드의 예시 형식은 11:15:35 또는 25:15:35입니다. SameAs: GTFS 실시간 메시지-트립 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)의 'start_time' 필드  - `stopInfo[object]`: 이 관측에 해당하는 차량이 이동하는 경로에 대한 정보  	- `stop_code[string]`: 이 필드에는 승객의 정류장을 고유하게 식별하는 짧은 텍스트 또는 숫자를 입력합니다. 공개용인 경우 stop_id와 동일할 수 있습니다. SameAs: GTFS 정적 필드 정의-stops.txt의 'stop_code' 필드(https://developers.google.com/transit/gtfs/reference#stopstxt)    
	- `stop_desc[string]`: 이 필드에는 정류장에 대한 설명이 포함되어 있습니다. SameAs: GTFS 정적 필드 정의-stops.txt의 'stop_desc' 필드(https://developers.google.com/transit/gtfs/reference#stopstxt)    
	- `stop_id[string]`: 이 관측에 해당하는 정류장에 할당된 고유 ID    
	- `stop_name[string]`: 정류장 또는 역의 이름을 설명합니다. SameAs: GTFS 정적 필드 정의-stops.txt의 'stop_name' 필드(https://developers.google.com/transit/gtfs/reference#stopstxt)    
	- `stop_url[string]`: 이 필드에는 특정 경유지에 대한 웹 페이지의 URL이 포함되며, 에이전시_url 및 노선_url 필드와는 다릅니다. SameAs: GTFS 정적 필드 정의-stops.txt의 'stop_url' 필드(https://developers.google.com/transit/gtfs/reference#stopstxt)    
- `stopTimeUpdateInfo[object]`: 이 관측에 해당하는 차량의 여행에 대해 정렬된 정류장 순서를 업데이트했으며, schedule_realionship이 취소된 경우 고려하지 않습니다. SameAs: GTFS 실시간 메시지-TripUpdate(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)의 'stop_time_update' 필드  	- `stopScheduleRelationship[string]`: 정적 스케줄과 스톱 간의 관계를 설명합니다. SameAs: GTFS 실시간 메시지의 'schedule_relationship' 필드-StopTimeUpdate ENUM[SCHEDULED, SKIPPED, NO_DATA] (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)    
	- `stop_id[string]`: 이 관측에 해당하는 정류장에 할당된 고유 ID    
	- `stop_sequence[number]`: 이 필드는 특정 여행의 경유지 순서를 식별합니다. stop_sequence의 값은 음수가 아닌 정수여야 하며, 여행에 따라 증가해야 합니다. 예를 들어, 여행의 첫 번째 경유지는 stop_sequence가 1, 두 번째 경유지는 stop_sequence가 23, 세 번째 경유지는 stop_sequence가 40이 될 수 있습니다.    
- `stopTimesInfo[object]`: 여행 중 차량의 일정에 대한 실시간 업데이트 설명자  	- `arrival_time[time]`: 경로의 특정 여행에 대한 특정 정류장 도착 시간을 지정합니다. 시간은 HH:MM:SS 형식의 8자리 숫자여야 합니다(시간이 0으로 시작하는 경우 HH:MM:SS도 허용됨). 참고: 여러 날짜에 걸쳐 있는 여행은 24:00:00보다 큰 정차 시간을 갖게 됩니다. 예를 들어, 오후 10:30:00에 시작하여 다음 날 오전 2:15:00에 끝나는 여행의 경우, 정차 시간은 22:30:00 및 26:15:00이 됩니다. 이러한 정차 시간을 22:30:00 및 02:15:00으로 입력하면 원하는 결과가 나오지 않습니다. SameAs: GTFS 정적 필드 정의-stop_times.txt의 '도착_시간' 필드(https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `continuous_drop_off[number]`: 라이더가 차량의 이동 경로를 따라 어느 지점에서든 환승 차량에서 하차할 수 있는지 여부를 나타냅니다.SameAs: GTFS 정적 필드 정의-stop_times.txt의 'continuous_drop_off' 필드(https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `continuous_pickup[number]`: 라이더가 차량의 이동 경로를 따라 어느 지점에서든 환승 차량에 탑승할 수 있는지 여부를 나타냅니다.SameAs: GTFS 정적 필드 정의-stop_times.txt의 '연속_픽업' 필드(https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `departure_time[time]`: 경로의 특정 여정에 대한 특정 정류장에서 출발 시간을 지정합니다. 시간은 HH:MM:SS 형식의 8자리 숫자여야 합니다(시간이 0으로 시작하는 경우 HH:MM:SS도 허용됨). 참고: 여러 날짜에 걸쳐 있는 여행은 24:00:00보다 큰 정차 시간을 갖게 됩니다. 예를 들어, 오후 10:30:00에 시작하여 다음 날 오전 2:15:00에 끝나는 여행의 경우, 정차 시간은 22:30:00 및 26:15:00이 됩니다. 이러한 정차 시간을 22:30:00 및 02:15:00으로 입력하면 원하는 결과가 나오지 않습니다. SameAs: GTFS 정적 필드 정의-stop_times.txt의 '출발_시간' 필드(https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `drop_off_type[string]`: 드롭오프 방법을 나타냅니다. SameAs: GTFS 정적 필드 정의-stop_times.txt(https://developers.google.com/transit/gtfs/reference#stop_timestxt)의 'drop_off_type' 필드    
	- `pickup_type[string]`: 픽업 방법을 나타냅니다: GTFS 정적 필드 정의-stop_times.txt의 'pickup_type' 필드(https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `stop_headsign[string]`: 이 필드에는 승객에게 여행의 목적지를 식별하는 표지판에 표시되는 텍스트가 포함됩니다. SameAs: GTFS 정적 필드 정의-stop_times.txt(https://developers.google.com/transit/gtfs/reference#stop_timestxt)의 'stop_headsign' 필드    
	- `stop_id[string]`: 이 관측에 해당하는 정류장에 할당된 고유 ID    
	- `stop_sequence[number]`: 이 필드는 특정 여행의 경유지 순서를 식별합니다. stop_sequence의 값은 음수가 아닌 정수여야 하며, 여행에 따라 증가해야 합니다. 예를 들어, 여행의 첫 번째 경유지는 stop_sequence가 1, 두 번째 경유지는 stop_sequence가 23, 세 번째 경유지는 stop_sequence가 40이 될 수 있습니다.    
	- `trip_id[string]`: 하루 중 시간과 주어진 경로의 여행 방향을 고려하여 이 관측에 해당하는 버스에 할당된 트립 ID/트립 이름입니다.    
- `stop_code[string]`: 이 필드에는 승객의 정류장을 고유하게 식별하는 짧은 텍스트 또는 숫자를 입력합니다. 공개용인 경우 stop_id와 동일할 수 있습니다. SameAs: GTFS 정적 필드 정의-stops.txt의 'stop_code' 필드(https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_desc[string]`: 이 필드에는 정류장에 대한 설명이 포함되어 있습니다. SameAs: GTFS 정적 필드 정의-stops.txt의 'stop_desc' 필드(https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_headsign[string]`: 이 필드에는 승객에게 여행의 목적지를 식별하는 표지판에 표시되는 텍스트가 포함됩니다. SameAs: GTFS 정적 필드 정의-stop_times.txt(https://developers.google.com/transit/gtfs/reference#stop_timestxt)의 'stop_headsign' 필드  - `stop_id[string]`: 이 관측에서 버스에 해당하는 버스 정류장의 정류장 ID/정류장 이름입니다. SameAs: GTFS 실시간 메시지-차량 위치(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 'stop_id' 필드  - `stop_name[string]`: 버스 정류장의 이름을 설명합니다. SameAs: GTFS 정적 필드 정의-stops.txt(https://developers.google.com/transit/gtfs/reference#stopstxt)의 'stop_name' 필드  - `stop_sequence[number]`: 이 관측에 해당하는 차량의 정지 시퀀스를 나타내며, GTFS 정적 피드 stop_times.txt에서 참조할 수 있습니다. SameAs: GTFS 실시간 메시지-StopTimeUpdate(https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)의 'stop_sequence' 필드  - `stop_sequence_detail[object]`: 대중교통 차량이 지정된 경로를 운행할 때 정차하는 순서를 설명합니다.SameAs: GTFS 정적 필드 정의-stop_times.txt의 'stop_sequence' 필드(https://developers.google.com/transit/gtfs/reference#stop_timestxt)  	- `stop_id[string]`: 해당 GTFS 피드에 있는 stops.txt와 동일해야 합니다. stop_sequence 또는 stop_id 중 하나는 StopTimeUpdate 내에 제공되어야 하며, 두 필드 모두 비어 있으면 안 됩니다.    
	- `stop_sequence[number]`: 해당 GTFS 피드에 있는 stop_times.txt와 동일해야 합니다. stop_sequence 또는 stop_id 중 하나는 StopTimeUpdate 내에 제공되어야 하며, 두 필드 모두 비워 둘 수 없습니다. stop_sequence는 예측이 어느 정류장에 대한 것인지 명확히 하기 위해 동일한 stop_id를 두 번 이상 방문하는 트립(예: 루프)에 필요합니다.    
- `stop_time_update[object]`: 이 여행을 제공하는 차량에 대한 추가 정보  	- `arrival[object]`: schedule_relationship이 비어 있거나 SCHEDULED인 경우 도착 또는 출발 중 하나를 StopTimeUpdate 내에 제공해야 하며, 두 필드 모두 비어 있을 수 없습니다. schedule_relationship이 SKIPPED인 경우 도착과 출발이 모두 비어 있을 수 있습니다. schedule_relationship이 NO_DATA인 경우 도착 및 출발이 비어 있어야 합니다.    
	- `departure[object]`: schedule_relationship이 비어 있거나 SCHEDULED인 경우 도착 또는 출발 중 하나를 StopTimeUpdate 내에 제공해야 하며, 두 필드 모두 비어 있을 수 없습니다. schedule_relationship이 SKIPPED인 경우 도착과 출발이 모두 비어 있을 수 있습니다. schedule_relationship이 NO_DATA인 경우 도착 및 출발이 비어 있어야 합니다.    
	- `schedule_relationship[string]`: Enum:'SCHEDULED, SKIPPED, NO_DATA'. SCHEDULED는 차량이 정해진 정차 스케줄에 따라 진행 중임을 의미하지만 반드시 스케줄의 시간에 따르지는 않습니다. 이것이 기본 동작입니다. 도착과 출발 중 하나 이상을 제공해야 합니다. 건너뛰기는 정류장을 건너뛰는 것, 즉 차량이 이 정류장에 정차하지 않음을 의미합니다. 도착 및 출발 필드는 선택 사항입니다. NO_DATA는 이 정류장에 대한 데이터가 제공되지 않음을 의미합니다. 사용 가능한 실시간 정보가 없음을 나타냅니다. NO_DATA를 설정하면 후속 정류장에 전파되므로 실시간 정보가 없는 정류장을 지정하는 데 권장되는 방법입니다. NO_DATA가 설정된 경우 도착 또는 출발 정보를 제공하지 않아야 합니다.    
	- `stop_id[string]`: 해당 GTFS 피드에 있는 stops.txt와 동일해야 합니다. stop_sequence 또는 stop_id 중 하나는 StopTimeUpdate 내에 제공되어야 하며, 두 필드 모두 비어 있으면 안 됩니다.    
	- `stop_sequence[number]`: 해당 GTFS 피드에 있는 stop_times.txt와 동일해야 합니다. stop_sequence 또는 stop_id 중 하나는 StopTimeUpdate 내에 제공되어야 하며, 두 필드 모두 비워 둘 수 없습니다. stop_sequence는 예측이 어느 정류장에 대한 것인지 명확히 하기 위해 동일한 stop_id를 두 번 이상 방문하는 트립(예: 루프)에 필요합니다.    
- `stop_url[string]`: 이 필드에는 특정 경유지에 대한 웹 페이지의 URL이 포함되며, 에이전시_url 및 노선_url 필드와는 다릅니다. SameAs: GTFS 정적 필드 정의-stops.txt의 'stop_url' 필드(https://developers.google.com/transit/gtfs/reference#stopstxt)  - `timestamp[date-time]`: 차량에서 마지막으로 보고된 관측 시간입니다. SameAs: GTFS 실시간 메시지-차량 위치(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 '타임스탬프' 필드  - `travelDistance[number]`: 출발지 버스 정류장과 목적지 버스 정류장 사이의 거리 또는 이 관측에 해당하는 총 이동 거리입니다.  - `travelTime[time]`: 이 관측에 해당하는 출발지 버스 정류장과 목적지 버스 정류장 간 이동에 걸린 시간을 HH:MM:SS 형식으로 표시합니다(시간이 0으로 시작하는 경우 HH:MM:SS도 허용됨).  - `trip[object]`: 이 관측에 해당하는 차량이 주행 중인 경로를 설명합니다. SameAs: GTFS 실시간 메시지-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)의 'trip' 필드  	- `direction_id[number]`: 이 관측에 해당하는 차량의 이동 방향을 나타내며, GTFS 정적 피드 trips.txt에서 참조할 수 있습니다. SameAs: GTFS 실시간 메시지-TripDescriptor의 'direction_id' 필드(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
	- `route_id[string]`: 이 관측의 버스에 해당하는 버스/차량이 현재 운행 중인 경로에 할당된 경로 ID입니다. SameAs: GTFS 실시간 메시지-트립 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)의 'route_id' 필드    
	- `schedule_relationship[string]`: 경로/여행이 예약되었는지 여부를 설명합니다. SameAs: enumScheduleRelationship의 'schedule_relationship' 필드(https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)    
	- `start_date[string]`: 이 관측에 해당하는 차량에 해당하는 여행의 초기 예정 날짜를 설명합니다. 이 필드의 예시 형식은 YYYYMMDD입니다. SameAs: GTFS 실시간 메시지-트립 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)의 'start_date' 필드    
	- `start_time[string]`: 이 관측에 해당하는 차량에 해당하는 여행의 최초 예정된 시작 시간을 설명합니다. 이 필드의 예시 형식은 11:15:35 또는 25:15:35입니다. SameAs: GTFS 실시간 메시지-트립 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)의 'start_time' 필드    
	- `trip_id[string]`: 하루 중 시간과 주어진 경로Id의 여행 방향을 고려하여 이 관측에 해당하는 버스에 할당된 트립 ID/트립 이름입니다. SameAs: GTFS 실시간 메시지-TripDescriptor의 'trip_id' 필드(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
- `tripDetails[object]`: 여행 중 차량의 일정에 대한 실시간 업데이트 설명자  	- `arrival_time[time]`:  경로의 특정 여행에 대한 특정 정류장 도착 시간을 지정합니다. 시간은 HH:MM:SS 형식의 8자리 숫자여야 합니다(시간이 0으로 시작하는 경우 HH:MM:SS도 허용됨). 참고: 여러 날짜에 걸쳐 있는 여행은 24:00:00보다 큰 정차 시간을 갖게 됩니다. 예를 들어, 오후 10:30:00에 시작하여 다음 날 오전 2:15:00에 끝나는 여행의 경우, 정차 시간은 22:30:00 및 26:15:00이 됩니다. 이러한 정차 시간을 22:30:00 및 02:15:00으로 입력하면 원하는 결과가 나오지 않습니다. SameAs: GTFS 정적 필드 정의-stop_times.txt의 '도착_시간' 필드(https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `departure_time[time]`: 경로의 특정 여정에 대한 특정 정류장에서 출발 시간을 지정합니다. 시간은 HH:MM:SS 형식의 8자리 숫자여야 합니다(시간이 0으로 시작하는 경우 HH:MM:SS도 허용됨). 참고: 여러 날짜에 걸쳐 있는 여행은 24:00:00보다 큰 정차 시간을 갖게 됩니다. 예를 들어, 오후 10:30:00에 시작하여 다음 날 오전 2:15:00에 끝나는 여행의 경우, 정차 시간은 22:30:00 및 26:15:00이 됩니다. 이러한 정차 시간을 22:30:00 및 02:15:00으로 입력하면 원하는 결과가 나오지 않습니다. SameAs: GTFS 정적 필드 정의-stop_times.txt의 '출발_시간' 필드(https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `stop_headsign[string]`: 이 필드에는 승객에게 여행의 목적지를 식별하는 표지판에 표시되는 텍스트가 포함됩니다. SameAs: GTFS 정적 필드 정의-stop_times.txt(https://developers.google.com/transit/gtfs/reference#stop_timestxt)의 'stop_headsign' 필드    
	- `stop_id[string]`: 이 관측에서 버스에 해당하는 버스 정류장의 정류장 ID/정류장 이름입니다. SameAs: GTFS 실시간 메시지-차량 위치(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 'stop_id' 필드    
	- `stop_sequence[number]`: 이 관측에 해당하는 차량의 정지 시퀀스를 나타내며, GTFS 정적 피드 stop_times.txt에서 참조할 수 있습니다. SameAs: GTFS 실시간 메시지-StopTimeUpdate(https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)의 'stop_sequence' 필드    
- `tripDirection[string]`: 차량이 이동 중인 방향을 ENUM[UP,DN]으로 지정합니다.  - `tripInfo[object]`: 이 관측에 해당하는 차량이 주행 중인 경로를 설명합니다. SameAs: GTFS 실시간 메시지-차량 위치(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 'trip' 필드  	- `route_id[string]`: 이 관측의 버스에 해당하는 버스/차량이 현재 운행 중인 경로에 할당된 경로 ID입니다.    
	- `schedule_relationship[string]`: 경로/여행이 예약되었는지 여부를 설명합니다. SameAs: GTFS 실시간 메시지-트립 설명자 ENUM[SCHEDULED, ADDED, UNSCHEDULED, CANCELED] (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)의 'schedule_relationship' 필드    
	- `start_date[string]`: 이 관측에 해당하는 차량에 해당하는 여행의 초기 예정 날짜를 설명합니다. 이 필드의 예시 형식은 YYYYMMDD입니다. SameAs: GTFS 실시간 메시지-트립 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)의 'start_date' 필드    
	- `start_time[time]`: 이 관측에 해당하는 차량에 해당하는 여행의 최초 예정된 시작 시간을 설명합니다. 이 필드의 예시 형식은 11:15:35 또는 25:15:35입니다. SameAs: GTFS 실시간 메시지-트립 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)의 'start_time' 필드    
	- `trip_direction[string]`: 이 관측에 해당하는 차량의 이동 방향을 나타내며, GTFS 정적 피드 trips.txt에서 참조할 수 있습니다. SameAs: GTFS 실시간 메시지-TripDescriptor의 'direction_id' 필드(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
	- `trip_id[string]`: 하루 중 시간과 주어진 경로의 여행 방향을 고려하여 이 관측에 해당하는 버스에 할당된 트립 ID/트립 이름입니다.    
- `trip_delay[number]`: 이 값은 초 단위로 양수 및 음수일 수 있으며 차량이 계획된 차량에서 얼마나 벗어났는지 보여줍니다. SameAs: GTFS 실시간 메시지의 '지연' 필드-StopTimeEvent(https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)  - `trip_details[object]`: 여행 중 차량의 일정에 대한 실시간 업데이트 설명자  	- `bearing[number]`: 방위(도)는 진북에서 시계 방향으로, 즉 0은 북쪽, 90은 동쪽입니다. 나침반 방위 또는 다음 경유지 또는 중간 위치로 향하는 방향일 수 있습니다. 클라이언트가 이전 데이터에서 계산할 수 있는 이전 위치 시퀀스에서 추론해서는 안 됩니다.    
	- `odometer[number]`: 주행 거리계 값(미터)    
	- `speed[number]`: 차량이 측정한 순간 속도(초당 미터)    
- `trip_direction[string]`: 차량이 주행 중인 방향을 지정합니다. SameAs: GTFS 실시간 메시지-트립 설명자의 'direction_id' 필드와 동일하지만 'direction_id'(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)에서 볼 수 있듯이 [0,1] 대신 ENUM[UP,DN] 형태로 표현됩니다.  - `trip_id[string]`: 하루 중 시간과 주어진 경로Id의 여행 방향을 고려하여 이 관측에 해당하는 버스에 할당된 트립 ID/트립 이름입니다. SameAs: GTFS 실시간 메시지-TripDescriptor의 'trip_id' 필드(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `trip_update[object]`: 해당 관측에 해당하는 차량의 운행에 대한 지연, 출발 등의 운행 정보를 설명합니다.SameAs: GTFS 실시간 메시지-피드엔티티(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)의 'trip_update' 필드입니다.  	- `stop_time_update[object]`: 이 여행을 제공하는 차량에 대한 추가 정보    
	- `timestamp[date-time]`: 차량에서 마지막으로 보고된 관측 시간입니다. SameAs: GTFS 실시간 메시지-차량 위치(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 '타임스탬프' 필드    
	- `trip[object]`: 이 관측에 해당하는 차량이 주행 중인 경로를 설명합니다. SameAs: GTFS 실시간 메시지-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)의 'trip' 필드    
	- `vehicleDesc[object]`: 해당 관측에 해당하는 차량의 추가 정보를 설명합니다. SameAs: GTFS 실시간 메시지 - 차량 위치(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)의 '차량' 필드    
- `type[string]`: NGSI 엔티티 유형. TransitManagement여야 합니다.  - `uncertainty[number]`: 불확실성을 생략하면 알 수 없는 것으로 해석됩니다. 완전히 확실한 예측을 지정하려면 불확실성을 0.SameAs로 설정합니다: '불확실성' 필드를 0으로 설정합니다. GTFS 실시간 메시지-StopTimeEvent(https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)  - `vehicleDesc[object]`: 해당 관측에 해당하는 차량의 추가 정보를 설명합니다. SameAs: GTFS 실시간 메시지 - 차량 위치(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)의 '차량' 필드  	- `license_plate[string]`: 차량의 번호판 번호를 제공합니다: GTFS 실시간 메시지의 'license_plate' 필드 - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)    
	- `vehicle_id[string]`: 이 관측에 해당하는 차량에 할당된 고유 ID로, 내부 시스템 식별에 사용됩니다.SameAs: GTFS 실시간 메시지의 'id' 필드 - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)    
	- `vehicle_label[string]`: 사용자가 볼 수 있는 레이블, 즉 올바른 차량을 식별하는 데 도움이 되도록 승객에게 표시해야 하는 항목입니다: GTFS 실시간 메시지의 '레이블' 필드 - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)    
- `vehicleInfo[object]`: 해당 관측에 해당하는 차량의 추가 정보를 설명합니다. SameAs: GTFS 실시간 메시지 - 차량 위치(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)의 '차량' 필드  	- `license_plate[string]`: 차량의 번호판 번호를 제공합니다. SameAs: GTFS 실시간 메시지-차량 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)의 'license_plate' 필드    
	- `vehicleID[string]`: 이 관측에 해당하는 차량에 할당된 고유 ID로, 내부 시스템 식별에 사용됩니다. SameAs: GTFS 실시간 메시지-차량 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)의 'id' 필드    
	- `vehicle_label[string]`: 사용자가 볼 수 있는 라벨, 즉 올바른 차량을 식별하기 위해 승객에게 보여줘야 하는 라벨입니다. SameAs: GTFS 실시간 메시지-차량 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)의 '레이블' 필드    
- `vehiclePositionInfo[object]`: 이 관측에 해당하는 차량의 실시간 위치를 설명합니다. GTFS 실시간 메시지-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)의 SameAs:'vehicle' 필드  	- `congestion_level[string]`: 이 차량에 영향을 미치는 혼잡 수준을 설명합니다. 열거형 [알 수 없는_혼잡_수준, 원활하게_달리고_있음, 스톱_앤_고, 혼잡, 심한_혼잡]    
	- `current_status[string]`: 이 관측에 해당하는 정차와 관련된 차량의 상태를 설명합니다. ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. 동일: GTFS 실시간 메시지-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 'current_status' 필드    
	- `current_stop_sequence[number]`: 현재 정류장의 정류장 시퀀스 인덱스를 제공합니다. 현재_상태가 누락된 경우 현재_상태를 고려하여 결정되며, IN_TRANSIT_TO가 가정됩니다. GTFS 실시간 메시지-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 SameAs:'current_stop_sequence' 필드    
	- `occupancy_status[string]`: 차량의 승객 탑승 정도입니다. ENUM [비어 있음, 많은_좌석_가능, 적은_좌석_가능, 입석_전용, 크러시_입석_전용, 가득 차 있음, 승객_수용 불가, NO_DATA_USABLE, 탑승 불가]    
	- `stop_id[string]`: 이 관측에 해당하는 정류장에 할당된 고유 ID    
- `vehicleType[string]`: 이 관측에 해당하는 차량 유형을 설명하며, 고형 폐기물 관리 차량의 경우 호퍼, 압축기, 티퍼, 덤퍼, ITMS 차량의 경우 BRT 미니버스, BRT 버스, 시내버스, 긴급 차량의 경우 구급차, 소방차, 경찰차 등, 차량 등록의 경우 오토바이/스쿠터, 모터사이클, 오토릭쇼, 자가용/지프차, 템포, 버스, e-모페드/스쿠터/오토바이, 공용 모터가 해당될 수 있습니다.  - `vehicle_id[string]`: 이 관측에 해당하는 차량에 할당된 고유 ID로, 내부 시스템 식별에 사용됩니다. SameAs: GTFS 실시간 메시지-차량 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)의 'id' 필드  - `vehicle_label[string]`: 사용자가 볼 수 있는 라벨, 즉 올바른 차량을 식별하기 위해 승객에게 보여줘야 하는 라벨입니다. SameAs: GTFS 실시간 메시지-차량 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)의 '레이블' 필드  - `vehicle_position[object]`: 이 관측에 해당하는 차량의 실시간 위치를 설명합니다. GTFS 실시간 메시지-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)의 SameAs:'vehicle' 필드  	- `current_status[string]`: 이 관측에 해당하는 정차와 관련된 차량의 상태를 설명합니다. ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. 동일: GTFS 실시간 메시지-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 'current_status' 필드    
	- `current_stop_sequence[number]`: 현재 정류장의 정류장 시퀀스 인덱스를 제공합니다. 현재_상태가 누락된 경우 현재_상태를 고려하여 결정되며, IN_TRANSIT_TO가 가정됩니다. GTFS 실시간 메시지-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 SameAs:'current_stop_sequence' 필드    
	- `position[object]`: 이 관측에 해당하는 차량의 현재 위치를 설명합니다. SameAs: GTFS 실시간 메시지-차량 위치(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 '위치' 필드    
	- `stop_id[string]`: 이 관측에서 버스에 해당하는 버스 정류장의 정류장 ID/정류장 이름입니다. SameAs: GTFS 실시간 메시지-차량 위치(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 'stop_id' 필드    
	- `timestamp[date-time]`: 차량에서 마지막으로 보고된 관측 시간입니다. SameAs:  GTFS 실시간 메시지-차량 위치(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)의 '타임스탬프' 필드    
	- `trip[object]`: 이 관측에 해당하는 차량이 주행 중인 경로를 설명합니다. SameAs: GTFS 실시간 메시지-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)의 'trip' 필드    
	- `vehicleDesc[object]`: 해당 관측에 해당하는 차량의 추가 정보를 설명합니다. SameAs: GTFS 실시간 메시지 - 차량 위치(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)의 '차량' 필드    
<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TransitManagement:    
  description: A public transit system Data Model    
  properties:    
    acAvailable:    
      description: Describes the presence of air conditioning option in the vehicle corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    ac_available:    
      description: Describes the presence of air conditioning option in the vehicle corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    actual_trip_end_time:    
      description: This field specifies the time at which service or trip corresponding to this observation is scheduled to end    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    actual_trip_start_time:    
      description: "This field specifies the time at which service actually began.  This is SameAs: absolute 'time'(StopTimeEvent) in the 'arrival' field of the stop_time_update (StopTimeUpdate) message of the GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
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
    agencyInfo:    
      description: Agency information corresponding to this observation    
      properties:    
        agency_email:    
          description: "Email address actively monitored by the agency’s customer service department. SameAs: 'agency_email' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        agency_fare_url:    
          description: "URL of a web page that contains the details of the fares and also could allow to purchase tickets for that agency online. SameAs: 'agency_fare_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        agency_id:    
          description: "ID that uniquely identifies a transit agency. A transit feed may represent data from more than one agency. The agency_id is dataset unique. This field is optional for transit feeds that only contain data for a single agency. SameAs: 'agency_id' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        agency_lang:    
          description: "Contains a two-letter ISO 639-1 code for the primary language used by this transit agency. The language code is case-insensitive (both en and EN are accepted). SameAs: 'agency_lang' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        agency_name:    
          description: "The agency_name field contains the full name of the transit agency. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        agency_phone:    
          description: "A voice telephone number for the specified agency.SameAs: 'agency_phone' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        agency_timezone:    
          description: "Timezone field contains the timezone where the transit agency is located. SameAs: 'agency_timezone' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        agency_url:    
          description: "The agency_url field contains the URL of the transit agency. SameAs: 'agency_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    agency_fare_url:    
      description: "URL of a web page that contains the details of the fares and also could allow to purchase tickets for that agency online. SameAs: 'agency_fare_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    agency_id:    
      description: "ID that uniquely identifies a transit agency. A transit feed may represent data from more than one agency. The agency_id is dataset unique. This field is optional for transit feeds that only contain data for a single agency. SameAs: 'agency_id' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    agency_lang:    
      description: "Contains a two-letter ISO 639-1 code for the primary language used by this transit agency. The language code is case-insensitive (both en and EN are accepted). SameAs: 'agency_lang' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    agency_name:    
      description: "The agency_name field contains the full name of the transit agency. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    agency_timezone:    
      description: "Timezone field contains the timezone where the transit agency is located. SameAs: 'agency_timezone' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    agency_url:    
      description: "The agency_url field contains the URL of the transit agency. SameAs: 'agency_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
      type: string    
      x-ngsi:    
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
    arrival:    
      description: "If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'arrival' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"    
      properties:    
        uncertainty:    
          description: "If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    arrivalUncertainty:    
      description: "If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'arrival' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"    
      type: number    
      x-ngsi:    
        type: Property    
    arrival_time:    
      description: "Specifies the arrival time at a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'arrival_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
      format: time    
      type: string    
      x-ngsi:    
        type: Property    
    bearing:    
      description: "Gives the vehicle GPS angle measured in a clockwise direction from the True North. SameAs 'bearing' field from GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)"    
      type: number    
      x-ngsi:    
        type: Property    
    current_status:    
      description: "Describes the status of the vehicle w.r.t the stop corresponding to this observation ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. SameAs:'current_status' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
      type: string    
      x-ngsi:    
        type: Property    
    current_stop_sequence:    
      description: "Gives the stop sequence index of the current stop. This is determined by considering current_status, if current_status is missing IN_TRANSIT_TO is assumed. SameAs:'current_stop_sequence' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
      type: number    
      x-ngsi:    
        type: Property    
    dataDescriptor:    
      description: URI pointing to the data-descriptor entity    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    departure:    
      description: "If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'departure' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"    
      properties:    
        uncertainty:    
          description: "If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    departureUncertainty:    
      description: "If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'departure' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"    
      type: number    
      x-ngsi:    
        type: Property    
    departure_time:    
      description: "Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). \nNote: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
      format: time    
      type: string    
      x-ngsi:    
        type: Property    
    depotID:    
      description: Describes the unique id of the bus depot corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    depotName:    
      description: Describes the depot name of the bus depot corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    depot_id:    
      description: Describes the unique id of the bus depot corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    depot_name:    
      description: Describes the depot name of the bus depot corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    deviceInfo:    
      description: Information about the device associated with the observations    
      properties:    
        deviceBatteryStatus:    
          description: 'Gives the Battery charging status of the reporting device(Connected, Disconnected)'    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        deviceID:    
          description: Device ID of the physical sensor/ measurement station corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        deviceModel:    
          description: 'Describes the information of the device, sensor or system in consideration'    
          properties:    
            brandName:    
              description: 'Name of the brand associated with an entity, e.g., sensor, device etc'    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            manufacturerName:    
              description: 'Name of the manufacturer associated with an entity, e.g., sensor, device etc'    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            modelName:    
              description: 'Name of a specific model associated with an entity, e.g., sensor, device etc'    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            modelURL:    
              description: 'URL providing further information of a specific model associated with an entity, e.g., sensor, device etc'    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            observationDateTime:    
              description: Last reported time of observation    
              format: date-time    
              type: string    
              x-ngsi:    
                type: Property    
            trip_update:    
              description: "Describes the trip information like delay, departures, etc., for a trip made by the vehicle corresponding to this observation.SameAs:'trip_update' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"    
              properties:    
                trip:    
                  description: 'Following the conventions of GTFS trip. '    
                  properties:    
                    direction_id:    
                      type: number    
                    route_id:    
                      type: string    
                    schedule_relationship:    
                      enum:    
                        - SCHEDULED    
                        - ADDED    
                        - UNSCHEDULED    
                        - CANCELED    
                      type: string    
                    start_date:    
                      type: string    
                    start_time:    
                      type: string    
                    trip_id:    
                      type: string    
                  type: object    
                  x-ngsi:    
                    model: "https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor"    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        deviceName:    
          description: Device Name or Station name of the sensor device/station corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        deviceSimNumber:    
          description: Gives the sim number of the device in the waste management vehicle    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        measurand:    
          description: Property/properties sensed/observed/measured by the device    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        rfID:    
          description: Gives the ID of the RFID reader    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    direction_id:    
      description: "Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: number    
      x-ngsi:    
        type: Property    
    entity_id:    
      description: "Feed unique ID for the entity corresponding to this observation.SameAs:'entity_id' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"    
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
    last_stop_arrival_time:    
      description: "Specifies the arrival time at the previous stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (H:MM:SS is also accepted, if the hour begins with 0). \nNote: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. This is SameAs: absolute 'time'(StopTimeEvent) in the 'arrival' field of the stop_time_update (StopTimeUpdate) message of the GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
      format: time    
      type: string    
      x-ngsi:    
        type: Property    
    last_stop_id:    
      description: "Stop ID/Stop name of the previous bus stop corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-VehiclePosition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
      type: string    
      x-ngsi:    
        type: Property    
    last_tracked_time:    
      description: Gives the time at which the vehicle was last tracked    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    license_plate:    
      description: "Gives the License Plate number of the vehicle. SameAs: 'license_plate' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
      type: string    
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
    observationDateTime:    
      description: Last reported time of observation    
      format: date-time    
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
    position:    
      description: "Describes the current position of the vehicle corresponding to this observation. SameAs: position field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
      properties:    
        bearing:    
          description: 'Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data'    
          type: number    
          x-ngsi:    
            type: Property    
        latitude:    
          description: 'Degrees North, in the WGS-84 coordinate system'    
          type: number    
          x-ngsi:    
            type: Property    
        longitude:    
          description: 'Degrees East, in the WGS-84 coordinate system'    
          type: number    
          x-ngsi:    
            type: Property    
        odometer:    
          description: 'Odometer value, in meters'    
          type: number    
          x-ngsi:    
            type: Property    
            units: meters    
        speed:    
          description: 'Momentary speed measured by the vehicle, in meters per second'    
          type: number    
          x-ngsi:    
            type: Property    
            units: meters per second    
      type: object    
      x-ngsi:    
        model: "https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition"    
        type: Property    
    positionInfo:    
      description: "Describes the current position of the vehicle corresponding to this observation. SameAs:'position' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
      properties:    
        bearing:    
          description: 'Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data'    
          type: number    
          x-ngsi:    
            type: Property    
        odometer:    
          description: Odometer value    
          type: number    
          x-ngsi:    
            type: Property    
        speed:    
          description: Momentary speed measured by the vehicle    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    routeInfo:    
      description: "Updated sorted stop sequence for the trip made by the vehicle corresponding to this observation, not to be considered if schedule_realtionship is CANCELED. SameAs: 'stop_time_update' field from GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
      properties:    
        route_color:    
          description: "If assigned, this field defines a color that corresponds to a route. The color must be provided as a six-character hexadecimal number, for example, 00FFFF. If no color is specified, the default route color is white (FFFFFF). SameAs: 'route_color' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        route_desc:    
          description: "Description of the route. This can include the entire route details including to and from destination and timing information in a text description form. SameAs: 'route_desc' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        route_id:    
          description: Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on    
          type: string    
          x-ngsi:    
            type: Property    
        route_long_name:    
          description: "Full name of a route. This name is more descriptive than the routeShortName and often includes the route's destination or stop. This mostly includes the to and from destination names of the route. SameAs: 'route_long_name' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        route_short_name:    
          description: "Short name of a route. This will often be the transit vehicle's board name like 402D, or Green that riders use to identify a route. SameAs: 'route_short_name' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        route_text_color:    
          description: "This field can be used to specify a legible color to use for text drawn against a background of route_color. The color must be provided as a six-character hexadecimal number, for example, FFD700. If no color is specified, the default text color is black (000000). SameAs: 'route_text_color' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        route_type:    
          description: "Number indicating the type of transport- 1 - Subway, Metro. Any underground rail system within a metropolitan area. 2 - Rail. Used for intercity or long-distance travel. 3 - Bus. Used for short- and long-distance bus routes. SameAs: 'route_type' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"    
          type: number    
          x-ngsi:    
            type: Property    
        route_url:    
          description: "Contains the URL of a web page about that particular route and is different from the agency_url. SameAs: 'route_url' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    routeStopSequence:    
      description: Gives the stop IDs/stop codes or station IDs/station codes in the right sequence for the route or line corresponding to this observation    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    route_color:    
      description: "If assigned, this field defines a color that corresponds to a route. The color must be provided as a six-character hexadecimal number, for example, 00FFFF. If no color is specified, the default route color is white (FFFFFF). SameAs: 'route_color' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    route_desc:    
      description: "Description of the route. This can include the entire route details including to and from destination and timing information in a text description form. SameAs: 'route_desc' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    route_id:    
      description: "Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: string    
      x-ngsi:    
        type: Property    
    route_long_name:    
      description: "Full name of a route. This name is more descriptive than the routeShortName and often includes the route's destination or stop. This mostly includes the to and from destination names of the route. SameAs: 'route_long_name' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    route_short_name:    
      description: "Short name of a route. This will often be the transit vehicle's board name like '402D',  or 'Green' that riders use to identify a route. SameAs: 'route_short_name' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    route_text_color:    
      description: "This field can be used to specify a legible color to use for text drawn against a background of route_color. The color must be provided as a six-character hexadecimal number, for example, FFD700. If no color is specified, the default text color is black (000000). SameAs: 'route_text_color' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    route_type:    
      description: "Number indicating the type of transport-1 - Subway, Metro. Any underground rail system within a metropolitan area.2 - Rail. Used for intercity or long-distance travel.3 - Bus. Used for short- and long-distance bus routes. SameAs: 'route_type' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    route_url:    
      description: "Contains the URL of a web page about that particular route and is different from the agency_url. SameAs: 'route_url' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    schedule_relationship:    
      description: "Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)"    
      type: string    
      x-ngsi:    
        type: Property    
    seating_capacity:    
      description: Describes the passenger seating capacity of the vehicle corresponding to this observation    
      type: number    
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
    shapeInfo:    
      description: Information about the path the vehicle corresponding to this observation travels along    
      properties:    
        shape_dist_traveled:    
          description: 'Actual distance traveled along the shape from the first shape point to the point specified in this record. Used by trip planners to show the correct portion of the shape on a map. Values must increase along with shape_pt_sequence; they cannot be used to show reverse travel along a route. Distance units must be consistent with those used in stop_times.txt. Example: If a bus travels along the three points defined above for A_shp, the additional shape_dist_traveled values (shown here in kilometers) would look like this: shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled A_shp,37.61956,-122.48161,0,0 A_shp,37.64430,-122.41070,6,6.8310 A_shp,37.65863,-122.30839,11,15.8765'    
          type: number    
          x-ngsi:    
            type: Property    
        shape_id:    
          description: Identifies a shape    
          type: string    
          x-ngsi:    
            type: Property    
        shape_pt_sequence:    
          description: 'Sequence in which the shape points connect to form the shape. Values must increase along the trip but do not need to be consecutive. Example: If the shape A_shp has three points in its definition, the shapes.txt file might contain these records to define the shape: shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence A_shp,37.61956,-122.48161,0 A_shp,37.64430,-122.41070,6 A_shp,37.65863,-122.30839,11'    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    speed:    
      description: "Gives the Speed  of the vehicle. SameAs 'speed' field from GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)"    
      type: number    
      x-ngsi:    
        type: Property    
    standing_capacity:    
      description: Describes the passenger standing capacity of the vehicle corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    start_date:    
      description: "Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: string    
      x-ngsi:    
        type: Property    
    start_time:    
      description: "Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      format: time    
      type: string    
      x-ngsi:    
        type: Property    
    stopInfo:    
      description: Information about the path the vehicle corresponding to this observation travels along    
      properties:    
        stop_code:    
          description: "This field contains short text or a number that uniquely identifies the stop for passengers. Can be same as stop_id if it is for public. SameAs: 'stop_code' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        stop_desc:    
          description: "This field contains a description of a stop. SameAs: 'stop_desc' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        stop_id:    
          description: Unique ID assigned to the stop corresponding to this observation    
          type: string    
          x-ngsi:    
            type: Property    
        stop_name:    
          description: "Describes the name of a stop or station. SameAs: 'stop_name' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        stop_url:    
          description: "This field contains the URL of a web page about a particular stop and is different from the agency_url and the route_url fields. SameAs: 'stop_url' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    stopTimeUpdateInfo:    
      description: "Updated sorted stop sequence for the trip made by the vehicle corresponding to this observation, not to be considered if schedule_realtionship is CANCELED. SameAs: 'stop_time_update' field from GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
      properties:    
        stopScheduleRelationship:    
          description: "Describes the relationship between the static schedule and the stop. SameAs: 'schedule_relationship' field from GTFS Realtime message-StopTimeUpdate ENUM[SCHEDULED, SKIPPED, NO_DATA] (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"    
          type: string    
          x-ngsi:    
            type: Property    
        stop_id:    
          description: Unique ID assigned to the stop corresponding to this observation    
          type: string    
          x-ngsi:    
            type: Property    
        stop_sequence:    
          description: 'This field identifies the order of the stops for a particular trip. The values for stop_sequence must be non-negative integers, and they must increase along the trip. For example, the first stop on the trip could have a stop_sequence of 1, the second stop on the trip could have a stop_sequence of 23, the third stop could have a stop_sequence of 40, and so on'    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    stopTimesInfo:    
      description: A descriptor of realtime update on the schedule of a vehicle along a trip    
      properties:    
        arrival_time:    
          description: "Specifies the arrival time at a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'arrival_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
          format: time    
          type: string    
          x-ngsi:    
            type: Property    
        continuous_drop_off:    
          description: "Indicates whether a rider can alight from the transit vehicle at any point along the vehicle’s travel path.SameAs: 'continuous_drop_off' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
          type: number    
          x-ngsi:    
            type: Property    
        continuous_pickup:    
          description: "Indicates whether a rider can board the transit vehicle at any point along the vehicle’s travel path.SameAs: 'continuous_pickup' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
          type: number    
          x-ngsi:    
            type: Property    
        departure_time:    
          description: "Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
          format: time    
          type: string    
          x-ngsi:    
            type: Property    
        drop_off_type:    
          description: "Indicates drop off method. SameAs: 'drop_off_type' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        pickup_type:    
          description: "Indicates pickup method.SameAs: 'pickup_type' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        stop_headsign:    
          description: "This field contains the text that appears on a sign that identifies the trip’s destination to passengers. SameAs: 'stop_headsign' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        stop_id:    
          description: Unique ID assigned to the stop corresponding to this observation    
          type: string    
          x-ngsi:    
            type: Property    
        stop_sequence:    
          description: 'This field identifies the order of the stops for a particular trip. The values for stop_sequence must be non-negative integers, and they must increase along the trip. For example, the first stop on the trip could have a stop_sequence of 1, the second stop on the trip could have a stop_sequence of 23, the third stop could have a stop_sequence of 40, and so on'    
          type: number    
          x-ngsi:    
            type: Property    
        trip_id:    
          description: 'Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId'    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    stop_code:    
      description: "This field contains short text or a number that uniquely identifies the stop for passengers. Can be same as stop_id if it is for public. SameAs: 'stop_code' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    stop_desc:    
      description: "This field contains a description of a stop. SameAs: 'stop_desc' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    stop_headsign:    
      description: "This field contains the text that appears on a sign that identifies the trip’s destination to passengers. SameAs: 'stop_headsign' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    stop_id:    
      description: "Stop ID/Stop name of the bus stops corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
      type: string    
      x-ngsi:    
        type: Property    
    stop_name:    
      description: "Describes the name of the Bus Stop. SameAs: 'stop_name' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    stop_sequence:    
      description: "Indicates the stop sequence of the vehicle corresponding to this observation, can be referenced from the GTFS static feed stop_times.txt. SameAs: 'stop_sequence' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"    
      type: number    
      x-ngsi:    
        type: Property    
    stop_sequence_detail:    
      description: "Describes the stop sequence for a trip in the designated route made by the public transit vehicle.SameAs: 'stop_sequence' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
      properties:    
        stop_id:    
          description: Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty    
          type: string    
          x-ngsi:    
            type: Property    
        stop_sequence:    
          description: 'Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for'    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    stop_time_update:    
      description: Additional information on the vehicle that is serving this trip    
      properties:    
        arrival:    
          description: 'If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty'    
          properties:    
            uncertainty:    
              description: "If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"    
              type: number    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        departure:    
          description: 'If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty'    
          properties:    
            uncertainty:    
              description: "If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"    
              type: number    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        schedule_relationship:    
          description: 'Enum:''SCHEDULED, SKIPPED, NO_DATA''. SCHEDULED means that the vehicle is proceeding in accordance with its static schedule of stops, although not necessarily according to the times of the schedule. This is the default behavior. At least one of arrival and departure must be provided. SKIPPED means that The stop is skipped, i.e., the vehicle will not stop at this stop. The arrival and departure fields are optional. NO_DATA means that no data is given for this stop. It indicates that there is no realtime information available. When set NO_DATA is propagated through subsequent stops so this is the recommended way of specifying from which stop you do not have realtime information. When NO_DATA is set neither arrival nor departure should be supplied'    
          enum:    
            - SCHEDULED    
            - SKIPPED    
            - NO_DATA    
          type: string    
          x-ngsi:    
            type: Property    
        stop_id:    
          description: Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty    
          type: string    
          x-ngsi:    
            type: Property    
        stop_sequence:    
          description: 'Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for'    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    stop_url:    
      description: "This field contains the URL of a web page about a particular stop and is different from the agency_url and the route_url fields. SameAs: 'stop_url' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"    
      type: string    
      x-ngsi:    
        type: Property    
    timestamp:    
      description: "Last reported time of observation from the vehicle. SameAs: 'timestamp' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    travelDistance:    
      description: The distance between the origin bus stop and the destination bus stop or the total distance travelled corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    travelTime:    
      description: 'The time taken to travel between the origin bus stop and the destination bus stop corresponding to this observation in HH:MM:SS format(HH:MM:SS is also accepted, if the hour begins with 0)'    
      format: time    
      type: string    
      x-ngsi:    
        type: Property    
    trip:    
      description: "Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
      properties:    
        direction_id:    
          description: "Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
          type: number    
          x-ngsi:    
            type: Property    
        route_id:    
          description: "Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
          type: string    
          x-ngsi:    
            type: Property    
        schedule_relationship:    
          description: "Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)"    
          type: string    
          x-ngsi:    
            type: Property    
        start_date:    
          description: "Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
          type: string    
          x-ngsi:    
            type: Property    
        start_time:    
          description: "Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
          type: string    
          x-ngsi:    
            type: Property    
        trip_id:    
          description: "Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    tripDetails:    
      description: A descriptor of realtime update on the schedule of a vehicle along a trip    
      properties:    
        arrival_time:    
          description: " Specifies the arrival time at a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'arrival_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
          format: time    
          type: string    
          x-ngsi:    
            type: Property    
        departure_time:    
          description: "Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
          format: time    
          type: string    
          x-ngsi:    
            type: Property    
        stop_headsign:    
          description: "This field contains the text that appears on a sign that identifies the trip’s destination to passengers. SameAs: 'stop_headsign' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
          type: string    
          x-ngsi:    
            type: Property    
        stop_id:    
          description: "Stop ID/Stop name of the bus stops corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
          type: string    
          x-ngsi:    
            type: Property    
        stop_sequence:    
          description: "Indicates the stop sequence of the vehicle corresponding to this observation, can be referenced from the GTFS static feed stop_times.txt. SameAs: 'stop_sequence' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    tripDirection:    
      description: 'Gives the direction in which the vehicle is travelling in ENUM[UP,DN]'    
      type: string    
      x-ngsi:    
        type: Property    
    tripInfo:    
      description: "Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
      properties:    
        route_id:    
          description: Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on    
          type: string    
          x-ngsi:    
            type: Property    
        schedule_relationship:    
          description: "Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from GTFS Realtime message-TripDescriptor ENUM[SCHEDULED, ADDED, UNSCHEDULED, CANCELED] (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
          type: string    
          x-ngsi:    
            type: Property    
        start_date:    
          description: "Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
          type: string    
          x-ngsi:    
            type: Property    
        start_time:    
          description: "Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
          format: time    
          type: string    
          x-ngsi:    
            type: Property    
        trip_direction:    
          description: "Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
          type: string    
          x-ngsi:    
            type: Property    
        trip_id:    
          description: 'Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId'    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    trip_delay:    
      description: "This can be positive and negative in seconds and shows how much the vehicle deviates from the planned one. SameAs: 'delay' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"    
      type: number    
      x-ngsi:    
        type: Property    
    trip_details:    
      description: A descriptor of realtime update on the schedule of a vehicle along a trip    
      properties:    
        bearing:    
          description: 'Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data'    
          type: number    
          x-ngsi:    
            type: Property    
        odometer:    
          description: 'Odometer value, in meters'    
          type: number    
          x-ngsi:    
            type: Property    
            units: meters    
        speed:    
          description: 'Momentary speed measured by the vehicle, in meters per second'    
          type: number    
          x-ngsi:    
            type: Property    
            units: meters per second    
      type: object    
      x-ngsi:    
        type: Property    
    trip_direction:    
      description: "Gives the direction in which the vehicle is travelling. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor but is represented in the form of an ENUM[UP,DN] in place of [0,1] as seen in 'direction_id' (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: string    
      x-ngsi:    
        type: Property    
    trip_id:    
      description: "Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: string    
      x-ngsi:    
        type: Property    
    trip_update:    
      description: "Describes the trip information like delay, departures, etc., for a trip made by the vehicle corresponding to this observation.SameAs:'trip_update' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"    
      properties:    
        stop_time_update:    
          description: Additional information on the vehicle that is serving this trip    
          properties:    
            arrival:    
              description: 'If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty'    
              properties:    
                uncertainty:    
                  description: "If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"    
                  type: number    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
            departure:    
              description: 'If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty'    
              properties:    
                uncertainty:    
                  description: "If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"    
                  type: number    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
            schedule_relationship:    
              description: 'Enum:''SCHEDULED, SKIPPED, NO_DATA''. SCHEDULED means that the vehicle is proceeding in accordance with its static schedule of stops, although not necessarily according to the times of the schedule. This is the default behavior. At least one of arrival and departure must be provided. SKIPPED means that The stop is skipped, i.e., the vehicle will not stop at this stop. The arrival and departure fields are optional. NO_DATA means that no data is given for this stop. It indicates that there is no realtime information available. When set NO_DATA is propagated through subsequent stops so this is the recommended way of specifying from which stop you do not have realtime information. When NO_DATA is set neither arrival nor departure should be supplied'    
              enum:    
                - SCHEDULED    
                - SKIPPED    
                - NO_DATA    
              type: string    
              x-ngsi:    
                type: Property    
            stop_id:    
              description: Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty    
              type: string    
              x-ngsi:    
                type: Property    
            stop_sequence:    
              description: 'Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for'    
              type: number    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        timestamp:    
          description: "Last reported time of observation from the vehicle. SameAs: 'timestamp' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
          format: date-time    
          type: string    
          x-ngsi:    
            type: Property    
        trip:    
          description: "Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
          properties:    
            direction_id:    
              description: "Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
              type: number    
              x-ngsi:    
                type: Property    
            route_id:    
              description: "Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
              type: string    
              x-ngsi:    
                type: Property    
            schedule_relationship:    
              description: "Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)"    
              type: string    
              x-ngsi:    
                type: Property    
            start_date:    
              description: "Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
              type: string    
              x-ngsi:    
                type: Property    
            start_time:    
              description: "Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
              type: string    
              x-ngsi:    
                type: Property    
            trip_id:    
              description: "Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        vehicleDesc:    
          description: "Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
          properties:    
            license_plate:    
              description: "Gives the License Plate number of the vehice.SameAs: 'license_plate' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
              type: string    
              x-ngsi:    
                type: Property    
            vehicle_id:    
              description: "Unique ID assigned to the vehicle corresponding to this observation,used in internal system identification.SameAs: 'id' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
              type: string    
              x-ngsi:    
                type: Property    
            vehicle_label:    
              description: "User visible label,i.e.,something that must be shown to the passenger to help identify the correct vehicle.SameAs: 'label' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be TransitManagement    
      enum:    
        - TransitManagement    
      type: string    
      x-ngsi:    
        type: Property    
    uncertainty:    
      description: "If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"    
      type: number    
      x-ngsi:    
        type: Property    
    vehicleDesc:    
      description: "Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
      properties:    
        license_plate:    
          description: "Gives the License Plate number of the vehice.SameAs: 'license_plate' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
          type: string    
          x-ngsi:    
            type: Property    
        vehicle_id:    
          description: "Unique ID assigned to the vehicle corresponding to this observation,used in internal system identification.SameAs: 'id' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
          type: string    
          x-ngsi:    
            type: Property    
        vehicle_label:    
          description: "User visible label,i.e.,something that must be shown to the passenger to help identify the correct vehicle.SameAs: 'label' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    vehicleInfo:    
      description: "Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
      properties:    
        license_plate:    
          description: "Gives the License Plate number of the vehice. SameAs: 'license_plate' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
          type: string    
          x-ngsi:    
            type: Property    
        vehicleID:    
          description: "Unique ID assigned to the vehicle corresponding to this observation, used in internal system identification. SameAs: 'id' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
          type: string    
          x-ngsi:    
            type: Property    
        vehicle_label:    
          description: "User visible label, i.e., something that must be shown to the passenger to help identify the correct vehicle. SameAs: 'label' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    vehiclePositionInfo:    
      description: "Describes the realtime position of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"    
      properties:    
        congestion_level:    
          description: 'Describes the congestion level that is affecting this vehicle. ENUM [UNKNOWN_CONGESTION_LEVEL, RUNNING_SMOOTHLY, STOP_AND_GO, CONGESTION, SEVERE_CONGESTION]'    
          type: string    
          x-ngsi:    
            type: Property    
        current_status:    
          description: "Describes the status of the vehicle w.r.t the stop corresponding to this observation ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. SameAs:'current_status' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
          type: string    
          x-ngsi:    
            type: Property    
        current_stop_sequence:    
          description: "Gives the stop sequence index of the current stop. This is determined by considering current_status, if current_status is missing IN_TRANSIT_TO is assumed. SameAs:'current_stop_sequence' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
          type: number    
          x-ngsi:    
            type: Property    
        occupancy_status:    
          description: 'The degree of passenger occupancy for the vehicle. ENUM [EMPTY, MANY_SEATS_AVAILABLE, FEW_SEATS_AVAILABLE, STANDING_ROOM_ONLY, CRUSHED_STANDING_ROOM_ONLY, FULL, NOT_ACCEPTING_PASSENGERS, NO_DATA_AVAILABLE, NOT_BOARDABLE]'    
          type: string    
          x-ngsi:    
            type: Property    
        stop_id:    
          description: Unique ID assigned to the stop corresponding to this observation    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    vehicleType:    
      description: 'Describes the type of vehicle corresponding to this observation, could be hopper, compactor, tipper, dumper in case of solid waste management vehicles, BRT mini bus, BRT bus, city bus in case of ITMS vehicles, Ambulance, Fire tender, Police van etc, in case of emergency vehicles and Moped/Scooter, Motor Cycle,  Autorickshaw, Private car/ Jeep car, Tempo, Bus, E-Moped/E-Scooter/E-Motor Cycle, Public motor in case of vehicle registration'    
      enum:    
        - agriculturalVehicle    
        - ambulance    
        - anyVehicle    
        - articulatedVehicle    
        - autorickshaw    
        - bicycle    
        - binTrolley    
        - BRT mini bus·    
        - BRT bus    
        - bus    
        - car    
        - caravan    
        - carOrLightVehicle    
        - carWithCaravan    
        - carWithTrailer    
        - cleaningTrolley    
        - compactor    
        - constructionOrMaintenanceVehicle    
        - dumper    
        - e-moped    
        - e-scooter    
        - e-motorcycle    
        - fireTender    
        - fourWheelDrive    
        - highSidedVehicle    
        - hopper    
        - lorry    
        - minibus    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - policeVan    
        - publicMotor    
        - sweepingMachine    
        - tanker    
        - tempo    
        - threeWheeledVehicle    
        - tipper    
        - trailer    
        - tram    
        - trolley    
        - twoWheeledVehicle    
        - van    
        - vehicleWithoutCatalyticConverter    
        - vehicleWithCaravan    
        - vehicleWithTrailer    
        - withEvenNumberedRegistrationPlates    
        - withOddNumberedRegistrationPlates    
        - other    
      type: string    
      x-ngsi:    
        type: Property    
    vehicle_id:    
      description: "Unique ID assigned to the vehicle corresponding to this observation, used in internal system identification. SameAs: 'id' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
      type: string    
      x-ngsi:    
        type: Property    
    vehicle_label:    
      description: "User visible label, i.e., something that must be shown to the passenger to help identify the correct vehicle. SameAs: 'label' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
      type: string    
      x-ngsi:    
        type: Property    
    vehicle_position:    
      description: "Describes the realtime position of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"    
      properties:    
        current_status:    
          description: "Describes the status of the vehicle w.r.t the stop corresponding to this observation ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. SameAs:'current_status' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
          type: string    
          x-ngsi:    
            type: Property    
        current_stop_sequence:    
          description: "Gives the stop sequence index of the current stop. This is determined by considering current_status, if current_status is missing IN_TRANSIT_TO is assumed. SameAs:'current_stop_sequence' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
          type: number    
          x-ngsi:    
            type: Property    
        position:    
          description: "Describes the current position of the vehicle corresponding to this observation. SameAs: 'position' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
          properties:    
            bearing:    
              description: 'Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data'    
              type: number    
              x-ngsi:    
                type: Property    
            latitude:    
              description: 'Degrees North, in the WGS-84 coordinate system'    
              type: number    
              x-ngsi:    
                type: Property    
            longitude:    
              description: 'Degrees East, in the WGS-84 coordinate system'    
              type: number    
              x-ngsi:    
                type: Property    
            odometer:    
              description: 'Odometer value, in meters'    
              type: number    
              x-ngsi:    
                type: Property    
                units: meters    
            speed:    
              description: 'Momentary speed measured by the vehicle, in meters per second'    
              type: number    
              x-ngsi:    
                type: Property    
                units: meters/second    
          type: object    
          x-ngsi:    
            type: Property    
        stop_id:    
          description: "Stop ID/Stop name of the bus stops corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
          type: string    
          x-ngsi:    
            type: Property    
        timestamp:    
          description: "Last reported time of observation from the vehicle. SameAs:  'timestamp' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
          format: date-time    
          type: string    
          x-ngsi:    
            type: Property    
        trip:    
          description: "Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
          properties:    
            direction_id:    
              description: "Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
              type: number    
              x-ngsi:    
                type: Property    
            route_id:    
              description: "Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
              type: string    
              x-ngsi:    
                type: Property    
            schedule_relationship:    
              description: "Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)"    
              type: string    
              x-ngsi:    
                type: Property    
            start_date:    
              description: "Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
              type: string    
              x-ngsi:    
                type: Property    
            start_time:    
              description: "Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
              type: string    
              x-ngsi:    
                type: Property    
            trip_id:    
              description: "Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        vehicleDesc:    
          description: "Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
          properties:    
            license_plate:    
              description: "Gives the License Plate number of the vehice.SameAs: 'license_plate' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
              type: string    
              x-ngsi:    
                type: Property    
            vehicle_id:    
              description: "Unique ID assigned to the vehicle corresponding to this observation,used in internal system identification.SameAs: 'id' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
              type: string    
              x-ngsi:    
                type: Property    
            vehicle_label:    
              description: "User visible label,i.e.,something that must be shown to the passenger to help identify the correct vehicle.SameAs: 'label' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/TransitManagement/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/TransitManagement/schema.json    
  x-model-tags: IUDX    
  x-version: 0.0.4    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### TransitManagement NGSI-v2 키-값 예제  
다음은 JSON-LD 형식의 TransitManagement를 키-값으로 사용하는 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "vehicle_label": "A03",  
  "current_stop_sequence": 1001,  
  "vehicleType": "hopper",  
  "route_color": "00FFFF",  
  "agency_fare_url": "http://charteredbike.in/surat/?page_id=1021",  
  "observationDateTime": "2021-10-28T08:13:22+05:30",  
  "stop_sequence": 24,  
  "route_type": "1",  
  "agency_lang": "en",  
  "start_date": "2022-03-01",  
  "start_time": "11:15:35",  
  "routeStopSequence": [  
    "10",  
    "1001",  
    "1002",  
    "1003",  
    "1004",  
    "1005"  
  ],  
  "direction_id": 0,  
  "actual_trip_start_time": "2021-10-28T07:46:51+05:30",  
  "agency_url": "http://charteredbike.in/surat/",  
  "type": "TransitManagement",  
  "travelTime": "22:11:14",  
  "agency_name": "Chartered Bike Surat",  
  "last_tracked_time": "2021-10-28T08:13:22",  
  "actual_trip_end_time": "2021-10-28T08:24:22+05:30",  
  "trip_id": "23952340",  
  "last_stop_id": "4032",  
  "stop_code": "F12",  
  "current_status": "INCOMING_AT",  
  "agency_timezone": "Asia/Kolkata",  
  "route_id": "17AD",  
  "travelDistance": 9.00174,  
  "tripDirection": "DN",  
  "trip_delay": 11968,  
  "route_long_name": "Baiyappanahalli to Mysuru Road",  
  "bearing": 90,  
  "stop_name": "DEVASHISH NAGAR MORA BHAGAL",  
  "speed": 28,  
  "stop_id": "1016",  
  "arrival_time": "22:00:28",  
  "route_desc": "Phase1-Phase2",  
  "last_stop_arrival_time": "13:30:12",  
  "route_text_color": "FFD700",  
  "id": "https://smart-data-models.github.io/IUDX/TransitManagement/schema.json",  
  "schedule_relationship": "SCHEDULED",  
  "agency_id": "agency001",  
  "license_plate": "GJ05BX1583",  
  "trip_direction": "DN",  
  "route_short_name": "Purple Line",  
  "departure_time": "22:00:33",  
  "standingCapacity": 20,  
  "vehicleID": "52TC12",  
  "depotID": "1",  
  "seatingCapacity": 70,  
  "depotName": "BHESTAN DEPOT",  
  "acAvailable": "yes",  
  "timestamp": "2021-10-28T08:13:22+05:30",  
  "vehicle_id": "52TC12",  
  "standing_capacity": 20,  
  "uncertainity": 0,  
  "ac_available": "yes",  
  "seating_capacity": 70,  
  "depot_id": "1",  
  "depot_name": "BHESTAN DEPOT"  
}  
```  
</details>  
#### TransitManagement NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 TransitManagement의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "https://smart-data-models.github.io/IUDX/TransitManagement/schema.json",  
  "type": "TransitManagement",  
  "vehicleType": {  
    "type": "Text",  
    "value": "hopper"  
  },  
  "trip_delay": {  
    "type": "Number",  
    "value": 11968  
  },  
  "agency_lang": {  
    "type": "Text",  
    "value": "en"  
  },  
  "depot_name": {  
    "type": "Text",  
    "value": "BHESTAN DEPOT"  
  },  
  "travelTime": {  
    "type": "Time",  
    "value": "22:11:14"  
  },  
  "direction_id": {  
    "type": "Number",  
    "value": 0  
  },  
  "schedule_relationship": {  
    "type": "Text",  
    "value": "SCHEDULED"  
  },  
  "vehicle_id": {  
    "type": "Text",  
    "value": "52TC12"  
  },  
  "agency_fare_url": {  
    "type": "URL",  
    "value": "http://charteredbike.in/surat/?page_id=1021"  
  },  
  "actual_trip_end_time": {  
    "type": "Date-Time",  
    "value": "2021-10-28T08:24:22+05:30"  
  },  
  "last_tracked_time": {  
    "type": "Time",  
    "value": "08:13:22"  
  },  
  "standing_capacity": {  
    "type": "Number",  
    "value": 20  
  },  
  "last_stop_arrival_time": {  
    "type": "Text",  
    "value": "13:30:12"  
  },  
  "agency_id": {  
    "type": "Text",  
    "value": "agency001"  
  },  
  "current_status": {  
    "type": "Text",  
    "value": "INCOMING_AT"  
  },  
  "route_type": {  
    "type": "Text",  
    "value": "1"  
  },  
  "speed": {  
    "type": "Number",  
    "value": 28  
  },  
  "route_id": {  
    "type": "Text",  
    "value": "17AD"  
  },  
  "seating_capacity": {  
    "type": "Number",  
    "value": 70  
  },  
  "vehicle_label": {  
    "type": "Text",  
    "value": "A03"  
  },  
  "timestamp": {  
    "format": "Date-Time",  
    "value": "2021-10-28T08:13:22+05:30"  
  },  
  "arrival_time": {  
    "type": "Time",  
    "value": "22:00:28"  
  },  
  "route_long_name": {  
    "type": "Text",  
    "value": "Baiyappanahalli to Mysuru Road"  
  },  
  "agency_timezone": {  
    "type": "Text",  
    "value": "Asia/Kolkata"  
  },  
  "stop_code": {  
    "type": "Text",  
    "value": "F12"  
  },  
  "agency_name": {  
    "type": "Text",  
    "value": "Chartered Bike Surat"  
  },  
  "route_desc": {  
    "type": "Text",  
    "value": "Phase1-Phase2"  
  },  
  "license_plate": {  
    "type": "Text",  
    "value": "GJ05BX1583"  
  },  
  "stop_id": {  
    "type": "Text",  
    "value": "1016"  
  },  
  "uncertainity": {  
    "type": "Boolean",  
    "value": "false"  
  },  
  "route_color": {  
    "type": "Text",  
    "value": "00FFFF"  
  },  
  "travelDistance": {  
    "type": "Number",  
    "value": 9.00174  
  },  
  "actual_trip_start_time": {  
    "type": "Date-Time",  
    "value": "2021-10-28T07:46:51+05:30"  
  },  
  "bearing": {  
    "type": "Number",  
    "value": 90  
  },  
  "stop_sequence": {  
    "type": "Number",  
    "value": 24  
  },  
  "start_date": {  
    "type": "Date",  
    "value": "2022-03-01"  
  },  
  "current_stop_sequence": {  
    "type": "Number",  
    "value": 1001  
  },  
  "start_time": {  
    "type": "Time",  
    "value": "11:15:35"  
  },  
  "trip_id": {  
    "type": "Text",  
    "value": "23952340"  
  },  
  "route_text_color": {  
    "type": "Text",  
    "value": "FFD700"  
  },  
  "ac_available": {  
    "type": "Text",  
    "value": "yes"  
  },  
  "tripDirection": {  
    "type": "Text",  
    "value": "DN"  
  },  
  "agency_url": {  
    "type": "URL",  
    "value": "http://charteredbike.in/surat/"  
  },  
  "routeStopSequence": {  
    "type": "array",  
    "value": [  
      "10",  
      "1001",  
      "1002",  
      "1003",  
      "1004",  
      "1005"  
    ]  
  },  
  "trip_direction": {  
    "type": "Text",  
    "value": "DN"  
  },  
  "departure_time": {  
    "type": "Time",  
    "value": "22:00:33"  
  },  
  "last_stop_id": {  
    "type": "Text",  
    "value": "4032"  
  },  
  "route_short_name": {  
    "type": "Text",  
    "value": "Purple Line"  
  },  
  "stop_name": {  
    "type": "Text",  
    "value": "DEVASHISH NAGAR MORA BHAGAL"  
  },  
  "depot_id": {  
    "type": "Text",  
    "value": "1"  
  },  
  "observationDateTime": {  
    "type": "Date-Time",  
    "value": "2021-10-28T08:13:22+05:30"  
  }  
}  
```  
</details>  
#### TransitManagement NGSI-LD 키-값 예제  
다음은 JSON-LD 형식의 TransitManagement를 키-값으로 사용하는 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "vehicle_label": "A03",  
  "current_stop_sequence": 1001,  
  "vehicleType": "hopper",  
  "route_color": "00FFFF",  
  "agency_fare_url": "http://charteredbike.in/surat/?page_id=1021",  
  "observationDateTime": "2021-10-28T08:13:22+05:30",  
  "stop_sequence": 24,  
  "route_type": "1",  
  "agency_lang": "en",  
  "start_date": "2022-03-01",  
  "start_time": "11:15:35",  
  "routeStopSequence": [  
    "10",  
    "1001",  
    "1002",  
    "1003",  
    "1004",  
    "1005"  
  ],  
  "direction_id": 0,  
  "actual_trip_start_time": "2021-10-28T07:46:51+05:30",  
  "agency_url": "http://charteredbike.in/surat/",  
  "type": "TransitManagement",  
  "travelTime": "22:11:14",  
  "agency_name": "Chartered Bike Surat",  
  "last_tracked_time": "2021-10-28T08:13:22",  
  "actual_trip_end_time": "2021-10-28T08:24:22+05:30",  
  "trip_id": "23952340",  
  "last_stop_id": "4032",  
  "stop_code": "F12",  
  "current_status": "INCOMING_AT",  
  "agency_timezone": "Asia/Kolkata",  
  "route_id": "17AD",  
  "travelDistance": 9.00174,  
  "tripDirection": "DN",  
  "trip_delay": 11968,  
  "route_long_name": "Baiyappanahalli to Mysuru Road",  
  "bearing": 90,  
  "stop_name": "DEVASHISH NAGAR MORA BHAGAL",  
  "speed": 28,  
  "stop_id": "1016",  
  "arrival_time": "22:00:28",  
  "route_desc": "Phase1-Phase2",  
  "last_stop_arrival_time": "13:30:12",  
  "route_text_color": "FFD700",  
  "id": "https://smart-data-models.github.io/IUDX/TransitManagement/schema.json",  
  "schedule_relationship": "SCHEDULED",  
  "agency_id": "agency001",  
  "license_plate": "GJ05BX1583",  
  "trip_direction": "DN",  
  "route_short_name": "Purple Line",  
  "departure_time": "22:00:33",  
  "standingCapacity": 20,  
  "vehicleID": "52TC12",  
  "depotID": "1",  
  "seatingCapacity": 70,  
  "depotName": "BHESTAN DEPOT",  
  "acAvailable": "yes",  
  "timestamp": "2021-10-28T08:13:22+05:30",  
  "vehicle_id": "52TC12",  
  "standing_capacity": 20,  
  "uncertainity": 0,  
  "ac_available": "yes",  
  "seating_capacity": 70,  
  "depot_id": "1",  
  "depot_name": "BHESTAN DEPOT",  
  "@context": [  
    "iudx:TransitManagement",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### TransitManagement NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 TransitManagement의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "https://smart-data-models.github.io/IUDX/TransitManagement/schema.json",  
  "type": "TransitManagement",  
  "vehicleType": {  
    "type": "Property",  
    "value": "hopper"  
  },  
  "trip_delay": {  
    "type": "Property",  
    "value": 11968  
  },  
  "agency_lang": {  
    "type": "Property",  
    "value": "en"  
  },  
  "depot_name": {  
    "type": "Property",  
    "value": "BHESTAN DEPOT"  
  },  
  "travelTime": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "22:11:14"  
    }  
  },  
  "direction_id": {  
    "type": "Property",  
    "value": "false"  
  },  
  "schedule_relationship": {  
    "type": "Property",  
    "value": "SCHEDULED"  
  },  
  "vehicle_id": {  
    "type": "Property",  
    "value": "52TC12"  
  },  
  "agency_fare_url": {  
    "type": "Property",  
    "value": "http://charteredbike.in/surat/?page_id=1021"  
  },  
  "actual_trip_end_time": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2021-10-28T08:24:22+05:30"  
    }  
  },  
  "last_tracked_time": {  
    "type": "Property",  
    "value": {  
      "@type": "time",  
      "@value": "08:13:22"  
    }  
  },  
  "standing_capacity": {  
    "type": "Property",  
    "value": 20  
  },  
  "last_stop_arrival_time": {  
    "type": "Property",  
    "value": {  
      "@type": "time",  
      "@value": "13:30:12"  
    }  
  },  
  "agency_id": {  
    "type": "Property",  
    "value": "agency001"  
  },  
  "current_status": {  
    "type": "Property",  
    "value": "INCOMING_AT"  
  },  
  "route_type": {  
    "type": "Property",  
    "value": "1"  
  },  
  "speed": {  
    "type": "Property",  
    "value": 28  
  },  
  "route_id": {  
    "type": "Property",  
    "value": "17AD"  
  },  
  "seating_capacity": {  
    "type": "Property",  
    "value": 70  
  },  
  "vehicle_label": {  
    "type": "Property",  
    "value": "A03"  
  },  
  "timestamp": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2021-10-28T08:13:22+05:30"  
    }  
  },  
  "arrival_time": {  
    "type": "Property",  
    "value": {  
      "@type": "time",  
      "@value": "22:00:28"  
    }  
  },  
  "route_long_name": {  
    "type": "Property",  
    "value": "Baiyappanahalli to Mysuru Road"  
  },  
  "agency_timezone": {  
    "type": "Property",  
    "value": "Asia/Kolkata"  
  },  
  "stop_code": {  
    "type": "Property",  
    "value": "F12"  
  },  
  "agency_name": {  
    "type": "Property",  
    "value": "Chartered Bike Surat"  
  },  
  "route_desc": {  
    "type": "Property",  
    "value": "Phase1-Phase2"  
  },  
  "license_plate": {  
    "type": "Property",  
    "value": "GJ05BX1583"  
  },  
  "stop_id": {  
    "type": "Property",  
    "value": "1016"  
  },  
  "uncertainity": {  
    "type": "Property",  
    "value": "false"  
  },  
  "route_color": {  
    "type": "Property",  
    "value": "00FFFF"  
  },  
  "travelDistance": {  
    "type": "Property",  
    "value": 9.00174  
  },  
  "actual_trip_start_time": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2021-10-28T07:46:51+05:30"  
    }  
  },  
  "bearing": {  
    "type": "Property",  
    "value": 90  
  },  
  "stop_sequence": {  
    "type": "Property",  
    "value": 24  
  },  
  "start_date": {  
    "type": "Property",  
    "value": {  
      "@type": "date",  
      "@value": "2022-03-01"  
    }  
  },  
  "current_stop_sequence": {  
    "type": "Property",  
    "value": 1001  
  },  
  "start_time": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "11:15:35"  
    }  
  },  
  "trip_id": {  
    "type": "Property",  
    "value": "23952340"  
  },  
  "route_text_color": {  
    "type": "Property",  
    "value": "FFD700"  
  },  
  "ac_available": {  
    "type": "Property",  
    "value": "yes"  
  },  
  "tripDirection": {  
    "type": "Property",  
    "value": "DN"  
  },  
  "agency_url": {  
    "type": "Property",  
    "value": "http://charteredbike.in/surat/"  
  },  
  "routeStopSequence": {  
    "type": "Property",  
    "value": [  
      "10",  
      "1001",  
      "1002",  
      "1003",  
      "1004",  
      "1005"  
    ]  
  },  
  "trip_direction": {  
    "type": "Property",  
    "value": "DN"  
  },  
  "departure_time": {  
    "type": "Property",  
    "value": {  
      "@type": "time",  
      "@value": "22:00:33"  
    }  
  },  
  "last_stop_id": {  
    "type": "Property",  
    "value": "4032"  
  },  
  "route_short_name": {  
    "type": "Property",  
    "value": "Purple Line"  
  },  
  "stop_name": {  
    "type": "Property",  
    "value": "DEVASHISH NAGAR MORA BHAGAL"  
  },  
  "depot_id": {  
    "type": "Property",  
    "value": "1"  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2021-10-28T08:13:22+05:30"  
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
