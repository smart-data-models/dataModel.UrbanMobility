from __future__ import annotations

from datetime import time
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class AgencyInfo(BaseModel):
    agency_email: Optional[str] = Field(
        None,
        description="Email address actively monitored by the agency’s customer service department. SameAs: 'agency_email' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    agency_fare_url: Optional[str] = Field(
        None,
        description="URL of a web page that contains the details of the fares and also could allow to purchase tickets for that agency online. SameAs: 'agency_fare_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    agency_id: Optional[str] = Field(
        None,
        description="ID that uniquely identifies a transit agency. A transit feed may represent data from more than one agency. The agency_id is dataset unique. This field is optional for transit feeds that only contain data for a single agency. SameAs: 'agency_id' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    agency_lang: Optional[str] = Field(
        None,
        description="Contains a two-letter ISO 639-1 code for the primary language used by this transit agency. The language code is case-insensitive (both en and EN are accepted). SameAs: 'agency_lang' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    agency_name: Optional[str] = Field(
        None,
        description="The agency_name field contains the full name of the transit agency. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    agency_phone: Optional[str] = Field(
        None,
        description="A voice telephone number for the specified agency.SameAs: 'agency_phone' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    agency_timezone: Optional[str] = Field(
        None,
        description="Timezone field contains the timezone where the transit agency is located. SameAs: 'agency_timezone' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    agency_url: Optional[str] = Field(
        None,
        description="The agency_url field contains the URL of the transit agency. SameAs: 'agency_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )


class Arrival(BaseModel):
    uncertainty: Optional[float] = Field(
        None,
        description="If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)",
    )


class Departure(BaseModel):
    uncertainty: Optional[float] = Field(
        None,
        description="If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)",
    )


class ScheduleRelationship(Enum):
    SCHEDULED = 'SCHEDULED'
    ADDED = 'ADDED'
    UNSCHEDULED = 'UNSCHEDULED'
    CANCELED = 'CANCELED'


class Trip(BaseModel):
    direction_id: Optional[float] = None
    route_id: Optional[str] = None
    schedule_relationship: Optional[ScheduleRelationship] = None
    start_date: Optional[str] = None
    start_time: Optional[str] = None
    trip_id: Optional[str] = None


class TripUpdate(BaseModel):
    trip: Optional[Trip] = Field(
        None, description='Following the conventions of GTFS trip. '
    )


class DeviceModel(BaseModel):
    brandName: Optional[str] = Field(
        None,
        description='Name of the brand associated with an entity, e.g., sensor, device etc',
    )
    manufacturerName: Optional[str] = Field(
        None,
        description='Name of the manufacturer associated with an entity, e.g., sensor, device etc',
    )
    modelName: Optional[str] = Field(
        None,
        description='Name of a specific model associated with an entity, e.g., sensor, device etc',
    )
    modelURL: Optional[str] = Field(
        None,
        description='URL providing further information of a specific model associated with an entity, e.g., sensor, device etc',
    )
    observationDateTime: Optional[AwareDatetime] = Field(
        None, description='Last reported time of observation'
    )
    trip_update: Optional[TripUpdate] = Field(
        None,
        description="Describes the trip information like delay, departures, etc., for a trip made by the vehicle corresponding to this observation.SameAs:'trip_update' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)",
    )


class DeviceInfo(BaseModel):
    deviceBatteryStatus: Optional[str] = Field(
        None,
        description='Gives the Battery charging status of the reporting device(Connected, Disconnected)',
    )
    deviceID: Optional[str] = Field(
        None,
        description='Device ID of the physical sensor/ measurement station corresponding to this observation',
    )
    deviceModel: Optional[DeviceModel] = Field(
        None,
        description='Describes the information of the device, sensor or system in consideration',
    )
    deviceName: Optional[str] = Field(
        None,
        description='Device Name or Station name of the sensor device/station corresponding to this observation',
    )
    deviceSimNumber: Optional[str] = Field(
        None,
        description='Gives the sim number of the device in the waste management vehicle',
    )
    measurand: Optional[str] = Field(
        None, description='Property/properties sensed/observed/measured by the device'
    )
    rfID: Optional[str] = Field(None, description='Gives the ID of the RFID reader')


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Position(BaseModel):
    bearing: Optional[float] = Field(
        None,
        description='Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data',
    )
    latitude: Optional[float] = Field(
        None, description='Degrees North, in the WGS-84 coordinate system'
    )
    longitude: Optional[float] = Field(
        None, description='Degrees East, in the WGS-84 coordinate system'
    )
    odometer: Optional[float] = Field(None, description='Odometer value, in meters')
    speed: Optional[float] = Field(
        None,
        description='Momentary speed measured by the vehicle, in meters per second',
    )


class PositionInfo(BaseModel):
    bearing: Optional[float] = Field(
        None,
        description='Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data',
    )
    odometer: Optional[float] = Field(None, description='Odometer value')
    speed: Optional[float] = Field(
        None, description='Momentary speed measured by the vehicle'
    )


class RouteInfo(BaseModel):
    route_color: Optional[str] = Field(
        None,
        description="If assigned, this field defines a color that corresponds to a route. The color must be provided as a six-character hexadecimal number, for example, 00FFFF. If no color is specified, the default route color is white (FFFFFF). SameAs: 'route_color' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)",
    )
    route_desc: Optional[str] = Field(
        None,
        description="Description of the route. This can include the entire route details including to and from destination and timing information in a text description form. SameAs: 'route_desc' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)",
    )
    route_id: Optional[str] = Field(
        None,
        description='Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on',
    )
    route_long_name: Optional[str] = Field(
        None,
        description="Full name of a route. This name is more descriptive than the routeShortName and often includes the route's destination or stop. This mostly includes the to and from destination names of the route. SameAs: 'route_long_name' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)",
    )
    route_short_name: Optional[str] = Field(
        None,
        description="Short name of a route. This will often be the transit vehicle's board name like 402D, or Green that riders use to identify a route. SameAs: 'route_short_name' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)",
    )
    route_text_color: Optional[str] = Field(
        None,
        description="This field can be used to specify a legible color to use for text drawn against a background of route_color. The color must be provided as a six-character hexadecimal number, for example, FFD700. If no color is specified, the default text color is black (000000). SameAs: 'route_text_color' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)",
    )
    route_type: Optional[float] = Field(
        None,
        description="Number indicating the type of transport- 1 - Subway, Metro. Any underground rail system within a metropolitan area. 2 - Rail. Used for intercity or long-distance travel. 3 - Bus. Used for short- and long-distance bus routes. SameAs: 'route_type' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)",
    )
    route_url: Optional[str] = Field(
        None,
        description="Contains the URL of a web page about that particular route and is different from the agency_url. SameAs: 'route_url' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)",
    )


class ShapeInfo(BaseModel):
    shape_dist_traveled: Optional[float] = Field(
        None,
        description='Actual distance traveled along the shape from the first shape point to the point specified in this record. Used by trip planners to show the correct portion of the shape on a map. Values must increase along with shape_pt_sequence; they cannot be used to show reverse travel along a route. Distance units must be consistent with those used in stop_times.txt. Example: If a bus travels along the three points defined above for A_shp, the additional shape_dist_traveled values (shown here in kilometers) would look like this: shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled A_shp,37.61956,-122.48161,0,0 A_shp,37.64430,-122.41070,6,6.8310 A_shp,37.65863,-122.30839,11,15.8765',
    )
    shape_id: Optional[str] = Field(None, description='Identifies a shape')
    shape_pt_sequence: Optional[float] = Field(
        None,
        description="Sequence in which the shape points connect to form the shape. Values must increase along the trip but do not need to be consecutive. Example: If the shape 'A_shp' has three points in its definition, the shapes.txt file might contain these records to define the shape: shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence A_shp,37.61956,-122.48161,0 A_shp,37.64430,-122.41070,6 A_shp,37.65863,-122.30839,11",
    )


class StopInfo(BaseModel):
    stop_code: Optional[str] = Field(
        None,
        description="This field contains short text or a number that uniquely identifies the stop for passengers. Can be same as stop_id if it is for public. SameAs: 'stop_code' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)",
    )
    stop_desc: Optional[str] = Field(
        None,
        description="This field contains a description of a stop. SameAs: 'stop_desc' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)",
    )
    stop_id: Optional[str] = Field(
        None,
        description='Unique ID assigned to the stop corresponding to this observation',
    )
    stop_name: Optional[str] = Field(
        None,
        description="Describes the name of a stop or station. SameAs: 'stop_name' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)",
    )
    stop_url: Optional[str] = Field(
        None,
        description="This field contains the URL of a web page about a particular stop and is different from the agency_url and the route_url fields. SameAs: 'stop_url' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)",
    )


class StopTimeUpdateInfo(BaseModel):
    stopScheduleRelationship: Optional[str] = Field(
        None,
        description="Describes the relationship between the static schedule and the stop. SameAs: 'schedule_relationship' field from GTFS Realtime message-StopTimeUpdate ENUM[SCHEDULED, SKIPPED, NO_DATA] (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)",
    )
    stop_id: Optional[str] = Field(
        None,
        description='Unique ID assigned to the stop corresponding to this observation',
    )
    stop_sequence: Optional[float] = Field(
        None,
        description='This field identifies the order of the stops for a particular trip. The values for stop_sequence must be non-negative integers, and they must increase along the trip. For example, the first stop on the trip could have a stop_sequence of 1, the second stop on the trip could have a stop_sequence of 23, the third stop could have a stop_sequence of 40, and so on',
    )


class StopTimesInfo(BaseModel):
    arrival_time: Optional[time] = Field(
        None,
        description="Specifies the arrival time at a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'arrival_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)",
    )
    continuous_drop_off: Optional[float] = Field(
        None,
        description="Indicates whether a rider can alight from the transit vehicle at any point along the vehicle’s travel path.SameAs: 'continuous_drop_off' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)",
    )
    continuous_pickup: Optional[float] = Field(
        None,
        description="Indicates whether a rider can board the transit vehicle at any point along the vehicle’s travel path.SameAs: 'continuous_pickup' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)",
    )
    departure_time: Optional[time] = Field(
        None,
        description="Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)",
    )
    drop_off_type: Optional[str] = Field(
        None,
        description="Indicates drop off method. SameAs: 'drop_off_type' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)",
    )
    pickup_type: Optional[str] = Field(
        None,
        description="Indicates pickup method.SameAs: 'pickup_type' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)",
    )
    stop_headsign: Optional[str] = Field(
        None,
        description="This field contains the text that appears on a sign that identifies the trip’s destination to passengers. SameAs: 'stop_headsign' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)",
    )
    stop_id: Optional[str] = Field(
        None,
        description='Unique ID assigned to the stop corresponding to this observation',
    )
    stop_sequence: Optional[float] = Field(
        None,
        description='This field identifies the order of the stops for a particular trip. The values for stop_sequence must be non-negative integers, and they must increase along the trip. For example, the first stop on the trip could have a stop_sequence of 1, the second stop on the trip could have a stop_sequence of 23, the third stop could have a stop_sequence of 40, and so on',
    )
    trip_id: Optional[str] = Field(
        None,
        description='Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId',
    )


class StopSequenceDetail(BaseModel):
    stop_id: Optional[str] = Field(
        None,
        description='Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty',
    )
    stop_sequence: Optional[float] = Field(
        None,
        description='Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for',
    )


class ScheduleRelationship1(Enum):
    SCHEDULED = 'SCHEDULED'
    SKIPPED = 'SKIPPED'
    NO_DATA = 'NO_DATA'


class StopTimeUpdate(BaseModel):
    arrival: Optional[Arrival] = Field(
        None,
        description='If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty',
    )
    departure: Optional[Departure] = Field(
        None,
        description='If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty',
    )
    schedule_relationship: Optional[ScheduleRelationship1] = Field(
        None,
        description="Enum:'SCHEDULED, SKIPPED, NO_DATA'. SCHEDULED means that the vehicle is proceeding in accordance with its static schedule of stops, although not necessarily according to the times of the schedule. This is the default behavior. At least one of arrival and departure must be provided. SKIPPED means that The stop is skipped, i.e., the vehicle will not stop at this stop. The arrival and departure fields are optional. NO_DATA means that no data is given for this stop. It indicates that there is no realtime information available. When set NO_DATA is propagated through subsequent stops so this is the recommended way of specifying from which stop you do not have realtime information. When NO_DATA is set neither arrival nor departure should be supplied",
    )
    stop_id: Optional[str] = Field(
        None,
        description='Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty',
    )
    stop_sequence: Optional[float] = Field(
        None,
        description='Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for',
    )


class Trip1(BaseModel):
    direction_id: Optional[float] = Field(
        None,
        description="Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    route_id: Optional[str] = Field(
        None,
        description="Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    schedule_relationship: Optional[str] = Field(
        None,
        description="Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)",
    )
    start_date: Optional[str] = Field(
        None,
        description="Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    start_time: Optional[str] = Field(
        None,
        description="Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    trip_id: Optional[str] = Field(
        None,
        description="Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )


class TripDetails(BaseModel):
    arrival_time: Optional[time] = Field(
        None,
        description=" Specifies the arrival time at a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'arrival_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)",
    )
    departure_time: Optional[time] = Field(
        None,
        description="Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)",
    )
    stop_headsign: Optional[str] = Field(
        None,
        description="This field contains the text that appears on a sign that identifies the trip’s destination to passengers. SameAs: 'stop_headsign' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)",
    )
    stop_id: Optional[str] = Field(
        None,
        description="Stop ID/Stop name of the bus stops corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    stop_sequence: Optional[float] = Field(
        None,
        description="Indicates the stop sequence of the vehicle corresponding to this observation, can be referenced from the GTFS static feed stop_times.txt. SameAs: 'stop_sequence' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)",
    )


class TripInfo(BaseModel):
    route_id: Optional[str] = Field(
        None,
        description='Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on',
    )
    schedule_relationship: Optional[str] = Field(
        None,
        description="Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from GTFS Realtime message-TripDescriptor ENUM[SCHEDULED, ADDED, UNSCHEDULED, CANCELED] (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    start_date: Optional[str] = Field(
        None,
        description="Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    start_time: Optional[time] = Field(
        None,
        description="Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    trip_direction: Optional[str] = Field(
        None,
        description="Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    trip_id: Optional[str] = Field(
        None,
        description='Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId',
    )


class TripDetails1(BaseModel):
    bearing: Optional[float] = Field(
        None,
        description='Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data',
    )
    odometer: Optional[float] = Field(None, description='Odometer value, in meters')
    speed: Optional[float] = Field(
        None,
        description='Momentary speed measured by the vehicle, in meters per second',
    )


class StopTimeUpdate1(BaseModel):
    arrival: Optional[Arrival] = Field(
        None,
        description='If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty',
    )
    departure: Optional[Departure] = Field(
        None,
        description='If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty',
    )
    schedule_relationship: Optional[ScheduleRelationship1] = Field(
        None,
        description="Enum:'SCHEDULED, SKIPPED, NO_DATA'. SCHEDULED means that the vehicle is proceeding in accordance with its static schedule of stops, although not necessarily according to the times of the schedule. This is the default behavior. At least one of arrival and departure must be provided. SKIPPED means that The stop is skipped, i.e., the vehicle will not stop at this stop. The arrival and departure fields are optional. NO_DATA means that no data is given for this stop. It indicates that there is no realtime information available. When set NO_DATA is propagated through subsequent stops so this is the recommended way of specifying from which stop you do not have realtime information. When NO_DATA is set neither arrival nor departure should be supplied",
    )
    stop_id: Optional[str] = Field(
        None,
        description='Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty',
    )
    stop_sequence: Optional[float] = Field(
        None,
        description='Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for',
    )


class VehicleDesc(BaseModel):
    license_plate: Optional[str] = Field(
        None,
        description="Gives the License Plate number of the vehice.SameAs: 'license_plate' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)",
    )
    vehicle_id: Optional[str] = Field(
        None,
        description="Unique ID assigned to the vehicle corresponding to this observation,used in internal system identification.SameAs: 'id' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)",
    )
    vehicle_label: Optional[str] = Field(
        None,
        description="User visible label,i.e.,something that must be shown to the passenger to help identify the correct vehicle.SameAs: 'label' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)",
    )


class TripUpdate1(BaseModel):
    stop_time_update: Optional[StopTimeUpdate1] = Field(
        None,
        description='Additional information on the vehicle that is serving this trip',
    )
    timestamp: Optional[AwareDatetime] = Field(
        None,
        description="Last reported time of observation from the vehicle. SameAs: 'timestamp' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    trip: Optional[Trip1] = Field(
        None,
        description="Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)",
    )
    vehicleDesc: Optional[VehicleDesc] = Field(
        None,
        description="Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)",
    )


class Type6(Enum):
    TransitManagement = 'TransitManagement'


class VehicleInfo(BaseModel):
    license_plate: Optional[str] = Field(
        None,
        description="Gives the License Plate number of the vehice. SameAs: 'license_plate' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)",
    )
    vehicleID: Optional[str] = Field(
        None,
        description="Unique ID assigned to the vehicle corresponding to this observation, used in internal system identification. SameAs: 'id' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)",
    )
    vehicle_label: Optional[str] = Field(
        None,
        description="User visible label, i.e., something that must be shown to the passenger to help identify the correct vehicle. SameAs: 'label' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)",
    )


class AgencyInfo1(BaseModel):
    agency_email: Optional[str] = Field(
        None,
        description="Email address actively monitored by the agency’s customer service department. SameAs: 'agency_email' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt).",
    )
    agency_fare_url: Optional[str] = Field(
        None,
        description="URL of a web page that contains the details of the fares and also could allow to purchase tickets for that agency online. SameAs: 'agency_fare_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt).",
    )
    agency_id: Optional[str] = Field(
        None,
        description="ID that uniquely identifies a transit agency. A transit feed may represent data from more than one agency. The agency_id is dataset unique. This field is optional for transit feeds that only contain data for a single agency. SameAs: 'agency_id' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt).",
    )
    agency_lang: Optional[str] = Field(
        None,
        description="Contains a two-letter ISO 639-1 code for the primary language used by this transit agency. The language code is case-insensitive (both en and EN are accepted). SameAs: 'agency_lang' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt).",
    )
    agency_name: Optional[str] = Field(
        None,
        description="The agency_name field contains the full name of the transit agency. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt).",
    )
    agency_phone: Optional[str] = Field(
        None,
        description="A voice telephone number for the specified agency.SameAs: 'agency_phone' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt).",
    )
    agency_timezone: Optional[str] = Field(
        None,
        description="Timezone field contains the timezone where the transit agency is located. SameAs: 'agency_timezone' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt).",
    )
    agency_url: Optional[str] = Field(
        None,
        description="The agency_url field contains the URL of the transit agency. SameAs: 'agency_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt).",
    )


class PositionInfo1(BaseModel):
    bearing: Optional[float] = Field(
        None,
        description='Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data',
    )
    odometer: Optional[float] = Field(None, description='Odometer value.')
    speed: Optional[float] = Field(
        None, description='Momentary speed measured by the vehicle.'
    )


class StopInfo1(BaseModel):
    stop_code: Optional[str] = Field(
        None,
        description="This field contains short text or a number that uniquely identifies the stop for passengers. Can be same as stop_id if it is for public. SameAs: 'stop_code' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt).",
    )
    stop_desc: Optional[str] = Field(
        None,
        description="This field contains a description of a stop. SameAs: 'stop_desc' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt).",
    )
    stop_id: Optional[str] = Field(
        None,
        description='Unique ID assigned to the stop corresponding to this observation.',
    )
    stop_name: Optional[str] = Field(
        None,
        description="Describes the name of a stop or station. SameAs: 'stop_name' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt).",
    )
    stop_url: Optional[str] = Field(
        None,
        description="This field contains the URL of a web page about a particular stop and is different from the agency_url and the route_url fields. SameAs: 'stop_url' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt).",
    )


class StopTimesInfo1(BaseModel):
    arrival_time: Optional[time] = Field(
        None,
        description="Specifies the arrival time at a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'arrival_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt).",
    )
    continuous_drop_off: Optional[float] = Field(
        None,
        description="Indicates whether a rider can alight from the transit vehicle at any point along the vehicle’s travel path.SameAs: 'continuous_drop_off' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt).",
    )
    continuous_pickup: Optional[float] = Field(
        None,
        description="Indicates whether a rider can board the transit vehicle at any point along the vehicle’s travel path.SameAs: 'continuous_pickup' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt).",
    )
    departure_time: Optional[time] = Field(
        None,
        description="Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt).",
    )
    drop_off_type: Optional[str] = Field(
        None,
        description="Indicates drop off method. SameAs: 'drop_off_type' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt).",
    )
    pickup_type: Optional[str] = Field(
        None,
        description="Indicates pickup method.SameAs: 'pickup_type' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt).",
    )
    stop_headsign: Optional[str] = Field(
        None,
        description="This field contains the text that appears on a sign that identifies the trip’s destination to passengers. SameAs: 'stop_headsign' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt).",
    )
    stop_id: Optional[str] = Field(
        None,
        description='Unique ID assigned to the stop corresponding to this observation.',
    )
    stop_sequence: Optional[float] = Field(
        None,
        description='This field identifies the order of the stops for a particular trip. The values for stop_sequence must be non-negative integers, and they must increase along the trip. For example, the first stop on the trip could have a stop_sequence of 1, the second stop on the trip could have a stop_sequence of 23, the third stop could have a stop_sequence of 40, and so on.',
    )
    trip_id: Optional[str] = Field(
        None,
        description='Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId.',
    )


class TripInfo1(BaseModel):
    route_id: Optional[str] = Field(
        None,
        description='Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on.',
    )
    schedule_relationship: Optional[str] = Field(
        None,
        description="Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from GTFS Realtime message-TripDescriptor ENUM[SCHEDULED, ADDED, UNSCHEDULED, CANCELED] (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor).",
    )
    start_date: Optional[str] = Field(
        None,
        description="Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor).",
    )
    start_time: Optional[time] = Field(
        None,
        description="Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor).",
    )
    trip_direction: Optional[str] = Field(
        None,
        description="Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor).",
    )
    trip_id: Optional[str] = Field(
        None,
        description='Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId.',
    )


class VehicleInfo1(BaseModel):
    license_plate: Optional[str] = Field(
        None,
        description="Gives the License Plate number of the vehice. SameAs: 'license_plate' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor).",
    )
    vehicleID: Optional[str] = Field(
        None,
        description="Unique ID assigned to the vehicle corresponding to this observation, used in internal system identification. SameAs: 'id' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor).",
    )
    vehicle_label: Optional[str] = Field(
        None,
        description="User visible label, i.e., something that must be shown to the passenger to help identify the correct vehicle. SameAs: 'label' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor).",
    )


class VehiclePositionInfo(BaseModel):
    actual_trip_start_time: Optional[AwareDatetime] = Field(
        None,
        description="This field specifies the time at which service actually began. This is SameAs: absolute 'time'(StopTimeEvent) in the 'arrival' field of the stop_time_update (StopTimeUpdate) message of the GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate).",
    )
    agencyInfo: Optional[AgencyInfo1] = Field(
        None, description='Agency information corresponding to this observation.'
    )
    arrivalUncertainty: Optional[float] = Field(
        None,
        description="If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'arrival' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate).",
    )
    congestion_level: Optional[str] = Field(
        None,
        description='Describes the congestion level that is affecting this vehicle. ENUM [UNKNOWN_CONGESTION_LEVEL, RUNNING_SMOOTHLY, STOP_AND_GO, CONGESTION, SEVERE_CONGESTION]',
    )
    current_status: Optional[str] = Field(
        None,
        description="Describes the status of the vehicle w.r.t the stop corresponding to this observation ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. SameAs:'current_status' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    current_stop_sequence: Optional[float] = Field(
        None,
        description="Gives the stop sequence index of the current stop. This is determined by considering current_status, if current_status is missing IN_TRANSIT_TO is assumed. SameAs:'current_stop_sequence' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    departureUncertainty: Optional[float] = Field(
        None,
        description="If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'departure' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate).",
    )
    depotID: Optional[str] = Field(
        None,
        description='Describes the unique id of the bus depot corresponding to this observation.',
    )
    depotName: Optional[str] = Field(
        None,
        description='Describes the depot name of the bus depot corresponding to this observation.',
    )
    entity_id: Optional[str] = Field(
        None,
        description="Feed unique ID for the entity corresponding to this observation.SameAs:'entity_id' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)",
    )
    occupancy_status: Optional[str] = Field(
        None,
        description='The degree of passenger occupancy for the vehicle. ENUM [EMPTY, MANY_SEATS_AVAILABLE, FEW_SEATS_AVAILABLE, STANDING_ROOM_ONLY, CRUSHED_STANDING_ROOM_ONLY, FULL, NOT_ACCEPTING_PASSENGERS, NO_DATA_AVAILABLE, NOT_BOARDABLE]',
    )
    positionInfo: Optional[PositionInfo1] = Field(
        None,
        description="Describes the current position of the vehicle corresponding to this observation. SameAs:'position' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition).",
    )
    route_id: Optional[str] = Field(
        None,
        description="Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor).",
    )
    stopInfo: Optional[StopInfo1] = Field(
        None,
        description='Information about the path the vehicle corresponding to this observation travels along.',
    )
    stopTimesInfo: Optional[StopTimesInfo1] = Field(
        None,
        description='A descriptor of realtime update on the schedule of a vehicle along a trip.',
    )
    stop_id: Optional[str] = Field(
        None,
        description='Unique ID assigned to the stop corresponding to this observation',
    )
    travelDistance: Optional[float] = Field(
        None,
        description='The distance between the origin location and the destination location or the total distance travelled corresponding to this observation.',
    )
    tripInfo: Optional[TripInfo1] = Field(
        None,
        description="Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition).",
    )
    vehicleInfo: Optional[VehicleInfo1] = Field(
        None,
        description="Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)",
    )


class VehicleType(Enum):
    agriculturalVehicle = 'agriculturalVehicle'
    ambulance = 'ambulance'
    anyVehicle = 'anyVehicle'
    articulatedVehicle = 'articulatedVehicle'
    autorickshaw = 'autorickshaw'
    bicycle = 'bicycle'
    binTrolley = 'binTrolley'
    BRT_mini_bus_ = 'BRT mini bus·'
    BRT_bus = 'BRT bus'
    bus = 'bus'
    car = 'car'
    caravan = 'caravan'
    carOrLightVehicle = 'carOrLightVehicle'
    carWithCaravan = 'carWithCaravan'
    carWithTrailer = 'carWithTrailer'
    cleaningTrolley = 'cleaningTrolley'
    compactor = 'compactor'
    constructionOrMaintenanceVehicle = 'constructionOrMaintenanceVehicle'
    dumper = 'dumper'
    e_moped = 'e-moped'
    e_scooter = 'e-scooter'
    e_motorcycle = 'e-motorcycle'
    fireTender = 'fireTender'
    fourWheelDrive = 'fourWheelDrive'
    highSidedVehicle = 'highSidedVehicle'
    hopper = 'hopper'
    lorry = 'lorry'
    minibus = 'minibus'
    moped = 'moped'
    motorcycle = 'motorcycle'
    motorcycleWithSideCar = 'motorcycleWithSideCar'
    motorscooter = 'motorscooter'
    policeVan = 'policeVan'
    publicMotor = 'publicMotor'
    sweepingMachine = 'sweepingMachine'
    tanker = 'tanker'
    tempo = 'tempo'
    threeWheeledVehicle = 'threeWheeledVehicle'
    tipper = 'tipper'
    trailer = 'trailer'
    tram = 'tram'
    trolley = 'trolley'
    twoWheeledVehicle = 'twoWheeledVehicle'
    van = 'van'
    vehicleWithoutCatalyticConverter = 'vehicleWithoutCatalyticConverter'
    vehicleWithCaravan = 'vehicleWithCaravan'
    vehicleWithTrailer = 'vehicleWithTrailer'
    withEvenNumberedRegistrationPlates = 'withEvenNumberedRegistrationPlates'
    withOddNumberedRegistrationPlates = 'withOddNumberedRegistrationPlates'
    other = 'other'


class VehiclePosition(BaseModel):
    current_status: Optional[str] = Field(
        None,
        description="Describes the status of the vehicle w.r.t the stop corresponding to this observation ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. SameAs:'current_status' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    current_stop_sequence: Optional[float] = Field(
        None,
        description="Gives the stop sequence index of the current stop. This is determined by considering current_status, if current_status is missing IN_TRANSIT_TO is assumed. SameAs:'current_stop_sequence' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    position: Optional[Position] = Field(
        None,
        description="Describes the current position of the vehicle corresponding to this observation. SameAs: 'position' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    stop_id: Optional[str] = Field(
        None,
        description="Stop ID/Stop name of the bus stops corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    timestamp: Optional[AwareDatetime] = Field(
        None,
        description="Last reported time of observation from the vehicle. SameAs:  'timestamp' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    trip: Optional[Trip1] = Field(
        None,
        description="Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)",
    )
    vehicleDesc: Optional[VehicleDesc] = Field(
        None,
        description="Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)",
    )


class TransitManagement(BaseModel):
    acAvailable: Optional[str] = Field(
        None,
        description='Describes the presence of air conditioning option in the vehicle corresponding to this observation',
    )
    ac_available: Optional[str] = Field(
        None,
        description='Describes the presence of air conditioning option in the vehicle corresponding to this observation',
    )
    actual_trip_end_time: Optional[AwareDatetime] = Field(
        None,
        description='This field specifies the time at which service or trip corresponding to this observation is scheduled to end',
    )
    actual_trip_start_time: Optional[AwareDatetime] = Field(
        None,
        description="This field specifies the time at which service actually began.  This is SameAs: absolute 'time'(StopTimeEvent) in the 'arrival' field of the stop_time_update (StopTimeUpdate) message of the GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)",
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    agencyInfo: Optional[AgencyInfo] = Field(
        None, description='Agency information corresponding to this observation'
    )
    agency_fare_url: Optional[str] = Field(
        None,
        description="URL of a web page that contains the details of the fares and also could allow to purchase tickets for that agency online. SameAs: 'agency_fare_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    agency_id: Optional[str] = Field(
        None,
        description="ID that uniquely identifies a transit agency. A transit feed may represent data from more than one agency. The agency_id is dataset unique. This field is optional for transit feeds that only contain data for a single agency. SameAs: 'agency_id' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    agency_lang: Optional[str] = Field(
        None,
        description="Contains a two-letter ISO 639-1 code for the primary language used by this transit agency. The language code is case-insensitive (both en and EN are accepted). SameAs: 'agency_lang' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    agency_name: Optional[str] = Field(
        None,
        description="The agency_name field contains the full name of the transit agency. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    agency_timezone: Optional[str] = Field(
        None,
        description="Timezone field contains the timezone where the transit agency is located. SameAs: 'agency_timezone' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    agency_url: Optional[str] = Field(
        None,
        description="The agency_url field contains the URL of the transit agency. SameAs: 'agency_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)",
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    arrival: Optional[Arrival] = Field(
        None,
        description="If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'arrival' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)",
    )
    arrivalUncertainty: Optional[float] = Field(
        None,
        description="If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'arrival' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)",
    )
    arrival_time: Optional[time] = Field(
        None,
        description="Specifies the arrival time at a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'arrival_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)",
    )
    bearing: Optional[float] = Field(
        None,
        description="Gives the vehicle GPS angle measured in a clockwise direction from the True North. SameAs 'bearing' field from GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)",
    )
    current_status: Optional[str] = Field(
        None,
        description="Describes the status of the vehicle w.r.t the stop corresponding to this observation ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. SameAs:'current_status' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    current_stop_sequence: Optional[float] = Field(
        None,
        description="Gives the stop sequence index of the current stop. This is determined by considering current_status, if current_status is missing IN_TRANSIT_TO is assumed. SameAs:'current_stop_sequence' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    dataDescriptor: Optional[AnyUrl] = Field(
        None, description='URI pointing to the data-descriptor entity'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    departure: Optional[Departure] = Field(
        None,
        description="If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'departure' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)",
    )
    departureUncertainty: Optional[float] = Field(
        None,
        description="If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'departure' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)",
    )
    departure_time: Optional[time] = Field(
        None,
        description="Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). \nNote: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)",
    )
    depotID: Optional[str] = Field(
        None,
        description='Describes the unique id of the bus depot corresponding to this observation',
    )
    depotName: Optional[str] = Field(
        None,
        description='Describes the depot name of the bus depot corresponding to this observation',
    )
    depot_id: Optional[str] = Field(
        None,
        description='Describes the unique id of the bus depot corresponding to this observation',
    )
    depot_name: Optional[str] = Field(
        None,
        description='Describes the depot name of the bus depot corresponding to this observation',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    deviceInfo: Optional[DeviceInfo] = Field(
        None,
        description='Information about the device associated with the observations',
    )
    direction_id: Optional[float] = Field(
        None,
        description="Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    entity_id: Optional[str] = Field(
        None,
        description="Feed unique ID for the entity corresponding to this observation.SameAs:'entity_id' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)",
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    last_stop_arrival_time: Optional[time] = Field(
        None,
        description="Specifies the arrival time at the previous stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (H:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. This is SameAs: absolute 'time'(StopTimeEvent) in the 'arrival' field of the stop_time_update (StopTimeUpdate) message of the GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)",
    )
    last_stop_id: Optional[str] = Field(
        None,
        description="Stop ID/Stop name of the previous bus stop corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-VehiclePosition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    last_tracked_time: Optional[AwareDatetime] = Field(
        None, description='Gives the time at which the vehicle was last tracked'
    )
    license_plate: Optional[str] = Field(
        None,
        description="Gives the License Plate number of the vehicle. SameAs: 'license_plate' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)",
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    observationDateTime: Optional[AwareDatetime] = Field(
        None, description='Last reported time of observation'
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    position: Optional[Position] = Field(
        None,
        description='Describes the current position of the vehicle corresponding to this observation. SameAs: position field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)',
    )
    positionInfo: Optional[PositionInfo] = Field(
        None,
        description="Describes the current position of the vehicle corresponding to this observation. SameAs:'position' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    routeInfo: Optional[RouteInfo] = Field(
        None,
        description="Updated sorted stop sequence for the trip made by the vehicle corresponding to this observation, not to be considered if schedule_relationship is 'CANCELED'. SameAs: 'stop_time_update' field from GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)",
    )
    routeStopSequence: Optional[List[str]] = Field(
        None,
        description='Gives the stop ids/stop codes or station ids/station codes in the right sequence for the route or line or trip corresponding to this observation',
    )
    route_color: Optional[str] = Field(
        None,
        description="If assigned, this field defines a color that corresponds to a route. The color must be provided as a six-character hexadecimal number, for example, 00FFFF. If no color is specified, the default route color is white (FFFFFF). SameAs: 'route_color' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)",
    )
    route_desc: Optional[str] = Field(
        None,
        description="Description of the route. This can include the entire route details including to and from destination and timing information in a text description form. SameAs: 'route_desc' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)",
    )
    route_id: Optional[str] = Field(
        None,
        description="Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    route_long_name: Optional[str] = Field(
        None,
        description="Full name of a route. This name is more descriptive than the routeShortName and often includes the route's destination or stop. This mostly includes the to and from destination names of the route. SameAs: 'route_long_name' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)",
    )
    route_short_name: Optional[str] = Field(
        None,
        description="Short name of a route. This will often be the transit vehicle's board name like '402D',  or 'Green' that riders use to identify a route. SameAs: 'route_short_name' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)",
    )
    route_text_color: Optional[str] = Field(
        None,
        description="This field can be used to specify a legible color to use for text drawn against a background of route_color. The color must be provided as a six-character hexadecimal number, for example, FFD700. If no color is specified, the default text color is black (000000). SameAs: 'route_text_color' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)",
    )
    route_type: Optional[str] = Field(
        None,
        description="Number indicating the type of transport-1 - Subway, Metro. Any underground rail system within a metropolitan area.2 - Rail. Used for intercity or long-distance travel.3 - Bus. Used for short- and long-distance bus routes. SameAs: 'route_type' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)",
    )
    route_url: Optional[str] = Field(
        None,
        description="Contains the URL of a web page about that particular route and is different from the agency_url. SameAs: 'route_url' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)",
    )
    schedule_relationship: Optional[str] = Field(
        None,
        description="Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)",
    )
    seating_capacity: Optional[float] = Field(
        None,
        description='Describes the passenger seating capacity of the vehicle corresponding to this observation',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    shapeInfo: Optional[ShapeInfo] = Field(
        None,
        description='Information about the path the vehicle corresponding to this observation travels along',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    speed: Optional[float] = Field(
        None,
        description="Gives the Speed  of the vehicle. SameAs 'speed' field from GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)",
    )
    standingCapacity: Optional[float] = Field(
        None,
        description='Describes the passenger standing capacity of the vehicle corresponding to this observation.',
    )
    standing_capacity: Optional[float] = Field(
        None,
        description='Describes the passenger standing capacity of the vehicle corresponding to this observation',
    )
    start_date: Optional[str] = Field(
        None,
        description="Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    start_time: Optional[time] = Field(
        None,
        description="Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    stopInfo: Optional[StopInfo] = Field(
        None,
        description='Information about the path the vehicle corresponding to this observation travels along',
    )
    stopTimeUpdateInfo: Optional[StopTimeUpdateInfo] = Field(
        None,
        description="Updated sorted stop sequence for the trip made by the vehicle corresponding to this observation, not to be considered if schedule_relationship is 'CANCELED'. SameAs: 'stop_time_update' field from GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)",
    )
    stopTimesInfo: Optional[StopTimesInfo] = Field(
        None,
        description='A descriptor of realtime update on the schedule of a vehicle along a trip',
    )
    stop_code: Optional[str] = Field(
        None,
        description="This field contains short text or a number that uniquely identifies the stop for passengers. Can be same as stop_id if it is for public. SameAs: 'stop_code' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)",
    )
    stop_desc: Optional[str] = Field(
        None,
        description="This field contains a description of a stop. SameAs: 'stop_desc' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)",
    )
    stop_headsign: Optional[str] = Field(
        None,
        description="This field contains the text that appears on a sign that identifies the trip’s destination to passengers. SameAs: 'stop_headsign' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)",
    )
    stop_id: Optional[str] = Field(
        None,
        description="Stop ID/Stop name of the bus stops corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    stop_name: Optional[str] = Field(
        None,
        description="Describes the name of the Bus Stop. SameAs: 'stop_name' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)",
    )
    stop_sequence: Optional[float] = Field(
        None,
        description="Indicates the stop sequence of the vehicle corresponding to this observation, can be referenced from the GTFS static feed stop_times.txt. SameAs: 'stop_sequence' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)",
    )
    stop_sequence_detail: Optional[StopSequenceDetail] = Field(
        None,
        description="Describes the stop sequence for a trip in the designated route made by the public transit vehicle.SameAs: 'stop_sequence' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)",
    )
    stop_time_update: Optional[StopTimeUpdate] = Field(
        None,
        description='Additional information on the vehicle that is serving this trip',
    )
    stop_url: Optional[str] = Field(
        None,
        description="This field contains the URL of a web page about a particular stop and is different from the agency_url and the route_url fields. SameAs: 'stop_url' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)",
    )
    timestamp: Optional[AwareDatetime] = Field(
        None,
        description="Last reported time of observation from the vehicle. SameAs: 'timestamp' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    travelDistance: Optional[float] = Field(
        None,
        description='The distance between the origin bus stop and the destination bus stop or the total distance travelled corresponding to this observation',
    )
    travelTime: Optional[time] = Field(
        None,
        description='The time taken to travel between the origin location and the destination location corresponding to this observation in HH:MM:SS format(HH:MM:SS is also accepted, if the hour begins with 0)',
    )
    trip: Optional[Trip1] = Field(
        None,
        description="Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)",
    )
    tripDetails: Optional[TripDetails] = Field(
        None,
        description='A descriptor of realtime update on the schedule of a vehicle along a trip',
    )
    tripDirection: Optional[str] = Field(
        None,
        description='Gives the direction in which the vehicle is travelling in ENUM[UP,DN]',
    )
    tripInfo: Optional[TripInfo] = Field(
        None,
        description="Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)",
    )
    trip_delay: Optional[float] = Field(
        None,
        description="This can be positive and negative in seconds and shows how much the vehicle deviates from the planned one. SameAs: 'delay' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)",
    )
    trip_details: Optional[TripDetails1] = Field(
        None,
        description='A descriptor of realtime update on the schedule of a vehicle along a trip',
    )
    trip_direction: Optional[str] = Field(
        None,
        description="Gives the direction in which the vehicle is travelling. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor but is represented in the form of an ENUM[UP,DN] in place of [0,1] as seen in 'direction_id' (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    trip_id: Optional[str] = Field(
        None,
        description="Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)",
    )
    trip_update: Optional[TripUpdate1] = Field(
        None,
        description="Describes the trip information like delay, departures, etc., for a trip made by the vehicle corresponding to this observation.SameAs:'trip_update' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)",
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be TransitManagement'
    )
    uncertainty: Optional[float] = Field(
        None,
        description="If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)",
    )
    vehicleDesc: Optional[VehicleDesc] = Field(
        None,
        description="Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)",
    )
    vehicleInfo: Optional[VehicleInfo] = Field(
        None,
        description="Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)",
    )
    vehiclePositionInfo: Optional[VehiclePositionInfo] = Field(
        None,
        description="Describes the realtime position of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)",
    )
    vehicleType: Optional[VehicleType] = Field(
        None,
        description='Describes the type of vehicle corresponding to this observation, could be hopper, compactor, tipper, dumper in case of solid waste management vehicles, BRT mini bus, BRT bus, city bus in case of ITMS vehicles, Ambulance, Fire tender, Police van etc, in case of emergency vehicles and Moped/Scooter, Motor Cycle,  Autorickshaw, Private car/ Jeep car, Tempo, Bus, E-Moped/E-Scooter/E-Motor Cycle, Public motor in case of vehicle registration',
    )
    vehicle_id: Optional[str] = Field(
        None,
        description="Unique ID assigned to the vehicle corresponding to this observation, used in internal system identification. SameAs: 'id' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)",
    )
    vehicle_label: Optional[str] = Field(
        None,
        description="User visible label, i.e., something that must be shown to the passenger to help identify the correct vehicle. SameAs: 'label' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)",
    )
    vehicle_position: Optional[VehiclePosition] = Field(
        None,
        description="Describes the realtime position of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)",
    )
