from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

doc_path = "./data/info_artificial.pdf"
model = "llama3.2"

# local PDF file uploads
if doc_path:
    loaders = UnstructuredPDFLoader(file_path = doc_path)
    data = loaders.load()
    print("done loading....")

else:
    print("Uplaod a PDF file")

    # preview first page
content = data[0].page_content
# print(content[:100])

#========= chunking -----------

from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import chroma

# split and chunk
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1200, chunk_overlap = 300)
chunks = text_splitter.split_documents(data)
print("done splitting.....")
