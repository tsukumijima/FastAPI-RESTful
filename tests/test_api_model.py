from __future__ import annotations

from dataclasses import dataclass

from fastapi_restful.api_model import APIModel


def test_model_validate() -> None:
    @dataclass
    class Data:
        x: int

    class Model(APIModel):
        x: int

    assert Model.model_validate(Data(x=1)).x == 1


def test_aliases() -> None:
    class Model(APIModel):
        some_field: str

    assert Model(some_field="a").some_field == "a"
    assert Model(someField="a").some_field == "a"  # type: ignore[call-arg]
