from config import client_openai
import asyncio

async def query_llm(prompt):
    system_prompt = {
        "role": "system",
        "content": open("prompts/elara_system_prompt.txt").read()
    }

    response = await asyncio.to_thread(
        lambda: client_openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[system_prompt, {"role": "user", "content": prompt}],
            temperature=0.7
        )
    )
    return response.choices[0].message.content.strip()