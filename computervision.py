from openai import OpenAI

endpoint = "https://project2469-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5.4-mini"
api_key = "653q0aypmnt06Z8atnPZBUsqeM0mqNriEcH1PfCg7wDNzLWaqlGUJQQJ99CKACNns7RXJ3w3AAAAACOGNzfr"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "what's in this image?"},
            {"type": "input_image", "image_url": "https://img.freepik.com/premium-photo/close-up-bicycle-wheel_766625-2488.jpg"},
        ],
    }],
)

print(f"answer: {response.output_text}")