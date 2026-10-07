/* (Beta) Export of data model GtfsStopTime of the subject dataModel.UrbanMobility for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE GtfsStopTime_dropOffType_type AS ENUM ('0', '1', '2', '3');
CREATE TYPE GtfsStopTime_pickupType_type AS ENUM ('0', '1', '2', '3');
CREATE TYPE GtfsStopTime_timepoint_type AS ENUM ('0', '1');
CREATE TYPE GtfsStopTime_type AS ENUM ('GtfsStopTime');
CREATE TABLE GtfsStopTime (
  "alternateName" TEXT,
  "arrivalTime" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "departureTime" TEXT,
  "description" TEXT,
  "distanceTravelled" NUMERIC,
  "dropOffType" GtfsStopTime_dropOffType_type,
  "hasStop" JSON,
  "hasTrip" JSON,
  "id" TEXT PRIMARY KEY,
  "name" TEXT,
  "owner" JSON,
  "pickupType" GtfsStopTime_pickupType_type,
  "seeAlso" JSON,
  "source" TEXT,
  "stopHeadsign" TEXT,
  "stopSequence" NUMERIC,
  "timepoint" GtfsStopTime_timepoint_type,
  "type" GtfsStopTime_type
);