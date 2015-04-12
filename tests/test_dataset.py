"""Tests of dataset metadata."""

import rasterio


def test_get_name(data):
    """Get the correct name of a dataset."""
    with rasterio.open(str(data.join('RGB.byte.tif'))) as src:
        assert src.name.endswith('RGB.byte.tif')


def test_get_driver(data):
    """Get the correct driver of a dataset."""
    with rasterio.open(str(data.join('RGB.byte.tif'))) as src:
        assert 'GTiff' == src.driver


def test_get_count(data):
    """Get the correct band count of a dataset."""
    with rasterio.open(str(data.join('RGB.byte.tif'))) as src:
        assert 3 == src.count


def test_get_height(data):
    """Get the correct height in pixels of a dataset."""
    with rasterio.open(str(data.join('RGB.byte.tif'))) as src:
        assert 718 == src.height


def test_get_width(data):
    """Get the correct width in pixels of a dataset."""
    with rasterio.open(str(data.join('RGB.byte.tif'))) as src:
        assert 791 == src.width


def test_get_shape(data):
    """Get the correct numpy shape of a dataset."""
    with rasterio.open(str(data.join('RGB.byte.tif'))) as src:
        assert (3, 718, 791) == src.shape


def test_get_dtype(data):
    """Get the correct numpy dtype of a dataset."""
    with rasterio.open(str(data.join('RGB.byte.tif'))) as src:
        assert tuple(rasterio.uint8 for _ in range(3)) == src.dtypes
