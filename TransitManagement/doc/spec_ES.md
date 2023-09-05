<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: TransitManagement  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/TransitManagement/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Modelo de datos de un sistema de transporte público  
versión: 0.0.4  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `acAvailable[string]`: Describe la presencia de la opción de aire acondicionado en el vehículo correspondiente a esta observación  - `ac_available[string]`: Describe la presencia de la opción de aire acondicionado en el vehículo correspondiente a esta observación  - `actual_trip_end_time[date-time]`: Este campo especifica la hora a la que está previsto que finalice el servicio o el viaje correspondiente a esta observación  - `actual_trip_start_time[date-time]`: Este campo especifica la hora a la que comenzó realmente el servicio.  Es SameAs: 'hora' absoluta(StopTimeEvent) en el campo 'llegada' del mensaje stop_time_update (StopTimeUpdate) del mensaje GTFS Realtime-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  - `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local    
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `agencyInfo[object]`: Información de la Agencia correspondiente a esta observación  	- `agency_email[string]`: Dirección de correo electrónico supervisada activamente por el servicio de atención al cliente de la agencia. Igual que: campo 'agency_email' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_fare_url[string]`: URL de una página web que contiene los detalles de las tarifas y también podría permitir comprar billetes para esa agencia en línea. Igual que: campo 'agency_fare_url' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_id[string]`: ID que identifica unívocamente a una agencia de transporte. Un feed de tránsito puede representar datos de más de una agencia. El agency_id es exclusivo del conjunto de datos. Este campo es opcional para los flujos de tránsito que sólo contienen datos de una única agencia. Igual que: campo 'agency_id' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_lang[string]`: Contiene un código ISO 639-1 de dos letras para la lengua principal utilizada por esta agencia de tránsito. El código de idioma no distingue entre mayúsculas y minúsculas (se aceptan tanto en como EN). Idéntico a: campo 'agency_lang' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_name[string]`: El campo agency_name contiene el nombre completo de la agencia de tránsito. Igual que: campo 'agency_name' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_phone[string]`: Un número de teléfono de voz para la agencia especificada.SameAs: campo 'agency_phone' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)    
	- `agency_timezone[string]`: El campo Zona horaria contiene la zona horaria en la que se encuentra la agencia de tránsito. Igual que: campo 'agency_timezone' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)    
