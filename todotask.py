task = []
def add_task(task):
 tasks.append(task)
 print(f"✓ Added: {task}")
def remove_task(task):
 if task in tasks:
  tasks.remove(task)
 print(f"✓ Completed: {task}")
else:
print(f"✗ Task not found: {task}")

def show_tasks():
 if len(tasks) == 0:
      print("No tasks! You're all done.")
 else:
print(f"\nTODO LIST ({len(tasks)} tasks):")
for i, task in enumerate(tasks, 1):
 print(f"{i}. {task}")
# Use the system
add_task("Study Python")
add_task("Complete assignment")
add_task("Practice coding")
show_tasks()
remove_task("Study Python")
show_tasks()