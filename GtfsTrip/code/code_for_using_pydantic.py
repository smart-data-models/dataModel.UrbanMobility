from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, constr


class BikesAllowed(Enum):
    number_0 = 0
    number_1 = 1
    number_2 = 2


class Direction(Enum):
    number_0 = 0
    number_1 = 1


class Type(Enum):
    GtfsTrip = 'GtfsTrip'


class WheelChairAccessible(Enum):
    number_0 = 0
    number_1 = 1
    number_2 = 2


class GtfsTrip(BaseModel):
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    bikesAllowed: Optional[BikesAllowed] = Field(
        None,
        description="Same as GTFS `bikes_allowed`. Enum:'0, 1, 2'. See [GTFS](https://developers.google.com/transit/gtfs/reference/#tripstxt)",
    )
    block: Optional[str] = Field(None, description='Same as GTFS `block_id`')
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
    direction: Optional[Direction] = Field(
        None, description="Same as GTFS `direction_id`. Enum:'0, 1'"
    )
    hasRoute: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Same as `route_id`. It shall point to an Entity of type GtfsRoute',
    )
    hasService: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Same as GTFS `service_id`. It shall point to an Entity of type GtfsService',
    )
    hasShape: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Same as GTFS `shape_id`. It shall point to an Entity of type GtfsShape',
    )
    headSign: Optional[str] = Field(None, description='Same as GTFS `trip_headsign`')
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
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    shortName: Optional[str] = Field(None, description='Same as GTFS `trip_short_name`')
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type] = Field(
        None, description='NGSI Entity type. It has to be GtfsTrip'
    )
    wheelChairAccessible: Optional[WheelChairAccessible] = Field(
        None, description="Same as GTFS `wheelchair_accessible`. Enum:'0, 1, 2'"
    )
