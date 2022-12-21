/* (Beta) Export of data model GtfsStation of the subject dataModel.UrbanMobility for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE GtfsStation_type AS ENUM ('GtfsStation');CREATE TYPE wheelChairAccessible_type AS ENUM (0, 1, 2);
CREATE TABLE GtfsStation (address json, alternateName text, areaServed text, code text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, hasAccessPoint json, hasParentStation text, hasService text, hasStop json, hasTrip text, id text, location json, name text, owner json, page text, seeAlso json, source text, stop_desc text, type GtfsStation_type, wheelChairAccessible wheelChairAccessible_type, zoneCode text);