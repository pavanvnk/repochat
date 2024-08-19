from huggingface_hub import snapshot_download

# Define the model repository and the local directory
model_repo = "TheBloke/CodeLlama-7B-GGUF"
local_dir = "./models/CodeLlama-7B-GGUF"  # Specify the directory where you want to download the model

# Download the model to the specified directory
model_dir = snapshot_download(repo_id=model_repo, local_dir=local_dir)

print(f"Model downloaded to: {model_dir}")

