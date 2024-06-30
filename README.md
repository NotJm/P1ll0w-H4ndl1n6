# p1ll0w h4ndl1n6

## Descripción

**p1ll0w h4ndl1n6** es una herramienta de manipulación de imágenes que permite convertir imágenes de una extensión a otra. Este proyecto está en sus primeras etapas de desarrollo y actualmente soporta la conversión básica entre diferentes formatos de imagen.

## Características

- Conversión de imágenes entre diferentes extensiones/formatos.
- Soporte para formatos de imagen populares como JPEG, PNG, BMP, y GIF.

## Uso

### Ejemplos de Uso

#### Convertir una imagen de JPEG a PNG

```python
from p1ll0w_h4ndl1n6 import convert_image

# Convertir una imagen de JPEG a PNG
convert_image('ruta/a/imagen.jpeg', 'ruta/a/imagen.png')
```

#### Convertir una imagen de BMP a GIF

```python
from p1ll0w_h4ndl1n6 import convert_image

# Convertir una imagen de BMP a GIF
convert_image('ruta/a/imagen.bmp', 'ruta/a/imagen.gif')
```

### Características Futuras

Estamos trabajando en añadir las siguientes funcionalidades:

- Redimensionamiento de imágenes
- Aplicación de filtros y efectos
- Soporte para metadatos EXIF
- Compresión y optimización de imágenes

## Instalación

Para instalar **p1ll0w h4ndl1n6**, sigue estos pasos:

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu-usuario/p1ll0w_h4ndl1n6.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd p1ll0w_h4ndl1n6
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva funcionalidad o corrección de errores: `git checkout -b mi-nueva-funcionalidad`.
3. Realiza tus cambios y haz commit: `git commit -m 'Añadir nueva funcionalidad'`.
4. Envía tus cambios al repositorio remoto: `git push origin mi-nueva-funcionalidad`.
5. Crea un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).
