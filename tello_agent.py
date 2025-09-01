
import os
from openai import OpenAI
import re
import tello_wrapper
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# GPT-OSS API CONFIGURATION via Hugging Face
# Get your FREE API key from: https://huggingface.co/settings/tokens
HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found in environment variables. Please set it in .env file.")
MODEL = "openai/gpt-oss-120b:cerebras"  # gpt-oss model via Cerebras provider

# Initialize drone
aw = tello_wrapper.TelloWrapper()

class TelloAgent:
    def __init__(self, system_prompts="system_prompts/airsim_basic.txt", knowledge_prompt="prompts/airsim_basic.txt", chat_history=[], reasoning_effort="medium"):
        # gpt-oss client via Hugging Face
        self.client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=HF_TOKEN,
        )
        self.reasoning_effort = reasoning_effort

        # Chat history list, global variable
        self.chat_history = []

        # System prompt, read and add to chat history
        sys_prompt = open(system_prompts, "r", encoding="utf8").read()
        chat_history.append(
            {
                "role": "system",
                "content": sys_prompt,
            }
        )

        # Knowledge base, add to chat history through chat function
        kg_prompt = open(knowledge_prompt, "r", encoding="utf8").read()
        self.ask(kg_prompt)

    # Call chat API with history for multi-turn conversation
    def ask(self, prompt):
        # Add user input prompt
        self.chat_history.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        completion = self.client.chat.completions.create(
            model=MODEL,
            messages=self.chat_history,  # chat_history[-10:0]
            temperature=0.1,
        )

        # Response
        content = completion.choices[0].message.content

        # Add bot response, equivalent to saving all history for multi-turn conversation
        self.chat_history.append(
            {
                "role": "assistant",
                "content": content,
            }
        )

        return content

    # Parse python code
    def extract_python_code(self, content):
        """
        Extracts the python code from a response.
        :param content:
        :return:
        """
        code_block_regex = re.compile(r"```(.*?)```", re.DOTALL)
        code_blocks = code_block_regex.findall(content)
        if code_blocks:
            full_code = "\n".join(code_blocks)

            if full_code.startswith("python"):
                full_code = full_code[7:]

            return full_code
        else:
            return None

    def process(self, command, run_python_code=False):
        # step 1, ask gpt-oss
        response = self.ask(command)

        # step 2, extract python code
        python_code = self.extract_python_code(response)

        # step 3, exec python code
        if run_python_code and python_code:
            exec(python_code)
        return python_code
    
    def advanced_reasoning(self, command, reasoning_effort="high"):
        """
        Use gpt-oss advanced reasoning capabilities for complex drone missions
        """
        try:
            enhanced_prompt = f"""
            TELLO DRONE MISSION: {command}
            
            Please provide detailed reasoning for this Tello drone mission including:
            1. Safety considerations for indoor/outdoor flight
            2. Step-by-step execution plan
            3. Potential risks and mitigation strategies
            4. Python code to execute the mission using Tello functions
            
            Use your advanced reasoning capabilities to ensure safe and optimal execution.
            """
            
            response = self.ask(enhanced_prompt)
            python_code = self.extract_python_code(response)
            
            return {
                'reasoning': response,
                'code': python_code
            }
        except Exception as e:
            print(f"Advanced reasoning failed, falling back to standard mode: {e}")
            return {
                'reasoning': self.ask(command),
                'code': self.extract_python_code(self.ask(command))
            }

if __name__=="__main__":
    tello_agent = TelloAgent()
    command = "takeoff"
    python_code = tello_agent.process(command)
    print("python_code:", python_code)
