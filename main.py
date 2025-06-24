import os
import platform
from pathlib import Path

import dearpygui.dearpygui as dpg

if platform.system() == "Windows":  # necessary for correct display of fonts on Windows
    os.environ["PYTHONIOENCODING"] = "utf-8"
    os.environ["PYTHONUTF8"] = "1"

dpg.create_context()
dpg.create_viewport(title="Test", width=600, height=600)


font_base_path = Path("non-ASCII_символы/fonts/Monocraft/Monocraft.otf")
with dpg.font_registry():
    # There should be an error when trying to register a font with non-ASCII
    with dpg.font(str(font_base_path), 13) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)

dpg.bind_font(default_font)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
