from db import Database

db = Database()

# Create a sample run
run_id = db.execute(
    """
    INSERT INTO evolution_runs (description, population_size, mutation_rate, crossover_rate)
    VALUES (?, ?, ?, ?)
    """,
    ("Sample Evolution Run", 20, 0.1, 0.7)
)

# Create generations
for gen in range(5):
    gen_id = db.execute(
        """
        INSERT INTO evolution_generations (run_id, generation_index, best_fitness)
        VALUES (?, ?, ?)
        """,
        (run_id, gen, 0.5 + gen * 0.1)
    )

    # Create agents
    for agent in range(10):
        db.execute(
            """
            INSERT INTO evolution_agents (generation_id, genome, fitness)
            VALUES (?, ?, ?)
            """,
            (gen_id, f'{{"weights": [{agent}, {gen}]}}', agent * 0.1)
        )

print("Seed complete. Run ID:", run_id)
