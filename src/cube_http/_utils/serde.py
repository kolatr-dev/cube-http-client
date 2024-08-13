from typing import Any, Type

from pydantic import BaseModel

from ..types._generics import M

__all__ = ["model_dict", "model_parse"]


def model_dict(m: BaseModel, **kwargs: Any) -> dict[str, Any]:
    if hasattr(m, "model_dump"):
        return getattr(m, "model_dump")(**kwargs)
    else:
        return getattr(m, "dict")(**kwargs)


def model_parse(m: Type[M], d: object, **kwargs: Any) -> M:
    if hasattr(m, "model_validate"):
        return getattr(m, "model_validate")(d, **kwargs)
    else:
        return getattr(m, "parse_obj")(d, **kwargs)
