import pytest
from honeybee_energy.properties.extension import (
    OpaqueConstructionProperties,
    ShadeConstructionProperties,
    WindowConstructionProperties,
    WindowConstructionShadeProperties,
)

from honeybee_energy_ref.properties.hb_obj import _HBObjectWithReferences


@pytest.mark.parametrize(
    "cls",
    [
        OpaqueConstructionProperties,
        ShadeConstructionProperties,
        WindowConstructionProperties,
        WindowConstructionShadeProperties,
    ],
)
def test_material_properties(cls):
    hb_obj = cls(None)
    assert hasattr(hb_obj, "_ref")


@pytest.mark.parametrize(
    "cls",
    [
        OpaqueConstructionProperties,
        ShadeConstructionProperties,
        WindowConstructionProperties,
        WindowConstructionShadeProperties,
    ],
)
def test_to_dict_from_dict_round_trip(cls):
    hb_obj = cls(None)
    d = hb_obj.ref.to_dict()
    hb_obj2 = _HBObjectWithReferences.from_dict(d["ref"], None)
    assert hb_obj2 == hb_obj.ref


@pytest.mark.parametrize(
    "cls",
    [
        OpaqueConstructionProperties,
        ShadeConstructionProperties,
        WindowConstructionProperties,
        WindowConstructionShadeProperties,
    ],
)
def test_duplicate(cls):
    hb_obj = cls(None)
    dup = hb_obj.ref.duplicate()
    assert dup == hb_obj.ref
    assert dup is not hb_obj.ref
