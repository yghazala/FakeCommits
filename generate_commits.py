from datetime import datetime, timedelta
import subprocess
import random

def create_commit(date: datetime):
    dateStr = date.strftime("%a %b %d %I:%M %Y +0700")
    with open("test.txt", "a") as f:
        f.write("Commit\n")
    subprocess.run(["git", "add", "test.txt"])
    subprocess.run(["git", "commit", "-m", "some stuff"])
    subprocess.run(["git", "commit", "--amend", "-m", "some stuff", f'--date="{dateStr}"'])

def create_commits_for_date(numCommits: int, date: datetime):
    print(f"Creating {numCommits} commits on {date.strftime('%a %b %d %Y')}")
    for _ in range(numCommits):
        create_commit(date)

def get_start_date():
    today = datetime.today()
    monday = today - timedelta(days=today.weekday())
    start_date = monday - timedelta(weeks=52, days=1)
    return start_date

def main():
    base_date = get_start_date()
    print(f"Base date: {base_date}")
    total_days = 52 * 7

    for day_offset in range(total_days):
        current_date = base_date + timedelta(days=day_offset)
        num_commits = random.randint(2, 29)  # Random number of commits for each day

        if num_commits > 0:
            create_commits_for_date(num_commits, current_date)

if __name__ == "__main__":
    main()
