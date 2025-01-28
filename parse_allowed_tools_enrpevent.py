import json
from collections import defaultdict


nrql = """ WITH aparse(allowed_tools, '*') AS tool
FROM ENRPEvent
SELECT tool
SINCE 1 day ago"""
data = """

  Run the NRQL in new relic and copy the JSON response here

"""


# Parse the JSON data
parsed_data = json.loads(data)

# Dictionary to store counts of tool and permission combinations
tool_permission_count = defaultdict(int)

# Extract tools and permissions from allowed_tools
for result in parsed_data:
    for res in result.get("results", []):
        for event in res.get("events", []):
            tool_data = event.get("tool", "")
            # Split by ','
            tools = [item.strip() for item in tool_data.split(',') if item]
            for tool in tools:
                tool_name, permission = tool.split('.')
                tool_permission_count[(tool_name, permission)] += 1

print(f"{'Tool':<10} {'Permission':<10} {'Count':<5}")
print("-" * 30)
for (tool, permission), count in tool_permission_count.items():
    print(f"{tool:<10} {permission:<10} {count:<5}")