- `agency_fare_url[string]`: URL de una página web que contiene los detalles de las tarifas y también podría permitir comprar billetes para esa agencia en línea. Igual que: campo 'agency_fare_url' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_id[string]`: ID que identifica unívocamente a una agencia de transporte. Un feed de tránsito puede representar datos de más de una agencia. El agency_id es exclusivo del conjunto de datos. Este campo es opcional para los flujos de tránsito que sólo contienen datos de una única agencia. Igual que: campo 'agency_id' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_lang[string]`: Contiene un código ISO 639-1 de dos letras para la lengua principal utilizada por esta agencia de tránsito. El código de idioma no distingue entre mayúsculas y minúsculas (se aceptan tanto en como EN). Idéntico a: campo 'agency_lang' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_name[string]`: El campo agency_name contiene el nombre completo de la agencia de tránsito. Igual que: campo 'agency_name' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_timezone[string]`: El campo Zona horaria contiene la zona horaria en la que se encuentra la agencia de tránsito. Igual que: campo 'agency_timezone' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_url[string]`: El campo agency_url contiene la URL de la agencia de tránsito. Igual que: campo 'agency_url' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrival[object]`: Si schedule_relationship está vacío o SCHEDULED, se debe proporcionar la llegada o la salida dentro de un StopTimeUpdate. Igual que: campo 'arrival' del mensaje GTFS Realtime-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  	  
- `arrivalUncertainty[number]`: Si schedule_relationship está vacío o SCHEDULED, se debe proporcionar la llegada o la salida dentro de un StopTimeUpdate. Igual que: campo 'arrival' del mensaje GTFS Realtime-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `arrival_time[time]`: Especifica la hora de llegada a una parada específica para un viaje específico en una ruta. Las horas deben tener ocho dígitos en formato HH:MM:SS (también se acepta HH:MM:SS, si la hora empieza por 0). Nota: Los viajes que abarcan varias fechas tendrán horas de parada superiores a 24:00:00. Por ejemplo, si un viaje comienza a las 22:30:00 y termina a las 2:15:00 del día siguiente, las horas de parada serán las 22:30:00 y las 26:15:00 horas. Introducir esas horas de parada como 22:30:00 y 02:15:00 no produciría los resultados deseados. Igual que: campo 'arrival_time' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `bearing[number]`: Indica el ángulo GPS del vehículo medido en el sentido de las agujas del reloj a partir del Norte verdadero. Igual que el campo "bearing" de GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)  - `current_status[string]`: Describe el estado del vehículo en relación con la parada correspondiente a esta observación ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. Idéntico al campo "current_status" del mensaje GTFS Realtime-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `current_stop_sequence[number]`: Proporciona el índice de secuencia de parada de la parada actual. Se determina teniendo en cuenta current_status, si current_status falta se asume IN_TRANSIT_TO. Idéntico al campo "current_stop_sequence" del mensaje GTFS en tiempo real VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `dataDescriptor[uri]`: URI que apunta a la entidad descriptora de datos  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `departure[object]`: Si schedule_relationship está vacío o SCHEDULED, se debe proporcionar la llegada o la salida dentro de un StopTimeUpdate. Igual que: campo 'departure' del mensaje GTFS Realtime-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  	  
- `departureUncertainty[number]`: Si schedule_relationship está vacío o SCHEDULED, se debe proporcionar la llegada o la salida dentro de un StopTimeUpdate. Igual que: campo 'departure' del mensaje GTFS Realtime-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `departure_time[time]`: Especifica la hora de salida desde una parada específica para un viaje específico en una ruta. Las horas deben tener ocho dígitos en formato HH:MM:SS (también se acepta HH:MM:SS, si la hora empieza por 0).  
Nota: Los viajes que abarcan varias fechas tendrán horas de parada superiores a 24:00:00. Por ejemplo, si un viaje comienza a las 22:30:00 y termina a las 2:15:00 del día siguiente, las horas de parada serán las 22:30:00 y las 26:15:00 horas. Introducir esas horas de parada como 22:30:00 y 02:15:00 no produciría los resultados deseados. Igual que: campo 'departure_time' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `depotID[string]`: Describe el identificador único del depósito de autobuses correspondiente a esta observación  - `depotName[string]`: Describe el nombre del depósito de autobuses correspondiente a esta observación  - `depot_id[string]`: Describe el identificador único del depósito de autobuses correspondiente a esta observación  - `depot_name[string]`: Describe el nombre del depósito de autobuses correspondiente a esta observación  - `description[string]`: Descripción de este artículo  - `deviceInfo[object]`: Información sobre el dispositivo asociado a las observaciones  . Model: [https://schema.org/Text](https://schema.org/Text)	- `deviceBatteryStatus[string]`: Indica el estado de carga de la batería del dispositivo informador (Conectado, Desconectado)  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceID[string]`: ID de dispositivo del sensor físico/estación de medición correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceModel[object]`: Describe la información del dispositivo, sensor o sistema en cuestión.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceName[string]`: Nombre del dispositivo o nombre de la estación del dispositivo/estación del sensor correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `deviceSimNumber[string]`: Indica el número sim del dispositivo del vehículo de gestión de residuos  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `measurand[string]`: Propiedad/propiedades detectadas/observadas/medidas por el dispositivo  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `direction_id[number]`: Indica la dirección de desplazamiento del vehículo correspondiente a esta observación, puede referenciarse desde el feed estático GTFS trips.txt. Igual que: campo 'direction_id' de GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `entity_id[string]`: ID único de alimentación para la entidad correspondiente a esta observación.SameAs:'entity_id' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  - `id[*]`: Identificador único de la entidad  - `last_stop_arrival_time[time]`: Especifica la hora de llegada a la parada anterior para un viaje específico en una ruta. Las horas deben tener ocho dígitos en formato HH:MM:SS (también se acepta H:MM:SS, si la hora empieza por 0).  
Nota: Los viajes que abarcan varias fechas tendrán horas de parada superiores a 24:00:00. Por ejemplo, si un viaje comienza a las 22:30:00 y termina a las 2:15:00 del día siguiente, las horas de parada serán las 22:30:00 y las 26:15:00 horas. Introducir esas horas de parada como 22:30:00 y 02:15:00 no produciría los resultados deseados. Esto es SameAs: absolute 'time'(StopTimeEvent) en el campo 'arrival' del mensaje stop_time_update (StopTimeUpdate) del mensaje GTFS Realtime-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  - `last_stop_id[string]`: ID de parada/Nombre de parada de la parada anterior correspondiente al autobús de esta observación. Igual que: campo 'stop_id' del mensaje en tiempo real GTFS-VehiclePosition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `last_tracked_time[date-time]`: Indica la hora a la que el vehículo fue rastreado por última vez  - `license_plate[string]`: Indica el número de matrícula del vehículo. Idéntico a campo 'license_plate' de GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `observationDateTime[date-time]`: Última hora de observación comunicada  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `position[object]`: Describe la posición actual del vehículo correspondiente a esta observación. Idéntico a: position field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  . Model: [https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition](https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)	- `bearing[number]`: Rumbo, en grados, en el sentido de las agujas del reloj a partir del Norte verdadero, es decir, 0 es Norte y 90 es Este. Puede ser el rumbo de la brújula o la dirección hacia la siguiente parada o ubicación intermedia. No debe deducirse de la secuencia de posiciones anteriores, que los clientes pueden calcular a partir de datos anteriores.    
	- `latitude[number]`: Grados Norte, en el sistema de coordenadas WGS-84    
	- `longitude[number]`: Grados Este, en el sistema de coordenadas WGS-84    
	- `odometer[number]`: Valor del cuentakilómetros, en metros    
- `positionInfo[object]`: Describe la posición actual del vehículo correspondiente a esta observación. Idéntico al campo "position" de GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  	- `bearing[number]`: Rumbo, en grados, en el sentido de las agujas del reloj a partir del Norte verdadero, es decir, 0 es Norte y 90 es Este. Puede ser el rumbo de la brújula o la dirección hacia la siguiente parada o ubicación intermedia. No debe deducirse de la secuencia de posiciones anteriores, que los clientes pueden calcular a partir de datos anteriores.    
	- `odometer[number]`: Valor del cuentakilómetros    
- `routeInfo[object]`: Secuencia de paradas ordenada actualizada para el viaje realizado por el vehículo correspondiente a esta observación, que no se tendrá en cuenta si schedule_realtionship es CANCELED. Igual que: campo 'stop_time_update' de GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `route_color[string]`: Si está asignado, este campo define un color que corresponde a una ruta. El color debe proporcionarse como un número hexadecimal de seis caracteres, por ejemplo, 00FFFF. Si no se especifica ningún color, el color de ruta por defecto es el blanco (FFFFFF). Igual que: campo 'route_color' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)    
	- `route_desc[string]`: Descripción de la ruta. Puede incluir todos los detalles de la ruta, incluido el destino de ida y vuelta y la información horaria en forma de descripción de texto. Igual que: campo 'route_desc' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)    
	- `route_id[string]`: ID de ruta asignada a la ruta por la que circula actualmente el autobús/vehículo correspondiente al autobús de esta observación    
	- `route_long_name[string]`: Nombre completo de una ruta. Este nombre es más descriptivo que el routeShortName y a menudo incluye el destino o la parada de la ruta. Suele incluir los nombres de destino de ida y vuelta de la ruta. Idéntico a campo 'route_long_name' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)    
	- `route_short_name[string]`: Nombre abreviado de una ruta. Suele ser el nombre del vehículo, como 402D o Green, que los usuarios utilizan para identificar una ruta. Igual que: campo 'route_short_name' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)    
	- `route_text_color[string]`: Este campo puede utilizarse para especificar un color legible que se utilizará para el texto dibujado sobre un fondo de route_color. El color debe proporcionarse como un número hexadecimal de seis caracteres, por ejemplo, FFD700. Si no se especifica ningún color, el color por defecto del texto es el negro (000000). Igual que: campo 'route_text_color' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)    
	- `route_type[number]`: Número que indica el tipo de transporte: 1 - Metro. Cualquier sistema ferroviario subterráneo dentro de un área metropolitana. 2 - Ferrocarril. Utilizado para viajes interurbanos o de larga distancia. 3 - Autobús. Utilizado para rutas de autobús de corta y larga distancia. Idéntico a: campo 'route_type' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)    
