from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, confloat, constr


class Type(Enum):
    GtfsFrequency = 'GtfsFrequency'


class GtfsFrequency(BaseModel):
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
    endTime: Optional[
        constr(pattern=r'^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$')
    ] = Field(None, description='Same as GTFS `end_time`')
    exactTimes: Optional[bool] = Field(
        None,
        description='Same as GTFS `exact_times` but encoded as a Boolean; `false`: Frequency-based trips are not exactly scheduled. `true`: Frequency-based trips are exactly scheduled',
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
    headwaySeconds: Optional[confloat(ge=1.0)] = Field(
        None, description='Same as GTFS `headway_secs`'
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
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startTime: Optional[
        constr(pattern=r'^([0-3][0-9]|4[0-7]):[0-5][0-9]:[0-5][0-9]$')
    ] = Field(None, description='Same as GTFS `start_time`')
    type: Optional[Type] = Field(
        None, description='NGSI Entity type. It has to be GtfsFrequency'
    )
