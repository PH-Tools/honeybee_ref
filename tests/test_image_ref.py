from honeybee_energy_ref.image_ref import ImageReference


def test_blank_image_reference_to_dict_from_dict_roundtrip():
    img_ref = ImageReference()

    # Convert to dictionary and back
    img_dict = img_ref.to_dict()
    new_img_ref = ImageReference.from_dict(img_dict)

    # Check if the new instance matches the original
    assert new_img_ref.identifier == img_ref.identifier
    assert new_img_ref.thumbnail_image_uri == img_ref.thumbnail_image_uri
    assert new_img_ref.full_size_image_uri == img_ref.full_size_image_uri


def test_image_reference_to_dict_from_dict_roundtrip():
    img_ref = ImageReference()
    img_ref.thumbnail_image_uri = "http://example.com/thumbnail.jpg"
    img_ref.full_size_image_uri = "http://example.com/fullsize.jpg"

    # Convert to dictionary and back
    img_dict = img_ref.to_dict()
    new_img_ref = ImageReference.from_dict(img_dict)

    # Check if the new instance matches the original
    assert new_img_ref.identifier == img_ref.identifier
    assert new_img_ref.thumbnail_image_uri == img_ref.thumbnail_image_uri
    assert new_img_ref.full_size_image_uri == img_ref.full_size_image_uri


def test_blank_image_reference_duplicate():
    img_ref = ImageReference()

    # Duplicate the instance
    duplicated_img_ref = img_ref.duplicate()
    assert duplicated_img_ref.identifier == img_ref.identifier


def test_image_reference_duplicate():
    img_ref = ImageReference()
    img_ref.thumbnail_image_uri = "http://example.com/thumbnail.jpg"
    img_ref.full_size_image_uri = "http://example.com/fullsize.jpg"

    # Duplicate the instance
    duplicated_img_ref = img_ref.duplicate()

    # Check if the duplicated instance matches the original
    assert duplicated_img_ref.identifier == img_ref.identifier
    assert duplicated_img_ref.thumbnail_image_uri == img_ref.thumbnail_image_uri
    assert duplicated_img_ref.full_size_image_uri == img_ref.full_size_image_uri