- `routeStopSequence[array]`: Proporciona los identificadores de parada/códigos de parada o identificadores de estación/códigos de estación en la secuencia correcta para la ruta o línea correspondiente a esta observación.  - `route_color[string]`: Si está asignado, este campo define un color que corresponde a una ruta. El color debe proporcionarse como un número hexadecimal de seis caracteres, por ejemplo, 00FFFF. Si no se especifica ningún color, el color de ruta por defecto es el blanco (FFFFFF). Igual que: campo 'route_color' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_desc[string]`: Descripción de la ruta. Puede incluir todos los detalles de la ruta, incluido el destino de ida y vuelta y la información horaria en forma de descripción de texto. Igual que: campo 'route_desc' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_id[string]`: ID de ruta asignado a la ruta por la que circula actualmente el autobús/vehículo correspondiente al autobús de esta observación. Igual que: campo 'route_id' de GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `route_long_name[string]`: Nombre completo de una ruta. Este nombre es más descriptivo que el routeShortName y a menudo incluye el destino o la parada de la ruta. Suele incluir los nombres de destino de ida y vuelta de la ruta. Idéntico a campo 'route_long_name' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_short_name[string]`: Nombre abreviado de una ruta. Suele ser el nombre del vehículo, como "402D" o "Verde", que los usuarios utilizan para identificar una ruta. Igual que: campo 'route_short_name' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_text_color[string]`: Este campo puede utilizarse para especificar un color legible que se utilizará para el texto dibujado sobre un fondo de route_color. El color debe proporcionarse como un número hexadecimal de seis caracteres, por ejemplo, FFD700. Si no se especifica ningún color, el color por defecto del texto es el negro (000000). Igual que: campo 'route_text_color' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_type[string]`: Número que indica el tipo de transporte-1 - Metro. Cualquier sistema ferroviario subterráneo dentro de un área metropolitana.2 - Ferrocarril. Utilizado para viajes interurbanos o de larga distancia.3 - Autobús. Utilizado para rutas de autobús de corta y larga distancia. Idéntico a: campo 'route_type' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_url[string]`: Contiene la URL de una página web sobre esa ruta en particular y es diferente de agency_url. Igual que: campo 'route_url' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `schedule_relationship[string]`: Describe si la Ruta/Viaje ha sido programada. Idéntico a campo 'schedule_relationship' de enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)  - `seating_capacity[number]`: Describe la capacidad de plazas de pasajeros del vehículo correspondiente a esta observación  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `shapeInfo[object]`: Información sobre la trayectoria que recorre el vehículo correspondiente a esta observación  	- `shape_dist_traveled[number]`: Distancia real recorrida a lo largo de la forma desde el primer punto de la forma hasta el punto especificado en este registro. Utilizado por los planificadores de viajes para mostrar la parte correcta de la forma en un mapa. Los valores deben aumentar junto con shape_pt_sequence; no pueden utilizarse para mostrar el recorrido inverso a lo largo de una ruta. Las unidades de distancia deben ser coherentes con las utilizadas en stop_times.txt. Ejemplo: Si un autobús recorre los tres puntos definidos anteriormente para A_shp, los valores shape_dist_traveled adicionales (mostrados aquí en kilómetros) tendrían el siguiente aspecto: shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled A_shp,37.61956,-122.48161,0,0 A_shp,37.64430,-122.41070,6,6.8310 A_shp,37.65863,-122.30839,11,15.8765    
	- `shape_id[string]`: Identifica una forma    
