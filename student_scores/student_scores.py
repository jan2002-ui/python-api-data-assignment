import matplotlib.pyplot as plt


# -----------------------------------
# Student test score data
# -----------------------------------

students = [
    {
        "student": "Arun",
        "score": 78
    },
    {
        "student": "Priya",
        "score": 85
    },
    {
        "student": "Rahul",
        "score": 92
    },
    {
        "student": "Divya",
        "score": 88
    },
    {
        "student": "Karthik",
        "score": 74
    }
]


# -----------------------------------
# Extract names and scores
# -----------------------------------

names = []
scores = []


for student in students:

    names.append(student["student"])
    scores.append(student["score"])


# -----------------------------------
# Calculate average
# -----------------------------------

average_score = sum(scores) / len(scores)


print("Student Test Scores")
print("-" * 40)

for student in students:

    print(
        f"{student['student']}: "
        f"{student['score']}"
    )

print("-" * 40)

print(
    f"Average Score: "
    f"{average_score:.2f}"
)


# -----------------------------------
# Create bar chart
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.bar(names, scores)

plt.xlabel("Students")
plt.ylabel("Test Score")

plt.title("Student Test Scores")

plt.axhline(
    average_score,
    linestyle="--",
    label=f"Average: {average_score:.2f}"
)

plt.legend()

plt.tight_layout()

plt.show()