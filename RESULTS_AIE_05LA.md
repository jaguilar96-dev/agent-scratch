# Resultados Sesion 05:

## Caso golden SET
  Resumen de 1 casos (juez local):
    recall@5: 1.00   intención: 1.00   fuentes: 1.00   hechos: 1.00
    apoyo: 5.0/5   relevancia: 5.0/5   cita correcta: 1.0
    fugas de datos personales: 0   citas de fuentes prohibidas: 0
    tokens: 1002 de entrada, 382 de salida

### chunks más chicos
Resumen de 31 casos (juez local):
  recall@8: 1.00   intención: 1.00   fuentes: 1.00   hechos: 0.89
  apoyo: 5.0/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 0
  tokens: 39884 de entrada, 16845 de salida
Detalle de cada caso: C:\Proyectos Personales\capacitacion\agent-scratch\data\eval\fraud-20261118-222016.json

### menos fragmentos
Resumen de 31 casos (juez local):
  recall@3: 1.00   intención: 1.00   fuentes: 1.00   hechos: 0.93
  apoyo: 4.9/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 0
  tokens: 26206 de entrada, 14802 de salida
Detalle de cada caso: C:\Proyectos Personales\capacitacion\agent-scratch\data\eval\fraud-20261118-222811.json

### más fragmentos
Resumen de 31 casos (juez local):
  recall@8: 1.00   intención: 1.00   fuentes: 1.00   hechos: 0.93
  apoyo: 4.9/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 0
  tokens: 39984 de entrada, 17786 de salida
Detalle de cada caso: C:\Proyectos Personales\capacitacion\agent-scratch\data\eval\fraud-20261118-200731.json

### base local, sin reranker
Resumen de 31 casos (juez local):
  recall@8: 1.00   intención: 1.00   fuentes: 1.00   hechos: 0.89
  apoyo: 5.0/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 0
  tokens: 37825 de entrada, 16135 de salida
Detalle de cada caso: C:\Proyectos Personales\capacitacion\agent-scratch\data\eval\fraud-20261118-231732.json

### Juez azure
Resumen de 31 casos (juez azure_evaluation):
  recall@5: 1.00   intención: 1.00   fuentes: 1.00   hechos: 0.93
  apoyo: 5.0/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 0
  tokens: 31677 de entrada, 16239 de salida
Detalle de cada caso: C:\Proyectos Personales\capacitacion\agent-scratch\data\eval\fraud-20261118-232338.json

### Juez Local
Resumen de 31 casos (juez local):
  recall@5: 1.00   intención: 1.00   fuentes: 1.00   hechos: 0.89
  apoyo: 5.0/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 0
  tokens: 31745 de entrada, 17052 de salida
Detalle de cada caso: C:\Proyectos Personales\capacitacion\agent-scratch\data\eval\fraud-20261118-233229.json

¿Las notas de apoyo y de cita correcta van en la misma dirección?

**Sí, van fuertemente alineadas y en la misma dirección positiva:**
- En todas las corridas completas de 31 casos, el **apoyo** se sitúa consistentemente entre **4.9 y 5.0 / 5** (prácticamente perfecto), y la **cita correcta** alcanza **1.0** (o ~0.97 - 1.0 en escala continua).
- Esto demuestra que cuando el agente basa sus respuestas en los fragmentos recuperados del corpus (alto apoyo), las fuentes citadas (`claims-regulation.pdf`, `card-replacement.docx`, `response-times.csv`, etc.) respaldan con exactitud las afirmaciones realizadas.
- Además, tras la corrección en las reglas de intención (`out_of_scope`), las **citas de fuentes prohibidas se mantuvieron en 0**, garantizando que el agente no cita fuentes indebidas (como la cafetería).

---

¿Cuánto tardó cada corrida?

Extrayendo la latencia acumulada exacta de cada archivo de evaluación (`data/eval/`):

1. **`chunks más chicos`** (`fraud-20261118-222016.json`):
   - **Tiempo total:** **183.43 s** (~3 min 03 s).
   - **Promedio por caso:** **5,917 ms** (~5.92 s).
   - Tokens: 39,884 entrada / 16,845 salida.

2. **`menos fragmentos (top_k=3)`** (`fraud-20261118-222811.json`):
   - **Tiempo total:** **162.29 s** (~2 min 42 s).
   - **Promedio por caso:** **5,235 ms** (~5.24 s).
   - Tokens: 26,206 entrada / 14,802 salida. *(Es la configuración más rápida y eficiente en tokens de entrada al reducir el contexto a 3 fragmentos)*.

