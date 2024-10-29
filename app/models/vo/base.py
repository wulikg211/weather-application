from typing import Any, Optional

from pydantic import Field, BaseModel


class BaseResponseData(BaseModel):
    code: int
    data: Optional[Any] = Field(default=None)
    message: Optional[Any] = Field(default=None)

