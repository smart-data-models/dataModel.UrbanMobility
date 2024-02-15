<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：运输管理  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/TransitManagement/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**公共交通系统数据模型**  
版本： 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `acAvailable[string]`: 描述与该观察结果相对应的车辆空调选项的存在情况  - `ac_available[string]`: 描述与该观察结果相对应的车辆空调选项的存在情况  - `actual_trip_end_time[date-time]`: 该字段指定与该观察结果相对应的服务或行程的计划结束时间  - `actual_trip_start_time[date-time]`: 该字段指定服务实际开始的时间。  这与：GTFS 实时报文--TripUpdate（https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate）的 stop_time_update （StopTimeUpdate）报文 "到达 "字段中的绝对 "时间"（StopTimeEvent）相同。  - `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 标识公共街道上特定房产的编号    
- `agencyInfo[object]`: 与这一观察结果相对应的机构信息  	- `agency_email[string]`: 由机构客户服务部门主动监控的电子邮件地址。相同：来自 GTFS 静态字段定义 - agency.txt 的 "agency_email "字段 (https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_fare_url[string]`: 包含票价详情的网页的 URL，也可用于在线购买该机构的机票。与此相同：来自 GTFS 静态字段定义 - agency.txt 的 "agency_ffare_url "字段 (https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_id[string]`: 唯一标识转运机构的 ID。一个转运信息源可能代表一个以上机构的数据。agency_id 是数据集唯一标识。对于只包含单个机构数据的转运信息源，此字段是可选的。相同：来自 GTFS 静态字段定义 - agency.txt 的 "agency_id "字段 (https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_lang[string]`: 包含一个双字母 ISO 639-1 代码，表示该交通局使用的主要语言。语言代码不区分大小写（en 和 EN 均可）。相同：来自 GTFS 静态字段定义 - agency.txt 的 "agency_lang "字段 (https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_name[string]`: agency_name 字段包含转运机构的全称。与此相同：来自 GTFS 静态字段定义 - agency.txt 的 "agency_name "字段 (https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_phone[string]`: 指定机构的语音电话号码：来自 GTFS 静态字段定义 - agency.txt 的 "agency_phone "字段 (https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_timezone[string]`: 时区字段包含转运机构所在的时区。与此相同：来自 GTFS 静态字段定义 - agency.txt 的 "agency_timezone "字段 (https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_url[string]`: agency_url 字段包含转运机构的 URL。与此相同：来自 GTFS 静态字段定义 - agency.txt 的 "agency_url "字段 (https://developers.google.com/transit/gtfs/reference#agencytxt)    
- `agency_fare_url[string]`: 包含票价详情的网页的 URL，也可用于在线购买该机构的机票。与此相同：来自 GTFS 静态字段定义 - agency.txt 的 "agency_ffare_url "字段 (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_id[string]`: 唯一标识转运机构的 ID。一个转运信息源可能代表一个以上机构的数据。agency_id 是数据集唯一标识。对于只包含单个机构数据的转运信息源，此字段是可选的。相同：来自 GTFS 静态字段定义 - agency.txt 的 "agency_id "字段 (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_lang[string]`: 包含一个双字母 ISO 639-1 代码，表示该交通局使用的主要语言。语言代码不区分大小写（en 和 EN 均可）。相同：来自 GTFS 静态字段定义 - agency.txt 的 "agency_lang "字段 (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_name[string]`: agency_name 字段包含转运机构的全称。与此相同：来自 GTFS 静态字段定义 - agency.txt 的 "agency_name "字段 (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_timezone[string]`: 时区字段包含转运机构所在的时区。与此相同：来自 GTFS 静态字段定义 - agency.txt 的 "agency_timezone "字段 (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_url[string]`: agency_url 字段包含转运机构的 URL。与此相同：来自 GTFS 静态字段定义 - agency.txt 的 "agency_url "字段 (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrival[object]`: 如果 schedule_relationship 为空或 SCHEDULED，则必须在 StopTimeUpdate 中提供到达或出发信息。与此相同：GTFS 实时报文-StopTimeUpdate 中的 "到达 "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  	- `uncertainty[number]`: 如果省略不确定性，则解释为未知。要指定一个完全确定的预测值，可将其不确定性设为 0.SameAs：GTFS实时报文-StopTimeEvent（https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent）中的 "不确定性 "字段    
- `arrivalUncertainty[number]`: 如果 schedule_relationship 为空或 SCHEDULED，则必须在 StopTimeUpdate 中提供到达或出发信息。与此相同：GTFS 实时报文-StopTimeUpdate 中的 "到达 "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `arrival_time[time]`: 指定路线上特定行程的特定站点的到达时间。时间必须是 HH:MM:SS 格式的八位数（如果小时以 0 开头，也可以接受 HH:MM:SS）。注意： 跨多个日期的行程的停车时间将大于 24:00:00。例如，如果行程开始于晚上 10:30:00，结束于次日凌晨 2:15:00，则停止时间为 22:30:00 和 26:15:00。将这些停止时间输入 22:30:00 和 02:15:00，不会产生所需的结果。相同：来自 GTFS 静态字段定义-stop_times.txt 的'arrival_time'字段 (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `bearing[number]`: 提供从真北方向顺时针方向测量的车辆 GPS 角度。与 GTFS 实时信息位置（https://developers.google.com/transit/gtfs-realtime/reference#message-position）中的 "方位 "字段相同。  - `current_status[string]`: 描述与该观测点相对应的停靠站的车辆状态 ENUM：[INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]。与 GTFS 实时信息--车辆位置（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition）中的 "current_status "字段相同。  - `current_stop_sequence[number]`: 给出当前停站的停站序列索引。这是通过考虑 current_status 确定的，如果缺少 current_status，则假定为 IN_TRANSIT_TO。与 GTFS 实时信息-车辆位置（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition）中的'current_stop_sequence'字段相同。  - `dataDescriptor[uri]`: 指向数据描述符实体的 URI  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `departure[object]`: 如果 schedule_relationship 为空或 SCHEDULED，则必须在 StopTimeUpdate 中提供到达或出发信息。与此相同：来自 GTFS 实时报文-StopTimeUpdate 的 "出发 "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  	- `uncertainty[number]`: 如果省略不确定性，则解释为未知。要指定一个完全确定的预测值，可将其不确定性设为 0.SameAs：GTFS实时报文-StopTimeEvent（https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent）中的 "不确定性 "字段    
- `departureUncertainty[number]`: 如果 schedule_relationship 为空或 SCHEDULED，则必须在 StopTimeUpdate 中提供到达或出发信息。与此相同：来自 GTFS 实时报文-StopTimeUpdate 的 "出发 "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `departure_time[time]`: 指定路线上特定行程从特定站点出发的时间。时间必须是 HH:MM:SS 格式的八位数（如果小时以 0 开头，也可以接受 HH:MM:SS）。  
注意： 跨多个日期的行程的停车时间将大于 24:00:00。例如，如果行程开始于晚上 10:30:00，结束于次日凌晨 2:15:00，则停止时间为 22:30:00 和 26:15:00。将这些停止时间输入 22:30:00 和 02:15:00，不会产生所需的结果。相同：来自 GTFS 静态字段定义-stop_times.txt 的 "departure_time "字段 (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `depotID[string]`: 描述与该观测值相对应的汽车站的唯一 ID  - `depotName[string]`: 描述与该观测值相对应的汽车站名称  - `depot_id[string]`: 描述与该观测值相对应的公交车站的唯一 ID  - `depot_name[string]`: 描述与该观测值相对应的汽车站名称  - `description[string]`: 项目描述  - `deviceInfo[object]`: 与观测结果相关的设备信息  . Model: [https://schema.org/Text](https://schema.org/Text)	- `deviceBatteryStatus[string]`: 显示报告设备的电池充电状态（连接、断开）  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceID[string]`: 与该观测值相对应的物理传感器/测量站的设备 ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceModel[object]`: 描述有关设备、传感器或系统的信息  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceName[string]`: 该观测点对应的传感设备/站的设备名称或站名  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceSimNumber[string]`: 提供废物管理车上设备的模拟号码  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `measurand[string]`: 设备感知/观测/测量的属性  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `rfID[string]`: 提供 RFID 阅读器的 ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `direction_id[number]`: 表示该观测点对应的车辆行驶方向，可从 GTFS 静态馈送 trips.txt 中引用。与此相同：GTFS 实时信息--tripDescriptor（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）中的 "direction_id "字段。  - `entity_id[string]`: 该观测值对应的实体的唯一馈送 ID。SameAs:'entity_id'字段来自 GTFS 实时消息-馈送实体(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  - `id[*]`: 实体的唯一标识符  - `last_stop_arrival_time[time]`: 指定路线上特定行程的前一站到达时间。时间必须是 HH:MM:SS 格式的八位数（如果小时以 0 开头，也可使用 H:MM:SS）。注意： 跨多个日期的行程的停车时间将大于 24:00:00。例如，如果行程开始于晚上 10:30:00，结束于次日凌晨 2:15:00，则停止时间为 22:30:00 和 26:15:00。如果将这些停止时间输入为 22:30:00 和 02:15:00，就不会产生所需的结果。这与：GTFS 实时报文--TripUpdate（https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate）的 stop_time_update (StopTimeUpdate) 报文 "到达 "字段中的绝对 "时间"（StopTimeEvent）相同。  - `last_stop_id[string]`: 与本次观测中的巴士相对应的上一个巴士站的站点 ID/站点名称。与此相同：GTFS 实时信息-车辆位置中的 "stop_id "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `last_tracked_time[date-time]`: 提供最后一次追踪车辆的时间  - `license_plate[string]`: 提供车辆的车牌号码。与此相同：GTFS 实时信息-车辆描述符中的 "license_plate "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `observationDateTime[date-time]`: 最后报告的观察时间  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `position[object]`: 描述与该观测数据相对应的车辆当前位置。同：GTFS 实时信息-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)中的位置字段。  . Model: [https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition](https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)	- `bearing[number]`: 方位，单位为度，从真北开始顺时针方向，即 0 为北，90 为东。这可以是指南针方位，也可以是下一站或中间位置的方向。这不应该从之前的位置序列中推导出来，客户可以从之前的数据中计算出来    
	- `latitude[number]`: WGS-84 坐标系中的北纬度数    
	- `longitude[number]`: 在 WGS-84 坐标系中为东度    
	- `odometer[number]`: 里程表数值，以米为单位    
	- `speed[number]`: 车辆测得的瞬时速度，单位为米/秒    
- `positionInfo[object]`: 描述与该观测数据相对应的车辆当前位置。与 GTFS 实时信息-车辆位置（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition）中的 "位置 "字段相同  	- `bearing[number]`: 方位，单位为度，从真北开始顺时针方向，即 0 为北，90 为东。这可以是指南针方位，也可以是下一站或中间位置的方向。这不应该从之前的位置序列中推导出来，客户可以从之前的数据中计算出来    
	- `odometer[number]`: 里程表值    
	- `speed[number]`: 车辆测量的瞬时速度    
- `routeInfo[object]`: 与该观测值相对应的车辆行程的最新排序停车顺序，如果 schedule_relationship 为 "CANCELED"，则不考虑该顺序。与此相同：GTFS 实时报文-TripUpdate（https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate）中的 "stop_time_update "字段。  	- `route_color[string]`: 如果指定了该字段，则该字段定义了与路由相对应的颜色。颜色必须是六位十六进制数，例如 00FFFFF。如果未指定颜色，默认路由颜色为白色（FFFFFF）。相同：GTFS 静态字段定义-routes.txt 中的 "route_color "字段 (https://developers.google.com/transit/gtfs/reference#routestxt)    
	- `route_desc[string]`: 路线描述。这可以包括以文字描述形式提供的整个路线详情，包括往返目的地和时间信息。与此相同：GTFS 静态字段定义-routes.txt 中的 "route_desc "字段 (https://developers.google.com/transit/gtfs/reference#routestxt)    
	- `route_id[string]`: 与本观测信息中的巴士相对应的巴士/车辆目前正在行驶的路线所分配的路线编号    
	- `route_long_name[string]`: 路线的全称。该名称比路线短名更具描述性，通常包括路线的目的地或停靠站。这主要包括路线的出发地和目的地名称。相同：来自 GTFS 静态字段定义-routes.txt 的 "route_long_name "字段 (https://developers.google.com/transit/gtfs/reference#routestxt)    
	- `route_short_name[string]`: 线路的简称。这通常是公交车辆的车牌号，如 402D，或乘客用来识别路线的绿色车牌号。与此相同：来自 GTFS 静态字段定义-routes.txt 的 "route_short_name "字段 (https://developers.google.com/transit/gtfs/reference#routestxt)    
	- `route_text_color[string]`: 此字段可用于指定在 route_color 背景下绘制的文本的可读颜色。颜色必须是六位十六进制数，例如 FFD700。如果没有指定颜色，则默认文本颜色为黑色（000000）。相同：GTFS 静态字段定义-routes.txt 中的 "route_text_color "字段 (https://developers.google.com/transit/gtfs/reference#routestxt)    
	- `route_type[number]`: 表示交通类型的数字-- 1 - 地铁、地铁。大都会区内的任何地下轨道系统。2 - 铁路。用于城际或长途旅行。3 - 公共汽车。用于短途和长途公共汽车线路。相同：来自 GTFS 静态字段定义-routes.txt 的 "route_type "字段 (https://developers.google.com/transit/gtfs/reference#routestxt)    
	- `route_url[string]`: 包含有关该航线的网页 URL，与 agency_url 不同。与此相同：来自 GTFS 静态字段定义-routes.txt 的 "route_url "字段 (https://developers.google.com/transit/gtfs/reference#routestxt)    
- `routeStopSequence[array]`: 按正确顺序给出与该观测结果相对应的路线、线路或车次的停靠站标识/停靠站代码或车站标识/车站代码  - `route_color[string]`: 如果指定了该字段，则该字段定义了与路由相对应的颜色。颜色必须是六位十六进制数，例如 00FFFFF。如果未指定颜色，默认路由颜色为白色（FFFFFF）。相同：GTFS 静态字段定义-routes.txt 中的 "route_color "字段 (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_desc[string]`: 路线描述。这可以包括以文字描述形式提供的整个路线详情，包括往返目的地和时间信息。与此相同：GTFS 静态字段定义-routes.txt 中的 "route_desc "字段 (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_id[string]`: 分配给与本观察结果中的巴士相对应的巴士/车辆当前正在行驶的路线的路线 ID。与此相同：GTFS 实时信息-行程描述符中的 "route_id "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `route_long_name[string]`: 路线的全称。该名称比路线短名更具描述性，通常包括路线的目的地或停靠站。这主要包括路线的出发地和目的地名称。相同：来自 GTFS 静态字段定义-routes.txt 的 "route_long_name "字段 (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_short_name[string]`: 线路的简称。这通常是公交车辆的车牌号，如 "402D "或 "Green"，乘客用它来识别路线。相同：来自 GTFS 静态字段定义-routes.txt 的 "route_short_name "字段 (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_text_color[string]`: 此字段可用于指定在 route_color 背景下绘制的文本的可读颜色。颜色必须是六位十六进制数，例如 FFD700。如果没有指定颜色，则默认文本颜色为黑色（000000）。相同：GTFS 静态字段定义-routes.txt 中的 "route_text_color "字段 (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_type[string]`: 表示交通类型的编号-1 - 地铁、地铁。大都市地区内的任何地下铁路系统。用于城际或长途旅行。用于短途和长途公共汽车线路。相同：来自 GTFS 静态字段定义-routes.txt 的 "route_type "字段 (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_url[string]`: 包含有关该航线的网页 URL，与 agency_url 不同。与此相同：来自 GTFS 静态字段定义-routes.txt 的 "route_url "字段 (https://developers.google.com/transit/gtfs/reference#routestxt)  - `schedule_relationship[string]`: 说明路线/行程是否已排定。相同：来自 enumScheduleRelationship 的'schedule_relationship'字段 (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)  - `seating_capacity[number]`: 描述与该观察结果相对应的车辆乘客座位数  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `shapeInfo[object]`: 该观测点对应的车辆行驶路径信息  	- `shape_dist_traveled[number]`: 从第一个形状点到本记录中指定的点沿形状实际移动的距离。由行程规划人员使用，在地图上显示形状的正确部分。数值必须随 shape_pt_sequence 的增加而增加；不能用于显示沿路线的反向行程。距离单位必须与 stop_times.txt 中使用的单位一致。举例说明：如果一辆公共汽车沿着上面为 A_shp 定义的三个点行驶，附加的 shape_dist_traveled 值（此处以公里为单位显示）将如下所示：shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled A_shp,37.61956,-122.48161,0,0 A_shp,37.64430,-122.41070,6,6.8310 A_shp,37.65863,-122.30839,11,15.8765    
	- `shape_id[string]`: 识别形状    
	- `shape_pt_sequence[number]`: 形状点连接形成形状的顺序。数值必须沿行程增加，但不必连续。举例说明：如果形状 "A_shp "的定义中有三个点，shapes.txt 文件可能包含以下记录来定义形状： shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence A_shp,37.61956,-122.48161,0 A_shp,37.64430,-122.41070,6 A_shp,37.65863,-122.30839,11    
- `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `speed[number]`: 给出车辆的速度。与 GTFS 实时信息位置（https://developers.google.com/transit/gtfs-realtime/reference#message-position）中的 "速度 "字段相同。  - `standingCapacity[number]`: 描述与该观测值相对应的车辆乘客站立能力。  - `standing_capacity[number]`: 描述与该观测值相对应的车辆乘客站立能力  - `start_date[string]`: 描述与本次观测车辆相对应的行程的初始预定日期。该字段的格式示例 - YYYYMMDD。与此相同：GTFS 实时信息--行程描述符（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）中的 "start_date "字段。  - `start_time[time]`: 描述与本次观测车辆相对应的行程的初始计划开始时间。该字段的格式示例 - 11:15:35 或 25:15:35。与 GTFS 实时信息中的'start_time'字段相同：GTFS 实时信息--行程描述符（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）中的 "start_time "字段。  - `stopInfo[object]`: 该观测点对应的车辆行驶路径信息  	- `stop_code[string]`: 该字段包含简短的文字或数字，用于向乘客唯一标识该站。如果是公共站，可与 stop_id 相同。相同：来自 GTFS 静态字段定义-stop.txt 的 "stop_code "字段 (https://developers.google.com/transit/gtfs/reference#stopstxt)    
	- `stop_desc[string]`: 该字段包含对停靠站的描述。与此相同：来自 GTFS 静态字段定义-stop.txt 的 "stop_desc "字段 (https://developers.google.com/transit/gtfs/reference#stopstxt)    
	- `stop_id[string]`: 分配给该观测站的唯一 ID    
	- `stop_name[string]`: 描述停靠站或车站的名称。与此相同：来自 GTFS 静态字段定义-stop.txt 的 "stop_name "字段 (https://developers.google.com/transit/gtfs/reference#stopstxt)    
	- `stop_url[string]`: 该字段包含有关特定站点的网页 URL，与 agency_url 和 route_url 字段不同。相同：来自 GTFS 静态字段定义-stop.txt 的 "stop_url "字段 (https://developers.google.com/transit/gtfs/reference#stopstxt)    
- `stopTimeUpdateInfo[object]`: 与该观测值相对应的车辆行程的最新排序停车顺序，如果 schedule_relationship 为 "CANCELED"，则不考虑该顺序。与此相同：GTFS 实时报文-TripUpdate（https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate）中的 "stop_time_update "字段。  	- `stopScheduleRelationship[string]`: 描述静态时刻表与停靠站之间的关系。与此相同：来自 GTFS 实时报文-StopTimeUpdate ENUM[SCHEDULED, SKIPPED, NO_DATA] 的'schedule_relationship'字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)    
	- `stop_id[string]`: 分配给该观测站的唯一 ID    
	- `stop_sequence[number]`: 该字段可确定特定行程的停车顺序。stop_sequence 的值必须是非负整数，且必须沿行程递增。例如，行程的第一个站点的 stop_sequence 可以是 1，行程的第二个站点的 stop_sequence 可以是 23，行程的第三个站点的 stop_sequence 可以是 40，依此类推。    
- `stopTimesInfo[object]`: 实时更新沿途车辆时刻表的描述符  	- `arrival_time[time]`: 指定路线上特定行程的特定站点的到达时间。时间必须是 HH:MM:SS 格式的八位数（如果小时以 0 开头，也可以接受 HH:MM:SS）。注意： 跨多个日期的行程的停车时间将大于 24:00:00。例如，如果行程开始于晚上 10:30:00，结束于次日凌晨 2:15:00，则停止时间为 22:30:00 和 26:15:00。将这些停止时间输入 22:30:00 和 02:15:00，不会产生所需的结果。相同：来自 GTFS 静态字段定义-stop_times.txt 的'arrival_time'字段 (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `continuous_drop_off[number]`: 表示乘客是否可以在车辆行驶路径上的任何地点下车：来自 GTFS 静态字段定义-stop_times.txt 的 "continuous_drop_off "字段 (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `continuous_pickup[number]`: 表示乘客是否可以在车辆行驶路径上的任何地点上车：来自 GTFS 静态字段定义-stop_times.txt 的 "continuous_pickup "字段 (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `departure_time[time]`: 指定路线上特定行程从特定站点出发的时间。时间必须是 HH:MM:SS 格式的八位数（如果小时以 0 开头，也可以接受 HH:MM:SS）。注意： 跨多个日期的行程的停车时间将大于 24:00:00。例如，如果行程开始于晚上 10:30:00，结束于次日凌晨 2:15:00，则停止时间为 22:30:00 和 26:15:00。将这些停止时间输入 22:30:00 和 02:15:00，不会产生所需的结果。相同：来自 GTFS 静态字段定义-stop_times.txt 的 "departure_time "字段 (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `drop_off_type[string]`: 表示投放方式。与此相同：来自 GTFS 静态字段定义-stop_times.txt 的 "drop_off_type "字段 (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `pickup_type[string]`: 表示拾取方式：来自 GTFS 静态字段定义-stop_times.txt 的 "pickup_type "字段 (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `stop_headsign[string]`: 此字段包含向乘客标明行程目的地的标志上的文字。与此相同：来自 GTFS 静态字段定义-stop_times.txt 的 "stop_headsign "字段 (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `stop_id[string]`: 分配给该观测站的唯一 ID    
	- `stop_sequence[number]`: 该字段可确定特定行程的停车顺序。stop_sequence 的值必须是非负整数，且必须沿行程递增。例如，行程的第一个站点的 stop_sequence 可以是 1，行程的第二个站点的 stop_sequence 可以是 23，行程的第三个站点的 stop_sequence 可以是 40，依此类推。    
	- `trip_id[string]`: 考虑到一天中的时间和给定路线 ID 上的行程方向，分配给与该观察结果相对应的公共汽车的行程 ID/行程名称    
- `stop_code[string]`: 该字段包含简短的文字或数字，用于向乘客唯一标识该站。如果是公共站，可与 stop_id 相同。相同：来自 GTFS 静态字段定义-stop.txt 的 "stop_code "字段 (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_desc[string]`: 该字段包含对停靠站的描述。与此相同：来自 GTFS 静态字段定义-stop.txt 的 "stop_desc "字段 (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_headsign[string]`: 此字段包含向乘客标明行程目的地的标志上的文字。与此相同：来自 GTFS 静态字段定义-stop_times.txt 的 "stop_headsign "字段 (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `stop_id[string]`: 与本次观测中的巴士相对应的巴士站 ID/站名。与此相同：GTFS 实时信息-车辆位置中的 "stop_id "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `stop_name[string]`: 描述巴士站的名称。与此相同：GTFS 静态字段定义-stop.txt 中的 "stop_name "字段 (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_sequence[number]`: 表示该观测点对应的车辆停止序列，可从 GTFS 静态馈送 stop_times.txt 中引用。与此相同：来自 GTFS 实时信息-StopTimeUpdate 的 "stop_sequence "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `stop_sequence_detail[object]`: 描述公交车辆在指定路线上的行程停靠顺序：来自 GTFS 静态字段定义-stop_times.txt 的 "stop_sequence "字段 (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  	- `stop_id[string]`: 必须与相应 GTFS feed 中 stops.txt 中的内容相同。StopTimeUpdate 中必须提供 stop_sequence 或 stop_id，两个字段都不能为空。    
	- `stop_sequence[number]`: 必须与相应 GTFS feed 中 stop_times.txt 中的内容相同。在 StopTimeUpdate 中必须提供 stop_sequence 或 stop_id，两个字段都不能为空。对于多次访问同一 stop_id 的行程（如循环），需要提供 stop_sequence，以明确预测的是哪一站。    
- `stop_time_update[object]`: 关于本次行程服务车辆的其他信息  	- `arrival[object]`: 如果 schedule_relationship 为空或 SCHEDULED，则必须在 StopTimeUpdate 中提供到达或出发信息 - 两个字段都不能为空。如果 schedule_relationship 为 NO_DATA，则到达和出发必须为空。    
	- `departure[object]`: 如果 schedule_relationship 为空或 SCHEDULED，则必须在 StopTimeUpdate 中提供到达或出发信息 - 两个字段都不能为空。如果 schedule_relationship 为 NO_DATA，则到达和出发必须为空。    
	- `schedule_relationship[string]`: 枚举：'SCHEDULED（已执行）, SKIPPED（跳过）, NO_DATA（无数据）'。SCHEDULED（已安排）表示车辆按照其静态停车时间表行驶，但不一定按照时间表的时间行驶。这是默认行为。必须提供至少一个到达和出发时间。SKIPPED 表示跳过该站，即车辆不会在该站停车。到达和出发字段为可选项。NO_DATA（无数据）表示未提供此站点的数据。表示没有可用的实时信息。设置 NO_DATA 后，数据将在后续站点传播，因此建议使用这种方式来指定没有实时信息的站点。设置 NO_DATA 时，不应提供到达或出发信息。    
	- `stop_id[string]`: 必须与相应 GTFS feed 中 stops.txt 中的内容相同。StopTimeUpdate 中必须提供 stop_sequence 或 stop_id，两个字段都不能为空。    
	- `stop_sequence[number]`: 必须与相应 GTFS feed 中 stop_times.txt 中的内容相同。在 StopTimeUpdate 中必须提供 stop_sequence 或 stop_id，两个字段都不能为空。对于多次访问同一 stop_id 的行程（如循环），需要提供 stop_sequence，以明确预测的是哪一站。    
- `stop_url[string]`: 该字段包含有关特定站点的网页 URL，与 agency_url 和 route_url 字段不同。相同：来自 GTFS 静态字段定义-stop.txt 的 "stop_url "字段 (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `timestamp[date-time]`: 最后报告的从车辆观察到的时间。与此相同：GTFS 实时信息-车辆位置中的 "时间戳 "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `travelDistance[number]`: 始发站和终点站之间的距离，或与该观测结果相对应的总行程距离  - `travelTime[time]`: 该观测点对应的起始地点和目的地之间的旅行时间，格式为 HH:MM:SS（如果小时以 0 开头，也可接受 HH:MM:SS）  - `trip[object]`: 描述该观测点对应的车辆正在进行的行程。SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `direction_id[number]`: 表示该观测点对应的车辆行驶方向，可从 GTFS 静态馈送 trips.txt 中引用。与此相同：GTFS 实时信息--tripDescriptor（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）中的 "direction_id "字段。    
	- `route_id[string]`: 分配给与本观察结果中的巴士相对应的巴士/车辆当前正在行驶的路线的路线 ID。与此相同：GTFS 实时信息-行程描述符中的 "route_id "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
	- `schedule_relationship[string]`: 说明路线/行程是否已排定。相同：来自 enumScheduleRelationship 的'schedule_relationship'字段 (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)    
	- `start_date[string]`: 描述与本次观测车辆相对应的行程的初始预定日期。该字段的格式示例 - YYYYMMDD。与此相同：GTFS 实时信息--行程描述符（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）中的 "start_date "字段。    
	- `start_time[string]`: 描述与本次观测车辆相对应的行程的初始计划开始时间。该字段的格式示例 - 11:15:35 或 25:15:35。与 GTFS 实时信息中的'start_time'字段相同：GTFS 实时信息--行程描述符（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）中的 "start_time "字段。    
	- `trip_id[string]`: 考虑到一天中的时间和给定路线 ID 上的行程方向，分配给与此观察结果相对应的公交车的行程 ID/行程名称。与此相同：GTFS 实时信息--tripDescriptor（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）中的 "trip_id "字段。    
- `tripDetails[object]`: 实时更新沿途车辆时刻表的描述符  	- `arrival_time[time]`: 指定路线上特定行程的特定站点的到达时间。时间必须是 HH:MM:SS 格式的八位数（如果小时以 0 开头，也可以接受 HH:MM:SS）。注意： 跨多个日期的行程的停车时间将大于 24:00:00。例如，如果行程开始于晚上 10:30:00，结束于次日凌晨 2:15:00，则停止时间为 22:30:00 和 26:15:00。将这些停止时间输入 22:30:00 和 02:15:00，不会产生所需的结果。相同：来自 GTFS 静态字段定义-stop_times.txt 的'arrival_time'字段 (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `departure_time[time]`: 指定路线上特定行程从特定站点出发的时间。时间必须是 HH:MM:SS 格式的八位数（如果小时以 0 开头，也可以接受 HH:MM:SS）。注意： 跨多个日期的行程的停车时间将大于 24:00:00。例如，如果行程开始于晚上 10:30:00，结束于次日凌晨 2:15:00，则停止时间为 22:30:00 和 26:15:00。将这些停止时间输入 22:30:00 和 02:15:00，不会产生所需的结果。相同：来自 GTFS 静态字段定义-stop_times.txt 的 "departure_time "字段 (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `stop_headsign[string]`: 此字段包含向乘客标明行程目的地的标志上的文字。与此相同：来自 GTFS 静态字段定义-stop_times.txt 的 "stop_headsign "字段 (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `stop_id[string]`: 与本次观测中的巴士相对应的巴士站 ID/站名。与此相同：GTFS 实时信息-车辆位置中的 "stop_id "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
	- `stop_sequence[number]`: 表示该观测点对应的车辆停止序列，可从 GTFS 静态馈送 stop_times.txt 中引用。与此相同：来自 GTFS 实时信息-StopTimeUpdate 的 "stop_sequence "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)    
- `tripDirection[string]`: 给出车辆行驶的 ENUM[UP,DN] 方向  - `tripInfo[object]`: 描述该观测点对应的车辆正在进行的行程。与 GTFS 实时信息-车辆位置（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition）中的 "trip "字段相同。  	- `route_id[string]`: 与本观测信息中的巴士相对应的巴士/车辆目前正在行驶的路线所分配的路线编号    
	- `schedule_relationship[string]`: 说明路线/行程是否已排定。与此相同：GTFS 实时消息-行程描述符 ENUM[SCHEDULED, ADDED, UNSCHEDULED, CANCELED] 中的'schedule_relationship'字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
	- `start_date[string]`: 描述与本次观测车辆相对应的行程的初始预定日期。该字段的格式示例 - YYYYMMDD。与此相同：GTFS 实时信息--行程描述符（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）中的 "start_date "字段。    
	- `start_time[time]`: 描述与本次观测车辆相对应的行程的初始计划开始时间。该字段的格式示例 - 11:15:35 或 25:15:35。与 GTFS 实时信息中的'start_time'字段相同：GTFS 实时信息--行程描述符（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）中的 "start_time "字段。    
	- `trip_direction[string]`: 表示该观测点对应的车辆行驶方向，可从 GTFS 静态馈送 trips.txt 中引用。与此相同：GTFS 实时信息--tripDescriptor（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）中的 "direction_id "字段。    
	- `trip_id[string]`: 考虑到一天中的时间和给定路线 ID 上的行程方向，分配给与该观察结果相对应的公共汽车的行程 ID/行程名称    
- `trip_delay[number]`: 以秒为单位，可以是正数，也可以是负数，显示车辆与计划偏离的程度。与此相同：来自 GTFS 实时信息-StopTimeEvent 的 "延迟 "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)  - `trip_details[object]`: 实时更新沿途车辆时刻表的描述符  	- `bearing[number]`: 方位，单位为度，从真北开始顺时针方向，即 0 为北，90 为东。这可以是指南针方位，也可以是下一站或中间位置的方向。这不应该从之前的位置序列中推导出来，客户可以从之前的数据中计算出来    
	- `odometer[number]`: 里程表数值，以米为单位    
	- `speed[number]`: 车辆测得的瞬时速度，单位为米/秒    
- `trip_direction[string]`: 提供车辆行驶的方向。与 GTFS 实时报文-行程描述符中的'direction_id'字段相同：与 GTFS 实时信息--TripDescriptor 中的 "direction_id "字段相同，但以 ENUM[UP,DN] 代替 "direction_id"（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）中的 [0,1]。  - `trip_id[string]`: 考虑到一天中的时间和给定路线 ID 上的行程方向，分配给与此观察结果相对应的公交车的行程 ID/行程名称。与此相同：GTFS 实时信息--tripDescriptor（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）中的 "trip_id "字段。  - `trip_update[object]`: 描述与该观测信息相对应的车辆所执行的行程信息，如延误、出发等。与 GTFS 实时信息-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)中的 "trip_update "字段相同。  	- `stop_time_update[object]`: 关于本次行程服务车辆的其他信息    
	- `timestamp[date-time]`: 最后报告的从车辆观察到的时间。与此相同：GTFS 实时信息-车辆位置中的 "时间戳 "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
	- `trip[object]`: 描述该观测点对应的车辆正在进行的行程。SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)    
	- `vehicleDesc[object]`: 描述与该观测信息相对应的车辆附加信息。SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)    
- `type[string]`: NGSI 实体类型。必须是 TransitManagement  - `uncertainty[number]`: 如果省略不确定性，则解释为未知。要指定一个完全确定的预测值，可将其不确定性设为 0.SameAs：GTFS实时报文-StopTimeEvent（https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent）中的 "不确定性 "字段  - `vehicleDesc[object]`: 描述与该观测信息相对应的车辆附加信息。SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `license_plate[string]`: 提供车辆的车牌号码：与 GTFS 实时信息 - VehicleDescriptor（https：//developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor）中的 "license_plate "字段相同。    
	- `vehicle_id[string]`: 分配给与此观察结果相对应的车辆的唯一 ID，用于内部系统识别：来自 GTFS 实时信息 - VehicleDescriptor 的 "id "字段（https：//developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor）    
	- `vehicle_label[string]`: 用户可见标签，即必须向乘客显示以帮助识别正确车辆的内容：来自 GTFS 实时信息 - VehicleDescriptor 的 "label "字段（https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor）    
- `vehicleInfo[object]`: 描述与该观测信息相对应的车辆附加信息。SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `license_plate[string]`: 提供车辆的车牌号码。与此相同：GTFS 实时信息-车辆描述符中的 "license_plate "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)    
	- `vehicleID[string]`: 分配给该观测值对应的车辆的唯一 ID，用于内部系统识别。与此相同：来自 GTFS 实时信息-车辆描述符（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor）的 "id "字段。    
	- `vehicle_label[string]`: 用户可见标签，即必须向乘客出示以帮助识别正确车辆的东西。与此相同：GTFS 实时信息-车辆描述符中的 "label "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)    
- `vehiclePositionInfo[object]`: 描述与该观测数据相对应的车辆的实时位置。SameAs:'vehicle' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  	- `actual_trip_start_time[date-time]`: 该字段指定服务实际开始的时间。这与：GTFS 实时报文--TripUpdate（https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate）的 stop_time_update (StopTimeUpdate) 报文 "到达 "字段中的绝对 "时间"（StopTimeEvent）相同。    
	- `agencyInfo[object]`: 与这一观察结果相对应的机构信息。    
	- `arrivalUncertainty[number]`: 如果 schedule_relationship 为空或 SCHEDULED，则必须在 StopTimeUpdate 中提供到达或出发信息。与此相同：GTFS实时报文-StopTimeUpdate（https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate）中的 "到达 "字段。    
	- `congestion_level[string]`: 描述影响该车辆的拥堵级别。枚举 [unknown_congestion_level, running_smoothly, stop_and_go, congestion, severe_congestion] （未知拥堵级别，平稳运行，走走停停，拥堵，严重拥堵    
	- `current_status[string]`: 描述与该观测点相对应的停靠站的车辆状态 ENUM：[INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]。与 GTFS 实时信息--车辆位置（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition）中的 "current_status "字段相同。    
	- `current_stop_sequence[number]`: 给出当前停站的停站序列索引。这是通过考虑 current_status 确定的，如果缺少 current_status，则假定为 IN_TRANSIT_TO。与 GTFS 实时报文-VehiclePosition（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition）中的'current_stop_sequence'字段相同。    
	- `departureUncertainty[number]`: 如果 schedule_relationship 为空或 SCHEDULED，则必须在 StopTimeUpdate 中提供到达或出发信息。与此相同：GTFS实时报文-StopTimeUpdate（https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate）中的 "出发 "字段。    
	- `depotID[string]`: 描述与该观测值相对应的公交车站的唯一 ID。    
	- `depotName[string]`: 描述与该观测值相对应的汽车站名称。    
	- `entity_id[string]`: 该观测值对应的实体的唯一馈送 ID。SameAs:'entity_id'字段来自 GTFS 实时消息-馈送实体(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)    
	- `occupancy_status[string]`: 车辆的乘客占用率。枚举 [empty, many_seats_available, few_seats_available, standing_room_only, crushed_standing_room_only, full, not_accepting_passengers, no_data_available, not_boardable] （空座位、多座位、少座位、仅有站立空间、仅有挤压站立空间、满座、不接受乘客、无数据、不可登机）。    
	- `positionInfo[object]`: 描述与该观测数据相对应的车辆当前位置。与 GTFS 实时信息-车辆位置（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition）中的 "位置 "字段相同。    
	- `route_id[string]`: 分配给与本观察结果中的巴士相对应的巴士/车辆当前正在行驶的路线的路线 ID。与此相同：GTFS 实时信息-行程描述符（https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor）中的 "route_id "字段。    
	- `stopInfo[object]`: 该观测点对应的车辆行驶路径信息。    
	- `stopTimesInfo[object]`: 实时更新车辆行程计划的描述符。    
	- `stop_id[string]`: 分配给该观测站的唯一 ID    
	- `travelDistance[number]`: 起始地点与目的地之间的距离，或与该观测值相对应的总行程距离。    
	- `tripInfo[object]`: 描述该观测点对应的车辆正在进行的行程。与 GTFS 实时信息-车辆位置（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition）中的 "trip "字段相同。    
	- `vehicleInfo[object]`: 描述与该观测信息相对应的车辆附加信息。SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)    
- `vehicleType[string]`: 描述与该观察结果相对应的车辆类型，如果是固体废物管理车辆，可以是料斗、压实机、自卸车、翻斗车；如果是 ITMS 车辆，可以是 BRT 小巴士、BRT 巴士、城市巴士；如果是应急车辆，可以是救护车、消防车、警车等；如果是车辆登记，可以是轻便摩托车/踏板车、摩托车、自动人力车、私家车/吉普车、Tempo、巴士、E-Moped/E-Scooter/E-Motor Cycle、公共汽车。  - `vehicle_id[string]`: 分配给该观测值对应的车辆的唯一 ID，用于内部系统识别。与此相同：来自 GTFS 实时信息-车辆描述符（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor）的 "id "字段。  - `vehicle_label[string]`: 用户可见标签，即必须向乘客出示以帮助识别正确车辆的东西。与此相同：GTFS 实时信息-车辆描述符中的 "label "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `vehicle_position[object]`: 描述与该观测数据相对应的车辆的实时位置。SameAs:'vehicle' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  	- `current_status[string]`: 描述与该观测点相对应的停靠站的车辆状态 ENUM：[INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]。与 GTFS 实时信息--车辆位置（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition）中的 "current_status "字段相同。    
	- `current_stop_sequence[number]`: 给出当前停站的停站序列索引。这是通过考虑 current_status 确定的，如果缺少 current_status，则假定为 IN_TRANSIT_TO。与 GTFS 实时报文-VehiclePosition（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition）中的'current_stop_sequence'字段相同。    
	- `position[object]`: 描述与该观测值相对应的车辆当前位置。相同：GTFS 实时信息-车辆位置（https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition）中的 "位置 "字段    
	- `stop_id[string]`: 与本次观测中的巴士相对应的巴士站 ID/站名。与此相同：GTFS 实时信息-车辆位置中的 "stop_id "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
	- `timestamp[date-time]`: 最后报告的从车辆观察到的时间。与此相同：  GTFS 实时信息-车辆位置中的 "时间戳 "字段 (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
	- `trip[object]`: 描述该观测点对应的车辆正在进行的行程。SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)    
	- `vehicleDesc[object]`: 描述与该观测信息相对应的车辆附加信息。SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)    
<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
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
## 有效载荷示例  
#### TransitManagement NGSI-v2 密钥值示例  
下面是一个以 JSON-LD 格式作为键值的 TransitManagement 示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### TransitManagement NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 TransitManagement 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### TransitManagement NGSI-LD key-values 示例  
下面是一个以 JSON-LD 格式作为键值的 TransitManagement 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
#### TransitManagement NGSI-LD 常态化示例  
下面是一个规范化 JSON-LD 格式的 TransitManagement 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
