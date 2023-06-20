/* (Beta) Export of data model GtfsStopTime of the subject dataModel.UrbanMobility for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE dropOffType_type AS ENUM (0, 1, 2, 3);CREATE TYPE pickupType_type AS ENUM (0, 1, 2, 3);CREATE TYPE timepoint_type AS ENUM (0, 1);CREATE TYPE GtfsStopTime_type AS ENUM ('GtfsStopTime');
CREATE TABLE GtfsStopTime (alternateName text, arrivalTime text, dataProvider text, dateCreated timestamp, dateModified timestamp, departureTime text, description text, distanceTravelled text, dropOffType dropOffType_type, hasStop text, hasTrip text, id text, name text, owner json, pickupType pickupType_type, seeAlso json, source text, stopHeadsign text, stopSequence integer, timepoint timepoint_type, type GtfsStopTime_type);