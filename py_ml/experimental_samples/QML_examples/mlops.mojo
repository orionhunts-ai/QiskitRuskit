struct MLOps:
    var data: String
    var tool_list: ListLiteral

    fn __init__( self, tool_list: ListLiteral, data: String):
        self.tool_list = tool_list
        self.data = data

    fn start_tools(self.tools):
        for ix in tools: