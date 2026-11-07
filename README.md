A simple Python script that scrapes news articles from the Telangana section of TV9 Telugu. For each article it saves the headline and paragraphs as a text file, and the main photo as a JPG image.

How it works

Opens the Telangana news page and collects all links starting with https://tv9telugu.com/telangana/.

Opens each article and reads its 'h1' and 'p' tags.

Cleans the headline by removing characters not allowed in file names and cutting it to 80 characters.

Writes the text to a .txt file with UTF-8 encoding.

Downloads the image with id="main-img" and saves it as a .jpg file with the same name.
