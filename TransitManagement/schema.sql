/* (Beta) Export of data model TransitManagement of the subject dataModel.UrbanMobility for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE TransitManagement_type AS ENUM ('TransitManagement');CREATE TYPE vehicleType_type AS ENUM ('agriculturalVehicle','ambulance','anyVehicle','articulatedVehicle','autorickshaw','bicycle','binTrolley','BRT mini bus·','BRT bus','bus','car','caravan','carOrLightVehicle','carWithCaravan','carWithTrailer','cleaningTrolley','compactor','constructionOrMaintenanceVehicle','dumper','e-moped','e-scooter','e-motorcycle','fireTender','fourWheelDrive','highSidedVehicle','hopper','lorry','minibus','moped','motorcycle','motorcycleWithSideCar','motorscooter','policeVan','publicMotor','sweepingMachine','tanker','tempo','threeWheeledVehicle','tipper','trailer','tram','trolley','twoWheeledVehicle','van','vehicleWithoutCatalyticConverter','vehicleWithCaravan','vehicleWithTrailer','withEvenNumberedRegistrationPlates','withOddNumberedRegistrationPlates','other');
CREATE TABLE TransitManagement (acAvailable TEXT, ac_available TEXT, actual_trip_end_time TIMESTAMP, actual_trip_start_time TIMESTAMP, address JSON, agencyInfo JSON, agency_fare_url TEXT, agency_id TEXT, agency_lang TEXT, agency_name TEXT, agency_timezone TEXT, agency_url TEXT, alternateName TEXT, areaServed TEXT, arrival JSON, arrivalUncertainty NUMERIC, arrival_time TIME, bearing NUMERIC, current_status TEXT, current_stop_sequence NUMERIC, dataDescriptor TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, departure JSON, departureUncertainty NUMERIC, departure_time TIME, depotID TEXT, depotName TEXT, depot_id TEXT, depot_name TEXT, description TEXT, deviceInfo JSON, direction_id NUMERIC, entity_id TEXT, id TEXT PRIMARY KEY, last_stop_arrival_time TIME, last_stop_id TEXT, last_tracked_time TIMESTAMP, license_plate TEXT, location JSON, name TEXT, observationDateTime TIMESTAMP, owner JSON, position JSON, positionInfo JSON, routeInfo JSON, routeStopSequence JSON, route_color TEXT, route_desc TEXT, route_id TEXT, route_long_name TEXT, route_short_name TEXT, route_text_color TEXT, route_type TEXT, route_url TEXT, schedule_relationship TEXT, seating_capacity NUMERIC, seeAlso JSON, shapeInfo JSON, source TEXT, speed NUMERIC, standing_capacity NUMERIC, start_date TEXT, start_time TIME, stopInfo JSON, stopTimeUpdateInfo JSON, stopTimesInfo JSON, stop_code TEXT, stop_desc TEXT, stop_headsign TEXT, stop_id TEXT, stop_name TEXT, stop_sequence NUMERIC, stop_sequence_detail JSON, stop_time_update JSON, stop_url TEXT, timestamp TIMESTAMP, travelDistance NUMERIC, travelTime TIME, trip JSON, tripDetails JSON, tripDirection TEXT, tripInfo JSON, trip_delay NUMERIC, trip_details JSON, trip_direction TEXT, trip_id TEXT, trip_update JSON, type TransitManagement_type, uncertainty NUMERIC, vehicleDesc JSON, vehicleInfo JSON, vehiclePositionInfo JSON, vehicleType vehicleType_type, vehicle_id TEXT, vehicle_label TEXT, vehicle_position JSON);