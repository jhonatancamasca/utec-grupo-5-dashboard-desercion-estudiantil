import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Dashboard pestañas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Dashboard Situación académica universitaria")

# Cargar datos
datos = pd.read_excel(
    r"C:\Users\jcama\Desktop\proyecto\utec-grupo-5-dashboard-desercion-estudiantil\data.xlsx",
    sheet_name="Sheet1",
)

# SIDEBAR - Pestañas
st.sidebar.header("📑 Navegación")
char_type = st.sidebar.selectbox(
    "Selecciona el tipo de visualización",
    [
        "Perfil sociodemográfico del estudiante",
        "Perfil académico de ingreso",
        "Perfil académico de estudio",
        "Situación académica por variables demográficas",
        "Situación académica por variables académicas",
    ],
)

st.sidebar.markdown("---")

# ====== PESTAÑA 1: PERFIL SOCIODEMOGRÁFICO ======
if char_type == "Perfil sociodemográfico del estudiante":
    st.sidebar.markdown("### 🔍 Filtros")

    year_choice = st.sidebar.slider(
        "Edad al momento de inscripción",
        min_value=int(datos["Edad al momento de la inscripcion."].min()),
        max_value=int(datos["Edad al momento de la inscripcion."].max()),
        step=1,
        value=int(datos["Edad al momento de la inscripcion."].min()),
    )

    datos_filtrados = datos[datos["Edad al momento de la inscripcion."] == year_choice]

    st.metric("Estudiantes filtrados", len(datos_filtrados))

    # Fila 1: 3 gráficos
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Estudiantes por estado civil**")
        cant = datos_filtrados["Estado Civil"].value_counts()
        fig = go.Figure([go.Pie(values=cant.values, labels=cant.index, hole=0.3)])
        fig.update_layout(
            height=280, margin=dict(t=20, b=20, l=20, r=20), showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("**Estudiantes por género**")
        cant = (
            datos_filtrados["Genero"]
            .value_counts()
            .rename({0: "Femenino", 1: "Masculino"})
        )
        fig, ax = plt.subplots(figsize=(4, 2.8))
        cant.plot(kind="bar", ax=ax, color="skyblue")
        ax.set_xlabel("Género", fontsize=8)
        ax.set_ylabel("Cantidad", fontsize=8)
        ax.tick_params(labelsize=7)
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=7)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col3:
        st.markdown("**Estudiantes por región**")
        fig, ax = plt.subplots(figsize=(4, 2.8))
        sns.countplot(data=datos_filtrados, x="Region", color="royalblue", ax=ax)
        ax.set_xlabel("Región", fontsize=8)
        ax.set_ylabel("Cantidad", fontsize=8)
        ax.tick_params(labelsize=7)
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=7)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    # Fila 2: 4 gráficos
    col4, col5, col6, col7 = st.columns(4)

    with col4:
        st.markdown("**Estudian fuera de residencia**")
        cant = (
            datos_filtrados["Estudia fuera de su lugar de residencia"]
            .value_counts()
            .rename({0: "No", 1: "Si"})
        )
        fig, ax = plt.subplots(figsize=(3, 2.5))
        ax.pie(
            cant.values,
            labels=cant.index,
            autopct="%1.1f%%",
            startangle=45,
            colors=["gold", "royalblue"],
            textprops={"fontsize": 7},
        )
        st.pyplot(fig)
        plt.close()

    with col5:
        st.markdown("**Necesidades especiales**")
        cant = datos_filtrados["Necesidades educativas especiales"].value_counts()
        fig, ax = plt.subplots(figsize=(3, 2.5))
        cant.plot(kind="barh", ax=ax, color="lightgreen")
        ax.set_xlabel("Cantidad", fontsize=7)
        ax.tick_params(labelsize=6)
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=6)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col6:
        st.markdown("**Estudiantes con deuda**")
        etiquetas = datos_filtrados["Deudor"].map({0: "Sin deuda", 1: "Con deuda"})
        conteo = etiquetas.value_counts()
        fig, ax = plt.subplots(figsize=(3, 2.5))
        ax.pie(
            conteo,
            labels=conteo.index,
            autopct="%1.1f%%",
            colors=["gold", "red"],
            textprops={"fontsize": 7},
        )
        st.pyplot(fig)
        plt.close()

    with col7:
        st.markdown("**Edad al ingreso**")
        fig, ax = plt.subplots(figsize=(3, 2.5))
        sns.countplot(
            data=datos_filtrados,
            x="Edad al momento de la inscripcion.",
            color="green",
            ax=ax,
        )
        ax.set_xlabel("Edad", fontsize=7)
        ax.set_ylabel("Cantidad", fontsize=7)
        ax.tick_params(labelsize=6, rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

# ====== PESTAÑA 2: PERFIL ACADÉMICO DE INGRESO ======
elif char_type == "Perfil académico de ingreso":
    st.sidebar.markdown("### 🔍 Filtros")

    nota_ing = st.sidebar.slider(
        "Nota de ingreso",
        min_value=float(datos["Nota de ingreso"].min()),
        max_value=float(datos["Nota de ingreso"].max()),
        step=0.1,
        value=float(datos["Nota de ingreso"].min()),
    )

    datos_filtrados = datos[datos["Nota de ingreso"] == nota_ing]
    st.metric("Estudiantes según nota filtrada", len(datos_filtrados))

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Distribución por rango de notas**")
        bins = [9.5, 11, 13, 15, 17, 19]
        labels = ["9.5-11", "11.1-13", "13.1-15", "15.1-17", "17.1-19"]
        rango_notas = pd.cut(
            datos_filtrados["Nota de ingreso"],
            bins=bins,
            labels=labels,
            include_lowest=True,
        )
        df_rangos = (
            pd.DataFrame({"RANGO_NOTA": rango_notas})
            .groupby("RANGO_NOTA", observed=False)
            .size()
            .reset_index(name="CANTIDAD")
        )

        fig, ax = plt.subplots(figsize=(6, 3.5))
        sns.barplot(
            data=df_rangos, x="RANGO_NOTA", y="CANTIDAD", color="skyblue", ax=ax
        )
        ax.set_xlabel("Rango de notas", fontsize=9)
        ax.set_ylabel("Cantidad", fontsize=9)
        ax.tick_params(labelsize=8)
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=8)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

        st.markdown("**Estudiantes por facultad**")
        cant = datos_filtrados["Facultad"].value_counts()
        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.bar(cant.index, cant.values, edgecolor="black")
        ax.set_xlabel("Facultad", fontsize=9)
        ax.set_ylabel("Cantidad", fontsize=9)
        ax.tick_params(labelsize=7, rotation=90)
        for p in ax.patches:
            ax.annotate(
                f"{int(p.get_height())}",
                (p.get_x() + p.get_width() / 2, p.get_height()),
                ha="center",
                va="bottom",
                fontsize=7,
            )
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        st.markdown("**Nivel educativo al ingreso**")
        cant = datos_filtrados["Nivel_educativo_ingreso"].value_counts()
        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.barh(cant.index, cant.values)
        ax.set_xlabel("Cantidad", fontsize=9)
        ax.set_ylabel("Nivel educativo", fontsize=9)
        ax.tick_params(labelsize=7)
        for i, valor in enumerate(cant.values):
            ax.text(valor + 0.5, i, str(int(valor)), va="center", ha="left", fontsize=8)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

        st.markdown("**Modalidad de postulación**")
        cant = datos_filtrados["Modalidad  de postulación"].value_counts()
        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.pie(
            cant,
            labels=cant.index,
            autopct="%1.1f%%",
            startangle=90,
            textprops={"fontsize": 8},
        )
        ax.legend(loc="upper right", fontsize=7)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

