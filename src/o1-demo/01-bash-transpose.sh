#!/bin/bash

input_string="$1"
echo "\ninput:\n$input_string"

# Replace '],[' with ']\n[' to separate rows
rows=$(echo "$input_string" | sed 's/],\[/]\n\[/g')
echo "\nrows:\n$rows"

# Read rows into array
IFS=$'\n' read -r -a row_array <<< "$rows"

declare -A matrix
row_count=0
col_count=0

for row in "${row_array[@]}"
do
  # Remove '[' and ']'
  row=${row#\[}
  row=${row%\]}
  # Split row by ','
  IFS=',' read -r -a nums <<< "$row"
  if (( col_count == 0 )); then
    col_count=${#nums[@]}
  fi
  for ((i=0; i<${#nums[@]}; i++))
  do
    matrix[$row_count,$i]=${nums[$i]}
  done
  ((row_count++))
done

# Now transpose the matrix
declare -A transpose

for ((i=0; i<col_count; i++))
do
  for ((j=0; j<row_count; j++))
  do
    transpose[$i,$j]=${matrix[$j,$i]}
  done
done

# Build the output string
output_rows=()

for ((i=0; i<col_count; i++))
do
  row_elements=()
  for ((j=0; j<row_count; j++))
  do
    row_elements+=("${transpose[$i,$j]}")
  done
  # Join row_elements with commas
  row_string=$(IFS=,; echo "${row_elements[*]}")
  # Add brackets
  row_string="[$row_string]"
  output_rows+=("$row_string")
done

# Join output_rows with commas
output_string=$(IFS=,; echo "${output_rows[*]}")

echo "$output_string"
