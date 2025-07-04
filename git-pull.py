import subprocess

repositorio = "https://github.com/MoreFerreyraDiaz/EscuelaOficios.git"

comando = ["git", "pull"]

try:
    subprocess.run(["cd", repositorio], shell=True, check=True)

    resultado = subprocess.run(comando, cwd=repositorio, check=True, text=True, capture_output=True)

    print("Resultado de git pull:\n")
    print(resultado.stdout)

except subprocess.CalledProcessError as e:
    print("Ocurrió un error al ejecutar git pull:")
    print(e.stderr)
