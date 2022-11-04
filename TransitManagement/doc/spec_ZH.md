<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。交通管理  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/TransitManagement/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**一个公共运输系统的数据模型**  
版本：0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `ac_available[string]`: 描述了与此观察相对应的车辆中存在的空调选项。  - `actual_trip_end_time[string]`: 这个字段规定了与这个观察结果相对应的服务或旅行预定结束的时间。  - `actual_trip_start_time[string]`: 这个字段规定了服务实际开始的时间。  这与GTFS实时消息-TripUpdate(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)的stop_time_update(StopTimeUpdate)消息的'到达'字段的绝对'时间'(StopTimeEvent)相同。  - `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `agency_fare_url[string]`: 包含票价详情的网页的URL，也可以允许在线购买该机构的票。与此相同。来自GTFS静态字段定义的'agency_fare_url'字段 - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_id[string]`: 唯一能识别一个交通机构的ID。一个交通资料可能代表来自一个以上机构的数据。机构ID是数据集唯一的。这个字段对于只包含一个机构的数据的转运资料是可选的。与此相同。来自GTFS静态字段定义的'agency_id'字段 - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_lang[string]`: 包含一个两个字母的ISO 639-1代码，用于该交通机构使用的主要语言。语言代码是不分大小写的（en和EN都可以接受）。与此相同。来自GTFS静态字段定义的'agency_lang'字段 - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_name[string]`: agency_name字段包含过境机构的全名。与此相同。来自GTFS静态字段定义的'agency_name'字段 - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_timezone[string]`: 时区字段包含交通机构所在的时区。与此相同。来自GTFS静态字段定义的'agency_timezone'字段 - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_url[string]`: agency_url字段包含交通机构的URL。与此相同。agency_url'字段来自GTFS静态字段定义--agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrival[object]`: 如果schedule_relationship为空或SCHEDULED，必须在StopTimeUpdate中提供到达或离开。与此相同。GTFS实时消息-停止时间更新中的'到达'字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `arrival_time[string]`: 指定路线上某一特定行程的某一站的到达时间。时间必须是八位数的HH:MM:SS格式（HH:MM:SS也可以接受，如果小时以0开头）。注意：跨越多个日期的旅行将有大于24:00:00的停车时间。例如，如果一个旅行在晚上10:30:00开始，在第二天凌晨2:15:00结束，停止时间将是22:30:00和26:15:00。将这些停车时间输入为22:30:00和02:15:00将不会产生所需的结果。同理。GTFS静态字段定义中的'到达时间'字段-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `bearing[number]`: 提供车辆GPS的角度，以顺时针方向从真北测量。与GTFS实时信息-位置(https://developers.google.com/transit/gtfs-realtime/reference#message-position)的 "方位 "字段相同。  - `current_status[string]`: 描述车辆在与此观察相对应的停车点的状态 ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]。同上：GTFS实时消息中的'当前状态'字段-车辆位置(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `current_stop_sequence[number]`: 给出当前站点的序列索引。这是通过考虑current_status确定的，如果current_status缺失，则假定为IN_TRANSIT_TO。与GTFS实时信息中的'current_stop_sequence'字段相同--车辆位置(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `dataDescriptor[string]`: 指向数据描述器实体的URI  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `departure[object]`: 如果schedule_relationship为空或SCHEDULED，必须在StopTimeUpdate中提供到达或离开。与此相同。GTFS实时消息中的'出发'字段-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `departure_time[string]`: 指定路线上某一特定行程从某一站出发的时间。时间必须是八位数的HH:MM:SS格式（HH:MM:SS也可以接受，如果小时以0开头）。  
注意：跨越多个日期的旅行将有大于24:00:00的停车时间。例如，如果一个旅行在晚上10:30:00开始，在第二天凌晨2:15:00结束，停止时间将是22:30:00和26:15:00。将这些停车时间输入为22:30:00和02:15:00将不会产生所需的结果。同理。'departure_time'字段来自GTFS静态字段定义-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `depot_id[string]`: 描述了与该观察值相对应的公交车库的唯一ID。  - `depot_name[string]`: 描述与该观察值相对应的公共汽车库的库区名称。  - `description[string]`: 对这个项目的描述  - `deviceInfo[object]`: 与观察结果有关的设备信息。  . Model: [https://schema.org/Text](https://schema.org/Text)- `direction_id[number]`: 表示与该观测值相对应的车辆行驶方向，可从GTFS静态资料trips.txt中引用。与此相同。来自GTFS实时消息-行程描述符的'方向_id'字段(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `entity_id[string]`: 响应此观察的实体的唯一ID。与GTFS实时消息-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)中的'entity_id'字段相同。  - `id[*]`: 实体的唯一标识符  - `last_stop_arrival_time[string]`: 指定路线上某一特定行程的前一站的到达时间。时间必须是八位数的HH:MM:SS格式（如果小时以0开头，H:MM:SS也可以接受）。  
注意：跨越多个日期的旅行将有大于24:00:00的停车时间。例如，如果一个旅行在晚上10:30:00开始，在第二天凌晨2:15:00结束，停止时间将是22:30:00和26:15:00。将这些停止时间输入为22:30:00和02:15:00将不会产生预期的结果。这是SameAs：GTFS实时消息-TripUpdate(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)的stop_time_update(StopTimeUpdate)消息的 "到达 "字段中的绝对 "时间"(StopTimeEvent)  - `last_stop_id[string]`: 与本次观察中的巴士相对应的前一个巴士站的站号/站名。与此相同。GTFS实时信息-车辆位置的'stop_id'字段(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `last_tracked_time[string]`: 提供车辆最后被追踪的时间。  - `license_plate[string]`: 提供车辆的车牌号。与此相同。来自GTFS实时信息-车辆描述符的'license_plate'字段(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `observationDateTime[string]`: 最后报告的观察时间。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `position[object]`: 描述了与此观测相对应的车辆的当前位置。同上：GTFS实时信息中的位置字段-车辆位置(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  . Model: [https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition](https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)- `routeStopSequence[array]`: 给出与此观察对应的路线或线路的正确顺序的站名IDs/站码或车站IDs/站码。  - `route_color[string]`: 如果分配了，这个字段定义了一个与路线相对应的颜色。颜色必须以六个字符的十六进制数字提供，例如，00FFFF。如果没有指定颜色，默认的路由颜色是白色(FFFFF)。与此相同。来自GTFS静态字段定义-routes.txt的'route_color'字段 (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_desc[string]`: 路线的描述。这可以包括整个路线的细节，包括往返目的地和时间信息的文本描述形式。与此相同。GTFS静态字段定义-routes.txt中的'route_desc'字段 (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_id[string]`: 分配给与本观察中的公共汽车/车辆相对应的公共汽车/车辆目前正在行驶的路线的路线ID。与此相同。GTFS实时消息-行程描述符中的'路线_ID'字段(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `route_long_name[string]`: 航线的全名。这个名称比routeShortName更有描述性，通常包括路线的目的地或停靠点。这主要包括路线的目的地和出发地名称。与此相同。'route_long_name' 字段来自 GTFS 静态字段定义-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_short_name[string]`: 一条路线的简短名称。这通常是公交车的车牌名，如'402D'，或'Green'，乘客用它来识别一条路线。与此相同。'route_short_name' 字段来自GTFS静态字段定义-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_text_color[string]`: 这个字段可以用来指定一个可读的颜色，用于在route_color的背景下绘制文本。颜色必须以六位数的十六进制数字提供，例如，FFD700。如果没有指定颜色，默认的文本颜色是黑色（0000）。同理。'route_text_color' 字段来自 GTFS 静态字段定义-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_type[string]`: 表示运输类型的数字-1-地铁，Metro。大都市范围内的任何地下铁路系统。2 - 铁路。用于城际或长途旅行。3 - 巴士。用于短途和长途巴士线路。与此相同。路线类型 "字段来自GTFS静态字段定义-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_url[string]`: 包含关于该特定路线的网页的URL，与agency_url不同。与此相同。'route_url' 字段来自 GTFS 静态字段定义-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `schedule_relationship[string]`: 描述路线/行程是否已被安排。与此相同。'schedule_relationship'字段来自enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)  - `seating_capacity[number]`: 描述了与该观察结果相对应的车辆的乘客座位数。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `speed[number]`: 给出车辆的速度。与GTFS实时信息中的'速度'字段相同(https://developers.google.com/transit/gtfs-realtime/reference#message-position)  - `standing_capacity[number]`: 描述了与该观察结果相对应的车辆的乘客站立能力。  - `start_date[string]`: 描述了与此观察的车辆相对应的行程的最初预定日期。这个字段的一个示例格式--YYYMMDD。与此相同。'start_date'字段来自GTFS实时消息-行程描述符(https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `start_time[string]`: 描述了与此观察的车辆相对应的行程的初始预定开始时间。这个字段的一个示例格式--11:15:35或25:15:35。与此相同。start_time "字段来自GTFS实时消息-行程描述符（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）。  - `stop_code[string]`: 这个字段包含简短的文本或数字，为乘客唯一地识别该站。如果是为公众服务，可以与stop_id相同。与此相同。'stop_code'字段来自GTFS静态字段定义-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_desc[string]`: 该字段包含对一个站点的描述。与此相同。'stop_desc'字段来自GTFS静态字段定义-stops.txt（https://developers.google.com/transit/gtfs/reference#stopstxt）。  - `stop_headsign[string]`: 这个字段包含了出现在标志上的文字，向乘客标明行程的目的地。与此相同。'stop_headsign' 字段来自GTFS静态字段定义-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `stop_id[string]`: 在此观察中，与公交车相对应的公交站点的站名ID/站名。与此相同。来自GTFS实时信息-车辆位置的'stop_id'字段(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `stop_name[string]`: 描述巴士站的名称。与此相同。'stop_name'字段来自GTFS静态字段定义-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_sequence[number]`: 表示与该观测值相对应的车辆停止序列，可从GTFS静态饲料stop_times.txt中引用。与此相同。'stop_sequence'字段来自GTFS实时消息-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `stop_sequence_detail[object]`: 描述公共交通车辆在指定路线上的一个行程的停车顺序。'stop_sequence' 字段来自GTFS静态字段定义-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `stop_time_update[object]`: 关于为这次旅行服务的车辆的其他信息。  - `stop_url[string]`: 这个字段包含关于特定站点的网页URL，与 agency_url 和 route_url字段不同。与此相同。'stop_url'字段来自GTFS静态字段定义-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `timestamp[string]`: 最后报告的来自车辆的观察时间。与此相同。GTFS实时信息-车辆位置的'时间戳'字段(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `travelDistance[number]`: 起点公交站和终点公交站之间的距离或与此观察相对应的总路程。  - `travelTime[string]`: 与该观察点相对应的始发站和终点站之间的旅行时间，格式为HH:MM:SS（如果小时以0开头，HH:MM:SS也可以接受）。  - `trip[object]`: 描述与此观察对应的车辆正在进行的行程。同理：GTFS实时信息中的'行程'字段-车辆位置(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  - `tripDetails[object]`: 一个实时更新车辆沿途时间表的描述符。  - `tripDirection[string]`: 给出车辆行驶的方向 ENUM[UP,DN] 。  - `trip_delay[number]`: 这可以是正的，也可以是负的，以秒为单位，显示车辆与计划中的偏差有多大。与此相同。GTFS实时信息-停止时间事件的'延迟'字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)  - `trip_details[object]`: 一个实时更新车辆沿途时间表的描述符。  - `trip_direction[string]`: 给出车辆行驶的方向。与此相同。GTFS实时消息-行程描述符中的'directory_id'字段，但以ENUM[UP,DN]的形式表示，而不是'directory_id'中的[0,1]（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）。  - `trip_id[string]`: 考虑到一天中的时间和给定路线上的行程方向，分配给该观察所对应的巴士的行程ID/行程名称。与此相同。GTFS实时消息-行程描述符中的'trip_id'字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `trip_update[object]`: 描述了与此观察相对应的车辆的行程信息，如延迟、出发等。与GTFS实时消息-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)中的'trip_update'域相同。  - `type[string]`: NGSI实体类型。它必须是TransitManagement  - `uncertainty[number]`: 如果省略了不确定性，则被解释为未知。要指定一个完全确定的预测，将其不确定性设置为0.SameAs。GTFS实时消息-StopTimeEvent的'不确定性'字段(https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)  - `vehicleDesc[object]`: 描述与此观察相对应的车辆的附加信息。同上：GTFS实时信息中的'车辆'字段-车辆位置(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  - `vehicleType[string]`: 描述与此观察相对应的车辆类型，如果是固体废物管理车辆，可以是料斗、压实机、翻斗车、翻斗车；如果是ITMS车辆，可以是BRT小型巴士、BRT巴士、城市巴士；如果是应急车辆，可以是救护车、消防车、警车等；如果是车辆登记，可以是轻便/摩托车、摩托车、自动人力车、私家车/吉普车、Tempo、巴士、电动摩托车/电动自行车、公共汽车。  - `vehicle_id[string]`: 分配给该观测点对应的车辆的唯一ID，用于内部系统识别。与此相同。来自GTFS实时信息-车辆描述符的'id'字段(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `vehicle_label[string]`: 用户可见的标签，即必须向乘客展示的东西，以帮助识别正确的车辆。与此相同。来自GTFS实时信息-车辆描述符的'标签'字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `vehicle_position[object]`: 描述了与此观测相对应的车辆的实时位置。同上：GTFS实时消息-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)中的'车辆'字段。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TransitManagement:    
  description: 'A public transit system Data Model'    
  properties:    
    ac_available:    
      description: 'Describes the presence of air conditioning option in the vehicle corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    actual_trip_end_time:    
      description: 'This field specifies the time at which service or trip corresponding to this observation is scheduled to end.'    
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
    arrival:    
      description: "If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'arrival' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"    
      properties:    
        uncertainty:    
          description: "Property. If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)."    
          type: number    
      type: object    
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
      description: 'URI pointing to the data-descriptor entity'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    departure:    
      description: "If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'departure' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"    
      properties:    
        uncertainty:    
          description: "Property. If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)."    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    departure_time:    
      description: "Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). \nNote: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
      format: time    
      type: string    
      x-ngsi:    
        type: Property    
    depot_id:    
      description: 'Describes the unique id of the bus depot corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    depot_name:    
      description: 'Describes the depot name of the bus depot corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    deviceInfo:    
      description: 'Information about the device associated with the observations.'    
      properties:    
        deviceBatteryStatus:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the Battery charging status of the reporting device(Connected, Disconnected).'    
          type: string    
        deviceID:    
          description: 'Property. Model:''https://schema.org/Text''. Device ID of the physical sensor/ measurement station corresponding to this observation.'    
          type: string    
        deviceModel:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the information of the device, sensor or system in consideration.'    
          properties:    
            brandName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of the brand associated with an entity, e.g., sensor, device etc.'    
              type: string    
            manufacturerName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of the manufacturer associated with an entity, e.g., sensor, device etc.'    
              type: string    
            modelName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of a specific model associated with an entity, e.g., sensor, device etc.'    
              type: string    
            modelURL:    
              description: 'Property. Model:''https://schema.org/Text''. URL providing further information of a specific model associated with an entity, e.g., sensor, device etc.'    
              type: string    
            observationDateTime:    
              description: 'Property. Last reported time of observation.'    
              format: date-time    
              type: string    
            trip_update:    
              description: "Property. Describes the trip information like delay, departures, etc., for a trip made by the vehicle corresponding to this observation.SameAs:'trip_update' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"    
              properties:    
                trip:    
                  description: "Property. Following the conventions of GTFS trip. Model:'https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor'. "    
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
              type: object    
          type: object    
        deviceName:    
          description: 'Property. Model:''https://schema.org/Text''. Device Name or Station name of the sensor device/station corresponding to this observation.'    
          type: string    
        deviceSimNumber:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the sim number of the device in the waste management vehicle.'    
          type: string    
        measurand:    
          description: 'Property. Model:''https://schema.org/Text''. Property/properties sensed/observed/measured by the device.'    
          type: string    
        rfID:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the ID of the RFID reader.'    
          type: string    
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
      description: "Feed unique ID for the entity corressponding to this observation.SameAs:'entity_id' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &transitmanagement_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Gives the time at which the vehicle was last tracked.'    
      format: time    
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
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *transitmanagement_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    position:    
      description: "Describes the current position of the vehicle corresponding to this observation. SameAs: position field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
      properties:    
        bearing:    
          description: 'Property. Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data'    
          type: number    
        latitude:    
          description: 'Property. Degrees North, in the WGS-84 coordinate system.'    
          type: number    
        longitude:    
          description: 'Property. Degrees East, in the WGS-84 coordinate system.'    
          type: number    
        odometer:    
          description: 'Property. Odometer value, in meters. Units:''meters'''    
          type: number    
        speed:    
          description: 'Property. Momentary speed measured by the vehicle, in meters per second. Units:''meters per second'''    
          type: number    
      type: object    
      x-ngsi:    
        model: "https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition"    
        type: Property    
    routeStopSequence:    
      description: 'Gives the stop IDs/stop codes or station IDs/station codes in the right sequence for the route or line corresponding to this observation.'    
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
      description: 'Describes the passenger seating capacity of the vehicle corresponding to this observation.'    
      type: number    
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
    speed:    
      description: "Gives the Speed  of the vehicle. SameAs 'speed' field from GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)"    
      type: number    
      x-ngsi:    
        type: Property    
    standing_capacity:    
      description: 'Describes the passenger standing capacity of the vehicle corresponding to this observation.'    
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
          description: 'Property. Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty.'    
          type: string    
        stop_sequence:    
          description: 'Property. Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for.'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    stop_time_update:    
      description: 'Additional information on the vehicle that is serving this trip.'    
      properties:    
        arrival:    
          description: 'Property. If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty.'    
          properties:    
            uncertainty:    
              description: "Property. If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)."    
              type: number    
          type: object    
        departure:    
          description: 'Property. If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty.'    
          properties:    
            uncertainty:    
              description: "Property. If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)."    
              type: number    
          type: object    
        schedule_relationship:    
          description: 'Property. Enum:''SCHEDULED, SKIPPED, NO_DATA''. SCHEDULED means that the vehicle is proceeding in accordance with its static schedule of stops, although not necessarily according to the times of the schedule. This is the default behavior. At least one of arrival and departure must be provided. SKIPPED means that The stop is skipped, i.e., the vehicle will not stop at this stop. The arrival and departure fields are optional. NO_DATA means that no data is given for this stop. It indicates that there is no realtime information available. When set NO_DATA is propagated through subsequent stops so this is the recommended way of specifying from which stop you do not have realtime information. When NO_DATA is set neither arrival nor departure should be supplied.'    
          enum:    
            - SCHEDULED    
            - SKIPPED    
            - NO_DATA    
          type: string    
        stop_id:    
          description: 'Property. Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty.'    
          type: string    
        stop_sequence:    
          description: 'Property. Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for.'    
          type: number    
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
      description: 'The distance between the origin bus stop and the destination bus stop or the total distance travelled corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    travelTime:    
      description: 'The time taken to travel between the origin bus stop and the destination bus stop corresponding to this observation in HH:MM:SS format(HH:MM:SS is also accepted, if the hour begins with 0).'    
      format: time    
      type: string    
      x-ngsi:    
        type: Property    
    trip:    
      description: "Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
      properties:    
        direction_id:    
          description: "Property. Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
          type: number    
        route_id:    
          description: "Property. Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
          type: string    
        schedule_relationship:    
          description: "Property. Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)."    
          type: string    
        start_date:    
          description: "Property. Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
          type: string    
        start_time:    
          description: "Property. Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
          type: string    
        trip_id:    
          description: "Property. Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
    tripDetails:    
      description: 'A descriptor of realtime update on the schedule of a vehicle along a trip.'    
      properties:    
        arrival_time:    
          description: "Property.  Specifies the arrival time at a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'arrival_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)."    
          format: time    
          type: string    
        departure_time:    
          description: "Property. Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)."    
          format: time    
          type: string    
        stop_headsign:    
          description: "Property. This field contains the text that appears on a sign that identifies the trip’s destination to passengers. SameAs: 'stop_headsign' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
          type: string    
        stop_id:    
          description: "Property. Stop ID/Stop name of the bus stops corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
          type: string    
        stop_sequence:    
          description: "Property. Indicates the stop sequence of the vehicle corresponding to this observation, can be referenced from the GTFS static feed stop_times.txt. SameAs: 'stop_sequence' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)."    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    tripDirection:    
      description: 'Gives the direction in which the vehicle is travelling in ENUM[UP,DN]'    
      type: string    
      x-ngsi:    
        type: Property    
    trip_delay:    
      description: "This can be positive and negative in seconds and shows how much the vehicle deviates from the planned one. SameAs: 'delay' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"    
      type: number    
      x-ngsi:    
        type: Property    
    trip_details:    
      description: 'A descriptor of realtime update on the schedule of a vehicle along a trip.'    
      properties:    
        bearing:    
          description: 'Property. Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data'    
          type: number    
        odometer:    
          description: 'Property. Odometer value, in meters. Units:''meters'''    
          type: number    
        speed:    
          description: 'Property. Momentary speed measured by the vehicle, in meters per second. Units:''meters per second'''    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    trip_direction:    
      description: "Gives the direction in which the vehicle is travelling. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor but is represented in the form of an ENUM[UP,DN] in place of [0,1] as seen in 'direction_id' (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
      type: string    
      x-ngsi:    
        type: Property    
    trip_id:    
      description: "Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: string    
      x-ngsi:    
        type: Property    
    trip_update:    
      description: "Describes the trip information like delay, departures, etc., for a trip made by the vehicle corresponding to this observation.SameAs:'trip_update' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)."    
      properties:    
        stop_time_update:    
          description: 'Property. Additional information on the vehicle that is serving this trip.'    
          properties:    
            arrival:    
              description: 'Property. If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty.'    
              properties:    
                uncertainty:    
                  description: "Property. If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)."    
                  type: number    
              type: object    
            departure:    
              description: 'Property. If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty.'    
              properties:    
                uncertainty:    
                  description: "Property. If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)."    
                  type: number    
              type: object    
            schedule_relationship:    
              description: 'Property. Enum:''SCHEDULED, SKIPPED, NO_DATA''. SCHEDULED means that the vehicle is proceeding in accordance with its static schedule of stops, although not necessarily according to the times of the schedule. This is the default behavior. At least one of arrival and departure must be provided. SKIPPED means that The stop is skipped, i.e., the vehicle will not stop at this stop. The arrival and departure fields are optional. NO_DATA means that no data is given for this stop. It indicates that there is no realtime information available. When set NO_DATA is propagated through subsequent stops so this is the recommended way of specifying from which stop you do not have realtime information. When NO_DATA is set neither arrival nor departure should be supplied.'    
              enum:    
                - SCHEDULED    
                - SKIPPED    
                - NO_DATA    
              type: string    
            stop_id:    
              description: 'Property. Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty.'    
              type: string    
            stop_sequence:    
              description: 'Property. Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for.'    
              type: number    
          type: object    
        timestamp:    
          description: "Property. Last reported time of observation from the vehicle. SameAs: 'timestamp' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)."    
          format: date-time    
          type: string    
        trip:    
          description: "Property. Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)."    
          properties:    
            direction_id:    
              description: "Property. Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: number    
            route_id:    
              description: "Property. Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
            schedule_relationship:    
              description: "Property. Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)."    
              type: string    
            start_date:    
              description: "Property. Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
            start_time:    
              description: "Property. Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
            trip_id:    
              description: "Property. Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
          type: object    
        vehicleDesc:    
          description: "Property. Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)."    
          properties:    
            license_plate:    
              description: "Property. Gives the License Plate number of the vehice.SameAs: 'license_plate' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
            vehicle_id:    
              description: "Property. Unique ID assigned to the vehicle corresponding to this observation,used in internal system identification.SameAs: 'id' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
            vehicle_label:    
              description: "Property. User visible label,i.e.,something that must be shown to the passenger to help identify the correct vehicle.SameAs: 'label' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
          type: object    
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be TransitManagement'    
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
          description: "Property. Gives the License Plate number of the vehice.SameAs: 'license_plate' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
          type: string    
        vehicle_id:    
          description: "Property. Unique ID assigned to the vehicle corresponding to this observation,used in internal system identification.SameAs: 'id' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
          type: string    
        vehicle_label:    
          description: "Property. User visible label,i.e.,something that must be shown to the passenger to help identify the correct vehicle.SameAs: 'label' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
    vehicleType:    
      description: 'Describes the type of vehicle corresponding to this observation, could be hopper, compactor, tipper, dumper in case of solid waste management vehicles, BRT mini bus, BRT bus, city bus in case of ITMS vehicles, Ambulance, Fire tender, Police van etc, in case of emergency vehicles and Moped/Scooter, Motor Cycle,  Autorickshaw, Private car/ Jeep car, Tempo, Bus, E-Moped/E-Scooter/E-Motor Cycle, Public motor in case of vehicle registration.'    
      enum:    
        - agriculturalVehicle    
        - ambulance    
        - anyVehicle    
        - articulatedVehicle    
        - autorickshaw    
        - bicycle    
        - binTrolley    
        - 'BRT mini bus·'    
        - 'BRT bus'    
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
          description: "Property. Describes the status of the vehicle w.r.t the stop corresponding to this observation ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. SameAs:'current_status' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)."    
          type: string    
        current_stop_sequence:    
          description: "Property. Gives the stop sequence index of the current stop. This is determined by considering current_status, if current_status is missing IN_TRANSIT_TO is assumed. SameAs:'current_stop_sequence' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)."    
          type: number    
        position:    
          description: "Property. Describes the current position of the vehicle corresponding to this observation. SameAs: 'position' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)."    
          properties: {}    
          type: object    
        stop_id:    
          description: "Property. Stop ID/Stop name of the bus stops corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)."    
          type: string    
        timestamp:    
          description: "Property. Last reported time of observation from the vehicle. SameAs:  'timestamp' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)."    
          format: date-time    
          type: string    
        trip:    
          description: "Property. Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)."    
          properties:    
            direction_id:    
              description: "Property. Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: number    
            route_id:    
              description: "Property. Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
            schedule_relationship:    
              description: "Property. Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)."    
              type: string    
            start_date:    
              description: "Property. Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
            start_time:    
              description: "Property. Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
            trip_id:    
              description: "Property. Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
          type: object    
        vehicleDesc:    
          description: "Property. Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)."    
          properties:    
            license_plate:    
              description: "Property. Gives the License Plate number of the vehice.SameAs: 'license_plate' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
            vehicle_id:    
              description: "Property. Unique ID assigned to the vehicle corresponding to this observation,used in internal system identification.SameAs: 'id' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
            vehicle_label:    
              description: "Property. User visible label,i.e.,something that must be shown to the passenger to help identify the correct vehicle.SameAs: 'label' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
          type: object    
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
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### TransitManagement NGSI-v2关键值示例  
这里有一个以JSON-LD格式作为key-values的TransitManagement的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "https://smart-data-models.github.io/IUDX/TransitManagement/schema.json",  
	"type": "TransitManagement",  
	"vehicleType":"hopper",  
	"trip_delay":11968,  
	"agency_lang":"en",  
	"depot_name":"BHESTAN DEPOT",  
	"travelTime":"22:11:14",  
	"direction_id":0,  
	"schedule_relationship":"SCHEDULED",  
	"vehicle_id":"52TC12",  
	"agency_fare_url":"http://charteredbike.in/surat/?page_id=1021",  
	"actual_trip_end_time":"2021-10-28T08:24:22+05:30",  
	"last_tracked_time":"08:13:22",  
	"standing_capacity":20,  
	"last_stop_arrival_time":"13:30:12",  
	"agency_id":"agency001",  
	"current_status":"INCOMING_AT",  
	"route_type":"1",  
	"speed":28,  
	"route_id":"17AD",  
	"seating_capacity":70,  
	"vehicle_label":"A03",  
	"timestamp":"2021-10-28T08:13:22+05:30",  
	"arrival_time":"22:00:28",  
	"route_long_name":"Baiyappanahalli to Mysuru Road",  
	"agency_timezone":"Asia/Kolkata",  
	"stop_code":"F12",  
	"agency_name":"Chartered Bike Surat",  
	"route_desc":"Phase1-Phase2",  
	"license_plate":"GJ05BX1583",  
	"stop_id":"1016",  
	"uncertainity":0,  
	"route_color":"00FFFF",  
	"travelDistance":9.00174,  
	"actual_trip_start_time":"2021-10-28T07:46:51+05:30",  
	"bearing":90,  
	"stop_sequence":24,  
	"start_date":"2022-03-01",  
	"current_stop_sequence":1001,  
	"start_time":"11:15:35",  
	"trip_id":"23952340",  
	"route_text_color":"FFD700",  
	"ac_available":"yes",  
	"tripDirection":"DN",  
	"agency_url": "http://charteredbike.in/surat/",  
	"routeStopSequence":["10","1001","1002","1003","1004","1005"],  
	"trip_direction":"DN",  
	"departure_time":"22:00:33",  
	"last_stop_id":"4032",  
	"route_short_name":"Purple Line",  
	"stop_name":"DEVASHISH NAGAR MORA BHAGAL",  
	"depot_id":"1",  
	"observationDateTime":"2021-10-28T08:13:22+05:30"  
}  
```  
</details>  
#### TransitManagement NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的TransitManagement的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
    "type": "Boolean",  
    "value": "false"  
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
#### TransitManagement NGSI-LD关键值示例  
这里是一个以JSON-LD格式作为关键值的TransitManagement的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "https://smart-data-models.github.io/IUDX/TransitManagement/schema.json",  
    "@context": [  
        "iudx:TransitManagement",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ],  
    "type": "TransitManagement",  
    "vehicleType": "hopper",  
    "trip_delay": 11968,  
    "agency_lang": "en",  
    "depot_name": "BHESTAN DEPOT",  
    "travelTime": "22:11:14",  
    "direction_id": 0,  
    "schedule_relationship": "SCHEDULED",  
    "vehicle_id": "52TC12",  
    "agency_fare_url": "http://charteredbike.in/surat/?page_id=1021",  
    "actual_trip_end_time": "2021-10-28T08:24:22+05:30",  
    "last_tracked_time": "08:13:22",  
    "standing_capacity": 20,  
    "last_stop_arrival_time": "13:30:12",  
    "agency_id": "agency001",  
    "current_status": "INCOMING_AT",  
    "route_type": "1",  
    "speed": 28,  
    "route_id": "17AD",  
    "seating_capacity": 70,  
    "vehicle_label": "A03",  
    "timestamp": "2021-10-28T08:13:22+05:30",  
    "arrival_time": "22:00:28",  
    "route_long_name": "Baiyappanahalli to Mysuru Road",  
    "agency_timezone": "Asia/Kolkata",  
    "stop_code": "F12",  
    "agency_name": "Chartered Bike Surat",  
    "route_desc": "Phase1-Phase2",  
    "license_plate": "GJ05BX1583",  
    "stop_id": "1016",  
    "uncertainity": 0,  
    "route_color": "00FFFF",  
    "travelDistance": 9.00174,  
    "actual_trip_start_time": "2021-10-28T07:46:51+05:30",  
    "bearing": 90,  
    "stop_sequence": 24,  
    "start_date": "2022-03-01",  
    "current_stop_sequence": 1001,  
    "start_time": "11:15:35",  
    "trip_id": "23952340",  
    "route_text_color": "FFD700",  
    "ac_available": "yes",  
    "tripDirection": "DN",  
    "agency_url": "http://charteredbike.in/surat/",  
    "routeStopSequence": [  
        "10",  
        "1001",  
        "1002",  
        "1003",  
        "1004",  
        "1005"  
    ],  
    "trip_direction": "DN",  
    "departure_time": "22:00:33",  
    "last_stop_id": "4032",  
    "route_short_name": "Purple Line",  
    "stop_name": "DEVASHISH NAGAR MORA BHAGAL",  
    "depot_id": "1",  
    "observationDateTime": "2021-10-28T08:13:22+05:30"  
}  
```  
</details>  
#### TransitManagement NGSI-LD规范化示例  
下面是一个以JSON-LD格式规范化的TransitManagement的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
  "@context": ["https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
