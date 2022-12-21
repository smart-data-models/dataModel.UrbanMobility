/* (Beta) Export of data model ArrivalEstimation of the subject dataModel.UrbanMobility for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ArrivalEstimation_type AS ENUM ('ArrivalEstimation');
CREATE TABLE ArrivalEstimation (alternateName text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, hasStop json, hasTrip text, headSign text, id text, name text, owner json, remainingDistance text, remainingTime text, seeAlso json, source text, type ArrivalEstimation_type);