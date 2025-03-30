import argparse
from flowtune.parser import QuantumFlowtuneParser
from flowtune.executor import QuantumFlowtuneExecutor

def main():
    parser = argparse.ArgumentParser(description='Run Flowtune script')
    parser.add_argument('file', help='Path to .ft script')
    args = parser.parse_args()

    p = QuantumFlowtuneParser(args.file)
    p.parse(auto_config=True)

    e = QuantumFlowtuneExecutor(p.resources, p.groups, p.execution_plan)
    e.run()

if __name__ == '__main__':
    main()
