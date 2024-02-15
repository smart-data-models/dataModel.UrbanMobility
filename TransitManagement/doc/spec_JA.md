<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティトランジットマネジメント  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/TransitManagement/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**公共交通システムのデータモデル  
バージョン: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `acAvailable[string]`: この観察に対応する車両のエアコンオプションの有無を記述する。  - `ac_available[string]`: この観察に対応する車両のエアコンオプションの有無を記述する。  - `actual_trip_end_time[date-time]`: このフィールドは、このオブザベーションに対応するサービスまたはトリップが終了する予定時刻を指定する。  - `actual_trip_start_time[date-time]`: このフィールドは、サービスが実際に開始された時刻を指定する。  これは SameAs: GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate) の stop_time_update (StopTimeUpdate) メッセージの 'arrival' フィールドの絶対 'time'(StopTimeEvent) である。  - `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `agencyInfo[object]`: この観測に対応する代理店情報  	- `agency_email[string]`: 代理店のカスタマーサービス部門が積極的に監視している電子メールアドレス。同じ：GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) の 'agency_email' フィールド。    
	- `agency_fare_url[string]`: 運賃の詳細が記載され、その航空会社のチケットをオンラインで購入できるウェブページのURL。同じ：GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) の 'agency_fare_url' フィールド。    
	- `agency_id[string]`: 交通機関を一意に識別する ID。1つの transit フィードが複数の機関のデータを表すこともある。agency_id はデータセットで一意である。このフィールドは、単一のエージェンシーのデータのみを含む transit フィードではオプションとなる。同じ：GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) の 'agency_id' フィールド。    
	- `agency_lang[string]`: この交通機関が使用する主要言語の2文字のISO 639-1コードを含む。言語コードは大文字と小文字を区別しない（enとenの両方が使用可能）。同じ：GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) の 'agency_lang' フィールド。    
	- `agency_name[string]`: agency_name フィールドには、交通機関の正式名称が入る。同じ：GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) の 'agency_name' フィールド。    
	- `agency_phone[string]`: 指定されたエージェンシーの音声電話番号：GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) の 'agency_phone' フィールド。    
	- `agency_timezone[string]`: Timezone（タイムゾーン）フィールドには、交通機関が所在するタイムゾーンが含まれる。同じ：GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) の 'agency_timezone' フィールド。    
	- `agency_url[string]`: agency_url フィールドには、交通機関の URL が含まれる。同じ：GTFS 静的フィールド定義 - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) の 'agency_url' フィールド。    
- `agency_fare_url[string]`: 運賃の詳細が記載され、その航空会社のチケットをオンラインで購入できるウェブページのURL。同じ：GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) の 'agency_fare_url' フィールド。  - `agency_id[string]`: 交通機関を一意に識別する ID。1つの transit フィードが複数の機関のデータを表すこともある。agency_id はデータセットで一意である。このフィールドは、単一のエージェンシーのデータのみを含む transit フィードではオプションとなる。同じ：GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) の 'agency_id' フィールド。  - `agency_lang[string]`: この交通機関が使用する主要言語の2文字のISO 639-1コードを含む。言語コードは大文字と小文字を区別しない（enとenの両方が使用可能）。同じ：GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) の 'agency_lang' フィールド。  - `agency_name[string]`: agency_name フィールドには、交通機関の正式名称が入る。同じ：GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) の 'agency_name' フィールド。  - `agency_timezone[string]`: Timezone（タイムゾーン）フィールドには、交通機関が所在するタイムゾーンが含まれる。同じ：GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) の 'agency_timezone' フィールド。  - `agency_url[string]`: agency_url フィールドには、交通機関の URL が含まれる。同じ：GTFS 静的フィールド定義 - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) の 'agency_url' フィールド。  - `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrival[object]`: schedule_relationshipが空またはSCHEDULEDの場合、StopTimeUpdate内で到着または出発のどちらかを提供する必要があります。同じ：GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)の'arrival'フィールド。  	- `uncertainty[number]`: 不確実性が省略された場合、不明と解釈される。完全に確実な予測を指定するには、その不確実性を0.SameAsに設定する：GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)の'uncertainty'フィールド。    
- `arrivalUncertainty[number]`: schedule_relationshipが空またはSCHEDULEDの場合、StopTimeUpdate内で到着または出発のどちらかを提供する必要があります。同じ：GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)の'arrival'フィールド。  - `arrival_time[time]`: ルート上の特定の旅行の特定の停留所への到着時刻を指定します。時間は、HH:MM:SS 形式で 8 桁である必要があります（時間が 0 で始まる場合は、HH:MM:SS も使用できます）。注：複数の日付にまたがるトリップは、24:00:00を超える停止時刻になります。たとえば、トリップが22時30分00秒に開始し、翌日の午前2時15分00秒に終了する場合、停止時刻は22時30分00秒と26時15分00秒になります。これらの停車時間を22:30:00と02:15:00と入力しても、望ましい結果は得られません。同じく：GTFS Static Field definitions-stop_times.txtの'arrival_time'フィールド (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `bearing[number]`: 真北から時計回りで測定した車両の GPS 角度を示す。GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)の'bearing'フィールドと同じ。  - `current_status[string]`: ENUM:[INCOMING_AT,STOPPED_AT,IN_TRANSIT_TO]。SameAs: GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'current_status'フィールド。  - `current_stop_sequence[number]`: 現在の停止位置の停止シーケンスインデックスを与える。current_status がない場合は IN_TRANSIT_TO とみなされる。GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'current_stop_sequence'フィールドと同じ。  - `dataDescriptor[uri]`: データ記述子エンティティを指すURI  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `departure[object]`: schedule_relationshipが空またはSCHEDULEDの場合、StopTimeUpdate内で到着または出発のどちらかを提供する必要があります。同じ：GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate) の 'departure' フィールド。  	- `uncertainty[number]`: 不確実性が省略された場合、不明と解釈される。完全に確実な予測を指定するには、その不確実性を0.SameAsに設定する：GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)の'uncertainty'フィールド。    
- `departureUncertainty[number]`: schedule_relationshipが空またはSCHEDULEDの場合、StopTimeUpdate内で到着または出発のどちらかを提供する必要があります。同じ：GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate) の 'departure' フィールド。  - `departure_time[time]`: ルート上の特定の旅行について、特定の停留所からの出発時刻を指定します。時間は、HH:MM:SS 形式で 8 桁でなければなりません（時間が 0 で始まる場合は、HH:MM:SS も使用できます）。  
注：複数の日付にまたがるトリップは、24:00:00より大きい停止時刻になります。たとえば、トリップが22時30分00秒に開始し、翌日の午前2時15分00秒に終了する場合、停止時刻は22時30分00秒と26時15分00秒になります。これらの停車時間を22:30:00と02:15:00と入力しても、望ましい結果は得られません。同じく：GTFS Static Field definitions-stop_times.txtの「departure_time」フィールド (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `depotID[string]`: このオブザベーションに対応するバスデポのユニークIDを記述する。  - `depotName[string]`: このオブザベーションに対応するバスデポのデポ名を記述する。  - `depot_id[string]`: このオブザベーションに対応するバスデポのユニークIDを記述する。  - `depot_name[string]`: このオブザベーションに対応するバスデポのデポ名を記述する。  - `description[string]`: この商品の説明  - `deviceInfo[object]`: オブザベーションに関連するデバイスに関する情報  . Model: [https://schema.org/Text](https://schema.org/Text)	- `deviceBatteryStatus[string]`: 報告デバイスのバッテリ充電状態を表示（接続、切断）  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceID[string]`: この観測に対応する物理センサー/計測ステーションのデバイスID  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceModel[object]`: 対象となるデバイス、センサー、システムの情報を記述する。  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceName[string]`: この観測に対応するセンサーデバイス/ステーションのデバイス名またはステーション名  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceSimNumber[string]`: 廃棄物管理車両に搭載されているデバイスのSIM番号を示す。  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `measurand[string]`: 装置によって感知／観察／測定される特性／性質  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `rfID[string]`: RFIDリーダーのID  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `direction_id[number]`: この観測に対応する車両の進行方向を示す。GTFS の静的フィード trips.txt から参照できる。同じ：GTFS Realtime message-TripDescriptorの'direction_id'フィールド (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `entity_id[string]`: このオブザベーションに対応するエンティティのフィードユニークID。SameAs:'entity_id' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  - `id[*]`: エンティティの一意識別子  - `last_stop_arrival_time[time]`: ルート上の特定の旅行の前の停留所への到着時刻を指定します。時間は、HH:MM:SS 形式で 8 桁でなければなりません（時間が 0 で始まる場合は、H:MM:SS も使用できます）。注：複数の日付にまたがるトリップの停止時間は、24:00:00より大きくなります。たとえば、トリップが22時30分00秒に開始し、翌日の午前2時15分00秒に終了する場合、停止時刻は22時30分00秒と26時15分00秒になります。これらの停止時間を22:30:00と02:15:00と入力しても、望ましい結果は得られない。これはSameAs: GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)のstop_time_update (StopTimeUpdate)メッセージの'arrival'フィールドの絶対'time'(StopTimeEvent)である。  - `last_stop_id[string]`: 停留所ID/停留所名：この観測のバスに対応する前の停留所のID/停留所名。同じ：GTFS Realtime message-VehiclePosition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'stop_id'フィールド。  - `last_tracked_time[date-time]`: 車両が最後に追跡された時刻を示します。  - `license_plate[string]`: 車両のナンバーを表示します。同じ：GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor) の 'license_plate' フィールド。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `observationDateTime[date-time]`: 最終観測報告時刻  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `position[object]`: この観測に対応する車両の現在位置を記述する。SameAs: GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)のpositionフィールド。  . Model: [https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition](https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)	- `bearing[number]`: 方位は度単位で、真北から時計回り、つまり0は北、90は東。これはコンパスの方位、または次の停車駅や中間地点に向かう方位である。これは、クライアントが以前のデータから計算できる、以前の位置のシーケンスから推測されるべきではありません。    
	- `latitude[number]`: 北緯度、WGS-84座標系において    
	- `longitude[number]`: 度東、WGS-84座標系において    
	- `odometer[number]`: オドメーター値（単位：メートル    
	- `speed[number]`: 車両が計測した瞬間速度（単位：メートル毎秒    
- `positionInfo[object]`: この観測に対応する車両の現在位置を記述する。GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'position'フィールドと同じ。  	- `bearing[number]`: 方位は度単位で、真北から時計回り、つまり0は北、90は東。これはコンパスの方位、または次の停車駅や中間地点に向かう方位である。これは、クライアントが以前のデータから計算できる、以前の位置のシーケンスから推測されるべきではありません。    
	- `odometer[number]`: オドメーター値    
	- `speed[number]`: 車両が計測した瞬間速度    
- `routeInfo[object]`: schedule_relationshipが'CANCELED'の場合は考慮されない。同じ：GTFS Realtime message-TripUpdateの'stop_time_update'フィールド (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `route_color[string]`: 割り当てられている場合、このフィールドはルートに対応する色を定義する。色は、例えば 00FFFF のように、6文字の16進数で指定しなければならない。色が指定されない場合、デフォルトのルート色は白(FFFFFF)である。同じ：GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt) の 'route_color' フィールド。    
	- `route_desc[string]`: ルートの説明。これは、目的地とタイミング情報を含むルート全体の詳細をテキスト記述形式で含むことができます。同じ：GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt) の 'route_desc' フィールド。    
	- `route_id[string]`: この観測のバスに対応するバス/車両が現在走行しているルートに割り当てられたルートID。    
	- `route_long_name[string]`: ルートのフルネーム。この名前は routeShortName よりも説明的で、多くの場合、ルートの目的地または停留所を含みます。この名前には、ルートの目的地名と停車駅名が含まれます。同じです：GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt) の 'route_long_name' フィールド。    
	- `route_short_name[string]`: 路線の略称。これは多くの場合、402Dのような輸送車両のボード名、またはライダーがルートを識別するために使用するグリーンとなる。同じ：GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt) の 'route_short_name' フィールド。    
	- `route_text_color[string]`: このフィールドは、route_color を背景に描画されるテキストに使用する読みやすい色を指定するために使用できる。色は、例えば FFD700 のように、6文字の16進数で指定する必要があります。色を指定しない場合、デフォルトのテキスト色は黒 (000000) です。同じです：GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt) の 'route_text_color' フィールド。    
	- `route_type[number]`: 交通機関の種類を示す番号 - 1 - 地下鉄、メトロ。大都市圏の地下鉄道システム。2 - 鉄道。都市間または長距離の移動に使われる。3 - バス。短距離および長距離バス路線。同じ：GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt) の 'route_type' フィールド。    
	- `route_url[string]`: 特定のルートに関するウェブページの URL を含み、agency_url とは異なる。同じ：GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt) の 'route_url' フィールド。    
- `routeStopSequence[array]`: この観測に対応するルート、ライン、またはトリップの正しい順序で、停留所ID/停留所コード、または駅ID/駅コードを与えます。  - `route_color[string]`: 割り当てられている場合、このフィールドはルートに対応する色を定義する。色は、例えば 00FFFF のように、6文字の16進数で指定しなければならない。色が指定されない場合、デフォルトのルート色は白(FFFFFF)である。同じ：GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt) の 'route_color' フィールド。  - `route_desc[string]`: ルートの説明。これは、目的地とタイミング情報を含むルート全体の詳細をテキスト記述形式で含むことができます。同じ：GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt) の 'route_desc' フィールド。  - `route_id[string]`: この観測のバスに対応するバス/車両が現在走行しているルートに割り当てられたルートID。同じ：GTFS Realtime message-TripDescriptorの'route_id'フィールド (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `route_long_name[string]`: ルートのフルネーム。この名前は routeShortName よりも説明的で、多くの場合、ルートの目的地または停留所を含みます。この名前には、ルートの目的地名と停車駅名が含まれます。同じです：GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt) の 'route_long_name' フィールド。  - `route_short_name[string]`: 路線の短い名前。これは多くの場合、「402D」や「Green」のような乗り物のボードネームで、ライダーがルートを識別するのに使う。同じ：GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt) の 'route_short_name' フィールド。  - `route_text_color[string]`: このフィールドは、route_color を背景に描画されるテキストに使用する読みやすい色を指定するために使用できる。色は、例えば FFD700 のように、6文字の16進数で指定する必要があります。色を指定しない場合、デフォルトのテキスト色は黒 (000000) です。同じです：GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt) の 'route_text_color' フィールド。  - `route_type[string]`: 交通機関の種類を示す番号。大都市圏内の地下鉄道システム。都市間または長距離の移動に使用される。近距離および長距離バス路線。同じ：GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt) の 'route_type' フィールド。  - `route_url[string]`: 特定のルートに関するウェブページの URL を含み、agency_url とは異なる。同じ：GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt) の 'route_url' フィールド。  - `schedule_relationship[string]`: ルート/トリップがスケジュールされているかどうかを説明します。同じ：enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2) の 'schedule_relationship' フィールドです。  - `seating_capacity[number]`: この観測に対応する車両の乗客定員を記述する。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `shapeInfo[object]`: この観測に対応する車両の走行経路に関する情報  	- `shape_dist_traveled[number]`: 最初のシェイプポイントからこのレコードで指定されたポイントまで、シェイプに沿って移動した実際の距離。トリッププランナーが地図上にシェイプの正しい部分を表示するために使用する。値は、shape_pt_sequence とともに増加しなければならない。距離の単位はstop_times.txtで使用されているものと一致しなければならない。例例：バスが上記の A_shp で定義された 3 点に沿って走行する場合、shape_dist_traveled の追加値 (ここではキロメートルで示す) は次のようになる：shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled A_shp,37.61956,-122.48161,0,0 A_shp,37.64430,-122.41070,6,6.8310 A_shp,37.65863,-122.30839,11,15.8765    
	- `shape_id[string]`: 形状を特定する    
	- `shape_pt_sequence[number]`: 形状を形成するために形状点が接続される順序。値は移動に伴って増加しなければならないが、連続している必要はない。例例：形状 'A_shp' の定義に 3 つの点がある場合、shapes.txt ファイルには、形状を定義するために次のレコードが 含まれる： shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence A_shp,37.61956,-122.48161,0 A_shp,37.64430,-122.41070,6 A_shp,37.65863,-122.30839,11    
- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `speed[number]`: 車両の速度を示す。GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)の'speed'フィールドと同じ。  - `standingCapacity[number]`: この観測に対応する車両の乗客定員を記述する。  - `standing_capacity[number]`: この観測に対応する車両の乗客定員を記述する。  - `start_date[string]`: この観測車両に対応する旅行の最初の予定日を記述する。このフィールドのフォーマット例 - YYYYMMDD。同じ：GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor) の 'start_date' フィールド。  - `start_time[time]`: この観測車両に対応するトリップの最初の予定開始時刻を記述する。このフィールドのフォーマット例 - 11:15:35または25:15:35。同じ：GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor) の 'start_time' フィールド。  - `stopInfo[object]`: この観測に対応する車両の走行経路に関する情報  	- `stop_code[string]`: このフィールドには、乗客のために停留所を一意に識別する短いテキストまたは番号が含まれる。公共の場合はstop_idと同じになる。同じ：GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt) の 'stop_code' フィールド。    
	- `stop_desc[string]`: このフィールドには停車駅の説明が含まれる。同じ：GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt) の 'stop_desc' フィールド。    
	- `stop_id[string]`: この観測に対応する停留所に割り当てられたユニークID    
	- `stop_name[string]`: 停留所や駅の名前。同じ：GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt) の 'stop_name' フィールド。    
	- `stop_url[string]`: このフィールドには、特定の停留所に関するウェブページの URL が含まれ、agency_url および route_url フィールドとは異なります。同じ：GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt) の 'stop_url' フィールド。    
- `stopTimeUpdateInfo[object]`: schedule_relationshipが'CANCELED'の場合は考慮されない。同じ：GTFS Realtime message-TripUpdateの'stop_time_update'フィールド (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `stopScheduleRelationship[string]`: 静的スケジュールと停車駅の関係を記述する。同じ：'schedule_relationship' field from GTFS Realtime message-StopTimeUpdate ENUM[SCHEDULED, SKIPPED, NO_DATA] (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)    
	- `stop_id[string]`: この観測に対応する停留所に割り当てられたユニークID    
	- `stop_sequence[number]`: このフィールドは、特定のトリップにおける停車駅の順序を示す。stop_sequenceの値は負でない整数でなければならない。例えば、最初の停車駅のstop_sequenceは1、2番目の停車駅のstop_sequenceは23、3番目の停車駅のstop_sequenceは40、といった具合である。    
- `stopTimesInfo[object]`: 車両の走行スケジュールをリアルタイムに更新する記述子。  	- `arrival_time[time]`: ルート上の特定の旅行の特定の停留所への到着時刻を指定します。時間は、HH:MM:SS 形式で 8 桁である必要があります（時間が 0 で始まる場合は、HH:MM:SS も使用できます）。注：複数の日付にまたがるトリップは、24:00:00を超える停止時刻になります。たとえば、トリップが22時30分00秒に開始し、翌日の午前2時15分00秒に終了する場合、停止時刻は22時30分00秒と26時15分00秒になります。これらの停車時間を22:30:00と02:15:00と入力しても、望ましい結果は得られません。同じく：GTFS Static Field definitions-stop_times.txtの'arrival_time'フィールド (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `continuous_drop_off[number]`: 乗り物が走行経路のどの地点でも降りられるかどうかを示す：GTFS Static Field definitions-stop_times.txt（https://developers.google.com/transit/gtfs/reference#stop_timestxt）の「continuous_drop_off」フィールド。    
	- `continuous_pickup[number]`: 乗り手が車両の走行経路のどの地点でも乗り込むことができるかどうかを示す：GTFS Static Field definitions-stop_times.txt（https://developers.google.com/transit/gtfs/reference#stop_timestxt）の「continuous_pickup」フィールド。    
	- `departure_time[time]`: ルート上の特定の旅行について、特定の停留所からの出発時刻を指定します。時間は、HH:MM:SS 形式で 8 桁でなければなりません（時間が 0 で始まる場合は、HH:MM:SS も使用できます）。注：複数の日付にまたがるトリップは、24:00:00より大きい停止時刻になります。たとえば、トリップが22時30分00秒に開始し、翌日の午前2時15分00秒に終了する場合、停止時刻は22時30分00秒と26時15分00秒になります。これらの停車時間を22:30:00と02:15:00と入力しても、望ましい結果は得られません。同じく：GTFS Static Field definitions-stop_times.txtの「departure_time」フィールド (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `drop_off_type[string]`: ドロップオフの方法を示す。同じ：GTFS Static Field definitions-stop_times.txtの'drop_off_type'フィールド (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `pickup_type[string]`: ピックアップ方法を示す：GTFS Static Field definitions-stop_times.txtの'pickup_type'フィールド (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `stop_headsign[string]`: このフィールドには、乗客に旅行の目的地を示す標識に表示されるテキストが含まれる。同じ：GTFS Static Field definitions-stop_times.txtの'stop_headsign'フィールド (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `stop_id[string]`: この観測に対応する停留所に割り当てられたユニークID    
	- `stop_sequence[number]`: このフィールドは、特定のトリップにおける停車駅の順序を示す。stop_sequenceの値は負でない整数でなければならない。例えば、最初の停車駅のstop_sequenceは1、2番目の停車駅のstop_sequenceは23、3番目の停車駅のstop_sequenceは40、といった具合である。    
	- `trip_id[string]`: この観測に対応するバスに割り当てられたトリップID/トリップ名。指定されたルートIDの時間帯と進行方向を考慮する。    
- `stop_code[string]`: このフィールドには、乗客のために停留所を一意に識別する短いテキストまたは番号が含まれる。公共の場合はstop_idと同じになる。同じ：GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt) の 'stop_code' フィールド。  - `stop_desc[string]`: このフィールドには停車駅の説明が含まれる。同じ：GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt) の 'stop_desc' フィールド。  - `stop_headsign[string]`: このフィールドには、乗客に旅行の目的地を示す標識に表示されるテキストが含まれる。同じ：GTFS Static Field definitions-stop_times.txtの'stop_headsign'フィールド (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `stop_id[string]`: 停留所ID/停留所名：この観測のバスに対応する停留所のID/停留所名。同じ：GTFS Realtime message-Vehiclepositionの'stop_id'フィールド (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `stop_name[string]`: バス停の名称を表します。同じ：GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt) の 'stop_name' フィールド。  - `stop_sequence[number]`: GTFSのstop_times.txtから参照できる。同じ：GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate) の 'stop_sequence' フィールド。  - `stop_sequence_detail[object]`: 公共交通車両が行う指定ルート内の移動の停車順序を記述する：GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt) の 'stop_sequence' フィールド。  	- `stop_id[string]`: 対応する GTFS フィードの stops.txt と同じでなければならない。StopTimeUpdate 内では、stop_sequence または stop_id のどちらかを指定する必要があります。    
	- `stop_sequence[number]`: 対応する GTFS フィードの stop_times.txt と同じでなければならない。stop_sequenceまたはstop_idのどちらかをStopTimeUpdate内で提供する必要がある - 両方のフィールドを空にすることはできない。stop_sequenceは、同じstop_idを複数回訪れるトリップ(ループなど)で、どのストップに対する予測かを曖昧にしないために必要である。    
- `stop_time_update[object]`: この旅行を提供する車両に関する追加情報  	- `arrival[object]`: schedule_relationshipが空またはSCHEDULEDの場合、StopTimeUpdate内で到着または出発のどちらかを指定する必要があり、両方のフィールドを空にすることはできません。schedule_relationship が NO_DATA の場合、 arrival と departure は空でなければなりません。    
	- `departure[object]`: schedule_relationshipが空またはSCHEDULEDの場合、StopTimeUpdate内で到着または出発のどちらかを指定する必要があり、両方のフィールドを空にすることはできません。schedule_relationship が NO_DATA の場合、 arrival と departure は空でなければなりません。    
	- `schedule_relationship[string]`: SCHEDULED、SKIPPED、NO_DATA'。SCHEDULEDは、車両が停車駅の静的なスケジュールに従って進行していることを意味するが、必ずしもスケジュールの時間に従っている必要はない。これはデフォルトの動作である。到着と出発の少なくとも一方は提供されなければならない。SKIPPEDは、ストップがスキップされる、すなわち、車両がこのストップで停止しないことを意味する。arrival と departure フィールドはオプションである。NO_DATA は、この停留所にデータが与えられていないことを意味する。これは、利用可能なリアルタイム情報がないことを示す。NO_DATA が設定されると、それ以降の停車駅に伝搬されるため、どの停車駅からリアルタイムの情報がないかを指定するには、この方法を推奨する。NO_DATAが設定されている場合、到着も出発も提供されるべきではない。    
	- `stop_id[string]`: 対応する GTFS フィードの stops.txt と同じでなければならない。StopTimeUpdate 内では、stop_sequence または stop_id のどちらかを指定する必要があります。    
	- `stop_sequence[number]`: 対応する GTFS フィードの stop_times.txt と同じでなければならない。stop_sequenceまたはstop_idのどちらかをStopTimeUpdate内で提供する必要がある - 両方のフィールドを空にすることはできない。stop_sequenceは、同じstop_idを複数回訪れるトリップ(ループなど)で、どのストップに対する予測かを曖昧にしないために必要である。    
- `stop_url[string]`: このフィールドには、特定の停留所に関するウェブページの URL が含まれ、agency_url および route_url フィールドとは異なります。同じ：GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt) の 'stop_url' フィールド。  - `timestamp[date-time]`: 車両からの最終観測報告時刻同じ：GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'timestamp'フィールド。  - `travelDistance[number]`: 出発地のバス停から目的地のバス停までの距離、またはこの観測に対応する総移動距離。  - `travelTime[time]`: HH:MM:SS形式（0から始まる場合はHH:MM:SSも可）での、この観測に対応する出発地と目的地間の移動に要した時間  - `trip[object]`: この観測に対応する車両が行っているトリップを記述する。SameAs: GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)の'trip'フィールド。  	- `direction_id[number]`: この観測に対応する車両の進行方向を示す。GTFS の静的フィード trips.txt から参照できる。同じ：GTFS Realtime message-TripDescriptorの'direction_id'フィールド (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
	- `route_id[string]`: この観測のバスに対応するバス/車両が現在走行しているルートに割り当てられたルートID。同じ：GTFS Realtime message-TripDescriptorの'route_id'フィールド (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
	- `schedule_relationship[string]`: ルート/トリップがスケジュールされているかどうかを説明します。同じ：enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2) の 'schedule_relationship' フィールドです。    
	- `start_date[string]`: この観測車両に対応する旅行の最初の予定日を記述する。このフィールドのフォーマット例 - YYYYMMDD。同じ：GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor) の 'start_date' フィールド。    
	- `start_time[string]`: この観測車両に対応するトリップの最初の予定開始時刻を記述する。このフィールドのフォーマット例 - 11:15:35または25:15:35。同じ：GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor) の 'start_time' フィールド。    
	- `trip_id[string]`: この観測に対応するバスに割り当てられたトリップID/トリップ名で、指定されたrouteIdの時間帯と進行方向を考慮する。同じ：GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor) の 'trip_id' フィールド。    
- `tripDetails[object]`: 車両の走行スケジュールをリアルタイムに更新する記述子。  	- `arrival_time[time]`: ルート上の特定の旅行の特定の停留所への到着時刻を指定します。時間は、HH:MM:SS 形式で 8 桁である必要があります（時間が 0 で始まる場合は、HH:MM:SS も使用できます）。注：複数の日付にまたがるトリップは、24:00:00を超える停止時刻になります。たとえば、トリップが22時30分00秒に開始し、翌日の午前2時15分00秒に終了する場合、停止時刻は22時30分00秒と26時15分00秒になります。これらの停車時間を22:30:00と02:15:00と入力しても、望ましい結果は得られません。同じく：GTFS Static Field definitions-stop_times.txtの'arrival_time'フィールド (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `departure_time[time]`: ルート上の特定の旅行について、特定の停留所からの出発時刻を指定します。時間は、HH:MM:SS 形式で 8 桁でなければなりません（時間が 0 で始まる場合は、HH:MM:SS も使用できます）。注：複数の日付にまたがるトリップは、24:00:00より大きい停止時刻になります。たとえば、トリップが22時30分00秒に開始し、翌日の午前2時15分00秒に終了する場合、停止時刻は22時30分00秒と26時15分00秒になります。これらの停車時間を22:30:00と02:15:00と入力しても、望ましい結果は得られません。同じく：GTFS Static Field definitions-stop_times.txtの「departure_time」フィールド (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `stop_headsign[string]`: このフィールドには、乗客に旅行の目的地を示す標識に表示されるテキストが含まれる。同じ：GTFS Static Field definitions-stop_times.txtの'stop_headsign'フィールド (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `stop_id[string]`: 停留所ID/停留所名：この観測のバスに対応する停留所のID/停留所名。同じ：GTFS Realtime message-Vehiclepositionの'stop_id'フィールド (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
	- `stop_sequence[number]`: GTFSのstop_times.txtから参照できる。同じ：GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate) の 'stop_sequence' フィールド。    
- `tripDirection[string]`: ENUM[UP,DN]で車両の進行方向を示す。  - `tripInfo[object]`: この観測に対応する車両が行っているトリップを記述する。SameAs: GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'trip'フィールド。  	- `route_id[string]`: この観測のバスに対応するバス/車両が現在走行しているルートに割り当てられたルートID。    
	- `schedule_relationship[string]`: ルート/トリップがスケジュールされているかどうかを説明します。同じ：GTFS Realtime message-TripDescriptorの'schedule_relationship'フィールド ENUM[SCHEDULED, ADDED, UNSCHEDULED, CANCELED] (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
	- `start_date[string]`: この観測車両に対応する旅行の最初の予定日を記述する。このフィールドのフォーマット例 - YYYYMMDD。同じ：GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor) の 'start_date' フィールド。    
	- `start_time[time]`: この観測車両に対応するトリップの最初の予定開始時刻を記述する。このフィールドのフォーマット例 - 11:15:35または25:15:35。同じ：GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor) の 'start_time' フィールド。    
	- `trip_direction[string]`: この観測に対応する車両の進行方向を示す。GTFS の静的フィード trips.txt から参照できる。同じ：GTFS Realtime message-TripDescriptorの'direction_id'フィールド (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
	- `trip_id[string]`: この観測に対応するバスに割り当てられたトリップID/トリップ名。指定されたルートIDの時間帯と進行方向を考慮する。    
- `trip_delay[number]`: これは秒単位でプラスにもマイナスにもなり、車両が計画からどれだけ逸脱したかを示す。同じ：GTFS Realtime message-StopTimeEventの'delay'フィールド (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)  - `trip_details[object]`: 車両の走行スケジュールをリアルタイムに更新する記述子。  	- `bearing[number]`: 方位は度単位で、真北から時計回り、つまり0は北、90は東。これはコンパスの方位、または次の停車駅や中間地点に向かう方位である。これは、クライアントが以前のデータから計算できる、以前の位置のシーケンスから推測されるべきではありません。    
	- `odometer[number]`: オドメーター値（単位：メートル    
	- `speed[number]`: 車両が計測した瞬間速度（単位：メートル毎秒    
- `trip_direction[string]`: 車両の進行方向を示す。同じ：GTFS Realtime message-TripDescriptorの'direction_id'フィールドであるが、'direction_id' (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)のように[0,1]の代わりにENUM[UP,DN]の形式で表現される。  - `trip_id[string]`: この観測に対応するバスに割り当てられたトリップID/トリップ名で、指定されたrouteIdの時間帯と進行方向を考慮する。同じ：GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor) の 'trip_id' フィールド。  - `trip_update[object]`: この観測に対応する車両が行ったトリップの遅延、出発などのトリップ情報を記述する。SameAs:'trip_update'フィールド from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  	- `stop_time_update[object]`: この旅行を提供する車両に関する追加情報    
	- `timestamp[date-time]`: 車両からの最終観測報告時刻同じ：GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'timestamp'フィールド。    
	- `trip[object]`: この観測に対応する車両が行っているトリップを記述する。SameAs: GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)の'trip'フィールド。    
	- `vehicleDesc[object]`: この観測に対応する車両の付加情報を記述する。SameAs: GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)の'vehicle'フィールド。    
- `type[string]`: NGSIエンティティタイプ。TransitManagement でなければならない。  - `uncertainty[number]`: 不確実性が省略された場合、不明と解釈される。完全に確実な予測を指定するには、その不確実性を0.SameAsに設定する：GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)の'uncertainty'フィールド。  - `vehicleDesc[object]`: この観測に対応する車両の付加情報を記述する。SameAs: GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)の'vehicle'フィールド。  	- `license_plate[string]`: 車両のナンバープレートを示す：SameAs: 'license_plate' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)    
	- `vehicle_id[string]`: このオブザベーションに対応する車両に割り当てられたユニークID：GTFSリアルタイムメッセージの'id'フィールド - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)    
	- `vehicle_label[string]`: ユーザーの目に見えるラベル。つまり、正しい車両を識別するために乗客に示さなければならないもの：GTFSリアルタイムメッセージの'label'フィールド - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)    
- `vehicleInfo[object]`: この観測に対応する車両の付加情報を記述する。SameAs: GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)の'vehicle'フィールド。  	- `license_plate[string]`: 車のナンバーを表示します。同じ：GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor) の 'license_plate' フィールド。    
	- `vehicleID[string]`: このオブザベーションに対応する車両に割り当てられたユニークID。同じ：GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor) の 'id' フィールド。    
	- `vehicle_label[string]`: ユーザーの目に見えるラベル、すなわち、正しい車両を識別するために同乗者に見せなければならないもの。同じ：GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor) の 'label' フィールド。    
- `vehiclePositionInfo[object]`: この観測に対応する車両のリアルタイム位置を記述する。GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)の'vehicle'フィールドと同じ。  	- `actual_trip_start_time[date-time]`: このフィールドは、実際にサービスが開始された時刻を指定する。これはSameAs: GTFS Realtime message-TripUpdate(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)の stop_time_update(StopTimeUpdate)メッセージの'arrival'フィールドの絶対 'time'(StopTimeEvent)である。    
	- `agencyInfo[object]`: この観測に対応する代理店情報。    
	- `arrivalUncertainty[number]`: schedule_relationshipが空またはSCHEDULEDの場合、StopTimeUpdate内で到着または出発のどちらかを提供する必要があります。同じ：GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)の'arrival'フィールド。    
	- `congestion_level[string]`: この車両に影響を及ぼしている混雑レベルを記述する。enum [unknown_congestion_level、running_smoothly、stop_and_go、congestion、severe_congestion]。    
	- `current_status[string]`: ENUM:[INCOMING_AT,STOPPED_AT,IN_TRANSIT_TO]。SameAs: GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'current_status'フィールド。    
	- `current_stop_sequence[number]`: 現在の停止位置の停止シーケンスインデックスを与える。current_status がない場合は IN_TRANSIT_TO とみなされる。GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'current_stop_sequence'フィールドと同じ。    
	- `departureUncertainty[number]`: schedule_relationshipが空またはSCHEDULEDの場合、StopTimeUpdate内で到着または出発のどちらかを提供する必要があります。同じ：GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)の'departure'フィールド。    
	- `depotID[string]`: このオブザベーションに対応するバスデポのユニークIDを記述する。    
	- `depotName[string]`: このオブザベーションに対応するバスデポのデポ名を記述する。    
	- `entity_id[string]`: このオブザベーションに対応するエンティティのフィードユニークID。SameAs:'entity_id' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)    
	- `occupancy_status[string]`: 車両の乗車率。enum [empty, many_seats_available, few_seats_available, standing_room_only, crushed_standing_room_only, full, not_accepting_passengers, no_data_available, not_boardable].    
	- `positionInfo[object]`: この観測に対応する車両の現在位置を記述する。GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'position'フィールドと同じ。    
	- `route_id[string]`: この観測のバスに対応するバス/車両が現在走行しているルートに割り当てられたルートID。同じ：GTFS Realtime message-TripDescriptorの'route_id'フィールド (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)。    
	- `stopInfo[object]`: この観測に対応する車両の走行経路に関する情報。    
	- `stopTimesInfo[object]`: 走行中の車両のスケジュールをリアルタイムに更新する記述子。    
	- `stop_id[string]`: この観測に対応する停留所に割り当てられたユニークID    
	- `travelDistance[number]`: 出発地から目的地までの距離、またはこの観測に対応する総移動距離。    
	- `tripInfo[object]`: この観測に対応する車両が行っているトリップを記述する。GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'trip'フィールドと同じ。    
	- `vehicleInfo[object]`: この観測に対応する車両の付加情報を記述する。SameAs: GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)の'vehicle'フィールド。    
- `vehicleType[string]`: 固形廃棄物処理車両の場合はホッパー、コンパクター、ティッパー、ダンパー、ITMS車両の場合はBRTミニバス、BRTバス、シティバス、緊急車両の場合は救急車、消防車、警察車両など、車両登録の場合は原付/スクーター、モーターサイクル、オートリキシャ、自家用車/ジープ車、テンポ、バス、E-原付/E-スクーター/E-モーターサイクル、公共モーターなど。  - `vehicle_id[string]`: このオブザベーションに対応する車両に割り当てられたユニークID。同じ：GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor) の 'id' フィールド。  - `vehicle_label[string]`: ユーザーの目に見えるラベル、すなわち、正しい車両を識別するために同乗者に見せなければならないもの。同じ：GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor) の 'label' フィールド。  - `vehicle_position[object]`: この観測に対応する車両のリアルタイム位置を記述する。GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)の'vehicle'フィールドと同じ。  	- `current_status[string]`: ENUM:[INCOMING_AT,STOPPED_AT,IN_TRANSIT_TO]。SameAs: GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'current_status'フィールド。    
	- `current_stop_sequence[number]`: 現在の停止位置の停止シーケンスインデックスを与える。current_status がない場合は IN_TRANSIT_TO とみなされる。GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'current_stop_sequence'フィールドと同じ。    
	- `position[object]`: このオブザベーションに対応する車両の現在位置を記述する。同じ：GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'position'フィールド。    
	- `stop_id[string]`: 停留所ID/停留所名：この観測のバスに対応する停留所のID/停留所名。同じ：GTFS Realtime message-Vehiclepositionの'stop_id'フィールド (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
	- `timestamp[date-time]`: 車両からの最終観測報告時刻同じ：  GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)の'timestamp'フィールド。    
	- `trip[object]`: この観測に対応する車両が行っているトリップを記述する。SameAs: GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)の'trip'フィールド。    
	- `vehicleDesc[object]`: この観測に対応する車両の付加情報を記述する。SameAs: GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)の'vehicle'フィールド。    
<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
      description: "Specifies the arrival time at the previous stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (H:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. This is SameAs: absolute 'time'(StopTimeEvent) in the 'arrival' field of the stop_time_update (StopTimeUpdate) message of the GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
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
      description: "Updated sorted stop sequence for the trip made by the vehicle corresponding to this observation, not to be considered if schedule_relationship is 'CANCELED'. SameAs: 'stop_time_update' field from GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
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
      description: Gives the stop ids/stop codes or station ids/station codes in the right sequence for the route or line or trip corresponding to this observation    
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
          description: 'Sequence in which the shape points connect to form the shape. Values must increase along the trip but do not need to be consecutive. Example: If the shape ''A_shp'' has three points in its definition, the shapes.txt file might contain these records to define the shape: shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence A_shp,37.61956,-122.48161,0 A_shp,37.64430,-122.41070,6 A_shp,37.65863,-122.30839,11'    
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
    standingCapacity:    
      description: Describes the passenger standing capacity of the vehicle corresponding to this observation.    
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
      description: "Updated sorted stop sequence for the trip made by the vehicle corresponding to this observation, not to be considered if schedule_relationship is 'CANCELED'. SameAs: 'stop_time_update' field from GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
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
      description: 'The time taken to travel between the origin location and the destination location corresponding to this observation in HH:MM:SS format(HH:MM:SS is also accepted, if the hour begins with 0)'    
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
        actual_trip_start_time:    
          description: "This field specifies the time at which service actually began. This is SameAs: absolute 'time'(StopTimeEvent) in the 'arrival' field of the stop_time_update (StopTimeUpdate) message of the GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)."    
          format: date-time    
          type: string    
          x-ngsi:    
            type: Property    
        agencyInfo:    
          description: Agency information corresponding to this observation.    
          properties:    
            agency_email:    
              description: "Email address actively monitored by the agency’s customer service department. SameAs: 'agency_email' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)."    
              type: string    
              x-ngsi:    
                type: Property    
            agency_fare_url:    
              description: "URL of a web page that contains the details of the fares and also could allow to purchase tickets for that agency online. SameAs: 'agency_fare_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)."    
              type: string    
              x-ngsi:    
                type: Property    
            agency_id:    
              description: "ID that uniquely identifies a transit agency. A transit feed may represent data from more than one agency. The agency_id is dataset unique. This field is optional for transit feeds that only contain data for a single agency. SameAs: 'agency_id' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)."    
              type: string    
              x-ngsi:    
                type: Property    
            agency_lang:    
              description: "Contains a two-letter ISO 639-1 code for the primary language used by this transit agency. The language code is case-insensitive (both en and EN are accepted). SameAs: 'agency_lang' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)."    
              type: string    
              x-ngsi:    
                type: Property    
            agency_name:    
              description: "The agency_name field contains the full name of the transit agency. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)."    
              type: string    
              x-ngsi:    
                type: Property    
            agency_phone:    
              description: "A voice telephone number for the specified agency.SameAs: 'agency_phone' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)."    
              type: string    
              x-ngsi:    
                type: Property    
            agency_timezone:    
              description: "Timezone field contains the timezone where the transit agency is located. SameAs: 'agency_timezone' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)."    
              type: string    
              x-ngsi:    
                type: Property    
            agency_url:    
              description: "The agency_url field contains the URL of the transit agency. SameAs: 'agency_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)."    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        arrivalUncertainty:    
          description: "If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'arrival' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)."    
          type: number    
          x-ngsi:    
            type: Property    
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
        departureUncertainty:    
          description: "If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'departure' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)."    
          type: number    
          x-ngsi:    
            type: Property    
        depotID:    
          description: Describes the unique id of the bus depot corresponding to this observation.    
          type: string    
          x-ngsi:    
            type: Property    
        depotName:    
          description: Describes the depot name of the bus depot corresponding to this observation.    
          type: string    
          x-ngsi:    
            type: Property    
        entity_id:    
          description: "Feed unique ID for the entity corresponding to this observation.SameAs:'entity_id' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"    
          type: string    
          x-ngsi:    
            type: Property    
        occupancy_status:    
          description: 'The degree of passenger occupancy for the vehicle. ENUM [EMPTY, MANY_SEATS_AVAILABLE, FEW_SEATS_AVAILABLE, STANDING_ROOM_ONLY, CRUSHED_STANDING_ROOM_ONLY, FULL, NOT_ACCEPTING_PASSENGERS, NO_DATA_AVAILABLE, NOT_BOARDABLE]'    
          type: string    
          x-ngsi:    
            type: Property    
        positionInfo:    
          description: "Describes the current position of the vehicle corresponding to this observation. SameAs:'position' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)."    
          properties:    
            bearing:    
              description: 'Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data'    
              type: number    
              x-ngsi:    
                type: Property    
            odometer:    
              description: Odometer value.    
              type: number    
              x-ngsi:    
                type: Property    
            speed:    
              description: Momentary speed measured by the vehicle.    
              type: number    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        route_id:    
          description: "Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
          type: string    
          x-ngsi:    
            type: Property    
        stopInfo:    
          description: Information about the path the vehicle corresponding to this observation travels along.    
          properties:    
            stop_code:    
              description: "This field contains short text or a number that uniquely identifies the stop for passengers. Can be same as stop_id if it is for public. SameAs: 'stop_code' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)."    
              type: string    
              x-ngsi:    
                type: Property    
            stop_desc:    
              description: "This field contains a description of a stop. SameAs: 'stop_desc' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)."    
              type: string    
              x-ngsi:    
                type: Property    
            stop_id:    
              description: Unique ID assigned to the stop corresponding to this observation.    
              type: string    
              x-ngsi:    
                type: Property    
            stop_name:    
              description: "Describes the name of a stop or station. SameAs: 'stop_name' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)."    
              type: string    
              x-ngsi:    
                type: Property    
            stop_url:    
              description: "This field contains the URL of a web page about a particular stop and is different from the agency_url and the route_url fields. SameAs: 'stop_url' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)."    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        stopTimesInfo:    
          description: A descriptor of realtime update on the schedule of a vehicle along a trip.    
          properties:    
            arrival_time:    
              description: "Specifies the arrival time at a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'arrival_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)."    
              format: time    
              type: string    
              x-ngsi:    
                type: Property    
            continuous_drop_off:    
              description: "Indicates whether a rider can alight from the transit vehicle at any point along the vehicle’s travel path.SameAs: 'continuous_drop_off' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)."    
              type: number    
              x-ngsi:    
                type: Property    
            continuous_pickup:    
              description: "Indicates whether a rider can board the transit vehicle at any point along the vehicle’s travel path.SameAs: 'continuous_pickup' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)."    
              type: number    
              x-ngsi:    
                type: Property    
            departure_time:    
              description: "Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)."    
              format: time    
              type: string    
              x-ngsi:    
                type: Property    
            drop_off_type:    
              description: "Indicates drop off method. SameAs: 'drop_off_type' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)."    
              type: string    
              x-ngsi:    
                type: Property    
            pickup_type:    
              description: "Indicates pickup method.SameAs: 'pickup_type' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)."    
              type: string    
              x-ngsi:    
                type: Property    
            stop_headsign:    
              description: "This field contains the text that appears on a sign that identifies the trip’s destination to passengers. SameAs: 'stop_headsign' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)."    
              type: string    
              x-ngsi:    
                type: Property    
            stop_id:    
              description: Unique ID assigned to the stop corresponding to this observation.    
              type: string    
              x-ngsi:    
                type: Property    
            stop_sequence:    
              description: 'This field identifies the order of the stops for a particular trip. The values for stop_sequence must be non-negative integers, and they must increase along the trip. For example, the first stop on the trip could have a stop_sequence of 1, the second stop on the trip could have a stop_sequence of 23, the third stop could have a stop_sequence of 40, and so on.'    
              type: number    
              x-ngsi:    
                type: Property    
            trip_id:    
              description: 'Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId.'    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        stop_id:    
          description: Unique ID assigned to the stop corresponding to this observation    
          type: string    
          x-ngsi:    
            type: Property    
        travelDistance:    
          description: The distance between the origin location and the destination location or the total distance travelled corresponding to this observation.    
          type: number    
          x-ngsi:    
            type: Property    
        tripInfo:    
          description: "Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)."    
          properties:    
            route_id:    
              description: Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on.    
              type: string    
              x-ngsi:    
                type: Property    
            schedule_relationship:    
              description: "Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from GTFS Realtime message-TripDescriptor ENUM[SCHEDULED, ADDED, UNSCHEDULED, CANCELED] (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
              x-ngsi:    
                type: Property    
            start_date:    
              description: "Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
              x-ngsi:    
                type: Property    
            start_time:    
              description: "Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              format: time    
              type: string    
              x-ngsi:    
                type: Property    
            trip_direction:    
              description: "Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
              x-ngsi:    
                type: Property    
            trip_id:    
              description: 'Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId.'    
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
              description: "Gives the License Plate number of the vehice. SameAs: 'license_plate' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
              x-ngsi:    
                type: Property    
            vehicleID:    
              description: "Unique ID assigned to the vehicle corresponding to this observation, used in internal system identification. SameAs: 'id' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
              x-ngsi:    
                type: Property    
            vehicle_label:    
              description: "User visible label, i.e., something that must be shown to the passenger to help identify the correct vehicle. SameAs: 'label' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/TransitManagement/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/TransitManagement/schema.json    
  x-model-tags: IUDX    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### TransitManagement NGSI-v2 キー値の例  
JSON-LD形式のTransitManagementのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
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
#### TransitManagement NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のTransitManagementの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "type": "Text",  
    "value": "22:11:14"  
  },  
  "direction_id": {  
    "type": "Boolean",  
    "value": false  
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
    "type": "Text",  
    "value": "http://charteredbike.in/surat/?page_id=1021"  
  },  
  "actual_trip_end_time": {  
    "type": "DateTime",  
    "value": "2021-10-28T08:24:22+05:30"  
  },  
  "last_tracked_time": {  
    "type": "Text",  
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
    "type": "DateTime",  
    "value": "2021-10-28T08:13:22+05:30"  
  },  
  "arrival_time": {  
    "type": "Text",  
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
    "value": false  
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
    "type": "DateTime",  
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
    "type": "DateTime",  
    "value": "2022-03-01"  
  },  
  "current_stop_sequence": {  
    "type": "Number",  
    "value": 1001  
  },  
  "start_time": {  
    "type": "Text",  
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
    "type": "Text",  
    "value": "http://charteredbike.in/surat/"  
  },  
  "routeStopSequence": {  
    "type": "StructuredValue",  
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
    "type": "Text",  
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
    "type": "DateTime",  
    "value": "2021-10-28T08:13:22+05:30"  
  }  
}  
```  
</details>  
#### TransitManagement NGSI-LD キー値の例  
JSON-LD形式のTransitManagementのkey-valuesの例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### トランジットマネジメント NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のTransitManagementの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
