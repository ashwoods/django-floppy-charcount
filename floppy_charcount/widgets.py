from floppyforms.widgets import TextInput, Textarea


class CountInput(TextInput):
    """Floppy input widget that adds a js char counter"""

    template_name = "floppy_charcount/input.html"


class CountTextArea(Textarea):
    """Floppy textarea widget that adds a js char counter"""

    template_name = "floppy_charcount/textarea.html"

    class Media:
        css = {'screen': ('floppy_charcount/css/charsleft.css',)}
        js = ('floppy_charcount/js/charsleft.js',)
