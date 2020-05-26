PublicTransportRoute
  - required
    - oneOf:
      - address
      - location
    - name
    - transportationType
  - type: "object"  
   - allOf:
      - $ref: "https://raw.githubusercontent.com/smart-data-models/data-models/master/common-schema.yaml#Common"

  - description :>
    ## Description
    Generic model for a public transport stop. It adopts some GTFS definitions, but it does not need to be linked to additional GTFS data.

    ## Data Model
  - properties:
    - source 
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "uri"
      - description: Specifies the URL to the source of this data (either organization or where relevant more specific source)

    - dataProvider: 
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: Specifies the URL to information about the provider of this information

    - address:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/address"
      - $ref: "https://raw.githubusercontent.com/smart-data-models/data-models/master/common-schema.yaml#Address"

    - location: 
      - x-ngsi:
        - type: "Property"
        - model: "https://tools.ietf.org/html/rfc7946"
      - $ref: "https://raw.githubusercontent.com/smart-data-models/data-models/master/common-schema.yaml#Geometry" 

    - stopCode: 
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"  
      - description: Identifier/code of the public transport stop.

    - shortStopCode: 
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string  
      - description: Shorter form of the identifier/code of the public transport stop.

    - name: 
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"  
      - description: The name of the public transport stop.

    - wheelchairAccessible: 
      - x-ngsi:
        - type: "Property"
        - model: "https://developers.google.com/transit/gtfs/reference/#stopstxt"
      - type: "integer"
      - minimum: 0
      - maximum: 2
      - description: Indicate whether or not this stop is accessible for wheelchairs. Used values are: 0-no information; 1-some vehicles of this stop allow wheelchair; 2-no vehicle of this stop allow wheelchair 

    - transportationType: 
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/Number"
      - type: "integer"  
      - minimum: 0
      - maximum: 7
      - required: true
      - description: Types of public transport using this stop as defined in (https://developers.google.com/transit/gtfs/reference/#routestxt). 

    - refPublicTransportRoute: 
      - x-ngsi:
        - type: "Property"
      - type: "array"  
        - items: 
          - type: "string"
          - format: "uri"
      - description: Public transport routes using this stop.

    - peopleCount: 
      - x-ngsi: 
        - type: "Property"
        - model: https://schema.org/Number
      - type: "integer"
      - minimum: 0  
      - description: Estimation of people waiting in the stop.

    - refPeopleCountDevice: 
      - x-ngsi: 
        - type: "Property"
      - type: "string"
      - format: "uri"  
      - description: Reference to the [Device](https://github.com/Fiware/dataModels/blob/master/specs/Device/Device/doc/spec.md) providing people count estimate.

    - openingHoursSpecification: 
      - x-ngsi: 
        - type: "Property"
        - model: "http://schema.org/openingHoursSpecification"
      - type: "array"
      - items:
        - $ref: ""
      - description: Opening hours of this stop.