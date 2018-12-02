from .forms import ProductForm, SupplierProductForm


def get_form_name(user_type):
    if user_type == 1:
        form = ProductForm
    elif user_type == 2:
        form = SupplierProductForm
    else:
        return None
    return form
