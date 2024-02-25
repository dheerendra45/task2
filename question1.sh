#!/bin/bash

dir="."

txt_files=$(find "$dir" -type f -name "*.txt")
mkdir -p modified
for txt_file in $txt_files; do
    base_name=$(basename "$txt_file" .txt)
    mv "$txt_file" "modified/$base_name.bk"
done
this will take current directory as input than search files with .txt extension than convert them into .bk extension

