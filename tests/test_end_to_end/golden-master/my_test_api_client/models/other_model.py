from __future__ import annotations

from dataclasses import astuple, dataclass
from typing import Any, Dict, List, Optional, cast

from .types import *


@dataclass
class OtherModel:
    """ A different model for calling from TestModel  """

    a_value: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "a_value": self.a_value,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> OtherModel:

        a_value = d["a_value"]

        return OtherModel(a_value=a_value,)
