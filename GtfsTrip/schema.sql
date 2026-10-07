/* (Beta) Export of data model GtfsTrip of the subject dataModel.UrbanMobility for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE GtfsTrip_bikesAllowed_type AS ENUM ('0', '1', '2');
CREATE TYPE GtfsTrip_direction_type AS ENUM ('0', '1');
CREATE TYPE GtfsTrip_type AS ENUM ('GtfsTrip');
CREATE TYPE GtfsTrip_wheelChairAccessible_type AS ENUM ('0', '1', '2');
CREATE TABLE GtfsTrip (
  "alternateName" TEXT,
  "bikesAllowed" GtfsTrip_bikesAllowed_type,
  "block" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "direction" GtfsTrip_direction_type,
  "hasRoute" TEXT,
  "hasService" JSON,
  "hasShape" JSON,
  "headSign" TEXT,
  "id" TEXT PRIMARY KEY,
  "name" TEXT,
  "owner" JSON,
  "seeAlso" JSON,
  "shortName" TEXT,
  "source" TEXT,
  "type" GtfsTrip_type,
  "wheelChairAccessible" GtfsTrip_wheelChairAccessible_type
);