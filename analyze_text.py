import logging
import requests
# Configure logging - change level to DEBUG and re-run, to ERROR and rerun 
logging.basicConfig(
  filename='text_analysis.log', 
  level=logging.INFO, 
  filemode='w', 
  format='%(name)s.%(levelname)s.%(message)s'
)

# Get a configured logger instance and name it logger
logger = logging.getLogger()


# Set url
url = 'https://www.gutenberg.org/ebooks/1112.txt.utf-8'
logger.debug(f"Requesting URL: {url}") 

# Request response object
response = requests.get(url)
logger.debug(f"Response object: {response}")

if response.status_code == 200:
    text = response.text.lower()
    logger.info("Fetched text successfully.")
else:
    logger.error(f"Failed to fetch text. Status code: {response.status_code}")
    text = ""


# Processing text data
words = text.split()
unique_words = set(words)
logger.info(f"Unique words count: {len(unique_words)}")


# Writing unique words to a file
with open('unique_words.txt', 'w') as file:
    for word in unique_words:
        file.write(word + '\n')

logger.info("Unique words written to unique_words.txt")



# Splitting text by newline into a list of lines
lines = text.split('\n')

# Count total lines
logger.info(f"Total number of lines: {len(lines)}")

longest_line = max(lines, key=len)
logger.info(f"Longest line: {longest_line}")

shortest_line = min(lines, key=len)
logger.info(f"Shortest line: {shortest_line}")

# reverse the lines
reversed_lines = lines[::-1]
logger.info(f"First 5 lines in reverse order: {reversed_lines[:5]}")