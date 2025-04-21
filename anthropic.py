import boto3
import json
import time
import asyncio
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client.
brt = boto3.client("bedrock-runtime", region_name="us-east-1")  # adjust region if needed

# Anthropic Claude 3 Sonnet Model ID
model_id = "us.anthropic.claude-3-5-haiku-20241022-v1:0"   # anthropic.claude-3-5-haiku-20241022-v1:0 / us.anthropic.claude-3-7-sonnet-20250219-v1:0

# Define multiple prompts
prompts = ["add here"]

# Iterate through prompts
for idx, prompt in enumerate(prompts):
    native_request = {
        "anthropic_version": "bedrock-2023-05-31",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 256,
        "temperature": 0.5
    }

    request_json = json.dumps(native_request)

    try:
        start_time = time.time()

        # Invoke Claude
        response = brt.invoke_model(
            modelId=model_id,
            body=request_json,
            contentType="application/json",
            accept="application/json"
        )

        duration = time.time() - start_time

        # Parse response
        model_response = json.loads(response["body"].read())
        assistant_message = model_response["content"][0]["text"]

        print(f"\n--- Prompt #{idx + 1} ---")
        print(f"Prompt: {prompt}")
        print(f"Response: {assistant_message}")
        print(f"Latency: {duration:.2f} seconds")

    except (ClientError, Exception) as e:
        print(f"❌ ERROR for prompt #{idx + 1}: {e}")
