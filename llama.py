import boto3
import json
import time
from botocore.exceptions import ClientError

# Initialize Bedrock client
brt = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set LLaMA model ID
# llama3-3-70b-instruct-v1:0 // llama3-2-3b-instruct-v1:0
model_id = "us.meta.llama3-3-70b-instruct-v1:0"  

# Define multiple prompts
prompts = ["add here"]
# Function to format prompt as a single chat string
def format_prompt(prompt_text):
    return f"<|start_header_id|>user<|end_header_id|>\n{prompt_text}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n"

# Loop through prompts
for idx, prompt in enumerate(prompts):
    llama_payload = {
        "prompt": format_prompt(prompt),
        "max_gen_len": 512,
        "temperature": 0.6,
        "top_p": 0.9
    }

    try:
        start_time = time.time()

        # Call the model
        response = brt.invoke_model(
            modelId=model_id,
            body=json.dumps(llama_payload),
            contentType="application/json",
            accept="application/json"
        )

        latency = time.time() - start_time

        # Parse model response
        model_response = json.loads(response["body"].read())

        print(f"\n--- Prompt #{idx + 1} ---")
        print(f"Prompt: {prompt}")
        print(f"Response: {model_response['generation']}")
        print(f"Latency: {latency:.2f} seconds")

    except (ClientError, Exception) as e:
        print(f"❌ ERROR for prompt #{idx + 1}: {e}")