- `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `speed[number]`: Indica la velocidad del vehículo. Igual que el campo "speed" de GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)  - `standing_capacity[number]`: Describe la capacidad de pasajeros de pie del vehículo correspondiente a esta observación  - `start_date[string]`: Describe la fecha inicial programada del viaje correspondiente al vehículo esta observación. Un formato de ejemplo para este campo - AAAAMMDD. Idéntico a campo 'start_date' de GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `start_time[time]`: Describe la hora inicial programada de inicio del viaje correspondiente al vehículo de esta observación. Un formato de ejemplo para este campo - 11:15:35 o 25:15:35. Idéntico a campo 'start_time' de GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `stopInfo[object]`: Información sobre la trayectoria que recorre el vehículo correspondiente a esta observación  	- `stop_code[string]`: Este campo contiene un texto corto o un número que identifica de forma única la parada para los pasajeros. Puede ser el mismo que stop_id si es para público. Idéntico a campo 'stop_code' de GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)    
	- `stop_desc[string]`: Este campo contiene la descripción de una parada. Idéntico a campo 'stop_desc' de GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)    
	- `stop_id[string]`: ID único asignado a la parada correspondiente a esta observación    
	- `stop_name[string]`: Describe el nombre de una parada o estación. Idéntico a campo 'stop_name' de GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)    
- `stopTimeUpdateInfo[object]`: Secuencia de paradas ordenada actualizada para el viaje realizado por el vehículo correspondiente a esta observación, que no se tendrá en cuenta si schedule_realtionship es CANCELED. Igual que: campo 'stop_time_update' de GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `stopScheduleRelationship[string]`: Describe la relación entre el horario estático y la parada. Idéntico a: campo 'schedule_relationship' de GTFS Realtime message-StopTimeUpdate ENUM[SCHEDULED, SKIPPED, NO_DATA] (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)    
	- `stop_id[string]`: ID único asignado a la parada correspondiente a esta observación    
- `stopTimesInfo[object]`: Un descriptor de la actualización en tiempo real del horario de un vehículo a lo largo de un viaje  	- `arrival_time[time]`: Especifica la hora de llegada a una parada específica para un viaje específico en una ruta. Las horas deben tener ocho dígitos en formato HH:MM:SS (también se acepta HH:MM:SS, si la hora empieza por 0). Nota: Los viajes que abarcan varias fechas tendrán horas de parada superiores a 24:00:00. Por ejemplo, si un viaje comienza a las 22:30:00 y termina a las 2:15:00 del día siguiente, las horas de parada serán las 22:30:00 y las 26:15:00 horas. Introducir esas horas de parada como 22:30:00 y 02:15:00 no produciría los resultados deseados. Igual que: campo 'arrival_time' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `continuous_drop_off[number]`: Indica si un pasajero puede bajarse del vehículo de tránsito en cualquier punto del recorrido del vehículo: campo 'continuous_drop_off' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `continuous_pickup[number]`: Indica si un pasajero puede subir al vehículo de tránsito en cualquier punto del recorrido del vehículo: campo 'continuous_pickup' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `departure_time[time]`: Especifica la hora de salida desde una parada específica para un viaje específico en una ruta. Las horas deben tener ocho dígitos en formato HH:MM:SS (también se acepta HH:MM:SS, si la hora empieza por 0). Nota: Los viajes que abarcan varias fechas tendrán horas de parada superiores a 24:00:00. Por ejemplo, si un viaje comienza a las 22:30:00 y termina a las 2:15:00 del día siguiente, las horas de parada serán las 22:30:00 y las 26:15:00 horas. Introducir esas horas de parada como 22:30:00 y 02:15:00 no produciría los resultados deseados. Igual que: campo 'departure_time' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `drop_off_type[string]`: Indica el método de entrega. Igual que: campo 'drop_off_type' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `pickup_type[string]`: Indica el método de recogida: campo 'pickup_type' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `stop_headsign[string]`: Este campo contiene el texto que aparece en un cartel que identifica el destino del viaje a los pasajeros. Igual que: campo 'stop_headsign' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `stop_id[string]`: ID único asignado a la parada correspondiente a esta observación    
	- `stop_sequence[number]`: Este campo identifica el orden de las paradas para un viaje en particular. Los valores de secuencia_paradas deben ser enteros no negativos y deben aumentar a lo largo del viaje. Por ejemplo, la primera parada del viaje podría tener una secuencia de paradas de 1, la segunda parada del viaje podría tener una secuencia de paradas de 23, la tercera parada podría tener una secuencia de paradas de 40, etc.    
- `stop_code[string]`: Este campo contiene un texto corto o un número que identifica de forma única la parada para los pasajeros. Puede ser el mismo que stop_id si es para público. Idéntico a campo 'stop_code' de GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_desc[string]`: Este campo contiene la descripción de una parada. Idéntico a campo 'stop_desc' de GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_headsign[string]`: Este campo contiene el texto que aparece en un cartel que identifica el destino del viaje a los pasajeros. Igual que: campo 'stop_headsign' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `stop_id[string]`: ID de parada/Nombre de parada de las paradas correspondientes al autobús en esta observación. Igual que: campo 'stop_id' del mensaje en tiempo real GTFS-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `stop_name[string]`: Describe el nombre de la parada de autobús. Idéntico a campo 'stop_name' de GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_sequence[number]`: Indica la secuencia de parada del vehículo correspondiente a esta observación, puede ser referenciada desde el feed estático GTFS stop_times.txt. Igual que: campo 'stop_sequence' del mensaje en tiempo real GTFS-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `stop_sequence_detail[object]`: Describe la secuencia de paradas para un viaje en la ruta designada realizada por el vehículo de transporte público.SameAs: campo 'stop_sequence' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  	- `stop_id[string]`: Debe ser el mismo que en stops.txt en el feed GTFS correspondiente. Se debe proporcionar stop_sequence o stop_id dentro de un StopTimeUpdate - ambos campos no pueden estar vacíos.    
- `stop_time_update[object]`: Información adicional sobre el vehículo que presta servicio en este viaje  	- `arrival[object]`: Si schedule_relationship está vacío o SCHEDULED, se debe proporcionar la llegada o la salida dentro de un StopTimeUpdate - ambos campos no pueden estar vacíos. arrival y departure pueden estar vacíos cuando schedule_relationship es SKIPPED. Si schedule_relationship es NO_DATA, arrival y departure deben estar vacíos.    
	- `departure[object]`: Si schedule_relationship está vacío o SCHEDULED, se debe proporcionar la llegada o la salida dentro de un StopTimeUpdate - ambos campos no pueden estar vacíos. arrival y departure pueden estar vacíos cuando schedule_relationship es SKIPPED. Si schedule_relationship es NO_DATA, arrival y departure deben estar vacíos.    
	- `schedule_relationship[string]`: Enum:'PROGRAMADO, OMITIDO, NO_DATA'. PROGRAMADO significa que el vehículo avanza de acuerdo con su programa estático de paradas, aunque no necesariamente de acuerdo con los tiempos del programa. Este es el comportamiento por defecto. Debe proporcionarse al menos uno de llegada y otro de salida. SKIPPED significa que La parada se salta, es decir, el vehículo no se detendrá en esta parada. Los campos de llegada y salida son opcionales. NO_DATA significa que no se proporcionan datos para esta parada. Indica que no hay información disponible en tiempo real. Cuando se establece NO_DATA se propaga a través de las paradas siguientes, por lo que es la forma recomendada de especificar a partir de qué parada no se dispone de información en tiempo real. Cuando se establece NO_DATA no se debe proporcionar ni la llegada ni la salida.    
	- `stop_id[string]`: Debe ser el mismo que en stops.txt en el feed GTFS correspondiente. Se debe proporcionar stop_sequence o stop_id dentro de un StopTimeUpdate - ambos campos no pueden estar vacíos.    
