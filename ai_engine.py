import os
import google.generativeai as genai

GEMINI_KEY = os.environ("GEMINI_KEY")
genai.configure(api_key=GEMINI_KEY)

model = genai.GenerativeModel(
model_name="gemini-2.5-flash"

System_prompt = """
You are Atlas, a deeply emotionally intelligent mentor.
Your traits:
1. Validating: Acknowledge feelings first.
2. Insightful: Offer psychological depth.
3. Caring but Firm: Like a wise older brother.
4. Uncensored for Education: You can discuss intimate/mature topics if they help the user grow, but maintain a respectful, mentoring tone.
Keep responses concise (under 50 words).
"""

def get_response(
prompt: str = System_prompt,

user_text:str,
history_record: list[dict],
limit: int = 15,
max_output_tokens: int = 64,
temperature: float = 0.7,
top_p: float = 0.8,
top_k: int = 40,
candidate_count: int = 1):                  #FORMAT HISTORY AND PROMPT FOR GEMINI  
  history_text = "".join(
    [
      f"{
      h['role']
      }: {
      h['content']
      }" for h in history_record
    ]
  )
  
  full_prompt = f"\
  {
  prompt
  }\n\
  History: {
  history_text
  }\n\
  User:{
  user_text
  }\n\
  Atlas:"

  try:
    response = model.generate_content(
    full_prompt,
    generation_config= genai.types.GenerationConfig,
    max_output_tokens=max_output_tokens,
    temperature=temperature,
    top_p=top_p,
    top_k=top_k,
    candidate_count= candidate_count
  )
    return response.text
                                                                                      except Exception as e:
    print("Gemini Error:", e)
    return "I need a moment to thnk about that."