# ====== PESTAÑA 3: PERFIL ACADÉMICO DE ESTUDIO ======
elif char_type == "Perfil académico de estudio":
    st.sidebar.markdown("### 🔍 Filtros")

    year_choice = st.sidebar.slider(
        "Número de cursos aprobados (1er año)",
        min_value=int(datos["Numero_cursos_aprobados_primer_año"].min()),
        max_value=int(datos["Numero_cursos_aprobados_primer_año"].max()),
        step=1,
        value=int(datos["Numero_cursos_aprobados_primer_año"].mean()),
    )

    datos_filtrados = datos[datos["Numero_cursos_aprobados_primer_año"] == year_choice]

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown("**Cursos 1er año**")
        fig, ax = plt.subplots(figsize=(2.5, 2.8))
        sns.countplot(
            data=datos_filtrados, x="Numero_cursos_aprobados_primer_año", ax=ax
        )
        ax.set_xlabel("Cursos", fontsize=7)
        ax.set_ylabel("Estudiantes", fontsize=7)
        ax.tick_params(labelsize=6)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        st.markdown("**Cursos 2do año**")
        fig, ax = plt.subplots(figsize=(2.5, 2.8))
        sns.countplot(
            data=datos_filtrados, x="Numero_cursos_aprobados_segundo_año", ax=ax
        )
        ax.set_xlabel("Cursos", fontsize=7)
        ax.set_ylabel("Estudiantes", fontsize=7)
        ax.tick_params(labelsize=6)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col3:
        st.markdown("**Notas 1er año**")
        bins = [0, 5, 10, 15, 20]
        labels = ["0-5", "5-10", "10-15", "15-20"]
        cant = pd.cut(
            datos_filtrados["Nota_promedio_primer_año"],
            bins=bins,
            labels=labels,
            right=False,
        ).value_counts(sort=False)
        fig, ax = plt.subplots(figsize=(2.5, 2.8))
        sns.barplot(x=cant.index, y=cant.values, ax=ax)
        ax.set_xlabel("Rango", fontsize=7)
        ax.set_ylabel("Cantidad", fontsize=7)
        ax.tick_params(labelsize=6)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col4:
        st.markdown("**Notas 2do año**")
        cant = pd.cut(
            datos_filtrados["Nota_promedio_segundo_año"],
            bins=bins,
            labels=labels,
            right=False,
        ).value_counts(sort=False)
        fig, ax = plt.subplots(figsize=(2.5, 2.8))
        sns.barplot(x=cant.index, y=cant.values, ax=ax)
        ax.set_xlabel("Rango", fontsize=7)
        ax.set_ylabel("Cantidad", fontsize=7)
        ax.tick_params(labelsize=6)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col5:
        st.markdown("**Variable objetivo**")
        fig, ax = plt.subplots(figsize=(2.5, 2.8))
        sns.countplot(
            data=datos_filtrados, x="Variable_Objetivo", palette="viridis", ax=ax
        )
        ax.set_xlabel("Situación", fontsize=7)
        ax.set_ylabel("Cantidad", fontsize=7)
        ax.tick_params(labelsize=5, rotation=45)
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=6)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

