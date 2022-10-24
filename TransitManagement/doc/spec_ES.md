<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: TransitManagement  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/TransitManagement/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Modelo de datos de un sistema de transporte público**  
versión: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `ac_available[string]`: Describe la presencia de la opción de aire acondicionado en el vehículo correspondiente a esta observación.  - `actual_trip_end_time[string]`: Este campo especifica la hora a la que está previsto que finalice el servicio o el viaje correspondiente a esta observación.  - `actual_trip_start_time[string]`: Este campo especifica la hora a la que comenzó realmente el servicio.  Es igual a: "tiempo" absoluto (StopTimeEvent) en el campo "llegada" del mensaje stop_time_update (StopTimeUpdate) del mensaje GTFS Realtime-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  - `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `agency_fare_url[string]`: URL de una página web que contiene los detalles de las tarifas y que también podría permitir la compra de billetes para esa agencia en línea. Igual que: Campo 'agency_fare_url' de la definición de campo estático GTFS - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_id[string]`: ID que identifica de forma exclusiva a una agencia de transporte. Una fuente de tránsito puede representar datos de más de una agencia. El agency_id es un conjunto de datos único. Este campo es opcional para los flujos de tránsito que sólo contienen datos de una única agencia. Igual que: campo 'agency_id' de la definición de campo estático GTFS - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_lang[string]`: Contiene un código ISO 639-1 de dos letras para la lengua principal utilizada por este organismo de tránsito. El código de idioma no distingue entre mayúsculas y minúsculas (se aceptan tanto en como EN). Igual que: Campo 'agency_lang' de la definición de campo estático GTFS - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_name[string]`: El campo agency_name contiene el nombre completo de la agencia de transporte. Igual que: Campo 'agency_name' de la definición de campo estático GTFS - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_timezone[string]`: El campo Zona horaria contiene la zona horaria en la que se encuentra la agencia de transporte. Igual que: Campo 'agency_timezone' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_url[string]`: El campo agency_url contiene la URL de la agencia de transporte. Igual que: Campo 'agency_url' de la definición de campo estático GTFS - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrival[object]`: Si schedule_relationship está vacío o SCHEDULED, la llegada o la salida deben ser proporcionadas dentro de un StopTimeUpdate. Igual que: campo 'arrival' del mensaje GTFS Realtime-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `arrival_time[string]`: Especifica la hora de llegada a una parada específica para un viaje específico en una ruta. Las horas deben tener ocho dígitos en formato HH:MM:SS (también se acepta HH:MM:SS, si la hora empieza por 0). Nota: Los viajes que abarcan varias fechas tendrán horas de parada superiores a las 24:00:00. Por ejemplo, si un viaje comienza a las 10:30:00 p.m. y termina a las 2:15:00 a.m. del día siguiente, las horas de parada serían 22:30:00 y 26:15:00. Introducir esas horas de parada como 22:30:00 y 02:15:00 no produciría los resultados deseados. Igual que: Campo 'arrival_time' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `bearing[number]`: Indica el ángulo GPS del vehículo medido en el sentido de las agujas del reloj a partir del Norte verdadero. Igual que el campo "bearing" del mensaje GTFS Realtime-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)  - `current_status[string]`: Describe el estado del vehículo en relación con la parada correspondiente a esta observación ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. Igual que el campo "current_status" del mensaje GTFS Realtime-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `current_stop_sequence[number]`: Da el índice de secuencia de parada de la parada actual. Se determina teniendo en cuenta current_status, si current_status no existe se asume IN_TRANSIT_TO. Igual que el campo "current_stop_sequence" del mensaje GTFS Realtime-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `dataDescriptor[string]`: URI que apunta a la entidad descriptora de datos  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `departure[object]`: Si schedule_relationship está vacío o SCHEDULED, la llegada o la salida deben ser proporcionadas dentro de un StopTimeUpdate. Igual que: campo 'departure' de GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `departure_time[string]`: Especifica la hora de salida desde una parada específica para un viaje específico en una ruta. Las horas deben tener ocho dígitos en formato HH:MM:SS (también se acepta HH:MM:SS, si la hora empieza por 0).  
Nota: Los viajes que abarcan varias fechas tendrán horas de parada superiores a las 24:00:00. Por ejemplo, si un viaje comienza a las 10:30:00 p.m. y termina a las 2:15:00 a.m. del día siguiente, las horas de parada serían 22:30:00 y 26:15:00. Introducir esas horas de parada como 22:30:00 y 02:15:00 no produciría los resultados deseados. Igual que: Campo 'departure_time' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `depot_id[string]`: Describe el identificador único de la cochera correspondiente a esta observación.  - `depot_name[string]`: Describe el nombre del depósito de autobuses correspondiente a esta observación.  - `description[string]`: Una descripción de este artículo  - `deviceInfo[object]`: Información sobre el dispositivo asociado a las observaciones.  . Model: [https://schema.org/Text](https://schema.org/Text)- `direction_id[number]`: Indica el sentido de la marcha del vehículo correspondiente a esta observación, se puede referenciar desde el feed estático GTFS trips.txt. Igual que: campo 'direction_id' del mensaje GTFS Realtime-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `entity_id[string]`: ID único de la entidad que responde a esta observación.SameAs:'entity_id' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  - `id[*]`: Identificador único de la entidad  - `last_stop_arrival_time[string]`: Especifica la hora de llegada a la parada anterior para un viaje específico en una ruta. Las horas deben tener ocho dígitos en formato HH:MM:SS (también se acepta H:MM:SS, si la hora empieza por 0).  
Nota: Los viajes que abarcan varias fechas tendrán horas de parada superiores a las 24:00:00. Por ejemplo, si un viaje comienza a las 10:30:00 p.m. y termina a las 2:15:00 a.m. del día siguiente, las horas de parada serían 22:30:00 y 26:15:00. Introducir esas horas de parada como 22:30:00 y 02:15:00 no produciría los resultados deseados. Esto es SameAs: "hora" absoluta (StopTimeEvent) en el campo "llegada" del mensaje stop_time_update (StopTimeUpdate) del mensaje GTFS Realtime-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  - `last_stop_id[string]`: ID de la parada/nombre de la parada anterior correspondiente al autobús en esta observación. Igual que: Campo 'stop_id' del mensaje GTFS Realtime-VehiclePosition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `last_tracked_time[string]`: Indica la hora en la que el vehículo fue rastreado por última vez.  - `license_plate[string]`: Indica el número de matrícula del vehículo. Igual que: campo 'license_plate' de GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name[string]`: El nombre de este artículo.  - `observationDateTime[string]`: Última hora de observación comunicada.  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `position[object]`: Describe la posición actual del vehículo correspondiente a esta observación. Igual que: campo de posición de GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  . Model: [https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition](https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)- `routeStopSequence[array]`: Proporciona los identificadores de parada/códigos de parada o los identificadores de estación/códigos de estación en la secuencia correcta para la ruta o línea correspondiente a esta observación.  - `route_color[string]`: Si se asigna, este campo define un color que corresponde a una ruta. El color debe proporcionarse como un número hexadecimal de seis caracteres, por ejemplo, 00FFFF. Si no se especifica ningún color, el color de la ruta por defecto es el blanco (FFFFFF). Igual que: campo 'route_color' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_desc[string]`: Descripción de la ruta. Puede incluir todos los detalles de la ruta, incluyendo el origen y el destino y la información sobre el tiempo en forma de descripción de texto. Igual que: campo 'route_desc' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_id[string]`: ID de la ruta asignada a la ruta en la que el autobús/vehículo correspondiente al autobús de esta observación está circulando actualmente. Igual que: campo 'route_id' del mensaje GTFS Realtime-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `route_long_name[string]`: Nombre completo de una ruta. Este nombre es más descriptivo que el routeShortName y suele incluir el destino o la parada de la ruta. Suele incluir los nombres de destino de ida y vuelta de la ruta. Igual que: campo 'route_long_name' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_short_name[string]`: Nombre corto de una ruta. Suele ser el nombre de la placa del vehículo de transporte, como "402D" o "Verde", que los usuarios utilizan para identificar una ruta. Igual que: campo 'route_short_name' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_text_color[string]`: Este campo puede utilizarse para especificar un color legible que se utilizará para el texto dibujado sobre un fondo de route_color. El color debe proporcionarse como un número hexadecimal de seis caracteres, por ejemplo, FFD700. Si no se especifica ningún color, el color del texto por defecto es el negro (000000). Igual que: campo 'route_text_color' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_type[string]`: Número que indica el tipo de transporte-1 - Metro. Cualquier sistema ferroviario subterráneo dentro de un área metropolitana.2 - Ferrocarril. Utilizado para viajes interurbanos o de larga distancia.3 - Autobús. Utilizado para rutas de autobús de corta y larga distancia. Igual que: Campo 'route_type' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_url[string]`: Contiene la URL de una página web sobre esa ruta en particular y es diferente de agency_url. Igual que: campo 'route_url' de GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `schedule_relationship[string]`: Describe si la ruta/viaje ha sido programada. Igual que: campo 'schedule_relationship' de enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)  - `seating_capacity[number]`: Describe la capacidad de pasajeros del vehículo correspondiente a esta observación.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `speed[number]`: Indica la velocidad del vehículo. Igual que el campo 'speed' de GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)  - `standing_capacity[number]`: Describe la capacidad de pasajeros de pie del vehículo correspondiente a esta observación.  - `start_date[string]`: Describe la fecha inicial programada del viaje correspondiente al vehículo de esta observación. Un formato de ejemplo para este campo - AAAAMMDD. Igual que: campo 'start_date' de GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `start_time[string]`: Describe la hora de inicio programada del viaje correspondiente al vehículo de esta observación. Un formato de ejemplo para este campo - 11:15:35 o 25:15:35. Igual que: campo 'start_time' del mensaje GTFS Realtime-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `stop_code[string]`: Este campo contiene un texto corto o un número que identifica de forma exclusiva la parada para los pasajeros. Puede ser el mismo que stop_id si es para público. Igual que: Campo 'stop_code' de GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_desc[string]`: Este campo contiene la descripción de una parada. Igual que: Campo 'stop_desc' de GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_headsign[string]`: Este campo contiene el texto que aparece en un cartel que identifica el destino del viaje a los pasajeros. Igual que: Campo 'stop_headsign' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `stop_id[string]`: ID de parada/Nombre de parada de las paradas correspondientes al autobús en esta observación. Igual que: Campo 'stop_id' del mensaje en tiempo real GTFS-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `stop_name[string]`: Describe el nombre de la parada de autobús. Igual que: Campo 'stop_name' de GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_sequence[number]`: Indica la secuencia de parada del vehículo correspondiente a esta observación, puede ser referenciada desde el feed estático GTFS stop_times.txt. Igual que: campo 'stop_sequence' del mensaje GTFS Realtime-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `stop_sequence_detail[object]`: Describe la secuencia de paradas para un viaje en la ruta designada que realiza el vehículo de transporte público.SameAs: campo 'stop_sequence' de GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `stop_time_update[object]`: Información adicional sobre el vehículo que sirve para este viaje.  - `stop_url[string]`: Este campo contiene la URL de una página web sobre una parada concreta y es diferente de los campos agency_url y route_url. Igual que: Campo 'stop_url' de GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `timestamp[string]`: Última hora de observación del vehículo. Igual que: campo "timestamp" de GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `travelDistance[number]`: La distancia entre la parada de autobús de origen y la de destino o la distancia total recorrida correspondiente a esta observación.  - `travelTime[string]`: El tiempo de viaje entre la parada de autobús de origen y la parada de autobús de destino correspondiente a esta observación en formato HH:MM:SS (también se acepta HH:MM:SS, si la hora empieza por 0).  - `trip[object]`: Describe el viaje que realiza el vehículo correspondiente a esta observación. Igual que el campo 'trip' del mensaje GTFS Realtime-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  - `tripDetails[object]`: Un descriptor de la actualización en tiempo real del horario de un vehículo a lo largo de un viaje.  - `tripDirection[string]`: Indica la dirección en la que se desplaza el vehículo ENUM[UP,DN]  - `trip_delay[number]`: Puede ser positivo y negativo en segundos y muestra cuánto se desvía el vehículo del previsto. Igual que: Campo 'delay' de GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)  - `trip_details[object]`: Un descriptor de la actualización en tiempo real del horario de un vehículo a lo largo de un viaje.  - `trip_direction[string]`: Indica la dirección en la que se desplaza el vehículo. Es igual que el campo 'direction_id' de GTFS Realtime message-TripDescriptor: Campo 'direction_id' de GTFS Realtime message-TripDescriptor pero se representa en forma de ENUM[UP,DN] en lugar de [0,1] como se ve en 'direction_id' (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor).  - `trip_id[string]`: ID del viaje/nombre del viaje asignado al autobús correspondiente a esta observación, en consideración a la hora del día y a la dirección del viaje en el routeId dado. Igual que: Campo 'trip_id' del mensaje GTFS Realtime-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `trip_update[object]`: Describe la información sobre el viaje, como el retraso, las salidas, etc., de un viaje realizado por el vehículo correspondiente a esta observación. Igual que el campo "trip_update" de GTFS Realtime message-FeedEntity (https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity).  - `type[string]`: Tipo de entidad NGSI. Tiene que ser TransitManagement  - `uncertainty[number]`: Si se omite la incertidumbre, se interpreta como desconocida. Para especificar una predicción completamente segura, establezca su incertidumbre en 0.SameAs: campo 'uncertainty' de GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)  - `vehicleDesc[object]`: Describe la información adicional del vehículo correspondiente a esta observación. Igual que: campo "vehículo" del mensaje GTFS en tiempo real-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  - `vehicleType[string]`: Describe el tipo de vehículo que corresponde a esta observación, puede ser una tolva, un compactador, un volquete, un dumper en el caso de los vehículos de gestión de residuos sólidos, un minibús BRT, un autobús BRT, un autobús urbano en el caso de los vehículos ITMS, una ambulancia, un camión de bomberos, un furgón de policía, etc., en el caso de los vehículos de emergencia, y un ciclomotor, una motocicleta, un autocar, un coche privado o un coche Jeep, un coche de alquiler, un autobús, un ciclomotor, una motocicleta pública.  - `vehicle_id[string]`: ID único asignado al vehículo correspondiente a esta observación, utilizado en la identificación interna del sistema. Igual que: Campo "id" del mensaje en tiempo real GTFS-Descriptor de vehículo (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `vehicle_label[string]`: Etiqueta visible para el usuario, es decir, algo que debe mostrarse al pasajero para ayudarle a identificar el vehículo correcto. Igual que: campo 'label' de GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `vehicle_position[object]`: Describe la posición en tiempo real del vehículo correspondiente a esta observación. Igual que el campo "vehicle" de GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        type: Geoproperty    
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
## Ejemplo de carga útil  
#### TransitManagement NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un TransitManagement en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### TransitManagement NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de un TransitManagement en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### TransitManagement NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un TransitManagement en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
