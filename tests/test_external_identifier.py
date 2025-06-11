import pytest
from honeybee_energy.properties.extension import (
    EnergyMaterialNoMassProperties,
    EnergyMaterialProperties,
    EnergyMaterialVegetationProperties,
    EnergyWindowFrameProperties,
    EnergyWindowMaterialBlindProperties,
    EnergyWindowMaterialGasCustomProperties,
    EnergyWindowMaterialGasMixtureProperties,
    EnergyWindowMaterialGasProperties,
    EnergyWindowMaterialGlazingsProperties,
    EnergyWindowMaterialShadeProperties,
    EnergyWindowMaterialSimpleGlazSysProperties,
)


@pytest.mark.parametrize(
    "cls",
    [
        EnergyMaterialNoMassProperties,
        EnergyMaterialProperties,
        EnergyMaterialVegetationProperties,
        EnergyWindowFrameProperties,
        EnergyWindowMaterialBlindProperties,
        EnergyWindowMaterialGasCustomProperties,
        EnergyWindowMaterialGasMixtureProperties,
        EnergyWindowMaterialGasProperties,
        EnergyWindowMaterialGlazingsProperties,
        EnergyWindowMaterialShadeProperties,
        EnergyWindowMaterialSimpleGlazSysProperties,
    ],
)
def test_material_properties_add_and_get_external_reference(cls):
    hb_obj = cls(None)
    hb_obj.ref.unlock()
    hb_obj.ref.add_external_identifier("a_test_domain", "a_test_ref_id")
    hb_obj.ref.lock()

    assert hb_obj.ref.get_external_identifier("a_test_domain") == "a_test_ref_id"
