from functools import wraps

class Templates(object):
    # self.view.line_endings() # can make use of this
    newline = "\n";
    function_begin = "function function_name() { %s" % newline
    function_end = "%s}" % newline
    assign = " = "
    variable_name = "variable"


    def cover_with_newlines(function):
        def wrapper(*args):
            return "{0}{1}{0}".format("\n", function(*args))
        return wrapper

    @classmethod
    @cover_with_newlines
    def get_variable(cls, var_name, expression, suffix=''):
        return "{0}{1}{2}".format(var_name + str(suffix), cls.assign, expression)

    def get_function(definition):
        refactored_definition = "\t"+definition.replace("\n", "\n\t")
        print(refactored_definition)
        return Templates.function_begin + refactored_definition + Templates.function_end

class VariableGenerator:

    seq_number = 0

    def get_unique_variable():
        VariableGenerator.seq_number += 1
        return "{0}{1}".format(Templates.variable_name, VariableGenerator.seq_number)

class Util:

    def get_all_matched_regions(view, pattern):
        if pattern:
            matched_regions = view.find_all(pattern)
            if matched_regions:
                return matched_regions
        return []

    def contains(boundary, point):
        if boundary and point:
            return (point.begin() >= boundary.begin() and point.end() <= boundary.end())

    def filter_regions_not_in_range(regions, range):
        return [region for region in regions if not Util.contains(range, region)]
