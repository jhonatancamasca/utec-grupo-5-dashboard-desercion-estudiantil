# 📊 Dashboard de Situación Académica Universitaria

Dashboard interactivo desarrollado con Streamlit para el análisis y visualización de datos relacionados con la deserción estudiantil universitaria.

## 🎯 Descripción

Este dashboard permite explorar y analizar diferentes aspectos de la situación académica de estudiantes universitarios a través de múltiples visualizaciones interactivas, incluyendo perfiles sociodemográficos, académicos y análisis de variables que pueden influir en la deserción estudiantil.

## ✨ Características

El dashboard está organizado en 5 pestañas principales:

### 1. Perfil sociodemográfico del estudiante
- Distribución por estado civil, género y región
- Análisis de estudiantes que viven fuera de su residencia
- Necesidades educativas especiales
- Situación de deuda
- Distribución por edad al ingreso

### 2. Perfil académico de ingreso
- Distribución por rango de notas de ingreso
- Estudiantes por facultad
- Nivel educativo al momento del ingreso
- Modalidad de postulación

### 3. Perfil académico de estudio
- Cursos aprobados en primer y segundo año
- Promedios de notas por año
- Estado de la variable objetivo (Graduado/Desertor/En curso)

### 4. Situación académica por variables demográficas
- Análisis cruzado de situación académica con:
  - Estado civil
  - Género
  - Región
  - Residencia
  - Rango de edad

### 5. Situación académica por variables académicas
- Métricas de desempeño (% graduados, desertores, en curso)
- Análisis por facultad y nivel educativo
- Cursos aprobados por año académico
- Orden de postulación
- Rangos de notas de ingreso

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Streamlit**: Framework principal para la interfaz web
- **Pandas**: Manipulación y análisis de datos
- **Matplotlib**: Visualizaciones estáticas
- **Seaborn**: Visualizaciones estadísticas
- **Plotly**: Gráficos interactivos
- **NumPy**: Operaciones numéricas
- **openpyxl**: Lectura de archivos Excel

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/dashboard-desercion-estudiantil.git
cd dashboard-desercion-estudiantil
```

2. Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
```

3. Activa el entorno virtual:
- **Windows:**
```bash
venv\Scripts\activate
```
- **macOS/Linux:**
```bash
source venv/bin/activate
```

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 📊 Estructura de Datos

El dashboard espera un archivo Excel (`data.xlsx`) con las siguientes columnas:

- `Edad al momento de la inscripcion.`
- `Estado Civil`
- `Genero` (0: Femenino, 1: Masculino)
- `Region`
- `Estudia fuera de su lugar de residencia` (0: No, 1: Sí)
- `Necesidades educativas especiales`
- `Deudor` (0: Sin deuda, 1: Con deuda)
- `Nota de ingreso`
- `Facultad`
- `Nivel_educativo_ingreso`
- `Modalidad  de postulación`
- `Numero_cursos_aprobados_primer_año`
- `Numero_cursos_aprobados_segundo_año`
- `Nota_promedio_primer_año`
- `Nota_promedio_segundo_año`
- `Variable_Objetivo` (Graduado/Desertor/En curso)
- `Orden de postulación`

## 💻 Uso

1. Coloca tu archivo `data.xlsx` en la ruta especificada o actualiza la ruta en el código:
```python
datos = pd.read_excel("ruta/a/tu/data.xlsx", sheet_name="Sheet1")
```

2. Ejecuta la aplicación:
```bash
streamlit run app.py
```

3. El dashboard se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 📱 Navegación

- Utiliza el **sidebar izquierdo** para seleccionar la pestaña de visualización
- Ajusta los **filtros interactivos** según tus necesidades de análisis
- Los gráficos se actualizan automáticamente al cambiar los filtros

## 🎨 Personalización

Puedes personalizar los siguientes aspectos del dashboard:

- **Colores de gráficos**: Modifica los parámetros `color`, `colors` o `palette` en cada gráfico
- **Rangos de análisis**: Ajusta los bins y labels en las secciones de categorización
- **Métricas**: Añade o modifica las métricas calculadas según tus necesidades

## 📝 Estructura del Proyecto

```
dashboard-desercion-estudiantil/
│
├── app.py                  # Archivo principal del dashboard
├── data.xlsx              # Archivo de datos (no incluido en el repositorio)
├── requirements.txt       # Dependencias del proyecto
└── README.md             # Este archivo
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- **UTEC Grupo 5** - Dashboard de Deserción Estudiantil

## 📧 Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio.

## 🙏 Agradecimientos

- A la Universidad de Ingeniería y Tecnología (UTEC)
- A todos los colaboradores del proyecto
- A la comunidad de Streamlit por su excelente framework

---

**Nota**: Asegúrate de no subir archivos con datos sensibles al repositorio. Usa `.gitignore` para excluir archivos de datos.