import os
import importlib

def run_all_demos(demos_folder="demos"):
    # List all .py files in demos folder
    demo_files = [f for f in os.listdir(demos_folder) if f.endswith(".py")]

    for demo in demo_files:
        module_name = f"{demos_folder}.{demo[:-3]}"  # strip .py
        try:
            module = importlib.import_module(module_name)
            print(f"\n=== Running {demo} ===")
            # If module has a main() or run_demo(), call it
            if hasattr(module, "main"):
                module.main()
            elif hasattr(module, "run_demo"):
                module.run_demo()
            else:
                print(f"No entry point found in {demo}")
        except Exception as e:
            print(f"Error running {demo}: {e}")

if __name__ == "__main__":
    print("Launching HeatFlowClean cockpit...")
    run_all_demos()