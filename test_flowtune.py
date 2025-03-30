from flowtune.parser import QuantumFlowtuneParser
from flowtune.executor import QuantumFlowtuneExecutor

def test_parser_executor():
    parser = QuantumFlowtuneParser('example.ft')
    parser.parse(auto_config=True)
    executor = QuantumFlowtuneExecutor(parser.resources, parser.groups, parser.execution_plan)
    executor.run()

if __name__ == '__main__':
    test_parser_executor()
