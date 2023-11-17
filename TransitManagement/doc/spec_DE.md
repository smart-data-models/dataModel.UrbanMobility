<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: TransitManagement    
==========================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/TransitManagement/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Datenmodell eines öffentlichen Nahverkehrssystems**    
Version: 0.0.4    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `acAvailable[string]`: Beschreibt das Vorhandensein einer Klimaanlage im Fahrzeug, die dieser Beobachtung entspricht  - `ac_available[string]`: Beschreibt das Vorhandensein einer Klimaanlage im Fahrzeug, die dieser Beobachtung entspricht  - `actual_trip_end_time[date-time]`: Dieses Feld gibt die Zeit an, zu der der Dienst oder die Reise, die dieser Beobachtung entspricht, planmäßig enden soll  - `actual_trip_start_time[date-time]`: Dieses Feld gibt die Zeit an, zu der der Dienst tatsächlich begann.  Dies ist SameAs: absolute "Zeit" (StopTimeEvent) im Feld "Ankunft" der Meldung stop_time_update (StopTimeUpdate) der GTFS-Echtzeitmeldung-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  - `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `agencyInfo[object]`: Informationen der Agentur zu dieser Beobachtung  	- `agency_email[string]`: E-Mail-Adresse, die vom Kundendienst der Agentur aktiv überwacht wird. SameAs: Feld "agency_email" aus GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)      
	- `agency_fare_url[string]`: URL einer Webseite, die Einzelheiten zu den Tarifen enthält und auch den Online-Kauf von Fahrkarten für diese Agentur ermöglichen könnte. SameAs: Feld "agency_fare_url" aus GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)      
	- `agency_id[string]`: ID zur eindeutigen Identifizierung eines Verkehrsunternehmens. Ein Transit-Feed kann Daten von mehr als einer Agentur enthalten. Die agency_id ist dataset unique. Dieses Feld ist optional für Transit-Feeds, die nur Daten für eine einzige Agentur enthalten. SameAs: Feld "agency_id" aus GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)      
	- `agency_lang[string]`: Enthält einen zweibuchstabigen ISO 639-1-Code für die von dieser Versandstelle verwendete Hauptsprache. Die Groß- und Kleinschreibung des Sprachcodes spielt keine Rolle (sowohl en als auch EN werden akzeptiert). Gleich wie: Feld "agency_lang" aus GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)      
	- `agency_name[string]`: Das Feld agency_name enthält den vollständigen Namen des Verkehrsunternehmens. SameAs: Feld 'agency_name' aus GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)      
	- `agency_phone[string]`: Eine Sprachtelefonnummer für die angegebene Agentur.SameAs: Feld "agency_phone" aus GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)      
	- `agency_timezone[string]`: Das Feld Zeitzone enthält die Zeitzone, in der sich das Verkehrsunternehmen befindet. SameAs: Feld "agency_timezone" aus GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)      
- `agency_fare_url[string]`: URL einer Webseite, die Einzelheiten zu den Tarifen enthält und auch den Online-Kauf von Fahrkarten für diese Agentur ermöglichen könnte. SameAs: Feld "agency_fare_url" aus GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_id[string]`: ID zur eindeutigen Identifizierung eines Verkehrsunternehmens. Ein Transit-Feed kann Daten von mehr als einer Agentur enthalten. Die agency_id ist dataset unique. Dieses Feld ist optional für Transit-Feeds, die nur Daten für eine einzige Agentur enthalten. SameAs: Feld "agency_id" aus GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_lang[string]`: Enthält einen zweibuchstabigen ISO 639-1-Code für die von dieser Versandstelle verwendete Hauptsprache. Die Groß- und Kleinschreibung des Sprachcodes spielt keine Rolle (sowohl en als auch EN werden akzeptiert). Gleich wie: Feld "agency_lang" aus GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_name[string]`: Das Feld agency_name enthält den vollständigen Namen des Verkehrsunternehmens. SameAs: Feld 'agency_name' aus GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_timezone[string]`: Das Feld Zeitzone enthält die Zeitzone, in der sich das Verkehrsunternehmen befindet. SameAs: Feld "agency_timezone" aus GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_url[string]`: Das Feld agency_url enthält die URL des Verkehrsunternehmens. SameAs: Feld 'agency_url' aus GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrival[object]`: Wenn schedule_relationship leer oder SCHEDULED ist, muss entweder Ankunft oder Abfahrt innerhalb eines StopTimeUpdate angegeben werden. SameAs: Feld "arrival" aus GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  	    
- `arrivalUncertainty[number]`: Wenn schedule_relationship leer oder SCHEDULED ist, muss entweder Ankunft oder Abfahrt innerhalb eines StopTimeUpdate angegeben werden. SameAs: Feld "arrival" aus GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `arrival_time[time]`: Gibt die Ankunftszeit an einer bestimmten Haltestelle für eine bestimmte Fahrt auf einer Route an. Die Zeiten müssen achtstellig im Format HH:MM:SS sein (HH:MM:SS wird auch akzeptiert, wenn die Stunde mit 0 beginnt). Hinweis: Fahrten, die sich über mehrere Daten erstrecken, haben Haltezeiten, die größer als 24:00:00 sind. Wenn zum Beispiel eine Fahrt um 22:30:00 Uhr beginnt und um 2:15:00 Uhr am nächsten Tag endet, wären die Haltezeiten 22:30:00 und 26:15:00 Uhr. Die Eingabe dieser Haltezeiten als 22:30:00 und 02:15:00 würde nicht zu den gewünschten Ergebnissen führen. SameAs: Feld "arrival_time" aus GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `bearing[number]`: Gibt den GPS-Winkel des Fahrzeugs, gemessen im Uhrzeigersinn vom wahren Norden, an. Entspricht dem Feld "Peilung" der GTFS-Echtzeitnachricht-Position (https://developers.google.com/transit/gtfs-realtime/reference#message-position)  - `current_status[string]`: Beschreibt den Status des Fahrzeugs in Bezug auf die dieser Beobachtung entsprechende Haltestelle ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. SameAs:'current_status'-Feld der GTFS-Echtzeitmeldung-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `current_stop_sequence[number]`: Gibt den Haltestellenfolgeindex der aktuellen Haltestelle an. Dieser wird unter Berücksichtigung von current_status ermittelt; wenn current_status fehlt, wird IN_TRANSIT_TO angenommen. SameAs:'current_stop_sequence' Feld aus GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `dataDescriptor[uri]`: URI, die auf die Daten-Deskriptor-Entität verweist  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `departure[object]`: Wenn schedule_relationship leer oder SCHEDULED ist, muss entweder Ankunft oder Abfahrt innerhalb eines StopTimeUpdate angegeben werden. SameAs: Feld "departure" aus GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  	    
- `departureUncertainty[number]`: Wenn schedule_relationship leer oder SCHEDULED ist, muss entweder Ankunft oder Abfahrt innerhalb eines StopTimeUpdate angegeben werden. SameAs: Feld "departure" aus GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `departure_time[time]`: Gibt die Abfahrtszeit von einer bestimmten Haltestelle für eine bestimmte Fahrt auf einer Route an. Die Zeiten müssen achtstellig im Format HH:MM:SS sein (HH:MM:SS wird auch akzeptiert, wenn die Stunde mit 0 beginnt).    
Hinweis: Fahrten, die sich über mehrere Daten erstrecken, haben Haltezeiten, die größer als 24:00:00 sind. Wenn zum Beispiel eine Fahrt um 22:30:00 Uhr beginnt und um 2:15:00 Uhr am nächsten Tag endet, wären die Haltezeiten 22:30:00 und 26:15:00 Uhr. Die Eingabe dieser Haltezeiten als 22:30:00 und 02:15:00 würde nicht zu den gewünschten Ergebnissen führen. SameAs: Feld "departure_time" aus GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `depotID[string]`: Beschreibt die eindeutige Kennung des Busdepots, das dieser Beobachtung entspricht  - `depotName[string]`: Beschreibt den Depotnamen des Busdepots, das dieser Beobachtung entspricht  - `depot_id[string]`: Beschreibt die eindeutige Kennung des Busdepots, das dieser Beobachtung entspricht  - `depot_name[string]`: Beschreibt den Depotnamen des Busdepots, das dieser Beobachtung entspricht  - `description[string]`: Eine Beschreibung dieses Artikels  - `deviceInfo[object]`: Informationen über das mit den Beobachtungen verbundene Gerät  . Model: [https://schema.org/Text](https://schema.org/Text)	- `deviceBatteryStatus[string]`: Gibt den Batterieladestatus des meldenden Geräts an (verbunden, getrennt)  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceID[string]`: Geräte-ID des physischen Sensors/der Messstation, der/die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceModel[object]`: Beschreibt die Informationen über das betreffende Gerät, den Sensor oder das System  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceName[string]`: Gerätename oder Stationsname des Sensorgeräts/der Station, das/die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceSimNumber[string]`: Gibt die Sim-Nummer des Geräts im Entsorgungsfahrzeug an  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `measurand[string]`: Vom Gerät erfasste/beobachtete/gemessene Eigenschaft/Eigenschaften  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `direction_id[number]`: Gibt die Fahrtrichtung des Fahrzeugs an, das dieser Beobachtung entspricht; kann aus dem statischen GTFS-Feed trips.txt entnommen werden. Gleich wie: Feld "direction_id" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `entity_id[string]`: Eindeutige Feed-ID für die Entität, die dieser Beobachtung entspricht SameAs:'entity_id' Feld von GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  - `id[*]`: Eindeutiger Bezeichner der Entität  - `last_stop_arrival_time[time]`: Gibt die Ankunftszeit an der vorherigen Haltestelle für eine bestimmte Fahrt auf einer Route an. Die Zeiten müssen achtstellig im Format HH:MM:SS sein (H:MM:SS wird auch akzeptiert, wenn die Stunde mit 0 beginnt).    
Hinweis: Fahrten, die sich über mehrere Daten erstrecken, haben Haltezeiten, die größer als 24:00:00 sind. Wenn zum Beispiel eine Fahrt um 22:30:00 Uhr beginnt und um 2:15:00 Uhr am nächsten Tag endet, wären die Haltezeiten 22:30:00 und 26:15:00 Uhr. Die Eingabe dieser Haltezeiten als 22:30:00 und 02:15:00 würde nicht zu den gewünschten Ergebnissen führen. Dies ist SameAs: absolute "Zeit" (StopTimeEvent) im Feld "Ankunft" der Meldung stop_time_update (StopTimeUpdate) der GTFS-Echtzeitmeldung-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  - `last_stop_id[string]`: Haltestellen-ID/Haltestellenname der vorherigen Bushaltestelle, die dem Bus in dieser Beobachtung entspricht. Gleich wie: Feld "stop_id" aus der GTFS-Echtzeitnachricht-VehiclePosition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `last_tracked_time[date-time]`: Gibt die Uhrzeit an, zu der das Fahrzeug zuletzt geortet wurde  - `license_plate[string]`: Gibt das Nummernschild des Fahrzeugs an. SameAs: Feld "license_plate" aus GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `observationDateTime[date-time]`: Letzter gemeldeter Zeitpunkt der Beobachtung  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `position[object]`: Beschreibt die aktuelle Position des Fahrzeugs, die dieser Beobachtung entspricht. SameAs: Positionsfeld der GTFS-Echtzeitnachricht-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  . Model: [https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition](https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)	- `bearing[number]`: Peilung, in Grad, im Uhrzeigersinn von True North, d.h. 0 ist Norden und 90 ist Osten. Dabei kann es sich um die Kompasspeilung oder um die Richtung zum nächsten Halt oder Zwischenziel handeln. Die Peilung sollte nicht aus der Abfolge der vorherigen Positionen abgeleitet werden, die der Kunde aus den vorherigen Daten berechnen kann.      
	- `latitude[number]`: Grad Nord, im WGS-84-Koordinatensystem      
	- `longitude[number]`: Grad Ost, im WGS-84-Koordinatensystem      
	- `odometer[number]`: Kilometerstand, in Metern      
- `positionInfo[object]`: Beschreibt die aktuelle Position des Fahrzeugs, die dieser Beobachtung entspricht. SameAs:'position'-Feld der GTFS-Echtzeitmeldung-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  	- `bearing[number]`: Peilung, in Grad, im Uhrzeigersinn von True North, d.h. 0 ist Norden und 90 ist Osten. Dabei kann es sich um die Kompasspeilung oder um die Richtung zum nächsten Halt oder Zwischenziel handeln. Die Peilung sollte nicht aus der Abfolge der vorherigen Positionen abgeleitet werden, die der Kunde aus den vorherigen Daten berechnen kann.      
	- `odometer[number]`: Wert des Kilometerzählers      
- `routeInfo[object]`: Aktualisierte sortierte Haltestellenfolge für die Fahrt des Fahrzeugs, die dieser Beobachtung entspricht, nicht zu berücksichtigen, wenn schedule_realtionship CANCELED ist. Gleichbedeutend mit: Feld "stop_time_update" aus GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `route_color[string]`: Falls zugewiesen, definiert dieses Feld eine Farbe, die einer Route entspricht. Die Farbe muss als sechsstellige Hexadezimalzahl angegeben werden, z. B. 00FFFF. Wenn keine Farbe angegeben wird, ist die Standardfarbe der Route weiß (FFFFFF). SameAs: Feld "route_color" aus GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)      
	- `route_desc[string]`: Beschreibung der Route. Diese kann die gesamten Streckendetails einschließlich des Ziels und der Zeitangaben in Form einer Textbeschreibung enthalten. SameAs: Feld "route_desc" aus GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)      
	- `route_id[string]`: Strecken-ID, die der Strecke zugewiesen wurde, auf der der Bus/das Fahrzeug, der/das dem Bus in dieser Beobachtung entspricht, derzeit verkehrt      
	- `route_long_name[string]`: Vollständiger Name einer Route. Dieser Name ist aussagekräftiger als der routeShortName und enthält oft das Ziel oder die Haltestelle der Route. Dazu gehören meist die Ziel- und Abfahrtsnamen der Route. SameAs: Feld 'route_long_name' aus GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)      
	- `route_short_name[string]`: Kurzer Name einer Route. Dies ist oft der Bordname des Transitfahrzeugs, wie z. B. 402D, oder Grün, das die Fahrgäste zur Identifizierung einer Strecke verwenden. SameAs: Feld "route_short_name" aus GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)      
	- `route_text_color[string]`: In diesem Feld kann eine lesbare Farbe für Text angegeben werden, der vor einem Hintergrund mit route_color gezeichnet werden soll. Die Farbe muss als sechsstellige Hexadezimalzahl angegeben werden, z. B. FFD700. Wird keine Farbe angegeben, ist die Standardtextfarbe Schwarz (000000). SameAs: Feld "route_text_color" aus GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)      
	- `route_type[number]`: Nummer, die die Art des Verkehrsmittels angibt - 1 - U-Bahn, Metro. Jedes unterirdische Schienensystem in einem Großstadtgebiet. 2 - Eisenbahn. Wird für Intercity- oder Langstreckenreisen verwendet. 3 - Bus. Wird für Nah- und Fernbuslinien verwendet. Gleich wie: Feld "route_type" aus GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)      
- `routeStopSequence[array]`: Gibt die Haltestellenkennungen/Haltestellencodes oder Bahnhofskennungen/Bahnhofscodes in der richtigen Reihenfolge für die Route oder Linie an, die dieser Beobachtung entspricht  - `route_color[string]`: Falls zugewiesen, definiert dieses Feld eine Farbe, die einer Route entspricht. Die Farbe muss als sechsstellige Hexadezimalzahl angegeben werden, z. B. 00FFFF. Wenn keine Farbe angegeben wird, ist die Standardfarbe der Route weiß (FFFFFF). SameAs: Feld "route_color" aus GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_desc[string]`: Beschreibung der Route. Diese kann die gesamten Streckendetails einschließlich des Ziels und der Zeitangaben in Form einer Textbeschreibung enthalten. SameAs: Feld "route_desc" aus GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_id[string]`: Strecken-ID, die der Strecke zugewiesen wurde, auf der der Bus/das Fahrzeug, der/das dem Bus in dieser Beobachtung entspricht, derzeit verkehrt. SameAs: Feld "route_id" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `route_long_name[string]`: Vollständiger Name einer Route. Dieser Name ist aussagekräftiger als der routeShortName und enthält oft das Ziel oder die Haltestelle der Route. Dazu gehören meist die Ziel- und Abfahrtsnamen der Route. SameAs: Feld 'route_long_name' aus GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_short_name[string]`: Kurzer Name einer Strecke. Dies ist oft der Bordname des Verkehrsmittels wie "402D" oder "Grün", mit dem die Fahrgäste eine Strecke identifizieren. SameAs: Feld "route_short_name" aus GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_text_color[string]`: In diesem Feld kann eine lesbare Farbe für Text angegeben werden, der vor einem Hintergrund mit route_color gezeichnet werden soll. Die Farbe muss als sechsstellige Hexadezimalzahl angegeben werden, z. B. FFD700. Wird keine Farbe angegeben, ist die Standardtextfarbe Schwarz (000000). SameAs: Feld "route_text_color" aus GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_type[string]`: Nummer, die die Art des Verkehrsmittels angibt-1 - U-Bahn, Metro. Jedes unterirdische Schienensystem innerhalb eines Ballungsraums.2 - Eisenbahn. Wird für den Intercity- oder Fernverkehr verwendet.3 - Bus. Wird für Nah- und Fernbuslinien verwendet. SameAs: Feld "route_type" aus GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_url[string]`: Enthält die URL einer Webseite über diese bestimmte Strecke und unterscheidet sich von agency_url. SameAs: Feld "route_url" aus GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `schedule_relationship[string]`: Beschreibt, ob die Route/Reise geplant wurde. SameAs: 'schedule_relationship' Feld von enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)  - `seating_capacity[number]`: Beschreibt die Fahrgastsitzkapazität des Fahrzeugs, die dieser Beobachtung entspricht  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `shapeInfo[object]`: Informationen über den Weg, den das Fahrzeug, das dieser Beobachtung entspricht, zurücklegt  	- `shape_dist_traveled[number]`: Tatsächliche Entfernung, die entlang der Form vom ersten Formpunkt bis zu dem in diesem Datensatz angegebenen Punkt zurückgelegt wurde. Wird von Tourenplanern verwendet, um den richtigen Abschnitt des Shapes auf einer Karte anzuzeigen. Die Werte müssen zusammen mit shape_pt_sequence ansteigen; sie können nicht verwendet werden, um die Rückwärtsfahrt entlang einer Route anzuzeigen. Die Entfernungseinheiten müssen mit den in stop_times.txt verwendeten Einheiten übereinstimmen. Beispiel: Wenn ein Bus entlang der drei oben für A_shp definierten Punkte fährt, würden die zusätzlichen shape_dist_traveled-Werte (hier in Kilometern angegeben) wie folgt aussehen: shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled A_shp,37.61956,-122.48161,0,0 A_shp,37.64430,-122.41070,6,6.8310 A_shp,37.65863,-122.30839,11,15.8765      
	- `shape_id[string]`: Identifiziert eine Form      
- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `speed[number]`: Gibt die Geschwindigkeit des Fahrzeugs an. Entspricht dem Feld "Geschwindigkeit" der GTFS-Echtzeitnachricht-Position (https://developers.google.com/transit/gtfs-realtime/reference#message-position)  - `standing_capacity[number]`: Beschreibt die Stehplatzkapazität des Fahrzeugs, die dieser Beobachtung entspricht  - `start_date[string]`: Beschreibt das ursprüngliche geplante Datum der Fahrt, die dem Fahrzeug dieser Beobachtung entspricht. Ein Beispielformat für dieses Feld - JJJJMMTT. Gleich wie: Feld "start_date" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `start_time[time]`: Beschreibt die ursprüngliche planmäßige Startzeit der Fahrt, die dem Fahrzeug dieser Beobachtung entspricht. Ein Beispielformat für dieses Feld - 11:15:35 oder 25:15:35. Gleich wie: Feld "start_time" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `stopInfo[object]`: Informationen über den Weg, den das Fahrzeug, das dieser Beobachtung entspricht, zurücklegt  	- `stop_code[string]`: Dieses Feld enthält einen kurzen Text oder eine Nummer, die die Haltestelle für Fahrgäste eindeutig identifiziert. Kann dasselbe sein wie stop_id, wenn es sich um eine öffentliche Haltestelle handelt. Gleich wie: Feld "stop_code" aus GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)      
	- `stop_desc[string]`: Dieses Feld enthält eine Beschreibung der Haltestelle. SameAs: Feld "stop_desc" aus GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)      
	- `stop_id[string]`: Eindeutige ID, die der Haltestelle zugewiesen wurde, die dieser Beobachtung entspricht      
	- `stop_name[string]`: Beschreibt den Namen einer Haltestelle oder eines Bahnhofs. SameAs: Feld "stop_name" aus GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)      
- `stopTimeUpdateInfo[object]`: Aktualisierte sortierte Haltestellenfolge für die Fahrt des Fahrzeugs, die dieser Beobachtung entspricht, nicht zu berücksichtigen, wenn schedule_realtionship CANCELED ist. Gleichbedeutend mit: Feld "stop_time_update" aus GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `stopScheduleRelationship[string]`: Beschreibt die Beziehung zwischen dem statischen Fahrplan und der Haltestelle. SameAs: 'schedule_relationship' Feld von GTFS Realtime message-StopTimeUpdate ENUM[SCHEDULED, SKIPPED, NO_DATA] (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)      
	- `stop_id[string]`: Eindeutige ID, die der Haltestelle zugewiesen wurde, die dieser Beobachtung entspricht      
- `stopTimesInfo[object]`: Ein Deskriptor für die Echtzeit-Aktualisierung des Fahrplans eines Fahrzeugs auf einer Reise  	- `arrival_time[time]`: Gibt die Ankunftszeit an einer bestimmten Haltestelle für eine bestimmte Fahrt auf einer Route an. Die Zeiten müssen achtstellig im Format HH:MM:SS sein (HH:MM:SS wird auch akzeptiert, wenn die Stunde mit 0 beginnt). Hinweis: Fahrten, die sich über mehrere Daten erstrecken, haben Haltezeiten, die größer als 24:00:00 sind. Wenn zum Beispiel eine Fahrt um 22:30:00 Uhr beginnt und um 2:15:00 Uhr am nächsten Tag endet, wären die Haltezeiten 22:30:00 und 26:15:00 Uhr. Die Eingabe dieser Haltezeiten als 22:30:00 und 02:15:00 würde nicht zu den gewünschten Ergebnissen führen. SameAs: Feld "arrival_time" aus GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)      
	- `continuous_drop_off[number]`: Gibt an, ob ein Fahrgast an einem beliebigen Punkt entlang des Fahrweges aus dem Fahrzeug aussteigen kann; entspricht: Feld "continuous_drop_off" aus GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)      
	- `continuous_pickup[number]`: Gibt an, ob ein Fahrgast an einem beliebigen Punkt auf dem Fahrweg des Fahrzeugs einsteigen kann: Feld "continuous_pickup" aus GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)      
	- `departure_time[time]`: Gibt die Abfahrtszeit von einer bestimmten Haltestelle für eine bestimmte Fahrt auf einer Route an. Die Zeiten müssen achtstellig im Format HH:MM:SS sein (HH:MM:SS wird auch akzeptiert, wenn die Stunde mit 0 beginnt). Hinweis: Fahrten, die sich über mehrere Daten erstrecken, haben Haltezeiten, die größer als 24:00:00 sind. Wenn zum Beispiel eine Fahrt um 22:30:00 Uhr beginnt und um 2:15:00 Uhr am nächsten Tag endet, wären die Haltezeiten 22:30:00 und 26:15:00 Uhr. Die Eingabe dieser Haltezeiten als 22:30:00 und 02:15:00 würde nicht zu den gewünschten Ergebnissen führen. SameAs: Feld "departure_time" aus GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)      
	- `drop_off_type[string]`: Gibt die Abgabemethode an. SameAs: Feld "drop_off_type" aus GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)      
	- `pickup_type[string]`: Zeigt die Abholmethode an.SameAs: Feld "pickup_type" aus GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)      
	- `stop_headsign[string]`: Dieses Feld enthält den Text, der auf einem Schild erscheint, das den Fahrgästen das Ziel der Reise anzeigt. SameAs: Feld "stop_headsign" aus GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)      
	- `stop_id[string]`: Eindeutige ID, die der Haltestelle zugewiesen wurde, die dieser Beobachtung entspricht      
	- `stop_sequence[number]`: Dieses Feld gibt die Reihenfolge der Haltestellen für eine bestimmte Fahrt an. Die Werte für stop_sequence müssen nicht-negative ganze Zahlen sein, und sie müssen entlang der Fahrt ansteigen. Zum Beispiel könnte die erste Haltestelle der Fahrt eine stop_sequence von 1 haben, die zweite Haltestelle der Fahrt könnte eine stop_sequence von 23 haben, die dritte Haltestelle könnte eine stop_sequence von 40 haben usw.      
- `stop_code[string]`: Dieses Feld enthält einen kurzen Text oder eine Nummer, die die Haltestelle für Fahrgäste eindeutig identifiziert. Kann dasselbe sein wie stop_id, wenn es sich um eine öffentliche Haltestelle handelt. Gleich wie: Feld "stop_code" aus GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_desc[string]`: Dieses Feld enthält eine Beschreibung der Haltestelle. SameAs: Feld "stop_desc" aus GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_headsign[string]`: Dieses Feld enthält den Text, der auf einem Schild erscheint, das den Fahrgästen das Ziel der Reise anzeigt. SameAs: Feld "stop_headsign" aus GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `stop_id[string]`: Haltestellen-ID/Haltestellenname der Bushaltestellen, die dem Bus in dieser Beobachtung entsprechen. Gleich wie: Feld "stop_id" der GTFS-Echtzeitnachricht-Fahrzeugposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `stop_name[string]`: Beschreibt den Namen der Bushaltestelle. SameAs: Feld "stop_name" aus GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_sequence[number]`: Gibt die Haltesequenz des Fahrzeugs an, die dieser Beobachtung entspricht; kann aus dem statischen GTFS-Feed stop_times.txt abgerufen werden. Gleichbedeutend mit: Feld "stop_sequence" aus der GTFS-Echtzeitmeldung "stopTimeUpdate" (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)  - `stop_sequence_detail[object]`: Beschreibt die Haltestellenreihenfolge für eine Fahrt des ÖPNV-Fahrzeugs auf der vorgesehenen Route: Feld "stop_sequence" aus GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  	- `stop_id[string]`: Muss dieselbe sein wie in stops.txt im entsprechenden GTFS-Feed. Entweder stop_sequence oder stop_id müssen in einem StopTimeUpdate angegeben werden - beide Felder dürfen nicht leer sein      
- `stop_time_update[object]`: Zusätzliche Informationen über das Fahrzeug, das für diese Reise eingesetzt wird  	- `arrival[object]`: Wenn schedule_relationship leer oder SCHEDULED ist, muss entweder arrival oder departure in einem StopTimeUpdate angegeben werden - beide Felder dürfen nicht leer sein. arrival und departure können beide leer sein, wenn schedule_relationship SKIPPED ist. Wenn schedule_relationship NO_DATA ist, müssen arrival und departure leer sein.      
	- `departure[object]`: Wenn schedule_relationship leer oder SCHEDULED ist, muss entweder arrival oder departure in einem StopTimeUpdate angegeben werden - beide Felder dürfen nicht leer sein. arrival und departure können beide leer sein, wenn schedule_relationship SKIPPED ist. Wenn schedule_relationship NO_DATA ist, müssen arrival und departure leer sein.      
	- `schedule_relationship[string]`: Enum:'SCHEDULED, SKIPPED, NO_DATA'. SCHEDULED bedeutet, dass das Fahrzeug nach seinem statischen Haltestellenplan fährt, wenn auch nicht unbedingt nach den Zeiten des Plans. Dies ist das Standardverhalten. Es muss mindestens eine Ankunfts- und eine Abfahrtszeit angegeben werden. SKIPPED bedeutet, dass die Haltestelle übersprungen wird, d. h. das Fahrzeug hält nicht an dieser Haltestelle. Die Felder Ankunft und Abfahrt sind optional. NO_DATA bedeutet, dass für diese Haltestelle keine Daten angegeben werden. Es bedeutet, dass keine Echtzeitinformationen verfügbar sind. Wenn NO_DATA gesetzt ist, wird es durch nachfolgende Haltestellen weitergegeben, so dass dies der empfohlene Weg ist, um anzugeben, von welcher Haltestelle Sie keine Echtzeitinformationen haben. Wenn NO_DATA gesetzt ist, sollten weder Ankunft noch Abfahrt angegeben werden.      
	- `stop_id[string]`: Muss dieselbe sein wie in stops.txt im entsprechenden GTFS-Feed. Entweder stop_sequence oder stop_id müssen in einem StopTimeUpdate angegeben werden - beide Felder dürfen nicht leer sein      
