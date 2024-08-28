# Repochat - GitHub Repository Interactive Chatbot

Repochat is an interactive chatbot that allows you to engage in dynamic conversations about GitHub repositories. Powered by a Large Language Models, you have the freedom to choose between two different options for the Language Model:

1. **OpenAI GPT-3.5-turbo model**: Utilize OpenAI's cutting-edge language model to have conversations about GitHub repositories.

2. **Hugging Face Model**: Alternatively, you can opt for any model available on Hugging Face (preferably models like [CodeLlama-Instruct](https://huggingface.co/codellama/CodeLlama-13b-Instruct-hf)). However, this choice comes with the added responsibility of creating an endpoint for your chosen model on Hugging Face. You'll need to provide the endpoint URL and Hugging Face token for this option.

https://github.com/pnkvalavala/repochat/assets/108526358/393f1367-d6e7-4b98-afc2-138b5b2dbcf4

## Branches

Repochat offers two branches with distinct functionalities:

### Main Branch

The [main](https://github.com/pnkvalavala/repochat) branch of Repochat is designed to run entirely on your local machine. This version of Repochat doesn't rely on external API calls and offers greater control over your data and processing. If you're looking for a self-contained solution, the `main` branch is the way to go.

### Cloud Branch

The [cloud](https://github.com/pnkvalavala/repochat/tree/cloud) branch of Repochat primarily relies on API calls to external services for model inference and storage. It's well-suited for those who prefer a cloud-based solution and don't want to set up a local environment.

## Features

- Choose your preferred Language Model:
  - OpenAI GPT models
  - Hugging Face Model (with custom endpoint)

- Choose between two methods for calculating embeddings:
  - OpenAI Embeddings
  - Hugging Face's [Sentence Transformers](https://huggingface.co/docs/hub/sentence-transformers)

- Utilize the power of Activeloop's Deeplake Vector Database for storing and retrieving embeddings.

## Getting Started

Follow the steps below to get started with Repochat:

### Prerequisites

- OpenAI API Key (for GPT-3.5-turbo and OpenAI Embeddings)
- Hugging Face Endpoint (if using a custom model)
- Hugging Face Token (if using a custom model)
- ActiveLoop API (for Deeplake Vector Database)

### Cloud Usage

1. Open the [RepoChat](https://repochat.streamlit.app/) deployed on Streamlit.

2. Configure your preferred language model and embeddings method. Enter all the tokens necessary. Your credentials are only stored in your session state.

3. Input the GitHub repository link you want to discuss. Repochat will fetch all files from the repository, chunk them into smaller files, and calculate and store their embeddings in the Deeplake Vector Database.

4. Start asking questions! Repochat will retrieve relevant documents from the vector database and send them, along with your question, to the Language Model to provide answers.

5. Enjoy interactive conversations about the GitHub repository with the retained memory of the chatbot.

### Local Usage

If you prefer to run the RepoChat project locally and avoid entering your API tokens into Streamlit, you can follow these steps:

1. Create a virtual environment and activate on your local machine to isolate the project's dependencies

   ```bash
   python -m venv repo_env
   source repo_env/bin/activate
   ```

2. Clone the Repochat repository and navigate to the project directory

   ```bash
   git clone -b cloud https://github.com/pnkvalavala/repochat.git
   cd repochat
   ```

3. Install the required Python packages using `pip`

   ```bash
   pip install -r requirements.txt
   ```

4. Run RepoChat Locally

   ```bash
   streamlit run app.py
   ```

Rest all instructions remain same as [Cloud Usage](#cloud-usage)

By following these instructions, you can use RepoChat without relying on a cloud-based deployment, keeping your API tokens and credentials secure on your local environment.

## License

This project is licensed under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0). For details, see the [LICENSE](LICENSE) file.
Please note that this is a change from the previous license, and it's important to review the terms and conditions of the new license.
