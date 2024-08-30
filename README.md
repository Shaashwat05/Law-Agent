# Law Agent using Adaptive RAG algorithm

The project aims to provide lawyers with a reliable information bot using the robust Adaptive RAG algorithm

## Algorithm 

The focus algorithm of this project is the **Adaptive RAG** Algorithm which has self-corrective, looping, and web searching capabilities. The first step is data collection and indexing - identifying documents pertaining to the Law for the Vector database(**ChromaDB**).
As the user query comes in, the LLM (**OpenAI GPT-4**) decides whether the input requires retrieval from the database or web scraping (**Tavily**). If retrieval, it gets similar documents from the Vector DB and checks for relevancy then hallucinations and finally, if the answer is good enough or not.
If the checks are not met, it rephrases the questions or regenerates the answers.

## Workflow of Adaptive RAG (By Langgraph)

![Project Workflow](https://github.com/Shaashwat05/Law-Agent/blob/main/resources/Adaptive%20RAG.png)

### Prerequisites

A list of dependencies
```
langchain==0.1.16
langchain-community==0.0.34
langchain-core==0.1.46
streamlit==1.33.0
streamlit-extras==0.4.0
weaviate-client==3.26.0
tiktoken==0.5.1
openai==0.28.1
```

## Steps to run

1. Clone the GitHub Repository
```bash
$ git clone https://github.com/Shaashwat05/conversationalAI
```
2. Install all dependencies using pip
```bash
$ pip install requirements.txt
```
3. Cd to the current cloned directory. In the app.py python file, enter a suitable API key for OpenAI models. Run the following command to start the application:
```bash
$ streamlit run app.py
```

## Results

![Model Training](https://github.com/Shaashwat05/Law-Agent/blob/main/resources/example.png)

## File Descriptions

### data_handling - Downloading Images based on traits 

### model_from_directory - loading data and trainingthe model 

### segmenting_data - segmenting the download images for training 

### prediction - prediciting trait value and analyzing the predictions 

### milkweed_clustering - Clustering Milkweed Images 

### plant_trait_EDA - Data Analysis on the complete data 
