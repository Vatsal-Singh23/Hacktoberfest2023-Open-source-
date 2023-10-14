def find_subsets_sum(arr):
    def generate_subsets(index, current_subset):
        if index == len(arr):
            subsets.append(current_subset)
        else:
            # Include the current element in the subset
            generate_subsets(index + 1, current_subset + [arr[index]])
            
            # Exclude the current element from the subset
            generate_subsets(index + 1, current_subset)
    
    subsets = []
    generate_subsets(0, [])
    
    subset_sums = [sum(subset) for subset in subsets]
    
    return subset_sums

# Example usage:
numbers = [1, 2, 3]
subset_sums = find_subsets_sum(numbers)
print("Subset Sums:", subset_sums)
