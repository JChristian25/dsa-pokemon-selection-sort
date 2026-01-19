"""UI Module - All visual presentation logic using Rich library"""
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box
from rich.text import Text

console = Console()

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    """Display application header"""
    console.print("\n")
    console.print(Panel("POKEMON SELECTION SORT", border_style="blue", box=box.DOUBLE))

def show_menu():
    """Display menu and get user choice"""
    menu_text = """
1. List of Pokemons (Original Order)
2. Sort by Evolution Stage (Ascending)
3. Sort by Generation (Ascending)
4. Sort by HP (Lowest to Highest)
5. Sort by Pokemon Type (Custom Order)
6. Sort Alphabetically (A-Z)
0. Exit
    """
    
    console.print(Panel(menu_text, title="MENU", border_style="blue", box=box.ROUNDED))
    choice = Prompt.ask("Enter your choice", choices=["0", "1", "2", "3", "4", "5", "6"])
    return choice

def display_pokemon_table(data, title="Pokemon List"):
    """Display Pokemon data in a table"""
    table = Table(title=title, box=box.SIMPLE, show_header=True, header_style="bold")
    
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Type")
    table.add_column("HP", justify="center")
    table.add_column("Gen", justify="center")
    table.add_column("Stage")
    
    for p in data:
        table.add_row(
            p['name'],
            p['type'],
            str(p['hp']),
            str(p['gen']),
            p['stage']
        )
    
    console.print(table)

def display_sort_step(data, current_index, min_index, comparing_index=None, operation="", stats=None):
    """Display current state of sorting with highlighting"""
    table = Table(box=box.SIMPLE, show_header=True, header_style="bold")
    
    table.add_column("Index", justify="center", style="dim")
    table.add_column("Name", no_wrap=True)
    table.add_column("Type")
    table.add_column("HP", justify="center")
    table.add_column("Status")
    
    for idx, p in enumerate(data):
        # Determine status
        if idx < current_index:
            status = "[green]✓ Sorted[/green]"
            style = "dim"
        elif idx == current_index:
            status = "[yellow]Current[/yellow]"
            style = "yellow"
        elif idx == min_index:
            status = "[cyan]Min[/cyan]"
            style = "cyan bold"
        elif idx == comparing_index:
            status = "[magenta]Compare[/magenta]"
            style = "magenta"
        else:
            status = "Unsorted"
            style = ""
        
        table.add_row(
            str(idx),
            f"[{style}]{p['name']}[/{style}]" if style else p['name'],
            p['type'],
            str(p['hp']),
            status
        )
    
    console.print(f"\n[bold]{operation}[/bold]")
    
    # Display live statistics if provided
    if stats:
        console.print(f"[dim]Comparisons: {stats['comparisons']} | Swaps: {stats['swaps']}[/dim]")
    
    console.print(table)

def display_swap_message(data, idx1, idx2):
    """Display swap operation"""
    console.print(f"\n[bold]→ Swapping:[/bold] {data[idx1]['name']} ↔ {data[idx2]['name']}\n")

def display_pass_summary(pass_num, total_passes, stats=None):
    """Display pass summary"""
    console.print(f"\n[bold]Pass {pass_num + 1}/{total_passes} completed[/bold]")
    if stats:
        console.print(f"[dim]Running totals - Comparisons: {stats['comparisons']} | Swaps: {stats['swaps']}[/dim]")
    Prompt.ask("\nPress Enter to continue")

def display_completion_message(stats=None):
    """Display sorting completion message"""
    console.print("\n[green bold]✓ Sorting Complete![/green bold]")
    if stats:
        console.print(f"\n[bold cyan]Final Statistics:[/bold cyan]")
        console.print(f"  Total Comparisons: [yellow]{stats['comparisons']}[/yellow]")
        console.print(f"  Total Swaps: [yellow]{stats['swaps']}[/yellow]")
        console.print()

def display_statistics(stats):
    """Display final statistics after sorting"""
    console.print(f"\n[bold cyan]Algorithm Statistics:[/bold cyan]")
    console.print(f"  Total Comparisons: [yellow]{stats['comparisons']}[/yellow]")
    console.print(f"  Total Swaps: [yellow]{stats['swaps']}[/yellow]")
    
    # Display elapsed time if available
    if 'time' in stats:
        elapsed_time = stats['time']
        if elapsed_time < 1:
            time_str = f"{elapsed_time * 1000:.2f} milliseconds"
        else:
            time_str = f"{elapsed_time:.4f} seconds"
        console.print(f"  Time Elapsed: [green]{time_str}[/green]")
    
    console.print()

def display_exit_message():
    """Display exit message"""
    console.print("\n[bold]Thank you for using Pokemon Selection Sort![/bold]\n")

def pause():
    """Pause execution and wait for user input"""
    Prompt.ask("\nPress Enter to continue", default="")

