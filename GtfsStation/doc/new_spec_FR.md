Entité : GtfsStation  
====================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Station GTFS**  

## Liste des biens  

`address`: L'adresse postale.  `alternateName`: Un autre nom pour cet article  `areaServed`: La zone géographique où un service ou un article offert est fourni.  `code`:   `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  `description`:   `hasAccessPoint`:   `hasParentStation`:   `hasStop`:   `id`:   `location`:   `name`:   `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  `page`:   `seeAlso`:   `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  `type`: NGSI Type d'entité  `wheelChairAccessible`:   `zoneCode`:   ## Modèle de données description des biens  
Classement par ordre alphabétique  
```yaml  
GtfsStation:    
  description: 'GTFS Station'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    code:    
      type: string    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      type: string    
    hasAccessPoint:    
      items:    
        format: uri    
        type: string    
      type: array    
    hasParentStation:    
      format: uri    
      type: string    
    hasStop:    
      items:    
        format: uri    
        type: string    
      type: array    
    id:    
      anyOf: &gtfsstation_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    name:    
      type: string    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *gtfsstation_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    page:    
      format: uri    
      type: string    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - GtfsStation    
      type: string    
    wheelChairAccessible:    
      enum:    
        - 0    
        - 1    
        - 2    
      type: string    
    zoneCode:    
      type: string    
  required:    
    - id    
    - type    
    - name    
    - location    
    - hasStop    
  type: object    
```  
Voici un exemple d'une GtfsStation au format JSON comme valeurs clés. Elle est compatible avec NGSI V2 lorsqu'elle utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsStation:Madrid:est_90_21",  
  "type": "GtfsStation",  
  "code": "21",  
  "name": "Intercambiador de Plaza de Castilla",  
  "location": {  
    "type": "Point",  
    "coordinates": [-3.6892, 40.4669]  
  },  
  "address": {  
    "streetAddress": "Paseo de la Castellana 189",  
    "addressLocality": "Madrid",  
    "addressCountry": "ES"  
  },  
  "hasStop": ["urn:ngsi-ld:GtfsStop:Madrid_par_4_1"]  
}  
```  
Voici un exemple d'une GtfsStation au format JSON normalisé. Elle est compatible avec NGSI V2 lorsqu'elle utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:GtfsStation:Madrid:est_90_21",  
  "type": "GtfsStation",  
  "code": {  
    "value": "21"  
  },  
  "name": {  
    "value": "Intercambiador de Plaza de Castilla"  
  },  
  "hasStop": {  
    "type": "Relationship",  
    "value": ["urn:ngsi-ld:GtfsStop:Madrid_par_4_1"]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-3.6892, 40.4669]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Madrid",  
      "addressCountry": "ES",  
      "streetAddress": "Paseo de la Castellana 189"  
    }  
  }  
}  
```  
Voici un exemple de GtfsStation au format JSON-LD comme valeurs clés. Elle est compatible avec le format NGSI-LD lorsqu'elle n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "address": {"addressCountry": "ES",  
             "addressLocality": "Madrid",  
             "streetAddress": "Paseo de la Castellana 189",  
             "type": "PostalAddress"},  
 "code": "21",  
 "hasStop": ["urn:ngsi-ld:GtfsStop:Madrid_par_4_1"],  
 "id": "urn:ngsi-ld:GtfsStation:Madrid:est_90_21",  
 "location": {"coordinates": [-3.6892, 40.4669], "type": "Point"},  
 "name": "Intercambiador de Plaza de Castilla",  
 "type": "GtfsStation"}  
```  
Voici un exemple d'une GtfsStation au format JSON-LD normalisé. Elle est compatible avec le format NGSI-LD lorsqu'elle n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:GtfsStation:Madrid:est_90_21",  
    "type": "GtfsStation",  
    "code": {  
        "type": "Property",  
        "value": "21"  
    },  
    "name": {  
        "type": "Property",  
        "value": "Intercambiador de Plaza de Castilla"  
    },  
    "hasStop": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:GtfsStop:Madrid_par_4_1"  
        ]  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -3.6892,  
                40.4669  
            ]  
        }  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressLocality": "Madrid",  
            "addressCountry": "ES",  
            "streetAddress": "Paseo de la Castellana 189",  
            "type": "PostalAddress"  
        }  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
