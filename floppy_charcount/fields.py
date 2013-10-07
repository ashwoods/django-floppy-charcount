from floppyforms.fields import CharField
from .widgets import CountTextArea, CountInput


class CountCharField(CharField):
    widget = CountInput

    def widget_attrs(self, widget):
        attrs = super(CharField, self).widget_attrs(widget)
        if attrs is None:
            attrs = {}
        # The HTML attribute is maxlength, not max_length.
        attrs.update({'maxlength': str(self.max_length)})
        return attrs


class CountTextAreaField(CharField):

    widget = CountTextArea

    def widget_attrs(self, widget):
        attrs = super(CharField, self).widget_attrs(widget)
        if attrs is None:
            attrs = {}
        # The HTML attribute is maxlength, not max_length.
        attrs.update({'maxlength': str(self.max_length)})
        return attrs
