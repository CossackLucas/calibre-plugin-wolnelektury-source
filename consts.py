'''
Source of main data
'''
import re

# pylint: disable=import-error
from calibre.constants import numeric_version

# needed to lower required calibre version below 6.12.0
try:
    from calibre.utils.localization import _
except ImportError:
    from gettext import gettext as _
# pylint: enable=import-error

# pylint: disable=undefined-variable
# required to run tests
try:
    load_translations()
except NameError:
    pass
# pylint: enable=undefined-variable

PLUGIN_VERSION = (1, 0, 1)
PLUGIN_NAME = 'WolneLektury'
WOLNELEKTURY_ID = 'wolnelektury'

ID_REGEX = re.compile(r'/katalog/lektura/([a-z\-]+)/')
AUTHOR_ID_REGEX = re.compile(r'/katalog/autor/([a-z\-]+)/')
WOLNELEKTURY_ID_REGEX = [
    re.compile(r'wolnelektury.pl\/katalog\/lektura\/([a-z\-]+)'),
    re.compile(r'wolnelektury.pl\/media\/book\/cover\/([a-z\-]+).jpg'),
    re.compile(r'wolnelektury.pl\/media\/book\/cover_simple\/([a-z\-]+)_[a-zA-Z0-9]+.jpg'
    )
]

PLUGIN_DESCRIPTION = _('Download metadata and covers from site wolnelektury.pl')

CONFIG_HELP_MESSAGE = '<p>' + \
    _('Calibre: {calibre_version} • Plugin version: {plugin_version}' + \
        ' • Please report bugs through the {mobileread_link}MobileRead{closing_link}' + \
        ' forum or {github_link}GitHub{closing_link}.').format(
        calibre_version = '<b>' + '.'.join([str(x) for x in numeric_version]) + '</b>',
        plugin_version = '<b>' + '.'.join([str(x) for x in PLUGIN_VERSION]) + '</b>',
        mobileread_link = '<a href="https://www.mobileread.com/forums/showthread.php?t=373972">',
        github_link = '<a href="https://github.com/CossackLucas/wolnelektury_source">',
        closing_link = '</a>') \
    + '<br>' + \
    _('{open_bold}Warning{closing_bold}: ' + \
        'ISBN could be pointing to different file format edition of the book.').format(
        open_bold = '<b>',
        closing_bold = '</b>') \
    + '</p>'
