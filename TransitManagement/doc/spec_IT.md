<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: TransitManagement  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/TransitManagement/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Modello di dati di un sistema di trasporto pubblico**  
versione: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `ac_available[string]`: Descrive la presenza dell'opzione di climatizzazione nel veicolo corrispondente a questa osservazione.  - `actual_trip_end_time[string]`: Questo campo specifica l'ora in cui è prevista la fine del servizio o del viaggio corrispondente a questa osservazione.  - `actual_trip_start_time[string]`: Questo campo specifica l'ora in cui il servizio è effettivamente iniziato.  È identico a: "tempo" assoluto (StopTimeEvent) nel campo "arrivo" del messaggio stop_time_update (StopTimeUpdate) del messaggio GTFS Realtime-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate).  - `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `agency_fare_url[string]`: URL di una pagina web che contiene i dettagli delle tariffe e che può consentire di acquistare online i biglietti di quell'agenzia. Come: Campo 'agency_fare_url' da GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_id[string]`: ID che identifica in modo univoco un'agenzia di transito. Un feed di transito può rappresentare i dati di più di un'agenzia. L'ID agenzia è unico per il set di dati. Questo campo è facoltativo per i feed di transito che contengono dati di una sola agenzia. Uguale a: Campo 'agency_id' da GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_lang[string]`: Contiene un codice ISO 639-1 di due lettere per la lingua principale utilizzata dall'agenzia di transito. Il codice della lingua non fa distinzione tra maiuscole e minuscole (sono accettati sia en che EN). Uguale a: Campo 'agency_lang' da GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_name[string]`: Il campo nome_agenzia contiene il nome completo dell'agenzia di transito. Uguale a: campo 'agency_name' da GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_timezone[string]`: Il campo Timezone contiene il fuso orario in cui si trova l'agenzia di transito. Uguale a: Campo 'agency_timezone' da GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_url[string]`: Il campo agency_url contiene l'URL dell'agenzia di transito. Uguale a: Campo 'agency_url' da GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrival[object]`: Se schedule_relationship è vuota o SCHEDULED, l'arrivo o la partenza devono essere forniti all'interno di uno StopTimeUpdate. Come: campo 'arrival' del messaggio in tempo reale GTFS StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate).  - `arrival_time[string]`: Specifica l'orario di arrivo a una fermata specifica per un viaggio specifico su un percorso. Gli orari devono essere di otto cifre nel formato HH:MM:SS (è accettato anche HH:MM:SS, se l'ora inizia con 0). Nota: i viaggi che si estendono su più date avranno orari di fermata superiori a 24:00:00. Ad esempio, se un viaggio inizia alle 22:30 e termina alle 2:15 del giorno successivo, gli orari di fermata saranno 22:30 e 26:15. Inserendo questi orari di fermata come 22:30:00 e 02:15:00 non si otterrebbero i risultati desiderati. Stessa cosa: Campo 'arrival_time' da GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `bearing[number]`: Indica l'angolo GPS del veicolo misurato in senso orario rispetto al Nord vero. Come il campo "bearing" del messaggio di posizione in tempo reale GTFS (https://developers.google.com/transit/gtfs-realtime/reference#message-position).  - `current_status[string]`: Descrive lo stato del veicolo rispetto alla fermata corrispondente a questa osservazione ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. Come: campo "current_status" del messaggio in tempo reale GTFS-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition).  - `current_stop_sequence[number]`: Fornisce l'indice di sequenza della fermata corrente. Viene determinato considerando current_status, se current_status manca si assume IN_TRANSIT_TO. Come: campo "current_stop_sequence" del messaggio GTFS Realtime-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition).  - `dataDescriptor[string]`: URI che punta all'entità descrittore di dati  - `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `departure[object]`: Se schedule_relationship è vuota o SCHEDULED, l'arrivo o la partenza devono essere forniti all'interno di uno StopTimeUpdate. Stesso discorso per il campo "departure" del messaggio GTFS Realtime StopTimeUpdate (): campo 'departure' del messaggio GTFS Realtime-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate).  - `departure_time[string]`: Specifica l'orario di partenza da una fermata specifica per un viaggio specifico su un percorso. Gli orari devono essere di otto cifre nel formato HH:MM:SS (è accettato anche HH:MM:SS, se l'ora inizia con 0).  
Nota: i viaggi che si estendono su più date avranno orari di fermata superiori a 24:00:00. Ad esempio, se un viaggio inizia alle 22:30 e termina alle 2:15 del giorno successivo, gli orari di sosta saranno 22:30 e 26:15. Inserendo questi orari di fermata come 22:30:00 e 02:15:00 non si otterrebbero i risultati desiderati. Stessa cosa: Campo 'departure_time' da GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `depot_id[string]`: Descrive l'id univoco del deposito di autobus corrispondente a questa osservazione.  - `depot_name[string]`: Descrive il nome del deposito dell'autobus corrispondente a questa osservazione.  - `description[string]`: Descrizione dell'articolo  - `deviceInfo[object]`: Informazioni sul dispositivo associato alle osservazioni.  . Model: [https://schema.org/Text](https://schema.org/Text)- `direction_id[number]`: Indica la direzione di marcia del veicolo corrispondente a questa osservazione; può essere riferito dal feed statico GTFS trips.txt. Uguale a: campo 'direction_id' del messaggio GTFS Realtime-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor).  - `entity_id[string]`: ID univoco del feed per l'entità corrispondente a questa osservazione.SameAs: campo 'entity_id' da GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  - `id[*]`: Identificatore univoco dell'entità  - `last_stop_arrival_time[string]`: Specifica l'ora di arrivo alla fermata precedente per un viaggio specifico su un percorso. Gli orari devono essere di otto cifre nel formato HH:MM:SS (è accettato anche H:MM:SS, se l'ora inizia con 0).  
Nota: i viaggi che coprono più date avranno orari di fermata maggiori di 24:00:00. Ad esempio, se un viaggio inizia alle ore 24:00:00, l'orario di partenza deve essere quello della fermata precedente. Ad esempio, se un viaggio inizia alle 22:30 e termina alle 2:15 del giorno successivo, gli orari di sosta saranno le 22:30 e le 26:15. Immettere questi orari di fermata come 22:30:00 e 02:15:00 non produrrebbe i risultati desiderati. Questo è SameAs: "tempo" assoluto (StopTimeEvent) nel campo "arrivo" del messaggio stop_time_update (StopTimeUpdate) del messaggio GTFS Realtime-TripUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate).  - `last_stop_id[string]`: ID fermata/nome fermata della fermata precedente corrispondente all'autobus oggetto dell'osservazione. Uguale a: campo 'stop_id' del messaggio in tempo reale GTFS-VehiclePosition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition).  - `last_tracked_time[string]`: Indica l'ora in cui il veicolo è stato tracciato per l'ultima volta.  - `license_plate[string]`: Indica il numero di targa del veicolo. Uguale a: campo 'license_plate' del messaggio in tempo reale GTFS-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor).  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `observationDateTime[string]`: Ultimo momento di osservazione segnalato.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `position[object]`: Descrive la posizione attuale del veicolo corrispondente a questa osservazione. Idem: campo position del messaggio in tempo reale GTFS-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition).  . Model: [https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition](https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)- `routeStopSequence[array]`: Fornisce gli ID delle fermate/codici delle fermate o gli ID delle stazioni/codici delle stazioni nella giusta sequenza per il percorso o la linea corrispondente a questa osservazione.  - `route_color[string]`: Se assegnato, questo campo definisce un colore che corrisponde a un percorso. Il colore deve essere fornito come numero esadecimale di sei caratteri, ad esempio 00FFFF. Se non viene specificato alcun colore, il colore predefinito della rotta è il bianco (FFFFFF). Uguale a: Campo 'route_color' da GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_desc[string]`: Descrizione del percorso. Può includere tutti i dettagli del percorso, comprese le informazioni sulla destinazione e sulla tempistica, in forma di descrizione testuale. Come: Campo 'route_desc' da GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_id[string]`: ID percorso assegnato al percorso su cui sta circolando l'autobus/veicolo corrispondente all'autobus oggetto dell'osservazione. Uguale a: campo 'route_id' del messaggio GTFS Realtime-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor).  - `route_long_name[string]`: Nome completo di un percorso. Questo nome è più descrittivo di routeShortName e spesso include la destinazione o la fermata del percorso. Include soprattutto i nomi delle destinazioni da e verso il percorso. Uguale a: Campo 'route_long_name' da GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_short_name[string]`: Nome breve di un percorso. Spesso si tratta del nome del veicolo di transito, come "402D" o "Green", che gli utenti usano per identificare un percorso. Uguale a: Campo 'route_short_name' da GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_text_color[string]`: Questo campo può essere usato per specificare un colore leggibile da usare per il testo disegnato su uno sfondo di colore_percorso. Il colore deve essere fornito come numero esadecimale di sei caratteri, ad esempio FFD700. Se non viene specificato alcun colore, il colore predefinito del testo è il nero (000000). Uguale a: Campo 'route_text_color' da GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_type[string]`: Numero che indica il tipo di trasporto-1 - Metropolitana, Metro. Qualsiasi sistema ferroviario sotterraneo all'interno di un'area metropolitana.2 - Ferrovia. Utilizzato per viaggi interurbani o a lunga distanza.3 - Autobus. Utilizzato per le linee di autobus a breve e lunga percorrenza. Uguale a: Campo 'route_type' da GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `route_url[string]`: Contiene l'URL di una pagina web relativa a quel particolare percorso ed è diverso da agency_url. Uguale a: Campo 'route_url' da GTFS Static Field definitions-routes.txt (https://developers.google.com/transit/gtfs/reference#routestxt)  - `schedule_relationship[string]`: Descrive se il percorso/viaggio è stato pianificato. Uguale a: Campo 'schedule_relationship' da enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)  - `seating_capacity[number]`: Descrive la capacità di posti a sedere del veicolo corrispondente a questa osservazione.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `speed[number]`: Fornisce la velocità del veicolo. Come il campo "velocità" del messaggio in tempo reale GTFS-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position).  - `standing_capacity[number]`: Descrive la capacità di carico del veicolo corrispondente a questa osservazione.  - `start_date[string]`: Descrive la data iniziale programmata del viaggio corrispondente al veicolo oggetto dell'osservazione. Un esempio di formato per questo campo è YYYYMMDD. Uguale a: campo 'start_date' di GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor).  - `start_time[string]`: Descrive l'orario iniziale programmato di inizio del viaggio corrispondente al veicolo oggetto dell'osservazione. Un esempio di formato per questo campo è 11:15:35 o 25:15:35. Uguale a: campo 'start_time' di GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor).  - `stop_code[string]`: Questo campo contiene un breve testo o un numero che identifica in modo univoco la fermata per i passeggeri. Può essere uguale a stop_id se si tratta di una fermata pubblica. Uguale a: Campo 'stop_code' da GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_desc[string]`: Questo campo contiene la descrizione di una fermata. Uguale a: Campo 'stop_desc' da GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_headsign[string]`: Questo campo contiene il testo che appare su un cartello che identifica la destinazione del viaggio ai passeggeri. Uguale a: Campo 'stop_headsign' da GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `stop_id[string]`: ID fermata/nome fermata delle fermate corrispondenti all'autobus in questa osservazione. Uguale a: campo 'stop_id' del messaggio in tempo reale GTFS-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition).  - `stop_name[string]`: Descrive il nome della fermata dell'autobus. Uguale a: campo 'stop_name' da GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `stop_sequence[number]`: Indica la sequenza di arresto del veicolo corrispondente a questa osservazione, che può essere ricavata dal file statico GTFS stop_times.txt. Uguale a: campo 'stop_sequence' del messaggio GTFS Realtime-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate).  - `stop_sequence_detail[object]`: Descrive la sequenza di fermate per un viaggio nel percorso designato effettuato dal veicolo di trasporto pubblico: Campo 'stop_sequence' da GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)  - `stop_time_update[object]`: Informazioni aggiuntive sul veicolo che sta effettuando il viaggio.  - `stop_url[string]`: Questo campo contiene l'URL di una pagina web relativa a una particolare fermata ed è diverso dai campi agency_url e route_url. Uguale a: Campo 'stop_url' da GTFS Static Field definitions-stops.txt (https://developers.google.com/transit/gtfs/reference#stopstxt)  - `timestamp[string]`: Ultimo momento di osservazione segnalato dal veicolo. Uguale a: campo 'timestamp' del messaggio in tempo reale GTFS-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition).  - `travelDistance[number]`: La distanza tra la fermata dell'autobus di origine e quella di destinazione o la distanza totale percorsa corrispondente a questa osservazione.  - `travelTime[string]`: Il tempo di percorrenza tra la fermata dell'autobus di origine e la fermata dell'autobus di destinazione corrispondente a questa osservazione nel formato HH:MM:SS (è accettato anche HH:MM:SS, se l'ora inizia con 0).  - `trip[object]`: Descrive il viaggio che il veicolo corrispondente a questa osservazione sta compiendo. Come: campo "viaggio" del messaggio in tempo reale GTFS-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)  - `tripDetails[object]`: Descrittore dell'aggiornamento in tempo reale della tabella di marcia di un veicolo lungo un viaggio.  - `tripDirection[string]`: Indica la direzione di marcia del veicolo ENUM[UP,DN]  - `trip_delay[number]`: Può essere positivo o negativo in secondi e mostra quanto il veicolo si discosta da quello pianificato. Uguale a: campo 'delay' da GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)  - `trip_details[object]`: Descrittore dell'aggiornamento in tempo reale della tabella di marcia di un veicolo lungo un viaggio.  - `trip_direction[string]`: Indica la direzione di marcia del veicolo. Uguale a: campo 'direction_id' del messaggio GTFS Realtime-TripDescriptor, ma è rappresentato sotto forma di ENUM[UP,DN] invece di [0,1] come visto in 'direction_id' (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor).  - `trip_id[string]`: ID viaggio/nome del viaggio assegnato all'autobus corrispondente a questa osservazione, in considerazione dell'ora del giorno e della direzione del viaggio sul routeId dato. Uguale a: campo 'trip_id' da GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  - `trip_update[object]`: Descrive le informazioni sul viaggio, come il ritardo, le partenze, ecc. per un viaggio effettuato dal veicolo corrispondente a questa osservazione.  - `type[string]`: Tipo di entità NGSI. Deve essere TransitManagement  - `uncertainty[number]`: Se l'incertezza viene omessa, viene interpretata come sconosciuta. Per specificare una previsione completamente certa, impostare l'incertezza a 0,SameAs: campo 'uncertainty' da GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)  - `vehicleDesc[object]`: Descrive le informazioni aggiuntive del veicolo corrispondente a questa osservazione. Stessa cosa: campo "veicolo" del messaggio in tempo reale GTFS-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate).  - `vehicleType[string]`: Descrive il tipo di veicolo corrispondente a questa osservazione, che può essere una tramoggia, un compattatore, un cassone ribaltabile, un dumper nel caso di veicoli per la gestione dei rifiuti solidi, un minibus BRT, un autobus BRT, un autobus urbano nel caso di veicoli ITMS, un'ambulanza, un'autopompa, un furgone della polizia, ecc. nel caso di veicoli di emergenza e un ciclomotore/scooter, un motociclo, un autocarro, un'autovettura privata/un'autovettura Jeep, un autobus, un ciclomotore/un motociclo, un'autovettura pubblica nel caso di immatricolazione del veicolo.  - `vehicle_id[string]`: ID univoco assegnato al veicolo corrispondente a questa osservazione, utilizzato per l'identificazione interna del sistema. Uguale a: campo 'id' del messaggio in tempo reale GTFS-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor).  - `vehicle_label[string]`: Etichetta visibile all'utente, cioè qualcosa che deve essere mostrato al passeggero per aiutare a identificare il veicolo corretto. Uguale a: campo 'label' del messaggio in tempo reale GTFS-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  - `vehicle_position[object]`: Descrive la posizione in tempo reale del veicolo corrispondente a questa osservazione. SameAs: campo "vehicle" da GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TransitManagement:    
  description: 'A public transit system Data Model'    
  properties:    
    ac_available:    
      description: 'Describes the presence of air conditioning option in the vehicle corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    actual_trip_end_time:    
      description: 'This field specifies the time at which service or trip corresponding to this observation is scheduled to end.'    
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
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
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
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    arrival:    
      description: "If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'arrival' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"    
      properties:    
        uncertainty:    
          description: "Property. If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)."    
          type: number    
      type: object    
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
      description: 'URI pointing to the data-descriptor entity'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    departure:    
      description: "If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate. SameAs: 'departure' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)"    
      properties:    
        uncertainty:    
          description: "Property. If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)."    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    departure_time:    
      description: "Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). \nNote: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
      format: time    
      type: string    
      x-ngsi:    
        type: Property    
    depot_id:    
      description: 'Describes the unique id of the bus depot corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    depot_name:    
      description: 'Describes the depot name of the bus depot corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    deviceInfo:    
      description: 'Information about the device associated with the observations.'    
      properties:    
        deviceBatteryStatus:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the Battery charging status of the reporting device(Connected, Disconnected).'    
          type: string    
        deviceID:    
          description: 'Property. Model:''https://schema.org/Text''. Device ID of the physical sensor/ measurement station corresponding to this observation.'    
          type: string    
        deviceModel:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the information of the device, sensor or system in consideration.'    
          properties:    
            brandName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of the brand associated with an entity, e.g., sensor, device etc.'    
              type: string    
            manufacturerName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of the manufacturer associated with an entity, e.g., sensor, device etc.'    
              type: string    
            modelName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of a specific model associated with an entity, e.g., sensor, device etc.'    
              type: string    
            modelURL:    
              description: 'Property. Model:''https://schema.org/Text''. URL providing further information of a specific model associated with an entity, e.g., sensor, device etc.'    
              type: string    
            observationDateTime:    
              description: 'Property. Last reported time of observation.'    
              format: date-time    
              type: string    
            trip_update:    
              description: "Property. Describes the trip information like delay, departures, etc., for a trip made by the vehicle corresponding to this observation.SameAs:'trip_update' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"    
              properties:    
                trip:    
                  description: "Property. Following the conventions of GTFS trip. Model:'https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor'. "    
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
              type: object    
          type: object    
        deviceName:    
          description: 'Property. Model:''https://schema.org/Text''. Device Name or Station name of the sensor device/station corresponding to this observation.'    
          type: string    
        deviceSimNumber:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the sim number of the device in the waste management vehicle.'    
          type: string    
        measurand:    
          description: 'Property. Model:''https://schema.org/Text''. Property/properties sensed/observed/measured by the device.'    
          type: string    
        rfID:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the ID of the RFID reader.'    
          type: string    
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
      description: "Feed unique ID for the entity corressponding to this observation.SameAs:'entity_id' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)"    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &transitmanagement_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
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
      description: 'Gives the time at which the vehicle was last tracked.'    
      format: time    
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
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *transitmanagement_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    position:    
      description: "Describes the current position of the vehicle corresponding to this observation. SameAs: position field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
      properties:    
        bearing:    
          description: 'Property. Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data'    
          type: number    
        latitude:    
          description: 'Property. Degrees North, in the WGS-84 coordinate system.'    
          type: number    
        longitude:    
          description: 'Property. Degrees East, in the WGS-84 coordinate system.'    
          type: number    
        odometer:    
          description: 'Property. Odometer value, in meters. Units:''meters'''    
          type: number    
        speed:    
          description: 'Property. Momentary speed measured by the vehicle, in meters per second. Units:''meters per second'''    
          type: number    
      type: object    
      x-ngsi:    
        model: "https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition"    
        type: Property    
    routeStopSequence:    
      description: 'Gives the stop IDs/stop codes or station IDs/station codes in the right sequence for the route or line corresponding to this observation.'    
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
      description: 'Describes the passenger seating capacity of the vehicle corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    speed:    
      description: "Gives the Speed  of the vehicle. SameAs 'speed' field from GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)"    
      type: number    
      x-ngsi:    
        type: Property    
    standing_capacity:    
      description: 'Describes the passenger standing capacity of the vehicle corresponding to this observation.'    
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
          description: 'Property. Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty.'    
          type: string    
        stop_sequence:    
          description: 'Property. Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for.'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    stop_time_update:    
      description: 'Additional information on the vehicle that is serving this trip.'    
      properties:    
        arrival:    
          description: 'Property. If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty.'    
          properties:    
            uncertainty:    
              description: "Property. If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)."    
              type: number    
          type: object    
        departure:    
          description: 'Property. If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty.'    
          properties:    
            uncertainty:    
              description: "Property. If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)."    
              type: number    
          type: object    
        schedule_relationship:    
          description: 'Property. Enum:''SCHEDULED, SKIPPED, NO_DATA''. SCHEDULED means that the vehicle is proceeding in accordance with its static schedule of stops, although not necessarily according to the times of the schedule. This is the default behavior. At least one of arrival and departure must be provided. SKIPPED means that The stop is skipped, i.e., the vehicle will not stop at this stop. The arrival and departure fields are optional. NO_DATA means that no data is given for this stop. It indicates that there is no realtime information available. When set NO_DATA is propagated through subsequent stops so this is the recommended way of specifying from which stop you do not have realtime information. When NO_DATA is set neither arrival nor departure should be supplied.'    
          enum:    
            - SCHEDULED    
            - SKIPPED    
            - NO_DATA    
          type: string    
        stop_id:    
          description: 'Property. Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty.'    
          type: string    
        stop_sequence:    
          description: 'Property. Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for.'    
          type: number    
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
      description: 'The distance between the origin bus stop and the destination bus stop or the total distance travelled corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    travelTime:    
      description: 'The time taken to travel between the origin bus stop and the destination bus stop corresponding to this observation in HH:MM:SS format(HH:MM:SS is also accepted, if the hour begins with 0).'    
      format: time    
      type: string    
      x-ngsi:    
        type: Property    
    trip:    
      description: "Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)"    
      properties:    
        direction_id:    
          description: "Property. Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
          type: number    
        route_id:    
          description: "Property. Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
          type: string    
        schedule_relationship:    
          description: "Property. Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)."    
          type: string    
        start_date:    
          description: "Property. Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
          type: string    
        start_time:    
          description: "Property. Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
          type: string    
        trip_id:    
          description: "Property. Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
    tripDetails:    
      description: 'A descriptor of realtime update on the schedule of a vehicle along a trip.'    
      properties:    
        arrival_time:    
          description: "Property.  Specifies the arrival time at a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'arrival_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)."    
          format: time    
          type: string    
        departure_time:    
          description: "Property. Specifies the departure time from a specific stop for a specific trip on a route. Times must be eight digits in HH:MM:SS format (HH:MM:SS is also accepted, if the hour begins with 0). Note: Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. SameAs: 'departure_time' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)."    
          format: time    
          type: string    
        stop_headsign:    
          description: "Property. This field contains the text that appears on a sign that identifies the trip’s destination to passengers. SameAs: 'stop_headsign' field from GTFS Static Field definitions-stop_times.txt (https://developers.google.com/transit/gtfs/reference#stop_timestxt)"    
          type: string    
        stop_id:    
          description: "Property. Stop ID/Stop name of the bus stops corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)"    
          type: string    
        stop_sequence:    
          description: "Property. Indicates the stop sequence of the vehicle corresponding to this observation, can be referenced from the GTFS static feed stop_times.txt. SameAs: 'stop_sequence' field from GTFS Realtime message-StopTimeUpdate (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeupdate)."    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    tripDirection:    
      description: 'Gives the direction in which the vehicle is travelling in ENUM[UP,DN]'    
      type: string    
      x-ngsi:    
        type: Property    
    trip_delay:    
      description: "This can be positive and negative in seconds and shows how much the vehicle deviates from the planned one. SameAs: 'delay' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)"    
      type: number    
      x-ngsi:    
        type: Property    
    trip_details:    
      description: 'A descriptor of realtime update on the schedule of a vehicle along a trip.'    
      properties:    
        bearing:    
          description: 'Property. Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data'    
          type: number    
        odometer:    
          description: 'Property. Odometer value, in meters. Units:''meters'''    
          type: number    
        speed:    
          description: 'Property. Momentary speed measured by the vehicle, in meters per second. Units:''meters per second'''    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    trip_direction:    
      description: "Gives the direction in which the vehicle is travelling. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor but is represented in the form of an ENUM[UP,DN] in place of [0,1] as seen in 'direction_id' (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
      type: string    
      x-ngsi:    
        type: Property    
    trip_id:    
      description: "Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: string    
      x-ngsi:    
        type: Property    
    trip_update:    
      description: "Describes the trip information like delay, departures, etc., for a trip made by the vehicle corresponding to this observation.SameAs:'trip_update' field from GTFS Realtime message-FeedEntity(https://developers.google.com/transit/gtfs-realtime/reference#message-feedentity)."    
      properties:    
        stop_time_update:    
          description: 'Property. Additional information on the vehicle that is serving this trip.'    
          properties:    
            arrival:    
              description: 'Property. If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty.'    
              properties:    
                uncertainty:    
                  description: "Property. If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)."    
                  type: number    
              type: object    
            departure:    
              description: 'Property. If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. If schedule_relationship is NO_DATA, arrival and departure must be empty.'    
              properties:    
                uncertainty:    
                  description: "Property. If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.SameAs: 'uncertainty' field from GTFS Realtime message-StopTimeEvent (https://developers.google.com/transit/gtfs-realtime/reference#message-stoptimeevent)."    
                  type: number    
              type: object    
            schedule_relationship:    
              description: 'Property. Enum:''SCHEDULED, SKIPPED, NO_DATA''. SCHEDULED means that the vehicle is proceeding in accordance with its static schedule of stops, although not necessarily according to the times of the schedule. This is the default behavior. At least one of arrival and departure must be provided. SKIPPED means that The stop is skipped, i.e., the vehicle will not stop at this stop. The arrival and departure fields are optional. NO_DATA means that no data is given for this stop. It indicates that there is no realtime information available. When set NO_DATA is propagated through subsequent stops so this is the recommended way of specifying from which stop you do not have realtime information. When NO_DATA is set neither arrival nor departure should be supplied.'    
              enum:    
                - SCHEDULED    
                - SKIPPED    
                - NO_DATA    
              type: string    
            stop_id:    
              description: 'Property. Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty.'    
              type: string    
            stop_sequence:    
              description: 'Property. Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for.'    
              type: number    
          type: object    
        timestamp:    
          description: "Property. Last reported time of observation from the vehicle. SameAs: 'timestamp' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)."    
          format: date-time    
          type: string    
        trip:    
          description: "Property. Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)."    
          properties:    
            direction_id:    
              description: "Property. Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: number    
            route_id:    
              description: "Property. Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
            schedule_relationship:    
              description: "Property. Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)."    
              type: string    
            start_date:    
              description: "Property. Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
            start_time:    
              description: "Property. Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
            trip_id:    
              description: "Property. Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
          type: object    
        vehicleDesc:    
          description: "Property. Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)."    
          properties:    
            license_plate:    
              description: "Property. Gives the License Plate number of the vehice.SameAs: 'license_plate' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
            vehicle_id:    
              description: "Property. Unique ID assigned to the vehicle corresponding to this observation,used in internal system identification.SameAs: 'id' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
            vehicle_label:    
              description: "Property. User visible label,i.e.,something that must be shown to the passenger to help identify the correct vehicle.SameAs: 'label' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
          type: object    
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be TransitManagement'    
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
          description: "Property. Gives the License Plate number of the vehice.SameAs: 'license_plate' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
          type: string    
        vehicle_id:    
          description: "Property. Unique ID assigned to the vehicle corresponding to this observation,used in internal system identification.SameAs: 'id' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
          type: string    
        vehicle_label:    
          description: "Property. User visible label,i.e.,something that must be shown to the passenger to help identify the correct vehicle.SameAs: 'label' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
    vehicleType:    
      description: 'Describes the type of vehicle corresponding to this observation, could be hopper, compactor, tipper, dumper in case of solid waste management vehicles, BRT mini bus, BRT bus, city bus in case of ITMS vehicles, Ambulance, Fire tender, Police van etc, in case of emergency vehicles and Moped/Scooter, Motor Cycle,  Autorickshaw, Private car/ Jeep car, Tempo, Bus, E-Moped/E-Scooter/E-Motor Cycle, Public motor in case of vehicle registration.'    
      enum:    
        - agriculturalVehicle    
        - ambulance    
        - anyVehicle    
        - articulatedVehicle    
        - autorickshaw    
        - bicycle    
        - binTrolley    
        - 'BRT mini bus·'    
        - 'BRT bus'    
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
          description: "Property. Describes the status of the vehicle w.r.t the stop corresponding to this observation ENUM: [INCOMING_AT, STOPPED_AT, IN_TRANSIT_TO]. SameAs:'current_status' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)."    
          type: string    
        current_stop_sequence:    
          description: "Property. Gives the stop sequence index of the current stop. This is determined by considering current_status, if current_status is missing IN_TRANSIT_TO is assumed. SameAs:'current_stop_sequence' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)."    
          type: number    
        position:    
          description: "Property. Describes the current position of the vehicle corresponding to this observation. SameAs: 'position' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)."    
          properties: {}    
          type: object    
        stop_id:    
          description: "Property. Stop ID/Stop name of the bus stops corresponding to the bus in this observation. SameAs: 'stop_id' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)."    
          type: string    
        timestamp:    
          description: "Property. Last reported time of observation from the vehicle. SameAs:  'timestamp' field from GTFS Realtime message-Vehicleposition (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)."    
          format: date-time    
          type: string    
        trip:    
          description: "Property. Describes the trip the vehicle corresponding to this observation is making. SameAs:'trip' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)."    
          properties:    
            direction_id:    
              description: "Property. Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: number    
            route_id:    
              description: "Property. Route ID assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
            schedule_relationship:    
              description: "Property. Describes if the Route/Trip has been scheduled. SameAs: 'schedule_relationship' field from enumScheduleRelationship (https://developers.google.com/transit/gtfs-realtime/reference#enum-schedulerelationship-2)."    
              type: string    
            start_date:    
              description: "Property. Describes the initial scheduled date of the trip corresponding to the vehicle this observation. An example format for this field - YYYYMMDD. SameAs: 'start_date' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
            start_time:    
              description: "Property. Describes the initial scheduled start time of the trip corresponding to the vehicle this observation. An example format for this field - 11:15:35 or 25:15:35. SameAs: 'start_time' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
            trip_id:    
              description: "Property. Trip ID/Trip name allotted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)."    
              type: string    
          type: object    
        vehicleDesc:    
          description: "Property. Describes the additional information of the vehicle corresponding to this observation. SameAs:'vehicle' field from GTFS Realtime message-VehiclePosition(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicleposition)/(https://developers.google.com/transit/gtfs-realtime/reference#message-tripupdate)."    
          properties:    
            license_plate:    
              description: "Property. Gives the License Plate number of the vehice.SameAs: 'license_plate' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
            vehicle_id:    
              description: "Property. Unique ID assigned to the vehicle corresponding to this observation,used in internal system identification.SameAs: 'id' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
            vehicle_label:    
              description: "Property. User visible label,i.e.,something that must be shown to the passenger to help identify the correct vehicle.SameAs: 'label' field from GTFS Realtime message - VehicleDescriptor(https: //developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)."    
              type: string    
          type: object    
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
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### TransitManagement NGSI-v2 valori chiave Esempio  
Ecco un esempio di TransitManagement in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "https://smart-data-models.github.io/IUDX/TransitManagement/schema.json",  
	"type": "TransitManagement",  
	"vehicleType":"hopper",  
	"trip_delay":11968,  
	"agency_lang":"en",  
	"depot_name":"BHESTAN DEPOT",  
	"travelTime":"22:11:14",  
	"direction_id":0,  
	"schedule_relationship":"SCHEDULED",  
	"vehicle_id":"52TC12",  
	"agency_fare_url":"http://charteredbike.in/surat/?page_id=1021",  
	"actual_trip_end_time":"2021-10-28T08:24:22+05:30",  
	"last_tracked_time":"08:13:22",  
	"standing_capacity":20,  
	"last_stop_arrival_time":"13:30:12",  
	"agency_id":"agency001",  
	"current_status":"INCOMING_AT",  
	"route_type":"1",  
	"speed":28,  
	"route_id":"17AD",  
	"seating_capacity":70,  
	"vehicle_label":"A03",  
	"timestamp":"2021-10-28T08:13:22+05:30",  
	"arrival_time":"22:00:28",  
	"route_long_name":"Baiyappanahalli to Mysuru Road",  
	"agency_timezone":"Asia/Kolkata",  
	"stop_code":"F12",  
	"agency_name":"Chartered Bike Surat",  
	"route_desc":"Phase1-Phase2",  
	"license_plate":"GJ05BX1583",  
	"stop_id":"1016",  
	"uncertainity":0,  
	"route_color":"00FFFF",  
	"travelDistance":9.00174,  
	"actual_trip_start_time":"2021-10-28T07:46:51+05:30",  
	"bearing":90,  
	"stop_sequence":24,  
	"start_date":"2022-03-01",  
	"current_stop_sequence":1001,  
	"start_time":"11:15:35",  
	"trip_id":"23952340",  
	"route_text_color":"FFD700",  
	"ac_available":"yes",  
	"tripDirection":"DN",  
	"agency_url": "http://charteredbike.in/surat/",  
	"routeStopSequence":["10","1001","1002","1003","1004","1005"],  
	"trip_direction":"DN",  
	"departure_time":"22:00:33",  
	"last_stop_id":"4032",  
	"route_short_name":"Purple Line",  
	"stop_name":"DEVASHISH NAGAR MORA BHAGAL",  
	"depot_id":"1",  
	"observationDateTime":"2021-10-28T08:13:22+05:30"  
}  
```  
</details>  
#### TransitManagement NGSI-v2 normalizzato Esempio  
Ecco un esempio di TransitManagement in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
    "type": "Time",  
    "value": "22:11:14"  
  },  
  "direction_id": {  
    "type": "Boolean",  
    "value": "false"  
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
    "type": "URL",  
    "value": "http://charteredbike.in/surat/?page_id=1021"  
  },  
  "actual_trip_end_time": {  
    "type": "Date-Time",  
    "value": "2021-10-28T08:24:22+05:30"  
  },  
  "last_tracked_time": {  
    "type": "Time",  
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
    "format": "Date-Time",  
    "value": "2021-10-28T08:13:22+05:30"  
  },  
  "arrival_time": {  
    "type": "Time",  
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
    "value": "false"  
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
    "type": "Date-Time",  
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
    "type": "Date",  
    "value": "2022-03-01"  
  },  
  "current_stop_sequence": {  
    "type": "Number",  
    "value": 1001  
  },  
  "start_time": {  
    "type": "Time",  
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
    "type": "URL",  
    "value": "http://charteredbike.in/surat/"  
  },  
  "routeStopSequence": {  
    "type": "array",  
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
    "type": "Time",  
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
    "type": "Date-Time",  
    "value": "2021-10-28T08:13:22+05:30"  
  }  
}  
```  
</details>  
#### TransitManagement Valori-chiave NGSI-LD Esempio  
Ecco un esempio di TransitManagement in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "https://smart-data-models.github.io/IUDX/TransitManagement/schema.json",  
    "@context": [  
        "iudx:TransitManagement",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ],  
    "type": "TransitManagement",  
    "vehicleType": "hopper",  
    "trip_delay": 11968,  
    "agency_lang": "en",  
    "depot_name": "BHESTAN DEPOT",  
    "travelTime": "22:11:14",  
    "direction_id": 0,  
    "schedule_relationship": "SCHEDULED",  
    "vehicle_id": "52TC12",  
    "agency_fare_url": "http://charteredbike.in/surat/?page_id=1021",  
    "actual_trip_end_time": "2021-10-28T08:24:22+05:30",  
    "last_tracked_time": "08:13:22",  
    "standing_capacity": 20,  
    "last_stop_arrival_time": "13:30:12",  
    "agency_id": "agency001",  
    "current_status": "INCOMING_AT",  
    "route_type": "1",  
    "speed": 28,  
    "route_id": "17AD",  
    "seating_capacity": 70,  
    "vehicle_label": "A03",  
    "timestamp": "2021-10-28T08:13:22+05:30",  
    "arrival_time": "22:00:28",  
    "route_long_name": "Baiyappanahalli to Mysuru Road",  
    "agency_timezone": "Asia/Kolkata",  
    "stop_code": "F12",  
    "agency_name": "Chartered Bike Surat",  
    "route_desc": "Phase1-Phase2",  
    "license_plate": "GJ05BX1583",  
    "stop_id": "1016",  
    "uncertainity": 0,  
    "route_color": "00FFFF",  
    "travelDistance": 9.00174,  
    "actual_trip_start_time": "2021-10-28T07:46:51+05:30",  
    "bearing": 90,  
    "stop_sequence": 24,  
    "start_date": "2022-03-01",  
    "current_stop_sequence": 1001,  
    "start_time": "11:15:35",  
    "trip_id": "23952340",  
    "route_text_color": "FFD700",  
    "ac_available": "yes",  
    "tripDirection": "DN",  
    "agency_url": "http://charteredbike.in/surat/",  
    "routeStopSequence": [  
        "10",  
        "1001",  
        "1002",  
        "1003",  
        "1004",  
        "1005"  
    ],  
    "trip_direction": "DN",  
    "departure_time": "22:00:33",  
    "last_stop_id": "4032",  
    "route_short_name": "Purple Line",  
    "stop_name": "DEVASHISH NAGAR MORA BHAGAL",  
    "depot_id": "1",  
    "observationDateTime": "2021-10-28T08:13:22+05:30"  
}  
```  
</details>  
#### TransitManagement NGSI-LD normalizzato Esempio  
Ecco un esempio di TransitManagement in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
    "type": "array",  
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
  "@context": ["https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
