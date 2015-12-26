import sublime
import sublime_plugin
import pdb
import sys
from sublime import Region
from .util import *

class ExtractVariableCommand(sublime_plugin.TextCommand):

    def replace_all_occurences(self, region, edit):
        expression = self.view.substr(region)
        unique_variable = VariableGenerator.get_unique_variable()
        self.replace_all(edit, expression, region.begin(), unique_variable)
        assign_value = Templates.get_variable(unique_variable, expression)
        # assign expression as value to variable before the usage
        found = self.view.find(unique_variable, 0)
        self.view.insert(edit, found.begin() ,assign_value)

    def replace_all(self, edit, expression, start, replacement_value):
        occurence = self.view.find(expression, start)
        while occurence:
            self.view.replace(edit, occurence, replacement_value)
            occurence = self.view.find(expression, occurence.begin() + 1)

    def run(self, edit):
        regions = self.view.sel()
        for index, region in enumerate(regions):
            self.replace_all_occurences(region, edit)
