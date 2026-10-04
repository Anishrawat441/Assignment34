# Assignment 34 -- Text Summarization using Langchain

# PART 1---Basic Text Summarization using PromptTemplate
## 1. Load the document using Langchain document loaders or manual loading.
## 2. Print:
## . Total character
## . Sample content preview

from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('medical_health_data_document.pdf')
documents=loader.load()
text = "\n".join(doc.page_content for doc in documents)

## print total charecters
print("Number of pages:", len(documents))
## print sample content
print(text[:1000])


# Task 2: Prompt