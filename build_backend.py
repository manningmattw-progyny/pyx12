from __future__ import absolute_import

import sys


if sys.version_info >= (3, 8):
    try:
        import hatchling.build as _backend
    except ImportError:
        raise RuntimeError(
            "hatchling is required to build pyx12 on Python >= 3.8"
        )
else:
    try:
        from setuptools.build_meta import __legacy__ as _backend
    except Exception:
        from setuptools import build_meta as _backend


_HOOKS = [
    "build_wheel",
    "build_sdist",
    "build_editable",
    "get_requires_for_build_wheel",
    "get_requires_for_build_sdist",
    "get_requires_for_build_editable",
    "prepare_metadata_for_build_wheel",
    "prepare_metadata_for_build_sdist",
    "prepare_metadata_for_build_editable",
]

for _name in _HOOKS:
    if hasattr(_backend, _name):
        globals()[_name] = getattr(_backend, _name)
