
class ToolAgent:
    def fetch_data(self):
        return {"data": [1,2,3]}

    def analyze_data(self, data):
        return sum(data)

    def generate_report(self, result):
        return f"Report: result={result}"
