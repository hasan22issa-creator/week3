
# ─────────────────────────────────────────────
# 3. filter_tasks() WITH **kwargs
# ─────────────────────────────────────────────



tasks = [
    {"title": "Fix login bug",    "status": "open",   "owner": "Hasan"},
    {"title": "Write unit tests", "status": "closed", "owner": "Ali"},
    {"title": "Deploy to server", "status": "open",   "owner": "Hasan"},
    {"title": "Code review",      "status": "open",   "owner": "Ali"},
]

def filter_tasks(tasks, status=None, owner=None):
    # Go through every task and keep it only if it matches the given filters.
    # If a filter is None, it means "don't filter by this" — so everything passes.
    return [
        task for task in tasks
        if (status is None or task["status"] == status)
        and (owner is None or task["owner"] == owner)
    ]




# Get all open tasks (no owner filter)
open_tasks = filter_tasks(tasks, status="open")
print("Open tasks:")
for t in open_tasks:
    print(f"  - {t['title']} (owner: {t['owner']})")

# Get all of Hasan's tasks (no status filter)
hasan_tasks = filter_tasks(tasks, owner="Hasan")
print("\nHasan's tasks:")
for t in hasan_tasks:
    print(f"  - {t['title']} (status: {t['status']})")

# Get Ali's open tasks only
ali_open = filter_tasks(tasks, status="open", owner="Ali")
print("\nAli's open tasks:")
for t in ali_open:
    print(f"  - {t['title']}")