# ====== PESTAÑA 4: SITUACIÓN ACADÉMICA POR VARIABLES DEMOGRÁFICAS ======
elif char_type == "Situación académica por variables demográficas":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Situación por Estado civil**")
        df_pivot = datos.groupby(["Variable_Objetivo", "Estado Civil"]).size().unstack()
        df_long = df_pivot.reset_index().melt(
            id_vars="Variable_Objetivo", var_name="Estado Civil", value_name="Cantidad"
        )
        fig = px.bar(
            df_long,
            x="Estado Civil",
            y="Cantidad",
            color="Variable_Objetivo",
            barmode="group",
            text="Cantidad",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            height=300,
        )
        fig.update_traces(textposition="outside")
        fig.update_layout(margin=dict(t=20, b=20, l=20, r=20), font=dict(size=9))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("**Situación por Género**")
        df_pivot = (
            datos.groupby(["Variable_Objetivo", "Genero"])
            .size()
            .unstack()
            .rename(columns={0: "Femenino", 1: "Masculino"})
        )
        fig, ax = plt.subplots(figsize=(4, 3))
        df_pivot.plot(
            kind="bar", ax=ax, stacked=True, color=["darkorchid", "royalblue"]
        )
        ax.set_xlabel("Situación académica", fontsize=8)
        ax.set_ylabel("Cantidad", fontsize=8)
        ax.tick_params(labelsize=7)
        ax.legend(fontsize=7)
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=6)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col3:
        st.markdown("**Situación por Región**")
        df_pivot = datos.groupby(["Variable_Objetivo", "Region"]).size().unstack()
        fig, ax = plt.subplots(figsize=(4, 3))
        df_pivot.plot(kind="bar", ax=ax, color=["gold", "green", "royalblue"])
        ax.set_xlabel("Situación académica", fontsize=8)
        ax.set_ylabel("Cantidad", fontsize=8)
        ax.tick_params(labelsize=7)
        ax.legend(fontsize=7)
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=6)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("**Estudian fuera de residencia**")
        df_pivot = (
            datos.groupby(
                ["Variable_Objetivo", "Estudia fuera de su lugar de residencia"]
            )
            .size()
            .unstack()
            .rename(columns={0: "No", 1: "Si"})
        )
        fig, ax = plt.subplots(figsize=(4, 3))
        df_pivot.plot(kind="bar", ax=ax, color=["orangered", "lightseagreen"])
        ax.set_xlabel("Situación académica", fontsize=8)
        ax.set_ylabel("Cantidad", fontsize=8)
        ax.tick_params(labelsize=7)
        ax.legend(fontsize=7)
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=6)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col5:
        st.markdown("**Por rango de edad**")
        bins = [17, 20, 24, 28, 32, 36, 40]
        labels = ["17-20", "21-24", "25-28", "29-32", "33-36", "36-40"]
        rango_edades = pd.cut(
            datos["Edad al momento de la inscripcion."],
            bins=bins,
            labels=labels,
            include_lowest=True,
        )
        df_temp = pd.DataFrame(
            {
                "RANGO_EDAD": rango_edades,
                "Variable_Objetivo": datos["Variable_Objetivo"],
            }
        )
        df_rangos = (
            df_temp.groupby(["RANGO_EDAD", "Variable_Objetivo"], observed=True)
            .size()
            .reset_index(name="CANTIDAD")
        )

        fig, ax = plt.subplots(figsize=(4, 3))
        sns.lineplot(
            data=df_rangos,
            x="RANGO_EDAD",
            y="CANTIDAD",
            hue="Variable_Objetivo",
            marker="o",
            palette="Set2",
            ax=ax,
        )
        ax.set_xlabel("Rango de edad", fontsize=8)
        ax.set_ylabel("Cantidad", fontsize=8)
        ax.tick_params(labelsize=6, rotation=45)
        ax.legend(fontsize=6)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

