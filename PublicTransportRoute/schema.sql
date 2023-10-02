/* (Beta) Export of data model PublicTransportRoute of the subject dataModel.UrbanMobility for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE transportationType_type AS ENUM ('0','1','2','3','4','5','6','7');CREATE TYPE PublicTransportRoute_type AS ENUM ('PublicTransportRoute');
CREATE TABLE PublicTransportRoute (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, name TEXT, owner JSON, routeCode TEXT, routeColor TEXT, routeSegments JSON, routeTextColor TEXT, schedule JSON, shortRouteCode TEXT, source TEXT, transportationType transportationType_type, type PublicTransportRoute_type);