- `stop_url[string]`: Dieses Feld enthält die URL einer Webseite über eine bestimmte Haltestelle und unterscheidet sich von den Feldern agency_url und route_url. SameAs: Feld "stop_url" aus GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `timestamp[date-time]`: Letzter gemeldeter Zeitpunkt der Beobachtung durch das Fahrzeug. SameAs: Feld "timestamp" aus der GTFS-Echtzeitmeldung - Fahrzeugposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  - `travelDistance[number]`: Die Entfernung zwischen der Ausgangshaltestelle und der Zielhaltestelle oder die insgesamt zurückgelegte Strecke entsprechend dieser Beobachtung  - `travelTime[time]`: Die Fahrzeit zwischen der Ausgangshaltestelle und der Zielhaltestelle, die dieser Beobachtung entspricht, im Format HH:MM:SS (HH:MM:SS wird auch akzeptiert, wenn die Stunde mit 0 beginnt)  - `trip[object]`: Beschreibt die Fahrt, die das Fahrzeug, das dieser Beobachtung entspricht, unternimmt. SameAs:'trip'-Feld der GTFS-Echtzeitmeldung-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `direction_id[number]`: Gibt die Fahrtrichtung des Fahrzeugs an, das dieser Beobachtung entspricht; kann aus dem statischen GTFS-Feed trips.txt entnommen werden. Gleich wie: Feld "direction_id" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)      
	- `route_id[string]`: Strecken-ID, die der Strecke zugewiesen wurde, auf der der Bus/das Fahrzeug, der/das dem Bus in dieser Beobachtung entspricht, derzeit verkehrt. SameAs: Feld "route_id" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)      
	- `schedule_relationship[string]`: Beschreibt, ob die Route/Reise geplant wurde. SameAs: 'schedule_relationship' Feld von enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)      
	- `start_date[string]`: Beschreibt das ursprüngliche geplante Datum der Fahrt, die dem Fahrzeug dieser Beobachtung entspricht. Ein Beispielformat für dieses Feld - JJJJMMTT. Gleich wie: Feld "start_date" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)      
	- `start_time[string]`: Beschreibt die ursprüngliche planmäßige Startzeit der Fahrt, die dem Fahrzeug dieser Beobachtung entspricht. Ein Beispielformat für dieses Feld - 11:15:35 oder 25:15:35. Gleich wie: Feld "start_time" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)      
