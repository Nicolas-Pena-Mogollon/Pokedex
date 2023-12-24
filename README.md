# Nombre del Proyecto

Solución prueba técnica HP

## Instalación

Asegúrate de tener Python y pip instalados. Luego, puedes seguir estos pasos:

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tuusuario/tuproyecto.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd tuproyecto
    ```

3. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    ```

4. Activa el entorno virtual:

    - En Windows:

        ```bash
        venv\Scripts\activate
        ```

    - En Linux/Mac:

        ```bash
        source venv/bin/activate
        ```

5. Instala las dependencias:
    - Django
    - requests

## Uso

Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```
La aplicación estará disponible en http://127.0.0.1:8000/.

## Menú:
  - /: Lista de los 50 Pokémon.
  - weight/: Lista de los Pokémon en un rango de peso.
  - grass/: Lista de los Pokémon de tipo grass.
  - flying/: Lista de los Pokémon de tipo y con height mayor a 10.
  - reverse/: Lista de los nombres de los Pokémon junto con su inverso.

## Tecnologías usadas:
  - Django.
  - Python.
  - HTML.
  - CSS.
  - Graphql (Uso de la API Beta de PokeAPI), usando esta API se mejoró el rendimiento de as solicitudes, así como el procesamiento y filtrado de los datos.

## Posibles mejoras:
  - Uso de la API PokeAPI sprites para poder hacer uso de las imágenes de cada Pokémon.
  - Carga progresiva de la información hacia las tablas, para no almacenar todo en memoria.
