#!/bin/bash

generate_random() {
    random_num=$((RANDOM % 10))  
    echo "$random_num"
}

password=()
read -p "Enter length of password: " len

for ((i = 0; i < len; i++))
do
    a=$(generate_random)
    password+=("$a") 
done

echo "Password: ${password[@]}"