- `stop_url[string]`: Este campo contiene la URL de una página web sobre una parada concreta y es diferente de los campos agency_url y route_url. Igual que: campo 'stop_url' de GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `timestamp[date-time]`: Última hora de observación del vehículo comunicada. Igual que: campo "timestamp" de GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `travelDistance[number]`: La distancia entre la parada de origen y la parada de destino o la distancia total recorrida correspondiente a esta observación  - `travelTime[time]`: El tiempo empleado en el trayecto entre la parada de origen y la parada de destino correspondiente a esta observación en formato HH:MM:SS(también se acepta HH:MM:SS, si la hora empieza por 0)  - `trip[object]`: Describe el viaje que está realizando el vehículo correspondiente a esta observación. Idéntico al campo 'trip' del mensaje GTFS Realtime-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `direction_id[number]`: Indica la dirección de desplazamiento del vehículo correspondiente a esta observación, puede referenciarse desde el feed estático GTFS trips.txt. Igual que: campo 'direction_id' de GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
	- `route_id[string]`: ID de ruta asignado a la ruta por la que circula actualmente el autobús/vehículo correspondiente al autobús de esta observación. Igual que: campo 'route_id' de GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
	- `schedule_relationship[string]`: Describe si la Ruta/Viaje ha sido programada. Idéntico a campo 'schedule_relationship' de enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)    
	- `start_date[string]`: Describe la fecha inicial programada del viaje correspondiente al vehículo esta observación. Un formato de ejemplo para este campo - AAAAMMDD. Idéntico a campo 'start_date' de GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
	- `start_time[string]`: Describe la hora inicial programada de inicio del viaje correspondiente al vehículo de esta observación. Un formato de ejemplo para este campo - 11:15:35 o 25:15:35. Idéntico a campo 'start_time' de GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
