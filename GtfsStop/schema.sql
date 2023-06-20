/* (Beta) Export of data model GtfsStop of the subject dataModel.UrbanMobility for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE GtfsStop_type AS ENUM ('GtfsStop');CREATE TYPE wheelChairAccessible_type AS ENUM (0, 1, 2);
CREATE TABLE GtfsStop (address json, alternateName text, areaServed text, code text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, hasParentStation text, hasService text, hasStop json, hasTrip text, id text, location json, name text, operatedBy json, owner json, page text, seeAlso json, source text, stop_desc text, type GtfsStop_type, wheelChairAccessible wheelChairAccessible_type, zoneCode text);