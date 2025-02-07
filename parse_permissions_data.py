
data = """
get allowed tools data from new relic and paste it here
"""


# Parse the JSON string
parsed_data = json.loads(data)

# Dictionary to store counts of tool and permission combinations
tool_permission_count = defaultdict(int)

# Extract tools and permissions
for result in parsed_data:
    for res in result.get("results", []):
        for event in res.get("events", []):
            tool_data = event.get("tool", "")
            # Split by ',' and process each item
            tools = [item.strip() for item in tool_data.split(',') if item]
            for tool in tools:
                tool_name, permission = tool.split('.')
                tool_permission_count[(tool_name, permission)] += 1

# Generate and print the grouped table
print(f"{'Tool':<10} {'Permission':<10} {'Count':<5}")
print("-" * 30)
for (tool, permission), count in tool_permission_count.items():
    print(f"{tool:<10} {permission:<10} {count:<5}")
