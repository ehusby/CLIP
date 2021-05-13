from lib import base_func
base_func.test_pyperclip_import_standalone()
import pyperclip
try:
    from lib.shared_func import geo_coords_to_address

    pyperclip.copy(
        geo_coords_to_address(
            pyperclip.paste(),
            coord_axis_order=('lat', 'lon')
        )
    )

except:
    base_func.display_error_message()
    base_func.wait_for_user_exit()
