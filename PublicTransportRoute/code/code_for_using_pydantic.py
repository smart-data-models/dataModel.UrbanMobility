from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class RouteSegment(BaseModel):
    refPublicTransportStops: Optional[List[AnyUrl]] = Field(
        None, description='relation to public transport stops'
    )
    segmentName: Optional[str] = Field(None, description='Name of the segment in route')


class DayOfWeek(Enum):
    Friday = 'Friday'
    Monday = 'Monday'
    PublicHolidays = 'PublicHolidays'
    Saturday = 'Saturday'
    Sunday = 'Sunday'
    Thursday = 'Thursday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'


class ScheduleItem(BaseModel):
    closes: Optional[constr(pattern=r'[0-9]{2}:[0-9]{2}')] = Field(
        None, description='Time for the end of the route'
    )
    dayOfWeek: Optional[DayOfWeek] = Field(
        None, description='Day of the week for the route schedule'
    )
    opens: Optional[constr(pattern=r'[0-9]{2}:[0-9]{2}')] = Field(
        None, description='Time for the start of the route'
    )


class TransportationType(Enum):
    number_0 = 0
    number_1 = 1
    number_2 = 2
    number_3 = 3
    number_4 = 4
    number_5 = 5
    number_6 = 6
    number_7 = 7


class Type6(Enum):
    PublicTransportRoute = 'PublicTransportRoute'


class PublicTransportRoute(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    routeCode: Optional[str] = Field(
        None, description='ID or code of the route (e.g. HT5200104000)'
    )
    routeColor: Optional[constr(pattern=r'^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$')] = Field(
        None, description='Color assigned to route in text'
    )
    routeSegments: Optional[List[RouteSegment]] = Field(
        None, description='Segments of this route defined by their name and stops'
    )
    routeTextColor: Optional[str] = Field(
        None, description='Color assigned to route in hexadecimal'
    )
    schedule: Optional[List[ScheduleItem]] = Field(
        None, description='Working hours of this route', min_length=1
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    shortRouteCode: Optional[str] = Field(
        None, description='Shorter form of the ID/code of the route (e.g. 5200104000)'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    transportationType: Optional[TransportationType] = Field(
        None,
        description="Types of public transport using this stop as defined in (https://developers.google.com/transit/gtfs/reference/#routestxt). Enum:'0, 1, 2, 3, 4, 5, 6, 7'",
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be PublicTransportRoute'
    )
