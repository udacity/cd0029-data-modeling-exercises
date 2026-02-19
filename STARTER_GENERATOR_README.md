# Notebook Starter Generator

A simple Python script to automatically generate starter notebooks from solution notebooks for educational purposes.

## Features

- **Recursive search**: Finds all `.ipynb` files in folders named `solution`
- **Automatic structure**: Creates corresponding `starter` folders as siblings to `solution` folders
- **Smart renaming**: Replaces "Solutions" with "Starter" in filenames
- **Solution removal**: Removes code between solution markers and replaces with placeholders

## Solution Markers

The script handles two types of solution markers:

### Triple-dash markers
```
--- BEGIN SOLUTION
code here
--- END SOLUTION
```
Replaced with: `-- YOUR CODE HERE`

### Triple-hash markers
```
### BEGIN SOLUTION
code here
### END SOLUTION
```
Replaced with: `### YOUR CODE HERE`

## Usage

### Process all notebooks in current directory
```bash
python generate_starter_notebooks.py
```

### Process notebooks in a specific directory
```bash
python generate_starter_notebooks.py /path/to/your/directory
```

## Example

Given this structure:
```
Lesson 1/
  Exercise1/
    solution/
      L1 Exercise 1 Solutions DRAFT.ipynb
```

The script will create:
```
Lesson 1/
  Exercise1/
    solution/
      L1 Exercise 1 Solutions DRAFT.ipynb
    starter/
      L1 Exercise 1 Starter DRAFT.ipynb    ← Generated!
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## How It Works

1. Searches recursively for all `solution` directories
2. For each `.ipynb` file found:
   - Loads the notebook JSON
   - Processes all cells, replacing solution blocks with placeholders
   - Creates the `starter` directory if it doesn't exist
   - Writes the processed notebook with a new name

## Notes

- Original notebooks are never modified (read-only operation)
- `starter` directories are created automatically
- The script preserves all notebook metadata and structure
- Works with standard Jupyter notebook format (.ipynb)
