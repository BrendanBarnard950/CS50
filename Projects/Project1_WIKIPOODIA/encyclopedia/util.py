import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    I had to edit this because my line breaks were duplicating. I don't know why.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content.encode('ascii')))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.line.replace("**", "<b>", 1)
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


def markdown_to_html(content):
    """
    This is gonna convert my Markdown to nice HTML. Hopefully.
    """
    bolds=True
    listing = False
    paragraphing = False
    heading = False
    heading2 = False
    content = content.split("\r\n")
    listinc = 0
    final = ""
    for line in content:
        heading = False
        if line.find("##") != -1:
            line = line.replace("## ", "<h4>")
            heading2 = True
        elif line.find("#") == 0:
            line = line.replace("# ", "<h3>")
            heading = True
        
        while bolds:         
            if line.find("**") != -1:
                line = line.replace("**", "<b>", 1)
                line = line.replace("**", "</b>", 1)
            else:
                bolds=False
        bolds=True
        
        linkcount = line.count("[")
        i = 0
        for i in range(linkcount):
            if line.find("(") != -1 and line.find(")") != -1 and line.find("[") != -1 and line.find("]") != -1:
                start = line.find("(") +1
                end = line.find(")")
                link = ""
                word = ""
                while start < end:
                    link += line[start]
                    start +=1
                start = line.find("[") +1
                end = line.find("]")
                while start < end:
                    word += line[start]
                    start +=1
                print(word)
                line = line.replace(("[" + word + "](" + link + ")"), '<a href="' + link + '">' + word + "</a>")
        i += 1
            
        if line.find("*") != -1:
            listinc += 1
            if listing == False:
                line = "<ul>" + line
                line = line.replace("*", "<li>",1)
                line += "</li>"
                listing = True
            else:
                line = line.replace("*", "<li>",1)
                line += "</li>"
        elif listing == True and line.find("*") == -1:
            line += "</ul>"
            listing = False 
            
        if heading:
            final += line + "</h3>"
        elif heading2:
            final += line + "</h4>"
        elif listing:
            final += line
        elif line == "" and paragraphing == False:
            final += "<p>" + line
            paragraphing = True
        elif line == "" and paragraphing == True:
            final += line + "</p>"
        elif listinc != 0:
            final += line
            listinc = 0
        else:
            final += line + "<br>"
    if paragraphing == True:
        final += "</p>"   
            
    return final