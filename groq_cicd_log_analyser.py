from groq import Groq
import os

def analyse_logs(log_file, out_file):
    try:
        from gen_prompt import prompt_func
        
        client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt_func(log_file),
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        groq_resp = "".join(chat_completion.choices[0].message.content)
        
        with open(out_file, "w") as file:
            file.write(groq_resp)
        
        
    except Exception as e:
        print(f"Exception caught in main: {e}")

if __name__ == "__main__":
    log_file = "jenkins_logs.txt"
    out_file = "groq_analysis.md"
    analyse_logs(log_file, out_file)