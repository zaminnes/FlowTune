class QuantumFlowtuneExecutor:
    def __init__(self, resources, groups, execution_plan):
        self.resources = resources
        self.groups = groups
        self.execution_plan = execution_plan

    def run(self):
        print("Executing Flowtune Plan...")
        for group in self.execution_plan:
            print(f"Loading group: {group}")
            for res in self.groups[group]:
                print(f" -> Loading: {res} (priority: {self.resources[res]['priority']})")
