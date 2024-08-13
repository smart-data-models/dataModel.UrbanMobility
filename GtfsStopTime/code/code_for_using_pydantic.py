from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, confloat, constr


class DropOffType(Enum):
    field_0 = 0
    field_1 = 1
    field_2 = 2
    field_3 = 3


class PickupType(Enum):
    field_0 = 0
    field_1 = 1
    field_2 = 2
    field_3 = 3


class Timepoint(Enum):
    field_0 = 0
    field_1 = 1


class Type(Enum):
    GtfsStopTime = 'GtfsStopTime'


class GtfsStopTime(BaseModel):
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    arrivalTime: Optional[
        constr(pattern=r'^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$')
    ] = Field(None, description='Same as GTFS `arrival_time`')
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
    departureTime: Optional[
        constr(pattern=r'^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$')
    ] = Field(None, description='Same as GTFS `departure_time`')
    description: Optional[str] = Field(None, description='A description of this item')
    distanceTravelled: Optional[confloat(ge=0.0)] = Field(
        None, description='Same as GTFS `shape_dist_traveled`'
    )
    dropOffType: Optional[DropOffType] = Field(
        0, description="Same as GTFS `drop_off_type`. Enum:'0, 1, 2, 3'"
    )
    hasStop: Optional[
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
        description='Same as GTFS `stop_id`. It shall point to an Entity of type GtfsStop',
    )
    hasTrip: Optional[
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
        description='Trip associated to this Entity. It shall point to an Entity of Type GtfsTrip',
    )
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
    pickupType: Optional[PickupType] = Field(
        0, description="Same as GTFS `pickup_type`. Enum:'0, 1, 2, 3' "
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    stopHeadsign: Optional[str] = Field(
        None, description='Same as GTFS `stop_headsign`'
    )
    stopSequence: Optional[confloat(ge=1.0)] = Field(
        None, description='Same as GTFS `stop_sequence`. Starting with `1`'
    )
    timepoint: Optional[Timepoint] = Field(
        1, description="Same as GTFS `timepoint`. Enum:'0, 1'"
    )
    type: Optional[Type] = Field(
        None, description='NGSI Entity type. It has to be GtfsStopTime'
    )
