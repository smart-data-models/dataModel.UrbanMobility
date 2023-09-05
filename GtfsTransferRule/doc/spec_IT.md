<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: GtfsTransferRule  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.UrbanMobility/blob/master/GtfsTransferRule/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Regola di trasferimento GTFS**  
versione: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `alternateName[string]`: Un nome alternativo per questa voce  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `hasDestination[*]`: Viaggio associato a questa entità. Deve puntare a un'entità di tipo GtfsStop o GtfsStation.  . Model: [http://schema.org/URL](http://schema.org/URL)- `hasOrigin[*]`: Viaggio associato a questa entità. Deve puntare a un'entità di tipo GtfsStop o GtfsStation.  . Model: [http://schema.org/URL](http://schema.org/URL)- `id[*]`: Identificatore univoco dell'entità  - `minimumTransferTime[number]`: Come GTFS `min_transfer_time`. Unità:'secondi'.  . Model: [https://schema.org/Integer](https://schema.org/Integer)- `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `transferType[string]`: Uguale a `Transfer_type` di GTFS. Enum:'0, 1, 2, 3'  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo di entità NGSI. Deve essere GtfsTransferRule  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `hasDestination`  - `hasOrigin`  - `id`  - `transferType`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Vedere [https://developers.google.com/transit/gtfs/reference/#transferstxt](https://developers.google.com/transit/gtfs/reference/#transferstxt)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
GtfsTransferRule:    
  description: GTFS Transfer Rule    
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
    hasDestination:    
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
      description: Trip associated to this Entity. It shall point to an Entity of type GtfsStop or GtfsStation    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    hasOrigin:    
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
      description: Trip associated to this Entity. It shall point to an Entity of type GtfsStop or GtfsStation    
      x-ngsi:    
        model: http://schema.org/URL    
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
    minimumTransferTime:    
      description: 'Same as GTFS `min_transfer_time`. Unit:''seconds'''    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Integer    
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
    transferType:    
      description: 'Same as GTFS `transfer_type`. Enum:''0, 1, 2, 3'''    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be GtfsTransferRule    
      enum:    
        - GtfsTransferRule    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - hasOrigin    
    - hasDestination    
    - transferType    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsTransferRule/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.UrbanMobility/GtfsTransferRule/schema.json    
  x-model-tags: ""    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### GtfsTransferRule Valori chiave NGSI-v2 Esempio  
Ecco un esempio di GtfsTransferRule in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:GtfsTransferRule:Malaga:Linea1_Linea5",  
  "type": "GtfsTransferRule",  
  "name": "L1_L5",  
  "hasOrigin": "urn:ngsi-ld:GtfsStop:Malaga_101",  
  "hasDestination": "urn:ngsi-ld:GtfsStop:Malaga_508",  
  "transferType": "0",  
  "minimumTransferTime": 10  
}  
```  
</details>  
#### GtfsTransferRule NGSI-v2 normalizzato Esempio  
Ecco un esempio di GtfsTransferRule in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:GtfsTransferRule:Malaga:Linea1_Linea5",  
  "type": "GtfsTransferRule",  
  "transferType": {  
    "type": "Text",  
    "value": "0"  
  },  
  "minimumTransferTime": {  
    "type": "Number",  
    "value": 10  
  },  
  "hasDestination": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:GtfsStop:Malaga_508"  
  },  
  "hasOrigin": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:GtfsStop:Malaga_101"  
  },  
  "name": {  
    "value": "L1_L5"  
  }  
}  
```  
</details>  
#### GtfsTransferRule Valori chiave NGSI-LD Esempio  
Ecco un esempio di GtfsTransferRule in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:GtfsTransferRule:Malaga:Linea1_Linea5",  
    "type": "GtfsTransferRule",  
    "hasDestination": "urn:ngsi-ld:GtfsStop:Malaga_508",  
    "hasOrigin": "urn:ngsi-ld:GtfsStop:Malaga_101",  
    "minimumTransferTime": 10,  
    "name": "L1_L5",  
    "transferType": "0",  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### GtfsTransferRule Esempio normalizzato NGSI-LD  
Ecco un esempio di GtfsTransferRule in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:GtfsTransferRule:Malaga:Linea1_Linea5",  
    "type": "GtfsTransferRule",  
    "hasDestination": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsStop:Malaga_508"  
    },  
    "hasOrigin": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:GtfsStop:Malaga_101"  
    },  
    "minimumTransferTime": {  
        "type": "Property",  
        "value": 10  
    },  
    "name": {  
        "type": "Property",  
        "value": "L1_L5"  
    },  
    "transferType": {  
        "type": "Property",  
        "value": "0"  
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
