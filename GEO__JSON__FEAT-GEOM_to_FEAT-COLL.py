#!/usr/bin/env python

from lib import base_func
base_func.test_pyperclip_import()
import pyperclip

pyperclip.copy(
"""
{
  "aoi": {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "properties": {},
        "geometry": %CLIP%
      }
    ]
  }
}
""".replace("%CLIP%", pyperclip.paste())
)
