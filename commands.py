import sublime_plugin
from .util import Templates

class ExtractFunctionCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        selected_view=self.view.sel()
        for region in selected_view:
            selected_text = self.view.substr(region)
            self.view.replace(edit, region, Templates.get_function(selected_text))
