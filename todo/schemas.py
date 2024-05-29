from datetime import datetime
from typing import Annotated, Optional

from pydantic import BaseModel, StringConstraints


class STaskCreate(BaseModel):
    """Schema for task"""

    title: Annotated[str, StringConstraints(max_length=100)]
    description: Annotated[str, StringConstraints(max_length=250)] | None 


class STaskUpdate(BaseModel):
    """Schema for task"""

    title: Annotated[str, StringConstraints(max_length=100)] | None = None
    description: Annotated[str, StringConstraints(max_length=250)] | None = None


class STaskInfo(BaseModel):
    """Schema for task"""

    id: int
    title: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime


class STasksInfo(BaseModel):
    """Schema for list all tasks"""

    tasks: list[STaskInfo]
