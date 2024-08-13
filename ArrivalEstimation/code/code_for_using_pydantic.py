from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    ConfigDict,
    Field,
    confloat,
    constr,
)


class Type(Enum):
    ArrivalEstimation = 'ArrivalEstimation'


class ArrivalEstimation(BaseModel):
    model_config = ConfigDict(
        regex_engine="python-re",
    )
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
    hasStop: Optional[
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
    ] = Field(None, description='It shall point to an Entity of Type GtfsStop')
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
    headSign: Optional[str] = Field(
        None,
        description="It shall contain the text that appears on a sign that identifies the trip's destination to passengers",
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
    remainingDistance: Optional[confloat(ge=0.0)] = Field(
        None,
        description='It shall contain the remaining distance (in meters) of arrival for the trip heading to the concerned stop',
    )
    remainingTime: Optional[
        constr(
            pattern=r'^P(?=\\w*\\d)(?:\\d+Y|Y)?(?:\\d+M|M)?(?:\\d+W|W)?(?:\\d+D|D)?(?:T(?:\\d+H|H)?(?:\\d+M|M)?(?:\\d+(?:\\?.\\d{1,2})?S|S)?)?$'
        )
    ] = Field(
        None,
        description='It shall contain the remaining time of arrival for the trip heading to the concerned stop. Remaining time shall be encoded as a ISO8601 duration. Ex. `PT8M5S`',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type] = Field(
        None,
        description="NGSI Entity Type: It has to be ArrivalEstimation. Enum:'ArrivalEstimation'",
    )