- `tripDetails[object]`: Un descriptor de la actualización en tiempo real del horario de un vehículo a lo largo de un viaje  	- `arrival_time[time]`:  Especifica la hora de llegada a una parada específica para un viaje específico en una ruta. Las horas deben tener ocho dígitos en formato HH:MM:SS (también se acepta HH:MM:SS, si la hora empieza por 0). Nota: Los viajes que abarcan varias fechas tendrán horas de parada superiores a 24:00:00. Por ejemplo, si un viaje comienza a las 22:30:00 y termina a las 2:15:00 del día siguiente, las horas de parada serán las 22:30:00 y las 26:15:00 horas. Introducir esas horas de parada como 22:30:00 y 02:15:00 no produciría los resultados deseados. Igual que: campo 'arrival_time' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `departure_time[time]`: Especifica la hora de salida desde una parada específica para un viaje específico en una ruta. Las horas deben tener ocho dígitos en formato HH:MM:SS (también se acepta HH:MM:SS, si la hora empieza por 0). Nota: Los viajes que abarcan varias fechas tendrán horas de parada superiores a 24:00:00. Por ejemplo, si un viaje comienza a las 22:30:00 y termina a las 2:15:00 del día siguiente, las horas de parada serán las 22:30:00 y las 26:15:00 horas. Introducir esas horas de parada como 22:30:00 y 02:15:00 no produciría los resultados deseados. Igual que: campo 'departure_time' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `stop_headsign[string]`: Este campo contiene el texto que aparece en un cartel que identifica el destino del viaje a los pasajeros. Igual que: campo 'stop_headsign' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)    
	- `stop_id[string]`: ID de parada/Nombre de parada de las paradas correspondientes al autobús en esta observación. Igual que: campo 'stop_id' del mensaje en tiempo real GTFS-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
