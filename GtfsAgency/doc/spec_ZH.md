<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

========
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `addressCountry[string]`: 的国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)
<!-- 35-RequiredProperties -->

- `agencyName`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

GtfsAgency:    
  description: 'GTFS Agency'    
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
    agencyName:    
      description: 'Same as GTFS `agency_name`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
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
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    entitySource:    
      description: 'A sequence of characters giving the original source of the Entity data as a URL. It shall point to the URL of the original GTFS feed used to generate this Entity'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    id:    
      anyOf: &gtfsagency_-_properties_-_owner_-_items_-_anyof    
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
    language:    
      description: "Same as GTFS `agency_language`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfsagency_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    page:    
      description: 'Same as GTFS `stop_url`'    
      format: uri    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Property    
    phone:    
      description: 'Same as GFTS `agency_phone`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    streetAddress:    
      description: 'The street address'    
      type: string    
      x-ngsi:    
        model: https://schema.org/streetAddress    
        type: Property    
    timezone:    
      description: "Same as GTFS `agency_timezone`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#agencytxt)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity Type: It has to be GtfsAgency. Enum:''GtfsAgency'''    
      enum:    
        - GtfsAgency    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - agencyName    
    - source    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/GtfsAgency/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.UrbanMobility/GtfsAgency/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
  "type": "GtfsAgency",  
  "agencyName": "Empresa Malagueña de Transportes",  
  "page": "http://www.emtmalaga.es/",  
  "timezone": "Europe/Madrid",  
  "language": "ES",  
  "source": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52"  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
  "type": "GtfsAgency",  
  "agencyName": {  
    "value": "Empresa Malague\u00f1a de Transportes"  
  },  
  "language": {  
    "value": "ES"  
  },  
  "page": {  
    "value": "http://www.emtmalaga.es/"  
  },  
  "source": {  
    "value": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52"  
  },  
  "timezone": {  
    "value": "Europe/Madrid"  
  }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
    "type": "GtfsAgency",  
    "agencyName": {  
        "type": "Property",  
        "value": "Empresa Malague\u00f1a de Transportes"  
    },  
    "language": {  
        "type": "Property",  
        "value": "ES"  
    },  
    "page": {  
        "type": "Property",  
        "value": "http://www.emtmalaga.es/"  
    },  
    "source": {  
        "type": "Property",  
        "value": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52"  
    },  
    "timezone": {  
        "type": "Property",  
        "value": "Europe/Madrid"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/master/context.jsonld"  
    ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:GtfsAgency:Malaga_EMT",  
    "type": "GtfsAgency",  
    "agencyName": "Empresa Malague\u00f1a de Transportes",  
    "language": "ES",  
    "page": "http://www.emtmalaga.es/",  
    "source": "http://datosabiertos.malaga.eu/dataset/lineas-y-horarios-bus-google-transit/resource/24e86888-b91e-45bf-a48c-09855832fd52",  
    "timezone": "Europe/Madrid",  
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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
