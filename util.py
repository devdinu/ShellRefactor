class Templates:
    function_begin = "function function_name() {\n"
    function_end = "\n}"

    def get_function(definition):
        refactored_definition = "\t"+definition.replace("\n", "\n\t")
        print(refactored_definition)
        return Templates.function_begin + refactored_definition + Templates.function_end 

