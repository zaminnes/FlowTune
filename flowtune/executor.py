
import requests

class SimpleFlowtuneExecutor:
    def __init__(self, resources):
        self.resources = resources
        self.loaded_resources = set()

    def load_resource(self, name, url):
        if url not in self.loaded_resources:
            response = requests.get(url)
            if response.status_code == 200:
                self.loaded_resources.add(url)
                print(f"Resource '{name}' loaded and tracked successfully.")
            else:
                print(f"Failed to load resource '{name}'. Status code: {response.status_code}")
        else:
            print(f"Resource '{name}' already loaded. Skipping.")

    def run(self):
        for name, resource in sorted(self.resources.items(), key=lambda item: item[1]['priority']):
            self.load_resource(name, resource['url'])
