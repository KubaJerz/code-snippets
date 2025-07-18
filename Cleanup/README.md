# cleanup.sh Documentation

## Overview
Bash script that moves files from experiment run subdirectories to a cleanup archive while preserving important files in their original locations.

## Usage
```bash
./cleanup.sh <experiment_run_directory> [subdirectory_to_ignore...]
```

## What It Does

1. **Creates cleanup archive**: `~/.cleanups/{YYYY-MM-DD}_{experiment_basename}/`
2. **Processes subdirectories**: Moves files except preserved ones
3. **Preserves important files**: Keeps specific files in original locations
4. **Handles duplicates**: Auto-increments directory names if cleanup already exists

## Preserved Files (Configurable)
- `best_dev_metrics.json`
- `metrics.png` 
- `run_param.toml`

## Directory Structure
```
~/.cleanups/
├── 2024-01-15_experiment_run/
├── 2024-01-15_experiment_run_1/    # If run multiple times
└── 2024-01-16_other_experiment/
```

## Configuration
Edit the `PRESERVED_FILES` array at the top of the script:
```bash
PRESERVED_FILES=(
    "best_dev_metrics.json"
    "metrics.png"
    "run_param.toml"
    # Add more files here
)
```


## Requirements
- Bash shell
- Write permissions to `~/.cleanups`
- Read permissions on experiment directory



```
# Basic usage
./cleanup.sh /path/to/experiment_run

# With ignored subdirectories
./cleanup.sh /path/to/experiment_run subdir1 subdir2 subdir3

# Help information
./cleanup.sh --help
```
