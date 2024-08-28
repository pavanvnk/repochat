# Repochat - GitHub Repository Interactive Chatbot

Repochat is an interactive chatbot project designed to engage in conversations about GitHub repositories using a Large Language Model (LLM). It allows users to have meaningful discussions, ask questions, and retrieve relevant information from a GitHub repository. This README provides step-by-step instructions for setting up and using Repochat on your local machine.

https://github.com/pnkvalavala/repochat/assets/108526358/91819459-ddbf-4985-ab84-81c8c67da0e6

## Table of Contents

- [Branches](#branches)
- [Installation](#installation)
- [Usage](#usage)
- [Chatbot Functionality](#chatbot-functionality)
- [Issues](#raising-issues)
- [License](#license)

## Branches

Repochat offers 2 branches with distinct functionalities:

### Main Branch

The [main](https://github.com/pnkvalavala/repochat) branch of Repochat is designed to run entirely on your local machine. This version of Repochat doesn't rely on external API calls and offers greater control over your data. If you're looking for a self-contained solution, the `main` branch is the way to go.

### Cloud Branch

The [cloud](https://github.com/pnkvalavala/repochat/tree/cloud) branch of Repochat primarily relies on API calls to external services for model inference and storage. It's well-suited for those who prefer a cloud-based solution and don't want to set up a local environment.


## Installation

To get started with Repochat, you'll need to follow these installation steps:

1. Create a virtual environment and activate on your local machine to isolate the project's dependencies.
   ```bash
   python -m venv repochat-env
   source repochat-env/bin/activate
   ```

2. Clone the Repochat repository and navigate to the project directory.
   ```bash
   git clone https://github.com/pnkvalavala/repochat.git
   cd repochat
   ```

3. Install the required Python packages using `pip`.
   ```bash
   pip install -r requirements.txt
   ```

4. Install the "llama-cpp-python" library.
    ### Installation without Hardware Acceleration
   ```bash
   pip install llama-cpp-python
   ```

   ### Installation with Hardware Acceleration

    `llama.cpp` supports multiple BLAS backends for faster processing.

    To install with OpenBLAS, set the `LLAMA_BLAS and LLAMA_BLAS_VENDOR` environment variables before installing:

    ```bash
    CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama-cpp-python
    ```

    To install with cuBLAS, set the `LLAMA_CUBLAS=1` environment variable before installing:

    ```bash
    CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
    ```

    To install with CLBlast, set the `LLAMA_CLBLAST=1` environment variable before installing:

    ```bash
    CMAKE_ARGS="-DLLAMA_CLBLAST=on" pip install llama-cpp-python
    ```

    To install with Metal (MPS), set the `LLAMA_METAL=on` environment variable before installing:

    ```bash
    CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
    ```

    To install with hipBLAS / ROCm support for AMD cards, set the `LLAMA_HIPBLAS=on` environment variable before installing:

    ```bash
    CMAKE_ARGS="-DLLAMA_HIPBLAS=on" pip install llama-cpp-python
    ```

    To get to know more about Hardware Acceleration, refer to official README from [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)

5. Create a folder named `models` in the project directory.

6. Download a Language Model from the Hugging Face Model Hub based on your computer's capabilities. It is recommended using the following model as a starting point: [TheBloke/CodeLlama-7B-GGUF](https://huggingface.co/TheBloke/CodeLlama-7B-GGUF/blob/main/codellama-7b.Q4_K_M.gguf). If you want to quantize a model available on Hugging Face, follow the instructions from [llama.cpp](https://github.com/ggerganov/llama.cpp)

7. Copy the downloaded model file to the "models" folder.

8. Open the `models.py` file located in the "repochat" folder and set the model file location in the `code_llama()` function as follows:
   ```python
   def code_llama():
       callbackmanager = CallbackManager([StreamingStdOutCallbackHandler()])
       llm = LlamaCpp(
           model_path="./models/codellama-7b.Q4_K_M.gguf",
           n_ctx=2048,
           max_tokens=200,
           n_gpu_layers=1,
           f16_kv=True,
           callback_manager=callbackmanager,
           verbose=True,
           use_mlock=True
       )
       return llm
   ```

## Usage

1. Open your terminal and run the following command to start the Repochat application:
   ```bash
   streamlit run app.py
   ```

2. You can now input the GitHub repository link.

3. Repochat will fetch all the files from the repository and store them in a folder named "cloned_repo." It will then split the files into smaller chunks and calculate their embeddings using the Sentence Transformers model, specifically [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2).

4. The embeddings are stored locally in a vector database called ChromaDB.

## Chatbot Functionality

Repochat allows you to engage in conversations with the chatbot. You can ask questions or provide input, and the chatbot will retrieve relevant documents from the vector database. It then sends your input, along with the retrieved documents, to the Language Model for generating responses. By default, I've set the model to "codellama-7b-instruct," but you can change it based on your computer's speed, and you can even try the 13b quantized model for responses.

The chatbot retains memory during the conversation to provide contextually relevant responses.

## Raising Issues

If you encounter any issues, have suggestions, or want to report a bug, please visit the [Issues](https://github.com/pnkvalavala/repochat/issues) section of the Repochat repository and create a new issue. Provide detailed information about the problem you're facing, and I'll do my best to assist you.

## License

This project is licensed under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0). For details, see the [LICENSE](LICENSE) file.
Please note that this is a change from the previous license, and it's important to review the terms and conditions of the new license.
