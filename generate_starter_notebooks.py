"""
Simple notebook processor to generate starter notebooks from solution notebooks.

This script:
1. Recursively finds .ipynb files in 'solution' folders
2. Creates corresponding 'starter' folders
3. Copies notebooks with 'Solutions' replaced by 'Starter' in the filename
4. Replaces solution code blocks with placeholders
"""

import os
import json
import re
from pathlib import Path


def process_cell_content(content):
    """
    Replace solution blocks with placeholders in cell content.
    
    Handles both:
    - --- BEGIN SOLUTION / --- END SOLUTION (replaced with -- YOUR CODE HERE)
    - ### BEGIN SOLUTION / ### END SOLUTION (replaced with ### YOUR CODE HERE)
    """
    # Handle triple-dash markers (---)
    pattern_triple = r'--- BEGIN SOLUTION.*?--- END SOLUTION'
    content = re.sub(pattern_triple, '-- YOUR CODE HERE', content, flags=re.DOTALL)
    
    # Handle triple-hash markers (###)
    pattern_triple_hash = r'### BEGIN SOLUTION.*?### END SOLUTION'
    content = re.sub(pattern_triple_hash, '### YOUR CODE HERE', content, flags=re.DOTALL)
    
    return content


def process_notebook(notebook_data):
    """
    Process a notebook JSON object, replacing solution blocks in all cells.
    """
    if 'cells' in notebook_data:
        for cell in notebook_data['cells']:
            if 'source' in cell:
                if isinstance(cell['source'], list):
                    # Join lines, process, then split back
                    content = ''.join(cell['source'])
                    processed = process_cell_content(content)
                    # Split back into lines, preserving original line structure
                    cell['source'] = [processed]
                elif isinstance(cell['source'], str):
                    cell['source'] = process_cell_content(cell['source'])
    
    return notebook_data


def find_solution_notebooks(root_dir):
    """
    Recursively find all .ipynb files in folders named 'solution'.
    
    Returns a list of Path objects.
    """
    root_path = Path(root_dir)
    solution_notebooks = []
    
    for solution_dir in root_path.rglob('solution'):
        if solution_dir.is_dir():
            for notebook in solution_dir.glob('*.ipynb'):
                solution_notebooks.append(notebook)
    
    return solution_notebooks


def generate_starter_notebook(solution_notebook_path):
    """
    Generate a starter notebook from a solution notebook.
    
    Args:
        solution_notebook_path: Path object pointing to the solution notebook
    """
    # Read the solution notebook
    with open(solution_notebook_path, 'r', encoding='utf-8') as f:
        notebook_data = json.load(f)
    
    # Process the notebook (replace solution blocks)
    processed_notebook = process_notebook(notebook_data)
    
    # Determine output path
    solution_dir = solution_notebook_path.parent
    parent_dir = solution_dir.parent
    starter_dir = parent_dir / 'starter'
    
    # Create starter directory if it doesn't exist
    starter_dir.mkdir(exist_ok=True)
    
    # Generate new filename (replace 'Solutions' with 'Starter')
    original_name = solution_notebook_path.name
    new_name = original_name.replace('Solutions', 'Starter').replace('SOLUTIONS', 'STARTER')
    
    # If no 'Solutions' in name, replace 'Solution' with 'Starter'
    if new_name == original_name:
        new_name = original_name.replace('Solution', 'Starter').replace('SOLUTION', 'STARTER')
    
    # If still no change, just add 'Starter' before the extension
    if new_name == original_name:
        name_parts = original_name.rsplit('.', 1)
        new_name = f"{name_parts[0]} Starter.{name_parts[1]}"
    
    output_path = starter_dir / new_name
    
    # Write the processed notebook
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(processed_notebook, f, indent=2, ensure_ascii=False)
    
    return output_path


def main(root_directory='.'):
    """
    Main function to process all solution notebooks in the directory tree.
    
    Args:
        root_directory: Root directory to start searching (default: current directory)
    """
    print(f"Searching for solution notebooks in: {root_directory}")
    
    solution_notebooks = find_solution_notebooks(root_directory)
    
    if not solution_notebooks:
        print("No solution notebooks found.")
        return
    
    print(f"\nFound {len(solution_notebooks)} solution notebook(s):\n")
    
    for notebook_path in solution_notebooks:
        print(f"Processing: {notebook_path}")
        try:
            output_path = generate_starter_notebook(notebook_path)
            print(f"  → Created: {output_path}\n")
        except Exception as e:
            print(f"  ✗ Error: {e}\n")
    
    print("Done!")


if __name__ == '__main__':
    import sys
    
    # Allow passing root directory as command line argument
    root_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    main(root_dir)