# ====== PESTAÑA 5: SITUACIÓN ACADÉMICA POR VARIABLES ACADÉMICAS ======
elif char_type == "Situación académica por variables académicas":
    st.sidebar.markdown("### 🔍 Filtros")

    nota_ing = st.sidebar.slider(
        "Nota de ingreso",
        min_value=float(datos["Nota de ingreso"].min()),
        max_value=float(datos["Nota de ingreso"].max()),
        step=0.1,
        value=float(datos["Nota de ingreso"].min()),
    )

    datos_filtrados = datos[datos["Nota de ingreso"] == nota_ing]

    # Métricas
    colA, colB, colC, colD = st.columns(4)
    total = len(datos_filtrados)
    pct_grad = datos_filtrados["Variable_Objetivo"].eq("Graduado").mean() * 100
    pct_des = datos_filtrados["Variable_Objetivo"].eq("Desertor").mean() * 100
    pct_enc = datos_filtrados["Variable_Objetivo"].eq("En curso").mean() * 100

    with colA:
        st.metric("Total estudiantes", f"{total:,}")
    with colB:
        st.metric("% Graduados", f"{pct_grad:.1f}%")
    with colC:
        st.metric("% Desertores", f"{pct_des:.1f}%")
    with colD:
        st.metric("% En curso", f"{pct_enc:.1f}%")

    # Fila 1: 3 gráficos compactos
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("**Cantidad por Variable Objetivo**")
        conteos = datos_filtrados["Variable_Objetivo"].value_counts()
        fig = go.Figure(
            [
                go.Bar(
                    x=conteos.index,
                    y=conteos.values,
                    text=conteos.values,
                    textposition="outside",
                    marker_color=["#80b1d3", "#fb8072", "#b3de69"],
                )
            ]
        )
        fig.update_layout(
            height=220, margin=dict(t=10, b=10, l=10, r=10), font=dict(size=9)
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.markdown("**Situación por Facultad**")
        df_pivot = (
            datos_filtrados.groupby(["Facultad", "Variable_Objetivo"]).size().unstack()
        )
        fig, ax = plt.subplots(figsize=(3.5, 2.2))
        df_pivot.plot(kind="bar", ax=ax, width=0.7)
        ax.set_xlabel("Facultad", fontsize=7)
        ax.set_ylabel("Cantidad", fontsize=7)
        ax.tick_params(labelsize=5, rotation=90)
        ax.legend(fontsize=5, loc="upper right")
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=5)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with c3:
        st.markdown("**Nivel educativo de ingreso**")
        fig, ax = plt.subplots(figsize=(3.5, 2.2))
        sns.countplot(
            data=datos_filtrados,
            x="Nivel_educativo_ingreso",
            hue="Variable_Objetivo",
            ax=ax,
        )
        ax.set_xlabel("Nivel educativo", fontsize=7)
        ax.set_ylabel("Cantidad", fontsize=7)
        ax.tick_params(labelsize=5, rotation=90)
        ax.legend(fontsize=5, loc="upper right")
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=5)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    # Fila 2: 3 gráficos compactos
    c4, c5, c6 = st.columns(3)

    with c4:
        st.markdown("**Cursos aprobados (1er año)**")
        fig, ax = plt.subplots(figsize=(3.5, 2.2))
        sns.countplot(
            data=datos_filtrados,
            x="Numero_cursos_aprobados_primer_año",
            hue="Variable_Objetivo",
            ax=ax,
        )
        ax.set_xlabel("Cursos", fontsize=7)
        ax.set_ylabel("Cantidad", fontsize=7)
        ax.tick_params(labelsize=6)
        ax.legend(fontsize=5, loc="upper right")
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=5)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with c5:
        st.markdown("**Cursos aprobados (2do año)**")
        fig, ax = plt.subplots(figsize=(3.5, 2.2))
        sns.countplot(
            data=datos_filtrados,
            x="Numero_cursos_aprobados_segundo_año",
            hue="Variable_Objetivo",
            ax=ax,
        )
        ax.set_xlabel("Cursos", fontsize=7)
        ax.set_ylabel("Cantidad", fontsize=7)
        ax.tick_params(labelsize=6)
        ax.legend(fontsize=5, loc="upper right")
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=5)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with c6:
        st.markdown("**Orden de postulación**")
        df_pivot = (
            datos_filtrados.groupby(["Variable_Objetivo", "Orden de postulación"])
            .size()
            .unstack()
        )
        fig, ax = plt.subplots(figsize=(3.5, 2.2))
        df_pivot.plot(kind="barh", ax=ax)
        ax.set_xlabel("Cantidad", fontsize=7)
        ax.set_ylabel("Situación", fontsize=7)
        ax.tick_params(labelsize=6)
        ax.legend(fontsize=5, loc="lower right")
        for bar in ax.containers:
            ax.bar_label(bar, fmt="%.0f", fontsize=5)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    # Última fila: 1 gráfico ancho
    st.markdown("**Situación por Rango de nota al ingreso**")
    bins = [0, 5, 10, 15, 20]
    labels = ["0-5", "5-10", "10-15", "15-20"]
    datos_filtrados["Nota_de_ingreso_rango"] = pd.cut(
        datos_filtrados["Nota de ingreso"], bins=bins, labels=labels, right=False
    )
    df_pivot = (
        datos_filtrados.groupby(["Nota_de_ingreso_rango", "Variable_Objetivo"])
        .size()
        .unstack()
    )

    fig, ax = plt.subplots(figsize=(11, 2.5))
    df_pivot.plot(kind="bar", ax=ax)
    ax.set_xlabel("Rango de notas", fontsize=9)
    ax.set_ylabel("Cantidad", fontsize=9)
    ax.tick_params(labelsize=8)
    ax.legend(fontsize=8, loc="upper right")
    for bar in ax.containers:
        ax.bar_label(bar, fmt="%.0f", fontsize=7)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
