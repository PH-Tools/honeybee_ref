from honeybee_energy_ref.document_ref import DocumentReference


def test_blank_document_reference_to_dict_from_dict_roundtrip():
    doc_ref = DocumentReference()

    # Convert to dictionary and back
    img_dict = doc_ref.to_dict()
    new_img_ref = DocumentReference.from_dict(img_dict)

    # Check if the new instance matches the original
    assert new_img_ref.identifier == doc_ref.identifier
    assert new_img_ref.thumbnail_image_uri == doc_ref.thumbnail_image_uri
    assert new_img_ref.full_size_image_uri == doc_ref.full_size_image_uri


def test_document_reference_to_dict_from_dict_roundtrip():
    doc_ref = DocumentReference()
    doc_ref.document_uri = "http://example.com/document.pdf"
    doc_ref.thumbnail_image_uri = "http://example.com/thumbnail.jpg"
    doc_ref.full_size_image_uri = "http://example.com/fullsize.jpg"

    # Convert to dictionary and back
    img_dict = doc_ref.to_dict()
    new_img_ref = DocumentReference.from_dict(img_dict)

    # Check if the new instance matches the original
    assert new_img_ref.identifier == doc_ref.identifier
    assert new_img_ref.document_uri == doc_ref.document_uri
    assert new_img_ref.thumbnail_image_uri == doc_ref.thumbnail_image_uri
    assert new_img_ref.full_size_image_uri == doc_ref.full_size_image_uri


def test_blank_document_reference_duplicate():
    doc_ref = DocumentReference()

    # Duplicate the instance
    duplicated_img_ref = doc_ref.duplicate()
    assert duplicated_img_ref.identifier == doc_ref.identifier


def test_document_reference_duplicate():
    doc_ref = DocumentReference()
    doc_ref.document_uri = "http://example.com/document.pdf"
    doc_ref.thumbnail_image_uri = "http://example.com/thumbnail.jpg"
    doc_ref.full_size_image_uri = "http://example.com/fullsize.jpg"

    # Duplicate the instance
    duplicated_img_ref = doc_ref.duplicate()

    # Check if the duplicated instance matches the original
    assert duplicated_img_ref.identifier == doc_ref.identifier
    assert duplicated_img_ref.document_uri == doc_ref.document_uri
    assert duplicated_img_ref.thumbnail_image_uri == doc_ref.thumbnail_image_uri
    assert duplicated_img_ref.full_size_image_uri == doc_ref.full_size_image_uri
