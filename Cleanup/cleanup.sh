#!/bin/bash

# cleanup.sh - Move files from experiment run subdirectories to cleanup archive
# Usage: ./cleanup.sh /path/to/experiment_run [subdir1] [subdir2] ...

# =============================================================================
# CONFIGURATION - Easily modifiable preservation list
# =============================================================================
PRESERVED_FILES=(
    "best_dev_metrics.json"
    "metrics.png"
    "run_param.toml"
)

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

# Print usage information
usage() {
    echo "Usage: $0 <experiment_run_directory> [subdirectory_to_ignore...]"
    echo ""
    echo "Moves files from experiment run subdirectories to cleanup archive"
    echo "while preserving important files in their original locations."
    echo ""
    echo "Arguments:"
    echo "  experiment_run_directory  Path to the experiment run directory"
    echo "  subdirectory_to_ignore    Names of subdirectories to skip (optional)"
    echo ""
    echo "Preserved files (configurable at top of script):"
    for file in "${PRESERVED_FILES[@]}"; do
        echo "  - $file"
    done
    echo ""
    echo "Example:"
    echo "  $0 /path/to/experiment_run subdir1 subdir2"
}

# Print error message and exit
error_exit() {
    echo "ERROR: $1" >&2
    exit 1
}

# Print info message
info() {
    echo "INFO: $1"
}

# Check if file should be preserved
is_preserved_file() {
    local filename="$1"
    for preserved in "${PRESERVED_FILES[@]}"; do
        if [[ "$filename" == "$preserved" ]]; then
            return 0
        fi
    done
    return 1
}

# Create directory with error handling
create_directory() {
    local dir="$1"
    if ! mkdir -p "$dir" 2>/dev/null; then
        error_exit "Failed to create directory: $dir"
    fi
}

# =============================================================================
# MAIN SCRIPT
# =============================================================================

# Check for help flag
if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    usage
    exit 0
fi

# Validate arguments
if [[ $# -lt 1 ]]; then
    echo "ERROR: Missing required argument" >&2
    echo ""
    usage
    exit 1
fi

EXPERIMENT_RUN_DIR="$1"
shift
IGNORE_SUBDIRS=("$@")

# Validate experiment run directory exists
if [[ ! -d "$EXPERIMENT_RUN_DIR" ]]; then
    error_exit "Experiment run directory does not exist: $EXPERIMENT_RUN_DIR"
fi

# Convert to absolute path for safety
EXPERIMENT_RUN_DIR="$(cd "$EXPERIMENT_RUN_DIR" && pwd)" || error_exit "Failed to resolve absolute path for experiment run directory"

# =============================================================================
# SETUP PHASE
# =============================================================================

info "Starting cleanup process..."
info "Experiment run directory: $EXPERIMENT_RUN_DIR"
info "Ignored subdirectories: ${IGNORE_SUBDIRS[*]:-none}"

# Create ~/.cleanups directory
CLEANUPS_DIR="$HOME/.cleanups"
create_directory "$CLEANUPS_DIR"

# Generate target directory name
CURRENT_DATE=$(date +%Y-%m-%d)
EXPERIMENT_BASENAME=$(basename "$EXPERIMENT_RUN_DIR")
BASE_TARGET_NAME="${CURRENT_DATE}_${EXPERIMENT_BASENAME}"
TARGET_DIR="$CLEANUPS_DIR/$BASE_TARGET_NAME"

# Handle existing directories - add suffix if needed
counter=0
while [[ -d "$TARGET_DIR" ]]; do
    info "Directory already exists: $TARGET_DIR"
    TARGET_DIR="$CLEANUPS_DIR/${BASE_TARGET_NAME}_${counter}"
    ((counter++))
done

# Create target directory
create_directory "$TARGET_DIR"
info "Created cleanup target directory: $TARGET_DIR"

# =============================================================================
# PROCESSING PHASE
# =============================================================================

# Initialize counters
PROCESSED_SUBDIRS=0
MOVED_FILES=0
PRESERVED_FILES_COUNT=0

# Process each subdirectory
for subdir in "$EXPERIMENT_RUN_DIR"/*; do
    # Skip if not a directory
    if [[ ! -d "$subdir" ]]; then
        continue
    fi
    
    subdir_name=$(basename "$subdir")
    
    # Check if subdirectory should be ignored
    skip_subdir=false
    for ignore in "${IGNORE_SUBDIRS[@]}"; do
        if [[ "$subdir_name" == "$ignore" ]]; then
            info "Skipping ignored subdirectory: $subdir_name"
            skip_subdir=true
            break
        fi
    done
    
    if [[ "$skip_subdir" == true ]]; then
        continue
    fi
    
    info "Processing subdirectory: $subdir_name"
    
    # Create corresponding subdirectory in target
    target_subdir="$TARGET_DIR/$subdir_name"
    create_directory "$target_subdir"
    
    # Process files in subdirectory
    subdir_moved=0
    subdir_preserved=0
    
    # Use find to handle files with spaces properly
    while IFS= read -r -d '' file; do
        filename=$(basename "$file")
        
        if is_preserved_file "$filename"; then
            info "  Preserving: $filename"
            ((subdir_preserved++))
            ((PRESERVED_FILES_COUNT++))
        else
            # Move file to target directory
            if mv "$file" "$target_subdir/" 2>/dev/null; then
                info "  Moved: $filename"
                ((subdir_moved++))
                ((MOVED_FILES++))
            else
                echo "WARNING: Failed to move file: $file" >&2
            fi
        fi
    done < <(find "$subdir" -maxdepth 1 -type f -print0)
    
    # Handle subdirectories within subdirectories
    while IFS= read -r -d '' nested_dir; do
        nested_name=$(basename "$nested_dir")
        target_nested="$target_subdir/$nested_name"
        
        if mv "$nested_dir" "$target_nested" 2>/dev/null; then
            info "  Moved directory: $nested_name"
            ((subdir_moved++))
        else
            echo "WARNING: Failed to move directory: $nested_dir" >&2
        fi
    done < <(find "$subdir" -maxdepth 1 -type d -not -path "$subdir" -print0)
    
    if [[ $subdir_moved -gt 0 || $subdir_preserved -gt 0 ]]; then
        info "  Completed $subdir_name: $subdir_moved moved, $subdir_preserved preserved"
        ((PROCESSED_SUBDIRS++))
    else
        info "  No files found in $subdir_name"
        # Remove empty target subdirectory
        rmdir "$target_subdir" 2>/dev/null
    fi
done

# =============================================================================
# SUMMARY
# =============================================================================

info "Cleanup completed successfully!"
info "Summary:"
info "  - Processed subdirectories: $PROCESSED_SUBDIRS"
info "  - Files moved to cleanup: $MOVED_FILES"
info "  - Files preserved in place: $PRESERVED_FILES_COUNT"
info "  - Cleanup archive location: $TARGET_DIR"

# Remove target directory if empty
if [[ $MOVED_FILES -eq 0 ]]; then
    if rmdir "$TARGET_DIR" 2>/dev/null; then
        info "Removed empty cleanup directory"
    fi
fi

exit 0