- `tripDirection[string]`: Indica la dirección en la que se desplaza el vehículo ENUM[UP,DN]  - `tripInfo[object]`: Describe el viaje que está realizando el vehículo correspondiente a esta observación. Idéntico al campo "trip" de GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  	- `route_id[string]`: ID de ruta asignada a la ruta por la que circula actualmente el autobús/vehículo correspondiente al autobús de esta observación    
	- `schedule_relationship[string]`: Describe si la Ruta/Viaje ha sido programada. Idéntico a: campo 'schedule_relationship' de GTFS Realtime message-TripDescriptor ENUM[SCHEDULED, ADDED, UNSCHEDULED, CANCELED] (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
	- `start_date[string]`: Describe la fecha inicial programada del viaje correspondiente al vehículo esta observación. Un formato de ejemplo para este campo - AAAAMMDD. Idéntico a campo 'start_date' de GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
	- `start_time[time]`: Describe la hora inicial programada de inicio del viaje correspondiente al vehículo de esta observación. Un formato de ejemplo para este campo - 11:15:35 o 25:15:35. Idéntico a campo 'start_time' de GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
	- `trip_direction[string]`: Indica la dirección de desplazamiento del vehículo correspondiente a esta observación, puede referenciarse desde el feed estático GTFS trips.txt. Igual que: campo 'direction_id' de GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)    
- `trip_delay[number]`: Puede ser positivo y negativo en segundos y muestra cuánto se desvía el vehículo del previsto. Igual que: campo 'delay' de GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)  - `trip_details[object]`: Un descriptor de la actualización en tiempo real del horario de un vehículo a lo largo de un viaje  	- `bearing[number]`: Rumbo, en grados, en el sentido de las agujas del reloj a partir del Norte verdadero, es decir, 0 es Norte y 90 es Este. Puede ser el rumbo de la brújula o la dirección hacia la siguiente parada o ubicación intermedia. No debe deducirse de la secuencia de posiciones anteriores, que los clientes pueden calcular a partir de datos anteriores.    
	- `odometer[number]`: Valor del cuentakilómetros, en metros    
- `trip_direction[string]`: Indica la dirección en la que circula el vehículo. Igual que: campo "direction_id" del descriptor de viaje-mensaje GTFS en tiempo real, pero se representa en forma de ENUM[UP,DN] en lugar de [0,1] como se ve en "direction_id" (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor).  - `trip_id[string]`: ID del viaje/Nombre del viaje asignado al autobús correspondiente a esta observación, teniendo en cuenta la hora del día y la dirección del viaje en el routeId dado. Igual que: campo 'trip_id' de GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `trip_update[object]`: Describe la información del viaje, como retrasos, salidas, etc., de un viaje realizado por el vehículo correspondiente a esta observación.SameAs:'trip_update' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  	- `stop_time_update[object]`: Información adicional sobre el vehículo que presta servicio en este viaje    
	- `timestamp[date-time]`: Última hora de observación del vehículo comunicada. Igual que: campo "timestamp" de GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
	- `trip[object]`: Describe el viaje que está realizando el vehículo correspondiente a esta observación. Idéntico al campo 'trip' del mensaje GTFS Realtime-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)    
- `type[string]`: Tipo de entidad NGSI. Tiene que ser TransitManagement  - `uncertainty[number]`: Si se omite la incertidumbre, se interpreta como desconocida. Para especificar una predicción completamente segura, establezca su incertidumbre en 0.SameAs: campo 'uncertainty' de GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)  - `vehicleDesc[object]`: Describe la información adicional del vehículo correspondiente a esta observación. Idéntico a: campo 'vehicle' del mensaje GTFS Realtime-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `license_plate[string]`: Proporciona el número de matrícula del vehículo: campo 'license_plate' del mensaje GTFS Realtime - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)    
	- `vehicle_id[string]`: ID único asignado al vehículo correspondiente a esta observación, utilizado en la identificación interna del sistema: campo 'id' del mensaje GTFS Realtime - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)    
