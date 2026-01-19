# Pokemon Selection Sort - Core Algorithm Logic
import ui
import time

# Dataset
pokemon_db = [
    {"name": "Greninja",    "stage": "Stage 2",       "gen": 6, "hp": 72,  "type": "Water Dark"},
    {"name": "Bulbasaur",   "stage": "Basic",         "gen": 1, "hp": 45,  "type": "Grass Poison"},
    {"name": "Lucario",     "stage": "Stage 1",       "gen": 4, "hp": 70,  "type": "Fighting Steel"},
    {"name": "Pikachu",     "stage": "Stage 1",       "gen": 1, "hp": 35,  "type": "Electric"},
    {"name": "Gardevoir",   "stage": "Stage 2",       "gen": 3, "hp": 68,  "type": "Psychic Fairy"},
    {"name": "Charmander",  "stage": "Basic",         "gen": 1, "hp": 39,  "type": "Fire"},
    {"name": "Froakie",     "stage": "Basic",         "gen": 6, "hp": 41,  "type": "Water"},
    {"name": "Ivysaur",     "stage": "Stage 1",       "gen": 1, "hp": 60,  "type": "Grass Poison"},
    {"name": "Zoroark",     "stage": "Stage 1",       "gen": 5, "hp": 60,  "type": "Dark"},
    {"name": "Charizard",   "stage": "Stage 2",       "gen": 1, "hp": 78,  "type": "Fire Flying"},
    {"name": "Riolu",       "stage": "Basic",         "gen": 4, "hp": 40,  "type": "Fighting"},
    {"name": "Empoleon",    "stage": "Stage 2",       "gen": 4, "hp": 84,  "type": "Water Steel"},
    {"name": "Frogadier",   "stage": "Stage 1",       "gen": 6, "hp": 54,  "type": "Water"},
    {"name": "Blaziken",    "stage": "Stage 2",       "gen": 3, "hp": 80,  "type": "Fire Fighting"},
    {"name": "Eevee",       "stage": "Basic",         "gen": 1, "hp": 55,  "type": "Normal"},
    {"name": "Sylveon",     "stage": "Stage 1",       "gen": 6, "hp": 95,  "type": "Fairy"},
    {"name": "Tyranitar",   "stage": "Stage 2",       "gen": 2, "hp": 100, "type": "Rock Dark"},
    {"name": "Abra",        "stage": "Basic",         "gen": 1, "hp": 25,  "type": "Psychic"}
]
# Helper Functions for Key Extraction
def get_stage_value(pokemon):
    """Converts stage string to integer for comparison"""
    stage = pokemon["stage"]
    if "Basic" in stage: return 1
    if "Stage 1" in stage: return 2
    if "Stage 2" in stage: return 3
    return 4

def get_type_value(pokemon):
    """Handles dual types by using the first type"""
    order = [
        "Normal", "Fire", "Water", "Electric", "Grass", "Ice", 
        "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", 
        "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"
    ]
    
    primary_type = pokemon["type"].split()[0]
    
    if primary_type in order:
        return order.index(primary_type)
    else:
        return 99