- `tripDetails[object]`: Ein Deskriptor für die Echtzeit-Aktualisierung des Fahrplans eines Fahrzeugs auf einer Reise  	- `arrival_time[time]`:  Gibt die Ankunftszeit an einer bestimmten Haltestelle für eine bestimmte Fahrt auf einer Route an. Die Zeiten müssen achtstellig im Format HH:MM:SS sein (HH:MM:SS wird auch akzeptiert, wenn die Stunde mit 0 beginnt). Hinweis: Fahrten, die sich über mehrere Daten erstrecken, haben Haltezeiten, die größer als 24:00:00 sind. Wenn zum Beispiel eine Fahrt um 22:30:00 Uhr beginnt und um 2:15:00 Uhr am nächsten Tag endet, wären die Haltezeiten 22:30:00 und 26:15:00 Uhr. Die Eingabe dieser Haltezeiten als 22:30:00 und 02:15:00 würde nicht zu den gewünschten Ergebnissen führen. SameAs: Feld "arrival_time" aus GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)      
	- `departure_time[time]`: Gibt die Abfahrtszeit von einer bestimmten Haltestelle für eine bestimmte Fahrt auf einer Route an. Die Zeiten müssen achtstellig im Format HH:MM:SS sein (HH:MM:SS wird auch akzeptiert, wenn die Stunde mit 0 beginnt). Hinweis: Fahrten, die sich über mehrere Daten erstrecken, haben Haltezeiten, die größer als 24:00:00 sind. Wenn zum Beispiel eine Fahrt um 22:30:00 Uhr beginnt und um 2:15:00 Uhr am nächsten Tag endet, wären die Haltezeiten 22:30:00 und 26:15:00 Uhr. Die Eingabe dieser Haltezeiten als 22:30:00 und 02:15:00 würde nicht zu den gewünschten Ergebnissen führen. SameAs: Feld "departure_time" aus GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)      
	- `stop_headsign[string]`: Dieses Feld enthält den Text, der auf einem Schild erscheint, das den Fahrgästen das Ziel der Reise anzeigt. SameAs: Feld "stop_headsign" aus GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)      
	- `stop_id[string]`: Haltestellen-ID/Haltestellenname der Bushaltestellen, die dem Bus in dieser Beobachtung entsprechen. Gleich wie: Feld "stop_id" der GTFS-Echtzeitnachricht-Fahrzeugposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)      
- `tripDirection[string]`: Gibt die Fahrtrichtung an, in der das Fahrzeug fährt ENUM[UP,DN]  - `tripInfo[object]`: Beschreibt die Fahrt, die das Fahrzeug, das dieser Beobachtung entspricht, unternimmt. SameAs:'trip'-Feld von GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)  	- `route_id[string]`: Strecken-ID, die der Strecke zugewiesen wurde, auf der der Bus/das Fahrzeug, der/das dem Bus in dieser Beobachtung entspricht, derzeit verkehrt      
	- `schedule_relationship[string]`: Beschreibt, ob die Route/Reise geplant wurde. SameAs: 'schedule_relationship' Feld aus GTFS Realtime message-TripDescriptor ENUM[SCHEDULED, ADDED, UNSCHEDULED, CANCELED] (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)      
	- `start_date[string]`: Beschreibt das ursprüngliche geplante Datum der Fahrt, die dem Fahrzeug dieser Beobachtung entspricht. Ein Beispielformat für dieses Feld - JJJJMMTT. Gleich wie: Feld "start_date" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)      
	- `start_time[time]`: Beschreibt die ursprüngliche planmäßige Startzeit der Fahrt, die dem Fahrzeug dieser Beobachtung entspricht. Ein Beispielformat für dieses Feld - 11:15:35 oder 25:15:35. Gleich wie: Feld "start_time" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)      
	- `trip_direction[string]`: Gibt die Fahrtrichtung des Fahrzeugs an, das dieser Beobachtung entspricht; kann aus dem statischen GTFS-Feed trips.txt entnommen werden. Gleich wie: Feld "direction_id" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)      
- `trip_delay[number]`: Diese kann in Sekunden positiv und negativ sein und zeigt an, wie stark das Fahrzeug vom Plan abweicht. SameAs: Feld "delay" aus GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)  - `trip_details[object]`: Ein Deskriptor für die Echtzeit-Aktualisierung des Fahrplans eines Fahrzeugs auf einer Reise  	- `bearing[number]`: Peilung, in Grad, im Uhrzeigersinn von True North, d.h. 0 ist Norden und 90 ist Osten. Dabei kann es sich um die Kompasspeilung oder um die Richtung zum nächsten Halt oder Zwischenziel handeln. Die Peilung sollte nicht aus der Abfolge der vorherigen Positionen abgeleitet werden, die der Kunde aus den vorherigen Daten berechnen kann.      
	- `odometer[number]`: Kilometerstand, in Metern      
