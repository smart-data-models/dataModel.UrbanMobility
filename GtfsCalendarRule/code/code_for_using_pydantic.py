from __future__ import annotations

from datetime import date
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, constr


class Type(Enum):
    GtfsCalendarRule = 'GtfsCalendarRule'


class GtfsCalendarRule(BaseModel):
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
    endDate: Optional[date] = Field(
        None,
        description='End date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `end_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)',
    )
    friday: Optional[bool] = Field(None, description='Same as GTFS `friday`')
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
        description='Service to which this rule applies to. Derived from `service_id`',
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
    monday: Optional[bool] = Field(None, description='Same as GTFS `monday`')
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
    saturday: Optional[bool] = Field(None, description='Same as GTFS `saturday`')
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startDate: Optional[date] = Field(
        None,
        description='Start date of this rule in `YYYY-MM-DD` format. It can be obtained from the field `start_date` of [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)',
    )
    sunday: Optional[bool] = Field(None, description='Same as GTFS `sunday`')
    thursday: Optional[bool] = Field(None, description='Same as GTFS `thursday`')
    tuesday: Optional[bool] = Field(None, description='Same as GTFS `tuesday`')
    type: Optional[Type] = Field(
        None, description='NGSI Entity Type: It has to be GtfsCalendarRule'
    )
    wednesday: Optional[bool] = Field(None, description='Same as GTFS `wednesday`')
