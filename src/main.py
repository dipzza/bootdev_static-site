import os
import shutil

from markdown_parsers import extract_title
from markdown_to_html_node import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  for element in os.listdir(dir_path_content):
    src_path = os.path.join(dir_path_content, element)
    dest_path = os.path.join(dest_dir_path, element)
    if os.path.isfile(src_path):
      name, _ = os.path.splitext(dest_path)
      generate_page(src_path, template_path, name + ".html")

    if os.path.isdir(src_path):
      generate_pages_recursive(src_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  markdown = open(from_path).read()
  template = open(template_path).read()
  html = markdown_to_html_node(markdown).to_html()
  title = extract_title(markdown)
  final_page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

  os.makedirs(os.path.dirname(dest_path), exist_ok=True)

  with open(dest_path, 'w') as file:
    file.write(final_page)


def copy_dir(source, destination):
  if os.path.exists(destination):
    shutil.rmtree(destination)

  os.mkdir(destination)

  for element in os.listdir(source):
    src_path = os.path.join(source, element)
    dest_path = os.path.join(destination, element)
    print(src_path, dest_path)
    if os.path.isfile(src_path):
      shutil.copy(src_path, dest_path)

    if os.path.isdir(src_path):
      copy_dir(src_path, dest_path)

def main():
  copy_dir("./static", "./public")
  generate_pages_recursive("./content/", "./template.html", "./public/")

main()