from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

client = OpenAI()
video_id = "VIDEO_ID_HERE"

transcript = YouTubeTranscriptApi.get_transcript(video_id)
text = " ".join([t["text"] for t in transcript])

summary = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": f"Summarize:\n{text}"}],
)

with open("knowledge_base.txt", "a") as f:
    f.write(summary.choices[0].message.content + "\n\n")
