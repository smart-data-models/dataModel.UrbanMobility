/* (Beta) Export of data model GtfsShape of the subject dataModel.UrbanMobility for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE GtfsShape_type AS ENUM ('GtfsShape');
CREATE TABLE GtfsShape (address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, distanceTravelled json, id text, location json, name text, owner json, seeAlso json, source text, type GtfsShape_type);