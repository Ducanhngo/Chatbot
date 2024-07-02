{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMw4m0Yh+gGKzJOPGHX9Bns",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ducanhngo/Chatbot/blob/feature/Chainlit.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Install libraries\n"
      ],
      "metadata": {
        "id": "d6VhFP8MWblc"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fW3tdd6fWXPx",
        "outputId": "2fd01832-2e41-49c7-db98-ef34994d45cd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m119.8/119.8 MB\u001b[0m \u001b[31m5.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m21.3/21.3 MB\u001b[0m \u001b[31m38.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m309.4/309.4 kB\u001b[0m \u001b[31m3.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m974.6/974.6 kB\u001b[0m \u001b[31m10.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m332.8/332.8 kB\u001b[0m \u001b[31m32.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m127.4/127.4 kB\u001b[0m \u001b[31m13.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m145.0/145.0 kB\u001b[0m \u001b[31m12.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m559.5/559.5 kB\u001b[0m \u001b[31m5.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m92.0/92.0 kB\u001b[0m \u001b[31m11.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.4/2.4 MB\u001b[0m \u001b[31m45.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.4/62.4 kB\u001b[0m \u001b[31m7.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m41.3/41.3 kB\u001b[0m \u001b[31m5.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.8/6.8 MB\u001b[0m \u001b[31m42.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m59.9/59.9 kB\u001b[0m \u001b[31m7.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m107.0/107.0 kB\u001b[0m \u001b[31m12.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m67.3/67.3 kB\u001b[0m \u001b[31m6.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Installing build dependencies ... \u001b[?25l\u001b[?25hdone\n",
            "  Getting requirements to build wheel ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m283.7/283.7 kB\u001b[0m \u001b[31m27.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.7/1.7 MB\u001b[0m \u001b[31m23.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m67.6/67.6 kB\u001b[0m \u001b[31m5.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m75.6/75.6 kB\u001b[0m \u001b[31m8.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m71.9/71.9 kB\u001b[0m \u001b[31m8.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m53.6/53.6 kB\u001b[0m \u001b[31m6.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m307.7/307.7 kB\u001b[0m \u001b[31m13.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m77.9/77.9 kB\u001b[0m \u001b[31m8.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m58.3/58.3 kB\u001b[0m \u001b[31m6.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m46.0/46.0 kB\u001b[0m \u001b[31m5.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m52.5/52.5 kB\u001b[0m \u001b[31m6.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m130.5/130.5 kB\u001b[0m \u001b[31m15.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m341.4/341.4 kB\u001b[0m \u001b[31m27.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.4/3.4 MB\u001b[0m \u001b[31m53.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.2/1.2 MB\u001b[0m \u001b[31m49.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m130.2/130.2 kB\u001b[0m \u001b[31m12.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m86.8/86.8 kB\u001b[0m \u001b[31m10.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Building wheel for pypika (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.2/2.2 MB\u001b[0m \u001b[31m18.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m49.2/49.2 kB\u001b[0m \u001b[31m4.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m40.3/40.3 kB\u001b[0m \u001b[31m1.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m327.5/327.5 kB\u001b[0m \u001b[31m7.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.1/1.1 MB\u001b[0m \u001b[31m40.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m227.1/227.1 kB\u001b[0m \u001b[31m4.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.3/4.3 MB\u001b[0m \u001b[31m30.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m91.8/91.8 kB\u001b[0m \u001b[31m11.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m48.7/48.7 kB\u001b[0m \u001b[31m5.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m18.2/18.2 MB\u001b[0m \u001b[31m70.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m53.0/53.0 kB\u001b[0m \u001b[31m6.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m76.2/76.2 kB\u001b[0m \u001b[31m9.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m60.3/60.3 kB\u001b[0m \u001b[31m7.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.3/1.3 MB\u001b[0m \u001b[31m75.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m57.7/57.7 kB\u001b[0m \u001b[31m7.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Building wheel for literalai (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for syncer (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m290.4/290.4 kB\u001b[0m \u001b[31m4.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[K\u001b[?25h/tools/node/bin/lt -> /tools/node/lib/node_modules/localtunnel/bin/lt.js\n",
            "+ localtunnel@2.0.2\n",
            "added 22 packages from 22 contributors in 2.012s\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m17.6/17.6 MB\u001b[0m \u001b[31m38.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "chainlit 1.1.304 requires numpy<2.0,>=1.26; python_version >= \"3.9\", but you have numpy 1.25.0 which is incompatible.\u001b[0m\u001b[31m\n",
            "\u001b[0m"
          ]
        }
      ],
      "source": [
        "!pip install -q transformers==4.41.2\n",
        "!pip install -q bitsandbytes==0.43.1\n",
        "!pip install -q accelerate==0.31.0\n",
        "!pip install -q langchain==0.2.5\n",
        "!pip install -q langchainhub==0.1.20\n",
        "!pip install -q langchain-chroma==0.1.1\n",
        "!pip install -q langchain-community==0.2.5\n",
        "!pip install -q langchain-openai==0.1.9\n",
        "!pip install -q langchain_huggingface==0.0.3\n",
        "!pip install -q chainlit==1.1.304\n",
        "!pip install -q python-dotenv==1.0.1\n",
        "!pip install -q pypdf==4.2.0\n",
        "!npm install -g localtunnel\n",
        "!pip install -q numpy==1.25.0"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import chainlit as cl\n",
        "import torch\n",
        "from chainlit.types import AskFileResponse\n",
        "from transformers import BitsAndBytesConfig\n",
        "from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline\n",
        "from langchain_huggingface.llms import HuggingFacePipeline\n",
        "from langchain.memory import ConversationBufferMemory\n",
        "from langchain_community.chat_message_histories import ChatMessageHistory\n",
        "from langchain.chains import ConversationalRetrievalChain\n",
        "from langchain_huggingface import HuggingFaceEmbeddings\n",
        "from langchain_chroma import Chroma\n",
        "from langchain_community.document_loaders import PyPDFLoader, TextLoader\n",
        "from langchain_text_splitters import RecursiveCharacterTextSplitter\n",
        "from langchain_core.runnables import RunnablePassthrough\n",
        "from langchain_core.output_parsers import StrOutputParser\n",
        "from langchain import hub"
      ],
      "metadata": {
        "id": "Z0r1B8IaW9YB"
      },
      "execution_count": 39,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "text_splitter = RecursiveCharacterTextSplitter(chunk_size =1000, chunk_overlap =100)\n",
        "embedding = HuggingFaceEmbeddings()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "O2ndrIPhXUOP",
        "outputId": "edc4b9b2-a449-489c-d9d0-2b3a9dee1d13"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_token.py:89: UserWarning: \n",
            "The secret `HF_TOKEN` does not exist in your Colab secrets.\n",
            "To authenticate with the Hugging Face Hub, create a token in your settings tab (https://huggingface.co/settings/tokens), set it as secret in your Google Colab and restart your session.\n",
            "You will be able to reuse this secret in all of your notebooks.\n",
            "Please note that authentication is recommended but still optional to access public models or datasets.\n",
            "  warnings.warn(\n",
            "/usr/local/lib/python3.10/dist-packages/huggingface_hub/file_download.py:1132: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.\n",
            "  warnings.warn(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def process_file ( file : AskFileResponse ) :\n",
        "  if file.type == \"text/plain\":\n",
        "    Loader = TextLoader\n",
        "  elif file.type == \"application/pdf\":\n",
        "    Loader = PyPDFLoader\n",
        "  loader = Loader(file.path)\n",
        "  documents = loader.load()\n",
        "  docs = text_splitter.split_documents(documents)\n",
        "  for i, doc in enumerate(docs):\n",
        "    doc.metadata[\"source\"] = f\"source_ {i}\"\n",
        "  return docs"
      ],
      "metadata": {
        "id": "B2qfgN-cXolf"
      },
      "execution_count": 41,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def get_vector_db(file: AskFileResponse):\n",
        "  docs = process_file(file)\n",
        "  cl.user_session.set(\"docs\",docs)\n",
        "  vector_db = Chroma.from_documents ( documents =docs, embedding = embedding)\n",
        "  return vector_db"
      ],
      "metadata": {
        "id": "2IlnHIQxYilS"
      },
      "execution_count": 42,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def get_huggingface_llm(model_name: str = \"lmsys/vicuna-7b-v1.5\",\n",
        "                        max_new_token: int = 512):\n",
        "    nf4_config = BitsAndBytesConfig(\n",
        "        load_in_4bit=True,\n",
        "        bnb_4bit_quant_type=\"nf4\",\n",
        "        bnb_4bit_use_double_quant=True,\n",
        "        bnb_4bit_compute_dtype=torch.bfloat16\n",
        "    )\n",
        "    model = AutoModelForCausalLM.from_pretrained(\n",
        "        model_name,\n",
        "        quantization_config=nf4_config,\n",
        "        low_cpu_mem_usage=True\n",
        "    )\n",
        "    tokenizer = AutoTokenizer.from_pretrained(model_name)\n",
        "\n",
        "    model_pipeline = pipeline(\n",
        "        \"text-generation\",\n",
        "        model=model,\n",
        "        tokenizer=tokenizer,\n",
        "        max_new_tokens=max_new_token,\n",
        "        pad_token_id=tokenizer.eos_token_id,\n",
        "        device_map=\"auto\"\n",
        "    )\n",
        "\n",
        "    llm = HuggingFacePipeline(\n",
        "        pipeline=model_pipeline,\n",
        "    )\n",
        "    return llm\n",
        "\n",
        "LLM = get_huggingface_llm()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 339
        },
        "id": "udh0ZsAPYkm5",
        "outputId": "77358c6e-231c-4691-a201-e2bbeb229f20"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "error",
          "ename": "RuntimeError",
          "evalue": "No GPU found. A GPU is needed for quantization.",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-43-639c9758bffb>\u001b[0m in \u001b[0;36m<cell line: 30>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     28\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mllm\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     29\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 30\u001b[0;31m \u001b[0mLLM\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mget_huggingface_llm\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-43-639c9758bffb>\u001b[0m in \u001b[0;36mget_huggingface_llm\u001b[0;34m(model_name, max_new_token)\u001b[0m\n\u001b[1;32m      7\u001b[0m         \u001b[0mbnb_4bit_compute_dtype\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtorch\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbfloat16\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m     )\n\u001b[0;32m----> 9\u001b[0;31m     model = AutoModelForCausalLM.from_pretrained(\n\u001b[0m\u001b[1;32m     10\u001b[0m         \u001b[0mmodel_name\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m         \u001b[0mquantization_config\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mnf4_config\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/transformers/models/auto/auto_factory.py\u001b[0m in \u001b[0;36mfrom_pretrained\u001b[0;34m(cls, pretrained_model_name_or_path, *model_args, **kwargs)\u001b[0m\n\u001b[1;32m    561\u001b[0m         \u001b[0;32melif\u001b[0m \u001b[0mtype\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mconfig\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mcls\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_model_mapping\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mkeys\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    562\u001b[0m             \u001b[0mmodel_class\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_get_model_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mconfig\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcls\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_model_mapping\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 563\u001b[0;31m             return model_class.from_pretrained(\n\u001b[0m\u001b[1;32m    564\u001b[0m                 \u001b[0mpretrained_model_name_or_path\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0mmodel_args\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconfig\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mconfig\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mhub_kwargs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    565\u001b[0m             )\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/transformers/modeling_utils.py\u001b[0m in \u001b[0;36mfrom_pretrained\u001b[0;34m(cls, pretrained_model_name_or_path, config, cache_dir, ignore_mismatched_sizes, force_download, local_files_only, token, revision, use_safetensors, *model_args, **kwargs)\u001b[0m\n\u001b[1;32m   3200\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3201\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mhf_quantizer\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3202\u001b[0;31m             hf_quantizer.validate_environment(\n\u001b[0m\u001b[1;32m   3203\u001b[0m                 \u001b[0mtorch_dtype\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtorch_dtype\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfrom_tf\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mfrom_tf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfrom_flax\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mfrom_flax\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdevice_map\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdevice_map\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3204\u001b[0m             )\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/transformers/quantizers/quantizer_bnb_4bit.py\u001b[0m in \u001b[0;36mvalidate_environment\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m     60\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mvalidate_environment\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     61\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mtorch\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcuda\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_available\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 62\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mRuntimeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"No GPU found. A GPU is needed for quantization.\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     63\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mis_accelerate_available\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mis_bitsandbytes_available\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     64\u001b[0m             raise ImportError(\n",
            "\u001b[0;31mRuntimeError\u001b[0m: No GPU found. A GPU is needed for quantization."
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "welcome_message = \"\"\" Welcome to the PDF QA! To get started :\n",
        "1. Upload a PDF or text file\n",
        "2. Ask a question about the file\n",
        "\"\"\""
      ],
      "metadata": {
        "id": "s0FIKeshYqQB"
      },
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "@cl.on_chat_start\n",
        "async def on_chat_start():\n",
        "    files = None\n",
        "    while files is None:\n",
        "        files = await cl.AskFileMessage(\n",
        "            content=welcome_message,\n",
        "            accept=[\"text/plain\", \"application/pdf\"],\n",
        "            max_size_mb=20,\n",
        "            timeout=180,\n",
        "        ).send()\n",
        "        file = files[0]\n",
        "\n",
        "        msg = cl.Message(content=f\"Processing '{file.name}'...\",\n",
        "                         disable_feedback=True)\n",
        "        await msg.send()\n",
        "\n",
        "        vector_db = await cl.make_async(get_vector_db)(file)\n",
        "\n",
        "        message_history = ChatMessageHistory()\n",
        "        memory = ConversationBufferMemory(\n",
        "            memory_key=\"chat_history\",\n",
        "            output_key=\"answer\",\n",
        "            chat_memory=message_history,\n",
        "            return_messages=True,\n",
        "        )\n",
        "\n",
        "        retriever = vector_db.as_retriever(search_type=\"mmr\", search_kwargs={'k': 3})\n",
        "\n",
        "        chain = ConversationalRetrievalChain.from_llm(\n",
        "            llm=LLM,\n",
        "            chain_type=\"stuff\",\n",
        "            retriever=retriever,\n",
        "            memory=memory,\n",
        "            return_source_documents=True\n",
        "        )\n",
        "\n",
        "        msg.content = f\"'{file.name}' processed. You can now ask questions!\"\n",
        "        await msg.update()\n",
        "\n",
        "        cl.user_session.set(\"chain\", chain)\n"
      ],
      "metadata": {
        "id": "sejMClcTYsRw"
      },
      "execution_count": 45,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "@cl.on_message\n",
        "async def on_message(message: cl.Message):\n",
        "    chain = cl.user_session.get(\"chain\")\n",
        "    cb = cl.AsyncLangchainCallbackHandler()\n",
        "    res = await chain.ainvoke(message.content, callbacks=[cb])\n",
        "    answer = res[\"answer\"]\n",
        "    source_documents = res[\"source_documents\"]\n",
        "    text_elements = []\n",
        "\n",
        "    if source_documents:\n",
        "        for source_idx, source_doc in enumerate(source_documents):\n",
        "            source_name = f\"source_{source_idx}\"\n",
        "            text_elements.append(\n",
        "                cl.Text(content=source_doc.page_content,\n",
        "                        name=source_name)\n",
        "            )\n",
        "        source_names = [text_el.name for text_el in text_elements]\n",
        "\n",
        "        if source_names:\n",
        "            answer += f\"\\nSources: {', '.join(source_names)}\"\n",
        "        else:\n",
        "            answer += \"\\nNo sources found\"\n",
        "\n",
        "    await cl.Message(content=answer, elements=text_elements).send()\n"
      ],
      "metadata": {
        "id": "Q04oOFxNYzo1"
      },
      "execution_count": 46,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!chainlit run app.py --host 0.0.0.0 --port 8000 /content/logs.txt"
      ],
      "metadata": {
        "id": "ptBqnJxHClcU"
      },
      "execution_count": 47,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import urllib\n",
        "print(\"Password/Enpoint IP for localtunnel is:\", urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip(\"\\n\"))\n",
        "!lt --port 8000 --subdomain aivn-simple-rag\n"
      ],
      "metadata": {
        "id": "1eqq0Ih-a2p7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5e5e6b17-d959-466b-8aa3-4c83e18b6352"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Password/Enpoint IP for localtunnel is: 34.106.9.192\n",
            "your url is: https://aivn-simple-rag.loca.lt\n",
            "^C\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Using Ngrok"
      ],
      "metadata": {
        "id": "fDadsO714AYC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "\n",
        "import chainlit as cl\n",
        "import torch\n",
        "from chainlit.types import AskFileResponse\n",
        "from transformers import BitsAndBytesConfig\n",
        "from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline\n",
        "from langchain_huggingface.llms import HuggingFacePipeline\n",
        "from langchain.memory import ConversationBufferMemory\n",
        "from langchain_community.chat_message_histories import ChatMessageHistory\n",
        "from langchain.chains import ConversationalRetrievalChain\n",
        "from langchain_huggingface import HuggingFaceEmbeddings\n",
        "from langchain_chroma import Chroma\n",
        "from langchain_community.document_loaders import PyPDFLoader, TextLoader\n",
        "from langchain_text_splitters import RecursiveCharacterTextSplitter\n",
        "from langchain_core.runnables import RunnablePassthrough\n",
        "from langchain_core.output_parsers import StrOutputParser\n",
        "from langchain import hub\n",
        "\n",
        "\n",
        "text_splitter = RecursiveCharacterTextSplitter(chunk_size =1000, chunk_overlap =100)\n",
        "embedding = HuggingFaceEmbeddings()\n",
        "\n",
        "\n",
        "def process_file(file: AskFileResponse):\n",
        "  if file.type == \"text/plain\":\n",
        "    Loader = TextLoader\n",
        "  elif file.type == \"application/pdf\":\n",
        "    Loader = PyPDFLoader\n",
        "\n",
        "  loader = Loader(file.path)\n",
        "  documents = loader.load()\n",
        "  docs = text_splitter.split_documents(documents)\n",
        "  for i, doc in enumerate(docs):\n",
        "    doc.metadata[\"source\"] = f\"source_ {i}\"\n",
        "  return docs\n",
        "\n",
        "\n",
        "def get_vector_db(file: AskFileResponse):\n",
        "  docs = process_file(file)\n",
        "  cl.user_session.set(\"docs\",docs)\n",
        "  vector_db = Chroma.from_documents ( documents =docs, embedding = embedding)\n",
        "  return vector_db\n",
        "\n",
        "\n",
        "def get_huggingface_llm(model_name: str = \"lmsys/vicuna-7b-v1.5\",\n",
        "                        max_new_token: int = 512):\n",
        "    nf4_config = BitsAndBytesConfig(\n",
        "        load_in_4bit=True,\n",
        "        bnb_4bit_quant_type=\"nf4\",\n",
        "        bnb_4bit_use_double_quant=True,\n",
        "        bnb_4bit_compute_dtype=torch.bfloat16\n",
        "    )\n",
        "    model = AutoModelForCausalLM.from_pretrained(\n",
        "        model_name,\n",
        "        quantization_config=nf4_config,\n",
        "        low_cpu_mem_usage=True\n",
        "    )\n",
        "    tokenizer = AutoTokenizer.from_pretrained(model_name)\n",
        "\n",
        "    model_pipeline = pipeline(\n",
        "        \"text-generation\",\n",
        "        model=model,\n",
        "        tokenizer=tokenizer,\n",
        "        max_new_tokens=max_new_token,\n",
        "        pad_token_id=tokenizer.eos_token_id,\n",
        "        device_map=\"auto\"\n",
        "    )\n",
        "\n",
        "    llm = HuggingFacePipeline(\n",
        "        pipeline=model_pipeline,\n",
        "    )\n",
        "    return llm\n",
        "\n",
        "\n",
        "LLM = get_huggingface_llm()\n",
        "\n",
        "welcome_message = \"\"\" Welcome to the PDF QA! To get started :\n",
        "1. Upload a PDF or text file\n",
        "2. Ask a question about the file\n",
        "\"\"\"\n",
        "\n",
        "\n",
        "@cl.on_chat_start\n",
        "async def on_chat_start():\n",
        "    files = None\n",
        "    while files is None:\n",
        "        files = await cl.AskFileMessage(\n",
        "            content=welcome_message,\n",
        "            accept=[\"text/plain\", \"application/pdf\"],\n",
        "            max_size_mb=20,\n",
        "            timeout=180,\n",
        "        ).send()\n",
        "\n",
        "    file = files[0]\n",
        "\n",
        "    msg = cl.Message(content=f\"Processing '{file.name}'...\",\n",
        "                         disable_feedback=True)\n",
        "    await msg.send()\n",
        "\n",
        "    vector_db = await cl.make_async(get_vector_db)(file)\n",
        "\n",
        "    message_history = ChatMessageHistory()\n",
        "    memory = ConversationBufferMemory(\n",
        "        memory_key=\"chat_history\",\n",
        "        output_key=\"answer\",\n",
        "        chat_memory=message_history,\n",
        "        return_messages=True,\n",
        "        )\n",
        "\n",
        "    retriever = vector_db.as_retriever(search_type=\"mmr\", search_kwargs={'k': 3})\n",
        "\n",
        "    chain = ConversationalRetrievalChain.from_llm(\n",
        "        llm=LLM,\n",
        "        chain_type=\"stuff\",\n",
        "        retriever=retriever,\n",
        "        memory=memory,\n",
        "        return_source_documents=True\n",
        "        )\n",
        "\n",
        "    msg.content = f\"'{file.name}' processed. You can now ask questions!\"\n",
        "    await msg.update()\n",
        "\n",
        "    cl.user_session.set(\"chain\", chain)\n",
        "\n",
        "\n",
        "@cl.on_message\n",
        "async def on_message(message: cl.Message):\n",
        "    chain = cl.user_session.get(\"chain\")\n",
        "    cb = cl.AsyncLangchainCallbackHandler()\n",
        "    res = await chain.ainvoke(message.content, callbacks=[cb])\n",
        "    answer = res[\"answer\"]\n",
        "    source_documents = res[\"source_documents\"]\n",
        "    text_elements = []\n",
        "\n",
        "    if source_documents:\n",
        "        for source_idx, source_doc in enumerate(source_documents):\n",
        "            source_name = f\"source_{source_idx}\"\n",
        "            text_elements.append(\n",
        "                cl.Text(content=source_doc.page_content,\n",
        "                        name=source_name)\n",
        "            )\n",
        "        source_names = [text_el.name for text_el in text_elements]\n",
        "\n",
        "        if source_names:\n",
        "            answer += f\"\\nSources: {', '.join(source_names)}\"\n",
        "        else:\n",
        "            answer += \"\\nNo sources found\"\n",
        "\n",
        "    await cl.Message(content=answer, elements=text_elements).send()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dQmswX9X1k2x",
        "outputId": "88381064-be64-4122-d8e5-becfbdedc9c6"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install pyngrok -q\n",
        "from pyngrok import ngrok"
      ],
      "metadata": {
        "id": "fbd0VrIh51Mo"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!ngrok config add-authtoken 2ieNAkipb3WCW2JHDbjkqen4bte_3QwRAfiu9QeKVJaDpYtvH\n",
        "public_url = ngrok.connect(8501)\n",
        "print(public_url)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bbMvIKGw4F55",
        "outputId": "141a6686-0297-42d7-d3b9-881c8d4fdb19"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Authtoken saved to configuration file: /root/.config/ngrok/ngrok.yml\n",
            "NgrokTunnel: \"https://b0e4-34-106-9-192.ngrok-free.app\" -> \"http://localhost:8000\"\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ngrok.kill()"
      ],
      "metadata": {
        "id": "_tgOHoWZ-yXo"
      },
      "execution_count": 38,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!chainlit run app.py"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Td7Eof8t4dwQ",
        "outputId": "f4f6e071-b49b-4c9d-f3e0-64dc5867bba3"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2024-07-02 01:01:52.894438: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:9261] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered\n",
            "2024-07-02 01:01:52.894510: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:607] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered\n",
            "2024-07-02 01:01:52.896696: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1515] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered\n",
            "2024-07-02 01:01:52.908293: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.\n",
            "To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.\n",
            "2024-07-02 01:01:54.549046: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT\n",
            "2024-07-02 01:02:00 - Use pytorch device_name: cpu\n",
            "2024-07-02 01:02:00 - Load pretrained SentenceTransformer: sentence-transformers/all-mpnet-base-v2\n",
            "/usr/local/lib/python3.10/dist-packages/huggingface_hub/file_download.py:1132: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.\n",
            "  warnings.warn(\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/bin/chainlit\", line 8, in <module>\n",
            "    sys.exit(cli())\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/click/core.py\", line 1157, in __call__\n",
            "    return self.main(*args, **kwargs)\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/click/core.py\", line 1078, in main\n",
            "    rv = self.invoke(ctx)\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/click/core.py\", line 1688, in invoke\n",
            "    return _process_result(sub_ctx.command.invoke(sub_ctx))\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/click/core.py\", line 1434, in invoke\n",
            "    return ctx.invoke(self.callback, **ctx.params)\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/click/core.py\", line 783, in invoke\n",
            "    return __callback(*args, **kwargs)\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/chainlit/cli/__init__.py\", line 201, in chainlit_run\n",
            "    run_chainlit(target)\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/chainlit/cli/__init__.py\", line 66, in run_chainlit\n",
            "    load_module(config.run.module_name)\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/chainlit/config.py\", line 416, in load_module\n",
            "    spec.loader.exec_module(module)\n",
            "  File \"<frozen importlib._bootstrap_external>\", line 883, in exec_module\n",
            "  File \"<frozen importlib._bootstrap>\", line 241, in _call_with_frames_removed\n",
            "  File \"/content/app.py\", line 75, in <module>\n",
            "    LLM = get_huggingface_llm()\n",
            "  File \"/content/app.py\", line 53, in get_huggingface_llm\n",
            "    model = AutoModelForCausalLM.from_pretrained(\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/transformers/models/auto/auto_factory.py\", line 563, in from_pretrained\n",
            "    return model_class.from_pretrained(\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/transformers/modeling_utils.py\", line 3202, in from_pretrained\n",
            "    hf_quantizer.validate_environment(\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/transformers/quantizers/quantizer_bnb_4bit.py\", line 62, in validate_environment\n",
            "    raise RuntimeError(\"No GPU found. A GPU is needed for quantization.\")\n",
            "RuntimeError: No GPU found. A GPU is needed for quantization.\n"
          ]
        }
      ]
    }
  ]
}