3. **`más fragmentos (top_k=8)`** (`fraud-20261118-200731.json`):
   - **Tiempo total:** **185.07 s** (~3 min 05 s).
   - **Promedio por caso:** **5,970 ms** (~5.97 s).
   - Tokens: 39,984 entrada / 17,786 salida. *(La de mayor tiempo y consumo de tokens debido a la sobrecarga de 8 fragmentos)*.

4. **`base local, sin reranker`** (`fraud-20261118-231732.json`):
   - **Tiempo total:** **166.88 s** (~2 min 47 s).
   - **Promedio por caso:** **5,383 ms** (~5.38 s).
   - Tokens: 37,825 entrada / 16,135 salida.

5. **`Juez azure (decision-1)`** (`fraud-20261118-232338.json`):
   - **Tiempo total:** **157.77 s** (~2 min 38 s).
   - **Promedio por caso:** **5,089 ms** (~5.09 s).
   - Tokens: 31,677 entrada / 16,239 salida.

6. **`Juez Local (G-Eval / gpt-5-mini)`** (`fraud-20261118-233229.json`):
   - **Tiempo total:** **178.25 s** (~2 min 58 s).
   - **Promedio por caso:** **5,750 ms** (~5.75 s).
   - Tokens: 31,745 entrada / 17,052 salida.

---

Para los casos donde no coinciden, abre el detalle de G-Eval: su reasoning explica qué vio.

Al contrastar la evaluación de **Azure (`decision-1`)** frente a **Local (`G-Eval`)**:

1. **Diferencia de estilo de puntuación:**
   - **Azure (`decision-1`):** Calcula probabilidades continuas ponderadas por nivel (por ejemplo, notas como `apoyo: 4.87`, `cita_correcta: 0.71`), mostrando mayor sensibilidad numérica a matices o incertidumbres.
   - **G-Eval (Juez Local):** Aplica un razonamiento cualitativo previo (`reasoning`) paso a paso y asigna puntajes enteros de 1 a 5 (mapeados a escala 5.0 y 1.0).

2. **Casos clave donde difieren y qué vio G-Eval:**
   - **`fraud-04` (Ampliación de plazo de respuesta):**
     - *Azure:* Asignó `cita_correcta: 0.71` (detectó dudas sobre si todos los detalles de suspensión y plazos estaban completamente respaldados).
     - *Reasoning de G-Eval:* Explica que la respuesta no inventó nada y recogió todas las reglas explícitas del corpus:
       > *"La respuesta recoge las reglas exactas de los fragmentos: plazos máximos (15 días, 10 días para operaciones no reconocidas), ampliación única de 15 días cuando se requiere información de terceros, excepción para cobro duplicado del banco y suspensión por falta de información hasta 5 días. Las fuentes citadas (claims-regulation.pdf y response-times.csv) contienen esas afirmaciones, por lo que está bien fundamentada y responde directamente la pregunta."* (Calificó apoyo 5.0 y cita 1.0).
   - **`fraud-20` (Documentos requeridos para contracargo):**
     - *Azure:* Asignó un apoyo de `4.69`.
     - *Reasoning de G-Eval:* Justifica por qué el desglose por tipo de motivo es correcto mapeando cada afirmación al fragmento correspondiente:
       > *"La respuesta enumera los campos de titular y la documentación requerida, y cada afirmación está presente en los fragmentos: los datos del titular aparecen en [4], la carta de desconocimiento y requisitos por motivo están en [5], y la evidencia de contacto para producto no recibido/suscripción en [2]. No se detectan afirmaciones inventadas ni contradicciones."* (Calificó 5.0).
   - **`fraud-16` (Información mínima para presentar reclamo):**
     - En la corrida local, el agente respondió *"número de documento"* en vez de la frase literal *"documento de identidad"*, lo que bajó `hechos` a `0.89` (por chequeo de subcadena exacta), pero **G-Eval comprendió el significado y le otorgó 5.0**:
       > *"La respuesta enumera exactamente los cuatro elementos que el Reglamento indica como información mínima... Todas las afirmaciones aparecen en el fragmento [1] y la fuente citada (claims-regulation.pdf) contiene esa información."*
