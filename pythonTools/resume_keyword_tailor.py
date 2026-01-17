from openai import OpenAI

client = OpenAI()

resume = open("resume.md").read()
job = open("job.txt").read()

prompt = f"""
Compare this resume to the job description.
List missing or weak keywords to improve ATS matching.

RESUME:
{resume}

JOB DESCRIPTION:
{job}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)
