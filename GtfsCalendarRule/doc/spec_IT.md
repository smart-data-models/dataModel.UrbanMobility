<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: GtfsCalendarRule    
========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsCalendarRule/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Modelli di dati intelligenti. Regola del calendario GTFS**    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `alternateName[string]`: Un nome alternativo per questa voce  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzati  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `endDate[date]`: Data di fine di questa regola nel formato `YYY-MM-DD`. Può essere ottenuta dal campo `end_date` di [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt).  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `friday[boolean]`: Come il `venerdì` di GTFS  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `hasService[string]`: Servizio a cui si applica questa regola. Derivato da `service_id  . Model: [https://schema.org/URL](https://schema.org/URL)- `id[*]`: Identificatore univoco dell'entità  - `monday[boolean]`: Come GTFS `monday  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `saturday[boolean]`: Come il `sabato` di GTFS  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `startDate[date]`: Data di inizio di questa regola nel formato `YYY-MM-DD`. Può essere ottenuta dal campo `start_date` di [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt).  . Model: [https://schema.org/Date](https://schema.org/Date)- `sunday[boolean]`: Come GTFS `domenica`  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `thursday[boolean]`: Come GTFS `Giovedì`  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `tuesday[boolean]`: Come GTFS `tuesday`  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `type[string]`: Tipo di entità NGSI: Deve essere GtfsCalendarRule  - `wednesday[boolean]`: Come il `mercoledì` di GTFS  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `endDate`  - `friday`  - `hasService`  - `id`  - `monday`  - `saturday`  - `startDate`  - `sunday`  - `thursday`  - `tuesday`  - `type`  - `wednesday`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Vedere [https://developers.google.com/transit/gtfs/reference/#calendartxt](https://developers.google.com/transit/gtfs/reference/#calendartxt)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
GtfsCalendarRule:      
  description: Smart Data Models. GTFS Calendar Rule      
  properties:      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
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
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    endDate:      
      description: "End date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `end_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)"      
      format: date      
      type: string      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    friday:      
      description: Same as GTFS `friday`      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    hasService:      
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
      description: Service to which this rule applies to. Derived from `service_id`      
      type: string      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
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
    monday:      
      description: Same as GTFS `monday`      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    name:      
      description: The name of this item      
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
    saturday:      
      description: Same as GTFS `saturday`      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
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
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    startDate:      
      description: "Start date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `start_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)"      
      format: date      
      type: string      
      x-ngsi:      
        model: https://schema.org/Date      
        type: Property      
    sunday:      
      description: Same as GTFS `sunday`      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    thursday:      
      description: Same as GTFS `thursday`      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    tuesday:      
      description: Same as GTFS `tuesday`      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    type:      
      description: 'NGSI Entity Type: It has to be GtfsCalendarRule'      
      enum:      
        - GtfsCalendarRule      
      type: string      
      x-ngsi:      
        type: Property      
    wednesday:      
      description: Same as GTFS `wednesday`      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
  required:      
    - id      
    - type      
    - hasService      
    - monday      
    - tuesday      
    - wednesday      
    - thursday      
    - friday      
    - saturday      
    - sunday      
    - startDate      
    - endDate      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsCalendarRule/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/GtfsCalendarRule/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### GtfsCalendarRule Valori chiave NGSI-v2 Esempio    
Ecco un esempio di GtfsCalendarRule in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "type": "GtfsCalendarRule",  
  "name": "Rule Hospital Service 1",  
  "hasService": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1",  
  "monday": true,  
  "tuesday": true,  
  "wednesday": true,  
  "thursday": true,  
  "friday": true,  
  "saturday": false,  
  "sunday": false,  
  "startDate": "2018-01-01",  
  "endDate": "2019-01-01"  
}  
```  
</details>    
#### GtfsCalendarRule NGSI-v2 normalizzato Esempio    
Ecco un esempio di GtfsCalendarRule in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "type": "GtfsCalendarRule",  
  "startDate": {  
    "type": "DateTime",  
    "value": "2018-01-01"  
  },  
  "endDate": {  
    "type": "DateTime",  
    "value": "2019-01-01"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Rule Hospital Service 1"  
  },  
  "monday": {  
    "type": "Boolean",  
    "value": true  
  },  
  "tuesday": {  
    "type": "Boolean",  
    "value": true  
  },  
  "friday": {  
    "type": "Boolean",  
    "value": true  
  },  
  "wednesday": {  
    "type": "Boolean",  
    "value": true  
  },  
  "thursday": {  
    "type": "Boolean",  
    "value": true  
  },  
  "sunday": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasService": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1"  
  },  
  "saturday": {  
    "type": "Boolean",  
    "value": false  
  }  
}  
```  
</details>    
#### GtfsCalendarRule Valori chiave NGSI-LD Esempio    
Ecco un esempio di GtfsCalendarRule in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
  "type": "GtfsCalendarRule",  
  "endDate": "2019-01-01",  
  "friday": true,  
  "hasService": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1",  
  "monday": true,  
  "name": "Rule Hospital Service 1",  
  "saturday": false,  
  "startDate": "2018-01-01",  
  "sunday": false,  
  "thursday": true,  
  "tuesday": true,  
  "wednesday": true,  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### GtfsCalendarRule Esempio normalizzato NGSI-LD    
Ecco un esempio di GtfsCalendarRule in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",  
    "type": "GtfsCalendarRule",  
    "endDate": {  
        "type": "Property",  
        "value": {  
            "@type": "Date",  
            "@value": "2019-01-01"  
        }  
    },  
    "friday": {  
        "type": "Property",  
        "value": true  
    },  
    "hasService": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1"  
    },  
    "monday": {  
        "type": "Property",  
        "value": true  
    },  
    "name": {  
        "type": "Property",  
        "value": "Rule Hospital Service 1"  
    },  
    "saturday": {  
        "type": "Property",  
        "value": false  
    },  
    "startDate": {  
        "type": "Property",  
        "value": {  
            "@type": "Date",  
            "@value": "2018-01-01"  
        }  
    },  
    "sunday": {  
        "type": "Property",  
        "value": false  
    },  
    "thursday": {  
        "type": "Property",  
        "value": true  
    },  
    "tuesday": {  
        "type": "Property",  
        "value": true  
    },  
    "wednesday": {  
        "type": "Property",  
        "value": true  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
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
