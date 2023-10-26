/* (Beta) Export of data model GtfsTrip of the subject dataModel.UrbanMobility for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE bikesAllowed_type AS ENUM ('0','1','2');CREATE TYPE direction_type AS ENUM ('0','1');CREATE TYPE GtfsTrip_type AS ENUM ('GtfsTrip');CREATE TYPE wheelChairAccessible_type AS ENUM ('0','1','2');
CREATE TABLE GtfsTrip (alternateName TEXT, bikesAllowed bikesAllowed_type, block TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, direction direction_type, hasRoute TEXT, headSign TEXT, id TEXT PRIMARY KEY, name TEXT, owner JSON, seeAlso JSON, shortName TEXT, source TEXT, type GtfsTrip_type, wheelChairAccessible wheelChairAccessible_type);