# Selection Sort Algorithm
def selection_sort(data, key_extractor, visualize=False):
    """
    Sorts list 'data' in-place using Selection Sort.
    
    Args:
        data: List to sort
        key_extractor: Function that returns the value to compare
        visualize: If True, shows step-by-step visualization
    
    Returns:
        dict: Statistics with 'comparisons' and 'swaps' counts
    """
    n = len(data)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        min_idx = i
        
        stats = {'comparisons': comparisons, 'swaps': swaps}
        
        if visualize:
            ui.clear_screen()
            ui.show_header()
            ui.display_sort_step(
                data, i, min_idx, None,
                f"Pass {i + 1}/{n}: Finding minimum in unsorted portion...",
                stats
            )
            ui.pause()
        
        # Find minimum in unsorted portion
        for j in range(i + 1, n):
            comparisons += 1
            stats = {'comparisons': comparisons, 'swaps': swaps}
            
            if visualize:
                ui.clear_screen()
                ui.show_header()
                ui.display_sort_step(
                    data, i, min_idx, j,
                    f"Pass {i + 1}/{n}: Comparing {data[j]['name']} with current min {data[min_idx]['name']}",
                    stats
                )
                ui.pause()
            
            # Compare using the value returned by key_extractor
            if key_extractor(data[j]) < key_extractor(data[min_idx]):
                min_idx = j
                
                if visualize:
                    ui.clear_screen()
                    ui.show_header()
                    ui.display_sort_step(
                        data, i, min_idx, j,
                        f"Pass {i + 1}/{n}: New minimum found: {data[min_idx]['name']}",
                        stats
                    )
                    ui.pause()
        
        # Swap if needed
        if min_idx != i:
            swaps += 1
            stats = {'comparisons': comparisons, 'swaps': swaps}
            
            if visualize:
                ui.clear_screen()
                ui.show_header()
                ui.display_swap_message(data, i, min_idx)
                ui.display_sort_step(
                    data, i, min_idx, None,
                    f"Pass {i + 1}/{n}: Swapping to place minimum in sorted position",
                    stats
                )
                ui.pause()
            
            data[i], data[min_idx] = data[min_idx], data[i]
        
        if visualize and i < n - 1:
            ui.display_pass_summary(i, n, stats)
    
    # Return final statistics
    stats = {'comparisons': comparisons, 'swaps': swaps}
    
    if visualize:
        ui.display_completion_message(stats)
        ui.pause()
    
    return stats

# Main Application Logic
def run_sort(data, key_extractor, title, show_process=False):
    """Execute sorting and display results with statistics"""
    ui.clear_screen()
    ui.show_header()
    
    # Start timing
    start_time = time.time()
    
    if show_process:
        stats = selection_sort(data, key_extractor, visualize=True)
        ui.clear_screen()
        ui.show_header()
    else:
        stats = selection_sort(data, key_extractor, visualize=False)
    
    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Add elapsed time to stats
    stats['time'] = elapsed_time
    
    ui.display_pokemon_table(data, title)
    ui.display_statistics(stats)
    ui.pause()

def main():
    """Main application loop"""
    while True:
        ui.clear_screen()
        ui.show_header()
        choice = ui.show_menu()
        
        # Create a copy to preserve original order
        current_list = pokemon_db[:]
        
        if choice == '1':
            ui.clear_screen()
            ui.show_header()
            ui.display_pokemon_table(pokemon_db, "Original List")
            ui.pause()
            
        elif choice == '2':
            show_viz = ui.Prompt.ask(
                "Show step-by-step visualization?", 
                choices=["y", "n"], 
                default="y"
            )
            run_sort(current_list, get_stage_value, "Sorted by Evolution Stage", show_viz == "y")
            
        elif choice == '3':
            show_viz = ui.Prompt.ask(
                "Show step-by-step visualization?", 
                choices=["y", "n"], 
                default="y"
            )
            run_sort(current_list, lambda x: x['gen'], "Sorted by Generation", show_viz == "y")
            
        elif choice == '4':
            show_viz = ui.Prompt.ask(
                "Show step-by-step visualization?", 
                choices=["y", "n"], 
                default="y"
            )
            run_sort(current_list, lambda x: x['hp'], "Sorted by HP", show_viz == "y")
            
        elif choice == '5':
            show_viz = ui.Prompt.ask(
                "Show step-by-step visualization?", 
                choices=["y", "n"], 
                default="y"
            )
            run_sort(current_list, get_type_value, "Sorted by Type (Primary)", show_viz == "y")
            
        elif choice == '6':
            show_viz = ui.Prompt.ask(
                "Show step-by-step visualization?", 
                choices=["y", "n"], 
                default="y"
            )
            run_sort(current_list, lambda x: x['name'], "Sorted Alphabetically", show_viz == "y")
            
        elif choice == '0':
            ui.clear_screen()
            ui.display_exit_message()
            break

if __name__ == "__main__":
    main()