import json
import logging

from processor import read_file
from cleaner import clean_text

logging.basicConfig(
    filename="../log/app.log",
    level=logging.INFO
    )
logger=logging.getLogger(__name__)

logger.info("starting Document processing")
file_path="../input/sample.txt"

try:
    raw_text=read_file(file_path)
    logger.info("Docunent read succesfully")
    cleaned_text=clean_text(raw_text)
    logger.info("Document cleaned successfully")

    document={
        "File_name":"sample.txt",
        "content":cleaned_text,
        "character_count":len(cleaned_text)
        }

    with open("../output/processed.json","w",encoding="utf-8") as file:
        json.dump(document,file,indent=4)
    
    print("Document processed successfully")    
    logger.info("Document processed successfull--")
except FileNotFoundError:
    logger.error("File not found: %s",file_path)
    print ("input file does not exist")
