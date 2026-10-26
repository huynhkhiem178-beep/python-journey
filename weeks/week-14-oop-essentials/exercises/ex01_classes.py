"""Exercise 01: class, object and methods."""


class Progress:
    def __init__(self, completed, total):
        self.completed = completed
        self.total = total

    def percentage(self):
        if self.total == 0:
            return 0
        return self.completed / self.total * 100

    def __str__(self):
        return f"Progress: {self.completed}/{self.total}"


progress = Progress(3, 5)

print(progress)
print(f"Percentage: {progress.percentage():.1f}%")
