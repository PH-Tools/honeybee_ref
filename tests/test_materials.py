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

from honeybee_energy_ref.properties.hb_obj import _HBObjectWithReferences
from honeybee_energy_ref.image_ref import ImageReference
from honeybee_energy_ref.document_ref import DocumentReference

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
    ]
)
def test_material_properties(cls):
    hb_obj = cls(None)
    assert hasattr(hb_obj, "_ref")


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
    ]
)
def test_to_dict_from_dict_round_trip(cls):
    # -------------------------------------------------------------------------
    # Test empty
    hb_parent_obj = cls(None)
    d = hb_parent_obj.ref.to_dict()
    hb_obj2 = _HBObjectWithReferences.from_dict(d["ref"], None)
    assert hb_obj2 == hb_parent_obj.ref

    # -------------------------------------------------------------------------
    # Test with ImageReference
    img_ref = ImageReference()
    img_ref.thumbnail_image_uri = "http://example.com/thumbnail.jpg"
    img_ref.full_size_image_uri = "http://example.com/fullsize.jpg"
    dup_ref_obj = hb_parent_obj.ref.duplicate()
    dup_ref_obj.unlock()
    dup_ref_obj.add_image_ref(img_ref)

    d = dup_ref_obj.to_dict()
    new_ref = _HBObjectWithReferences.from_dict(d["ref"], None)
    assert new_ref == dup_ref_obj

    # -------------------------------------------------------------------------
    # Test with DocumentReference
    doc_ref = DocumentReference()
    doc_ref.document_uri = "http://example.com/document.pdf"
    doc_ref.thumbnail_image_uri = "http://example.com/thumbnail.jpg"
    doc_ref.full_size_image_uri = "http://example.com/fullsize.jpg"
    dup_ref_obj = hb_parent_obj.ref.duplicate()
    dup_ref_obj.unlock()
    dup_ref_obj.add_document_ref(doc_ref)

    d = dup_ref_obj.to_dict()
    new_ref = _HBObjectWithReferences.from_dict(d["ref"], None)
    assert new_ref == dup_ref_obj

    # -------------------------------------------------------------------------
    # Test with URIs
    dup_ref_obj = hb_parent_obj.ref.duplicate()
    dup_ref_obj.unlock()
    dup_ref_obj.add_uri("http://example.com/resource1")
    dup_ref_obj.add_uri("http://example.com/resource2")
    d = dup_ref_obj.to_dict()
    new_ref = _HBObjectWithReferences.from_dict(d["ref"], None)
    assert new_ref == dup_ref_obj


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
    ]
)
def test_duplicate(cls):
    # -------------------------------------------------------------------------
    # Test empty
    hb_obj = cls(None)
    dup = hb_obj.ref.duplicate()
    assert dup == hb_obj.ref
    assert dup is not hb_obj.ref

    # -------------------------------------------------------------------------
    # Test with ImageReference
    img_ref = ImageReference()
    img_ref.thumbnail_image_uri = "http://example.com/thumbnail.jpg"
    img_ref.full_size_image_uri = "http://example.com/fullsize.jpg"
    dup_ref_obj = hb_obj.ref.duplicate()
    dup_ref_obj.unlock()
    dup_ref_obj.add_image_ref(img_ref)
    dup = dup_ref_obj.duplicate()
    assert dup == dup_ref_obj

    # -------------------------------------------------------------------------
    # Test with DocumentReference
    doc_ref = DocumentReference()
    doc_ref.document_uri = "http://example.com/document.pdf"
    doc_ref.thumbnail_image_uri = "http://example.com/thumbnail.jpg"
    doc_ref.full_size_image_uri = "http://example.com/fullsize.jpg"
    dup_ref_obj = hb_obj.ref.duplicate()
    dup_ref_obj.unlock()
    dup_ref_obj.add_document_ref(doc_ref)
    dup = dup_ref_obj.duplicate()
    assert dup == dup_ref_obj

    # -------------------------------------------------------------------------
    # Test with URIs
    dup_ref_obj = hb_obj.ref.duplicate()
    dup_ref_obj.unlock()
    dup_ref_obj.add_uri("http://example.com/resource1")
    dup_ref_obj.add_uri("http://example.com/resource2")
    dup = dup_ref_obj.duplicate()
    assert dup == dup_ref_obj

