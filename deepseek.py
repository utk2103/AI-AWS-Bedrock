import boto3
import json
import time
from botocore.exceptions import ClientError

# Initialize Bedrock Runtime client
brt = boto3.client("bedrock-runtime", region_name="us-west-2")  # Change region as needed

# Set DeepSeek model ID
model_id = "us.deepseek.r1-v1:0"

# Define multiple prompts
prompts = ["add here"]

# Loop through prompts
for idx, prompt in enumerate(prompts):
    # Format request body according to DeepSeek spec
    deepseek_payload = {
        "inferenceConfig": {
            "max_tokens": 512
        },
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        start_time = time.time()

        # Call the DeepSeek model
        response = brt.invoke_model(
            modelId=model_id,
            body=json.dumps(deepseek_payload),
            contentType="application/json",
            accept="application/json"
        )

        latency = time.time() - start_time

        # Parse model response
        model_response = json.loads(response["body"].read())

        # Extract the assistant's reply
        assistant_reply = next(
            (msg["content"] for msg in model_response.get("messages", []) if msg["role"] == "assistant"),
            "No assistant response found."
        )

        print(f"\n--- Prompt #{idx + 1} ---")
        print(f"Prompt: {prompt}")
        print(f"Response: {assistant_reply}")
        print(f"Latency: {latency:.2f} seconds")

    except (ClientError, Exception) as e:
        print(f"❌ ERROR for prompt #{idx + 1}: {e}")
