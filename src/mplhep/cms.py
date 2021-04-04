import inspect
from matplotlib import docstring

# Log styles
from .styles import cms as style
from . import label as label_base
from .label import lumitext
import mplhep

# import mplhep._deprecate as deprecate

__all__ = ("style", "lumitext")


# Experiment wrappers:
def _cms_text(text="", **kwargs):
    for key, value in dict(mplhep.rcParams.text._get_kwargs()).items():
        if (
            value is not None
            and key not in kwargs.keys()
            and key in inspect.getfullargspec(label_base.exp_text).kwonlyargs
        ):
            kwargs[key] = value
    return label_base.exp_text("CMS", text=text, italic=(False, True), **kwargs)


def _cms_label(**kwargs):
    for key, value in dict(mplhep.rcParams.label._get_kwargs()).items():
        if (
            value is not None
            and key not in kwargs.keys()
            and key in inspect.getfullargspec(label_base.exp_label).kwonlyargs
        ):
            kwargs[key] = value
        print(kwargs)
    return label_base.exp_label(exp="CMS", **kwargs)


# Deprecation example
# @deprecate.deprecate("Naming convention is changing. Use ``mplhep.cms.label``.")
# def cmslabel(*args, **kwargs):
#     return _cms_label(*args, **kwargs)


@docstring.copy(label_base.exp_text)
def text(*args, **kwargs):
    return _cms_text(*args, **kwargs)


def label(**kwargs):
    return _cms_label(**kwargs)
