from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, confloat, constr


class RouteType(Enum):
    field_0 = 0
    field_1 = 1
    field_2 = 2
    field_3 = 3
    field_4 = 4
    field_5 = 5
    field_6 = 6
    field_7 = 7


class Type(Enum):
    GtfsRoute = 'GtfsRoute'


class GtfsRoute(BaseModel):
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
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
    name: Optional[str] = Field(None, description='The name of this item')
    operatedBy: Optional[
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
        description='Agency that operates this route. It shall point to an Entity of Type GtfsAgency',
    )
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
    page: Optional[AnyUrl] = Field(None, description='Same as GTFS `stop_url`')
    routeColor: Optional[str] = Field(
        None,
        description='Same as GTFS `route_color`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)',
    )
    routeSortOrder: Optional[confloat(ge=0.0)] = Field(
        None, description='Same as GTFS `route_sort_order`'
    )
    routeTextColor: Optional[str] = Field(
        None,
        description='Same as GTFS `route_text_color`. See [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt)',
    )
    routeType: Optional[RouteType] = Field(
        None,
        description="Same as GTFS `route_type`. allowed values those allowed for `route_type` as prescribed by [GTFS](https://developers.google.com/transit/gtfs/reference/#routestxt). Enum:'0, 1, 2, 3, 4, 5, 6, 7'",
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    shortName: Optional[str] = Field(
        None, description='Same as GTFS `route_short_name`'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type] = Field(
        None, description='NGSI Entity type. It has to be GtfsRoute'
    )