- `trip_direction[string]`: Gibt die Richtung an, in der das Fahrzeug unterwegs ist. Gleich wie: Feld "direction_id" aus dem GTFS Realtime message-TripDescriptor, wird jedoch in Form eines ENUM[UP,DN] anstelle von [0,1] wie in "direction_id" dargestellt (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `trip_id[string]`: Fahrt-ID/Fahrtenname, der dem Bus, der dieser Beobachtung entspricht, unter Berücksichtigung der Tageszeit und der Fahrtrichtung auf der angegebenen routeId zugewiesen wurde. SameAs: Feld "trip_id" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `trip_update[object]`: Beschreibt die Fahrtinformationen wie Verspätung, Abfahrten usw. für eine Fahrt des Fahrzeugs, die dieser Beobachtung entspricht. entspricht dem Feld "trip_update" aus dem GTFS Realtime message-FeedEntity (https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  	- `stop_time_update[object]`: Zusätzliche Informationen über das Fahrzeug, das für diese Reise eingesetzt wird      
	- `timestamp[date-time]`: Letzter gemeldeter Zeitpunkt der Beobachtung durch das Fahrzeug. SameAs: Feld "timestamp" aus der GTFS-Echtzeitmeldung - Fahrzeugposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)      
	- `trip[object]`: Beschreibt die Fahrt, die das Fahrzeug, das dieser Beobachtung entspricht, unternimmt. SameAs:'trip'-Feld der GTFS-Echtzeitmeldung-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)      
- `type[string]`: NGSI-Entitätstyp. Es muss TransitManagement sein.  - `uncertainty[number]`: Wenn die Unsicherheit weggelassen wird, wird sie als unbekannt interpretiert. Um eine völlig sichere Vorhersage anzugeben, setzen Sie die Unsicherheit auf 0.SameAs: Feld "uncertainty" aus GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)  - `vehicleDesc[object]`: Beschreibt die zusätzlichen Informationen zu dem Fahrzeug, das dieser Beobachtung entspricht. SameAs: Feld "Fahrzeug" aus der GTFS-Echtzeitmeldung - VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `license_plate[string]`: Gibt das Kennzeichen des Fahrzeugs an.SameAs: Feld "license_plate" aus GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)      
	- `vehicle_id[string]`: Eindeutige ID, die dem Fahrzeug, das dieser Beobachtung entspricht, zugewiesen wurde und für die interne Systemidentifizierung verwendet wird; entspricht dem: Feld "id" der GTFS-Echtzeitmeldung - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)      
- `vehicleInfo[object]`: Beschreibt die zusätzlichen Informationen zu dem Fahrzeug, das dieser Beobachtung entspricht. SameAs: Feld "Fahrzeug" aus der GTFS-Echtzeitmeldung - VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  	- `license_plate[string]`: Gibt das Nummernschild des Fahrzeugs an. SameAs: Feld "license_plate" aus GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)      
	- `vehicleID[string]`: Eindeutige ID, die dem Fahrzeug, das dieser Beobachtung entspricht, zugewiesen wurde und für die interne Systemidentifikation verwendet wird. SameAs: Feld "id" aus GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)      
- `vehiclePositionInfo[object]`: Beschreibt die Echtzeitposition des Fahrzeugs, das dieser Beobachtung entspricht. SameAs:'vehicle' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  	- `congestion_level[string]`: Beschreibt die Stauebene, von der dieses Fahrzeug betroffen ist. ENUM [UNKNOWN_CONGESTION_LEVEL, RUNNING_SMOOTHLY, STOP_AND_GO, CONGESTION, SEVERE_CONGESTION]      
	- `current_status[string]`: Beschreibt den Status des Fahrzeugs in Bezug auf die dieser Beobachtung entsprechende Haltestelle ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. SameAs:'current_status'-Feld der GTFS-Echtzeitmeldung-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)      
	- `current_stop_sequence[number]`: Gibt den Haltestellenfolgeindex der aktuellen Haltestelle an. Dieser wird unter Berücksichtigung von current_status ermittelt; wenn current_status fehlt, wird IN_TRANSIT_TO angenommen. SameAs:'current_stop_sequence' Feld aus GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)      
	- `occupancy_status[string]`: Der Grad der Fahrgastbelegung des Fahrzeugs. ENUM [LEER, VIELE_SITZPLÄTZE_VERFÜGBAR, WENIGE_SITZPLÄTZE_VERFÜGBAR, NUR STEHPLÄTZE_VERFÜGBAR, GEQUETSCHTE_STEHPLÄTZE_VERFÜGBAR, VOLL, KEINE_PASSAGIERE_ANNEHMEND, KEINE_DATEN_VERFÜGBAR, NICHT_EINSTEIGEFÄHIG]      
- `vehicleType[string]`: Beschreibt den Fahrzeugtyp, der dieser Beobachtung entspricht, z. B. Bunker, Verdichter, Kipper, Dumper bei Fahrzeugen der Abfallwirtschaft, BRT-Minibus, BRT-Bus, Stadtbus bei ITMS-Fahrzeugen, Krankenwagen, Feuerwehrauto, Polizeiwagen usw. bei Einsatzfahrzeugen und Moped/Scooter, Motorrad, Autorikscha, Privatwagen/Jeep, Tempo, Bus, E-Moped/E-Scooter/E-Motorrad, öffentliches Fahrzeug bei der Fahrzeugzulassung  - `vehicle_id[string]`: Eindeutige ID, die dem Fahrzeug, das dieser Beobachtung entspricht, zugewiesen wurde und für die interne Systemidentifikation verwendet wird. SameAs: Feld "id" aus GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `vehicle_label[string]`: Vom Benutzer sichtbare Kennzeichnung, d.h. etwas, das dem Fahrgast gezeigt werden muss, um das richtige Fahrzeug zu identifizieren. SameAs: Feld "label" aus GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `vehicle_position[object]`: Beschreibt die Echtzeitposition des Fahrzeugs, das dieser Beobachtung entspricht. SameAs:'vehicle' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  	- `current_status[string]`: Beschreibt den Status des Fahrzeugs in Bezug auf die dieser Beobachtung entsprechende Haltestelle ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. SameAs:'current_status'-Feld der GTFS-Echtzeitmeldung-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)      
	- `current_stop_sequence[number]`: Gibt den Haltestellenfolgeindex der aktuellen Haltestelle an. Dieser wird unter Berücksichtigung von current_status ermittelt; wenn current_status fehlt, wird IN_TRANSIT_TO angenommen. SameAs:'current_stop_sequence' Feld aus GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)      
	- `position[object]`: Beschreibt die aktuelle Position des Fahrzeugs, die dieser Beobachtung entspricht. SameAs: Feld "position" aus der GTFS-Echtzeitmeldung "VehiclePosition"(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)      
	- `stop_id[string]`: Haltestellen-ID/Haltestellenname der Bushaltestellen, die dem Bus in dieser Beobachtung entsprechen. Gleich wie: Feld "stop_id" der GTFS-Echtzeitnachricht-Fahrzeugposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)      
	- `timestamp[date-time]`: Letzter gemeldeter Zeitpunkt der Beobachtung durch das Fahrzeug. SameAs:  Feld "timestamp" aus der GTFS-Echtzeitmeldung - Fahrzeugposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)      
	- `trip[object]`: Beschreibt die Fahrt, die das Fahrzeug, das dieser Beobachtung entspricht, unternimmt. SameAs:'trip'-Feld der GTFS-Echtzeitmeldung-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)      