- `vehicleInfo[object]`: Describe la información adicional del vehículo correspondiente a esta observación. Idéntico a: campo 'vehicle' del mensaje GTFS Realtime-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `license_plate[string]`: Indica el número de matrícula del vehículo. Igual que: campo 'license_plate' de GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)    
	- `vehicleID[string]`: ID único asignado al vehículo correspondiente a esta observación, utilizado en la identificación interna del sistema. Igual que: campo "id" de GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)    
- `vehiclePositionInfo[object]`: Describe la posición en tiempo real del vehículo correspondiente a esta observación. Idéntico al campo "vehicle" de GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  	- `congestion_level[string]`: Describe el nivel de congestión que afecta a este vehículo. ENUM [UNKNOWN_CONGESTION_LEVEL, RUNNING_SMOOTHLY, STOP_AND_GO, CONGESTION, SEVERE_CONGESTION]    
	- `current_status[string]`: Describe el estado del vehículo en relación con la parada correspondiente a esta observación ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. Idéntico al campo "current_status" del mensaje GTFS Realtime-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
	- `current_stop_sequence[number]`: Proporciona el índice de secuencia de parada de la parada actual. Se determina teniendo en cuenta current_status, si current_status falta se asume IN_TRANSIT_TO. Idéntico al campo "current_stop_sequence" del mensaje GTFS en tiempo real VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
	- `occupancy_status[string]`: Grado de ocupación de pasajeros del vehículo. ENUM [EMPTY, MANY_SEATS_AVAILABLE, FEW_SEATS_AVAILABLE, STANDING_ROOM_ONLY, CRUSHED_STANDING_ROOM_ONLY, FULL, NOT_ACCEPTING_PASSENGERS, NO_DATA_AVAILABLE, NOT_BOARDABLE].    
- `vehicleType[string]`: Describe el tipo de vehículo correspondiente a esta observación, puede ser tolva, compactador, volquete, dumper en el caso de vehículos de gestión de residuos sólidos, minibús BRT, autobús BRT, autobús urbano en el caso de vehículos ITMS, ambulancia, camión de bomberos, furgón de policía, etc., en el caso de vehículos de emergencia y ciclomotor/scooter, motocicleta, autorickshaw, coche particular/coche Jeep, Tempo, autobús, E-Moped/E-Scooter/E-Motor Cycle, motor público en el caso de matriculación de vehículos.  - `vehicle_id[string]`: ID único asignado al vehículo correspondiente a esta observación, utilizado en la identificación interna del sistema. Igual que: campo "id" de GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `vehicle_label[string]`: Etiqueta visible para el usuario, es decir, algo que debe mostrarse al pasajero para ayudarle a identificar el vehículo correcto. Igual que: campo 'label' de GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `vehicle_position[object]`: Describe la posición en tiempo real del vehículo correspondiente a esta observación. Idéntico al campo "vehicle" de GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  	- `current_status[string]`: Describe el estado del vehículo en relación con la parada correspondiente a esta observación ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. Idéntico al campo "current_status" del mensaje GTFS Realtime-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
	- `current_stop_sequence[number]`: Proporciona el índice de secuencia de parada de la parada actual. Se determina teniendo en cuenta current_status, si current_status falta se asume IN_TRANSIT_TO. Idéntico al campo "current_stop_sequence" del mensaje GTFS en tiempo real VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
	- `position[object]`: Describe la posición actual del vehículo correspondiente a esta observación. Idéntico a campo "position" de GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
	- `stop_id[string]`: ID de parada/Nombre de parada de las paradas correspondientes al autobús en esta observación. Igual que: campo 'stop_id' del mensaje en tiempo real GTFS-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
	- `timestamp[date-time]`: Última hora de observación del vehículo comunicada. Igual que:  campo "timestamp" de GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)    
	- `trip[object]`: Describe el viaje que está realizando el vehículo correspondiente a esta observación. Idéntico al campo 'trip' del mensaje GTFS Realtime-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)    
<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
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
## Ejemplo de carga útil  
#### TransitManagement NGSI-v2 key-values Ejemplo  
He aquí un ejemplo de un TransitManagement en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### TransitManagement NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de un TransitManagement en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### TransitManagement NGSI-LD key-values Ejemplo  
He aquí un ejemplo de un TransitManagement en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### TransitManagement NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un TransitManagement en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
