# LLAMA-PARSE 
 - gen-ai based document parsing platform 
 - can be accessed in two ways : llama-parse cloud, llama-parse api
 - free tier : 1000 pages / day or 7000 credits per week
 - main goal : to parse and clean the data, ensuring that it's good quality before passing to any downstream LLM use case such as advanced RAG.


# FEATURES 

 - state of art table extraction
 - provide natural language instructions to parse the output in the exact format you want it.
 - JSON mode
 - image extraction
 - support for 10+ file types (.pdf, .pptx, .docx, .html, .xml, and more)
 - foreign language support


# PARSE SETTINGS

- MODE:
  - fast : best for text-only pdfs. skips ocr, image extraction, table/heading identification

  - accurate : ideal for complex documents with images. performs ocr, image extraaction, table/heading identification. default mode in api

  - premium : ideal for complex documents with images. performs ocr, image extraaction, table/heading identification. output equations in latex format and images in mermaid format.

  - 3rd-party muti-modal : transforms (pdf page to image ) for every page, and uses 3rd party multi modal to convert these individual images to Markdown or JSON. this mode will not give output in raw text.


- PARSING INSTRUCTIONS :
  - we can provide the instructions to the model for document parsing. 
  - instructions are applied per every page


- LANGUAGE FOR OCR FROM IMAGES
  - we can mention the language parameter, to specify which language to use for OCR for processing images inside the document.

- TAKING SCREENSHOTS OF DOCUMENT
  - we can mention whether we have to collect screenshots of every page as JSON data

- SKIP OCR 
  - we can skip the OCR step, for processing the document faster. 

- PAGE SPECIFICATION
 - we can mention which specific pages to be processed / parsed. 
 - by default all the pages will be processed
 - we can mention the page numbers (starting from 0) separated by commas.

- BOUNDING BOX
  - we can mention which specific area of the document page to be parsed / processed. 
  - we can mention this as clock wise values (between 0 and 1 rep. percentages of secion/area ) to be excluded 
  - for example we can exclude the header and footer areas by maintaing the bounding box as : 0.1,0,0.1,0, which ignores/excludes the top 10% and bottom 10% of the document.

- PAGE SEPARATOR
   - we can use the page separator string. by default it is ( --- )

  
- PAGE PREFIX AND SUFFIX 
  - we can mention prefix and suffix for each page 


# OBSERVATIONS
  - tabular data extracted accurated in markdown syntax
  - all the images are being extracted separately
  - proper division of pages
  - using appropriate parsing-mode based on complexity of document data ( plain text, with images, with formulas, with flow diagrams, with tables etc) , helps in reducing cost/credit usage


# SAMPLE USED FOR LLAMA-PARSE CLOUD BASED TESTING 
 - research paper : from paperswithcode 
 - reference link : https://paperswithcode.com/paper/omnigen-unified-image-generation