<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
TransitManagement:      
  description: A public transit system Data Model      
  properties:      
    acAvailable:      
      description: Describes the presence of air conditioning option in the vehicle corresponding to this observation      
      type: string      
      x-ngsi:      
        type: Property      
    ac_available:      
      description: Describes the presence of air conditioning option in the vehicle corresponding to this observation      
      type: string      
      x-ngsi:      
        type: Property      
    actual_trip_end_time:      
      description: This field specifies the time at which service or trip corresponding to this observation is scheduled to end      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    actual_trip_start_time:      
      description: "This field specifies the time at which service actually began.  This is SameAs: absolute 'time'(StopTimeEvent) in the 'arrival' field of the stop_time_update (StopTimeUpdate) message of the GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    agencyInfo:      
      description: Agency information corresponding to this observation      
      properties:      
        agency_email:      
          description: "Email address actively monitored by the agency’s customer service department. SameAs: 'agency_email' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        agency_fare_url:      
          description: "URL of a web page that contains the details of the fares and also could allow to purchase tickets for that agency online. SameAs: 'agency_fare_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        agency_id:      
          description: "ID that uniquely identifies a transit agency. A transit feed may represent data from more than one agency. The agency_id is dataset unique. This field is optional for transit feeds that only contain data for a single agency. SameAs: 'agency_id' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        agency_lang:      
          description: "Contains a two-letter ISO 639-1 code for the primary language used by this transit agency. The language code is case-insensitive (both en and EN are accepted). SameAs: 'agency_lang' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        agency_name:      
          description: "The agency_name field contains the full name of the transit agency. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        agency_phone:      
          description: "A voice telephone number for the specified agency.SameAs: 'agency_phone' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        agency_timezone:      
          description: "Timezone field contains the timezone where the transit agency is located. SameAs: 'agency_timezone' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        agency_url:      
          description: "The agency_url field contains the URL of the transit agency. SameAs: 'agency_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    agency_fare_url:      
      description: "URL of a web page that contains the details of the fares and also could allow to purchase tickets for that agency online. SameAs: 'agency_fare_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    agency_id:      
      description: "ID that uniquely identifies a transit agency. A transit feed may represent data from more than one agency. The agency_id is dataset unique. This field is optional for transit feeds that only contain data for a single agency. SameAs: 'agency_id' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    agency_lang:      
      description: "Contains a two-letter ISO 639-1 code for the primary language used by this transit agency. The language code is case-insensitive (both en and EN are accepted). SameAs: 'agency_lang' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    agency_name:      
      description: "The agency_name field contains the full name of the transit agency. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    agency_timezone:      
      description: "Timezone field contains the timezone where the transit agency is located. SameAs: 'agency_timezone' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    agency_url:      
      description: "The agency_url field contains the URL of the transit agency. SameAs: 'agency_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    arrival:      
      description: "If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'arrival' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"      
      properties:      
        uncertainty:      
          description: "If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    arrivalUncertainty:      
      description: "If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'arrival' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"      
      type: number      
      x-ngsi:      
        type: Property      
    arrival_time:      
      description: "Specifies the arrival time at a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'arrival_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"      
      format: time      
      type: string      
      x-ngsi:      
        type: Property      
    bearing:      
      description: "Gives the vehicle GPS angle measured in a clockwise direction from the True North. SameAs 'bearing' field from GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)"      
      type: number      
      x-ngsi:      
        type: Property      
    current_status:      
      description: "Describes the status of the vehicle w.r.t the stop corresponding to this observation ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. SameAs:'current_status' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
      type: string      
      x-ngsi:      
        type: Property      
    current_stop_sequence:      
      description: "Gives the stop sequence index of the current stop. This is determined by considering current_status, if current_status is missing IN_TRANSIT_TO is assumed. SameAs:'current_stop_sequence' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
      type: number      
      x-ngsi:      
        type: Property      
    dataDescriptor:      
      description: URI pointing to the data-descriptor entity      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    departure:      
      description: "If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'departure' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"      
      properties:      
        uncertainty:      
          description: "If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    departureUncertainty:      
      description: "If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'departure' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"      
      type: number      
      x-ngsi:      
        type: Property      
    departure_time:      
      description: "Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). \nNote: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"      
      format: time      
      type: string      
      x-ngsi:      
        type: Property      
    depotID:      
      description: Describes the unique id of the bus depot corresponding to this observation      
      type: string      
      x-ngsi:      
        type: Property      
    depotName:      
      description: Describes the depot name of the bus depot corresponding to this observation      
      type: string      
      x-ngsi:      
        type: Property      
    depot_id:      
      description: Describes the unique id of the bus depot corresponding to this observation      
      type: string      
      x-ngsi:      
        type: Property      
    depot_name:      
      description: Describes the depot name of the bus depot corresponding to this observation      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    deviceInfo:      
      description: Information about the device associated with the observations      
      properties:      
        deviceBatteryStatus:      
          description: 'Gives the Battery charging status of the reporting device(Connected, Disconnected)'      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        deviceID:      
          description: Device ID of the physical sensor/ measurement station corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        deviceModel:      
          description: 'Describes the information of the device, sensor or system in consideration'      
          properties:      
            brandName:      
              description: 'Name of the brand associated with an entity, e.g., sensor, device etc'      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            manufacturerName:      
              description: 'Name of the manufacturer associated with an entity, e.g., sensor, device etc'      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            modelName:      
              description: 'Name of a specific model associated with an entity, e.g., sensor, device etc'      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            modelURL:      
              description: 'URL providing further information of a specific model associated with an entity, e.g., sensor, device etc'      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            observationDateTime:      
              description: Last reported time of observation      
              format: date-time      
              type: string      
              x-ngsi:      
                type: Property      
            trip_update:      
              description: "Describes the trip information like delay, departures, etc., for a trip made by the vehicle corresponding to this observation.SameAs:'trip_update' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"      
              properties:      
                trip:      
                  description: 'Following the conventions of GTFS trip. '      
                  properties:      
                    direction_id:      
                      type: number      
                    route_id:      
                      type: string      
                    schedule_relationship:      
                      enum:      
                        - SCHEDULED      
                        - ADDED      
                        - UNSCHEDULED      
                        - CANCELED      
                      type: string      
                    start_date:      
                      type: string      
                    start_time:      
                      type: string      
                    trip_id:      
                      type: string      
                  type: object      
                  x-ngsi:      
                    model: "https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor"      
                    type: Property      
              type: object      
              x-ngsi:      
                type: Property      
          type: object      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        deviceName:      
          description: Device Name or Station name of the sensor device/station corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        deviceSimNumber:      
          description: Gives the sim number of the device in the waste management vehicle      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        measurand:      
          description: Property/properties sensed/observed/measured by the device      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        rfID:      
          description: Gives the ID of the RFID reader      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    direction_id:      
      description: "Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
      type: number      
      x-ngsi:      
        type: Property      
    entity_id:      
      description: "Feed unique ID for the entity corresponding to this observation.SameAs:'entity_id' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"      
      type: string      
      x-ngsi:      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    last_stop_arrival_time:      
      description: "Specifies the arrival time at the previous stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (H:MM:SS is also accepted, if the hour begins with 0). \nNote: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. This is SameAs: absolute 'time'(StopTimeEvent) in the 'arrival' field of the stop_time_update (StopTimeUpdate) message of the GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"      
      format: time      
      type: string      
      x-ngsi:      
        type: Property      
    last_stop_id:      
      description: "Stop ID/Stop name of the previous bus stop corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-VehiclePosition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
      type: string      
      x-ngsi:      
        type: Property      
    last_tracked_time:      
      description: Gives the time at which the vehicle was last tracked      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    license_plate:      
      description: "Gives the License Plate number of the vehicle. SameAs: 'license_plate' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
      type: string      
      x-ngsi:      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                type: number      
              minItems: 2      
              type: array      
            type:      
              enum:      
                - Point      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              minItems: 2      
              type: array      
            type:      
              enum:      
                - LineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 4      
                type: array      
              type: array      
            type:      
              enum:      
                - Polygon      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiPoint      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 2      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiLineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    items:      
                      type: number      
                    minItems: 2      
                    type: array      
                  minItems: 4      
                  type: array      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiPolygon      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    observationDateTime:      
      description: Last reported time of observation      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    position:      
      description: "Describes the current position of the vehicle corresponding to this observation. SameAs: position field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
      properties:      
        bearing:      
          description: 'Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data'      
          type: number      
          x-ngsi:      
            type: Property      
        latitude:      
          description: 'Degrees North, in the WGS-84 coordinate system'      
          type: number      
          x-ngsi:      
            type: Property      
        longitude:      
          description: 'Degrees East, in the WGS-84 coordinate system'      
          type: number      
          x-ngsi:      
            type: Property      
        odometer:      
          description: 'Odometer value, in meters'      
          type: number      
          x-ngsi:      
            type: Property      
            units: meters      
        speed:      
          description: 'Momentary speed measured by the vehicle, in meters per second'      
          type: number      
          x-ngsi:      
            type: Property      
            units: meters per second      
      type: object      
      x-ngsi:      
        model: "https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition"      
        type: Property      
    positionInfo:      
      description: "Describes the current position of the vehicle corresponding to this observation. SameAs:'position' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
      properties:      
        bearing:      
          description: 'Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data'      
          type: number      
          x-ngsi:      
            type: Property      
        odometer:      
          description: Odometer value      
          type: number      
          x-ngsi:      
            type: Property      
        speed:      
          description: Momentary speed measured by the vehicle      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    routeInfo:      
      description: "Updated sorted stop sequence for the trip made by the vehicle corresponding to this observation, not to be considered if schedule_realtionship is CANCELED. SameAs: 'stop_time_update' field from GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"      
      properties:      
        route_color:      
          description: "If assigned, this field defines a color that corresponds to a route. The color must be provided as a six-character hexadecimal number, for example, 00FFFF. If no color is specified, the default route color is white (FFFFFF). SameAs: 'route_color' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        route_desc:      
          description: "Description of the route. This can include the entire route details including to and from destination and timing information in a text description form. SameAs: 'route_desc' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        route_id:      
          description: Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on      
          type: string      
          x-ngsi:      
            type: Property      
        route_long_name:      
          description: "Full name of a route. This name is more descriptive than the routeShortName and often includes the route's destination or stop. This mostly includes the to and from destination names of the route. SameAs: 'route_long_name' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        route_short_name:      
          description: "Short name of a route. This will often be the transit vehicle's board name like 402D, or Green that riders use to identify a route. SameAs: 'route_short_name' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        route_text_color:      
          description: "This field can be used to specify a legible color to use for text drawn against a background of route_color. The color must be provided as a six-character hexadecimal number, for example, FFD700. If no color is specified, the default text color is black (000000). SameAs: 'route_text_color' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        route_type:      
          description: "Number indicating the type of transport- 1 - Subway, Metro. Any underground rail system within a metropolitan area. 2 - Rail. Used for intercity or long-distance travel. 3 - Bus. Used for short- and long-distance bus routes. SameAs: 'route_type' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"      
          type: number      
          x-ngsi:      
            type: Property      
        route_url:      
          description: "Contains the URL of a web page about that particular route and is different from the agency_url. SameAs: 'route_url' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    routeStopSequence:      
      description: Gives the stop IDs/stop codes or station IDs/station codes in the right sequence for the route or line corresponding to this observation      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        type: Property      
    route_color:      
      description: "If assigned, this field defines a color that corresponds to a route. The color must be provided as a six-character hexadecimal number, for example, 00FFFF. If no color is specified, the default route color is white (FFFFFF). SameAs: 'route_color' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    route_desc:      
      description: "Description of the route. This can include the entire route details including to and from destination and timing information in a text description form. SameAs: 'route_desc' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    route_id:      
      description: "Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
      type: string      
      x-ngsi:      
        type: Property      
    route_long_name:      
      description: "Full name of a route. This name is more descriptive than the routeShortName and often includes the route's destination or stop. This mostly includes the to and from destination names of the route. SameAs: 'route_long_name' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    route_short_name:      
      description: "Short name of a route. This will often be the transit vehicle's board name like '402D',  or 'Green' that riders use to identify a route. SameAs: 'route_short_name' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    route_text_color:      
      description: "This field can be used to specify a legible color to use for text drawn against a background of route_color. The color must be provided as a six-character hexadecimal number, for example, FFD700. If no color is specified, the default text color is black (000000). SameAs: 'route_text_color' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    route_type:      
      description: "Number indicating the type of transport-1 - Subway, Metro. Any underground rail system within a metropolitan area.2 - Rail. Used for intercity or long-distance travel.3 - Bus. Used for short- and long-distance bus routes. SameAs: 'route_type' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    route_url:      
      description: "Contains the URL of a web page about that particular route and is different from the agency_url. SameAs: 'route_url' field from GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    schedule_relationship:      
      description: "Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)"      
      type: string      
      x-ngsi:      
        type: Property      
    seating_capacity:      
      description: Describes the passenger seating capacity of the vehicle corresponding to this observation      
      type: number      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
      oneOf:      
        - items:      
            format: uri      
            type: string      
          minItems: 1      
          type: array      
        - format: uri      
          type: string      
      x-ngsi:      
        type: Property      
    shapeInfo:      
      description: Information about the path the vehicle corresponding to this observation travels along      
      properties:      
        shape_dist_traveled:      
          description: 'Actual distance traveled along the shape from the first shape point to the point specified in this record. Used by trip planners to show the correct portion of the shape on a map. Values must increase along with shape_pt_sequence; they cannot be used to show reverse travel along a route. Distance units must be consistent with those used in stop_times.txt. Example: If a bus travels along the three points defined above for A_shp, the additional shape_dist_traveled values (shown here in kilometers) would look like this: shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled A_shp,37.61956,-122.48161,0,0 A_shp,37.64430,-122.41070,6,6.8310 A_shp,37.65863,-122.30839,11,15.8765'      
          type: number      
          x-ngsi:      
            type: Property      
        shape_id:      
          description: Identifies a shape      
          type: string      
          x-ngsi:      
            type: Property      
        shape_pt_sequence:      
          description: 'Sequence in which the shape points connect to form the shape. Values must increase along the trip but do not need to be consecutive. Example: If the shape A_shp has three points in its definition, the shapes.txt file might contain these records to define the shape: shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence A_shp,37.61956,-122.48161,0 A_shp,37.64430,-122.41070,6 A_shp,37.65863,-122.30839,11'      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    speed:      
      description: "Gives the Speed  of the vehicle. SameAs 'speed' field from GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)"      
      type: number      
      x-ngsi:      
        type: Property      
    standing_capacity:      
      description: Describes the passenger standing capacity of the vehicle corresponding to this observation      
      type: number      
      x-ngsi:      
        type: Property      
    start_date:      
      description: "Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
      type: string      
      x-ngsi:      
        type: Property      
    start_time:      
      description: "Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
      format: time      
      type: string      
      x-ngsi:      
        type: Property      
    stopInfo:      
      description: Information about the path the vehicle corresponding to this observation travels along      
      properties:      
        stop_code:      
          description: "This field contains short text or a number that uniquely identifies the stop for passengers. Can be same as stop_id if it is for public. SameAs: 'stop_code' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        stop_desc:      
          description: "This field contains a description of a stop. SameAs: 'stop_desc' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        stop_id:      
          description: Unique ID assigned to the stop corresponding to this observation      
          type: string      
          x-ngsi:      
            type: Property      
        stop_name:      
          description: "Describes the name of a stop or station. SameAs: 'stop_name' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        stop_url:      
          description: "This field contains the URL of a web page about a particular stop and is different from the agency_url and the route_url fields. SameAs: 'stop_url' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    stopTimeUpdateInfo:      
      description: "Updated sorted stop sequence for the trip made by the vehicle corresponding to this observation, not to be considered if schedule_realtionship is CANCELED. SameAs: 'stop_time_update' field from GTFS Realtime message-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"      
      properties:      
        stopScheduleRelationship:      
          description: "Describes the relationship between the static schedule and the stop. SameAs: 'schedule_relationship' field from GTFS Realtime message-StopTimeUpdate ENUM[SCHEDULED, SKIPPED, NO_DATA] (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"      
          type: string      
          x-ngsi:      
            type: Property      
        stop_id:      
          description: Unique ID assigned to the stop corresponding to this observation      
          type: string      
          x-ngsi:      
            type: Property      
        stop_sequence:      
          description: 'This field identifies the order of the stops for a particular trip. The values for stop_sequence must be non-negative integers, and they must increase along the trip. For example, the first stop on the trip could have a stop_sequence of 1, the second stop on the trip could have a stop_sequence of 23, the third stop could have a stop_sequence of 40, and so on'      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    stopTimesInfo:      
      description: A descriptor of realtime update on the schedule of a vehicle along a trip      
      properties:      
        arrival_time:      
          description: "Specifies the arrival time at a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'arrival_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"      
          format: time      
          type: string      
          x-ngsi:      
            type: Property      
        continuous_drop_off:      
          description: "Indicates whether a rider can alight from the transit vehicle at any point along the vehicle’s travel path.SameAs: 'continuous_drop_off' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"      
          type: number      
          x-ngsi:      
            type: Property      
        continuous_pickup:      
          description: "Indicates whether a rider can board the transit vehicle at any point along the vehicle’s travel path.SameAs: 'continuous_pickup' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"      
          type: number      
          x-ngsi:      
            type: Property      
        departure_time:      
          description: "Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"      
          format: time      
          type: string      
          x-ngsi:      
            type: Property      
        drop_off_type:      
          description: "Indicates drop off method. SameAs: 'drop_off_type' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        pickup_type:      
          description: "Indicates pickup method.SameAs: 'pickup_type' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        stop_headsign:      
          description: "This field contains the text that appears on a sign that identifies the trip’s destination to passengers. SameAs: 'stop_headsign' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        stop_id:      
          description: Unique ID assigned to the stop corresponding to this observation      
          type: string      
          x-ngsi:      
            type: Property      
        stop_sequence:      
          description: 'This field identifies the order of the stops for a particular trip. The values for stop_sequence must be non-negative integers, and they must increase along the trip. For example, the first stop on the trip could have a stop_sequence of 1, the second stop on the trip could have a stop_sequence of 23, the third stop could have a stop_sequence of 40, and so on'      
          type: number      
          x-ngsi:      
            type: Property      
        trip_id:      
          description: 'Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId'      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    stop_code:      
      description: "This field contains short text or a number that uniquely identifies the stop for passengers. Can be same as stop_id if it is for public. SameAs: 'stop_code' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    stop_desc:      
      description: "This field contains a description of a stop. SameAs: 'stop_desc' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    stop_headsign:      
      description: "This field contains the text that appears on a sign that identifies the trip’s destination to passengers. SameAs: 'stop_headsign' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    stop_id:      
      description: "Stop ID/Stop name of the bus stops corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
      type: string      
      x-ngsi:      
        type: Property      
    stop_name:      
      description: "Describes the name of the Bus Stop. SameAs: 'stop_name' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    stop_sequence:      
      description: "Indicates the stop sequence of the vehicle corresponding to this observation, can be referenced from the GTFS static feed stop_times.txt. SameAs: 'stop_sequence' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"      
      type: number      
      x-ngsi:      
        type: Property      
    stop_sequence_detail:      
      description: "Describes the stop sequence for a trip in the designated route made by the public transit vehicle.SameAs: 'stop_sequence' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"      
      properties:      
        stop_id:      
          description: Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty      
          type: string      
          x-ngsi:      
            type: Property      
        stop_sequence:      
          description: 'Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for'      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    stop_time_update:      
      description: Additional information on the vehicle that is serving this trip      
      properties:      
        arrival:      
          description: 'If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty'      
          properties:      
            uncertainty:      
              description: "If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"      
              type: number      
              x-ngsi:      
                type: Property      
          type: object      
          x-ngsi:      
            type: Property      
        departure:      
          description: 'If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty'      
          properties:      
            uncertainty:      
              description: "If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"      
              type: number      
              x-ngsi:      
                type: Property      
          type: object      
          x-ngsi:      
            type: Property      
        schedule_relationship:      
          description: 'Enum:''SCHEDULED, SKIPPED, NO_DATA''. SCHEDULED means that the vehicle is proceeding in accordance with its static schedule of stops, although not necessarily according to the times of the schedule. This is the default behavior. At least one of arrival and departure must be provided. SKIPPED means that The stop is skipped, i.e., the vehicle will not stop at this stop. The arrival and departure fields are optional. NO_DATA means that no data is given for this stop. It indicates that there is no realtime information available. When set NO_DATA is propagated through subsequent stops so this is the recommended way of specifying from which stop you do not have realtime information. When NO_DATA is set neither arrival nor departure should be supplied'      
          enum:      
            - SCHEDULED      
            - SKIPPED      
            - NO_DATA      
          type: string      
          x-ngsi:      
            type: Property      
        stop_id:      
          description: Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty      
          type: string      
          x-ngsi:      
            type: Property      
        stop_sequence:      
          description: 'Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for'      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    stop_url:      
      description: "This field contains the URL of a web page about a particular stop and is different from the agency_url and the route_url fields. SameAs: 'stop_url' field from GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)"      
      type: string      
      x-ngsi:      
        type: Property      
    timestamp:      
      description: "Last reported time of observation from the vehicle. SameAs: 'timestamp' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    travelDistance:      
      description: The distance between the origin bus stop and the destination bus stop or the total distance travelled corresponding to this observation      
      type: number      
      x-ngsi:      
        type: Property      
    travelTime:      
      description: 'The time taken to travel between the origin bus stop and the destination bus stop corresponding to this observation in HH:MM:SS format(HH:MM:SS is also accepted, if the hour begins with 0)'      
      format: time      
      type: string      
      x-ngsi:      
        type: Property      
    trip:      
      description: "Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"      
      properties:      
        direction_id:      
          description: "Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
          type: number      
          x-ngsi:      
            type: Property      
        route_id:      
          description: "Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
          type: string      
          x-ngsi:      
            type: Property      
        schedule_relationship:      
          description: "Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)"      
          type: string      
          x-ngsi:      
            type: Property      
        start_date:      
          description: "Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
          type: string      
          x-ngsi:      
            type: Property      
        start_time:      
          description: "Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
          type: string      
          x-ngsi:      
            type: Property      
        trip_id:      
          description: "Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    tripDetails:      
      description: A descriptor of realtime update on the schedule of a vehicle along a trip      
      properties:      
        arrival_time:      
          description: " Specifies the arrival time at a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'arrival_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"      
          format: time      
          type: string      
          x-ngsi:      
            type: Property      
        departure_time:      
          description: "Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"      
          format: time      
          type: string      
          x-ngsi:      
            type: Property      
        stop_headsign:      
          description: "This field contains the text that appears on a sign that identifies the trip’s destination to passengers. SameAs: 'stop_headsign' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"      
          type: string      
          x-ngsi:      
            type: Property      
        stop_id:      
          description: "Stop ID/Stop name of the bus stops corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
          type: string      
          x-ngsi:      
            type: Property      
        stop_sequence:      
          description: "Indicates the stop sequence of the vehicle corresponding to this observation, can be referenced from the GTFS static feed stop_times.txt. SameAs: 'stop_sequence' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    tripDirection:      
      description: 'Gives the direction in which the vehicle is travelling in ENUM[UP,DN]'      
      type: string      
      x-ngsi:      
        type: Property      
    tripInfo:      
      description: "Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
      properties:      
        route_id:      
          description: Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on      
          type: string      
          x-ngsi:      
            type: Property      
        schedule_relationship:      
          description: "Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from GTFS Realtime message-TripDescriptor ENUM[SCHEDULED, ADDED, UNSCHEDULED, CANCELED] (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
          type: string      
          x-ngsi:      
            type: Property      
        start_date:      
          description: "Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
          type: string      
          x-ngsi:      
            type: Property      
        start_time:      
          description: "Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
          format: time      
          type: string      
          x-ngsi:      
            type: Property      
        trip_direction:      
          description: "Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
          type: string      
          x-ngsi:      
            type: Property      
        trip_id:      
          description: 'Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId'      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    trip_delay:      
      description: "This can be positive and negative in seconds and shows how much the vehicle deviates from the planned one. SameAs: 'delay' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"      
      type: number      
      x-ngsi:      
        type: Property      
    trip_details:      
      description: A descriptor of realtime update on the schedule of a vehicle along a trip      
      properties:      
        bearing:      
          description: 'Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data'      
          type: number      
          x-ngsi:      
            type: Property      
        odometer:      
          description: 'Odometer value, in meters'      
          type: number      
          x-ngsi:      
            type: Property      
            units: meters      
        speed:      
          description: 'Momentary speed measured by the vehicle, in meters per second'      
          type: number      
          x-ngsi:      
            type: Property      
            units: meters per second      
      type: object      
      x-ngsi:      
        type: Property      
    trip_direction:      
      description: "Gives the direction in which the vehicle is travelling. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor but is represented in the form of an ENUM[UP,DN] in place of [0,1] as seen in 'direction_id' (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
      type: string      
      x-ngsi:      
        type: Property      
    trip_id:      
      description: "Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
      type: string      
      x-ngsi:      
        type: Property      
    trip_update:      
      description: "Describes the trip information like delay, departures, etc., for a trip made by the vehicle corresponding to this observation.SameAs:'trip_update' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"      
      properties:      
        stop_time_update:      
          description: Additional information on the vehicle that is serving this trip      
          properties:      
            arrival:      
              description: 'If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty'      
              properties:      
                uncertainty:      
                  description: "If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"      
                  type: number      
                  x-ngsi:      
                    type: Property      
              type: object      
              x-ngsi:      
                type: Property      
            departure:      
              description: 'If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty'      
              properties:      
                uncertainty:      
                  description: "If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"      
                  type: number      
                  x-ngsi:      
                    type: Property      
              type: object      
              x-ngsi:      
                type: Property      
            schedule_relationship:      
              description: 'Enum:''SCHEDULED, SKIPPED, NO_DATA''. SCHEDULED means that the vehicle is proceeding in accordance with its static schedule of stops, although not necessarily according to the times of the schedule. This is the default behavior. At least one of arrival and departure must be provided. SKIPPED means that The stop is skipped, i.e., the vehicle will not stop at this stop. The arrival and departure fields are optional. NO_DATA means that no data is given for this stop. It indicates that there is no realtime information available. When set NO_DATA is propagated through subsequent stops so this is the recommended way of specifying from which stop you do not have realtime information. When NO_DATA is set neither arrival nor departure should be supplied'      
              enum:      
                - SCHEDULED      
                - SKIPPED      
                - NO_DATA      
              type: string      
              x-ngsi:      
                type: Property      
            stop_id:      
              description: Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty      
              type: string      
              x-ngsi:      
                type: Property      
            stop_sequence:      
              description: 'Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for'      
              type: number      
              x-ngsi:      
                type: Property      
          type: object      
          x-ngsi:      
            type: Property      
        timestamp:      
          description: "Last reported time of observation from the vehicle. SameAs: 'timestamp' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
          format: date-time      
          type: string      
          x-ngsi:      
            type: Property      
        trip:      
          description: "Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"      
          properties:      
            direction_id:      
              description: "Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
              type: number      
              x-ngsi:      
                type: Property      
            route_id:      
              description: "Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
              type: string      
              x-ngsi:      
                type: Property      
            schedule_relationship:      
              description: "Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)"      
              type: string      
              x-ngsi:      
                type: Property      
            start_date:      
              description: "Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
              type: string      
              x-ngsi:      
                type: Property      
            start_time:      
              description: "Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
              type: string      
              x-ngsi:      
                type: Property      
            trip_id:      
              description: "Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
              type: string      
              x-ngsi:      
                type: Property      
          type: object      
          x-ngsi:      
            type: Property      
        vehicleDesc:      
          description: "Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"      
          properties:      
            license_plate:      
              description: "Gives the License Plate number of the vehice.SameAs: 'license_plate' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
              type: string      
              x-ngsi:      
                type: Property      
            vehicle_id:      
              description: "Unique ID assigned to the vehicle corresponding to this observation,used in internal system identification.SameAs: 'id' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
              type: string      
              x-ngsi:      
                type: Property      
            vehicle_label:      
              description: "User visible label,i.e.,something that must be shown to the passenger to help identify the correct vehicle.SameAs: 'label' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
              type: string      
              x-ngsi:      
                type: Property      
          type: object      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be TransitManagement      
      enum:      
        - TransitManagement      
      type: string      
      x-ngsi:      
        type: Property      
    uncertainty:      
      description: "If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"      
      type: number      
      x-ngsi:      
        type: Property      
    vehicleDesc:      
      description: "Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"      
      properties:      
        license_plate:      
          description: "Gives the License Plate number of the vehice.SameAs: 'license_plate' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
          type: string      
          x-ngsi:      
            type: Property      
        vehicle_id:      
          description: "Unique ID assigned to the vehicle corresponding to this observation,used in internal system identification.SameAs: 'id' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
          type: string      
          x-ngsi:      
            type: Property      
        vehicle_label:      
          description: "User visible label,i.e.,something that must be shown to the passenger to help identify the correct vehicle.SameAs: 'label' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    vehicleInfo:      
      description: "Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"      
      properties:      
        license_plate:      
          description: "Gives the License Plate number of the vehice. SameAs: 'license_plate' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
          type: string      
          x-ngsi:      
            type: Property      
        vehicleID:      
          description: "Unique ID assigned to the vehicle corresponding to this observation, used in internal system identification. SameAs: 'id' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
          type: string      
          x-ngsi:      
            type: Property      
        vehicle_label:      
          description: "User visible label, i.e., something that must be shown to the passenger to help identify the correct vehicle. SameAs: 'label' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    vehiclePositionInfo:      
      description: "Describes the realtime position of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"      
      properties:      
        congestion_level:      
          description: 'Describes the congestion level that is affecting this vehicle. ENUM [UNKNOWN_CONGESTION_LEVEL, RUNNING_SMOOTHLY, STOP_AND_GO, CONGESTION, SEVERE_CONGESTION]'      
          type: string      
          x-ngsi:      
            type: Property      
        current_status:      
          description: "Describes the status of the vehicle w.r.t the stop corresponding to this observation ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. SameAs:'current_status' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
          type: string      
          x-ngsi:      
            type: Property      
        current_stop_sequence:      
          description: "Gives the stop sequence index of the current stop. This is determined by considering current_status, if current_status is missing IN_TRANSIT_TO is assumed. SameAs:'current_stop_sequence' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
          type: number      
          x-ngsi:      
            type: Property      
        occupancy_status:      
          description: 'The degree of passenger occupancy for the vehicle. ENUM [EMPTY, MANY_SEATS_AVAILABLE, FEW_SEATS_AVAILABLE, STANDING_ROOM_ONLY, CRUSHED_STANDING_ROOM_ONLY, FULL, NOT_ACCEPTING_PASSENGERS, NO_DATA_AVAILABLE, NOT_BOARDABLE]'      
          type: string      
          x-ngsi:      
            type: Property      
        stop_id:      
          description: Unique ID assigned to the stop corresponding to this observation      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    vehicleType:      
      description: 'Describes the type of vehicle corresponding to this observation, could be hopper, compactor, tipper, dumper in case of solid waste management vehicles, BRT mini bus, BRT bus, city bus in case of ITMS vehicles, Ambulance, Fire tender, Police van etc, in case of emergency vehicles and Moped/Scooter, Motor Cycle,  Autorickshaw, Private car/ Jeep car, Tempo, Bus, E-Moped/E-Scooter/E-Motor Cycle, Public motor in case of vehicle registration'      
      enum:      
        - agriculturalVehicle      
        - ambulance      
        - anyVehicle      
        - articulatedVehicle      
        - autorickshaw      
        - bicycle      
        - binTrolley      
        - BRT mini bus·      
        - BRT bus      
        - bus      
        - car      
        - caravan      
        - carOrLightVehicle      
        - carWithCaravan      
        - carWithTrailer      
        - cleaningTrolley      
        - compactor      
        - constructionOrMaintenanceVehicle      
        - dumper      
        - e-moped      
        - e-scooter      
        - e-motorcycle      
        - fireTender      
        - fourWheelDrive      
        - highSidedVehicle      
        - hopper      
        - lorry      
        - minibus      
        - moped      
        - motorcycle      
        - motorcycleWithSideCar      
        - motorscooter      
        - policeVan      
        - publicMotor      
        - sweepingMachine      
        - tanker      
        - tempo      
        - threeWheeledVehicle      
        - tipper      
        - trailer      
        - tram      
        - trolley      
        - twoWheeledVehicle      
        - van      
        - vehicleWithoutCatalyticConverter      
        - vehicleWithCaravan      
        - vehicleWithTrailer      
        - withEvenNumberedRegistrationPlates      
        - withOddNumberedRegistrationPlates      
        - other      
      type: string      
      x-ngsi:      
        type: Property      
    vehicle_id:      
      description: "Unique ID assigned to the vehicle corresponding to this observation, used in internal system identification. SameAs: 'id' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
      type: string      
      x-ngsi:      
        type: Property      
    vehicle_label:      
      description: "User visible label, i.e., something that must be shown to the passenger to help identify the correct vehicle. SameAs: 'label' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
      type: string      
      x-ngsi:      
        type: Property      
    vehicle_position:      
      description: "Describes the realtime position of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"      
      properties:      
        current_status:      
          description: "Describes the status of the vehicle w.r.t the stop corresponding to this observation ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. SameAs:'current_status' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
          type: string      
          x-ngsi:      
            type: Property      
        current_stop_sequence:      
          description: "Gives the stop sequence index of the current stop. This is determined by considering current_status, if current_status is missing IN_TRANSIT_TO is assumed. SameAs:'current_stop_sequence' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
          type: number      
          x-ngsi:      
            type: Property      
        position:      
          description: "Describes the current position of the vehicle corresponding to this observation. SameAs: 'position' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
          properties:      
            bearing:      
              description: 'Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data'      
              type: number      
              x-ngsi:      
                type: Property      
            latitude:      
              description: 'Degrees North, in the WGS-84 coordinate system'      
              type: number      
              x-ngsi:      
                type: Property      
            longitude:      
              description: 'Degrees East, in the WGS-84 coordinate system'      
              type: number      
              x-ngsi:      
                type: Property      
            odometer:      
              description: 'Odometer value, in meters'      
              type: number      
              x-ngsi:      
                type: Property      
                units: meters      
            speed:      
              description: 'Momentary speed measured by the vehicle, in meters per second'      
              type: number      
              x-ngsi:      
                type: Property      
                units: meters/second      
          type: object      
          x-ngsi:      
            type: Property      
        stop_id:      
          description: "Stop ID/Stop name of the bus stops corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
          type: string      
          x-ngsi:      
            type: Property      
        timestamp:      
          description: "Last reported time of observation from the vehicle. SameAs:  'timestamp' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"      
          format: date-time      
          type: string      
          x-ngsi:      
            type: Property      
        trip:      
          description: "Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"      
          properties:      
            direction_id:      
              description: "Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
              type: number      
              x-ngsi:      
                type: Property      
            route_id:      
              description: "Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
              type: string      
              x-ngsi:      
                type: Property      
            schedule_relationship:      
              description: "Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)"      
              type: string      
              x-ngsi:      
                type: Property      
            start_date:      
              description: "Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
              type: string      
              x-ngsi:      
                type: Property      
            start_time:      
              description: "Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
              type: string      
              x-ngsi:      
                type: Property      
            trip_id:      
              description: "Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"      
              type: string      
              x-ngsi:      
                type: Property      
          type: object      
          x-ngsi:      
            type: Property      
        vehicleDesc:      
          description: "Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"      
          properties:      
            license_plate:      
              description: "Gives the License Plate number of the vehice.SameAs: 'license_plate' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
              type: string      
              x-ngsi:      
                type: Property      
            vehicle_id:      
              description: "Unique ID assigned to the vehicle corresponding to this observation,used in internal system identification.SameAs: 'id' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
              type: string      
              x-ngsi:      
                type: Property      
            vehicle_label:      
              description: "User visible label,i.e.,something that must be shown to the passenger to help identify the correct vehicle.SameAs: 'label' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
              type: string      
              x-ngsi:      
                type: Property      
          type: object      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/TransitManagement/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/TransitManagement/schema.json      
  x-model-tags: IUDX      
  x-version: 0.0.4      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### TransitManagement NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für ein TransitManagement im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "vehicle_label": "A03",  
  "current_stop_sequence": 1001,  
  "vehicleType": "hopper",  
  "route_color": "00FFFF",  
  "agency_fare_url": "http://charteredbike.in/surat/?page_id=1021",  
  "observationDateTime": "2021-10-28T08:13:22+05:30",  
  "stop_sequence": 24,  
  "route_type": "1",  
  "agency_lang": "en",  
  "start_date": "2022-03-01",  
  "start_time": "11:15:35",  
  "routeStopSequence": [  
    "10",  
    "1001",  
    "1002",  
    "1003",  
    "1004",  
    "1005"  
  ],  
  "direction_id": 0,  
  "actual_trip_start_time": "2021-10-28T07:46:51+05:30",  
  "agency_url": "http://charteredbike.in/surat/",  
  "type": "TransitManagement",  
  "travelTime": "22:11:14",  
  "agency_name": "Chartered Bike Surat",  
  "last_tracked_time": "2021-10-28T08:13:22",  
  "actual_trip_end_time": "2021-10-28T08:24:22+05:30",  
  "trip_id": "23952340",  
  "last_stop_id": "4032",  
  "stop_code": "F12",  
  "current_status": "INCOMING_AT",  
  "agency_timezone": "Asia/Kolkata",  
  "route_id": "17AD",  
  "travelDistance": 9.00174,  
  "tripDirection": "DN",  
  "trip_delay": 11968,  
  "route_long_name": "Baiyappanahalli to Mysuru Road",  
  "bearing": 90,  
  "stop_name": "DEVASHISH NAGAR MORA BHAGAL",  
  "speed": 28,  
  "stop_id": "1016",  
  "arrival_time": "22:00:28",  
  "route_desc": "Phase1-Phase2",  
  "last_stop_arrival_time": "13:30:12",  
  "route_text_color": "FFD700",  
  "id": "https://smart-data-models.github.io/IUDX/TransitManagement/schema.json",  
  "schedule_relationship": "SCHEDULED",  
  "agency_id": "agency001",  
  "license_plate": "GJ05BX1583",  
  "trip_direction": "DN",  
  "route_short_name": "Purple Line",  
  "departure_time": "22:00:33",  
  "standingCapacity": 20,  
  "vehicleID": "52TC12",  
  "depotID": "1",  
  "seatingCapacity": 70,  
  "depotName": "BHESTAN DEPOT",  
  "acAvailable": "yes",  
  "timestamp": "2021-10-28T08:13:22+05:30",  
  "vehicle_id": "52TC12",  
  "standing_capacity": 20,  
  "uncertainity": 0,  
  "ac_available": "yes",  
  "seating_capacity": 70,  
  "depot_id": "1",  
  "depot_name": "BHESTAN DEPOT"  
}  
```  
</details>    
#### TransitManagement NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein TransitManagement im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "https://smart-data-models.github.io/IUDX/TransitManagement/schema.json",  
  "type": "TransitManagement",  
  "vehicleType": {  
    "type": "Text",  
    "value": "hopper"  
  },  
  "trip_delay": {  
    "type": "Number",  
    "value": 11968  
  },  
  "agency_lang": {  
    "type": "Text",  
    "value": "en"  
  },  
  "depot_name": {  
    "type": "Text",  
    "value": "BHESTAN DEPOT"  
  },  
  "travelTime": {  
    "type": "Text",  
    "value": "22:11:14"  
  },  
  "direction_id": {  
    "type": "Boolean",  
    "value": false  
  },  
  "schedule_relationship": {  
    "type": "Text",  
    "value": "SCHEDULED"  
  },  
  "vehicle_id": {  
    "type": "Text",  
    "value": "52TC12"  
  },  
  "agency_fare_url": {  
    "type": "Text",  
    "value": "http://charteredbike.in/surat/?page_id=1021"  
  },  
  "actual_trip_end_time": {  
    "type": "DateTime",  
    "value": "2021-10-28T08:24:22+05:30"  
  },  
  "last_tracked_time": {  
    "type": "Text",  
    "value": "08:13:22"  
  },  
  "standing_capacity": {  
    "type": "Number",  
    "value": 20  
  },  
  "last_stop_arrival_time": {  
    "type": "Text",  
    "value": "13:30:12"  
  },  
  "agency_id": {  
    "type": "Text",  
    "value": "agency001"  
  },  
  "current_status": {  
    "type": "Text",  
    "value": "INCOMING_AT"  
  },  
  "route_type": {  
    "type": "Text",  
    "value": "1"  
  },  
  "speed": {  
    "type": "Number",  
    "value": 28  
  },  
  "route_id": {  
    "type": "Text",  
    "value": "17AD"  
  },  
  "seating_capacity": {  
    "type": "Number",  
    "value": 70  
  },  
  "vehicle_label": {  
    "type": "Text",  
    "value": "A03"  
  },  
  "timestamp": {  
    "type": "DateTime",  
    "value": "2021-10-28T08:13:22+05:30"  
  },  
  "arrival_time": {  
    "type": "Text",  
    "value": "22:00:28"  
  },  
  "route_long_name": {  
    "type": "Text",  
    "value": "Baiyappanahalli to Mysuru Road"  
  },  
  "agency_timezone": {  
    "type": "Text",  
    "value": "Asia/Kolkata"  
  },  
  "stop_code": {  
    "type": "Text",  
    "value": "F12"  
  },  
  "agency_name": {  
    "type": "Text",  
    "value": "Chartered Bike Surat"  
  },  
  "route_desc": {  
    "type": "Text",  
    "value": "Phase1-Phase2"  
  },  
  "license_plate": {  
    "type": "Text",  
    "value": "GJ05BX1583"  
  },  
  "stop_id": {  
    "type": "Text",  
    "value": "1016"  
  },  
  "uncertainity": {  
    "type": "Boolean",  
    "value": false  
  },  
  "route_color": {  
    "type": "Text",  
    "value": "00FFFF"  
  },  
  "travelDistance": {  
    "type": "Number",  
    "value": 9.00174  
  },  
  "actual_trip_start_time": {  
    "type": "DateTime",  
    "value": "2021-10-28T07:46:51+05:30"  
  },  
  "bearing": {  
    "type": "Number",  
    "value": 90  
  },  
  "stop_sequence": {  
    "type": "Number",  
    "value": 24  
  },  
  "start_date": {  
    "type": "DateTime",  
    "value": "2022-03-01"  
  },  
  "current_stop_sequence": {  
    "type": "Number",  
    "value": 1001  
  },  
  "start_time": {  
    "type": "Text",  
    "value": "11:15:35"  
  },  
  "trip_id": {  
    "type": "Text",  
    "value": "23952340"  
  },  
  "route_text_color": {  
    "type": "Text",  
    "value": "FFD700"  
  },  
  "ac_available": {  
    "type": "Text",  
    "value": "yes"  
  },  
  "tripDirection": {  
    "type": "Text",  
    "value": "DN"  
  },  
  "agency_url": {  
    "type": "Text",  
    "value": "http://charteredbike.in/surat/"  
  },  
  "routeStopSequence": {  
    "type": "StructuredValue",  
    "value": [  
      "10",  
      "1001",  
      "1002",  
      "1003",  
      "1004",  
      "1005"  
    ]  
  },  
  "trip_direction": {  
    "type": "Text",  
    "value": "DN"  
  },  
  "departure_time": {  
    "type": "Text",  
    "value": "22:00:33"  
  },  
  "last_stop_id": {  
    "type": "Text",  
    "value": "4032"  
  },  
  "route_short_name": {  
    "type": "Text",  
    "value": "Purple Line"  
  },  
  "stop_name": {  
    "type": "Text",  
    "value": "DEVASHISH NAGAR MORA BHAGAL"  
  },  
  "depot_id": {  
    "type": "Text",  
    "value": "1"  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2021-10-28T08:13:22+05:30"  
  }  
}  
```  
</details>    
#### TransitManagement NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für ein TransitManagement im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "vehicle_label": "A03",  
  "current_stop_sequence": 1001,  
  "vehicleType": "hopper",  
  "route_color": "00FFFF",  
  "agency_fare_url": "http://charteredbike.in/surat/?page_id=1021",  
  "observationDateTime": "2021-10-28T08:13:22+05:30",  
  "stop_sequence": 24,  
  "route_type": "1",  
  "agency_lang": "en",  
  "start_date": "2022-03-01",  
  "start_time": "11:15:35",  
  "routeStopSequence": [  
    "10",  
    "1001",  
    "1002",  
    "1003",  
    "1004",  
    "1005"  
  ],  
  "direction_id": 0,  
  "actual_trip_start_time": "2021-10-28T07:46:51+05:30",  
  "agency_url": "http://charteredbike.in/surat/",  
  "type": "TransitManagement",  
  "travelTime": "22:11:14",  
  "agency_name": "Chartered Bike Surat",  
  "last_tracked_time": "2021-10-28T08:13:22",  
  "actual_trip_end_time": "2021-10-28T08:24:22+05:30",  
  "trip_id": "23952340",  
  "last_stop_id": "4032",  
  "stop_code": "F12",  
  "current_status": "INCOMING_AT",  
  "agency_timezone": "Asia/Kolkata",  
  "route_id": "17AD",  
  "travelDistance": 9.00174,  
  "tripDirection": "DN",  
  "trip_delay": 11968,  
  "route_long_name": "Baiyappanahalli to Mysuru Road",  
  "bearing": 90,  
  "stop_name": "DEVASHISH NAGAR MORA BHAGAL",  
  "speed": 28,  
  "stop_id": "1016",  
  "arrival_time": "22:00:28",  
  "route_desc": "Phase1-Phase2",  
  "last_stop_arrival_time": "13:30:12",  
  "route_text_color": "FFD700",  
  "id": "https://smart-data-models.github.io/IUDX/TransitManagement/schema.json",  
  "schedule_relationship": "SCHEDULED",  
  "agency_id": "agency001",  
  "license_plate": "GJ05BX1583",  
  "trip_direction": "DN",  
  "route_short_name": "Purple Line",  
  "departure_time": "22:00:33",  
  "standingCapacity": 20,  
  "vehicleID": "52TC12",  
  "depotID": "1",  
  "seatingCapacity": 70,  
  "depotName": "BHESTAN DEPOT",  
  "acAvailable": "yes",  
  "timestamp": "2021-10-28T08:13:22+05:30",  
  "vehicle_id": "52TC12",  
  "standing_capacity": 20,  
  "uncertainity": 0,  
  "ac_available": "yes",  
  "seating_capacity": 70,  
  "depot_id": "1",  
  "depot_name": "BHESTAN DEPOT",  
  "@context": [  
    "iudx:TransitManagement",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### TransitManagement NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein TransitManagement im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "https://smart-data-models.github.io/IUDX/TransitManagement/schema.json",  
  "type": "TransitManagement",  
  "vehicleType": {  
    "type": "Property",  
    "value": "hopper"  
  },  
  "trip_delay": {  
    "type": "Property",  
    "value": 11968  
  },  
  "agency_lang": {  
    "type": "Property",  
    "value": "en"  
  },  
  "depot_name": {  
    "type": "Property",  
    "value": "BHESTAN DEPOT"  
  },  
  "travelTime": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "22:11:14"  
    }  
  },  
  "direction_id": {  
    "type": "Property",  
    "value": "false"  
  },  
  "schedule_relationship": {  
    "type": "Property",  
    "value": "SCHEDULED"  
  },  
  "vehicle_id": {  
    "type": "Property",  
    "value": "52TC12"  
  },  
  "agency_fare_url": {  
    "type": "Property",  
    "value": "http://charteredbike.in/surat/?page_id=1021"  
  },  
  "actual_trip_end_time": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2021-10-28T08:24:22+05:30"  
    }  
  },  
  "last_tracked_time": {  
    "type": "Property",  
    "value": {  
      "@type": "time",  
      "@value": "08:13:22"  
    }  
  },  
  "standing_capacity": {  
    "type": "Property",  
    "value": 20  
  },  
  "last_stop_arrival_time": {  
    "type": "Property",  
    "value": {  
      "@type": "time",  
      "@value": "13:30:12"  
    }  
  },  
  "agency_id": {  
    "type": "Property",  
    "value": "agency001"  
  },  
  "current_status": {  
    "type": "Property",  
    "value": "INCOMING_AT"  
  },  
  "route_type": {  
    "type": "Property",  
    "value": "1"  
  },  
  "speed": {  
    "type": "Property",  
    "value": 28  
  },  
  "route_id": {  
    "type": "Property",  
    "value": "17AD"  
  },  
  "seating_capacity": {  
    "type": "Property",  
    "value": 70  
  },  
  "vehicle_label": {  
    "type": "Property",  
    "value": "A03"  
  },  
  "timestamp": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2021-10-28T08:13:22+05:30"  
    }  
  },  
  "arrival_time": {  
    "type": "Property",  
    "value": {  
      "@type": "time",  
      "@value": "22:00:28"  
    }  
  },  
  "route_long_name": {  
    "type": "Property",  
    "value": "Baiyappanahalli to Mysuru Road"  
  },  
  "agency_timezone": {  
    "type": "Property",  
    "value": "Asia/Kolkata"  
  },  
  "stop_code": {  
    "type": "Property",  
    "value": "F12"  
  },  
  "agency_name": {  
    "type": "Property",  
    "value": "Chartered Bike Surat"  
  },  
  "route_desc": {  
    "type": "Property",  
    "value": "Phase1-Phase2"  
  },  
  "license_plate": {  
    "type": "Property",  
    "value": "GJ05BX1583"  
  },  
  "stop_id": {  
    "type": "Property",  
    "value": "1016"  
  },  
  "uncertainity": {  
    "type": "Property",  
    "value": "false"  
  },  
  "route_color": {  
    "type": "Property",  
    "value": "00FFFF"  
  },  
  "travelDistance": {  
    "type": "Property",  
    "value": 9.00174  
  },  
  "actual_trip_start_time": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2021-10-28T07:46:51+05:30"  
    }  
  },  
  "bearing": {  
    "type": "Property",  
    "value": 90  
  },  
  "stop_sequence": {  
    "type": "Property",  
    "value": 24  
  },  
  "start_date": {  
    "type": "Property",  
    "value": {  
      "@type": "date",  
      "@value": "2022-03-01"  
    }  
  },  
  "current_stop_sequence": {  
    "type": "Property",  
    "value": 1001  
  },  
  "start_time": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "11:15:35"  
    }  
  },  
  "trip_id": {  
    "type": "Property",  
    "value": "23952340"  
  },  
  "route_text_color": {  
    "type": "Property",  
    "value": "FFD700"  
  },  
  "ac_available": {  
    "type": "Property",  
    "value": "yes"  
  },  
  "tripDirection": {  
    "type": "Property",  
    "value": "DN"  
  },  
  "agency_url": {  
    "type": "Property",  
    "value": "http://charteredbike.in/surat/"  
  },  
  "routeStopSequence": {  
    "type": "Property",  
    "value": [  
      "10",  
      "1001",  
      "1002",  
      "1003",  
      "1004",  
      "1005"  
    ]  
  },  
  "trip_direction": {  
    "type": "Property",  
    "value": "DN"  
  },  
  "departure_time": {  
    "type": "Property",  
    "value": {  
      "@type": "time",  
      "@value": "22:00:33"  
    }  
  },  
  "last_stop_id": {  
    "type": "Property",  
    "value": "4032"  
  },  
  "route_short_name": {  
    "type": "Property",  
    "value": "Purple Line"  
  },  
  "stop_name": {  
    "type": "Property",  
    "value": "DEVASHISH NAGAR MORA BHAGAL"  
  },  
  "depot_id": {  
    "type": "Property",  
    "value": "1"  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2021-10-28T08:13:22+05:30"  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
