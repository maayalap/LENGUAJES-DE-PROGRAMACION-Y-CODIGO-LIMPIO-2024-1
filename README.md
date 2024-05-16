## LENGUAJES DE PROGRAMACIÓN Y CÓDIGO LIMPIO 2024-1

### POR:
Rostin Santiago Alzate Montoya y
Miguel Ayala Parra

# Calculadora de Hipoteca Inversa

## Descripción
Esta aplicación web calcula la hipoteca inversa en tres modalidades diferentes: Temporal, Vitalicia y Única.

## Estructura de Carpetas
El proyecto está estructurado de la siguiente manera:

- Carpeta `controller`: Contiene los controladores de Flask para manejar las rutas de la aplicación.
    - `controller_user.py`: Controlador para la autenticación de usuarios.
    - `controller_mortgages.py`: Controlador para el cálculo de hipotecas inversas.
- Carpeta `logic`: Contiene la lógica de negocio de la aplicación.
    - `Calculations.py`: Funciones para calcular la hipoteca inversa en diferentes modalidades.
- Carpeta `model`: Contiene los modelos de datos de la aplicación.
    - `database_manager.py`: Gestor de la base de datos.
    - `model_user.py`: Modelo de usuario.
- Carpeta `static`: Contiene archivos estáticos como CSS, fuentes y scripts.
    - Carpeta `content`: Contiene archivos CSS para estilos de la interfaz.
    - Carpeta `fonts`: Contiene archivos de fuentes para estilos de la interfaz.
    - Carpeta `scripts`: Contiene archivos javascript para funcionamientos de la interfaz.

- Carpeta `view`: Contiene las plantillas HTML para las vistas de la aplicación.
    - `index.html`: Página de inicio.
    - `index_login.html`: Página de inicio con sesión iniciada.
    - `layout.html`: Página de el layout cuando se a iniciaso sesion.
    - `layout_login.html`: Página de el layoutu cuando se a inicado sesion.
    - `lifetime.html`: Página de hipoteca inversa vitalicia.
    - `login.html`: Página de inicio de sesion.
    - `register.html`: Página de registro.
    - `temporary.html`: Página de hipoteca inversa temporal.
    - `unique.html`: Página de hipoteca inversa unica.
    - `result.html`: Página de muestra de consultas.
- Archivo `app.py`: Archivo de ejecucion principal.
- Archivo `requeriments.py`: Dependencias para el funcionamiento de la aplicacion.
- Archivo `routes.py`: Define las rutas de las url de la aplicacion.
- Archivo `secret.cfg`: Contiene los datos de la conexion a la base de datos
## Cómo Ejecutar la Aplicación
1. Asegúrate de tener Python instalado en tu sistema.
2. Instala las dependencias del proyecto. Puedes hacerlo ejecutando `pip install -r requirements.txt`.
3. Configura las variables de entorno en un archivo `.env` o directamente en el archivo `app.py`.
4. Abre una terminal y navega hasta la carpeta raíz del proyecto.
5. Ejecuta el archivo `app.py` con el siguiente comando:
    ```
    python app.py
    ```
6. Abre un navegador web y ve a la dirección `http://localhost:5555/index` para acceder a la aplicación.

Con estos pasos, podrás ejecutar y probar la funcionalidad de la aplicación Flask para calcular hipotecas inversas.

Recuerda que debes tener una base de datos configurada correctamente para el funcionamiento de la aplicación y dtener acceso a internet. Para que uses tu base de datos debes cambiar los datos en el archivo secret.cfg y poner los de tu conexion
