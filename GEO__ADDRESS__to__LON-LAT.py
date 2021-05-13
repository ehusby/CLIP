from lib import clip_func
clip_func.test_pyperclip_import_standalone()
import pyperclip
try:
    from lib.shared_func import geo_address_to_coords

    pyperclip.copy(
        geo_address_to_coords(
            pyperclip.paste(),
            coord_axis_order=('lon', 'lat')
        )
    )

except:
    clip_func.display_error_message()
    clip_func.wait_for_user_exit()