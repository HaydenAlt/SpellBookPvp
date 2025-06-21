import os

script_dir = os.path.dirname(os.path.abspath(__file__))
for filename in os.listdir(script_dir):
    if filename.endswith('.mcfunction'):
        with open(os.path.join(script_dir, filename), 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.startswith("particle minecraft:"):
                    line = line[len("particle minecraft:"):].strip()
                    parts = line.split()
                    if len(parts) >= 6:
                        a, b, c, d, e, f = parts[0], *parts[1:5], ' '.join(parts[5:])
                        line = f"particle {a}{{color:[{b},{c},{d}],scale:{e}}} {f}\n"
                file.write(line)
            file.truncate()