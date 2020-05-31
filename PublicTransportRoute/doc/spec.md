PublicTransportRoute
  - required
    - id
    - type 
    - name
    - transportationType
  - type: "object"  
  - description :>
    ## Description
      Generic model for public transport route. It adopts some GTFS definitions, but it does not need to be linked to additional GTFS data. A route is a journey, offered by one public transport service, that goes through a set of stops.

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

    - routeCode: 
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"  
      - description: ID or code of the route (e.g. ‘HT5200104000’)
  
    - shortRouteCode:
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"          
      - description: Shorter form of the ID/code of the route (e.g. ‘5200104000’’)

    - name: 
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"  
      - description: Name of the route
  
    - transportationType: 
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/Number"
      - type: "integer"  
      - minimum: 0
      - maximum: 7
      - required: true
      - description: Types of public transport using this stop as defined in (https://developers.google.com/transit/gtfs/reference/#routestxt). 
  
    - routeColor: 
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/color"
      - type: "string"  
      - description: Color assigned to route in hexadecimal.
  
    - routeTextColor: 
      - x-ngsi: 
        - type: "property"
        - model: "https://schema.org/color"
      - type: "string"  
      - description: Color assigned to route in text.
  
    - routeSegments: 
      - x-ngsi: 
        - type: "Property"
      - type: "array"
      - items: 
        - $ref: "https://github.com/smart-data-models/dataModel.UrbanMobility/blob/master/PublicTransportStop/schema.json"
      - description: Segments of this route defined by their name and stops.
    
    - schedule: 
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/OpeningHoursSpecification" 
      - type: "array"
      - items: 
        - $ref: "" 
      - description: Working hours of this route.  
