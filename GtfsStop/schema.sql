/* (Beta) Export of data model GtfsStop of the subject dataModel.UrbanMobility for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE GtfsStop_type AS ENUM ('GtfsStop');CREATE TYPE wheelChairAccessible_type AS ENUM ('0','1','2');
CREATE TABLE GtfsStop (address JSON, alternateName TEXT, areaServed TEXT, code TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, hasService TEXT, hasStop JSON, id TEXT PRIMARY KEY, location JSON, name TEXT, operatedBy JSON, owner JSON, page TEXT, seeAlso JSON, source TEXT, stop_desc TEXT, type GtfsStop_type, wheelChairAccessible wheelChairAccessible_type, zoneCode TEXT);